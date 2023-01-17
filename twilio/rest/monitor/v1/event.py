"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Monitor
    This is the public Twilio REST API.

    NOTE: This class is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
    Do not edit the class manually.
"""


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource

from twilio.base.page import Page




class EventContext(InstanceContext):
    def __init__(self, version: V1, sid: str):
        # TODO: needs autogenerated docs
        super(EventContextList, self).__init__(version)

        # Path Solution
        self._solution = { sid,  }
        self._uri = '/Events/${sid}'
        
        
        def fetch(self):
            
            """
            Fetch the EventInstance

            :returns: The fetched EventInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return EventInstance(
                self._version,
                payload,
                sid=self._solution['sid'],
            )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.EventContext>'



class EventInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super(EventInstance, self).__init__(version)
        self._properties = { 
            'account_sid' = payload.get('account_sid'),
            'actor_sid' = payload.get('actor_sid'),
            'actor_type' = payload.get('actor_type'),
            'description' = payload.get('description'),
            'event_data' = payload.get('event_data'),
            'event_date' = payload.get('event_date'),
            'event_type' = payload.get('event_type'),
            'resource_sid' = payload.get('resource_sid'),
            'resource_type' = payload.get('resource_type'),
            'sid' = payload.get('sid'),
            'source' = payload.get('source'),
            'source_ip_address' = payload.get('source_ip_address'),
            'url' = payload.get('url'),
            'links' = payload.get('links'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = EventContext(
                self._version,
                sid=self._solution['sid'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.EventInstance {}>'.format(context)



class EventListInstance(ListResource):
    def __init__(self, version: V1):
        # TODO: needs autogenerated docs
        super(EventListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/Events'
        
        
        def page(self, actor_sid, event_type, resource_sid, source_ip_address, start_date, end_date, page_size):
            
            data = values.of({
                'actor_sid': actor_sid,'event_type': event_type,'resource_sid': resource_sid,'source_ip_address': source_ip_address,'start_date': start_date,'end_date': end_date,'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return EventPage(self._version, payload, )
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.EventListInstance>'

