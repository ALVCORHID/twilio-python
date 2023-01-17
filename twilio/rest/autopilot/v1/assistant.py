"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Autopilot
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource

from twilio.base.page import Page

from twilio.rest.assistant.defaults import DefaultsListInstancefrom twilio.rest.assistant.dialogue import DialogueListInstancefrom twilio.rest.assistant.field_type import FieldTypeListInstancefrom twilio.rest.assistant.model_build import ModelBuildListInstancefrom twilio.rest.assistant.query import QueryListInstancefrom twilio.rest.assistant.style_sheet import StyleSheetListInstancefrom twilio.rest.assistant.task import TaskListInstancefrom twilio.rest.assistant.webhook import WebhookListInstance


class AssistantContext(InstanceContext):
    def __init__(self, version: V1, sid: str):
        # TODO: needs autogenerated docs
        super(AssistantContextList, self).__init__(version)

        # Path Solution
        self._solution = { sid,  }
        self._uri = '/Assistants/${sid}'
        
        self._defaults = None
        self._dialogues = None
        self._field_types = None
        self._model_builds = None
        self._queries = None
        self._style_sheet = None
        self._tasks = None
        self._webhooks = None
        
        def delete(self):
            
            
            """
            Deletes the AssistantInstance

            :returns: True if delete succeeds, False otherwise
            :rtype: bool
            """
            return self._version.delete(method='DELETE', uri=self._uri, )
        
        def fetch(self):
            
            """
            Fetch the AssistantInstance

            :returns: The fetched AssistantInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return AssistantInstance(
                self._version,
                payload,
                sid=self._solution['sid'],
            )
            
            
        
        def update(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.update(method='post', uri=self._uri, data=data, )

            return AssistantInstance(self._version, payload, sid=self._solution['sid'], )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.AssistantContext>'



class AssistantInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super(AssistantInstance, self).__init__(version)
        self._properties = { 
            'account_sid' = payload.get('account_sid'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'friendly_name' = payload.get('friendly_name'),
            'latest_model_build_sid' = payload.get('latest_model_build_sid'),
            'links' = payload.get('links'),
            'log_queries' = payload.get('log_queries'),
            'development_stage' = payload.get('development_stage'),
            'needs_model_build' = payload.get('needs_model_build'),
            'sid' = payload.get('sid'),
            'unique_name' = payload.get('unique_name'),
            'url' = payload.get('url'),
            'callback_url' = payload.get('callback_url'),
            'callback_events' = payload.get('callback_events'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = AssistantContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def defaults(self):
        return self._proxy.defaults
    @property
    def dialogues(self):
        return self._proxy.dialogues
    @property
    def field_types(self):
        return self._proxy.field_types
    @property
    def model_builds(self):
        return self._proxy.model_builds
    @property
    def queries(self):
        return self._proxy.queries
    @property
    def style_sheet(self):
        return self._proxy.style_sheet
    @property
    def tasks(self):
        return self._proxy.tasks
    @property
    def webhooks(self):
        return self._proxy.webhooks
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.AssistantInstance {}>'.format(context)



class AssistantListInstance(ListResource):
    def __init__(self, version: V1):
        # TODO: needs autogenerated docs
        super(AssistantListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Assistants'
        
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return AssistantInstance(self._version, payload, )
            
        
        def page(self, page_size):
            
            data = values.of({
                'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return AssistantPage(self._version, payload, )
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.AssistantListInstance>'

