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


class StyleSheetInstance(InstanceResource):
    """
    :ivar account_sid: The unique ID of the Account that created this Assistant
    :ivar assistant_sid: The unique ID of the Assistant
    :ivar url:
    :ivar data: The JSON style sheet object
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
        self._context: Optional[StyleSheetContext] = None

    @property
    def _proxy(self) -> "StyleSheetContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: StyleSheetContext for this StyleSheetInstance
        """
        if self._context is None:
            self._context = StyleSheetContext(
                self._version,
                assistant_sid=self._solution["assistant_sid"],
            )
        return self._context

    def fetch(self) -> "StyleSheetInstance":
        """
        Fetch the StyleSheetInstance


        :returns: The fetched StyleSheetInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "StyleSheetInstance":
        """
        Asynchronous coroutine to fetch the StyleSheetInstance


        :returns: The fetched StyleSheetInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self, style_sheet: Union[object, object] = values.unset
    ) -> "StyleSheetInstance":
        """
        Update the StyleSheetInstance

        :param style_sheet: The JSON Style sheet string

        :returns: The updated StyleSheetInstance
        """
        return self._proxy.update(
            style_sheet=style_sheet,
        )

    async def update_async(
        self, style_sheet: Union[object, object] = values.unset
    ) -> "StyleSheetInstance":
        """
        Asynchronous coroutine to update the StyleSheetInstance

        :param style_sheet: The JSON Style sheet string

        :returns: The updated StyleSheetInstance
        """
        return await self._proxy.update_async(
            style_sheet=style_sheet,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Understand.StyleSheetInstance {}>".format(context)


class StyleSheetContext(InstanceContext):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the StyleSheetContext

        :param version: Version that contains the resource
        :param assistant_sid: The unique ID of the Assistant
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
        }
        self._uri = "/Assistants/{assistant_sid}/StyleSheet".format(**self._solution)

    def fetch(self) -> StyleSheetInstance:
        """
        Fetch the StyleSheetInstance


        :returns: The fetched StyleSheetInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return StyleSheetInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
        )

    async def fetch_async(self) -> StyleSheetInstance:
        """
        Asynchronous coroutine to fetch the StyleSheetInstance


        :returns: The fetched StyleSheetInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return StyleSheetInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
        )

    def update(
        self, style_sheet: Union[object, object] = values.unset
    ) -> StyleSheetInstance:
        """
        Update the StyleSheetInstance

        :param style_sheet: The JSON Style sheet string

        :returns: The updated StyleSheetInstance
        """
        data = values.of(
            {
                "StyleSheet": serialize.object(style_sheet),
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return StyleSheetInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    async def update_async(
        self, style_sheet: Union[object, object] = values.unset
    ) -> StyleSheetInstance:
        """
        Asynchronous coroutine to update the StyleSheetInstance

        :param style_sheet: The JSON Style sheet string

        :returns: The updated StyleSheetInstance
        """
        data = values.of(
            {
                "StyleSheet": serialize.object(style_sheet),
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return StyleSheetInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Preview.Understand.StyleSheetContext {}>".format(context)


class StyleSheetList(ListResource):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the StyleSheetList

        :param version: Version that contains the resource
        :param assistant_sid: The unique ID of the Assistant

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
        }

    def get(self) -> StyleSheetContext:
        """
        Constructs a StyleSheetContext

        """
        return StyleSheetContext(
            self._version, assistant_sid=self._solution["assistant_sid"]
        )

    def __call__(self) -> StyleSheetContext:
        """
        Constructs a StyleSheetContext

        """
        return StyleSheetContext(
            self._version, assistant_sid=self._solution["assistant_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Preview.Understand.StyleSheetList>"
