# h1.ComputeProjectReplicaApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compute_project_replica_create**](ComputeProjectReplicaApi.md#compute_project_replica_create) | **POST** /compute/{locationId}/project/{projectId}/replica | Create compute/replica
[**compute_project_replica_delete**](ComputeProjectReplicaApi.md#compute_project_replica_delete) | **DELETE** /compute/{locationId}/project/{projectId}/replica/{replicaId} | Delete compute/replica
[**compute_project_replica_event_get**](ComputeProjectReplicaApi.md#compute_project_replica_event_get) | **GET** /compute/{locationId}/project/{projectId}/replica/{replicaId}/event/{eventId} | Get compute/replica.event
[**compute_project_replica_event_list**](ComputeProjectReplicaApi.md#compute_project_replica_event_list) | **GET** /compute/{locationId}/project/{projectId}/replica/{replicaId}/event | List compute/replica.event
[**compute_project_replica_get**](ComputeProjectReplicaApi.md#compute_project_replica_get) | **GET** /compute/{locationId}/project/{projectId}/replica/{replicaId} | Get compute/replica
[**compute_project_replica_list**](ComputeProjectReplicaApi.md#compute_project_replica_list) | **GET** /compute/{locationId}/project/{projectId}/replica | List compute/replica
[**compute_project_replica_service_get**](ComputeProjectReplicaApi.md#compute_project_replica_service_get) | **GET** /compute/{locationId}/project/{projectId}/replica/{replicaId}/service/{serviceId} | Get compute/replica.service
[**compute_project_replica_service_list**](ComputeProjectReplicaApi.md#compute_project_replica_service_list) | **GET** /compute/{locationId}/project/{projectId}/replica/{replicaId}/service | List compute/replica.service
[**compute_project_replica_tag_create**](ComputeProjectReplicaApi.md#compute_project_replica_tag_create) | **POST** /compute/{locationId}/project/{projectId}/replica/{replicaId}/tag | Create compute/replica.tag
[**compute_project_replica_tag_delete**](ComputeProjectReplicaApi.md#compute_project_replica_tag_delete) | **DELETE** /compute/{locationId}/project/{projectId}/replica/{replicaId}/tag/{tagId} | Delete compute/replica.tag
[**compute_project_replica_tag_get**](ComputeProjectReplicaApi.md#compute_project_replica_tag_get) | **GET** /compute/{locationId}/project/{projectId}/replica/{replicaId}/tag/{tagId} | Get compute/replica.tag
[**compute_project_replica_tag_list**](ComputeProjectReplicaApi.md#compute_project_replica_tag_list) | **GET** /compute/{locationId}/project/{projectId}/replica/{replicaId}/tag | List compute/replica.tag
[**compute_project_replica_tag_put**](ComputeProjectReplicaApi.md#compute_project_replica_tag_put) | **PUT** /compute/{locationId}/project/{projectId}/replica/{replicaId}/tag | Replace compute/replica.tag


# **compute_project_replica_create**
> Replica compute_project_replica_create(project_id, location_id, compute_project_replica_create)

Create compute/replica

Create replica

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_replica_api
from h1.model.compute_project_replica_create import ComputeProjectReplicaCreate
from h1.model.inline_response400 import InlineResponse400
from h1.model.replica import Replica
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_project_replica_api.ComputeProjectReplicaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    compute_project_replica_create = ComputeProjectReplicaCreate(
        hostname="hostname_example",
        secret="secret_example",
    ) # ComputeProjectReplicaCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create compute/replica
        api_response = api_instance.compute_project_replica_create(project_id, location_id, compute_project_replica_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create compute/replica
        api_response = api_instance.compute_project_replica_create(project_id, location_id, compute_project_replica_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **compute_project_replica_create** | [**ComputeProjectReplicaCreate**](ComputeProjectReplicaCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Replica**](Replica.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**202** | operation queued |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_project_replica_delete**
> compute_project_replica_delete(project_id, location_id, replica_id)

Delete compute/replica

Delete replica

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_replica_api
from h1.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_project_replica_api.ComputeProjectReplicaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    replica_id = "replicaId_example" # str | Replica Id

    # example passing only required values which don't have defaults set
    try:
        # Delete compute/replica
        api_instance.compute_project_replica_delete(project_id, location_id, replica_id)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **replica_id** | **str**| Replica Id |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_project_replica_event_get**
> Event compute_project_replica_event_get(project_id, location_id, replica_id, event_id)

Get compute/replica.event

Get compute/replica.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_replica_api
from h1.model.event import Event
from h1.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_project_replica_api.ComputeProjectReplicaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    replica_id = "replicaId_example" # str | Replica Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get compute/replica.event
        api_response = api_instance.compute_project_replica_event_get(project_id, location_id, replica_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **replica_id** | **str**| Replica Id |
 **event_id** | **str**| eventId |

### Return type

[**Event**](Event.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_project_replica_event_list**
> [Event] compute_project_replica_event_list(project_id, location_id, replica_id)

List compute/replica.event

List compute/replica.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_replica_api
from h1.model.event import Event
from h1.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_project_replica_api.ComputeProjectReplicaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    replica_id = "replicaId_example" # str | Replica Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List compute/replica.event
        api_response = api_instance.compute_project_replica_event_list(project_id, location_id, replica_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List compute/replica.event
        api_response = api_instance.compute_project_replica_event_list(project_id, location_id, replica_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **replica_id** | **str**| Replica Id |
 **limit** | **float**| $limit | [optional] if omitted the server will use the default value of 100
 **skip** | **float**| $skip | [optional]

### Return type

[**[Event]**](Event.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_project_replica_get**
> Replica compute_project_replica_get(project_id, location_id, replica_id)

Get compute/replica

Returns a single replica

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_replica_api
from h1.model.inline_response400 import InlineResponse400
from h1.model.replica import Replica
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_project_replica_api.ComputeProjectReplicaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    replica_id = "replicaId_example" # str | Replica Id

    # example passing only required values which don't have defaults set
    try:
        # Get compute/replica
        api_response = api_instance.compute_project_replica_get(project_id, location_id, replica_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **replica_id** | **str**| Replica Id |

### Return type

[**Replica**](Replica.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_project_replica_list**
> [Replica] compute_project_replica_list(project_id, location_id)

List compute/replica

List replica

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_replica_api
from h1.model.inline_response400 import InlineResponse400
from h1.model.replica import Replica
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_project_replica_api.ComputeProjectReplicaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    name = "name_example" # str | Filter by name (optional)

    # example passing only required values which don't have defaults set
    try:
        # List compute/replica
        api_response = api_instance.compute_project_replica_list(project_id, location_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List compute/replica
        api_response = api_instance.compute_project_replica_list(project_id, location_id, name=name)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **name** | **str**| Filter by name | [optional]

### Return type

[**[Replica]**](Replica.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_project_replica_service_get**
> ResourceService compute_project_replica_service_get(project_id, location_id, replica_id, service_id)

Get compute/replica.service

Get compute/replica.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_replica_api
from h1.model.resource_service import ResourceService
from h1.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_project_replica_api.ComputeProjectReplicaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    replica_id = "replicaId_example" # str | Replica Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get compute/replica.service
        api_response = api_instance.compute_project_replica_service_get(project_id, location_id, replica_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **replica_id** | **str**| Replica Id |
 **service_id** | **str**| serviceId |

### Return type

[**ResourceService**](ResourceService.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_project_replica_service_list**
> [ResourceService] compute_project_replica_service_list(project_id, location_id, replica_id)

List compute/replica.service

List compute/replica.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_replica_api
from h1.model.resource_service import ResourceService
from h1.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_project_replica_api.ComputeProjectReplicaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    replica_id = "replicaId_example" # str | Replica Id

    # example passing only required values which don't have defaults set
    try:
        # List compute/replica.service
        api_response = api_instance.compute_project_replica_service_list(project_id, location_id, replica_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **replica_id** | **str**| Replica Id |

### Return type

[**[ResourceService]**](ResourceService.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_project_replica_tag_create**
> Tag compute_project_replica_tag_create(project_id, location_id, replica_id, tag)

Create compute/replica.tag

Create compute/replica.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_replica_api
from h1.model.tag import Tag
from h1.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_project_replica_api.ComputeProjectReplicaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    replica_id = "replicaId_example" # str | Replica Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create compute/replica.tag
        api_response = api_instance.compute_project_replica_tag_create(project_id, location_id, replica_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **replica_id** | **str**| Replica Id |
 **tag** | [**Tag**](Tag.md)|  |

### Return type

[**Tag**](Tag.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_project_replica_tag_delete**
> compute_project_replica_tag_delete(project_id, location_id, replica_id, tag_id)

Delete compute/replica.tag

Delete compute/replica.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_replica_api
from h1.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_project_replica_api.ComputeProjectReplicaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    replica_id = "replicaId_example" # str | Replica Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete compute/replica.tag
        api_instance.compute_project_replica_tag_delete(project_id, location_id, replica_id, tag_id)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **replica_id** | **str**| Replica Id |
 **tag_id** | **str**| tagId |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_project_replica_tag_get**
> Tag compute_project_replica_tag_get(project_id, location_id, replica_id, tag_id)

Get compute/replica.tag

Get compute/replica.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_replica_api
from h1.model.tag import Tag
from h1.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_project_replica_api.ComputeProjectReplicaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    replica_id = "replicaId_example" # str | Replica Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get compute/replica.tag
        api_response = api_instance.compute_project_replica_tag_get(project_id, location_id, replica_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **replica_id** | **str**| Replica Id |
 **tag_id** | **str**| tagId |

### Return type

[**Tag**](Tag.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_project_replica_tag_list**
> [Tag] compute_project_replica_tag_list(project_id, location_id, replica_id)

List compute/replica.tag

List compute/replica.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_replica_api
from h1.model.tag import Tag
from h1.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_project_replica_api.ComputeProjectReplicaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    replica_id = "replicaId_example" # str | Replica Id

    # example passing only required values which don't have defaults set
    try:
        # List compute/replica.tag
        api_response = api_instance.compute_project_replica_tag_list(project_id, location_id, replica_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **replica_id** | **str**| Replica Id |

### Return type

[**[Tag]**](Tag.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_project_replica_tag_put**
> [Tag] compute_project_replica_tag_put(project_id, location_id, replica_id, tag_array)

Replace compute/replica.tag

Replace compute/replica.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_replica_api
from h1.model.tag_array import TagArray
from h1.model.tag import Tag
from h1.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = compute_project_replica_api.ComputeProjectReplicaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    replica_id = "replicaId_example" # str | Replica Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace compute/replica.tag
        api_response = api_instance.compute_project_replica_tag_put(project_id, location_id, replica_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectReplicaApi->compute_project_replica_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **replica_id** | **str**| Replica Id |
 **tag_array** | [**TagArray**](TagArray.md)|  |

### Return type

[**[Tag]**](Tag.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

