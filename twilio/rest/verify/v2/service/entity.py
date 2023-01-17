"""
    This code was generated by
    ___ _ _ _ _ _    _ ____    ____ ____ _    ____ ____ _  _ ____ ____ ____ ___ __   __
    |  | | | | |    | |  | __ |  | |__| | __ | __ |___ |\ | |___ |__/ |__|  | |  | |__/
    |  |_|_| | |___ | |__|    |__| |  | |    |__] |___ | \| |___ |  \ |  |  | |__| |  \

    Twilio - Verify
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

from twilio.rest.entity.challenge import ChallengeListInstancefrom twilio.rest.entity.factor import FactorListInstancefrom twilio.rest.entity.new_factor import NewFactorListInstance


class EntityContext(InstanceContext):
    def __init__(self, version: V2, service_sid: str, identity: str):
        # TODO: needs autogenerated docs
        super(EntityContextList, self).__init__(version)

        # Path Solution
        self._solution = { service_sid, identity,  }
        self._uri = '/Services/${service_sid}/Entities/${identity}'
        
        self._challenges = None
        self._factors = None
        self._new_factors = None
        
        def delete(self):
            
            
            """
            Deletes the EntityInstance

            :returns: True if delete succeeds, False otherwise
            :rtype: bool
            """
            return self._version.delete(method='DELETE', uri=self._uri, )
        
        def fetch(self):
            
            """
            Fetch the EntityInstance

            :returns: The fetched EntityInstance
            #TODO: add rtype docs
            """
            payload = self._version.fetch(method='GET', uri=self._uri, )
            return EntityInstance(
                self._version,
                payload,
                service_sididentity=self._solution['service_sid''identity'],
            )
            
            
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.EntityContext>'



class EntityInstance(InstanceResource):
    def __init__(self, version, payload, service_sid: str, identity: str):
        super(EntityInstance, self).__init__(version)
        self._properties = { 
            'sid' = payload.get('sid'),
            'identity' = payload.get('identity'),
            'account_sid' = payload.get('account_sid'),
            'service_sid' = payload.get('service_sid'),
            'date_created' = payload.get('date_created'),
            'date_updated' = payload.get('date_updated'),
            'url' = payload.get('url'),
            'links' = payload.get('links'),
        }

        self._context = None
        self._solution = {
            'service_sid': service_sid or self._properties['service_sid']'identity': identity or self._properties['identity']
        }

    @property
    def _proxy(self):
        if self._context is None:
            self._context = EntityContext(
                self._version,
                service_sid=self._solution['service_sid'],identity=self._solution['identity'],
            )
        return self._context

    @property
    def challenges(self):
        return self._proxy.challenges
    @property
    def factors(self):
        return self._proxy.factors
    @property
    def new_factors(self):
        return self._proxy.new_factors
    

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Api.V2.EntityInstance {}>'.format(context)



class EntityListInstance(ListResource):
    def __init__(self, version: V2, service_sid: str):
        # TODO: needs autogenerated docs
        super(EntityListInstanceList, self).__init__(version)

        # Path Solution
        self._solution = { service_sid,  }
        self._uri = '/Services/${service_sid}/Entities'
        
        
        def create(self, body):
            data = values.of({
                'body': body,
            })

            payload = self._version.create(method='post', uri=self._uri, data=data, )

            return EntityInstance(self._version, payload, service_sid=self._solution['service_sid'])
            
        
        def page(self, page_size):
            
            data = values.of({
                'page_size': page_size,
            })

            payload = self._version.create(method='get', uri=self._uri, data=data, )

            return EntityPage(self._version, payload, service_sid=self._solution['service_sid'])
        

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2.EntityListInstance>'

