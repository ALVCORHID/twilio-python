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

from typing import Any, Dict, Optional
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class OauthInstance(InstanceResource):
    """
    :ivar keys: A collection of certificates where are signed Twilio-issued tokens.
    :ivar url:
    """

    def __init__(self, version: Version, payload: Dict[str, Any]):
        super().__init__(version)

        self.keys: Optional[Dict[str, object]] = payload.get("keys")
        self.url: Optional[str] = payload.get("url")

        self._context: Optional[OauthContext] = None

    @property
    def _proxy(self) -> "OauthContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: OauthContext for this OauthInstance
        """
        if self._context is None:
            self._context = OauthContext(
                self._version,
            )
        return self._context

    def fetch(self) -> "OauthInstance":
        """
        Fetch the OauthInstance


        :returns: The fetched OauthInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "OauthInstance":
        """
        Asynchronous coroutine to fetch the OauthInstance


        :returns: The fetched OauthInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Oauth.V1.OauthInstance>"


class OauthContext(InstanceContext):

    def __init__(self, version: Version):
        """
        Initialize the OauthContext

        :param version: Version that contains the resource
        """
        super().__init__(version)

        self._uri = "/certs"

    def fetch(self) -> OauthInstance:
        """
        Fetch the OauthInstance


        :returns: The fetched OauthInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return OauthInstance(
            self._version,
            payload,
        )

    async def fetch_async(self) -> OauthInstance:
        """
        Asynchronous coroutine to fetch the OauthInstance


        :returns: The fetched OauthInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return OauthInstance(
            self._version,
            payload,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """

        return "<Twilio.Oauth.V1.OauthContext>"


class OauthList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the OauthList

        :param version: Version that contains the resource

        """
        super().__init__(version)

    def get(self) -> OauthContext:
        """
        Constructs a OauthContext

        """
        return OauthContext(self._version)

    def __call__(self) -> OauthContext:
        """
        Constructs a OauthContext

        """
        return OauthContext(self._version)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Oauth.V1.OauthList>"
