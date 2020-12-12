# h1.WebsiteProjectInstanceApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**website_project_instance_connect_get**](WebsiteProjectInstanceApi.md#website_project_instance_connect_get) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/connect/{connectId} | Get website/instance.connect
[**website_project_instance_connect_list**](WebsiteProjectInstanceApi.md#website_project_instance_connect_list) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/connect | List website/instance.connect
[**website_project_instance_create**](WebsiteProjectInstanceApi.md#website_project_instance_create) | **POST** /website/{locationId}/project/{projectId}/instance | Create website/instance
[**website_project_instance_credential_create**](WebsiteProjectInstanceApi.md#website_project_instance_credential_create) | **POST** /website/{locationId}/project/{projectId}/instance/{instanceId}/credential | Create website/instance.credential
[**website_project_instance_credential_delete**](WebsiteProjectInstanceApi.md#website_project_instance_credential_delete) | **DELETE** /website/{locationId}/project/{projectId}/instance/{instanceId}/credential/{credentialId} | Delete website/instance.credential
[**website_project_instance_credential_get**](WebsiteProjectInstanceApi.md#website_project_instance_credential_get) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/credential/{credentialId} | Get website/instance.credential
[**website_project_instance_credential_list**](WebsiteProjectInstanceApi.md#website_project_instance_credential_list) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/credential | List website/instance.credential
[**website_project_instance_credential_patch**](WebsiteProjectInstanceApi.md#website_project_instance_credential_patch) | **PATCH** /website/{locationId}/project/{projectId}/instance/{instanceId}/credential/{credentialId} | Update website/instance.credential
[**website_project_instance_delete**](WebsiteProjectInstanceApi.md#website_project_instance_delete) | **DELETE** /website/{locationId}/project/{projectId}/instance/{instanceId} | Delete website/instance
[**website_project_instance_domain_create**](WebsiteProjectInstanceApi.md#website_project_instance_domain_create) | **POST** /website/{locationId}/project/{projectId}/instance/{instanceId}/domain | Create website/instance.domain
[**website_project_instance_domain_delete**](WebsiteProjectInstanceApi.md#website_project_instance_domain_delete) | **DELETE** /website/{locationId}/project/{projectId}/instance/{instanceId}/domain/{domainId} | Delete website/instance.domain
[**website_project_instance_domain_get**](WebsiteProjectInstanceApi.md#website_project_instance_domain_get) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/domain/{domainId} | Get website/instance.domain
[**website_project_instance_domain_list**](WebsiteProjectInstanceApi.md#website_project_instance_domain_list) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/domain | List website/instance.domain
[**website_project_instance_env_create**](WebsiteProjectInstanceApi.md#website_project_instance_env_create) | **POST** /website/{locationId}/project/{projectId}/instance/{instanceId}/env | Create website/instance.env
[**website_project_instance_env_delete**](WebsiteProjectInstanceApi.md#website_project_instance_env_delete) | **DELETE** /website/{locationId}/project/{projectId}/instance/{instanceId}/env/{envId} | Delete website/instance.env
[**website_project_instance_env_get**](WebsiteProjectInstanceApi.md#website_project_instance_env_get) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/env/{envId} | Get website/instance.env
[**website_project_instance_env_list**](WebsiteProjectInstanceApi.md#website_project_instance_env_list) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/env | List website/instance.env
[**website_project_instance_event_get**](WebsiteProjectInstanceApi.md#website_project_instance_event_get) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/event/{eventId} | Get website/instance.event
[**website_project_instance_event_list**](WebsiteProjectInstanceApi.md#website_project_instance_event_list) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/event | List website/instance.event
[**website_project_instance_get**](WebsiteProjectInstanceApi.md#website_project_instance_get) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId} | Get website/instance
[**website_project_instance_link_create**](WebsiteProjectInstanceApi.md#website_project_instance_link_create) | **POST** /website/{locationId}/project/{projectId}/instance/{instanceId}/link | Create website/instance.link
[**website_project_instance_link_delete**](WebsiteProjectInstanceApi.md#website_project_instance_link_delete) | **DELETE** /website/{locationId}/project/{projectId}/instance/{instanceId}/link/{linkId} | Delete website/instance.link
[**website_project_instance_link_get**](WebsiteProjectInstanceApi.md#website_project_instance_link_get) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/link/{linkId} | Get website/instance.link
[**website_project_instance_link_list**](WebsiteProjectInstanceApi.md#website_project_instance_link_list) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/link | List website/instance.link
[**website_project_instance_list**](WebsiteProjectInstanceApi.md#website_project_instance_list) | **GET** /website/{locationId}/project/{projectId}/instance | List website/instance
[**website_project_instance_log_get**](WebsiteProjectInstanceApi.md#website_project_instance_log_get) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/log/{logId} | Get website/instance.log
[**website_project_instance_log_list**](WebsiteProjectInstanceApi.md#website_project_instance_log_list) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/log | List website/instance.log
[**website_project_instance_log_read**](WebsiteProjectInstanceApi.md#website_project_instance_log_read) | **POST** /website/{locationId}/project/{projectId}/instance/{instanceId}/log/{logId}/actions/read | Read website/instance.log
[**website_project_instance_metric_get**](WebsiteProjectInstanceApi.md#website_project_instance_metric_get) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/metric/{metricId} | Get website/instance.metric
[**website_project_instance_metric_list**](WebsiteProjectInstanceApi.md#website_project_instance_metric_list) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/metric | List website/instance.metric
[**website_project_instance_metric_point_list**](WebsiteProjectInstanceApi.md#website_project_instance_metric_point_list) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/metric/{metricId}/point | List website/instance.point
[**website_project_instance_restart**](WebsiteProjectInstanceApi.md#website_project_instance_restart) | **POST** /website/{locationId}/project/{projectId}/instance/{instanceId}/actions/restart | Restart website/instance
[**website_project_instance_service_get**](WebsiteProjectInstanceApi.md#website_project_instance_service_get) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/service/{serviceId} | Get website/instance.service
[**website_project_instance_service_list**](WebsiteProjectInstanceApi.md#website_project_instance_service_list) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/service | List website/instance.service
[**website_project_instance_sideapp_create**](WebsiteProjectInstanceApi.md#website_project_instance_sideapp_create) | **POST** /website/{locationId}/project/{projectId}/instance/{instanceId}/sideapp | Create website/instance.sideapp
[**website_project_instance_sideapp_delete**](WebsiteProjectInstanceApi.md#website_project_instance_sideapp_delete) | **DELETE** /website/{locationId}/project/{projectId}/instance/{instanceId}/sideapp/{sideappId} | Delete website/instance.sideapp
[**website_project_instance_sideapp_get**](WebsiteProjectInstanceApi.md#website_project_instance_sideapp_get) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/sideapp/{sideappId} | Get website/instance.sideapp
[**website_project_instance_sideapp_list**](WebsiteProjectInstanceApi.md#website_project_instance_sideapp_list) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/sideapp | List website/instance.sideapp
[**website_project_instance_snapshot_create**](WebsiteProjectInstanceApi.md#website_project_instance_snapshot_create) | **POST** /website/{locationId}/project/{projectId}/instance/{instanceId}/snapshot | Create website/instance.snapshot
[**website_project_instance_snapshot_delete**](WebsiteProjectInstanceApi.md#website_project_instance_snapshot_delete) | **DELETE** /website/{locationId}/project/{projectId}/instance/{instanceId}/snapshot/{snapshotId} | Delete website/instance.snapshot
[**website_project_instance_snapshot_download**](WebsiteProjectInstanceApi.md#website_project_instance_snapshot_download) | **POST** /website/{locationId}/project/{projectId}/instance/{instanceId}/snapshot/{snapshotId}/actions/download | Download website/instance.snapshot
[**website_project_instance_snapshot_get**](WebsiteProjectInstanceApi.md#website_project_instance_snapshot_get) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/snapshot/{snapshotId} | Get website/instance.snapshot
[**website_project_instance_snapshot_list**](WebsiteProjectInstanceApi.md#website_project_instance_snapshot_list) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/snapshot | List website/instance.snapshot
[**website_project_instance_start**](WebsiteProjectInstanceApi.md#website_project_instance_start) | **POST** /website/{locationId}/project/{projectId}/instance/{instanceId}/actions/start | Start website/instance
[**website_project_instance_stop**](WebsiteProjectInstanceApi.md#website_project_instance_stop) | **POST** /website/{locationId}/project/{projectId}/instance/{instanceId}/actions/stop | Stop website/instance
[**website_project_instance_tag_create**](WebsiteProjectInstanceApi.md#website_project_instance_tag_create) | **POST** /website/{locationId}/project/{projectId}/instance/{instanceId}/tag | Create website/instance.tag
[**website_project_instance_tag_delete**](WebsiteProjectInstanceApi.md#website_project_instance_tag_delete) | **DELETE** /website/{locationId}/project/{projectId}/instance/{instanceId}/tag/{tagId} | Delete website/instance.tag
[**website_project_instance_tag_get**](WebsiteProjectInstanceApi.md#website_project_instance_tag_get) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/tag/{tagId} | Get website/instance.tag
[**website_project_instance_tag_list**](WebsiteProjectInstanceApi.md#website_project_instance_tag_list) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/tag | List website/instance.tag
[**website_project_instance_tag_put**](WebsiteProjectInstanceApi.md#website_project_instance_tag_put) | **PUT** /website/{locationId}/project/{projectId}/instance/{instanceId}/tag | Replace website/instance.tag
[**website_project_instance_transfer**](WebsiteProjectInstanceApi.md#website_project_instance_transfer) | **POST** /website/{locationId}/project/{projectId}/instance/{instanceId}/actions/transfer | Transfer website/instance
[**website_project_instance_update**](WebsiteProjectInstanceApi.md#website_project_instance_update) | **PATCH** /website/{locationId}/project/{projectId}/instance/{instanceId} | Update website/instance


# **website_project_instance_connect_get**
> ResourceConnect website_project_instance_connect_get(project_id, location_id, instance_id, connect_id)

Get website/instance.connect

Get website/instance.connect

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
connect_id = 'connect_id_example' # str | connectId

    try:
        # Get website/instance.connect
        api_response = api_instance.website_project_instance_connect_get(project_id, location_id, instance_id, connect_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_connect_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **connect_id** | **str**| connectId | 

### Return type

[**ResourceConnect**](ResourceConnect.md)

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

# **website_project_instance_connect_list**
> list[ResourceConnect] website_project_instance_connect_list(project_id, location_id, instance_id)

List website/instance.connect

List website/instance.connect

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List website/instance.connect
        api_response = api_instance.website_project_instance_connect_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_connect_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 

### Return type

[**list[ResourceConnect]**](ResourceConnect.md)

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

# **website_project_instance_create**
> Website website_project_instance_create(project_id, location_id, website_project_instance_create, x_idempotency_key=x_idempotency_key)

Create website/instance

Create instance

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
website_project_instance_create = h1.WebsiteProjectInstanceCreate() # WebsiteProjectInstanceCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create website/instance
        api_response = api_instance.website_project_instance_create(project_id, location_id, website_project_instance_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **website_project_instance_create** | [**WebsiteProjectInstanceCreate**](WebsiteProjectInstanceCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Website**](Website.md)

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

# **website_project_instance_credential_create**
> WebsiteCredential website_project_instance_credential_create(project_id, location_id, instance_id, website_credential)

Create website/instance.credential

Create website/instance.credential

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
website_credential = h1.WebsiteCredential() # WebsiteCredential | 

    try:
        # Create website/instance.credential
        api_response = api_instance.website_project_instance_credential_create(project_id, location_id, instance_id, website_credential)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_credential_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **website_credential** | [**WebsiteCredential**](WebsiteCredential.md)|  | 

### Return type

[**WebsiteCredential**](WebsiteCredential.md)

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

# **website_project_instance_credential_delete**
> Website website_project_instance_credential_delete(project_id, location_id, instance_id, credential_id)

Delete website/instance.credential

Delete website/instance.credential

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
credential_id = 'credential_id_example' # str | credentialId

    try:
        # Delete website/instance.credential
        api_response = api_instance.website_project_instance_credential_delete(project_id, location_id, instance_id, credential_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_credential_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **credential_id** | **str**| credentialId | 

### Return type

[**Website**](Website.md)

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

# **website_project_instance_credential_get**
> WebsiteCredential website_project_instance_credential_get(project_id, location_id, instance_id, credential_id)

Get website/instance.credential

Get website/instance.credential

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
credential_id = 'credential_id_example' # str | credentialId

    try:
        # Get website/instance.credential
        api_response = api_instance.website_project_instance_credential_get(project_id, location_id, instance_id, credential_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_credential_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **credential_id** | **str**| credentialId | 

### Return type

[**WebsiteCredential**](WebsiteCredential.md)

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

# **website_project_instance_credential_list**
> list[WebsiteCredential] website_project_instance_credential_list(project_id, location_id, instance_id)

List website/instance.credential

List website/instance.credential

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List website/instance.credential
        api_response = api_instance.website_project_instance_credential_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_credential_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 

### Return type

[**list[WebsiteCredential]**](WebsiteCredential.md)

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

# **website_project_instance_credential_patch**
> WebsiteCredential website_project_instance_credential_patch(project_id, location_id, instance_id, credential_id, website_project_instance_credential_patch)

Update website/instance.credential

Update website/instance.credential

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
credential_id = 'credential_id_example' # str | credentialId
website_project_instance_credential_patch = h1.WebsiteProjectInstanceCredentialPatch() # WebsiteProjectInstanceCredentialPatch | 

    try:
        # Update website/instance.credential
        api_response = api_instance.website_project_instance_credential_patch(project_id, location_id, instance_id, credential_id, website_project_instance_credential_patch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_credential_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **credential_id** | **str**| credentialId | 
 **website_project_instance_credential_patch** | [**WebsiteProjectInstanceCredentialPatch**](WebsiteProjectInstanceCredentialPatch.md)|  | 

### Return type

[**WebsiteCredential**](WebsiteCredential.md)

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

# **website_project_instance_delete**
> website_project_instance_delete(project_id, location_id, instance_id)

Delete website/instance

Delete instance

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # Delete website/instance
        api_instance.website_project_instance_delete(project_id, location_id, instance_id)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 

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

# **website_project_instance_domain_create**
> Domain website_project_instance_domain_create(project_id, location_id, instance_id, domain)

Create website/instance.domain

Create website/instance.domain

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
domain = h1.Domain() # Domain | 

    try:
        # Create website/instance.domain
        api_response = api_instance.website_project_instance_domain_create(project_id, location_id, instance_id, domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_domain_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **domain** | [**Domain**](Domain.md)|  | 

### Return type

[**Domain**](Domain.md)

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

# **website_project_instance_domain_delete**
> website_project_instance_domain_delete(project_id, location_id, instance_id, domain_id)

Delete website/instance.domain

Delete website/instance.domain

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
domain_id = 'domain_id_example' # str | domainId

    try:
        # Delete website/instance.domain
        api_instance.website_project_instance_domain_delete(project_id, location_id, instance_id, domain_id)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_domain_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **domain_id** | **str**| domainId | 

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

# **website_project_instance_domain_get**
> Domain website_project_instance_domain_get(project_id, location_id, instance_id, domain_id)

Get website/instance.domain

Get website/instance.domain

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
domain_id = 'domain_id_example' # str | domainId

    try:
        # Get website/instance.domain
        api_response = api_instance.website_project_instance_domain_get(project_id, location_id, instance_id, domain_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_domain_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **domain_id** | **str**| domainId | 

### Return type

[**Domain**](Domain.md)

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

# **website_project_instance_domain_list**
> list[Domain] website_project_instance_domain_list(project_id, location_id, instance_id)

List website/instance.domain

List website/instance.domain

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List website/instance.domain
        api_response = api_instance.website_project_instance_domain_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_domain_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 

### Return type

[**list[Domain]**](Domain.md)

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

# **website_project_instance_env_create**
> WebsiteEnv website_project_instance_env_create(project_id, location_id, instance_id, website_env)

Create website/instance.env

Create website/instance.env

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
website_env = h1.WebsiteEnv() # WebsiteEnv | 

    try:
        # Create website/instance.env
        api_response = api_instance.website_project_instance_env_create(project_id, location_id, instance_id, website_env)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_env_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **website_env** | [**WebsiteEnv**](WebsiteEnv.md)|  | 

### Return type

[**WebsiteEnv**](WebsiteEnv.md)

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

# **website_project_instance_env_delete**
> website_project_instance_env_delete(project_id, location_id, instance_id, env_id)

Delete website/instance.env

Delete website/instance.env

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
env_id = 'env_id_example' # str | envId

    try:
        # Delete website/instance.env
        api_instance.website_project_instance_env_delete(project_id, location_id, instance_id, env_id)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_env_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **env_id** | **str**| envId | 

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

# **website_project_instance_env_get**
> WebsiteEnv website_project_instance_env_get(project_id, location_id, instance_id, env_id)

Get website/instance.env

Get website/instance.env

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
env_id = 'env_id_example' # str | envId

    try:
        # Get website/instance.env
        api_response = api_instance.website_project_instance_env_get(project_id, location_id, instance_id, env_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_env_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **env_id** | **str**| envId | 

### Return type

[**WebsiteEnv**](WebsiteEnv.md)

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

# **website_project_instance_env_list**
> list[WebsiteEnv] website_project_instance_env_list(project_id, location_id, instance_id)

List website/instance.env

List website/instance.env

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List website/instance.env
        api_response = api_instance.website_project_instance_env_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_env_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 

### Return type

[**list[WebsiteEnv]**](WebsiteEnv.md)

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

# **website_project_instance_event_get**
> Event website_project_instance_event_get(project_id, location_id, instance_id, event_id)

Get website/instance.event

Get website/instance.event

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get website/instance.event
        api_response = api_instance.website_project_instance_event_get(project_id, location_id, instance_id, event_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_event_get: %s\n" % e)
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

# **website_project_instance_event_list**
> list[Event] website_project_instance_event_list(project_id, location_id, instance_id, limit=limit, skip=skip)

List website/instance.event

List website/instance.event

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List website/instance.event
        api_response = api_instance.website_project_instance_event_list(project_id, location_id, instance_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_event_list: %s\n" % e)
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

# **website_project_instance_get**
> Website website_project_instance_get(project_id, location_id, instance_id)

Get website/instance

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # Get website/instance
        api_response = api_instance.website_project_instance_get(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 

### Return type

[**Website**](Website.md)

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

# **website_project_instance_link_create**
> WebsiteLink website_project_instance_link_create(project_id, location_id, instance_id, website_link)

Create website/instance.link

Create website/instance.link

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
website_link = h1.WebsiteLink() # WebsiteLink | 

    try:
        # Create website/instance.link
        api_response = api_instance.website_project_instance_link_create(project_id, location_id, instance_id, website_link)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_link_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **website_link** | [**WebsiteLink**](WebsiteLink.md)|  | 

### Return type

[**WebsiteLink**](WebsiteLink.md)

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

# **website_project_instance_link_delete**
> website_project_instance_link_delete(project_id, location_id, instance_id, link_id)

Delete website/instance.link

Delete website/instance.link

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
link_id = 'link_id_example' # str | linkId

    try:
        # Delete website/instance.link
        api_instance.website_project_instance_link_delete(project_id, location_id, instance_id, link_id)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_link_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **link_id** | **str**| linkId | 

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

# **website_project_instance_link_get**
> WebsiteLink website_project_instance_link_get(project_id, location_id, instance_id, link_id)

Get website/instance.link

Get website/instance.link

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
link_id = 'link_id_example' # str | linkId

    try:
        # Get website/instance.link
        api_response = api_instance.website_project_instance_link_get(project_id, location_id, instance_id, link_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_link_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **link_id** | **str**| linkId | 

### Return type

[**WebsiteLink**](WebsiteLink.md)

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

# **website_project_instance_link_list**
> list[WebsiteLink] website_project_instance_link_list(project_id, location_id, instance_id)

List website/instance.link

List website/instance.link

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List website/instance.link
        api_response = api_instance.website_project_instance_link_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_link_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 

### Return type

[**list[WebsiteLink]**](WebsiteLink.md)

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

# **website_project_instance_list**
> list[Website] website_project_instance_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)

List website/instance

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
name = 'name_example' # str | Filter by name (optional)
tag_value = 'tag_value_example' # str | Filter by tag.value (optional)
tag_key = 'tag_key_example' # str | Filter by tag.key (optional)

    try:
        # List website/instance
        api_response = api_instance.website_project_instance_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_list: %s\n" % e)
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

[**list[Website]**](Website.md)

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

# **website_project_instance_log_get**
> Log website_project_instance_log_get(project_id, location_id, instance_id, log_id)

Get website/instance.log

Get website/instance.log

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
log_id = 'log_id_example' # str | logId

    try:
        # Get website/instance.log
        api_response = api_instance.website_project_instance_log_get(project_id, location_id, instance_id, log_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **log_id** | **str**| logId | 

### Return type

[**Log**](Log.md)

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

# **website_project_instance_log_list**
> list[Log] website_project_instance_log_list(project_id, location_id, instance_id)

List website/instance.log

List website/instance.log

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List website/instance.log
        api_response = api_instance.website_project_instance_log_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_log_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 

### Return type

[**list[Log]**](Log.md)

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

# **website_project_instance_log_read**
> website_project_instance_log_read(project_id, location_id, instance_id, log_id)

Read website/instance.log

action read

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
log_id = 'log_id_example' # str | logId

    try:
        # Read website/instance.log
        api_instance.website_project_instance_log_read(project_id, location_id, instance_id, log_id)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_log_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **log_id** | **str**| logId | 

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
**201** | Log request accepted |  * location - Absolute URL <br>  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_project_instance_metric_get**
> Metric website_project_instance_metric_get(project_id, location_id, instance_id, metric_id)

Get website/instance.metric

Get website/instance.metric

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
metric_id = 'metric_id_example' # str | metricId

    try:
        # Get website/instance.metric
        api_response = api_instance.website_project_instance_metric_get(project_id, location_id, instance_id, metric_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_metric_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
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

# **website_project_instance_metric_list**
> list[Metric] website_project_instance_metric_list(project_id, location_id, instance_id)

List website/instance.metric

List website/instance.metric

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List website/instance.metric
        api_response = api_instance.website_project_instance_metric_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_metric_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 

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

# **website_project_instance_metric_point_list**
> list[Point] website_project_instance_metric_point_list(project_id, location_id, instance_id, metric_id, interval=interval, timespan=timespan)

List website/instance.point

List website/instance.point

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
metric_id = 'metric_id_example' # str | metricId
interval = 'interval_example' # str | interval (optional)
timespan = 'timespan_example' # str | timespan (optional)

    try:
        # List website/instance.point
        api_response = api_instance.website_project_instance_metric_point_list(project_id, location_id, instance_id, metric_id, interval=interval, timespan=timespan)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_metric_point_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **metric_id** | **str**| metricId | 
 **interval** | **str**| interval | [optional] 
 **timespan** | **str**| timespan | [optional] 

### Return type

[**list[Point]**](Point.md)

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

# **website_project_instance_restart**
> Website website_project_instance_restart(project_id, location_id, instance_id, x_idempotency_key=x_idempotency_key)

Restart website/instance

action restart

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Restart website/instance
        api_response = api_instance.website_project_instance_restart(project_id, location_id, instance_id, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_restart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Website**](Website.md)

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

# **website_project_instance_service_get**
> ResourceService website_project_instance_service_get(project_id, location_id, instance_id, service_id)

Get website/instance.service

Get website/instance.service

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
service_id = 'service_id_example' # str | serviceId

    try:
        # Get website/instance.service
        api_response = api_instance.website_project_instance_service_get(project_id, location_id, instance_id, service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_service_get: %s\n" % e)
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

# **website_project_instance_service_list**
> list[ResourceService] website_project_instance_service_list(project_id, location_id, instance_id)

List website/instance.service

List website/instance.service

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List website/instance.service
        api_response = api_instance.website_project_instance_service_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_service_list: %s\n" % e)
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

# **website_project_instance_sideapp_create**
> WebsiteSideapp website_project_instance_sideapp_create(project_id, location_id, instance_id, website_sideapp)

Create website/instance.sideapp

Create website/instance.sideapp

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
website_sideapp = h1.WebsiteSideapp() # WebsiteSideapp | 

    try:
        # Create website/instance.sideapp
        api_response = api_instance.website_project_instance_sideapp_create(project_id, location_id, instance_id, website_sideapp)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_sideapp_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **website_sideapp** | [**WebsiteSideapp**](WebsiteSideapp.md)|  | 

### Return type

[**WebsiteSideapp**](WebsiteSideapp.md)

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

# **website_project_instance_sideapp_delete**
> website_project_instance_sideapp_delete(project_id, location_id, instance_id, sideapp_id)

Delete website/instance.sideapp

Delete website/instance.sideapp

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
sideapp_id = 'sideapp_id_example' # str | sideappId

    try:
        # Delete website/instance.sideapp
        api_instance.website_project_instance_sideapp_delete(project_id, location_id, instance_id, sideapp_id)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_sideapp_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **sideapp_id** | **str**| sideappId | 

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

# **website_project_instance_sideapp_get**
> WebsiteSideapp website_project_instance_sideapp_get(project_id, location_id, instance_id, sideapp_id)

Get website/instance.sideapp

Get website/instance.sideapp

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
sideapp_id = 'sideapp_id_example' # str | sideappId

    try:
        # Get website/instance.sideapp
        api_response = api_instance.website_project_instance_sideapp_get(project_id, location_id, instance_id, sideapp_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_sideapp_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **sideapp_id** | **str**| sideappId | 

### Return type

[**WebsiteSideapp**](WebsiteSideapp.md)

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

# **website_project_instance_sideapp_list**
> list[WebsiteSideapp] website_project_instance_sideapp_list(project_id, location_id, instance_id)

List website/instance.sideapp

List website/instance.sideapp

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List website/instance.sideapp
        api_response = api_instance.website_project_instance_sideapp_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_sideapp_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 

### Return type

[**list[WebsiteSideapp]**](WebsiteSideapp.md)

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

# **website_project_instance_snapshot_create**
> WebsiteSnapshot website_project_instance_snapshot_create(project_id, location_id, instance_id, website_snapshot)

Create website/instance.snapshot

Create website/instance.snapshot

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
website_snapshot = h1.WebsiteSnapshot() # WebsiteSnapshot | 

    try:
        # Create website/instance.snapshot
        api_response = api_instance.website_project_instance_snapshot_create(project_id, location_id, instance_id, website_snapshot)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_snapshot_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **website_snapshot** | [**WebsiteSnapshot**](WebsiteSnapshot.md)|  | 

### Return type

[**WebsiteSnapshot**](WebsiteSnapshot.md)

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

# **website_project_instance_snapshot_delete**
> Website website_project_instance_snapshot_delete(project_id, location_id, instance_id, snapshot_id)

Delete website/instance.snapshot

Delete website/instance.snapshot

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
snapshot_id = 'snapshot_id_example' # str | snapshotId

    try:
        # Delete website/instance.snapshot
        api_response = api_instance.website_project_instance_snapshot_delete(project_id, location_id, instance_id, snapshot_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_snapshot_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **snapshot_id** | **str**| snapshotId | 

### Return type

[**Website**](Website.md)

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

# **website_project_instance_snapshot_download**
> website_project_instance_snapshot_download(project_id, location_id, instance_id, snapshot_id, website_project_instance_snapshot_download)

Download website/instance.snapshot

action download

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
snapshot_id = 'snapshot_id_example' # str | snapshotId
website_project_instance_snapshot_download = h1.WebsiteProjectInstanceSnapshotDownload() # WebsiteProjectInstanceSnapshotDownload | 

    try:
        # Download website/instance.snapshot
        api_instance.website_project_instance_snapshot_download(project_id, location_id, instance_id, snapshot_id, website_project_instance_snapshot_download)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_snapshot_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **snapshot_id** | **str**| snapshotId | 
 **website_project_instance_snapshot_download** | [**WebsiteProjectInstanceSnapshotDownload**](WebsiteProjectInstanceSnapshotDownload.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Download request accepted |  * location - Absolute URL <br>  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **website_project_instance_snapshot_get**
> WebsiteSnapshot website_project_instance_snapshot_get(project_id, location_id, instance_id, snapshot_id)

Get website/instance.snapshot

Get website/instance.snapshot

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
snapshot_id = 'snapshot_id_example' # str | snapshotId

    try:
        # Get website/instance.snapshot
        api_response = api_instance.website_project_instance_snapshot_get(project_id, location_id, instance_id, snapshot_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_snapshot_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **snapshot_id** | **str**| snapshotId | 

### Return type

[**WebsiteSnapshot**](WebsiteSnapshot.md)

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

# **website_project_instance_snapshot_list**
> list[WebsiteSnapshot] website_project_instance_snapshot_list(project_id, location_id, instance_id)

List website/instance.snapshot

List website/instance.snapshot

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List website/instance.snapshot
        api_response = api_instance.website_project_instance_snapshot_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_snapshot_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 

### Return type

[**list[WebsiteSnapshot]**](WebsiteSnapshot.md)

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

# **website_project_instance_start**
> Website website_project_instance_start(project_id, location_id, instance_id, x_idempotency_key=x_idempotency_key)

Start website/instance

action start

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Start website/instance
        api_response = api_instance.website_project_instance_start(project_id, location_id, instance_id, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Website**](Website.md)

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

# **website_project_instance_stop**
> Website website_project_instance_stop(project_id, location_id, instance_id, x_idempotency_key=x_idempotency_key)

Stop website/instance

action stop

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Stop website/instance
        api_response = api_instance.website_project_instance_stop(project_id, location_id, instance_id, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Website**](Website.md)

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

# **website_project_instance_tag_create**
> Tag website_project_instance_tag_create(project_id, location_id, instance_id, tag)

Create website/instance.tag

Create website/instance.tag

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
tag = h1.Tag() # Tag | 

    try:
        # Create website/instance.tag
        api_response = api_instance.website_project_instance_tag_create(project_id, location_id, instance_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_tag_create: %s\n" % e)
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

# **website_project_instance_tag_delete**
> website_project_instance_tag_delete(project_id, location_id, instance_id, tag_id)

Delete website/instance.tag

Delete website/instance.tag

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Delete website/instance.tag
        api_instance.website_project_instance_tag_delete(project_id, location_id, instance_id, tag_id)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_tag_delete: %s\n" % e)
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

# **website_project_instance_tag_get**
> Tag website_project_instance_tag_get(project_id, location_id, instance_id, tag_id)

Get website/instance.tag

Get website/instance.tag

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Get website/instance.tag
        api_response = api_instance.website_project_instance_tag_get(project_id, location_id, instance_id, tag_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_tag_get: %s\n" % e)
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

# **website_project_instance_tag_list**
> list[Tag] website_project_instance_tag_list(project_id, location_id, instance_id)

List website/instance.tag

List website/instance.tag

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List website/instance.tag
        api_response = api_instance.website_project_instance_tag_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_tag_list: %s\n" % e)
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

# **website_project_instance_tag_put**
> list[Tag] website_project_instance_tag_put(project_id, location_id, instance_id, tag)

Replace website/instance.tag

Replace website/instance.tag

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
tag = [h1.Tag()] # list[Tag] | 

    try:
        # Replace website/instance.tag
        api_response = api_instance.website_project_instance_tag_put(project_id, location_id, instance_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_tag_put: %s\n" % e)
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

# **website_project_instance_transfer**
> Website website_project_instance_transfer(project_id, location_id, instance_id, website_project_instance_transfer, x_idempotency_key=x_idempotency_key)

Transfer website/instance

action transfer

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
website_project_instance_transfer = h1.WebsiteProjectInstanceTransfer() # WebsiteProjectInstanceTransfer | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Transfer website/instance
        api_response = api_instance.website_project_instance_transfer(project_id, location_id, instance_id, website_project_instance_transfer, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **website_project_instance_transfer** | [**WebsiteProjectInstanceTransfer**](WebsiteProjectInstanceTransfer.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Website**](Website.md)

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

# **website_project_instance_update**
> Website website_project_instance_update(project_id, location_id, instance_id, website_project_instance_update)

Update website/instance

Returns modified instance

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
    api_instance = h1.WebsiteProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
website_project_instance_update = h1.WebsiteProjectInstanceUpdate() # WebsiteProjectInstanceUpdate | 

    try:
        # Update website/instance
        api_response = api_instance.website_project_instance_update(project_id, location_id, instance_id, website_project_instance_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **website_project_instance_update** | [**WebsiteProjectInstanceUpdate**](WebsiteProjectInstanceUpdate.md)|  | 

### Return type

[**Website**](Website.md)

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

