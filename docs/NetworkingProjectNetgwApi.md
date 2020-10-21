# h1-client-python.NetworkingProjectNetgwApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networking_project_netgw_attach**](NetworkingProjectNetgwApi.md#networking_project_netgw_attach) | **POST** /networking/{locationId}/project/{projectId}/netgw/{netgwId}/actions/attach | Attach networking/netgw
[**networking_project_netgw_create**](NetworkingProjectNetgwApi.md#networking_project_netgw_create) | **POST** /networking/{locationId}/project/{projectId}/netgw | Create networking/netgw
[**networking_project_netgw_delete**](NetworkingProjectNetgwApi.md#networking_project_netgw_delete) | **DELETE** /networking/{locationId}/project/{projectId}/netgw/{netgwId} | Delete networking/netgw
[**networking_project_netgw_detach**](NetworkingProjectNetgwApi.md#networking_project_netgw_detach) | **POST** /networking/{locationId}/project/{projectId}/netgw/{netgwId}/actions/detach | Detach networking/netgw
[**networking_project_netgw_event_get**](NetworkingProjectNetgwApi.md#networking_project_netgw_event_get) | **GET** /networking/{locationId}/project/{projectId}/netgw/{netgwId}/event/{eventId} | Get networking/netgw.event
[**networking_project_netgw_event_list**](NetworkingProjectNetgwApi.md#networking_project_netgw_event_list) | **GET** /networking/{locationId}/project/{projectId}/netgw/{netgwId}/event | List networking/netgw.event
[**networking_project_netgw_get**](NetworkingProjectNetgwApi.md#networking_project_netgw_get) | **GET** /networking/{locationId}/project/{projectId}/netgw/{netgwId} | Get networking/netgw
[**networking_project_netgw_list**](NetworkingProjectNetgwApi.md#networking_project_netgw_list) | **GET** /networking/{locationId}/project/{projectId}/netgw | List networking/netgw
[**networking_project_netgw_service_get**](NetworkingProjectNetgwApi.md#networking_project_netgw_service_get) | **GET** /networking/{locationId}/project/{projectId}/netgw/{netgwId}/service/{serviceId} | Get networking/netgw.service
[**networking_project_netgw_service_list**](NetworkingProjectNetgwApi.md#networking_project_netgw_service_list) | **GET** /networking/{locationId}/project/{projectId}/netgw/{netgwId}/service | List networking/netgw.service
[**networking_project_netgw_tag_create**](NetworkingProjectNetgwApi.md#networking_project_netgw_tag_create) | **POST** /networking/{locationId}/project/{projectId}/netgw/{netgwId}/tag | Create networking/netgw.tag
[**networking_project_netgw_tag_delete**](NetworkingProjectNetgwApi.md#networking_project_netgw_tag_delete) | **DELETE** /networking/{locationId}/project/{projectId}/netgw/{netgwId}/tag/{tagId} | Delete networking/netgw.tag
[**networking_project_netgw_tag_get**](NetworkingProjectNetgwApi.md#networking_project_netgw_tag_get) | **GET** /networking/{locationId}/project/{projectId}/netgw/{netgwId}/tag/{tagId} | Get networking/netgw.tag
[**networking_project_netgw_tag_list**](NetworkingProjectNetgwApi.md#networking_project_netgw_tag_list) | **GET** /networking/{locationId}/project/{projectId}/netgw/{netgwId}/tag | List networking/netgw.tag
[**networking_project_netgw_tag_put**](NetworkingProjectNetgwApi.md#networking_project_netgw_tag_put) | **PUT** /networking/{locationId}/project/{projectId}/netgw/{netgwId}/tag | Replace networking/netgw.tag
[**networking_project_netgw_update**](NetworkingProjectNetgwApi.md#networking_project_netgw_update) | **PATCH** /networking/{locationId}/project/{projectId}/netgw/{netgwId} | Update networking/netgw


# **networking_project_netgw_attach**
> Netgw networking_project_netgw_attach(project_id, location_id, netgw_id, networking_project_netgw_attach, x_idempotency_key=x_idempotency_key)

Attach networking/netgw

action attach

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netgw_id = 'netgw_id_example' # str | Netgw Id
networking_project_netgw_attach = h1-client-python.NetworkingProjectNetgwAttach() # NetworkingProjectNetgwAttach | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Attach networking/netgw
        api_response = api_instance.networking_project_netgw_attach(project_id, location_id, netgw_id, networking_project_netgw_attach, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_attach: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netgw_id** | **str**| Netgw Id | 
 **networking_project_netgw_attach** | [**NetworkingProjectNetgwAttach**](NetworkingProjectNetgwAttach.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Netgw**](Netgw.md)

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

# **networking_project_netgw_create**
> Netgw networking_project_netgw_create(project_id, location_id, networking_project_netgw_create, x_idempotency_key=x_idempotency_key)

Create networking/netgw

Create netgw

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
networking_project_netgw_create = h1-client-python.NetworkingProjectNetgwCreate() # NetworkingProjectNetgwCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create networking/netgw
        api_response = api_instance.networking_project_netgw_create(project_id, location_id, networking_project_netgw_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **networking_project_netgw_create** | [**NetworkingProjectNetgwCreate**](NetworkingProjectNetgwCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Netgw**](Netgw.md)

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

# **networking_project_netgw_delete**
> networking_project_netgw_delete(project_id, location_id, netgw_id)

Delete networking/netgw

Delete netgw

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netgw_id = 'netgw_id_example' # str | Netgw Id

    try:
        # Delete networking/netgw
        api_instance.networking_project_netgw_delete(project_id, location_id, netgw_id)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netgw_id** | **str**| Netgw Id | 

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

# **networking_project_netgw_detach**
> Netgw networking_project_netgw_detach(project_id, location_id, netgw_id, x_idempotency_key=x_idempotency_key)

Detach networking/netgw

action detach

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netgw_id = 'netgw_id_example' # str | Netgw Id
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Detach networking/netgw
        api_response = api_instance.networking_project_netgw_detach(project_id, location_id, netgw_id, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_detach: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netgw_id** | **str**| Netgw Id | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Netgw**](Netgw.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**202** | operation queued |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **networking_project_netgw_event_get**
> Event networking_project_netgw_event_get(project_id, location_id, netgw_id, event_id)

Get networking/netgw.event

Get networking/netgw.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netgw_id = 'netgw_id_example' # str | Netgw Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get networking/netgw.event
        api_response = api_instance.networking_project_netgw_event_get(project_id, location_id, netgw_id, event_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netgw_id** | **str**| Netgw Id | 
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

# **networking_project_netgw_event_list**
> list[Event] networking_project_netgw_event_list(project_id, location_id, netgw_id, limit=limit, skip=skip)

List networking/netgw.event

List networking/netgw.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netgw_id = 'netgw_id_example' # str | Netgw Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List networking/netgw.event
        api_response = api_instance.networking_project_netgw_event_list(project_id, location_id, netgw_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netgw_id** | **str**| Netgw Id | 
 **limit** | **float**| $limit | [optional] [default to 100]
 **skip** | **float**| $skip | [optional] 

### Return type

[**list[Event]**](Event.md)

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

# **networking_project_netgw_get**
> Netgw networking_project_netgw_get(project_id, location_id, netgw_id)

Get networking/netgw

Returns a single netgw

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netgw_id = 'netgw_id_example' # str | Netgw Id

    try:
        # Get networking/netgw
        api_response = api_instance.networking_project_netgw_get(project_id, location_id, netgw_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netgw_id** | **str**| Netgw Id | 

### Return type

[**Netgw**](Netgw.md)

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

# **networking_project_netgw_list**
> list[Netgw] networking_project_netgw_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)

List networking/netgw

List netgw

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
name = 'name_example' # str | Filter by name (optional)
tag_value = 'tag_value_example' # str | Filter by tag.value (optional)
tag_key = 'tag_key_example' # str | Filter by tag.key (optional)

    try:
        # List networking/netgw
        api_response = api_instance.networking_project_netgw_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_list: %s\n" % e)
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

[**list[Netgw]**](Netgw.md)

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

# **networking_project_netgw_service_get**
> ResourceService networking_project_netgw_service_get(project_id, location_id, netgw_id, service_id)

Get networking/netgw.service

Get networking/netgw.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netgw_id = 'netgw_id_example' # str | Netgw Id
service_id = 'service_id_example' # str | serviceId

    try:
        # Get networking/netgw.service
        api_response = api_instance.networking_project_netgw_service_get(project_id, location_id, netgw_id, service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netgw_id** | **str**| Netgw Id | 
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

# **networking_project_netgw_service_list**
> list[ResourceService] networking_project_netgw_service_list(project_id, location_id, netgw_id)

List networking/netgw.service

List networking/netgw.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netgw_id = 'netgw_id_example' # str | Netgw Id

    try:
        # List networking/netgw.service
        api_response = api_instance.networking_project_netgw_service_list(project_id, location_id, netgw_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netgw_id** | **str**| Netgw Id | 

### Return type

[**list[ResourceService]**](ResourceService.md)

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

# **networking_project_netgw_tag_create**
> Tag networking_project_netgw_tag_create(project_id, location_id, netgw_id, tag)

Create networking/netgw.tag

Create networking/netgw.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netgw_id = 'netgw_id_example' # str | Netgw Id
tag = h1-client-python.Tag() # Tag | 

    try:
        # Create networking/netgw.tag
        api_response = api_instance.networking_project_netgw_tag_create(project_id, location_id, netgw_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netgw_id** | **str**| Netgw Id | 
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

# **networking_project_netgw_tag_delete**
> networking_project_netgw_tag_delete(project_id, location_id, netgw_id, tag_id)

Delete networking/netgw.tag

Delete networking/netgw.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netgw_id = 'netgw_id_example' # str | Netgw Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Delete networking/netgw.tag
        api_instance.networking_project_netgw_tag_delete(project_id, location_id, netgw_id, tag_id)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netgw_id** | **str**| Netgw Id | 
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

# **networking_project_netgw_tag_get**
> Tag networking_project_netgw_tag_get(project_id, location_id, netgw_id, tag_id)

Get networking/netgw.tag

Get networking/netgw.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netgw_id = 'netgw_id_example' # str | Netgw Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Get networking/netgw.tag
        api_response = api_instance.networking_project_netgw_tag_get(project_id, location_id, netgw_id, tag_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netgw_id** | **str**| Netgw Id | 
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

# **networking_project_netgw_tag_list**
> list[Tag] networking_project_netgw_tag_list(project_id, location_id, netgw_id)

List networking/netgw.tag

List networking/netgw.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netgw_id = 'netgw_id_example' # str | Netgw Id

    try:
        # List networking/netgw.tag
        api_response = api_instance.networking_project_netgw_tag_list(project_id, location_id, netgw_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netgw_id** | **str**| Netgw Id | 

### Return type

[**list[Tag]**](Tag.md)

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

# **networking_project_netgw_tag_put**
> list[Tag] networking_project_netgw_tag_put(project_id, location_id, netgw_id, tag)

Replace networking/netgw.tag

Replace networking/netgw.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netgw_id = 'netgw_id_example' # str | Netgw Id
tag = [h1-client-python.Tag()] # list[Tag] | 

    try:
        # Replace networking/netgw.tag
        api_response = api_instance.networking_project_netgw_tag_put(project_id, location_id, netgw_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netgw_id** | **str**| Netgw Id | 
 **tag** | [**list[Tag]**](Tag.md)|  | 

### Return type

[**list[Tag]**](Tag.md)

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

# **networking_project_netgw_update**
> Netgw networking_project_netgw_update(project_id, location_id, netgw_id, networking_project_netgw_update)

Update networking/netgw

Returns modified netgw

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1-client-python
from h1-client-python.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1-client-python.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1-client-python.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1-client-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = h1-client-python.NetworkingProjectNetgwApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netgw_id = 'netgw_id_example' # str | Netgw Id
networking_project_netgw_update = h1-client-python.NetworkingProjectNetgwUpdate() # NetworkingProjectNetgwUpdate | 

    try:
        # Update networking/netgw
        api_response = api_instance.networking_project_netgw_update(project_id, location_id, netgw_id, networking_project_netgw_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netgw_id** | **str**| Netgw Id | 
 **networking_project_netgw_update** | [**NetworkingProjectNetgwUpdate**](NetworkingProjectNetgwUpdate.md)|  | 

### Return type

[**Netgw**](Netgw.md)

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

