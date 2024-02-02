r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Taskrouter
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
from twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_cumulative_statistics import (
    TaskQueueCumulativeStatisticsList,
)
from twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_real_time_statistics import (
    TaskQueueRealTimeStatisticsList,
)
from twilio.rest.taskrouter.v1.workspace.task_queue.task_queue_statistics import (
    TaskQueueStatisticsList,
)
from twilio.rest.taskrouter.v1.workspace.task_queue.task_queues_statistics import (
    TaskQueuesStatisticsList,
)


class TaskQueueInstance(InstanceResource):

    class TaskOrder(object):
        FIFO = "FIFO"
        LIFO = "LIFO"

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the TaskQueue resource.
    :ivar assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned for them.
    :ivar assignment_activity_name: The name of the Activity to assign Workers when a task is assigned for them.
    :ivar date_created: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar max_reserved_workers: The maximum number of Workers to reserve for the assignment of a task in the queue. Can be an integer between 1 and 50, inclusive and defaults to 1.
    :ivar reservation_activity_sid: The SID of the Activity to assign Workers once a task is reserved for them.
    :ivar reservation_activity_name: The name of the Activity to assign Workers once a task is reserved for them.
    :ivar sid: The unique string that we created to identify the TaskQueue resource.
    :ivar target_workers: A string describing the Worker selection criteria for any Tasks that enter the TaskQueue. For example `'\"language\" == \"spanish\"'` If no TargetWorkers parameter is provided, Tasks will wait in the TaskQueue until they are either deleted or moved to another TaskQueue. Additional examples on how to describing Worker selection criteria below. Defaults to 1==1.
    :ivar task_order: 
    :ivar url: The absolute URL of the TaskQueue resource.
    :ivar workspace_sid: The SID of the Workspace that contains the TaskQueue.
    :ivar links: The URLs of related resources.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        workspace_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.assignment_activity_sid: Optional[str] = payload.get(
            "assignment_activity_sid"
        )
        self.assignment_activity_name: Optional[str] = payload.get(
            "assignment_activity_name"
        )
        self.date_created: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.iso8601_datetime(
            payload.get("date_updated")
        )
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.max_reserved_workers: Optional[int] = deserialize.integer(
            payload.get("max_reserved_workers")
        )
        self.reservation_activity_sid: Optional[str] = payload.get(
            "reservation_activity_sid"
        )
        self.reservation_activity_name: Optional[str] = payload.get(
            "reservation_activity_name"
        )
        self.sid: Optional[str] = payload.get("sid")
        self.target_workers: Optional[str] = payload.get("target_workers")
        self.task_order: Optional["TaskQueueInstance.TaskOrder"] = payload.get(
            "task_order"
        )
        self.url: Optional[str] = payload.get("url")
        self.workspace_sid: Optional[str] = payload.get("workspace_sid")
        self.links: Optional[Dict[str, object]] = payload.get("links")

        self._solution = {
            "workspace_sid": workspace_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[TaskQueueContext] = None

    @property
    def _proxy(self) -> "TaskQueueContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: TaskQueueContext for this TaskQueueInstance
        """
        if self._context is None:
            self._context = TaskQueueContext(
                self._version,
                workspace_sid=self._solution["workspace_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the TaskQueueInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the TaskQueueInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "TaskQueueInstance":
        """
        Fetch the TaskQueueInstance


        :returns: The fetched TaskQueueInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "TaskQueueInstance":
        """
        Asynchronous coroutine to fetch the TaskQueueInstance


        :returns: The fetched TaskQueueInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        target_workers: Union[str, object] = values.unset,
        reservation_activity_sid: Union[str, object] = values.unset,
        assignment_activity_sid: Union[str, object] = values.unset,
        max_reserved_workers: Union[int, object] = values.unset,
        task_order: Union["TaskQueueInstance.TaskOrder", object] = values.unset,
    ) -> "TaskQueueInstance":
        """
        Update the TaskQueueInstance

        :param friendly_name: A descriptive string that you create to describe the TaskQueue. For example `Support-Tier 1`, `Sales`, or `Escalation`.
        :param target_workers: A string describing the Worker selection criteria for any Tasks that enter the TaskQueue. For example '\\\"language\\\" == \\\"spanish\\\"' If no TargetWorkers parameter is provided, Tasks will wait in the queue until they are either deleted or moved to another queue. Additional examples on how to describing Worker selection criteria below.
        :param reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
        :param assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned for them.
        :param max_reserved_workers: The maximum number of Workers to create reservations for the assignment of a task while in the queue. Maximum of 50.
        :param task_order:

        :returns: The updated TaskQueueInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            target_workers=target_workers,
            reservation_activity_sid=reservation_activity_sid,
            assignment_activity_sid=assignment_activity_sid,
            max_reserved_workers=max_reserved_workers,
            task_order=task_order,
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        target_workers: Union[str, object] = values.unset,
        reservation_activity_sid: Union[str, object] = values.unset,
        assignment_activity_sid: Union[str, object] = values.unset,
        max_reserved_workers: Union[int, object] = values.unset,
        task_order: Union["TaskQueueInstance.TaskOrder", object] = values.unset,
    ) -> "TaskQueueInstance":
        """
        Asynchronous coroutine to update the TaskQueueInstance

        :param friendly_name: A descriptive string that you create to describe the TaskQueue. For example `Support-Tier 1`, `Sales`, or `Escalation`.
        :param target_workers: A string describing the Worker selection criteria for any Tasks that enter the TaskQueue. For example '\\\"language\\\" == \\\"spanish\\\"' If no TargetWorkers parameter is provided, Tasks will wait in the queue until they are either deleted or moved to another queue. Additional examples on how to describing Worker selection criteria below.
        :param reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
        :param assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned for them.
        :param max_reserved_workers: The maximum number of Workers to create reservations for the assignment of a task while in the queue. Maximum of 50.
        :param task_order:

        :returns: The updated TaskQueueInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            target_workers=target_workers,
            reservation_activity_sid=reservation_activity_sid,
            assignment_activity_sid=assignment_activity_sid,
            max_reserved_workers=max_reserved_workers,
            task_order=task_order,
        )

    @property
    def cumulative_statistics(self) -> TaskQueueCumulativeStatisticsList:
        """
        Access the cumulative_statistics
        """
        return self._proxy.cumulative_statistics

    @property
    def real_time_statistics(self) -> TaskQueueRealTimeStatisticsList:
        """
        Access the real_time_statistics
        """
        return self._proxy.real_time_statistics

    @property
    def statistics(self) -> TaskQueueStatisticsList:
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
        return "<Twilio.Taskrouter.V1.TaskQueueInstance {}>".format(context)


class TaskQueueContext(InstanceContext):

    def __init__(self, version: Version, workspace_sid: str, sid: str):
        """
        Initialize the TaskQueueContext

        :param version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the TaskQueue to update.
        :param sid: The SID of the TaskQueue resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
            "sid": sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/TaskQueues/{sid}".format(
            **self._solution
        )

        self._cumulative_statistics: Optional[TaskQueueCumulativeStatisticsList] = None
        self._real_time_statistics: Optional[TaskQueueRealTimeStatisticsList] = None
        self._statistics: Optional[TaskQueueStatisticsList] = None

    def delete(self) -> bool:
        """
        Deletes the TaskQueueInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the TaskQueueInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> TaskQueueInstance:
        """
        Fetch the TaskQueueInstance


        :returns: The fetched TaskQueueInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return TaskQueueInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> TaskQueueInstance:
        """
        Asynchronous coroutine to fetch the TaskQueueInstance


        :returns: The fetched TaskQueueInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return TaskQueueInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        target_workers: Union[str, object] = values.unset,
        reservation_activity_sid: Union[str, object] = values.unset,
        assignment_activity_sid: Union[str, object] = values.unset,
        max_reserved_workers: Union[int, object] = values.unset,
        task_order: Union["TaskQueueInstance.TaskOrder", object] = values.unset,
    ) -> TaskQueueInstance:
        """
        Update the TaskQueueInstance

        :param friendly_name: A descriptive string that you create to describe the TaskQueue. For example `Support-Tier 1`, `Sales`, or `Escalation`.
        :param target_workers: A string describing the Worker selection criteria for any Tasks that enter the TaskQueue. For example '\\\"language\\\" == \\\"spanish\\\"' If no TargetWorkers parameter is provided, Tasks will wait in the queue until they are either deleted or moved to another queue. Additional examples on how to describing Worker selection criteria below.
        :param reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
        :param assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned for them.
        :param max_reserved_workers: The maximum number of Workers to create reservations for the assignment of a task while in the queue. Maximum of 50.
        :param task_order:

        :returns: The updated TaskQueueInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "TargetWorkers": target_workers,
                "ReservationActivitySid": reservation_activity_sid,
                "AssignmentActivitySid": assignment_activity_sid,
                "MaxReservedWorkers": max_reserved_workers,
                "TaskOrder": task_order,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskQueueInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        target_workers: Union[str, object] = values.unset,
        reservation_activity_sid: Union[str, object] = values.unset,
        assignment_activity_sid: Union[str, object] = values.unset,
        max_reserved_workers: Union[int, object] = values.unset,
        task_order: Union["TaskQueueInstance.TaskOrder", object] = values.unset,
    ) -> TaskQueueInstance:
        """
        Asynchronous coroutine to update the TaskQueueInstance

        :param friendly_name: A descriptive string that you create to describe the TaskQueue. For example `Support-Tier 1`, `Sales`, or `Escalation`.
        :param target_workers: A string describing the Worker selection criteria for any Tasks that enter the TaskQueue. For example '\\\"language\\\" == \\\"spanish\\\"' If no TargetWorkers parameter is provided, Tasks will wait in the queue until they are either deleted or moved to another queue. Additional examples on how to describing Worker selection criteria below.
        :param reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
        :param assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned for them.
        :param max_reserved_workers: The maximum number of Workers to create reservations for the assignment of a task while in the queue. Maximum of 50.
        :param task_order:

        :returns: The updated TaskQueueInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "TargetWorkers": target_workers,
                "ReservationActivitySid": reservation_activity_sid,
                "AssignmentActivitySid": assignment_activity_sid,
                "MaxReservedWorkers": max_reserved_workers,
                "TaskOrder": task_order,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskQueueInstance(
            self._version,
            payload,
            workspace_sid=self._solution["workspace_sid"],
            sid=self._solution["sid"],
        )

    @property
    def cumulative_statistics(self) -> TaskQueueCumulativeStatisticsList:
        """
        Access the cumulative_statistics
        """
        if self._cumulative_statistics is None:
            self._cumulative_statistics = TaskQueueCumulativeStatisticsList(
                self._version,
                self._solution["workspace_sid"],
                self._solution["sid"],
            )
        return self._cumulative_statistics

    @property
    def real_time_statistics(self) -> TaskQueueRealTimeStatisticsList:
        """
        Access the real_time_statistics
        """
        if self._real_time_statistics is None:
            self._real_time_statistics = TaskQueueRealTimeStatisticsList(
                self._version,
                self._solution["workspace_sid"],
                self._solution["sid"],
            )
        return self._real_time_statistics

    @property
    def statistics(self) -> TaskQueueStatisticsList:
        """
        Access the statistics
        """
        if self._statistics is None:
            self._statistics = TaskQueueStatisticsList(
                self._version,
                self._solution["workspace_sid"],
                self._solution["sid"],
            )
        return self._statistics

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Taskrouter.V1.TaskQueueContext {}>".format(context)


class TaskQueuePage(Page):

    def get_instance(self, payload: Dict[str, Any]) -> TaskQueueInstance:
        """
        Build an instance of TaskQueueInstance

        :param payload: Payload response from the API
        """
        return TaskQueueInstance(
            self._version, payload, workspace_sid=self._solution["workspace_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Taskrouter.V1.TaskQueuePage>"


class TaskQueueList(ListResource):

    def __init__(self, version: Version, workspace_sid: str):
        """
        Initialize the TaskQueueList

        :param version: Version that contains the resource
        :param workspace_sid: The SID of the Workspace with the TaskQueue to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "workspace_sid": workspace_sid,
        }
        self._uri = "/Workspaces/{workspace_sid}/TaskQueues".format(**self._solution)

        self._statistics: Optional[TaskQueuesStatisticsList] = None

    def create(
        self,
        friendly_name: str,
        target_workers: Union[str, object] = values.unset,
        max_reserved_workers: Union[int, object] = values.unset,
        task_order: Union["TaskQueueInstance.TaskOrder", object] = values.unset,
        reservation_activity_sid: Union[str, object] = values.unset,
        assignment_activity_sid: Union[str, object] = values.unset,
    ) -> TaskQueueInstance:
        """
        Create the TaskQueueInstance

        :param friendly_name: A descriptive string that you create to describe the TaskQueue. For example `Support-Tier 1`, `Sales`, or `Escalation`.
        :param target_workers: A string that describes the Worker selection criteria for any Tasks that enter the TaskQueue. For example, `'\\\"language\\\" == \\\"spanish\\\"'`. The default value is `1==1`. If this value is empty, Tasks will wait in the TaskQueue until they are deleted or moved to another TaskQueue. For more information about Worker selection, see [Describing Worker selection criteria](https://www.twilio.com/docs/taskrouter/api/taskqueues#target-workers).
        :param max_reserved_workers: The maximum number of Workers to reserve for the assignment of a Task in the queue. Can be an integer between 1 and 50, inclusive and defaults to 1.
        :param task_order:
        :param reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
        :param assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned to them.

        :returns: The created TaskQueueInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "TargetWorkers": target_workers,
                "MaxReservedWorkers": max_reserved_workers,
                "TaskOrder": task_order,
                "ReservationActivitySid": reservation_activity_sid,
                "AssignmentActivitySid": assignment_activity_sid,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskQueueInstance(
            self._version, payload, workspace_sid=self._solution["workspace_sid"]
        )

    async def create_async(
        self,
        friendly_name: str,
        target_workers: Union[str, object] = values.unset,
        max_reserved_workers: Union[int, object] = values.unset,
        task_order: Union["TaskQueueInstance.TaskOrder", object] = values.unset,
        reservation_activity_sid: Union[str, object] = values.unset,
        assignment_activity_sid: Union[str, object] = values.unset,
    ) -> TaskQueueInstance:
        """
        Asynchronously create the TaskQueueInstance

        :param friendly_name: A descriptive string that you create to describe the TaskQueue. For example `Support-Tier 1`, `Sales`, or `Escalation`.
        :param target_workers: A string that describes the Worker selection criteria for any Tasks that enter the TaskQueue. For example, `'\\\"language\\\" == \\\"spanish\\\"'`. The default value is `1==1`. If this value is empty, Tasks will wait in the TaskQueue until they are deleted or moved to another TaskQueue. For more information about Worker selection, see [Describing Worker selection criteria](https://www.twilio.com/docs/taskrouter/api/taskqueues#target-workers).
        :param max_reserved_workers: The maximum number of Workers to reserve for the assignment of a Task in the queue. Can be an integer between 1 and 50, inclusive and defaults to 1.
        :param task_order:
        :param reservation_activity_sid: The SID of the Activity to assign Workers when a task is reserved for them.
        :param assignment_activity_sid: The SID of the Activity to assign Workers when a task is assigned to them.

        :returns: The created TaskQueueInstance
        """

        data = values.of(
            {
                "FriendlyName": friendly_name,
                "TargetWorkers": target_workers,
                "MaxReservedWorkers": max_reserved_workers,
                "TaskOrder": task_order,
                "ReservationActivitySid": reservation_activity_sid,
                "AssignmentActivitySid": assignment_activity_sid,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return TaskQueueInstance(
            self._version, payload, workspace_sid=self._solution["workspace_sid"]
        )

    def stream(
        self,
        friendly_name: Union[str, object] = values.unset,
        evaluate_worker_attributes: Union[str, object] = values.unset,
        worker_sid: Union[str, object] = values.unset,
        ordering: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[TaskQueueInstance]:
        """
        Streams TaskQueueInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str friendly_name: The `friendly_name` of the TaskQueue resources to read.
        :param str evaluate_worker_attributes: The attributes of the Workers to read. Returns the TaskQueues with Workers that match the attributes specified in this parameter.
        :param str worker_sid: The SID of the Worker with the TaskQueue resources to read.
        :param str ordering: Sorting parameter for TaskQueues
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            friendly_name=friendly_name,
            evaluate_worker_attributes=evaluate_worker_attributes,
            worker_sid=worker_sid,
            ordering=ordering,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        evaluate_worker_attributes: Union[str, object] = values.unset,
        worker_sid: Union[str, object] = values.unset,
        ordering: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[TaskQueueInstance]:
        """
        Asynchronously streams TaskQueueInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str friendly_name: The `friendly_name` of the TaskQueue resources to read.
        :param str evaluate_worker_attributes: The attributes of the Workers to read. Returns the TaskQueues with Workers that match the attributes specified in this parameter.
        :param str worker_sid: The SID of the Worker with the TaskQueue resources to read.
        :param str ordering: Sorting parameter for TaskQueues
        :param limit: Upper limit for the number of records to return. stream()
                      guarantees to never return more than limit.  Default is no limit
        :param page_size: Number of records to fetch per request, when not set will use
                          the default value of 50 records.  If no page_size is defined
                          but a limit is defined, stream() will attempt to read the
                          limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        """
        limits = self._version.read_limits(limit, page_size)
        page = await self.page_async(
            friendly_name=friendly_name,
            evaluate_worker_attributes=evaluate_worker_attributes,
            worker_sid=worker_sid,
            ordering=ordering,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        friendly_name: Union[str, object] = values.unset,
        evaluate_worker_attributes: Union[str, object] = values.unset,
        worker_sid: Union[str, object] = values.unset,
        ordering: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[TaskQueueInstance]:
        """
        Lists TaskQueueInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str friendly_name: The `friendly_name` of the TaskQueue resources to read.
        :param str evaluate_worker_attributes: The attributes of the Workers to read. Returns the TaskQueues with Workers that match the attributes specified in this parameter.
        :param str worker_sid: The SID of the Worker with the TaskQueue resources to read.
        :param str ordering: Sorting parameter for TaskQueues
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
                friendly_name=friendly_name,
                evaluate_worker_attributes=evaluate_worker_attributes,
                worker_sid=worker_sid,
                ordering=ordering,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        evaluate_worker_attributes: Union[str, object] = values.unset,
        worker_sid: Union[str, object] = values.unset,
        ordering: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[TaskQueueInstance]:
        """
        Asynchronously lists TaskQueueInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str friendly_name: The `friendly_name` of the TaskQueue resources to read.
        :param str evaluate_worker_attributes: The attributes of the Workers to read. Returns the TaskQueues with Workers that match the attributes specified in this parameter.
        :param str worker_sid: The SID of the Worker with the TaskQueue resources to read.
        :param str ordering: Sorting parameter for TaskQueues
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
                friendly_name=friendly_name,
                evaluate_worker_attributes=evaluate_worker_attributes,
                worker_sid=worker_sid,
                ordering=ordering,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        friendly_name: Union[str, object] = values.unset,
        evaluate_worker_attributes: Union[str, object] = values.unset,
        worker_sid: Union[str, object] = values.unset,
        ordering: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> TaskQueuePage:
        """
        Retrieve a single page of TaskQueueInstance records from the API.
        Request is executed immediately

        :param friendly_name: The `friendly_name` of the TaskQueue resources to read.
        :param evaluate_worker_attributes: The attributes of the Workers to read. Returns the TaskQueues with Workers that match the attributes specified in this parameter.
        :param worker_sid: The SID of the Worker with the TaskQueue resources to read.
        :param ordering: Sorting parameter for TaskQueues
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of TaskQueueInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "EvaluateWorkerAttributes": evaluate_worker_attributes,
                "WorkerSid": worker_sid,
                "Ordering": ordering,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return TaskQueuePage(self._version, response, self._solution)

    async def page_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        evaluate_worker_attributes: Union[str, object] = values.unset,
        worker_sid: Union[str, object] = values.unset,
        ordering: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> TaskQueuePage:
        """
        Asynchronously retrieve a single page of TaskQueueInstance records from the API.
        Request is executed immediately

        :param friendly_name: The `friendly_name` of the TaskQueue resources to read.
        :param evaluate_worker_attributes: The attributes of the Workers to read. Returns the TaskQueues with Workers that match the attributes specified in this parameter.
        :param worker_sid: The SID of the Worker with the TaskQueue resources to read.
        :param ordering: Sorting parameter for TaskQueues
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of TaskQueueInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "EvaluateWorkerAttributes": evaluate_worker_attributes,
                "WorkerSid": worker_sid,
                "Ordering": ordering,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return TaskQueuePage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> TaskQueuePage:
        """
        Retrieve a specific page of TaskQueueInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of TaskQueueInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return TaskQueuePage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> TaskQueuePage:
        """
        Asynchronously retrieve a specific page of TaskQueueInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of TaskQueueInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return TaskQueuePage(self._version, response, self._solution)

    @property
    def statistics(self) -> TaskQueuesStatisticsList:
        """
        Access the statistics
        """
        if self._statistics is None:
            self._statistics = TaskQueuesStatisticsList(
                self._version, workspace_sid=self._solution["workspace_sid"]
            )
        return self._statistics

    def get(self, sid: str) -> TaskQueueContext:
        """
        Constructs a TaskQueueContext

        :param sid: The SID of the TaskQueue resource to update.
        """
        return TaskQueueContext(
            self._version, workspace_sid=self._solution["workspace_sid"], sid=sid
        )

    def __call__(self, sid: str) -> TaskQueueContext:
        """
        Constructs a TaskQueueContext

        :param sid: The SID of the TaskQueue resource to update.
        """
        return TaskQueueContext(
            self._version, workspace_sid=self._solution["workspace_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Taskrouter.V1.TaskQueueList>"
