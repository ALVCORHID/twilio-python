r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Api
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
from twilio.rest.api.v2010.account.address.dependent_phone_number import (
    DependentPhoneNumberList,
)


class AddressInstance(InstanceResource):

    """
    :ivar account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource.
    :ivar city: The city in which the address is located.
    :ivar customer_name: The name associated with the address.This property has a maximum length of 16 4-byte characters, or 21 3-byte characters.
    :ivar date_created: The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar date_updated: The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    :ivar friendly_name: The string that you assigned to describe the resource.
    :ivar iso_country: The ISO country code of the address.
    :ivar postal_code: The postal code of the address.
    :ivar region: The state or region of the address.
    :ivar sid: The unique string that that we created to identify the Address resource.
    :ivar street: The number and street address of the address.
    :ivar uri: The URI of the resource, relative to `https://api.twilio.com`.
    :ivar emergency_enabled: Whether emergency calling has been enabled on this number.
    :ivar validated: Whether the address has been validated to comply with local regulation. In countries that require valid addresses, an invalid address will not be accepted. `true` indicates the Address has been validated. `false` indicate the country doesn't require validation or the Address is not valid.
    :ivar verified: Whether the address has been verified to comply with regulation. In countries that require valid addresses, an invalid address will not be accepted. `true` indicates the Address has been verified. `false` indicate the country doesn't require verified or the Address is not valid.
    :ivar street_secondary: The additional number and street address of the address.
    """

    def __init__(
        self,
        version: Version,
        payload: Dict[str, Any],
        account_sid: str,
        sid: Optional[str] = None,
    ):
        super().__init__(version)

        self.account_sid: Optional[str] = payload.get("account_sid")
        self.city: Optional[str] = payload.get("city")
        self.customer_name: Optional[str] = payload.get("customer_name")
        self.date_created: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_created")
        )
        self.date_updated: Optional[datetime] = deserialize.rfc2822_datetime(
            payload.get("date_updated")
        )
        self.friendly_name: Optional[str] = payload.get("friendly_name")
        self.iso_country: Optional[str] = payload.get("iso_country")
        self.postal_code: Optional[str] = payload.get("postal_code")
        self.region: Optional[str] = payload.get("region")
        self.sid: Optional[str] = payload.get("sid")
        self.street: Optional[str] = payload.get("street")
        self.uri: Optional[str] = payload.get("uri")
        self.emergency_enabled: Optional[bool] = payload.get("emergency_enabled")
        self.validated: Optional[bool] = payload.get("validated")
        self.verified: Optional[bool] = payload.get("verified")
        self.street_secondary: Optional[str] = payload.get("street_secondary")

        self._solution = {
            "account_sid": account_sid,
            "sid": sid or self.sid,
        }
        self._context: Optional[AddressContext] = None

    @property
    def _proxy(self) -> "AddressContext":
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: AddressContext for this AddressInstance
        """
        if self._context is None:
            self._context = AddressContext(
                self._version,
                account_sid=self._solution["account_sid"],
                sid=self._solution["sid"],
            )
        return self._context

    def delete(self) -> bool:
        """
        Deletes the AddressInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._proxy.delete()

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AddressInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._proxy.delete_async()

    def fetch(self) -> "AddressInstance":
        """
        Fetch the AddressInstance


        :returns: The fetched AddressInstance
        """
        return self._proxy.fetch()

    async def fetch_async(self) -> "AddressInstance":
        """
        Asynchronous coroutine to fetch the AddressInstance


        :returns: The fetched AddressInstance
        """
        return await self._proxy.fetch_async()

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        customer_name: Union[str, object] = values.unset,
        street: Union[str, object] = values.unset,
        city: Union[str, object] = values.unset,
        region: Union[str, object] = values.unset,
        postal_code: Union[str, object] = values.unset,
        emergency_enabled: Union[bool, object] = values.unset,
        auto_correct_address: Union[bool, object] = values.unset,
        street_secondary: Union[str, object] = values.unset,
    ) -> "AddressInstance":
        """
        Update the AddressInstance

        :param friendly_name: A descriptive string that you create to describe the address. It can be up to 64 characters long.
        :param customer_name: The name to associate with the address.
        :param street: The number and street address of the address.
        :param city: The city of the address.
        :param region: The state or region of the address.
        :param postal_code: The postal code of the address.
        :param emergency_enabled: Whether to enable emergency calling on the address. Can be: `true` or `false`.
        :param auto_correct_address: Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
        :param street_secondary: The additional number and street address of the address.

        :returns: The updated AddressInstance
        """
        return self._proxy.update(
            friendly_name=friendly_name,
            customer_name=customer_name,
            street=street,
            city=city,
            region=region,
            postal_code=postal_code,
            emergency_enabled=emergency_enabled,
            auto_correct_address=auto_correct_address,
            street_secondary=street_secondary,
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        customer_name: Union[str, object] = values.unset,
        street: Union[str, object] = values.unset,
        city: Union[str, object] = values.unset,
        region: Union[str, object] = values.unset,
        postal_code: Union[str, object] = values.unset,
        emergency_enabled: Union[bool, object] = values.unset,
        auto_correct_address: Union[bool, object] = values.unset,
        street_secondary: Union[str, object] = values.unset,
    ) -> "AddressInstance":
        """
        Asynchronous coroutine to update the AddressInstance

        :param friendly_name: A descriptive string that you create to describe the address. It can be up to 64 characters long.
        :param customer_name: The name to associate with the address.
        :param street: The number and street address of the address.
        :param city: The city of the address.
        :param region: The state or region of the address.
        :param postal_code: The postal code of the address.
        :param emergency_enabled: Whether to enable emergency calling on the address. Can be: `true` or `false`.
        :param auto_correct_address: Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
        :param street_secondary: The additional number and street address of the address.

        :returns: The updated AddressInstance
        """
        return await self._proxy.update_async(
            friendly_name=friendly_name,
            customer_name=customer_name,
            street=street,
            city=city,
            region=region,
            postal_code=postal_code,
            emergency_enabled=emergency_enabled,
            auto_correct_address=auto_correct_address,
            street_secondary=street_secondary,
        )

    @property
    def dependent_phone_numbers(self) -> DependentPhoneNumberList:
        """
        Access the dependent_phone_numbers
        """
        return self._proxy.dependent_phone_numbers

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AddressInstance {}>".format(context)


class AddressContext(InstanceContext):
    def __init__(self, version: Version, account_sid: str, sid: str):
        """
        Initialize the AddressContext

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to update.
        :param sid: The Twilio-provided string that uniquely identifies the Address resource to update.
        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
            "sid": sid,
        }
        self._uri = "/Accounts/{account_sid}/Addresses/{sid}.json".format(
            **self._solution
        )

        self._dependent_phone_numbers: Optional[DependentPhoneNumberList] = None

    def delete(self) -> bool:
        """
        Deletes the AddressInstance


        :returns: True if delete succeeds, False otherwise
        """
        return self._version.delete(
            method="DELETE",
            uri=self._uri,
        )

    async def delete_async(self) -> bool:
        """
        Asynchronous coroutine that deletes the AddressInstance


        :returns: True if delete succeeds, False otherwise
        """
        return await self._version.delete_async(
            method="DELETE",
            uri=self._uri,
        )

    def fetch(self) -> AddressInstance:
        """
        Fetch the AddressInstance


        :returns: The fetched AddressInstance
        """

        payload = self._version.fetch(
            method="GET",
            uri=self._uri,
        )

        return AddressInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    async def fetch_async(self) -> AddressInstance:
        """
        Asynchronous coroutine to fetch the AddressInstance


        :returns: The fetched AddressInstance
        """

        payload = await self._version.fetch_async(
            method="GET",
            uri=self._uri,
        )

        return AddressInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    def update(
        self,
        friendly_name: Union[str, object] = values.unset,
        customer_name: Union[str, object] = values.unset,
        street: Union[str, object] = values.unset,
        city: Union[str, object] = values.unset,
        region: Union[str, object] = values.unset,
        postal_code: Union[str, object] = values.unset,
        emergency_enabled: Union[bool, object] = values.unset,
        auto_correct_address: Union[bool, object] = values.unset,
        street_secondary: Union[str, object] = values.unset,
    ) -> AddressInstance:
        """
        Update the AddressInstance

        :param friendly_name: A descriptive string that you create to describe the address. It can be up to 64 characters long.
        :param customer_name: The name to associate with the address.
        :param street: The number and street address of the address.
        :param city: The city of the address.
        :param region: The state or region of the address.
        :param postal_code: The postal code of the address.
        :param emergency_enabled: Whether to enable emergency calling on the address. Can be: `true` or `false`.
        :param auto_correct_address: Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
        :param street_secondary: The additional number and street address of the address.

        :returns: The updated AddressInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "CustomerName": customer_name,
                "Street": street,
                "City": city,
                "Region": region,
                "PostalCode": postal_code,
                "EmergencyEnabled": emergency_enabled,
                "AutoCorrectAddress": auto_correct_address,
                "StreetSecondary": street_secondary,
            }
        )

        payload = self._version.update(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    async def update_async(
        self,
        friendly_name: Union[str, object] = values.unset,
        customer_name: Union[str, object] = values.unset,
        street: Union[str, object] = values.unset,
        city: Union[str, object] = values.unset,
        region: Union[str, object] = values.unset,
        postal_code: Union[str, object] = values.unset,
        emergency_enabled: Union[bool, object] = values.unset,
        auto_correct_address: Union[bool, object] = values.unset,
        street_secondary: Union[str, object] = values.unset,
    ) -> AddressInstance:
        """
        Asynchronous coroutine to update the AddressInstance

        :param friendly_name: A descriptive string that you create to describe the address. It can be up to 64 characters long.
        :param customer_name: The name to associate with the address.
        :param street: The number and street address of the address.
        :param city: The city of the address.
        :param region: The state or region of the address.
        :param postal_code: The postal code of the address.
        :param emergency_enabled: Whether to enable emergency calling on the address. Can be: `true` or `false`.
        :param auto_correct_address: Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
        :param street_secondary: The additional number and street address of the address.

        :returns: The updated AddressInstance
        """
        data = values.of(
            {
                "FriendlyName": friendly_name,
                "CustomerName": customer_name,
                "Street": street,
                "City": city,
                "Region": region,
                "PostalCode": postal_code,
                "EmergencyEnabled": emergency_enabled,
                "AutoCorrectAddress": auto_correct_address,
                "StreetSecondary": street_secondary,
            }
        )

        payload = await self._version.update_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressInstance(
            self._version,
            payload,
            account_sid=self._solution["account_sid"],
            sid=self._solution["sid"],
        )

    @property
    def dependent_phone_numbers(self) -> DependentPhoneNumberList:
        """
        Access the dependent_phone_numbers
        """
        if self._dependent_phone_numbers is None:
            self._dependent_phone_numbers = DependentPhoneNumberList(
                self._version,
                self._solution["account_sid"],
                self._solution["sid"],
            )
        return self._dependent_phone_numbers

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        context = " ".join("{}={}".format(k, v) for k, v in self._solution.items())
        return "<Twilio.Api.V2010.AddressContext {}>".format(context)


class AddressPage(Page):
    def get_instance(self, payload: Dict[str, Any]) -> AddressInstance:
        """
        Build an instance of AddressInstance

        :param payload: Payload response from the API
        """
        return AddressInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AddressPage>"


class AddressList(ListResource):
    def __init__(self, version: Version, account_sid: str):
        """
        Initialize the AddressList

        :param version: Version that contains the resource
        :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that is responsible for the Address resource to read.

        """
        super().__init__(version)

        # Path Solution
        self._solution = {
            "account_sid": account_sid,
        }
        self._uri = "/Accounts/{account_sid}/Addresses.json".format(**self._solution)

    def create(
        self,
        customer_name: str,
        street: str,
        city: str,
        region: str,
        postal_code: str,
        iso_country: str,
        friendly_name: Union[str, object] = values.unset,
        emergency_enabled: Union[bool, object] = values.unset,
        auto_correct_address: Union[bool, object] = values.unset,
        street_secondary: Union[str, object] = values.unset,
    ) -> AddressInstance:
        """
        Create the AddressInstance

        :param customer_name: The name to associate with the new address.
        :param street: The number and street address of the new address.
        :param city: The city of the new address.
        :param region: The state or region of the new address.
        :param postal_code: The postal code of the new address.
        :param iso_country: The ISO country code of the new address.
        :param friendly_name: A descriptive string that you create to describe the new address. It can be up to 64 characters long.
        :param emergency_enabled: Whether to enable emergency calling on the new address. Can be: `true` or `false`.
        :param auto_correct_address: Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
        :param street_secondary: The additional number and street address of the address.

        :returns: The created AddressInstance
        """

        data = values.of(
            {
                "CustomerName": customer_name,
                "Street": street,
                "City": city,
                "Region": region,
                "PostalCode": postal_code,
                "IsoCountry": iso_country,
                "FriendlyName": friendly_name,
                "EmergencyEnabled": emergency_enabled,
                "AutoCorrectAddress": auto_correct_address,
                "StreetSecondary": street_secondary,
            }
        )

        payload = self._version.create(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    async def create_async(
        self,
        customer_name: str,
        street: str,
        city: str,
        region: str,
        postal_code: str,
        iso_country: str,
        friendly_name: Union[str, object] = values.unset,
        emergency_enabled: Union[bool, object] = values.unset,
        auto_correct_address: Union[bool, object] = values.unset,
        street_secondary: Union[str, object] = values.unset,
    ) -> AddressInstance:
        """
        Asynchronously create the AddressInstance

        :param customer_name: The name to associate with the new address.
        :param street: The number and street address of the new address.
        :param city: The city of the new address.
        :param region: The state or region of the new address.
        :param postal_code: The postal code of the new address.
        :param iso_country: The ISO country code of the new address.
        :param friendly_name: A descriptive string that you create to describe the new address. It can be up to 64 characters long.
        :param emergency_enabled: Whether to enable emergency calling on the new address. Can be: `true` or `false`.
        :param auto_correct_address: Whether we should automatically correct the address. Can be: `true` or `false` and the default is `true`. If empty or `true`, we will correct the address you provide if necessary. If `false`, we won't alter the address you provide.
        :param street_secondary: The additional number and street address of the address.

        :returns: The created AddressInstance
        """

        data = values.of(
            {
                "CustomerName": customer_name,
                "Street": street,
                "City": city,
                "Region": region,
                "PostalCode": postal_code,
                "IsoCountry": iso_country,
                "FriendlyName": friendly_name,
                "EmergencyEnabled": emergency_enabled,
                "AutoCorrectAddress": auto_correct_address,
                "StreetSecondary": street_secondary,
            }
        )

        payload = await self._version.create_async(
            method="POST",
            uri=self._uri,
            data=data,
        )

        return AddressInstance(
            self._version, payload, account_sid=self._solution["account_sid"]
        )

    def stream(
        self,
        customer_name: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> Iterator[AddressInstance]:
        """
        Streams AddressInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str customer_name: The `customer_name` of the Address resources to read.
        :param str friendly_name: The string that identifies the Address resources to read.
        :param str iso_country: The ISO country code of the Address resources to read.
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
            customer_name=customer_name,
            friendly_name=friendly_name,
            iso_country=iso_country,
            page_size=limits["page_size"],
        )

        return self._version.stream(page, limits["limit"])

    async def stream_async(
        self,
        customer_name: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> AsyncIterator[AddressInstance]:
        """
        Asynchronously streams AddressInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param str customer_name: The `customer_name` of the Address resources to read.
        :param str friendly_name: The string that identifies the Address resources to read.
        :param str iso_country: The ISO country code of the Address resources to read.
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
            customer_name=customer_name,
            friendly_name=friendly_name,
            iso_country=iso_country,
            page_size=limits["page_size"],
        )

        return self._version.stream_async(page, limits["limit"])

    def list(
        self,
        customer_name: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AddressInstance]:
        """
        Lists AddressInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str customer_name: The `customer_name` of the Address resources to read.
        :param str friendly_name: The string that identifies the Address resources to read.
        :param str iso_country: The ISO country code of the Address resources to read.
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
                customer_name=customer_name,
                friendly_name=friendly_name,
                iso_country=iso_country,
                limit=limit,
                page_size=page_size,
            )
        )

    async def list_async(
        self,
        customer_name: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        limit: Optional[int] = None,
        page_size: Optional[int] = None,
    ) -> List[AddressInstance]:
        """
        Asynchronously lists AddressInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param str customer_name: The `customer_name` of the Address resources to read.
        :param str friendly_name: The string that identifies the Address resources to read.
        :param str iso_country: The ISO country code of the Address resources to read.
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
                customer_name=customer_name,
                friendly_name=friendly_name,
                iso_country=iso_country,
                limit=limit,
                page_size=page_size,
            )
        ]

    def page(
        self,
        customer_name: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AddressPage:
        """
        Retrieve a single page of AddressInstance records from the API.
        Request is executed immediately

        :param customer_name: The `customer_name` of the Address resources to read.
        :param friendly_name: The string that identifies the Address resources to read.
        :param iso_country: The ISO country code of the Address resources to read.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AddressInstance
        """
        data = values.of(
            {
                "CustomerName": customer_name,
                "FriendlyName": friendly_name,
                "IsoCountry": iso_country,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = self._version.page(method="GET", uri=self._uri, params=data)
        return AddressPage(self._version, response, self._solution)

    async def page_async(
        self,
        customer_name: Union[str, object] = values.unset,
        friendly_name: Union[str, object] = values.unset,
        iso_country: Union[str, object] = values.unset,
        page_token: Union[str, object] = values.unset,
        page_number: Union[int, object] = values.unset,
        page_size: Union[int, object] = values.unset,
    ) -> AddressPage:
        """
        Asynchronously retrieve a single page of AddressInstance records from the API.
        Request is executed immediately

        :param customer_name: The `customer_name` of the Address resources to read.
        :param friendly_name: The string that identifies the Address resources to read.
        :param iso_country: The ISO country code of the Address resources to read.
        :param page_token: PageToken provided by the API
        :param page_number: Page Number, this value is simply for client state
        :param page_size: Number of records to return, defaults to 50

        :returns: Page of AddressInstance
        """
        data = values.of(
            {
                "CustomerName": customer_name,
                "FriendlyName": friendly_name,
                "IsoCountry": iso_country,
                "PageToken": page_token,
                "Page": page_number,
                "PageSize": page_size,
            }
        )

        response = await self._version.page_async(
            method="GET", uri=self._uri, params=data
        )
        return AddressPage(self._version, response, self._solution)

    def get_page(self, target_url: str) -> AddressPage:
        """
        Retrieve a specific page of AddressInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AddressInstance
        """
        response = self._version.domain.twilio.request("GET", target_url)
        return AddressPage(self._version, response, self._solution)

    async def get_page_async(self, target_url: str) -> AddressPage:
        """
        Asynchronously retrieve a specific page of AddressInstance records from the API.
        Request is executed immediately

        :param target_url: API-generated URL for the requested results page

        :returns: Page of AddressInstance
        """
        response = await self._version.domain.twilio.request_async("GET", target_url)
        return AddressPage(self._version, response, self._solution)

    def get(self, sid: str) -> AddressContext:
        """
        Constructs a AddressContext

        :param sid: The Twilio-provided string that uniquely identifies the Address resource to update.
        """
        return AddressContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __call__(self, sid: str) -> AddressContext:
        """
        Constructs a AddressContext

        :param sid: The Twilio-provided string that uniquely identifies the Address resource to update.
        """
        return AddressContext(
            self._version, account_sid=self._solution["account_sid"], sid=sid
        )

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Api.V2010.AddressList>"
