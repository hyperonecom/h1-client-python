# h1.VmhostProjectInstanceApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vmhost_project_instance_event_get**](VmhostProjectInstanceApi.md#vmhost_project_instance_event_get) | **GET** /vmhost/{locationId}/project/{projectId}/instance/{instanceId}/event/{eventId} | Get vmhost/instance.event
[**vmhost_project_instance_event_list**](VmhostProjectInstanceApi.md#vmhost_project_instance_event_list) | **GET** /vmhost/{locationId}/project/{projectId}/instance/{instanceId}/event | List vmhost/instance.event
[**vmhost_project_instance_get**](VmhostProjectInstanceApi.md#vmhost_project_instance_get) | **GET** /vmhost/{locationId}/project/{projectId}/instance/{instanceId} | Get vmhost/instance
[**vmhost_project_instance_list**](VmhostProjectInstanceApi.md#vmhost_project_instance_list) | **GET** /vmhost/{locationId}/project/{projectId}/instance | List vmhost/instance
[**vmhost_project_instance_service_get**](VmhostProjectInstanceApi.md#vmhost_project_instance_service_get) | **GET** /vmhost/{locationId}/project/{projectId}/instance/{instanceId}/service/{serviceId} | Get vmhost/instance.service
[**vmhost_project_instance_service_list**](VmhostProjectInstanceApi.md#vmhost_project_instance_service_list) | **GET** /vmhost/{locationId}/project/{projectId}/instance/{instanceId}/service | List vmhost/instance.service
[**vmhost_project_instance_tag_create**](VmhostProjectInstanceApi.md#vmhost_project_instance_tag_create) | **POST** /vmhost/{locationId}/project/{projectId}/instance/{instanceId}/tag | Create vmhost/instance.tag
[**vmhost_project_instance_tag_delete**](VmhostProjectInstanceApi.md#vmhost_project_instance_tag_delete) | **DELETE** /vmhost/{locationId}/project/{projectId}/instance/{instanceId}/tag/{tagId} | Delete vmhost/instance.tag
[**vmhost_project_instance_tag_get**](VmhostProjectInstanceApi.md#vmhost_project_instance_tag_get) | **GET** /vmhost/{locationId}/project/{projectId}/instance/{instanceId}/tag/{tagId} | Get vmhost/instance.tag
[**vmhost_project_instance_tag_list**](VmhostProjectInstanceApi.md#vmhost_project_instance_tag_list) | **GET** /vmhost/{locationId}/project/{projectId}/instance/{instanceId}/tag | List vmhost/instance.tag
[**vmhost_project_instance_tag_put**](VmhostProjectInstanceApi.md#vmhost_project_instance_tag_put) | **PUT** /vmhost/{locationId}/project/{projectId}/instance/{instanceId}/tag | Replace vmhost/instance.tag


# **vmhost_project_instance_event_get**
> Event vmhost_project_instance_event_get(project_id, location_id, instance_id, event_id)

Get vmhost/instance.event

Get vmhost/instance.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.VmhostProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get vmhost/instance.event
        api_response = api_instance.vmhost_project_instance_event_get(project_id, location_id, instance_id, event_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VmhostProjectInstanceApi->vmhost_project_instance_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
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

# **vmhost_project_instance_event_list**
> list[Event] vmhost_project_instance_event_list(project_id, location_id, instance_id, limit=limit, skip=skip)

List vmhost/instance.event

List vmhost/instance.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.VmhostProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List vmhost/instance.event
        api_response = api_instance.vmhost_project_instance_event_list(project_id, location_id, instance_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VmhostProjectInstanceApi->vmhost_project_instance_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
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

# **vmhost_project_instance_get**
> Vmhost vmhost_project_instance_get(project_id, location_id, instance_id)

Get vmhost/instance

Returns a single instance

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.VmhostProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # Get vmhost/instance
        api_response = api_instance.vmhost_project_instance_get(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VmhostProjectInstanceApi->vmhost_project_instance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 

### Return type

[**Vmhost**](Vmhost.md)

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

# **vmhost_project_instance_list**
> list[Vmhost] vmhost_project_instance_list(project_id, location_id, enabled_services=enabled_services)

List vmhost/instance

List instance

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.VmhostProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
enabled_services = 'enabled_services_example' # str | Filter by enabledServices (optional)

    try:
        # List vmhost/instance
        api_response = api_instance.vmhost_project_instance_list(project_id, location_id, enabled_services=enabled_services)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VmhostProjectInstanceApi->vmhost_project_instance_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **enabled_services** | **str**| Filter by enabledServices | [optional] 

### Return type

[**list[Vmhost]**](Vmhost.md)

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

# **vmhost_project_instance_service_get**
> ResourceService vmhost_project_instance_service_get(project_id, location_id, instance_id, service_id)

Get vmhost/instance.service

Get vmhost/instance.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.VmhostProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
service_id = 'service_id_example' # str | serviceId

    try:
        # Get vmhost/instance.service
        api_response = api_instance.vmhost_project_instance_service_get(project_id, location_id, instance_id, service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VmhostProjectInstanceApi->vmhost_project_instance_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
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

# **vmhost_project_instance_service_list**
> list[ResourceService] vmhost_project_instance_service_list(project_id, location_id, instance_id)

List vmhost/instance.service

List vmhost/instance.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.VmhostProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List vmhost/instance.service
        api_response = api_instance.vmhost_project_instance_service_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VmhostProjectInstanceApi->vmhost_project_instance_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 

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

# **vmhost_project_instance_tag_create**
> Tag vmhost_project_instance_tag_create(project_id, location_id, instance_id, tag)

Create vmhost/instance.tag

Create vmhost/instance.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.VmhostProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
tag = h1.Tag() # Tag | 

    try:
        # Create vmhost/instance.tag
        api_response = api_instance.vmhost_project_instance_tag_create(project_id, location_id, instance_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VmhostProjectInstanceApi->vmhost_project_instance_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
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

# **vmhost_project_instance_tag_delete**
> vmhost_project_instance_tag_delete(project_id, location_id, instance_id, tag_id)

Delete vmhost/instance.tag

Delete vmhost/instance.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.VmhostProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Delete vmhost/instance.tag
        api_instance.vmhost_project_instance_tag_delete(project_id, location_id, instance_id, tag_id)
    except ApiException as e:
        print("Exception when calling VmhostProjectInstanceApi->vmhost_project_instance_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
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

# **vmhost_project_instance_tag_get**
> Tag vmhost_project_instance_tag_get(project_id, location_id, instance_id, tag_id)

Get vmhost/instance.tag

Get vmhost/instance.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.VmhostProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Get vmhost/instance.tag
        api_response = api_instance.vmhost_project_instance_tag_get(project_id, location_id, instance_id, tag_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VmhostProjectInstanceApi->vmhost_project_instance_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
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

# **vmhost_project_instance_tag_list**
> list[Tag] vmhost_project_instance_tag_list(project_id, location_id, instance_id)

List vmhost/instance.tag

List vmhost/instance.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.VmhostProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List vmhost/instance.tag
        api_response = api_instance.vmhost_project_instance_tag_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VmhostProjectInstanceApi->vmhost_project_instance_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 

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

# **vmhost_project_instance_tag_put**
> list[Tag] vmhost_project_instance_tag_put(project_id, location_id, instance_id, tag)

Replace vmhost/instance.tag

Replace vmhost/instance.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.VmhostProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
tag = [h1.Tag()] # list[Tag] | 

    try:
        # Replace vmhost/instance.tag
        api_response = api_instance.vmhost_project_instance_tag_put(project_id, location_id, instance_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VmhostProjectInstanceApi->vmhost_project_instance_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
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

