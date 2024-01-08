r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Serverless
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
from twilio.rest.serverless.v1.service.asset import AssetList
from twilio.rest.serverless.v1.service.build import BuildList
from twilio.rest.serverless.v1.service.environment import EnvironmentList
from twilio.rest.serverless.v1.service.function import FunctionList


class ServiceInstance(InstanceResource):

    """
    :ivar sid: The unique string that we created to identify the Service resource.
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Service resource.
    :ivar friendly_name: The string that you assigned to describe the Service resource.
    :ivar unique_name: A user-defined string that uniquely identifies the Service resource. It can be used in place of the Service resource's `sid` in the URL to address the Service resource.
    :ivar include_credentials: Whether to inject Account credentials into a function invocation context.
    :ivar ui_editable: Whether the Service resource's properties and subresources can be edited via the UI.
    :ivar domain_base: The base domain name for this Service, which is a combination of the unique name and a randomly generated string.
    :ivar date_created: The date and time in GMT when the Service resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar date_updated: The date and time in GMT when the Service resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    :ivar url: The absolute URL of the Service resource.
    :ivar links: The URLs of the Service's nested resources.
    """

    def __init__(
        self, version: Version, payload: Dict[str, Any], sid: Optional[str] = None
    ):
        super().__init__(version)

        self.sid: Optional[str] = payload.get("sid")
        self.account_sid: Optional[str] = payload.get("account_sid")
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.include_credentials: Optional[bool] = payload.get("include_credentials")
        self.ui_editable: Optional[bool] = payload.get("ui_editable")
        self.domain_base: Optional[str] = payload.get("domain_base")
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.url: Optional[str] = payload.get("url")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "sid": sid or self.sid,
        }
        self._context: Optional[ServiceContext] = None

    @property
    def _proxy(self) -> "ServiceContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ServiceContext for this ServiceInstance
        """
        if self._context is None:
            self._context = ServiceContext(
                self._version,
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "ServiceInstance":
        """
        Fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "ServiceInstance":
        """
        Asynchronous coroutine to fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        include_credentials: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        ui_editable: Union[bool, object] = values.unset,
    ) -> "ServiceInstance":
        """
        Update the ServiceInstance

        :param include_credentials: Whether to inject Account credentials into a function invocation context.
        :param friendly_name: A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters.
        :param ui_editable: Whether the Service resource's properties and subresources can be edited via the UI. The default value is `false`.

        :returns: The updated ServiceInstance
        """
        return self._proxy.update(
            include_credentials=include_credentials,
            friendly_name=friendly_name,
            ui_editable=ui_editable,
        )

    async def update_async(
        self,
        include_credentials: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        ui_editable: Union[bool, object] = values.unset,
    ) -> "ServiceInstance":
        """
        Asynchronous coroutine to update the ServiceInstance

        :param include_credentials: Whether to inject Account credentials into a function invocation context.
        :param friendly_name: A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters.
        :param ui_editable: Whether the Service resource's properties and subresources can be edited via the UI. The default value is `false`.

        :returns: The updated ServiceInstance
        """
        return await self._proxy.update_async(
            include_credentials=include_credentials,
            friendly_name=friendly_name,
            ui_editable=ui_editable,
        )

    @property
    def assets(self) -> AssetList:
        """
        Access the assets
        """
        return self._proxy.assets

    @property
    def builds(self) -> BuildList:
        """
        Access the builds
        """
        return self._proxy.builds

    @property
    def environments(self) -> EnvironmentList:
        """
        Access the environments
        """
        return self._proxy.environments

    @property
    def functions(self) -> FunctionList:
        """
        Access the functions
        """
        return self._proxy.functions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.ServiceInstance {}>".format(context)


class ServiceContext(InstanceContext):
    def __init__(self, version: Version, sid: str):
        """
        Initialize the ServiceContext

        :param version: Version that contains the resource
        :param sid: The `sid` or `unique_name` of the Service resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "sid": sid,
        }
        self._uri = "/Services/{sid}".format(**self._solution)

        self._assets: Optional[AssetList] = None
        self._builds: Optional[BuildList] = None
        self._environments: Optional[EnvironmentList] = None
        self._functions: Optional[FunctionList] = None

    def delete(self) -> bool:
        """
        Deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the ServiceInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> ServiceInstance:
        """
        Fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> ServiceInstance:
        """
        Asynchronous coroutine to fetch the ServiceInstance


        :returns: The fetched ServiceInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return ServiceInstance(
            self._version,
            payload,
            sid=self._solution["sid"],
        )

    def update(
        self,
        include_credentials: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        ui_editable: Union[bool, object] = values.unset,
    ) -> ServiceInstance:
        """
        Update the ServiceInstance

        :param include_credentials: Whether to inject Account credentials into a function invocation context.
        :param friendly_name: A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters.
        :param ui_editable: Whether the Service resource's properties and subresources can be edited via the UI. The default value is `false`.

        :returns: The updated ServiceInstance
        """
        data = values.of(
            {
                "IncludeCredentials": include_credentials,
                "FriendlyName": friendly_name,
                "UiEditable": ui_editable,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload, sid=self._solution["sid"])

    async def update_async(
        self,
        include_credentials: Union[bool, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        ui_editable: Union[bool, object] = values.unset,
    ) -> ServiceInstance:
        """
        Asynchronous coroutine to update the ServiceInstance

        :param include_credentials: Whether to inject Account credentials into a function invocation context.
        :param friendly_name: A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters.
        :param ui_editable: Whether the Service resource's properties and subresources can be edited via the UI. The default value is `false`.

        :returns: The updated ServiceInstance
        """
        data = values.of(
            {
                "IncludeCredentials": include_credentials,
                "FriendlyName": friendly_name,
                "UiEditable": ui_editable,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload, sid=self._solution["sid"])

    @property
    def assets(self) -> AssetList:
        """
        Access the assets
        """
        if self._assets is None:
            self._assets = AssetList(
                self._version,
                self._solution["sid"],
            )
        return self._assets

    @property
    def builds(self) -> BuildList:
        """
        Access the builds
        """
        if self._builds is None:
            self._builds = BuildList(
                self._version,
                self._solution["sid"],
            )
        return self._builds

    @property
    def environments(self) -> EnvironmentList:
        """
        Access the environments
        """
        if self._environments is None:
            self._environments = EnvironmentList(
                self._version,
                self._solution["sid"],
            )
        return self._environments

    @property
    def functions(self) -> FunctionList:
        """
        Access the functions
        """
        if self._functions is None:
            self._functions = FunctionList(
                self._version,
                self._solution["sid"],
            )
        return self._functions

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Serverless.V1.ServiceContext {}>".format(context)


class ServicePage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> ServiceInstance:
        """
        Build an instance of ServiceInstance

        :param payload: Payload response from the API
        """
        return ServiceInstance(self._version, payload)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.ServicePage>"


class ServiceList(ListResource):
    def __init__(self, version: Version):
        """
        Initialize the ServiceList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Services"

    def create(
        self,
        unique_name: str,
        friendly_name: str,
        include_credentials: Union[bool, object] = values.unset,
        ui_editable: Union[bool, object] = values.unset,
    ) -> ServiceInstance:
        """
        Create the ServiceInstance

        :param unique_name: A user-defined string that uniquely identifies the Service resource. It can be used as an alternative to the `sid` in the URL path to address the Service resource. This value must be 50 characters or less in length and be unique.
        :param friendly_name: A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters.
        :param include_credentials: Whether to inject Account credentials into a function invocation context. The default value is `true`.
        :param ui_editable: Whether the Service's properties and subresources can be edited via the UI. The default value is `false`.

        :returns: The created ServiceInstance
        """

        data = values.of(
            {
                "UniqueName": unique_name,
                "FriendlyName": friendly_name,
                "IncludeCredentials": include_credentials,
                "UiEditable": ui_editable,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload)

    async def create_async(
        self,
        unique_name: str,
        friendly_name: str,
        include_credentials: Union[bool, object] = values.unset,
        ui_editable: Union[bool, object] = values.unset,
    ) -> ServiceInstance:
        """
        Asynchronously create the ServiceInstance

        :param unique_name: A user-defined string that uniquely identifies the Service resource. It can be used as an alternative to the `sid` in the URL path to address the Service resource. This value must be 50 characters or less in length and be unique.
        :param friendly_name: A descriptive string that you create to describe the Service resource. It can be a maximum of 255 characters.
        :param include_credentials: Whether to inject Account credentials into a function invocation context. The default value is `true`.
        :param ui_editable: Whether the Service's properties and subresources can be edited via the UI. The default value is `false`.

        :returns: The created ServiceInstance
        """

        data = values.of(
            {
                "UniqueName": unique_name,
                "FriendlyName": friendly_name,
                "IncludeCredentials": include_credentials,
                "UiEditable": ui_editable,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return ServiceInstance(self._version, payload)

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[ServiceInstance]:
        """
        Streams ServiceInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[ServiceInstance]:
        """
        Asynchronously streams ServiceInstance records from the API as a generator stream.
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
    ) -> List[ServiceInstance]:
        """
        Lists ServiceInstance records from the API as a list.
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
    ) -> List[ServiceInstance]:
        """
        Asynchronously lists ServiceInstance records from the API as a list.
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
    ) -> ServicePage:
        """
        Retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return ServicePage(self._version, response)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> ServicePage:
        """
        Asynchronously retrieve a single page of ServiceInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of ServiceInstance
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
        return ServicePage(self._version, response)

    def get_page(self, target_url: str) -> ServicePage:
        """
        Retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return ServicePage(self._version, response)

    async def get_page_async(self, target_url: str) -> ServicePage:
        """
        Asynchronously retrieve a specific page of ServiceInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of ServiceInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return ServicePage(self._version, response)

    def get(self, sid: str) -> ServiceContext:
        """
        Constructs a ServiceContext

        :param sid: The `sid` or `unique_name` of the Service resource to update.
        """
        return ServiceContext(self._version, sid=sid)

    def __call__(self, sid: str) -> ServiceContext:
        """
        Constructs a ServiceContext

        :param sid: The `sid` or `unique_name` of the Service resource to update.
        """
        return ServiceContext(self._version, sid=sid)

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Serverless.V1.ServiceList>"
