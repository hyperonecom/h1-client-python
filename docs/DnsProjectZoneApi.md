# h1-client-python.DnsProjectZoneApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dns_project_zone_create**](DnsProjectZoneApi.md#dns_project_zone_create) | **POST** /dns/{locationId}/project/{projectId}/zone | Create dns/zone
[**dns_project_zone_delete**](DnsProjectZoneApi.md#dns_project_zone_delete) | **DELETE** /dns/{locationId}/project/{projectId}/zone/{zoneId} | Delete dns/zone
[**dns_project_zone_event_get**](DnsProjectZoneApi.md#dns_project_zone_event_get) | **GET** /dns/{locationId}/project/{projectId}/zone/{zoneId}/event/{eventId} | Get dns/zone.event
[**dns_project_zone_event_list**](DnsProjectZoneApi.md#dns_project_zone_event_list) | **GET** /dns/{locationId}/project/{projectId}/zone/{zoneId}/event | List dns/zone.event
[**dns_project_zone_get**](DnsProjectZoneApi.md#dns_project_zone_get) | **GET** /dns/{locationId}/project/{projectId}/zone/{zoneId} | Get dns/zone
[**dns_project_zone_list**](DnsProjectZoneApi.md#dns_project_zone_list) | **GET** /dns/{locationId}/project/{projectId}/zone | List dns/zone
[**dns_project_zone_recordset_create**](DnsProjectZoneApi.md#dns_project_zone_recordset_create) | **POST** /dns/{locationId}/project/{projectId}/zone/{zoneId}/recordset | Create dns/zone.recordset
[**dns_project_zone_recordset_delete**](DnsProjectZoneApi.md#dns_project_zone_recordset_delete) | **DELETE** /dns/{locationId}/project/{projectId}/zone/{zoneId}/recordset/{recordsetId} | Delete dns/zone.recordset
[**dns_project_zone_recordset_get**](DnsProjectZoneApi.md#dns_project_zone_recordset_get) | **GET** /dns/{locationId}/project/{projectId}/zone/{zoneId}/recordset/{recordsetId} | Get dns/zone.recordset
[**dns_project_zone_recordset_list**](DnsProjectZoneApi.md#dns_project_zone_recordset_list) | **GET** /dns/{locationId}/project/{projectId}/zone/{zoneId}/recordset | List dns/zone.recordset
[**dns_project_zone_recordset_patch**](DnsProjectZoneApi.md#dns_project_zone_recordset_patch) | **PATCH** /dns/{locationId}/project/{projectId}/zone/{zoneId}/recordset/{recordsetId} | Update dns/zone.recordset
[**dns_project_zone_recordset_record_create**](DnsProjectZoneApi.md#dns_project_zone_recordset_record_create) | **POST** /dns/{locationId}/project/{projectId}/zone/{zoneId}/recordset/{recordsetId}/record | Create dns/zone.record
[**dns_project_zone_recordset_record_delete**](DnsProjectZoneApi.md#dns_project_zone_recordset_record_delete) | **DELETE** /dns/{locationId}/project/{projectId}/zone/{zoneId}/recordset/{recordsetId}/record/{recordId} | Delete dns/zone.record
[**dns_project_zone_recordset_record_get**](DnsProjectZoneApi.md#dns_project_zone_recordset_record_get) | **GET** /dns/{locationId}/project/{projectId}/zone/{zoneId}/recordset/{recordsetId}/record/{recordId} | Get dns/zone.record
[**dns_project_zone_recordset_record_list**](DnsProjectZoneApi.md#dns_project_zone_recordset_record_list) | **GET** /dns/{locationId}/project/{projectId}/zone/{zoneId}/recordset/{recordsetId}/record | List dns/zone.record
[**dns_project_zone_recordset_record_put**](DnsProjectZoneApi.md#dns_project_zone_recordset_record_put) | **PUT** /dns/{locationId}/project/{projectId}/zone/{zoneId}/recordset/{recordsetId}/record | Replace dns/zone.record
[**dns_project_zone_service_get**](DnsProjectZoneApi.md#dns_project_zone_service_get) | **GET** /dns/{locationId}/project/{projectId}/zone/{zoneId}/service/{serviceId} | Get dns/zone.service
[**dns_project_zone_service_list**](DnsProjectZoneApi.md#dns_project_zone_service_list) | **GET** /dns/{locationId}/project/{projectId}/zone/{zoneId}/service | List dns/zone.service
[**dns_project_zone_tag_create**](DnsProjectZoneApi.md#dns_project_zone_tag_create) | **POST** /dns/{locationId}/project/{projectId}/zone/{zoneId}/tag | Create dns/zone.tag
[**dns_project_zone_tag_delete**](DnsProjectZoneApi.md#dns_project_zone_tag_delete) | **DELETE** /dns/{locationId}/project/{projectId}/zone/{zoneId}/tag/{tagId} | Delete dns/zone.tag
[**dns_project_zone_tag_get**](DnsProjectZoneApi.md#dns_project_zone_tag_get) | **GET** /dns/{locationId}/project/{projectId}/zone/{zoneId}/tag/{tagId} | Get dns/zone.tag
[**dns_project_zone_tag_list**](DnsProjectZoneApi.md#dns_project_zone_tag_list) | **GET** /dns/{locationId}/project/{projectId}/zone/{zoneId}/tag | List dns/zone.tag
[**dns_project_zone_tag_put**](DnsProjectZoneApi.md#dns_project_zone_tag_put) | **PUT** /dns/{locationId}/project/{projectId}/zone/{zoneId}/tag | Replace dns/zone.tag
[**dns_project_zone_update**](DnsProjectZoneApi.md#dns_project_zone_update) | **PATCH** /dns/{locationId}/project/{projectId}/zone/{zoneId} | Update dns/zone


# **dns_project_zone_create**
> Zone dns_project_zone_create(project_id, location_id, dns_project_zone_create, x_idempotency_key=x_idempotency_key)

Create dns/zone

Create zone

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
dns_project_zone_create = h1-client-python.DnsProjectZoneCreate() # DnsProjectZoneCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create dns/zone
        api_response = api_instance.dns_project_zone_create(project_id, location_id, dns_project_zone_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **dns_project_zone_create** | [**DnsProjectZoneCreate**](DnsProjectZoneCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Zone**](Zone.md)

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

# **dns_project_zone_delete**
> dns_project_zone_delete(project_id, location_id, zone_id)

Delete dns/zone

Delete zone

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id

    try:
        # Delete dns/zone
        api_instance.dns_project_zone_delete(project_id, location_id, zone_id)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 

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

# **dns_project_zone_event_get**
> Event dns_project_zone_event_get(project_id, location_id, zone_id, event_id)

Get dns/zone.event

Get dns/zone.event

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get dns/zone.event
        api_response = api_instance.dns_project_zone_event_get(project_id, location_id, zone_id, event_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
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

# **dns_project_zone_event_list**
> list[Event] dns_project_zone_event_list(project_id, location_id, zone_id, limit=limit, skip=skip)

List dns/zone.event

List dns/zone.event

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List dns/zone.event
        api_response = api_instance.dns_project_zone_event_list(project_id, location_id, zone_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
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

# **dns_project_zone_get**
> Zone dns_project_zone_get(project_id, location_id, zone_id)

Get dns/zone

Returns a single zone

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id

    try:
        # Get dns/zone
        api_response = api_instance.dns_project_zone_get(project_id, location_id, zone_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 

### Return type

[**Zone**](Zone.md)

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

# **dns_project_zone_list**
> list[Zone] dns_project_zone_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)

List dns/zone

List zone

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
name = 'name_example' # str | Filter by name (optional)
tag_value = 'tag_value_example' # str | Filter by tag.value (optional)
tag_key = 'tag_key_example' # str | Filter by tag.key (optional)

    try:
        # List dns/zone
        api_response = api_instance.dns_project_zone_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_list: %s\n" % e)
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

[**list[Zone]**](Zone.md)

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

# **dns_project_zone_recordset_create**
> DnsRecordset dns_project_zone_recordset_create(project_id, location_id, zone_id, dns_recordset)

Create dns/zone.recordset

Create dns/zone.recordset

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
dns_recordset = h1-client-python.DnsRecordset() # DnsRecordset | 

    try:
        # Create dns/zone.recordset
        api_response = api_instance.dns_project_zone_recordset_create(project_id, location_id, zone_id, dns_recordset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_recordset_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
 **dns_recordset** | [**DnsRecordset**](DnsRecordset.md)|  | 

### Return type

[**DnsRecordset**](DnsRecordset.md)

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

# **dns_project_zone_recordset_delete**
> Zone dns_project_zone_recordset_delete(project_id, location_id, zone_id, recordset_id)

Delete dns/zone.recordset

Delete dns/zone.recordset

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
recordset_id = 'recordset_id_example' # str | recordsetId

    try:
        # Delete dns/zone.recordset
        api_response = api_instance.dns_project_zone_recordset_delete(project_id, location_id, zone_id, recordset_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_recordset_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
 **recordset_id** | **str**| recordsetId | 

### Return type

[**Zone**](Zone.md)

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

# **dns_project_zone_recordset_get**
> DnsRecordset dns_project_zone_recordset_get(project_id, location_id, zone_id, recordset_id)

Get dns/zone.recordset

Get dns/zone.recordset

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
recordset_id = 'recordset_id_example' # str | recordsetId

    try:
        # Get dns/zone.recordset
        api_response = api_instance.dns_project_zone_recordset_get(project_id, location_id, zone_id, recordset_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_recordset_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
 **recordset_id** | **str**| recordsetId | 

### Return type

[**DnsRecordset**](DnsRecordset.md)

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

# **dns_project_zone_recordset_list**
> list[DnsRecordset] dns_project_zone_recordset_list(project_id, location_id, zone_id)

List dns/zone.recordset

List dns/zone.recordset

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id

    try:
        # List dns/zone.recordset
        api_response = api_instance.dns_project_zone_recordset_list(project_id, location_id, zone_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_recordset_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 

### Return type

[**list[DnsRecordset]**](DnsRecordset.md)

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

# **dns_project_zone_recordset_patch**
> DnsRecordset dns_project_zone_recordset_patch(project_id, location_id, zone_id, recordset_id, dns_project_zone_recordset_patch)

Update dns/zone.recordset

Update dns/zone.recordset

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
recordset_id = 'recordset_id_example' # str | recordsetId
dns_project_zone_recordset_patch = h1-client-python.DnsProjectZoneRecordsetPatch() # DnsProjectZoneRecordsetPatch | 

    try:
        # Update dns/zone.recordset
        api_response = api_instance.dns_project_zone_recordset_patch(project_id, location_id, zone_id, recordset_id, dns_project_zone_recordset_patch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_recordset_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
 **recordset_id** | **str**| recordsetId | 
 **dns_project_zone_recordset_patch** | [**DnsProjectZoneRecordsetPatch**](DnsProjectZoneRecordsetPatch.md)|  | 

### Return type

[**DnsRecordset**](DnsRecordset.md)

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

# **dns_project_zone_recordset_record_create**
> DnsRecord dns_project_zone_recordset_record_create(project_id, location_id, zone_id, recordset_id, dns_record)

Create dns/zone.record

Create dns/zone.record

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
recordset_id = 'recordset_id_example' # str | recordsetId
dns_record = h1-client-python.DnsRecord() # DnsRecord | 

    try:
        # Create dns/zone.record
        api_response = api_instance.dns_project_zone_recordset_record_create(project_id, location_id, zone_id, recordset_id, dns_record)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_recordset_record_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
 **recordset_id** | **str**| recordsetId | 
 **dns_record** | [**DnsRecord**](DnsRecord.md)|  | 

### Return type

[**DnsRecord**](DnsRecord.md)

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

# **dns_project_zone_recordset_record_delete**
> dns_project_zone_recordset_record_delete(project_id, location_id, zone_id, recordset_id, record_id)

Delete dns/zone.record

Delete dns/zone.record

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
recordset_id = 'recordset_id_example' # str | recordsetId
record_id = 'record_id_example' # str | recordId

    try:
        # Delete dns/zone.record
        api_instance.dns_project_zone_recordset_record_delete(project_id, location_id, zone_id, recordset_id, record_id)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_recordset_record_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
 **recordset_id** | **str**| recordsetId | 
 **record_id** | **str**| recordId | 

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

# **dns_project_zone_recordset_record_get**
> DnsRecord dns_project_zone_recordset_record_get(project_id, location_id, zone_id, recordset_id, record_id)

Get dns/zone.record

Get dns/zone.record

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
recordset_id = 'recordset_id_example' # str | recordsetId
record_id = 'record_id_example' # str | recordId

    try:
        # Get dns/zone.record
        api_response = api_instance.dns_project_zone_recordset_record_get(project_id, location_id, zone_id, recordset_id, record_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_recordset_record_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
 **recordset_id** | **str**| recordsetId | 
 **record_id** | **str**| recordId | 

### Return type

[**DnsRecord**](DnsRecord.md)

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

# **dns_project_zone_recordset_record_list**
> list[DnsRecord] dns_project_zone_recordset_record_list(project_id, location_id, zone_id, recordset_id)

List dns/zone.record

List dns/zone.record

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
recordset_id = 'recordset_id_example' # str | recordsetId

    try:
        # List dns/zone.record
        api_response = api_instance.dns_project_zone_recordset_record_list(project_id, location_id, zone_id, recordset_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_recordset_record_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
 **recordset_id** | **str**| recordsetId | 

### Return type

[**list[DnsRecord]**](DnsRecord.md)

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

# **dns_project_zone_recordset_record_put**
> list[DnsRecord] dns_project_zone_recordset_record_put(project_id, location_id, zone_id, recordset_id, dns_record)

Replace dns/zone.record

Replace dns/zone.record

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
recordset_id = 'recordset_id_example' # str | recordsetId
dns_record = [h1-client-python.DnsRecord()] # list[DnsRecord] | 

    try:
        # Replace dns/zone.record
        api_response = api_instance.dns_project_zone_recordset_record_put(project_id, location_id, zone_id, recordset_id, dns_record)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_recordset_record_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
 **recordset_id** | **str**| recordsetId | 
 **dns_record** | [**list[DnsRecord]**](DnsRecord.md)|  | 

### Return type

[**list[DnsRecord]**](DnsRecord.md)

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

# **dns_project_zone_service_get**
> ResourceService dns_project_zone_service_get(project_id, location_id, zone_id, service_id)

Get dns/zone.service

Get dns/zone.service

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
service_id = 'service_id_example' # str | serviceId

    try:
        # Get dns/zone.service
        api_response = api_instance.dns_project_zone_service_get(project_id, location_id, zone_id, service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
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

# **dns_project_zone_service_list**
> list[ResourceService] dns_project_zone_service_list(project_id, location_id, zone_id)

List dns/zone.service

List dns/zone.service

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id

    try:
        # List dns/zone.service
        api_response = api_instance.dns_project_zone_service_list(project_id, location_id, zone_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 

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

# **dns_project_zone_tag_create**
> Tag dns_project_zone_tag_create(project_id, location_id, zone_id, tag)

Create dns/zone.tag

Create dns/zone.tag

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
tag = h1-client-python.Tag() # Tag | 

    try:
        # Create dns/zone.tag
        api_response = api_instance.dns_project_zone_tag_create(project_id, location_id, zone_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
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

# **dns_project_zone_tag_delete**
> dns_project_zone_tag_delete(project_id, location_id, zone_id, tag_id)

Delete dns/zone.tag

Delete dns/zone.tag

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Delete dns/zone.tag
        api_instance.dns_project_zone_tag_delete(project_id, location_id, zone_id, tag_id)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
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

# **dns_project_zone_tag_get**
> Tag dns_project_zone_tag_get(project_id, location_id, zone_id, tag_id)

Get dns/zone.tag

Get dns/zone.tag

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Get dns/zone.tag
        api_response = api_instance.dns_project_zone_tag_get(project_id, location_id, zone_id, tag_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
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

# **dns_project_zone_tag_list**
> list[Tag] dns_project_zone_tag_list(project_id, location_id, zone_id)

List dns/zone.tag

List dns/zone.tag

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id

    try:
        # List dns/zone.tag
        api_response = api_instance.dns_project_zone_tag_list(project_id, location_id, zone_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 

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

# **dns_project_zone_tag_put**
> list[Tag] dns_project_zone_tag_put(project_id, location_id, zone_id, tag)

Replace dns/zone.tag

Replace dns/zone.tag

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
tag = [h1-client-python.Tag()] # list[Tag] | 

    try:
        # Replace dns/zone.tag
        api_response = api_instance.dns_project_zone_tag_put(project_id, location_id, zone_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
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

# **dns_project_zone_update**
> Zone dns_project_zone_update(project_id, location_id, zone_id, dns_project_zone_update)

Update dns/zone

Returns modified zone

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
    api_instance = h1-client-python.DnsProjectZoneApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
zone_id = 'zone_id_example' # str | Zone Id
dns_project_zone_update = h1-client-python.DnsProjectZoneUpdate() # DnsProjectZoneUpdate | 

    try:
        # Update dns/zone
        api_response = api_instance.dns_project_zone_update(project_id, location_id, zone_id, dns_project_zone_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DnsProjectZoneApi->dns_project_zone_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **zone_id** | **str**| Zone Id | 
 **dns_project_zone_update** | [**DnsProjectZoneUpdate**](DnsProjectZoneUpdate.md)|  | 

### Return type

[**Zone**](Zone.md)

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

