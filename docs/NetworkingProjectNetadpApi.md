# h1-client-python.NetworkingProjectNetadpApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networking_project_netadp_create**](NetworkingProjectNetadpApi.md#networking_project_netadp_create) | **POST** /networking/{locationId}/project/{projectId}/netadp | Create networking/netadp
[**networking_project_netadp_delete**](NetworkingProjectNetadpApi.md#networking_project_netadp_delete) | **DELETE** /networking/{locationId}/project/{projectId}/netadp/{netadpId} | Delete networking/netadp
[**networking_project_netadp_event_get**](NetworkingProjectNetadpApi.md#networking_project_netadp_event_get) | **GET** /networking/{locationId}/project/{projectId}/netadp/{netadpId}/event/{eventId} | Get networking/netadp.event
[**networking_project_netadp_event_list**](NetworkingProjectNetadpApi.md#networking_project_netadp_event_list) | **GET** /networking/{locationId}/project/{projectId}/netadp/{netadpId}/event | List networking/netadp.event
[**networking_project_netadp_get**](NetworkingProjectNetadpApi.md#networking_project_netadp_get) | **GET** /networking/{locationId}/project/{projectId}/netadp/{netadpId} | Get networking/netadp
[**networking_project_netadp_list**](NetworkingProjectNetadpApi.md#networking_project_netadp_list) | **GET** /networking/{locationId}/project/{projectId}/netadp | List networking/netadp
[**networking_project_netadp_metric_get**](NetworkingProjectNetadpApi.md#networking_project_netadp_metric_get) | **GET** /networking/{locationId}/project/{projectId}/netadp/{netadpId}/metric/{metricId} | Get networking/netadp.metric
[**networking_project_netadp_metric_list**](NetworkingProjectNetadpApi.md#networking_project_netadp_metric_list) | **GET** /networking/{locationId}/project/{projectId}/netadp/{netadpId}/metric | List networking/netadp.metric
[**networking_project_netadp_metric_point_list**](NetworkingProjectNetadpApi.md#networking_project_netadp_metric_point_list) | **GET** /networking/{locationId}/project/{projectId}/netadp/{netadpId}/metric/{metricId}/point | List networking/netadp.point
[**networking_project_netadp_service_get**](NetworkingProjectNetadpApi.md#networking_project_netadp_service_get) | **GET** /networking/{locationId}/project/{projectId}/netadp/{netadpId}/service/{serviceId} | Get networking/netadp.service
[**networking_project_netadp_service_list**](NetworkingProjectNetadpApi.md#networking_project_netadp_service_list) | **GET** /networking/{locationId}/project/{projectId}/netadp/{netadpId}/service | List networking/netadp.service
[**networking_project_netadp_tag_create**](NetworkingProjectNetadpApi.md#networking_project_netadp_tag_create) | **POST** /networking/{locationId}/project/{projectId}/netadp/{netadpId}/tag | Create networking/netadp.tag
[**networking_project_netadp_tag_delete**](NetworkingProjectNetadpApi.md#networking_project_netadp_tag_delete) | **DELETE** /networking/{locationId}/project/{projectId}/netadp/{netadpId}/tag/{tagId} | Delete networking/netadp.tag
[**networking_project_netadp_tag_get**](NetworkingProjectNetadpApi.md#networking_project_netadp_tag_get) | **GET** /networking/{locationId}/project/{projectId}/netadp/{netadpId}/tag/{tagId} | Get networking/netadp.tag
[**networking_project_netadp_tag_list**](NetworkingProjectNetadpApi.md#networking_project_netadp_tag_list) | **GET** /networking/{locationId}/project/{projectId}/netadp/{netadpId}/tag | List networking/netadp.tag
[**networking_project_netadp_tag_put**](NetworkingProjectNetadpApi.md#networking_project_netadp_tag_put) | **PUT** /networking/{locationId}/project/{projectId}/netadp/{netadpId}/tag | Replace networking/netadp.tag
[**networking_project_netadp_update**](NetworkingProjectNetadpApi.md#networking_project_netadp_update) | **PATCH** /networking/{locationId}/project/{projectId}/netadp/{netadpId} | Update networking/netadp


# **networking_project_netadp_create**
> Netadp networking_project_netadp_create(project_id, location_id, networking_project_netadp_create, x_idempotency_key=x_idempotency_key)

Create networking/netadp

Create netadp

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
networking_project_netadp_create = h1-client-python.NetworkingProjectNetadpCreate() # NetworkingProjectNetadpCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create networking/netadp
        api_response = api_instance.networking_project_netadp_create(project_id, location_id, networking_project_netadp_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **networking_project_netadp_create** | [**NetworkingProjectNetadpCreate**](NetworkingProjectNetadpCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Netadp**](Netadp.md)

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

# **networking_project_netadp_delete**
> networking_project_netadp_delete(project_id, location_id, netadp_id)

Delete networking/netadp

Delete netadp

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netadp_id = 'netadp_id_example' # str | Netadp Id

    try:
        # Delete networking/netadp
        api_instance.networking_project_netadp_delete(project_id, location_id, netadp_id)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netadp_id** | **str**| Netadp Id | 

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

# **networking_project_netadp_event_get**
> Event networking_project_netadp_event_get(project_id, location_id, netadp_id, event_id)

Get networking/netadp.event

Get networking/netadp.event

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netadp_id = 'netadp_id_example' # str | Netadp Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get networking/netadp.event
        api_response = api_instance.networking_project_netadp_event_get(project_id, location_id, netadp_id, event_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netadp_id** | **str**| Netadp Id | 
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

# **networking_project_netadp_event_list**
> list[Event] networking_project_netadp_event_list(project_id, location_id, netadp_id, limit=limit, skip=skip)

List networking/netadp.event

List networking/netadp.event

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netadp_id = 'netadp_id_example' # str | Netadp Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List networking/netadp.event
        api_response = api_instance.networking_project_netadp_event_list(project_id, location_id, netadp_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netadp_id** | **str**| Netadp Id | 
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

# **networking_project_netadp_get**
> Netadp networking_project_netadp_get(project_id, location_id, netadp_id)

Get networking/netadp

Returns a single netadp

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netadp_id = 'netadp_id_example' # str | Netadp Id

    try:
        # Get networking/netadp
        api_response = api_instance.networking_project_netadp_get(project_id, location_id, netadp_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netadp_id** | **str**| Netadp Id | 

### Return type

[**Netadp**](Netadp.md)

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

# **networking_project_netadp_list**
> list[Netadp] networking_project_netadp_list(project_id, location_id, assigned_resource=assigned_resource, assigned_id=assigned_id, network=network, tag_value=tag_value, tag_key=tag_key)

List networking/netadp

List netadp

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
assigned_resource = 'assigned_resource_example' # str | Filter by assigned.resource (optional)
assigned_id = 'assigned_id_example' # str | Filter by assigned.id (optional)
network = 'network_example' # str | Filter by network (optional)
tag_value = 'tag_value_example' # str | Filter by tag.value (optional)
tag_key = 'tag_key_example' # str | Filter by tag.key (optional)

    try:
        # List networking/netadp
        api_response = api_instance.networking_project_netadp_list(project_id, location_id, assigned_resource=assigned_resource, assigned_id=assigned_id, network=network, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **assigned_resource** | **str**| Filter by assigned.resource | [optional] 
 **assigned_id** | **str**| Filter by assigned.id | [optional] 
 **network** | **str**| Filter by network | [optional] 
 **tag_value** | **str**| Filter by tag.value | [optional] 
 **tag_key** | **str**| Filter by tag.key | [optional] 

### Return type

[**list[Netadp]**](Netadp.md)

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

# **networking_project_netadp_metric_get**
> Metric networking_project_netadp_metric_get(project_id, location_id, netadp_id, metric_id)

Get networking/netadp.metric

Get networking/netadp.metric

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netadp_id = 'netadp_id_example' # str | Netadp Id
metric_id = 'metric_id_example' # str | metricId

    try:
        # Get networking/netadp.metric
        api_response = api_instance.networking_project_netadp_metric_get(project_id, location_id, netadp_id, metric_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_metric_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netadp_id** | **str**| Netadp Id | 
 **metric_id** | **str**| metricId | 

### Return type

[**Metric**](Metric.md)

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

# **networking_project_netadp_metric_list**
> list[Metric] networking_project_netadp_metric_list(project_id, location_id, netadp_id)

List networking/netadp.metric

List networking/netadp.metric

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netadp_id = 'netadp_id_example' # str | Netadp Id

    try:
        # List networking/netadp.metric
        api_response = api_instance.networking_project_netadp_metric_list(project_id, location_id, netadp_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_metric_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netadp_id** | **str**| Netadp Id | 

### Return type

[**list[Metric]**](Metric.md)

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

# **networking_project_netadp_metric_point_list**
> list[Serie] networking_project_netadp_metric_point_list(project_id, location_id, netadp_id, metric_id, interval=interval, timespan=timespan)

List networking/netadp.point

List networking/netadp.point

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netadp_id = 'netadp_id_example' # str | Netadp Id
metric_id = 'metric_id_example' # str | metricId
interval = 'interval_example' # str | interval (optional)
timespan = 'timespan_example' # str | timespan (optional)

    try:
        # List networking/netadp.point
        api_response = api_instance.networking_project_netadp_metric_point_list(project_id, location_id, netadp_id, metric_id, interval=interval, timespan=timespan)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_metric_point_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netadp_id** | **str**| Netadp Id | 
 **metric_id** | **str**| metricId | 
 **interval** | **str**| interval | [optional] 
 **timespan** | **str**| timespan | [optional] 

### Return type

[**list[Serie]**](Serie.md)

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

# **networking_project_netadp_service_get**
> ResourceService networking_project_netadp_service_get(project_id, location_id, netadp_id, service_id)

Get networking/netadp.service

Get networking/netadp.service

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netadp_id = 'netadp_id_example' # str | Netadp Id
service_id = 'service_id_example' # str | serviceId

    try:
        # Get networking/netadp.service
        api_response = api_instance.networking_project_netadp_service_get(project_id, location_id, netadp_id, service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netadp_id** | **str**| Netadp Id | 
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

# **networking_project_netadp_service_list**
> list[ResourceService] networking_project_netadp_service_list(project_id, location_id, netadp_id)

List networking/netadp.service

List networking/netadp.service

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netadp_id = 'netadp_id_example' # str | Netadp Id

    try:
        # List networking/netadp.service
        api_response = api_instance.networking_project_netadp_service_list(project_id, location_id, netadp_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netadp_id** | **str**| Netadp Id | 

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

# **networking_project_netadp_tag_create**
> Tag networking_project_netadp_tag_create(project_id, location_id, netadp_id, tag)

Create networking/netadp.tag

Create networking/netadp.tag

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netadp_id = 'netadp_id_example' # str | Netadp Id
tag = h1-client-python.Tag() # Tag | 

    try:
        # Create networking/netadp.tag
        api_response = api_instance.networking_project_netadp_tag_create(project_id, location_id, netadp_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netadp_id** | **str**| Netadp Id | 
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

# **networking_project_netadp_tag_delete**
> networking_project_netadp_tag_delete(project_id, location_id, netadp_id, tag_id)

Delete networking/netadp.tag

Delete networking/netadp.tag

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netadp_id = 'netadp_id_example' # str | Netadp Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Delete networking/netadp.tag
        api_instance.networking_project_netadp_tag_delete(project_id, location_id, netadp_id, tag_id)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netadp_id** | **str**| Netadp Id | 
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

# **networking_project_netadp_tag_get**
> Tag networking_project_netadp_tag_get(project_id, location_id, netadp_id, tag_id)

Get networking/netadp.tag

Get networking/netadp.tag

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netadp_id = 'netadp_id_example' # str | Netadp Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Get networking/netadp.tag
        api_response = api_instance.networking_project_netadp_tag_get(project_id, location_id, netadp_id, tag_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netadp_id** | **str**| Netadp Id | 
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

# **networking_project_netadp_tag_list**
> list[Tag] networking_project_netadp_tag_list(project_id, location_id, netadp_id)

List networking/netadp.tag

List networking/netadp.tag

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netadp_id = 'netadp_id_example' # str | Netadp Id

    try:
        # List networking/netadp.tag
        api_response = api_instance.networking_project_netadp_tag_list(project_id, location_id, netadp_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netadp_id** | **str**| Netadp Id | 

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

# **networking_project_netadp_tag_put**
> list[Tag] networking_project_netadp_tag_put(project_id, location_id, netadp_id, tag)

Replace networking/netadp.tag

Replace networking/netadp.tag

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netadp_id = 'netadp_id_example' # str | Netadp Id
tag = [h1-client-python.Tag()] # list[Tag] | 

    try:
        # Replace networking/netadp.tag
        api_response = api_instance.networking_project_netadp_tag_put(project_id, location_id, netadp_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netadp_id** | **str**| Netadp Id | 
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

# **networking_project_netadp_update**
> Netadp networking_project_netadp_update(project_id, location_id, netadp_id, networking_project_netadp_update)

Update networking/netadp

Returns modified netadp

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
    api_instance = h1-client-python.NetworkingProjectNetadpApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
netadp_id = 'netadp_id_example' # str | Netadp Id
networking_project_netadp_update = h1-client-python.NetworkingProjectNetadpUpdate() # NetworkingProjectNetadpUpdate | 

    try:
        # Update networking/netadp
        api_response = api_instance.networking_project_netadp_update(project_id, location_id, netadp_id, networking_project_netadp_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NetworkingProjectNetadpApi->networking_project_netadp_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **netadp_id** | **str**| Netadp Id | 
 **networking_project_netadp_update** | [**NetworkingProjectNetadpUpdate**](NetworkingProjectNetadpUpdate.md)|  | 

### Return type

[**Netadp**](Netadp.md)

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

