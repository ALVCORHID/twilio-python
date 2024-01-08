r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Trusthub
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class EndUserTypeInstance(InstanceResource):

    """
    :ivar sid: The unique string that identifies the End-User Type resource.
    :ivar friendly_name: A human-readable description that is assigned to describe the End-User Type resource. Examples can include first name, last name, email, business name, etc
    :ivar machine_name: A machine-readable description of the End-User Type resource. Examples can include first_name, last_name, email, business_name, etc.
    :ivar fields: The required information for creating an End-User. The required fields will change as regulatory needs change and will differ for businesses and individuals.
    :ivar url: The absolute URL of the End-User Type resource.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.machine_name: Optional[str] = payload.get("machine_name")
        self.fields: Optional[List[Dict[str, object]]] = payload.get("fields")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[EndUserTypeContext] = None

    @property
    def _proxy(self) -> "EndUserTypeContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: EndUserTypeContext for this EndUserTypeInstance
        """
        if self._context is None:
            self._context = EndUserTypeContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def fetch(self) -> "EndUserTypeInstance":
        """
        Fetch the EndUserTypeInstance


        :returns: The fetched EndUserTypeInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "EndUserTypeInstance":
        """
        Asynchronous coroutine to fetch the EndUserTypeInstance


        :returns: The fetched EndUserTypeInstance
        """
        return await self._proxy.fetch_async()

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trusthub.V1.EndUserTypeInstance {}>".format(context)


class EndUserTypeContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the EndUserTypeContext

        :param version: Version that contains the resource
        :param sid: The unique string that identifies the End-User Type resource.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/EndUserTypes/{sid}".format(**self._solution)

    def fetch(self) -> EndUserTypeInstance:
        """
        Fetch the EndUserTypeInstance


        :returns: The fetched EndUserTypeInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return EndUserTypeInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> EndUserTypeInstance:
        """
        Asynchronous coroutine to fetch the EndUserTypeInstance


        :returns: The fetched EndUserTypeInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return EndUserTypeInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Trusthub.V1.EndUserTypeContext {}>".format(context)


class EndUserTypePage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> EndUserTypeInstance:
        """
        Build an instance of EndUserTypeInstance

        :param payload: Payload response from the API
        """
        return EndUserTypeInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trusthub.V1.EndUserTypePage>"


class EndUserTypeList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the EndUserTypeList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/EndUserTypes"

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[EndUserTypeInstance]:
        """
        Streams EndUserTypeInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[EndUserTypeInstance]:
        """
        Asynchronously streams EndUserTypeInstance records from the API as a generator stream.
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
    ) -> List[EndUserTypeInstance]:
        """
        Lists EndUserTypeInstance records from the API as a list.
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
    ) -> List[EndUserTypeInstance]:
        """
        Asynchronously lists EndUserTypeInstance records from the API as a list.
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
    ) -> EndUserTypePage:
        """
        Retrieve a single page of EndUserTypeInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of EndUserTypeInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return EndUserTypePage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> EndUserTypePage:
        """
        Asynchronously retrieve a single page of EndUserTypeInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of EndUserTypeInstance
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
        return EndUserTypePage(self._version, response)

    def get_page(self, target_url: str) -> EndUserTypePage:
        """
        Retrieve a specific page of EndUserTypeInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of EndUserTypeInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return EndUserTypePage(self._version, response)

    async def get_page_async(self, target_url: str) -> EndUserTypePage:
        """
        Asynchronously retrieve a specific page of EndUserTypeInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of EndUserTypeInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return EndUserTypePage(self._version, response)

    def get(self, sid: str) -> EndUserTypeContext:
        """
        Constructs a EndUserTypeContext

        :param sid: The unique string that identifies the End-User Type resource.
        """
        return EndUserTypeContext(self._version, sid=sid)

    def __call__(self, sid: str) -> EndUserTypeContext:
        """
        Constructs a EndUserTypeContext

        :param sid: The unique string that identifies the End-User Type resource.
        """
        return EndUserTypeContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Trusthub.V1.EndUserTypeList>"
