# h1.NetworkingProjectNetgwApi

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
> Netgw networking_project_netgw_attach(project_id, location_id, netgw_id, networking_project_netgw_attach)

Attach networking/netgw

action attach

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_netgw_api
from h1.model.networking_project_netgw_attach import NetworkingProjectNetgwAttach
from h1.model.netgw import Netgw
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    netgw_id = "netgwId_example" # str | Netgw Id
    networking_project_netgw_attach = NetworkingProjectNetgwAttach(
        private=NetgwPrivate(
            network="network_example",
        ),
    ) # NetworkingProjectNetgwAttach | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Attach networking/netgw
        api_response = api_instance.networking_project_netgw_attach(project_id, location_id, netgw_id, networking_project_netgw_attach)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_attach: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Attach networking/netgw
        api_response = api_instance.networking_project_netgw_attach(project_id, location_id, netgw_id, networking_project_netgw_attach, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
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
 **x_dry_run** | **str**| Dry run | [optional]

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
> Netgw networking_project_netgw_create(project_id, location_id, networking_project_netgw_create)

Create networking/netgw

Create netgw

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_netgw_api
from h1.model.networking_project_netgw_create import NetworkingProjectNetgwCreate
from h1.model.netgw import Netgw
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    networking_project_netgw_create = NetworkingProjectNetgwCreate(
        name="name_example",
        public=NetgwPublic(
            ip="ip_example",
        ),
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # NetworkingProjectNetgwCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create networking/netgw
        api_response = api_instance.networking_project_netgw_create(project_id, location_id, networking_project_netgw_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create networking/netgw
        api_response = api_instance.networking_project_netgw_create(project_id, location_id, networking_project_netgw_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **networking_project_netgw_create** | [**NetworkingProjectNetgwCreate**](NetworkingProjectNetgwCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import networking_project_netgw_api
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    netgw_id = "netgwId_example" # str | Netgw Id

    # example passing only required values which don't have defaults set
    try:
        # Delete networking/netgw
        api_instance.networking_project_netgw_delete(project_id, location_id, netgw_id)
    except h1.ApiException as e:
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
> Netgw networking_project_netgw_detach(project_id, location_id, netgw_id)

Detach networking/netgw

action detach

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_netgw_api
from h1.model.netgw import Netgw
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    netgw_id = "netgwId_example" # str | Netgw Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Detach networking/netgw
        api_response = api_instance.networking_project_netgw_detach(project_id, location_id, netgw_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_detach: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Detach networking/netgw
        api_response = api_instance.networking_project_netgw_detach(project_id, location_id, netgw_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_detach: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **netgw_id** | **str**| Netgw Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import networking_project_netgw_api
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    netgw_id = "netgwId_example" # str | Netgw Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get networking/netgw.event
        api_response = api_instance.networking_project_netgw_event_get(project_id, location_id, netgw_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Event] networking_project_netgw_event_list(project_id, location_id, netgw_id)

List networking/netgw.event

List networking/netgw.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_netgw_api
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    netgw_id = "netgwId_example" # str | Netgw Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List networking/netgw.event
        api_response = api_instance.networking_project_netgw_event_list(project_id, location_id, netgw_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List networking/netgw.event
        api_response = api_instance.networking_project_netgw_event_list(project_id, location_id, netgw_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **netgw_id** | **str**| Netgw Id |
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

# **networking_project_netgw_get**
> Netgw networking_project_netgw_get(project_id, location_id, netgw_id)

Get networking/netgw

Returns a single netgw

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_netgw_api
from h1.model.netgw import Netgw
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    netgw_id = "netgwId_example" # str | Netgw Id

    # example passing only required values which don't have defaults set
    try:
        # Get networking/netgw
        api_response = api_instance.networking_project_netgw_get(project_id, location_id, netgw_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Netgw] networking_project_netgw_list(project_id, location_id)

List networking/netgw

List netgw

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_netgw_api
from h1.model.netgw import Netgw
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List networking/netgw
        api_response = api_instance.networking_project_netgw_list(project_id, location_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List networking/netgw
        api_response = api_instance.networking_project_netgw_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
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

[**[Netgw]**](Netgw.md)

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
import time
import h1
from h1.api import networking_project_netgw_api
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    netgw_id = "netgwId_example" # str | Netgw Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get networking/netgw.service
        api_response = api_instance.networking_project_netgw_service_get(project_id, location_id, netgw_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [ResourceService] networking_project_netgw_service_list(project_id, location_id, netgw_id)

List networking/netgw.service

List networking/netgw.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_netgw_api
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    netgw_id = "netgwId_example" # str | Netgw Id

    # example passing only required values which don't have defaults set
    try:
        # List networking/netgw.service
        api_response = api_instance.networking_project_netgw_service_list(project_id, location_id, netgw_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **netgw_id** | **str**| Netgw Id |

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

# **networking_project_netgw_tag_create**
> Tag networking_project_netgw_tag_create(project_id, location_id, netgw_id, tag)

Create networking/netgw.tag

Create networking/netgw.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_netgw_api
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    netgw_id = "netgwId_example" # str | Netgw Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create networking/netgw.tag
        api_response = api_instance.networking_project_netgw_tag_create(project_id, location_id, netgw_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import networking_project_netgw_api
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    netgw_id = "netgwId_example" # str | Netgw Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete networking/netgw.tag
        api_instance.networking_project_netgw_tag_delete(project_id, location_id, netgw_id, tag_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import networking_project_netgw_api
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    netgw_id = "netgwId_example" # str | Netgw Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get networking/netgw.tag
        api_response = api_instance.networking_project_netgw_tag_get(project_id, location_id, netgw_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Tag] networking_project_netgw_tag_list(project_id, location_id, netgw_id)

List networking/netgw.tag

List networking/netgw.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_netgw_api
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    netgw_id = "netgwId_example" # str | Netgw Id

    # example passing only required values which don't have defaults set
    try:
        # List networking/netgw.tag
        api_response = api_instance.networking_project_netgw_tag_list(project_id, location_id, netgw_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **netgw_id** | **str**| Netgw Id |

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

# **networking_project_netgw_tag_put**
> [Tag] networking_project_netgw_tag_put(project_id, location_id, netgw_id, tag_array)

Replace networking/netgw.tag

Replace networking/netgw.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_netgw_api
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    netgw_id = "netgwId_example" # str | Netgw Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace networking/netgw.tag
        api_response = api_instance.networking_project_netgw_tag_put(project_id, location_id, netgw_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectNetgwApi->networking_project_netgw_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **netgw_id** | **str**| Netgw Id |
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

# **networking_project_netgw_update**
> Netgw networking_project_netgw_update(project_id, location_id, netgw_id, networking_project_netgw_update)

Update networking/netgw

Returns modified netgw

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_netgw_api
from h1.model.networking_project_netgw_update import NetworkingProjectNetgwUpdate
from h1.model.netgw import Netgw
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
    api_instance = networking_project_netgw_api.NetworkingProjectNetgwApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    netgw_id = "netgwId_example" # str | Netgw Id
    networking_project_netgw_update = NetworkingProjectNetgwUpdate(
        name="name_example",
    ) # NetworkingProjectNetgwUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update networking/netgw
        api_response = api_instance.networking_project_netgw_update(project_id, location_id, netgw_id, networking_project_netgw_update)
        pprint(api_response)
    except h1.ApiException as e:
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

