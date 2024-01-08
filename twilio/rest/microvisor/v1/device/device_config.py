r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Microvisor
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class DeviceConfigInstance(InstanceResource):

    """
    :ivar device_sid: A 34-character string that uniquely identifies the parent Device.
    :ivar key: The config key; up to 100 characters.
    :ivar value: The config value; up to 4096 characters.
    :ivar date_updated:
    :ivar url: The absolute URL of the Config.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        device_sid: str,
        key: Optional[str] = None,
    ):
        super().__init__(version)

        self.device_sid: Optional[str] = payload.get("device_sid")
        self.key: Optional[str] = payload.get("key")
        self.value: Optional[str] = payload.get("value")
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "device_sid": device_sid,
            "key": key or self.key,
        }
        self._context: Optional[DeviceConfigContext] = None

    @property
    def _proxy(self) -> "DeviceConfigContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: DeviceConfigContext for this DeviceConfigInstance
        """
        if self._context is None:
            self._context = DeviceConfigContext(
                self._version,
                device_sid=self._solution["device_sid"],
                key=self._solution["key"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the DeviceConfigInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the DeviceConfigInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "DeviceConfigInstance":
        """
        Fetch the DeviceConfigInstance


        :returns: The fetched DeviceConfigInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "DeviceConfigInstance":
        """
        Asynchronous coroutine to fetch the DeviceConfigInstance


        :returns: The fetched DeviceConfigInstance
        """
        return await self._proxy.fetch_async()

    def update(self, value: str) -> "DeviceConfigInstance":
        """
        Update the DeviceConfigInstance

        :param value: The config value; up to 4096 characters.

        :returns: The updated DeviceConfigInstance
        """
        return self._proxy.update(
            value=value,
        )

    async def update_async(self, value: str) -> "DeviceConfigInstance":
        """
        Asynchronous coroutine to update the DeviceConfigInstance

        :param value: The config value; up to 4096 characters.

        :returns: The updated DeviceConfigInstance
        """
        return await self._proxy.update_async(
            value=value,
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Microvisor.V1.DeviceConfigInstance {}>".format(context)


class DeviceConfigContext(InstanceContext):
    def __init__(self, version: Version, device_sid: str, key: str):
        """
        Initialize the DeviceConfigContext

        :param version: Version that contains the resource
        :param device_sid: A 34-character string that uniquely identifies the Device.
        :param key: The config key; up to 100 characters.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "device_sid": device_sid,
            "key": key,
        }
        self._uri = "/Devices/{device_sid}/Configs/{key}".format(**self._solution)

    def delete(self) -> bool:
        """
        Deletes the DeviceConfigInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the DeviceConfigInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> DeviceConfigInstance:
        """
        Fetch the DeviceConfigInstance


        :returns: The fetched DeviceConfigInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return DeviceConfigInstance(
            self._version,
            payload,
            device_sid=self._solution["device_sid"],
            key=self._solution["key"],
        )

    async def fetch_async(self) -> DeviceConfigInstance:
        """
        Asynchronous coroutine to fetch the DeviceConfigInstance


        :returns: The fetched DeviceConfigInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return DeviceConfigInstance(
            self._version,
            payload,
            device_sid=self._solution["device_sid"],
            key=self._solution["key"],
        )

    def update(self, value: str) -> DeviceConfigInstance:
        """
        Update the DeviceConfigInstance

        :param value: The config value; up to 4096 characters.

        :returns: The updated DeviceConfigInstance
        """
        data = values.of(
            {
                "Value": value,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DeviceConfigInstance(
            self._version,
            payload,
            device_sid=self._solution["device_sid"],
            key=self._solution["key"],
        )

    async def update_async(self, value: str) -> DeviceConfigInstance:
        """
        Asynchronous coroutine to update the DeviceConfigInstance

        :param value: The config value; up to 4096 characters.

        :returns: The updated DeviceConfigInstance
        """
        data = values.of(
            {
                "Value": value,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DeviceConfigInstance(
            self._version,
            payload,
            device_sid=self._solution["device_sid"],
            key=self._solution["key"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Microvisor.V1.DeviceConfigContext {}>".format(context)


class DeviceConfigPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> DeviceConfigInstance:
        """
        Build an instance of DeviceConfigInstance

        :param payload: Payload response from the API
        """
        return DeviceConfigInstance(
            self._version, payload, device_sid=self._solution["device_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Microvisor.V1.DeviceConfigPage>"


class DeviceConfigList(ListResource):
    def __init__(self, version: Version, device_sid: str):
        """
        Initialize the DeviceConfigList

        :param version: Version that contains the resource
        :param device_sid: A 34-character string that uniquely identifies the Device.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "device_sid": device_sid,
        }
        self._uri = "/Devices/{device_sid}/Configs".format(**self._solution)

    def create(self, key: str, value: str) -> DeviceConfigInstance:
        """
        Create the DeviceConfigInstance

        :param key: The config key; up to 100 characters.
        :param value: The config value; up to 4096 characters.

        :returns: The created DeviceConfigInstance
        """

        data = values.of(
            {
                "Key": key,
                "Value": value,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DeviceConfigInstance(
            self._version, payload, device_sid=self._solution["device_sid"]
        )

    async def create_async(self, key: str, value: str) -> DeviceConfigInstance:
        """
        Asynchronously create the DeviceConfigInstance

        :param key: The config key; up to 100 characters.
        :param value: The config value; up to 4096 characters.

        :returns: The created DeviceConfigInstance
        """

        data = values.of(
            {
                "Key": key,
                "Value": value,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return DeviceConfigInstance(
            self._version, payload, device_sid=self._solution["device_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[DeviceConfigInstance]:
        """
        Streams DeviceConfigInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(page_size=limits["page_size"])

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[DeviceConfigInstance]:
        """
        Asynchronously streams DeviceConfigInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(page_size=limits["page_size"])

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DeviceConfigInstance]:
        """
        Lists DeviceConfigInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return list(
            self.stream(
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[DeviceConfigInstance]:
        """
        Asynchronously lists DeviceConfigInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param limit: Upper limit for the number of records to return. list() guarantees
                      never to return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, list() will attempt to read the limit
                          with the most efficient page size, i.e. min(limit, 1000)

        :returns: list that will contain up to limit results
        """
        return [
            record
            async for record in await self.stream_async(
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> DeviceConfigPage:
        """
        Retrieve a single page of DeviceConfigInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of DeviceConfigInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return DeviceConfigPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> DeviceConfigPage:
        """
        Asynchronously retrieve a single page of DeviceConfigInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of DeviceConfigInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return DeviceConfigPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> DeviceConfigPage:
        """
        Retrieve a specific page of DeviceConfigInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of DeviceConfigInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return DeviceConfigPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> DeviceConfigPage:
        """
        Asynchronously retrieve a specific page of DeviceConfigInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of DeviceConfigInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return DeviceConfigPage(self._version, response, self._solution)

    def get(self, key: str) -> DeviceConfigContext:
        """
        Constructs a DeviceConfigContext

        :param key: The config key; up to 100 characters.
        """
        return DeviceConfigContext(
            self._version, device_sid=self._solution["device_sid"], key=key
        )

    def __call__(self, key: str) -> DeviceConfigContext:
        """
        Constructs a DeviceConfigContext

        :param key: The config key; up to 100 characters.
        """
        return DeviceConfigContext(
            self._version, device_sid=self._solution["device_sid"], key=key
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Microvisor.V1.DeviceConfigList>"
