r"""
    This code was generated by
   ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Pricing
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""

from typing import Optional


from twilio.base.list_resource import ListResource
from twilio.base.version import Version

from twilio.rest.pricing.v2.voice.country import CountryList
from twilio.rest.pricing.v2.voice.number import NumberList


class VoiceList(ListResource):

    def __init__(self, version: Version):
        """
        Initialize the VoiceList

        :param version: Version that contains the resource

        """
        super().__init__(version)

        self._uri = "/Voice"

        self._countries: Optional[CountryList] = None
        self._numbers: Optional[NumberList] = None

    @property
    def countries(self) -> CountryList:
        """
        Access the countries
        """
        if self._countries is None:
            self._countries = CountryList(self._version)
        return self._countries

    @property
    def numbers(self) -> NumberList:
        """
        Access the numbers
        """
        if self._numbers is None:
            self._numbers = NumberList(self._version)
        return self._numbers

    def __repr__(self) -> str:
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        """
        return "<Twilio.Pricing.V2.VoiceList>"
