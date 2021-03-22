# h1.StorageProjectIsoApi

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
> Iso storage_project_iso_create(project_id, location_id, storage_project_iso_create)

Create storage/iso

Create iso

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_iso_api
from h1.model.iso import Iso
from h1.model.storage_project_iso_create import StorageProjectIsoCreate
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    storage_project_iso_create = StorageProjectIsoCreate(
        name="name_example",
        source="source_example",
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # StorageProjectIsoCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create storage/iso
        api_response = api_instance.storage_project_iso_create(project_id, location_id, storage_project_iso_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create storage/iso
        api_response = api_instance.storage_project_iso_create(project_id, location_id, storage_project_iso_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **storage_project_iso_create** | [**StorageProjectIsoCreate**](StorageProjectIsoCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import storage_project_iso_api
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    iso_id = "isoId_example" # str | Iso Id

    # example passing only required values which don't have defaults set
    try:
        # Delete storage/iso
        api_instance.storage_project_iso_delete(project_id, location_id, iso_id)
    except h1.ApiException as e:
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
> Iso storage_project_iso_detach(project_id, location_id, iso_id, storage_project_iso_detach)

Detach storage/iso

action detach

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_iso_api
from h1.model.storage_project_iso_detach import StorageProjectIsoDetach
from h1.model.iso import Iso
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    iso_id = "isoId_example" # str | Iso Id
    storage_project_iso_detach = StorageProjectIsoDetach(
        vm="vm_example",
    ) # StorageProjectIsoDetach | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Detach storage/iso
        api_response = api_instance.storage_project_iso_detach(project_id, location_id, iso_id, storage_project_iso_detach)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_detach: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Detach storage/iso
        api_response = api_instance.storage_project_iso_detach(project_id, location_id, iso_id, storage_project_iso_detach, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
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
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import storage_project_iso_api
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    iso_id = "isoId_example" # str | Iso Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get storage/iso.event
        api_response = api_instance.storage_project_iso_event_get(project_id, location_id, iso_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Event] storage_project_iso_event_list(project_id, location_id, iso_id)

List storage/iso.event

List storage/iso.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_iso_api
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    iso_id = "isoId_example" # str | Iso Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List storage/iso.event
        api_response = api_instance.storage_project_iso_event_list(project_id, location_id, iso_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List storage/iso.event
        api_response = api_instance.storage_project_iso_event_list(project_id, location_id, iso_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **iso_id** | **str**| Iso Id |
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

# **storage_project_iso_get**
> Iso storage_project_iso_get(project_id, location_id, iso_id)

Get storage/iso

Returns a single iso

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_iso_api
from h1.model.iso import Iso
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    iso_id = "isoId_example" # str | Iso Id

    # example passing only required values which don't have defaults set
    try:
        # Get storage/iso
        api_response = api_instance.storage_project_iso_get(project_id, location_id, iso_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Iso] storage_project_iso_list(project_id, location_id)

List storage/iso

List iso

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_iso_api
from h1.model.iso import Iso
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List storage/iso
        api_response = api_instance.storage_project_iso_list(project_id, location_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List storage/iso
        api_response = api_instance.storage_project_iso_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
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

[**[Iso]**](Iso.md)

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
import time
import h1
from h1.api import storage_project_iso_api
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    iso_id = "isoId_example" # str | Iso Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get storage/iso.service
        api_response = api_instance.storage_project_iso_service_get(project_id, location_id, iso_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [ResourceService] storage_project_iso_service_list(project_id, location_id, iso_id)

List storage/iso.service

List storage/iso.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_iso_api
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    iso_id = "isoId_example" # str | Iso Id

    # example passing only required values which don't have defaults set
    try:
        # List storage/iso.service
        api_response = api_instance.storage_project_iso_service_list(project_id, location_id, iso_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **iso_id** | **str**| Iso Id |

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

# **storage_project_iso_tag_create**
> Tag storage_project_iso_tag_create(project_id, location_id, iso_id, tag)

Create storage/iso.tag

Create storage/iso.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_iso_api
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    iso_id = "isoId_example" # str | Iso Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create storage/iso.tag
        api_response = api_instance.storage_project_iso_tag_create(project_id, location_id, iso_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import storage_project_iso_api
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    iso_id = "isoId_example" # str | Iso Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete storage/iso.tag
        api_instance.storage_project_iso_tag_delete(project_id, location_id, iso_id, tag_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import storage_project_iso_api
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    iso_id = "isoId_example" # str | Iso Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get storage/iso.tag
        api_response = api_instance.storage_project_iso_tag_get(project_id, location_id, iso_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Tag] storage_project_iso_tag_list(project_id, location_id, iso_id)

List storage/iso.tag

List storage/iso.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_iso_api
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    iso_id = "isoId_example" # str | Iso Id

    # example passing only required values which don't have defaults set
    try:
        # List storage/iso.tag
        api_response = api_instance.storage_project_iso_tag_list(project_id, location_id, iso_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_tag_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **iso_id** | **str**| Iso Id |

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

# **storage_project_iso_tag_put**
> [Tag] storage_project_iso_tag_put(project_id, location_id, iso_id, tag_array)

Replace storage/iso.tag

Replace storage/iso.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_iso_api
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    iso_id = "isoId_example" # str | Iso Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace storage/iso.tag
        api_response = api_instance.storage_project_iso_tag_put(project_id, location_id, iso_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_tag_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **iso_id** | **str**| Iso Id |
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

# **storage_project_iso_transfer**
> Iso storage_project_iso_transfer(project_id, location_id, iso_id, storage_project_iso_transfer)

Transfer storage/iso

action transfer

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_iso_api
from h1.model.iso import Iso
from h1.model.storage_project_iso_transfer import StorageProjectIsoTransfer
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    iso_id = "isoId_example" # str | Iso Id
    storage_project_iso_transfer = StorageProjectIsoTransfer(
        project="project_example",
    ) # StorageProjectIsoTransfer | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Transfer storage/iso
        api_response = api_instance.storage_project_iso_transfer(project_id, location_id, iso_id, storage_project_iso_transfer)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectIsoApi->storage_project_iso_transfer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Transfer storage/iso
        api_response = api_instance.storage_project_iso_transfer(project_id, location_id, iso_id, storage_project_iso_transfer, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
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
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import storage_project_iso_api
from h1.model.iso import Iso
from h1.model.storage_project_iso_update import StorageProjectIsoUpdate
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
    api_instance = storage_project_iso_api.StorageProjectIsoApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    iso_id = "isoId_example" # str | Iso Id
    storage_project_iso_update = StorageProjectIsoUpdate(
        name="name_example",
    ) # StorageProjectIsoUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update storage/iso
        api_response = api_instance.storage_project_iso_update(project_id, location_id, iso_id, storage_project_iso_update)
        pprint(api_response)
    except h1.ApiException as e:
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

