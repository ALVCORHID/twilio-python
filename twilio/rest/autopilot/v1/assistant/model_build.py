"""
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


from twilio.base import deserialize
from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.version import Version
from twilio.base.page import Page


class ModelBuildList(ListResource):

    def __init__(self, version: Version, assistant_sid: str):
        """
        Initialize the ModelBuildList

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resources to read.
        
        :returns: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildList
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildList
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 'assistant_sid': assistant_sid,  }
        self._uri = '/Assistants/{assistant_sid}/ModelBuilds'.format(**self._solution)
        
        
    
    
    
    
    def create(self, status_callback=values.unset, unique_name=values.unset):
        """
        Create the ModelBuildInstance

        :param str status_callback: The URL we should call using a POST method to send status information to your application.
        :param str unique_name: An application-defined string that uniquely identifies the new resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the `sid` in the URL path to address the resource.
        
        :returns: The created ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        """
        data = values.of({ 
            'StatusCallback': status_callback,
            'UniqueName': unique_name,
        })
        
        payload = self._version.create(method='POST', uri=self._uri, data=data,)

        return ModelBuildInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'])
    
    
    def stream(self, limit=None, page_size=None):
        """
        Streams ModelBuildInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.
        
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance]
        """
        limits = self._version.read_limits(limit, page_size)
        page = self.page(
            page_size=limits['page_size']
        )

        return self._version.stream(page, limits['limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists ModelBuildInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.
        
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance]
        """
        return list(self.stream(
            limit=limit,
            page_size=page_size,
        ))

    def page(self, page_token=values.unset, page_number=values.unset, page_size=values.unset):
        """
        Retrieve a single page of ModelBuildInstance records from the API.
        Request is executed immediately
        
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildPage
        """
        data = values.of({ 
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data)
        return ModelBuildPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of ModelBuildInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url
        )
        return ModelBuildPage(self._version, response, self._solution)


    def get(self, sid):
        """
        Constructs a ModelBuildContext
        
        :param sid: The Twilio-provided string that uniquely identifies the ModelBuild resource to update.
        
        :returns: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildContext
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildContext
        """
        return ModelBuildContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid)

    def __call__(self, sid):
        """
        Constructs a ModelBuildContext
        
        :param sid: The Twilio-provided string that uniquely identifies the ModelBuild resource to update.
        
        :returns: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildContext
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildContext
        """
        return ModelBuildContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=sid)

    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.ModelBuildList>'










class ModelBuildPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the ModelBuildPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildPage
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildPage
        """
        super().__init__(version, response)

        # Path solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of ModelBuildInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        """
        return ModelBuildInstance(self._version, payload, assistant_sid=self._solution['assistant_sid'])

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Autopilot.V1.ModelBuildPage>'




class ModelBuildContext(InstanceContext):

    def __init__(self, version: Version, assistant_sid: str, sid: str):
        """
        Initialize the ModelBuildContext

        :param Version version: Version that contains the resource
        :param assistant_sid: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource to update.:param sid: The Twilio-provided string that uniquely identifies the ModelBuild resource to update.

        :returns: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildContext
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildContext
        """
        super().__init__(version)

        # Path Solution
        self._solution = { 
            'assistant_sid': assistant_sid,
            'sid': sid,
        }
        self._uri = '/Assistants/{assistant_sid}/ModelBuilds/{sid}'.format(**self._solution)
        
    
    def delete(self):
        """
        Deletes the ModelBuildInstance

        
        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._version.delete(method='DELETE', uri=self._uri,)
        
    def fetch(self):
        """
        Fetch the ModelBuildInstance
        

        :returns: The fetched ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        """
        
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return ModelBuildInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid'],
            
        )
        
    def update(self, unique_name=values.unset):
        """
        Update the ModelBuildInstance
        
        :params str unique_name: An application-defined string that uniquely identifies the resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the `sid` in the URL path to address the resource.

        :returns: The updated ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        """
        data = values.of({ 
            'UniqueName': unique_name,
        })
        

        payload = self._version.update(method='POST', uri=self._uri, data=data,)

        return ModelBuildInstance(
            self._version,
            payload,
            assistant_sid=self._solution['assistant_sid'],
            sid=self._solution['sid']
        )
        
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.ModelBuildContext {}>'.format(context)

class ModelBuildInstance(InstanceResource):

    class ModelBuildStatus(object):
        ENQUEUED = "enqueued"
        BUILDING = "building"
        COMPLETED = "completed"
        FAILED = "failed"
        CANCELED = "canceled"

    def __init__(self, version, payload, assistant_sid: str, sid: str=None):
        """
        Initialize the ModelBuildInstance
        :returns: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        """
        super().__init__(version)

        self._properties = { 
            'account_sid': payload.get('account_sid'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'assistant_sid': payload.get('assistant_sid'),
            'sid': payload.get('sid'),
            'status': payload.get('status'),
            'unique_name': payload.get('unique_name'),
            'url': payload.get('url'),
            'build_duration': deserialize.integer(payload.get('build_duration')),
            'error_code': deserialize.integer(payload.get('error_code')),
        }

        self._context = None
        self._solution = { 'assistant_sid': assistant_sid, 'sid': sid or self._properties['sid'],  }
    
    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions. All instance actions are proxied to the context

        :returns: ModelBuildContext for this ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildContext
        """
        if self._context is None:
            self._context = ModelBuildContext(self._version, assistant_sid=self._solution['assistant_sid'], sid=self._solution['sid'],)
        return self._context
    
    @property
    def account_sid(self):
        """
        :returns: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ModelBuild resource.
        :rtype: str
        """
        return self._properties['account_sid']
    
    @property
    def date_created(self):
        """
        :returns: The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_created']
    
    @property
    def date_updated(self):
        """
        :returns: The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
        :rtype: datetime
        """
        return self._properties['date_updated']
    
    @property
    def assistant_sid(self):
        """
        :returns: The SID of the [Assistant](https://www.twilio.com/docs/autopilot/api/assistant) that is the parent of the resource.
        :rtype: str
        """
        return self._properties['assistant_sid']
    
    @property
    def sid(self):
        """
        :returns: The unique string that we created to identify the ModelBuild resource.
        :rtype: str
        """
        return self._properties['sid']
    
    @property
    def status(self):
        """
        :returns: 
        :rtype: ModelBuildStatus
        """
        return self._properties['status']
    
    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource. It can be used as an alternative to the `sid` in the URL path to address the resource.
        :rtype: str
        """
        return self._properties['unique_name']
    
    @property
    def url(self):
        """
        :returns: The absolute URL of the ModelBuild resource.
        :rtype: str
        """
        return self._properties['url']
    
    @property
    def build_duration(self):
        """
        :returns: The time in seconds it took to build the model.
        :rtype: int
        """
        return self._properties['build_duration']
    
    @property
    def error_code(self):
        """
        :returns: If the `status` for the model build is `failed`, this value is a code to more information about the failure. This value will be null for all other statuses. See [error code dictionary](https://www.twilio.com/docs/api/errors) for a description of the error.
        :rtype: int
        """
        return self._properties['error_code']
    
    def delete(self):
        """
        Deletes the ModelBuildInstance
        

        :returns: True if delete succeeds, False otherwise
        :rtype: bool
        """
        return self._proxy.delete()
    
    def fetch(self):
        """
        Fetch the ModelBuildInstance
        

        :returns: The fetched ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        """
        return self._proxy.fetch()
    
    def update(self, unique_name=values.unset):
        """
        Update the ModelBuildInstance
        
        :params str unique_name: An application-defined string that uniquely identifies the resource. This value must be a unique string of no more than 64 characters. It can be used as an alternative to the `sid` in the URL path to address the resource.

        :returns: The updated ModelBuildInstance
        :rtype: twilio.rest.autopilot.v1.assistant.model_build.ModelBuildInstance
        """
        return self._proxy.update(unique_name=unique_name, )
    
    def __repr__(self):
        """
        Provide a friendly representation
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Autopilot.V1.ModelBuildInstance {}>'.format(context)


