# h1-client-python.StorageProjectIsoApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_project_iso_create**](StorageProjectIsoApi.md#storage_project_iso_create) | **POST** /storage/{locationId}/project/{projectId}/iso | Create storage/iso
[**storage_project_iso_delete**](StorageProjectIsoApi.md#storage_project_iso_delete) | **DELETE** /storage/{locationId}/project/{projectId}/iso/{isoId} | Delete storage/iso
[**storage_project_iso_detach**](StorageProjectIsoApi.md#storage_project_iso_detach) | **POST** /storage/{locationId}/project/{projectId}/iso/{isoId}/actions/detach | Detach storage/iso
[**storage_project_iso_event_get**](StorageProjectIsoApi.md#storage_project_iso_event_get) | **GET** /storage/{locationId}/project/{projectId}/iso/{isoId}/event/{eventId} | Get storage/iso.event
[**storage_project_iso_event_list**](StorageProjectIsoApi.md#storage_project_iso_event_list) | **GET** /storage/{locationId}/project/{projectId}/iso/{isoId}/event | List storage/iso.event
[**storage_project_iso_get**](StorageProjectIsoApi.md#storage_project_iso_get) | **GET** /storage/{locationId}/project/{projectId}/iso/{isoId} | Get storage/iso
[**storage_project_iso_list**](StorageProjectIsoApi.md#storage_project_iso_list) | **GET** /storage/{locationId}/project/{projectId}/iso | List storage/iso
[**storage_project_iso_service_get**](StorageProjectIsoApi.md#storage_project_iso_service_get) | **GET** /storage/{locationId}/project/{projectId}/iso/{isoId}/service/{serviceId} | Get storage/iso.service
[**storage_project_iso_service_list**](StorageProjectIsoApi.md#storage_project_iso_service_list) | **GET** /storage/{locationId}/project/{projectId}/iso/{isoId}/service | List storage/iso.service
[**storage_project_iso_tag_create**](StorageProjectIsoApi.md#storage_project_iso_tag_create) | **POST** /storage/{locationId}/project/{projectId}/iso/{isoId}/tag | Create storage/iso.tag
[**storage_project_iso_tag_delete**](StorageProjectIsoApi.md#storage_project_iso_tag_delete) | **DELETE** /storage/{locationId}/project/{projectId}/iso/{isoId}/tag/{tagId} | Delete storage/iso.tag
[**storage_project_iso_tag_get**](StorageProjectIsoApi.md#storage_project_iso_tag_get) | **GET** /storage/{locationId}/project/{projectId}/iso/{isoId}/tag/{tagId} | Get storage/iso.tag
[**storage_project_iso_tag_list**](StorageProjectIsoApi.md#storage_project_iso_tag_list) | **GET** /storage/{locationId}/project/{projectId}/iso/{isoId}/tag | List storage/iso.tag
[**storage_project_iso_tag_put**](StorageProjectIsoApi.md#storage_project_iso_tag_put) | **PUT** /storage/{locationId}/project/{projectId}/iso/{isoId}/tag | Replace storage/iso.tag
[**storage_project_iso_transfer**](StorageProjectIsoApi.md#storage_project_iso_transfer) | **POST** /storage/{locationId}/project/{projectId}/iso/{isoId}/actions/transfer | Transfer storage/iso
[**storage_project_iso_update**](StorageProjectIsoApi.md#storage_project_iso_update) | **PATCH** /storage/{locationId}/project/{projectId}/iso/{isoId} | Update storage/iso


# **storage_project_iso_create**
> Iso storage_project_iso_create(project_id, location_id, storage_project_iso_create, x_idempotency_key=x_idempotency_key)

Create storage/iso

Create iso

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
storage_project_iso_create = h1-client-python.StorageProjectIsoCreate() # StorageProjectIsoCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create storage/iso
        api_response = api_instance.storage_project_iso_create(project_id, location_id, storage_project_iso_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **storage_project_iso_create** | [**StorageProjectIsoCreate**](StorageProjectIsoCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Iso**](Iso.md)

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

# **storage_project_iso_delete**
> storage_project_iso_delete(project_id, location_id, iso_id)

Delete storage/iso

Delete iso

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
iso_id = 'iso_id_example' # str | Iso Id

    try:
        # Delete storage/iso
        api_instance.storage_project_iso_delete(project_id, location_id, iso_id)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **iso_id** | **str**| Iso Id | 

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

# **storage_project_iso_detach**
> Iso storage_project_iso_detach(project_id, location_id, iso_id, storage_project_iso_detach, x_idempotency_key=x_idempotency_key)

Detach storage/iso

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
iso_id = 'iso_id_example' # str | Iso Id
storage_project_iso_detach = h1-client-python.StorageProjectIsoDetach() # StorageProjectIsoDetach | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Detach storage/iso
        api_response = api_instance.storage_project_iso_detach(project_id, location_id, iso_id, storage_project_iso_detach, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_detach: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **iso_id** | **str**| Iso Id | 
 **storage_project_iso_detach** | [**StorageProjectIsoDetach**](StorageProjectIsoDetach.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Iso**](Iso.md)

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

# **storage_project_iso_event_get**
> Event storage_project_iso_event_get(project_id, location_id, iso_id, event_id)

Get storage/iso.event

Get storage/iso.event

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
iso_id = 'iso_id_example' # str | Iso Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get storage/iso.event
        api_response = api_instance.storage_project_iso_event_get(project_id, location_id, iso_id, event_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **iso_id** | **str**| Iso Id | 
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

# **storage_project_iso_event_list**
> list[Event] storage_project_iso_event_list(project_id, location_id, iso_id, limit=limit, skip=skip)

List storage/iso.event

List storage/iso.event

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
iso_id = 'iso_id_example' # str | Iso Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List storage/iso.event
        api_response = api_instance.storage_project_iso_event_list(project_id, location_id, iso_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **iso_id** | **str**| Iso Id | 
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

# **storage_project_iso_get**
> Iso storage_project_iso_get(project_id, location_id, iso_id)

Get storage/iso

Returns a single iso

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
iso_id = 'iso_id_example' # str | Iso Id

    try:
        # Get storage/iso
        api_response = api_instance.storage_project_iso_get(project_id, location_id, iso_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **iso_id** | **str**| Iso Id | 

### Return type

[**Iso**](Iso.md)

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

# **storage_project_iso_list**
> list[Iso] storage_project_iso_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)

List storage/iso

List iso

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
name = 'name_example' # str | Filter by name (optional)
tag_value = 'tag_value_example' # str | Filter by tag.value (optional)
tag_key = 'tag_key_example' # str | Filter by tag.key (optional)

    try:
        # List storage/iso
        api_response = api_instance.storage_project_iso_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_list: %s\n" % e)
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

[**list[Iso]**](Iso.md)

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

# **storage_project_iso_service_get**
> ResourceService storage_project_iso_service_get(project_id, location_id, iso_id, service_id)

Get storage/iso.service

Get storage/iso.service

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
iso_id = 'iso_id_example' # str | Iso Id
service_id = 'service_id_example' # str | serviceId

    try:
        # Get storage/iso.service
        api_response = api_instance.storage_project_iso_service_get(project_id, location_id, iso_id, service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **iso_id** | **str**| Iso Id | 
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

# **storage_project_iso_service_list**
> list[ResourceService] storage_project_iso_service_list(project_id, location_id, iso_id)

List storage/iso.service

List storage/iso.service

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
iso_id = 'iso_id_example' # str | Iso Id

    try:
        # List storage/iso.service
        api_response = api_instance.storage_project_iso_service_list(project_id, location_id, iso_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **iso_id** | **str**| Iso Id | 

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

# **storage_project_iso_tag_create**
> Tag storage_project_iso_tag_create(project_id, location_id, iso_id, tag)

Create storage/iso.tag

Create storage/iso.tag

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
iso_id = 'iso_id_example' # str | Iso Id
tag = h1-client-python.Tag() # Tag | 

    try:
        # Create storage/iso.tag
        api_response = api_instance.storage_project_iso_tag_create(project_id, location_id, iso_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **iso_id** | **str**| Iso Id | 
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

# **storage_project_iso_tag_delete**
> storage_project_iso_tag_delete(project_id, location_id, iso_id, tag_id)

Delete storage/iso.tag

Delete storage/iso.tag

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
iso_id = 'iso_id_example' # str | Iso Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Delete storage/iso.tag
        api_instance.storage_project_iso_tag_delete(project_id, location_id, iso_id, tag_id)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **iso_id** | **str**| Iso Id | 
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

# **storage_project_iso_tag_get**
> Tag storage_project_iso_tag_get(project_id, location_id, iso_id, tag_id)

Get storage/iso.tag

Get storage/iso.tag

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
iso_id = 'iso_id_example' # str | Iso Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Get storage/iso.tag
        api_response = api_instance.storage_project_iso_tag_get(project_id, location_id, iso_id, tag_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **iso_id** | **str**| Iso Id | 
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

# **storage_project_iso_tag_list**
> list[Tag] storage_project_iso_tag_list(project_id, location_id, iso_id)

List storage/iso.tag

List storage/iso.tag

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
iso_id = 'iso_id_example' # str | Iso Id

    try:
        # List storage/iso.tag
        api_response = api_instance.storage_project_iso_tag_list(project_id, location_id, iso_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **iso_id** | **str**| Iso Id | 

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

# **storage_project_iso_tag_put**
> list[Tag] storage_project_iso_tag_put(project_id, location_id, iso_id, tag)

Replace storage/iso.tag

Replace storage/iso.tag

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
iso_id = 'iso_id_example' # str | Iso Id
tag = [h1-client-python.Tag()] # list[Tag] | 

    try:
        # Replace storage/iso.tag
        api_response = api_instance.storage_project_iso_tag_put(project_id, location_id, iso_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **iso_id** | **str**| Iso Id | 
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

# **storage_project_iso_transfer**
> Iso storage_project_iso_transfer(project_id, location_id, iso_id, storage_project_iso_transfer, x_idempotency_key=x_idempotency_key)

Transfer storage/iso

action transfer

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
iso_id = 'iso_id_example' # str | Iso Id
storage_project_iso_transfer = h1-client-python.StorageProjectIsoTransfer() # StorageProjectIsoTransfer | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Transfer storage/iso
        api_response = api_instance.storage_project_iso_transfer(project_id, location_id, iso_id, storage_project_iso_transfer, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **iso_id** | **str**| Iso Id | 
 **storage_project_iso_transfer** | [**StorageProjectIsoTransfer**](StorageProjectIsoTransfer.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Iso**](Iso.md)

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

# **storage_project_iso_update**
> Iso storage_project_iso_update(project_id, location_id, iso_id, storage_project_iso_update)

Update storage/iso

Returns modified iso

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
    api_instance = h1-client-python.StorageProjectIsoApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
iso_id = 'iso_id_example' # str | Iso Id
storage_project_iso_update = h1-client-python.StorageProjectIsoUpdate() # StorageProjectIsoUpdate | 

    try:
        # Update storage/iso
        api_response = api_instance.storage_project_iso_update(project_id, location_id, iso_id, storage_project_iso_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **iso_id** | **str**| Iso Id | 
 **storage_project_iso_update** | [**StorageProjectIsoUpdate**](StorageProjectIsoUpdate.md)|  | 

### Return type

[**Iso**](Iso.md)

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

