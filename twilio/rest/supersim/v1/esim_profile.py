"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Supersim
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




class EsimProfileContext(InstanceContext):
    def __init__(self, version: V1, sid: str):
        # TODO: needs autogenerated docs
        super(EsimProfileContextList, self).__init__(version)

        # Path Solution
        self._solution = { sid,  }
        self._uri = '/ESimProfiles/${sid}'
        
        
        def fetch(self):
            
            """
            Fetch the EsimProfileInstance

            :returns: The fetched EsimProfileInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return EsimProfileInstance(
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
        return '<Twilio.Api.V1.EsimProfileContext>'



class EsimProfileInstance(InstanceResource):
    def __init__(self, version, payload, sid: str):
        super(EsimProfileInstance, self).__init__(version)
        self._properties = { 
            'sid' = payload.get('sid'),
            'account_sid' = payload.get('account_sid'),
            'iccid' = payload.get('iccid'),
            'sim_sid' = payload.get('sim_sid'),
            'status' = payload.get('status'),
            'eid' = payload.get('eid'),
            'smdp_plus_address' = payload.get('smdp_plus_address'),
            'error_code' = payload.get('error_code'),
            'error_message' = payload.get('error_message'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'url' = payload.get('url'),
        }

        self._context = None
        self._solution = {
            'sid': sid or self._properties['sid']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = EsimProfileContext(
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
        return '<Twilio.Api.V1.EsimProfileInstance {}>'.format(context)



class EsimProfileListInstance(ListResource):
    def __init__(self, version: V1):
        # TODO: needs autogenerated docs
        super(EsimProfileListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = {  }
        self._uri = '/ESimProfiles'
        
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return EsimProfileInstance(self._version, payload, )
            
        
        def page(self, eid, sim_sid, status, page_size):
            
            data = values.of({
                'eid': eid,'sim_sid': sim_sid,'status': status,'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return EsimProfilePage(self._version, payload, )
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.EsimProfileListInstance>'

