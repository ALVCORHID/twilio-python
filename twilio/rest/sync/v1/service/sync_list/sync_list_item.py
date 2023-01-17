"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Sync
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




class SyncListItemContext(InstanceContext):
    def __init__(self, version: V1, service_sid: str, list_sid: str, index: int):
        # TODO: needs autogenerated docs
        super(SyncListItemContextList, self).__init__(version)

        # Path Solution
        self._solution = { service_sid, list_sid, index,  }
        self._uri = '/Services/${service_sid}/Lists/${list_sid}/Items/${index}'
        
        
        def delete(self, if_match):
            
            
            """
            Deletes the SyncListItemInstance

            :returns: True if delete succeeds, False otherwise
            :rtype: bool
            """
            return self._version.delete(method='DELETE', uri=self._uri, )
        
        def fetch(self):
            
            """
            Fetch the SyncListItemInstance

            :returns: The fetched SyncListItemInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return SyncListItemInstance(
                self._version,
                payload,
                service_sidlist_sidindex=self._solution['service_sid''list_sid''index'],
            )
            
            
        
        def update(self, if_match, body):
            data = values.of({
                'if_match': if_match,'body': body,
            })

            payload = self._version.update(method='post', uri=self._uri, data=data, )

            return SyncListItemInstance(self._version, payload, service_sid=self._solution['service_sid'], list_sid=self._solution['list_sid'], index=self._solution['index'], )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.SyncListItemContext>'



class SyncListItemInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, list_sid: str, index: int):
        super(SyncListItemInstance, self).__init__(version)
        self._properties = { 
            'index' = payload.get('index'),
            'account_sid' = payload.get('account_sid'),
            'service_sid' = payload.get('service_sid'),
            'list_sid' = payload.get('list_sid'),
            'url' = payload.get('url'),
            'revision' = payload.get('revision'),
            'data' = payload.get('data'),
            'date_expires' = payload.get('date_expires'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'created_by' = payload.get('created_by'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid']'list_sid': list_sid or self._properties['list_sid']'index': index or self._properties['index']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = SyncListItemContext(
                self._version,
                service_sid=self._solution['service_sid'],list_sid=self._solution['list_sid'],index=self._solution['index'],
            )
        return self._context

    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V1.SyncListItemInstance {}>'.format(context)



class SyncListItemListInstance(ListResource):
    def __init__(self, version: V1, service_sid: str, list_sid: str):
        # TODO: needs autogenerated docs
        super(SyncListItemListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = { service_sid, list_sid,  }
        self._uri = '/Services/${service_sid}/Lists/${list_sid}/Items'
        
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return SyncListItemInstance(self._version, payload, service_sid=self._solution['service_sid']list_sid=self._solution['list_sid'])
            
        
        def page(self, order, _from, bounds, page_size):
            
            data = values.of({
                'order': order,'_from': _from,'bounds': bounds,'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return SyncListItemPage(self._version, payload, service_sid=self._solution['service_sid']list_sid=self._solution['list_sid'])
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V1.SyncListItemListInstance>'

