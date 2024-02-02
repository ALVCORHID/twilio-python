r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Preview
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Any, Dict, Optional, Union
from twilio.base import serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class AssistantInitiationActionsInstance(InstanceResource):
    """
    :ivar account_sid:
    :ivar assistant_sid:
    :ivar url:
    :ivar data:
    """

    def __init__(self, version: Version, payload: Dict[str, Any], assistant_sid: str):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.assistant_sid: Optional[str] = payload.get("assistant_sid")
        self.url: Optional[str] = payload.get("url")
        self.data: Optional[Dict[str, object]] = payload.get("data")

        self._solution = {
            "assistant_sid": assistant_sid,
        }
        self._context: Optional[AssistantInitiationActionsContext] = None

    @property
    def _proxy(self) -> "AssistantInitiationActionsContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AssistantInitiationActionsContext for this AssistantInitiationActionsInstance
        """
        if self._context is None:
            self._context = AssistantInitiationActionsContext(
                self._version,
                assistant_sid=self._solution["assistant_sid"],
            )
        return self._context

    def fetch(self) -> "AssistantInitiationActionsInstance":
        """
        Fetch the AssistantInitiationActionsInstance


        :returns: The fetched AssistantInitiationActionsInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AssistantInitiationActionsInstance":
        """
        Asynchronous coroutine to fetch the AssistantInitiationActionsInstance


        :returns: The fetched AssistantInitiationActionsInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, initiation_actions: Union[object, object] = values.unset
    ) -> "AssistantInitiationActionsInstance":
        """
        Update the AssistantInitiationActionsInstance

        :param initiation_actions:

        :returns: The updated AssistantInitiationActionsInstance
        """
        return self._proxy.update(
            initiation_actions=initiation_actions,
        )

    async def update_async(
        self, initiation_actions: Union[object, object] = values.unset
    ) -> "AssistantInitiationActionsInstance":
        """
        Asynchronous coroutine to update the AssistantInitiationActionsInstance

        :param initiation_actions:

        :returns: The updated AssistantInitiationActionsInstance
        """
        return await self._proxy.update_async(
            initiation_actions=initiation_actions,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return (
            "<Twilio.Preview.Understand.AssistantInitiationActionsInstance {}>".format(
                context
            )
        )


class AssistantInitiationActionsContext(InstanceContext):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the AssistantInitiationActionsContext

        :param version: Version that contains the resource
        :param assistant_sid:
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
        }
        self._uri = "/Assistants/{assistant_sid}/InitiationActions".format(
            **self._solution
        )

    def fetch(self) -> AssistantInitiationActionsInstance:
        """
        Fetch the AssistantInitiationActionsInstance


        :returns: The fetched AssistantInitiationActionsInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AssistantInitiationActionsInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
        )

    async def fetch_async(self) -> AssistantInitiationActionsInstance:
        """
        Asynchronous coroutine to fetch the AssistantInitiationActionsInstance


        :returns: The fetched AssistantInitiationActionsInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AssistantInitiationActionsInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
        )

    def update(
        self, initiation_actions: Union[object, object] = values.unset
    ) -> AssistantInitiationActionsInstance:
        """
        Update the AssistantInitiationActionsInstance

        :param initiation_actions:

        :returns: The updated AssistantInitiationActionsInstance
        """
        data = values.of(
            {
                "InitiationActions": serialize.object(initiation_actions),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AssistantInitiationActionsInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    async def update_async(
        self, initiation_actions: Union[object, object] = values.unset
    ) -> AssistantInitiationActionsInstance:
        """
        Asynchronous coroutine to update the AssistantInitiationActionsInstance

        :param initiation_actions:

        :returns: The updated AssistantInitiationActionsInstance
        """
        data = values.of(
            {
                "InitiationActions": serialize.object(initiation_actions),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AssistantInitiationActionsInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return (
            "<Twilio.Preview.Understand.AssistantInitiationActionsContext {}>".format(
                context
            )
        )


class AssistantInitiationActionsList(ListResource):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the AssistantInitiationActionsList

        :param version: Version that contains the resource
        :param assistant_sid:

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
        }

    def get(self) -> AssistantInitiationActionsContext:
        """
        Constructs a AssistantInitiationActionsContext

        """
        return AssistantInitiationActionsContext(
            self._version, assistant_sid=self._solution["assistant_sid"]
        )

    def __call__(self) -> AssistantInitiationActionsContext:
        """
        Constructs a AssistantInitiationActionsContext

        """
        return AssistantInitiationActionsContext(
            self._version, assistant_sid=self._solution["assistant_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Understand.AssistantInitiationActionsList>"
