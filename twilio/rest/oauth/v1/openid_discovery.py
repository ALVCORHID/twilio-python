r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Oauth
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, List, Optional
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class OpenidDiscoveryInstance(InstanceResource):
    """
    :ivar issuer: The URL of the party that will create the token and sign it with its private key.
    :ivar authorization_endpoint: The endpoint that validates all authorization requests.
    :ivar device_authorization_endpoint: The endpoint that validates all device code related authorization requests.
    :ivar token_endpoint: The URL of the token endpoint. After a client has received an authorization code, that code is presented to the token endpoint and exchanged for an identity token, an access token, and a refresh token.
    :ivar userinfo_endpoint: The URL of the user info endpoint, which returns user profile information to a client. Keep in mind that the user info endpoint returns only the information that has been requested.
    :ivar revocation_endpoint: The endpoint used to revoke access or refresh tokens issued by the authorization server.
    :ivar jwk_uri: The URL of your JSON Web Key Set. This set is a collection of JSON Web Keys, a standard method for representing cryptographic keys in a JSON structure.
    :ivar response_type_supported: A collection of response type supported by authorization server.
    :ivar subject_type_supported: A collection of subject by authorization server.
    :ivar id_token_signing_alg_values_supported: A collection of JWS signing algorithms supported by authorization server to sign identity token.
    :ivar scopes_supported: A collection of scopes supported by authorization server for identity token
    :ivar claims_supported: A collection of claims supported by authorization server for identity token
    :ivar url:
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.issuer: Optional[str] = payload.get("issuer")
        self.authorization_endpoint: Optional[str] = payload.get(
            "authorization_endpoint"
        )
        self.device_authorization_endpoint: Optional[str] = payload.get(
            "device_authorization_endpoint"
        )
        self.token_endpoint: Optional[str] = payload.get("token_endpoint")
        self.userinfo_endpoint: Optional[str] = payload.get("userinfo_endpoint")
        self.revocation_endpoint: Optional[str] = payload.get("revocation_endpoint")
        self.jwk_uri: Optional[str] = payload.get("jwk_uri")
        self.response_type_supported: Optional[List[str]] = payload.get(
            "response_type_supported"
        )
        self.subject_type_supported: Optional[List[str]] = payload.get(
            "subject_type_supported"
        )
        self.id_token_signing_alg_values_supported: Optional[List[str]] = payload.get(
            "id_token_signing_alg_values_supported"
        )
        self.scopes_supported: Optional[List[str]] = payload.get("scopes_supported")
        self.claims_supported: Optional[List[str]] = payload.get("claims_supported")
        self.url: Optional[str] = payload.get("url")

        self._context: Optional[OpenidDiscoveryContext] = None

    @property
    def _proxy(self) -> "OpenidDiscoveryContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: OpenidDiscoveryContext for this OpenidDiscoveryInstance
        """
        if self._context is None:
            self._context = OpenidDiscoveryContext(
                self._version,
            )
        return self._context

    def fetch(self) -> "OpenidDiscoveryInstance":
        """
        Fetch the OpenidDiscoveryInstance


        :returns: The fetched OpenidDiscoveryInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "OpenidDiscoveryInstance":
        """
        Asynchronous coroutine to fetch the OpenidDiscoveryInstance


        :returns: The fetched OpenidDiscoveryInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Oauth.V1.OpenidDiscoveryInstance>"


class OpenidDiscoveryContext(InstanceContext):

    def __init__(self, version: Version):
        """
        Initialize the OpenidDiscoveryContext

        :param version: Version that contains the resource
        """
        super().__init__(version)

        self._uri = "/.well-known/openid-configuration"

    def fetch(self) -> OpenidDiscoveryInstance:
        """
        Fetch the OpenidDiscoveryInstance


        :returns: The fetched OpenidDiscoveryInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return OpenidDiscoveryInstance(
            self._version,
            payload,
        )

    async def fetch_async(self) -> OpenidDiscoveryInstance:
        """
        Asynchronous coroutine to fetch the OpenidDiscoveryInstance


        :returns: The fetched OpenidDiscoveryInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return OpenidDiscoveryInstance(
            self._version,
            payload,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Oauth.V1.OpenidDiscoveryContext>"


class OpenidDiscoveryList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the OpenidDiscoveryList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self) -> OpenidDiscoveryContext:
        """
        Constructs a OpenidDiscoveryContext

        """
        return OpenidDiscoveryContext(self._version)

    def __call__(self) -> OpenidDiscoveryContext:
        """
        Constructs a OpenidDiscoveryContext

        """
        return OpenidDiscoveryContext(self._version)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Oauth.V1.OpenidDiscoveryList>"
