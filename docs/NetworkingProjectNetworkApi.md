# h1.NetworkingProjectNetworkApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networking_project_network_create**](NetworkingProjectNetworkApi.md#networking_project_network_create) | **POST** /networking/{locationId}/project/{projectId}/network | Create networking/network
[**networking_project_network_delete**](NetworkingProjectNetworkApi.md#networking_project_network_delete) | **DELETE** /networking/{locationId}/project/{projectId}/network/{networkId} | Delete networking/network
[**networking_project_network_event_get**](NetworkingProjectNetworkApi.md#networking_project_network_event_get) | **GET** /networking/{locationId}/project/{projectId}/network/{networkId}/event/{eventId} | Get networking/network.event
[**networking_project_network_event_list**](NetworkingProjectNetworkApi.md#networking_project_network_event_list) | **GET** /networking/{locationId}/project/{projectId}/network/{networkId}/event | List networking/network.event
[**networking_project_network_get**](NetworkingProjectNetworkApi.md#networking_project_network_get) | **GET** /networking/{locationId}/project/{projectId}/network/{networkId} | Get networking/network
[**networking_project_network_list**](NetworkingProjectNetworkApi.md#networking_project_network_list) | **GET** /networking/{locationId}/project/{projectId}/network | List networking/network
[**networking_project_network_service_get**](NetworkingProjectNetworkApi.md#networking_project_network_service_get) | **GET** /networking/{locationId}/project/{projectId}/network/{networkId}/service/{serviceId} | Get networking/network.service
[**networking_project_network_service_list**](NetworkingProjectNetworkApi.md#networking_project_network_service_list) | **GET** /networking/{locationId}/project/{projectId}/network/{networkId}/service | List networking/network.service
[**networking_project_network_tag_create**](NetworkingProjectNetworkApi.md#networking_project_network_tag_create) | **POST** /networking/{locationId}/project/{projectId}/network/{networkId}/tag | Create networking/network.tag
[**networking_project_network_tag_delete**](NetworkingProjectNetworkApi.md#networking_project_network_tag_delete) | **DELETE** /networking/{locationId}/project/{projectId}/network/{networkId}/tag/{tagId} | Delete networking/network.tag
[**networking_project_network_tag_get**](NetworkingProjectNetworkApi.md#networking_project_network_tag_get) | **GET** /networking/{locationId}/project/{projectId}/network/{networkId}/tag/{tagId} | Get networking/network.tag
[**networking_project_network_tag_list**](NetworkingProjectNetworkApi.md#networking_project_network_tag_list) | **GET** /networking/{locationId}/project/{projectId}/network/{networkId}/tag | List networking/network.tag
[**networking_project_network_tag_put**](NetworkingProjectNetworkApi.md#networking_project_network_tag_put) | **PUT** /networking/{locationId}/project/{projectId}/network/{networkId}/tag | Replace networking/network.tag
[**networking_project_network_update**](NetworkingProjectNetworkApi.md#networking_project_network_update) | **PATCH** /networking/{locationId}/project/{projectId}/network/{networkId} | Update networking/network


# **networking_project_network_create**
> Network networking_project_network_create(project_id, location_id, networking_project_network_create)

Create networking/network

Create network

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_network_api
from h1.model.network import Network
from h1.model.networking_project_network_create import NetworkingProjectNetworkCreate
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
    api_instance = networking_project_network_api.NetworkingProjectNetworkApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    networking_project_network_create = NetworkingProjectNetworkCreate(
        name="name_example",
        address="address_example",
        gateway="gateway_example",
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # NetworkingProjectNetworkCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create networking/network
        api_response = api_instance.networking_project_network_create(project_id, location_id, networking_project_network_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create networking/network
        api_response = api_instance.networking_project_network_create(project_id, location_id, networking_project_network_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **networking_project_network_create** | [**NetworkingProjectNetworkCreate**](NetworkingProjectNetworkCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Network**](Network.md)

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

# **networking_project_network_delete**
> networking_project_network_delete(project_id, location_id, network_id)

Delete networking/network

Delete network

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_network_api
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
    api_instance = networking_project_network_api.NetworkingProjectNetworkApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    network_id = "networkId_example" # str | Network Id

    # example passing only required values which don't have defaults set
    try:
        # Delete networking/network
        api_instance.networking_project_network_delete(project_id, location_id, network_id)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **network_id** | **str**| Network Id |

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

# **networking_project_network_event_get**
> Event networking_project_network_event_get(project_id, location_id, network_id, event_id)

Get networking/network.event

Get networking/network.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_network_api
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
    api_instance = networking_project_network_api.NetworkingProjectNetworkApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    network_id = "networkId_example" # str | Network Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get networking/network.event
        api_response = api_instance.networking_project_network_event_get(project_id, location_id, network_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_event_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **network_id** | **str**| Network Id |
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

# **networking_project_network_event_list**
> [Event] networking_project_network_event_list(project_id, location_id, network_id)

List networking/network.event

List networking/network.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_network_api
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
    api_instance = networking_project_network_api.NetworkingProjectNetworkApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    network_id = "networkId_example" # str | Network Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List networking/network.event
        api_response = api_instance.networking_project_network_event_list(project_id, location_id, network_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List networking/network.event
        api_response = api_instance.networking_project_network_event_list(project_id, location_id, network_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **network_id** | **str**| Network Id |
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

# **networking_project_network_get**
> Network networking_project_network_get(project_id, location_id, network_id)

Get networking/network

Returns a single network

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_network_api
from h1.model.network import Network
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
    api_instance = networking_project_network_api.NetworkingProjectNetworkApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    network_id = "networkId_example" # str | Network Id

    # example passing only required values which don't have defaults set
    try:
        # Get networking/network
        api_response = api_instance.networking_project_network_get(project_id, location_id, network_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **network_id** | **str**| Network Id |

### Return type

[**Network**](Network.md)

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

# **networking_project_network_list**
> [Network] networking_project_network_list(project_id, location_id)

List networking/network

List network

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_network_api
from h1.model.network import Network
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
    api_instance = networking_project_network_api.NetworkingProjectNetworkApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List networking/network
        api_response = api_instance.networking_project_network_list(project_id, location_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List networking/network
        api_response = api_instance.networking_project_network_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **name** | **str**| Filter by name | [optional]
 **tag_value** | **str**| Filter by tag.value | [optional]
 **tag_key** | **str**| Filter by tag.key | [optional]

### Return type

[**[Network]**](Network.md)

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

# **networking_project_network_service_get**
> ResourceService networking_project_network_service_get(project_id, location_id, network_id, service_id)

Get networking/network.service

Get networking/network.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_network_api
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
    api_instance = networking_project_network_api.NetworkingProjectNetworkApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    network_id = "networkId_example" # str | Network Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get networking/network.service
        api_response = api_instance.networking_project_network_service_get(project_id, location_id, network_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **network_id** | **str**| Network Id |
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

# **networking_project_network_service_list**
> [ResourceService] networking_project_network_service_list(project_id, location_id, network_id)

List networking/network.service

List networking/network.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_network_api
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
    api_instance = networking_project_network_api.NetworkingProjectNetworkApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    network_id = "networkId_example" # str | Network Id

    # example passing only required values which don't have defaults set
    try:
        # List networking/network.service
        api_response = api_instance.networking_project_network_service_list(project_id, location_id, network_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **network_id** | **str**| Network Id |

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

# **networking_project_network_tag_create**
> Tag networking_project_network_tag_create(project_id, location_id, network_id, tag)

Create networking/network.tag

Create networking/network.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_network_api
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
    api_instance = networking_project_network_api.NetworkingProjectNetworkApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    network_id = "networkId_example" # str | Network Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create networking/network.tag
        api_response = api_instance.networking_project_network_tag_create(project_id, location_id, network_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_tag_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **network_id** | **str**| Network Id |
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

# **networking_project_network_tag_delete**
> networking_project_network_tag_delete(project_id, location_id, network_id, tag_id)

Delete networking/network.tag

Delete networking/network.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_network_api
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
    api_instance = networking_project_network_api.NetworkingProjectNetworkApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    network_id = "networkId_example" # str | Network Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete networking/network.tag
        api_instance.networking_project_network_tag_delete(project_id, location_id, network_id, tag_id)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_tag_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **network_id** | **str**| Network Id |
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

# **networking_project_network_tag_get**
> Tag networking_project_network_tag_get(project_id, location_id, network_id, tag_id)

Get networking/network.tag

Get networking/network.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_network_api
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
    api_instance = networking_project_network_api.NetworkingProjectNetworkApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    network_id = "networkId_example" # str | Network Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get networking/network.tag
        api_response = api_instance.networking_project_network_tag_get(project_id, location_id, network_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_tag_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **network_id** | **str**| Network Id |
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

# **networking_project_network_tag_list**
> [Tag] networking_project_network_tag_list(project_id, location_id, network_id)

List networking/network.tag

List networking/network.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_network_api
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
    api_instance = networking_project_network_api.NetworkingProjectNetworkApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    network_id = "networkId_example" # str | Network Id

    # example passing only required values which don't have defaults set
    try:
        # List networking/network.tag
        api_response = api_instance.networking_project_network_tag_list(project_id, location_id, network_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_tag_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **network_id** | **str**| Network Id |

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

# **networking_project_network_tag_put**
> [Tag] networking_project_network_tag_put(project_id, location_id, network_id, tag_array)

Replace networking/network.tag

Replace networking/network.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_network_api
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
    api_instance = networking_project_network_api.NetworkingProjectNetworkApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    network_id = "networkId_example" # str | Network Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace networking/network.tag
        api_response = api_instance.networking_project_network_tag_put(project_id, location_id, network_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_tag_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **network_id** | **str**| Network Id |
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

# **networking_project_network_update**
> Network networking_project_network_update(project_id, location_id, network_id, networking_project_network_update)

Update networking/network

Returns modified network

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_network_api
from h1.model.networking_project_network_update import NetworkingProjectNetworkUpdate
from h1.model.network import Network
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
    api_instance = networking_project_network_api.NetworkingProjectNetworkApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    network_id = "networkId_example" # str | Network Id
    networking_project_network_update = NetworkingProjectNetworkUpdate(
        name="name_example",
        gateway="gateway_example",
        firewall="firewall_example",
    ) # NetworkingProjectNetworkUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update networking/network
        api_response = api_instance.networking_project_network_update(project_id, location_id, network_id, networking_project_network_update)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetworkApi->networking_project_network_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **network_id** | **str**| Network Id |
 **networking_project_network_update** | [**NetworkingProjectNetworkUpdate**](NetworkingProjectNetworkUpdate.md)|  |

### Return type

[**Network**](Network.md)

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

