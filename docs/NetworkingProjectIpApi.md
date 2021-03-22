# h1.NetworkingProjectIpApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networking_project_ip_associate**](NetworkingProjectIpApi.md#networking_project_ip_associate) | **POST** /networking/{locationId}/project/{projectId}/ip/{ipId}/actions/associate | Associate networking/ip
[**networking_project_ip_create**](NetworkingProjectIpApi.md#networking_project_ip_create) | **POST** /networking/{locationId}/project/{projectId}/ip | Create networking/ip
[**networking_project_ip_delete**](NetworkingProjectIpApi.md#networking_project_ip_delete) | **DELETE** /networking/{locationId}/project/{projectId}/ip/{ipId} | Delete networking/ip
[**networking_project_ip_disassociate**](NetworkingProjectIpApi.md#networking_project_ip_disassociate) | **POST** /networking/{locationId}/project/{projectId}/ip/{ipId}/actions/disassociate | Disassociate networking/ip
[**networking_project_ip_event_get**](NetworkingProjectIpApi.md#networking_project_ip_event_get) | **GET** /networking/{locationId}/project/{projectId}/ip/{ipId}/event/{eventId} | Get networking/ip.event
[**networking_project_ip_event_list**](NetworkingProjectIpApi.md#networking_project_ip_event_list) | **GET** /networking/{locationId}/project/{projectId}/ip/{ipId}/event | List networking/ip.event
[**networking_project_ip_get**](NetworkingProjectIpApi.md#networking_project_ip_get) | **GET** /networking/{locationId}/project/{projectId}/ip/{ipId} | Get networking/ip
[**networking_project_ip_list**](NetworkingProjectIpApi.md#networking_project_ip_list) | **GET** /networking/{locationId}/project/{projectId}/ip | List networking/ip
[**networking_project_ip_persist**](NetworkingProjectIpApi.md#networking_project_ip_persist) | **POST** /networking/{locationId}/project/{projectId}/ip/{ipId}/actions/persist | Persist networking/ip
[**networking_project_ip_service_get**](NetworkingProjectIpApi.md#networking_project_ip_service_get) | **GET** /networking/{locationId}/project/{projectId}/ip/{ipId}/service/{serviceId} | Get networking/ip.service
[**networking_project_ip_service_list**](NetworkingProjectIpApi.md#networking_project_ip_service_list) | **GET** /networking/{locationId}/project/{projectId}/ip/{ipId}/service | List networking/ip.service
[**networking_project_ip_tag_create**](NetworkingProjectIpApi.md#networking_project_ip_tag_create) | **POST** /networking/{locationId}/project/{projectId}/ip/{ipId}/tag | Create networking/ip.tag
[**networking_project_ip_tag_delete**](NetworkingProjectIpApi.md#networking_project_ip_tag_delete) | **DELETE** /networking/{locationId}/project/{projectId}/ip/{ipId}/tag/{tagId} | Delete networking/ip.tag
[**networking_project_ip_tag_get**](NetworkingProjectIpApi.md#networking_project_ip_tag_get) | **GET** /networking/{locationId}/project/{projectId}/ip/{ipId}/tag/{tagId} | Get networking/ip.tag
[**networking_project_ip_tag_list**](NetworkingProjectIpApi.md#networking_project_ip_tag_list) | **GET** /networking/{locationId}/project/{projectId}/ip/{ipId}/tag | List networking/ip.tag
[**networking_project_ip_tag_put**](NetworkingProjectIpApi.md#networking_project_ip_tag_put) | **PUT** /networking/{locationId}/project/{projectId}/ip/{ipId}/tag | Replace networking/ip.tag
[**networking_project_ip_transfer**](NetworkingProjectIpApi.md#networking_project_ip_transfer) | **POST** /networking/{locationId}/project/{projectId}/ip/{ipId}/actions/transfer | Transfer networking/ip
[**networking_project_ip_update**](NetworkingProjectIpApi.md#networking_project_ip_update) | **PATCH** /networking/{locationId}/project/{projectId}/ip/{ipId} | Update networking/ip


# **networking_project_ip_associate**
> Ip networking_project_ip_associate(project_id, location_id, ip_id, networking_project_ip_associate)

Associate networking/ip

action associate

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
from h1.model.ip import Ip
from h1.model.networking_project_ip_associate import NetworkingProjectIpAssociate
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id
    networking_project_ip_associate = NetworkingProjectIpAssociate(
        ip="ip_example",
    ) # NetworkingProjectIpAssociate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Associate networking/ip
        api_response = api_instance.networking_project_ip_associate(project_id, location_id, ip_id, networking_project_ip_associate)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_associate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Associate networking/ip
        api_response = api_instance.networking_project_ip_associate(project_id, location_id, ip_id, networking_project_ip_associate, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_associate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |
 **networking_project_ip_associate** | [**NetworkingProjectIpAssociate**](NetworkingProjectIpAssociate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Ip**](Ip.md)

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

# **networking_project_ip_create**
> Ip networking_project_ip_create(project_id, location_id, networking_project_ip_create)

Create networking/ip

Create ip

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
from h1.model.ip import Ip
from h1.model.networking_project_ip_create import NetworkingProjectIpCreate
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    networking_project_ip_create = NetworkingProjectIpCreate(
        network="network_example",
        ptr_record="ptr_record_example",
        address="address_example",
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # NetworkingProjectIpCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create networking/ip
        api_response = api_instance.networking_project_ip_create(project_id, location_id, networking_project_ip_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create networking/ip
        api_response = api_instance.networking_project_ip_create(project_id, location_id, networking_project_ip_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **networking_project_ip_create** | [**NetworkingProjectIpCreate**](NetworkingProjectIpCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Ip**](Ip.md)

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

# **networking_project_ip_delete**
> networking_project_ip_delete(project_id, location_id, ip_id)

Delete networking/ip

Delete ip

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id

    # example passing only required values which don't have defaults set
    try:
        # Delete networking/ip
        api_instance.networking_project_ip_delete(project_id, location_id, ip_id)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |

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

# **networking_project_ip_disassociate**
> Ip networking_project_ip_disassociate(project_id, location_id, ip_id)

Disassociate networking/ip

action disassociate

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
from h1.model.ip import Ip
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Disassociate networking/ip
        api_response = api_instance.networking_project_ip_disassociate(project_id, location_id, ip_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_disassociate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Disassociate networking/ip
        api_response = api_instance.networking_project_ip_disassociate(project_id, location_id, ip_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_disassociate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Ip**](Ip.md)

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

# **networking_project_ip_event_get**
> Event networking_project_ip_event_get(project_id, location_id, ip_id, event_id)

Get networking/ip.event

Get networking/ip.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get networking/ip.event
        api_response = api_instance.networking_project_ip_event_get(project_id, location_id, ip_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_event_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |
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

# **networking_project_ip_event_list**
> [Event] networking_project_ip_event_list(project_id, location_id, ip_id)

List networking/ip.event

List networking/ip.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List networking/ip.event
        api_response = api_instance.networking_project_ip_event_list(project_id, location_id, ip_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List networking/ip.event
        api_response = api_instance.networking_project_ip_event_list(project_id, location_id, ip_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |
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

# **networking_project_ip_get**
> Ip networking_project_ip_get(project_id, location_id, ip_id)

Get networking/ip

Returns a single ip

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
from h1.model.ip import Ip
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id

    # example passing only required values which don't have defaults set
    try:
        # Get networking/ip
        api_response = api_instance.networking_project_ip_get(project_id, location_id, ip_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |

### Return type

[**Ip**](Ip.md)

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

# **networking_project_ip_list**
> [Ip] networking_project_ip_list(project_id, location_id)

List networking/ip

List ip

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
from h1.model.ip import Ip
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    network = "network_example" # str | Filter by network (optional)
    associated_netadp = "associated.netadp_example" # str | Filter by associated.netadp (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List networking/ip
        api_response = api_instance.networking_project_ip_list(project_id, location_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List networking/ip
        api_response = api_instance.networking_project_ip_list(project_id, location_id, network=network, associated_netadp=associated_netadp, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **network** | **str**| Filter by network | [optional]
 **associated_netadp** | **str**| Filter by associated.netadp | [optional]
 **tag_value** | **str**| Filter by tag.value | [optional]
 **tag_key** | **str**| Filter by tag.key | [optional]

### Return type

[**[Ip]**](Ip.md)

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

# **networking_project_ip_persist**
> Ip networking_project_ip_persist(project_id, location_id, ip_id)

Persist networking/ip

action persist

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
from h1.model.ip import Ip
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Persist networking/ip
        api_response = api_instance.networking_project_ip_persist(project_id, location_id, ip_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_persist: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Persist networking/ip
        api_response = api_instance.networking_project_ip_persist(project_id, location_id, ip_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_persist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Ip**](Ip.md)

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

# **networking_project_ip_service_get**
> ResourceService networking_project_ip_service_get(project_id, location_id, ip_id, service_id)

Get networking/ip.service

Get networking/ip.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get networking/ip.service
        api_response = api_instance.networking_project_ip_service_get(project_id, location_id, ip_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |
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

# **networking_project_ip_service_list**
> [ResourceService] networking_project_ip_service_list(project_id, location_id, ip_id)

List networking/ip.service

List networking/ip.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id

    # example passing only required values which don't have defaults set
    try:
        # List networking/ip.service
        api_response = api_instance.networking_project_ip_service_list(project_id, location_id, ip_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |

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

# **networking_project_ip_tag_create**
> Tag networking_project_ip_tag_create(project_id, location_id, ip_id, tag)

Create networking/ip.tag

Create networking/ip.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create networking/ip.tag
        api_response = api_instance.networking_project_ip_tag_create(project_id, location_id, ip_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_tag_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |
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

# **networking_project_ip_tag_delete**
> networking_project_ip_tag_delete(project_id, location_id, ip_id, tag_id)

Delete networking/ip.tag

Delete networking/ip.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete networking/ip.tag
        api_instance.networking_project_ip_tag_delete(project_id, location_id, ip_id, tag_id)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_tag_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |
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

# **networking_project_ip_tag_get**
> Tag networking_project_ip_tag_get(project_id, location_id, ip_id, tag_id)

Get networking/ip.tag

Get networking/ip.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get networking/ip.tag
        api_response = api_instance.networking_project_ip_tag_get(project_id, location_id, ip_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_tag_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |
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

# **networking_project_ip_tag_list**
> [Tag] networking_project_ip_tag_list(project_id, location_id, ip_id)

List networking/ip.tag

List networking/ip.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id

    # example passing only required values which don't have defaults set
    try:
        # List networking/ip.tag
        api_response = api_instance.networking_project_ip_tag_list(project_id, location_id, ip_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_tag_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |

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

# **networking_project_ip_tag_put**
> [Tag] networking_project_ip_tag_put(project_id, location_id, ip_id, tag_array)

Replace networking/ip.tag

Replace networking/ip.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace networking/ip.tag
        api_response = api_instance.networking_project_ip_tag_put(project_id, location_id, ip_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_tag_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |
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

# **networking_project_ip_transfer**
> Ip networking_project_ip_transfer(project_id, location_id, ip_id, networking_project_ip_transfer)

Transfer networking/ip

action transfer

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
from h1.model.ip import Ip
from h1.model.networking_project_ip_transfer import NetworkingProjectIpTransfer
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id
    networking_project_ip_transfer = NetworkingProjectIpTransfer(
        project="project_example",
    ) # NetworkingProjectIpTransfer | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Transfer networking/ip
        api_response = api_instance.networking_project_ip_transfer(project_id, location_id, ip_id, networking_project_ip_transfer)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_transfer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Transfer networking/ip
        api_response = api_instance.networking_project_ip_transfer(project_id, location_id, ip_id, networking_project_ip_transfer, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_transfer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |
 **networking_project_ip_transfer** | [**NetworkingProjectIpTransfer**](NetworkingProjectIpTransfer.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Ip**](Ip.md)

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

# **networking_project_ip_update**
> Ip networking_project_ip_update(project_id, location_id, ip_id, networking_project_ip_update)

Update networking/ip

Returns modified ip

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_ip_api
from h1.model.ip import Ip
from h1.model.networking_project_ip_update import NetworkingProjectIpUpdate
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
    api_instance = networking_project_ip_api.NetworkingProjectIpApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    ip_id = "ipId_example" # str | Ip Id
    networking_project_ip_update = NetworkingProjectIpUpdate(
        ptr_record="ptr_record_example",
    ) # NetworkingProjectIpUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update networking/ip
        api_response = api_instance.networking_project_ip_update(project_id, location_id, ip_id, networking_project_ip_update)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectIpApi->networking_project_ip_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **ip_id** | **str**| Ip Id |
 **networking_project_ip_update** | [**NetworkingProjectIpUpdate**](NetworkingProjectIpUpdate.md)|  |

### Return type

[**Ip**](Ip.md)

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

