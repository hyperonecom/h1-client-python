# h1-client-python.StorageProjectDiskApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_project_disk_attach**](StorageProjectDiskApi.md#storage_project_disk_attach) | **POST** /storage/{locationId}/project/{projectId}/disk/{diskId}/actions/attach | Attach storage/disk
[**storage_project_disk_create**](StorageProjectDiskApi.md#storage_project_disk_create) | **POST** /storage/{locationId}/project/{projectId}/disk | Create storage/disk
[**storage_project_disk_delete**](StorageProjectDiskApi.md#storage_project_disk_delete) | **DELETE** /storage/{locationId}/project/{projectId}/disk/{diskId} | Delete storage/disk
[**storage_project_disk_detach**](StorageProjectDiskApi.md#storage_project_disk_detach) | **POST** /storage/{locationId}/project/{projectId}/disk/{diskId}/actions/detach | Detach storage/disk
[**storage_project_disk_download**](StorageProjectDiskApi.md#storage_project_disk_download) | **POST** /storage/{locationId}/project/{projectId}/disk/{diskId}/actions/download | Download storage/disk
[**storage_project_disk_event_get**](StorageProjectDiskApi.md#storage_project_disk_event_get) | **GET** /storage/{locationId}/project/{projectId}/disk/{diskId}/event/{eventId} | Get storage/disk.event
[**storage_project_disk_event_list**](StorageProjectDiskApi.md#storage_project_disk_event_list) | **GET** /storage/{locationId}/project/{projectId}/disk/{diskId}/event | List storage/disk.event
[**storage_project_disk_get**](StorageProjectDiskApi.md#storage_project_disk_get) | **GET** /storage/{locationId}/project/{projectId}/disk/{diskId} | Get storage/disk
[**storage_project_disk_list**](StorageProjectDiskApi.md#storage_project_disk_list) | **GET** /storage/{locationId}/project/{projectId}/disk | List storage/disk
[**storage_project_disk_metric_get**](StorageProjectDiskApi.md#storage_project_disk_metric_get) | **GET** /storage/{locationId}/project/{projectId}/disk/{diskId}/metric/{metricId} | Get storage/disk.metric
[**storage_project_disk_metric_list**](StorageProjectDiskApi.md#storage_project_disk_metric_list) | **GET** /storage/{locationId}/project/{projectId}/disk/{diskId}/metric | List storage/disk.metric
[**storage_project_disk_metric_point_list**](StorageProjectDiskApi.md#storage_project_disk_metric_point_list) | **GET** /storage/{locationId}/project/{projectId}/disk/{diskId}/metric/{metricId}/point | List storage/disk.point
[**storage_project_disk_resize**](StorageProjectDiskApi.md#storage_project_disk_resize) | **POST** /storage/{locationId}/project/{projectId}/disk/{diskId}/actions/resize | Resize storage/disk
[**storage_project_disk_service_get**](StorageProjectDiskApi.md#storage_project_disk_service_get) | **GET** /storage/{locationId}/project/{projectId}/disk/{diskId}/service/{serviceId} | Get storage/disk.service
[**storage_project_disk_service_list**](StorageProjectDiskApi.md#storage_project_disk_service_list) | **GET** /storage/{locationId}/project/{projectId}/disk/{diskId}/service | List storage/disk.service
[**storage_project_disk_tag_create**](StorageProjectDiskApi.md#storage_project_disk_tag_create) | **POST** /storage/{locationId}/project/{projectId}/disk/{diskId}/tag | Create storage/disk.tag
[**storage_project_disk_tag_delete**](StorageProjectDiskApi.md#storage_project_disk_tag_delete) | **DELETE** /storage/{locationId}/project/{projectId}/disk/{diskId}/tag/{tagId} | Delete storage/disk.tag
[**storage_project_disk_tag_get**](StorageProjectDiskApi.md#storage_project_disk_tag_get) | **GET** /storage/{locationId}/project/{projectId}/disk/{diskId}/tag/{tagId} | Get storage/disk.tag
[**storage_project_disk_tag_list**](StorageProjectDiskApi.md#storage_project_disk_tag_list) | **GET** /storage/{locationId}/project/{projectId}/disk/{diskId}/tag | List storage/disk.tag
[**storage_project_disk_tag_put**](StorageProjectDiskApi.md#storage_project_disk_tag_put) | **PUT** /storage/{locationId}/project/{projectId}/disk/{diskId}/tag | Replace storage/disk.tag
[**storage_project_disk_transfer**](StorageProjectDiskApi.md#storage_project_disk_transfer) | **POST** /storage/{locationId}/project/{projectId}/disk/{diskId}/actions/transfer | Transfer storage/disk
[**storage_project_disk_update**](StorageProjectDiskApi.md#storage_project_disk_update) | **PATCH** /storage/{locationId}/project/{projectId}/disk/{diskId} | Update storage/disk


# **storage_project_disk_attach**
> Disk storage_project_disk_attach(project_id, location_id, disk_id, storage_project_disk_attach, x_idempotency_key=x_idempotency_key)

Attach storage/disk

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id
storage_project_disk_attach = h1-client-python.StorageProjectDiskAttach() # StorageProjectDiskAttach | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Attach storage/disk
        api_response = api_instance.storage_project_disk_attach(project_id, location_id, disk_id, storage_project_disk_attach, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_attach: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 
 **storage_project_disk_attach** | [**StorageProjectDiskAttach**](StorageProjectDiskAttach.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Disk**](Disk.md)

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

# **storage_project_disk_create**
> Disk storage_project_disk_create(project_id, location_id, storage_project_disk_create, x_idempotency_key=x_idempotency_key)

Create storage/disk

Create disk

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
storage_project_disk_create = h1-client-python.StorageProjectDiskCreate() # StorageProjectDiskCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create storage/disk
        api_response = api_instance.storage_project_disk_create(project_id, location_id, storage_project_disk_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **storage_project_disk_create** | [**StorageProjectDiskCreate**](StorageProjectDiskCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Disk**](Disk.md)

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

# **storage_project_disk_delete**
> storage_project_disk_delete(project_id, location_id, disk_id)

Delete storage/disk

Delete disk

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id

    try:
        # Delete storage/disk
        api_instance.storage_project_disk_delete(project_id, location_id, disk_id)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 

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

# **storage_project_disk_detach**
> Disk storage_project_disk_detach(project_id, location_id, disk_id, x_idempotency_key=x_idempotency_key)

Detach storage/disk

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Detach storage/disk
        api_response = api_instance.storage_project_disk_detach(project_id, location_id, disk_id, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_detach: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Disk**](Disk.md)

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

# **storage_project_disk_download**
> storage_project_disk_download(project_id, location_id, disk_id, x_idempotency_key=x_idempotency_key)

Download storage/disk

action download

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Download storage/disk
        api_instance.storage_project_disk_download(project_id, location_id, disk_id, x_idempotency_key=x_idempotency_key)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

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
**201** | Download request accepted |  * location - Absolute URL <br>  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_project_disk_event_get**
> Event storage_project_disk_event_get(project_id, location_id, disk_id, event_id)

Get storage/disk.event

Get storage/disk.event

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get storage/disk.event
        api_response = api_instance.storage_project_disk_event_get(project_id, location_id, disk_id, event_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 
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

# **storage_project_disk_event_list**
> list[Event] storage_project_disk_event_list(project_id, location_id, disk_id, limit=limit, skip=skip)

List storage/disk.event

List storage/disk.event

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List storage/disk.event
        api_response = api_instance.storage_project_disk_event_list(project_id, location_id, disk_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 
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

# **storage_project_disk_get**
> Disk storage_project_disk_get(project_id, location_id, disk_id)

Get storage/disk

Returns a single disk

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id

    try:
        # Get storage/disk
        api_response = api_instance.storage_project_disk_get(project_id, location_id, disk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 

### Return type

[**Disk**](Disk.md)

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

# **storage_project_disk_list**
> list[Disk] storage_project_disk_list(project_id, location_id, name=name, vm=vm, tag_value=tag_value, tag_key=tag_key)

List storage/disk

List disk

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
name = 'name_example' # str | Filter by name (optional)
vm = 'vm_example' # str | Filter by vm (optional)
tag_value = 'tag_value_example' # str | Filter by tag.value (optional)
tag_key = 'tag_key_example' # str | Filter by tag.key (optional)

    try:
        # List storage/disk
        api_response = api_instance.storage_project_disk_list(project_id, location_id, name=name, vm=vm, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **name** | **str**| Filter by name | [optional] 
 **vm** | **str**| Filter by vm | [optional] 
 **tag_value** | **str**| Filter by tag.value | [optional] 
 **tag_key** | **str**| Filter by tag.key | [optional] 

### Return type

[**list[Disk]**](Disk.md)

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

# **storage_project_disk_metric_get**
> Metric storage_project_disk_metric_get(project_id, location_id, disk_id, metric_id)

Get storage/disk.metric

Get storage/disk.metric

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id
metric_id = 'metric_id_example' # str | metricId

    try:
        # Get storage/disk.metric
        api_response = api_instance.storage_project_disk_metric_get(project_id, location_id, disk_id, metric_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_metric_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 
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

# **storage_project_disk_metric_list**
> list[Metric] storage_project_disk_metric_list(project_id, location_id, disk_id)

List storage/disk.metric

List storage/disk.metric

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id

    try:
        # List storage/disk.metric
        api_response = api_instance.storage_project_disk_metric_list(project_id, location_id, disk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_metric_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 

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

# **storage_project_disk_metric_point_list**
> list[Serie] storage_project_disk_metric_point_list(project_id, location_id, disk_id, metric_id, interval=interval, timespan=timespan)

List storage/disk.point

List storage/disk.point

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id
metric_id = 'metric_id_example' # str | metricId
interval = 'interval_example' # str | interval (optional)
timespan = 'timespan_example' # str | timespan (optional)

    try:
        # List storage/disk.point
        api_response = api_instance.storage_project_disk_metric_point_list(project_id, location_id, disk_id, metric_id, interval=interval, timespan=timespan)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_metric_point_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 
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

# **storage_project_disk_resize**
> Disk storage_project_disk_resize(project_id, location_id, disk_id, storage_project_disk_resize, x_idempotency_key=x_idempotency_key)

Resize storage/disk

action resize

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id
storage_project_disk_resize = h1-client-python.StorageProjectDiskResize() # StorageProjectDiskResize | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Resize storage/disk
        api_response = api_instance.storage_project_disk_resize(project_id, location_id, disk_id, storage_project_disk_resize, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_resize: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 
 **storage_project_disk_resize** | [**StorageProjectDiskResize**](StorageProjectDiskResize.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Disk**](Disk.md)

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

# **storage_project_disk_service_get**
> ResourceService storage_project_disk_service_get(project_id, location_id, disk_id, service_id)

Get storage/disk.service

Get storage/disk.service

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id
service_id = 'service_id_example' # str | serviceId

    try:
        # Get storage/disk.service
        api_response = api_instance.storage_project_disk_service_get(project_id, location_id, disk_id, service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 
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

# **storage_project_disk_service_list**
> list[ResourceService] storage_project_disk_service_list(project_id, location_id, disk_id)

List storage/disk.service

List storage/disk.service

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id

    try:
        # List storage/disk.service
        api_response = api_instance.storage_project_disk_service_list(project_id, location_id, disk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 

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

# **storage_project_disk_tag_create**
> Tag storage_project_disk_tag_create(project_id, location_id, disk_id, tag)

Create storage/disk.tag

Create storage/disk.tag

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id
tag = h1-client-python.Tag() # Tag | 

    try:
        # Create storage/disk.tag
        api_response = api_instance.storage_project_disk_tag_create(project_id, location_id, disk_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 
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

# **storage_project_disk_tag_delete**
> storage_project_disk_tag_delete(project_id, location_id, disk_id, tag_id)

Delete storage/disk.tag

Delete storage/disk.tag

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Delete storage/disk.tag
        api_instance.storage_project_disk_tag_delete(project_id, location_id, disk_id, tag_id)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 
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

# **storage_project_disk_tag_get**
> Tag storage_project_disk_tag_get(project_id, location_id, disk_id, tag_id)

Get storage/disk.tag

Get storage/disk.tag

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Get storage/disk.tag
        api_response = api_instance.storage_project_disk_tag_get(project_id, location_id, disk_id, tag_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 
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

# **storage_project_disk_tag_list**
> list[Tag] storage_project_disk_tag_list(project_id, location_id, disk_id)

List storage/disk.tag

List storage/disk.tag

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id

    try:
        # List storage/disk.tag
        api_response = api_instance.storage_project_disk_tag_list(project_id, location_id, disk_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 

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

# **storage_project_disk_tag_put**
> list[Tag] storage_project_disk_tag_put(project_id, location_id, disk_id, tag)

Replace storage/disk.tag

Replace storage/disk.tag

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id
tag = [h1-client-python.Tag()] # list[Tag] | 

    try:
        # Replace storage/disk.tag
        api_response = api_instance.storage_project_disk_tag_put(project_id, location_id, disk_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 
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

# **storage_project_disk_transfer**
> Disk storage_project_disk_transfer(project_id, location_id, disk_id, storage_project_disk_transfer, x_idempotency_key=x_idempotency_key)

Transfer storage/disk

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id
storage_project_disk_transfer = h1-client-python.StorageProjectDiskTransfer() # StorageProjectDiskTransfer | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Transfer storage/disk
        api_response = api_instance.storage_project_disk_transfer(project_id, location_id, disk_id, storage_project_disk_transfer, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 
 **storage_project_disk_transfer** | [**StorageProjectDiskTransfer**](StorageProjectDiskTransfer.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Disk**](Disk.md)

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

# **storage_project_disk_update**
> Disk storage_project_disk_update(project_id, location_id, disk_id, storage_project_disk_update)

Update storage/disk

Returns modified disk

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
    api_instance = h1-client-python.StorageProjectDiskApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
disk_id = 'disk_id_example' # str | Disk Id
storage_project_disk_update = h1-client-python.StorageProjectDiskUpdate() # StorageProjectDiskUpdate | 

    try:
        # Update storage/disk
        api_response = api_instance.storage_project_disk_update(project_id, location_id, disk_id, storage_project_disk_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectDiskApi->storage_project_disk_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **disk_id** | **str**| Disk Id | 
 **storage_project_disk_update** | [**StorageProjectDiskUpdate**](StorageProjectDiskUpdate.md)|  | 

### Return type

[**Disk**](Disk.md)

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

