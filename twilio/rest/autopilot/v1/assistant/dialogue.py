r"""
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

from typing import Any, Dict, Optional
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version


class DialogueInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Dialogue resource.
    :ivar assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource.
    :ivar sid: The unique string that we created to identify the Dialogue resource.
    :ivar data: The JSON string that describes the dialogue session object.
    :ivar url: The absolute URL of the Dialogue resource.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        assistant_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.assistant_sid: Optional[str] = payload.get("assistant_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.data: Optional[Dict[str, object]] = payload.get("data")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "assistant_sid": assistant_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[DialogueContext] = None

    @property
    def _proxy(self) -> "DialogueContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: DialogueContext for this DialogueInstance
        """
        if self._context is None:
            self._context = DialogueContext(
                self._version,
                assistant_sid=self._solution["assistant_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "DialogueInstance":
        """
        Fetch the DialogueInstance


        :returns: The fetched DialogueInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "DialogueInstance":
        """
        Asynchronous coroutine to fetch the DialogueInstance


        :returns: The fetched DialogueInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.DialogueInstance {}>".format(context)


class DialogueContext(InstanceContext):

    def __init__(self, version: Version, assistant_sid: str, sid: str):
        """
        Initialize the DialogueContext

        :param version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.
        :param sid: The Twilio-provided string that uniquely identifies the Dialogue resource to fetch.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "sid": sid,
        }
        self._uri = "/Assistants/{assistant_sid}/Dialogues/{sid}".format(
            **self._solution
        )

    def fetch(self) -> DialogueInstance:
        """
        Fetch the DialogueInstance


        :returns: The fetched DialogueInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return DialogueInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> DialogueInstance:
        """
        Asynchronous coroutine to fetch the DialogueInstance


        :returns: The fetched DialogueInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return DialogueInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.DialogueContext {}>".format(context)


class DialogueList(ListResource):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the DialogueList

        :param version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to fetch.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
        }

    def get(self, sid: str) -> DialogueContext:
        """
        Constructs a DialogueContext

        :param sid: The Twilio-provided string that uniquely identifies the Dialogue resource to fetch.
        """
        return DialogueContext(
            self._version, assistant_sid=self._solution["assistant_sid"], sid=sid
        )

    def __call__(self, sid: str) -> DialogueContext:
        """
        Constructs a DialogueContext

        :param sid: The Twilio-provided string that uniquely identifies the Dialogue resource to fetch.
        """
        return DialogueContext(
            self._version, assistant_sid=self._solution["assistant_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Autopilot.V1.DialogueList>"
