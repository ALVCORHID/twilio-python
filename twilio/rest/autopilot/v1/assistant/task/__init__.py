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

from datetime import datetime
from typing import Any, Dict, List, Optional, Union, Iterator, AsyncIterator
from twilio.base import deserialize, serialize, values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page
from twilio.rest.autopilot.v1.assistant.task.field import FieldList
from twilio.rest.autopilot.v1.assistant.task.sample import SampleList
from twilio.rest.autopilot.v1.assistant.task.task_actions import TaskActionsList
from twilio.rest.autopilot.v1.assistant.task.task_statistics import TaskStatisticsList


class TaskInstance(InstanceResource):
    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Task resource.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar friendly_name: The string that you assigned to describe the resource. It is not unique and can be up to 255 characters long.
    :ivar links: A list of the URLs of related resources.
    :ivar assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource.
    :ivar sid: The unique string that we created to identify the Task resource.
    :ivar unique_name: An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
    :ivar actions_url: The URL from which the Assistant can fetch actions.
    :ivar url: The absolute URL of the Task resource.
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
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.links: Optional[Dict[str, object]] = payload.get("links")
        self.assistant_sid: Optional[str] = payload.get("assistant_sid")
        self.sid: Optional[str] = payload.get("sid")
        self.unique_name: Optional[str] = payload.get("unique_name")
        self.actions_url: Optional[str] = payload.get("actions_url")
        self.url: Optional[str] = payload.get("url")

        self._solution = {
            "assistant_sid": assistant_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[TaskContext] = None

    @property
    def _proxy(self) -> "TaskContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TaskContext for this TaskInstance
        """
        if self._context is None:
            self._context = TaskContext(
                self._version,
                assistant_sid=self._solution["assistant_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the TaskInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the TaskInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "TaskInstance":
        """
        Fetch the TaskInstance


        :returns: The fetched TaskInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "TaskInstance":
        """
        Asynchronous coroutine to fetch the TaskInstance


        :returns: The fetched TaskInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        actions: Union[object, object] = values.unset,
        actions_url: Union[str, object] = values.unset,
    ) -> "TaskInstance":
        """
        Update the TaskInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 64 characters or less in length and be unique. It can be used as an alternative to the `sid` in the URL path to address the resource.
        :param actions: The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task.
        :param actions_url: The URL from which the Assistant can fetch actions.

        :returns: The updated TaskInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            unique_name=unique_name,
            actions=actions,
            actions_url=actions_url,
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        actions: Union[object, object] = values.unset,
        actions_url: Union[str, object] = values.unset,
    ) -> "TaskInstance":
        """
        Asynchronous coroutine to update the TaskInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 64 characters or less in length and be unique. It can be used as an alternative to the `sid` in the URL path to address the resource.
        :param actions: The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task.
        :param actions_url: The URL from which the Assistant can fetch actions.

        :returns: The updated TaskInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            unique_name=unique_name,
            actions=actions,
            actions_url=actions_url,
        )

    @property
    def fields(self) -> FieldList:
        """
        Access the fields
        """
        return self._proxy.fields

    @property
    def samples(self) -> SampleList:
        """
        Access the samples
        """
        return self._proxy.samples

    @property
    def task_actions(self) -> TaskActionsList:
        """
        Access the task_actions
        """
        return self._proxy.task_actions

    @property
    def statistics(self) -> TaskStatisticsList:
        """
        Access the statistics
        """
        return self._proxy.statistics

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.TaskInstance {}>".format(context)


class TaskContext(InstanceContext):

    def __init__(self, version: Version, assistant_sid: str, sid: str):
        """
        Initialize the TaskContext

        :param version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.
        :param sid: The Twilio-provided string that uniquely identifies the Task resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
            "sid": sid,
        }
        self._uri = "/Assistants/{assistant_sid}/Tasks/{sid}".format(**self._solution)

        self._fields: Optional[FieldList] = None
        self._samples: Optional[SampleList] = None
        self._task_actions: Optional[TaskActionsList] = None
        self._statistics: Optional[TaskStatisticsList] = None

    def delete(self) -> bool:
        """
        Deletes the TaskInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the TaskInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> TaskInstance:
        """
        Fetch the TaskInstance


        :returns: The fetched TaskInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return TaskInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> TaskInstance:
        """
        Asynchronous coroutine to fetch the TaskInstance


        :returns: The fetched TaskInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return TaskInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        actions: Union[object, object] = values.unset,
        actions_url: Union[str, object] = values.unset,
    ) -> TaskInstance:
        """
        Update the TaskInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 64 characters or less in length and be unique. It can be used as an alternative to the `sid` in the URL path to address the resource.
        :param actions: The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task.
        :param actions_url: The URL from which the Assistant can fetch actions.

        :returns: The updated TaskInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "Actions": serialize.object(actions),
                "ActionsUrl": actions_url,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        unique_name: Union[str, object] = values.unset,
        actions: Union[object, object] = values.unset,
        actions_url: Union[str, object] = values.unset,
    ) -> TaskInstance:
        """
        Asynchronous coroutine to update the TaskInstance

        :param friendly_name: A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
        :param unique_name: An application-defined string that uniquely identifies the resource. This value must be 64 characters or less in length and be unique. It can be used as an alternative to the `sid` in the URL path to address the resource.
        :param actions: The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task.
        :param actions_url: The URL from which the Assistant can fetch actions.

        :returns: The updated TaskInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "UniqueName": unique_name,
                "Actions": serialize.object(actions),
                "ActionsUrl": actions_url,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskInstance(
            self._version,
            payload,
            assistant_sid=self._solution["assistant_sid"],
            sid=self._solution["sid"],
        )

    @property
    def fields(self) -> FieldList:
        """
        Access the fields
        """
        if self._fields is None:
            self._fields = FieldList(
                self._version,
                self._solution["assistant_sid"],
                self._solution["sid"],
            )
        return self._fields

    @property
    def samples(self) -> SampleList:
        """
        Access the samples
        """
        if self._samples is None:
            self._samples = SampleList(
                self._version,
                self._solution["assistant_sid"],
                self._solution["sid"],
            )
        return self._samples

    @property
    def task_actions(self) -> TaskActionsList:
        """
        Access the task_actions
        """
        if self._task_actions is None:
            self._task_actions = TaskActionsList(
                self._version,
                self._solution["assistant_sid"],
                self._solution["sid"],
            )
        return self._task_actions

    @property
    def statistics(self) -> TaskStatisticsList:
        """
        Access the statistics
        """
        if self._statistics is None:
            self._statistics = TaskStatisticsList(
                self._version,
                self._solution["assistant_sid"],
                self._solution["sid"],
            )
        return self._statistics

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Autopilot.V1.TaskContext {}>".format(context)


class TaskPage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> TaskInstance:
        """
        Build an instance of TaskInstance

        :param payload: Payload response from the API
        """
        return TaskInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Autopilot.V1.TaskPage>"


class TaskList(ListResource):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the TaskList

        :param version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "assistant_sid": assistant_sid,
        }
        self._uri = "/Assistants/{assistant_sid}/Tasks".format(**self._solution)

    def create(
        self,
        unique_name: str,
        friendly_name: Union[str, object] = values.unset,
        actions: Union[object, object] = values.unset,
        actions_url: Union[str, object] = values.unset,
    ) -> TaskInstance:
        """
        Create the TaskInstance

        :param unique_name: An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the `sid` in the URL path to address the resource. This value must be unique and 64 characters or less in length.
        :param friendly_name: A descriptive string that you create to describe the new resource. It is not unique and can be up to 255 characters long.
        :param actions: The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task. It is optional and not unique.
        :param actions_url: The URL from which the Assistant can fetch actions.

        :returns: The created TaskInstance
        """

        data = values.of(
            {
                "UniqueName": unique_name,
                "FriendlyName": friendly_name,
                "Actions": serialize.object(actions),
                "ActionsUrl": actions_url,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    async def create_async(
        self,
        unique_name: str,
        friendly_name: Union[str, object] = values.unset,
        actions: Union[object, object] = values.unset,
        actions_url: Union[str, object] = values.unset,
    ) -> TaskInstance:
        """
        Asynchronously create the TaskInstance

        :param unique_name: An application-defined string that uniquely identifies the new resource. It can be used as an alternative to the `sid` in the URL path to address the resource. This value must be unique and 64 characters or less in length.
        :param friendly_name: A descriptive string that you create to describe the new resource. It is not unique and can be up to 255 characters long.
        :param actions: The JSON string that specifies the [actions](https://www.twilio.com/docs/autopilot/actions) that instruct the Assistant on how to perform the task. It is optional and not unique.
        :param actions_url: The URL from which the Assistant can fetch actions.

        :returns: The created TaskInstance
        """

        data = values.of(
            {
                "UniqueName": unique_name,
                "FriendlyName": friendly_name,
                "Actions": serialize.object(actions),
                "ActionsUrl": actions_url,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskInstance(
            self._version, payload, assistant_sid=self._solution["assistant_sid"]
        )

    def stream(
        self,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[TaskInstance]:
        """
        Streams TaskInstance records from the API as a generator stream.
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
    ) -> AsyncIterator[TaskInstance]:
        """
        Asynchronously streams TaskInstance records from the API as a generator stream.
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
    ) -> List[TaskInstance]:
        """
        Lists TaskInstance records from the API as a list.
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
    ) -> List[TaskInstance]:
        """
        Asynchronously lists TaskInstance records from the API as a list.
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
    ) -> TaskPage:
        """
        Retrieve a single page of TaskInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of TaskInstance
        """
        data = values.of(
            {
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return TaskPage(self._version, response, self._solution)

    async def page_async(
        self,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> TaskPage:
        """
        Asynchronously retrieve a single page of TaskInstance records from the API.
        Request is executed immediately

        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of TaskInstance
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
        return TaskPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> TaskPage:
        """
        Retrieve a specific page of TaskInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of TaskInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return TaskPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> TaskPage:
        """
        Asynchronously retrieve a specific page of TaskInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of TaskInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return TaskPage(self._version, response, self._solution)

    def get(self, sid: str) -> TaskContext:
        """
        Constructs a TaskContext

        :param sid: The Twilio-provided string that uniquely identifies the Task resource to update.
        """
        return TaskContext(
            self._version, assistant_sid=self._solution["assistant_sid"], sid=sid
        )

    def __call__(self, sid: str) -> TaskContext:
        """
        Constructs a TaskContext

        :param sid: The Twilio-provided string that uniquely identifies the Task resource to update.
        """
        return TaskContext(
            self._version, assistant_sid=self._solution["assistant_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Autopilot.V1.TaskList>"
