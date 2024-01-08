import os
import unittest
import time
import _thread

from http.server import BaseHTTPRequestHandler, HTTPServer
from py_localtunnel.tunnel import Tunnel
from twilio.request_validator import RequestValidator
from twilio.rest import Client


class RequestHandler(BaseHTTPRequestHandler):
    is_request_valid = False
    validator = RequestValidator(os.environ["TWILIO_AUTH_TOKEN"])

    def do_GET(self):
        self.process_request()

    def do_POST(self):
        self.process_request()

    def process_request(self):
        self.signature_header = self.headers.get("x-twilio-signature")
        self.url = (
            self.headers.get("x-forwarded-proto")
            + "://"
            + self.headers.get("host")
            + self.path
        )
        self.send_response(200)
        self.end_headers()
        RequestHandler.is_request_valid = RequestHandler.validator.validate(
            uri=self.url, params=None, signature=self.signature_header
        )


class WebhookTest(unittest.TestCase):
    def setUp(self):
        api_key = os.environ["TWILIO_API_KEY"]
        api_secret = os.environ["TWILIO_API_SECRET"]
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self.client = Client(api_key, api_secret, account_sid)

        port_number = 7777
        self.validation_server = HTTPServer(("", port_number), RequestHandler)
        self.tunnel = Tunnel()
        self.public_url = self.tunnel.get_url(None)
        print("public url ------ " + self.public_url)
        self.tunnel.create_tunnel(port_number)
        self.flow_sid = ""
        _thread.start_new_thread(self.start_http_server, ())

    def start_http_server(self):
        self.validation_server.serve_forever()

    def tearDown(self):
        self.client.studio.v2.flows(self.flow_sid).delete()
        self.tunnel.stop_tunnel()
        self.validation_server.shutdown()
        self.validation_server.server_close()

    def create_studio_flow(self, url, method):
        flow = self.client.studio.v2.flows.create(
            friendly_name="Python Cluster Test Flow",
            status="published",
            definition={
                "description": "Studio Flow",
                "states": [
                    {
                        "name": "Trigger",
                        "type": "trigger",
                        "transitions": [
                            {
                                "next": "httpRequest",
                                "event": "incomingRequest",
                            },
                        ],
                        "properties": {},
                    },
                    {
                        "name": "httpRequest",
                        "type": "make-http-request",
                        "transitions": [],
                        "properties": {
                            "method": method,
                            "content_type": "application/x-www-form-urlencoded;charset=utf-8",
                            "url": url,
                        },
                    },
                ],
                "initial_state": "Trigger",
                "flags": {
                    "allow_concurrent_calls": True,
                },
            },
        )
        return flow

    def validate(self, method):
        flow = self.create_studio_flow(url=self.public_url, method=method)
        self.flow_sid = flow.sid
        time.sleep(5)
        self.client.studio.v2.flows(self.flow_sid).executions.create(
            to="to", from_="from"
        )

    def test_get(self):
        time.sleep(5)
        self.validate("GET")
        time.sleep(5)
        self.assertEqual(RequestHandler.is_request_valid, True)

    def test_post(self):
        time.sleep(5)
        self.validate("POST")
        time.sleep(5)
        self.assertEqual(RequestHandler.is_request_valid, True)
