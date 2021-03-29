# h1.ProviderProjectDevelopmentApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**provider_project_development_connect_get**](ProviderProjectDevelopmentApi.md#provider_project_development_connect_get) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/connect/{connectId} | Get provider/development.connect
[**provider_project_development_connect_list**](ProviderProjectDevelopmentApi.md#provider_project_development_connect_list) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/connect | List provider/development.connect
[**provider_project_development_create**](ProviderProjectDevelopmentApi.md#provider_project_development_create) | **POST** /provider/{locationId}/project/{projectId}/development | Create provider/development
[**provider_project_development_credential_create**](ProviderProjectDevelopmentApi.md#provider_project_development_credential_create) | **POST** /provider/{locationId}/project/{projectId}/development/{developmentId}/credential | Create provider/development.credential
[**provider_project_development_credential_delete**](ProviderProjectDevelopmentApi.md#provider_project_development_credential_delete) | **DELETE** /provider/{locationId}/project/{projectId}/development/{developmentId}/credential/{credentialId} | Delete provider/development.credential
[**provider_project_development_credential_get**](ProviderProjectDevelopmentApi.md#provider_project_development_credential_get) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/credential/{credentialId} | Get provider/development.credential
[**provider_project_development_credential_list**](ProviderProjectDevelopmentApi.md#provider_project_development_credential_list) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/credential | List provider/development.credential
[**provider_project_development_credential_patch**](ProviderProjectDevelopmentApi.md#provider_project_development_credential_patch) | **PATCH** /provider/{locationId}/project/{projectId}/development/{developmentId}/credential/{credentialId} | Update provider/development.credential
[**provider_project_development_delete**](ProviderProjectDevelopmentApi.md#provider_project_development_delete) | **DELETE** /provider/{locationId}/project/{projectId}/development/{developmentId} | Delete provider/development
[**provider_project_development_domain_create**](ProviderProjectDevelopmentApi.md#provider_project_development_domain_create) | **POST** /provider/{locationId}/project/{projectId}/development/{developmentId}/domain | Create provider/development.domain
[**provider_project_development_domain_delete**](ProviderProjectDevelopmentApi.md#provider_project_development_domain_delete) | **DELETE** /provider/{locationId}/project/{projectId}/development/{developmentId}/domain/{domainId} | Delete provider/development.domain
[**provider_project_development_domain_get**](ProviderProjectDevelopmentApi.md#provider_project_development_domain_get) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/domain/{domainId} | Get provider/development.domain
[**provider_project_development_domain_list**](ProviderProjectDevelopmentApi.md#provider_project_development_domain_list) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/domain | List provider/development.domain
[**provider_project_development_env_create**](ProviderProjectDevelopmentApi.md#provider_project_development_env_create) | **POST** /provider/{locationId}/project/{projectId}/development/{developmentId}/env | Create provider/development.env
[**provider_project_development_env_delete**](ProviderProjectDevelopmentApi.md#provider_project_development_env_delete) | **DELETE** /provider/{locationId}/project/{projectId}/development/{developmentId}/env/{envId} | Delete provider/development.env
[**provider_project_development_env_get**](ProviderProjectDevelopmentApi.md#provider_project_development_env_get) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/env/{envId} | Get provider/development.env
[**provider_project_development_env_list**](ProviderProjectDevelopmentApi.md#provider_project_development_env_list) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/env | List provider/development.env
[**provider_project_development_event_get**](ProviderProjectDevelopmentApi.md#provider_project_development_event_get) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/event/{eventId} | Get provider/development.event
[**provider_project_development_event_list**](ProviderProjectDevelopmentApi.md#provider_project_development_event_list) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/event | List provider/development.event
[**provider_project_development_get**](ProviderProjectDevelopmentApi.md#provider_project_development_get) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId} | Get provider/development
[**provider_project_development_link_create**](ProviderProjectDevelopmentApi.md#provider_project_development_link_create) | **POST** /provider/{locationId}/project/{projectId}/development/{developmentId}/link | Create provider/development.link
[**provider_project_development_link_delete**](ProviderProjectDevelopmentApi.md#provider_project_development_link_delete) | **DELETE** /provider/{locationId}/project/{projectId}/development/{developmentId}/link/{linkId} | Delete provider/development.link
[**provider_project_development_link_get**](ProviderProjectDevelopmentApi.md#provider_project_development_link_get) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/link/{linkId} | Get provider/development.link
[**provider_project_development_link_list**](ProviderProjectDevelopmentApi.md#provider_project_development_link_list) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/link | List provider/development.link
[**provider_project_development_list**](ProviderProjectDevelopmentApi.md#provider_project_development_list) | **GET** /provider/{locationId}/project/{projectId}/development | List provider/development
[**provider_project_development_log_get**](ProviderProjectDevelopmentApi.md#provider_project_development_log_get) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/log/{logId} | Get provider/development.log
[**provider_project_development_log_list**](ProviderProjectDevelopmentApi.md#provider_project_development_log_list) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/log | List provider/development.log
[**provider_project_development_log_read**](ProviderProjectDevelopmentApi.md#provider_project_development_log_read) | **POST** /provider/{locationId}/project/{projectId}/development/{developmentId}/log/{logId}/actions/read | Read provider/development.log
[**provider_project_development_metric_get**](ProviderProjectDevelopmentApi.md#provider_project_development_metric_get) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/metric/{metricId} | Get provider/development.metric
[**provider_project_development_metric_list**](ProviderProjectDevelopmentApi.md#provider_project_development_metric_list) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/metric | List provider/development.metric
[**provider_project_development_metric_point_list**](ProviderProjectDevelopmentApi.md#provider_project_development_metric_point_list) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/metric/{metricId}/point | List provider/development.point
[**provider_project_development_restart**](ProviderProjectDevelopmentApi.md#provider_project_development_restart) | **POST** /provider/{locationId}/project/{projectId}/development/{developmentId}/actions/restart | Restart provider/development
[**provider_project_development_service_get**](ProviderProjectDevelopmentApi.md#provider_project_development_service_get) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/service/{serviceId} | Get provider/development.service
[**provider_project_development_service_list**](ProviderProjectDevelopmentApi.md#provider_project_development_service_list) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/service | List provider/development.service
[**provider_project_development_sideapp_get**](ProviderProjectDevelopmentApi.md#provider_project_development_sideapp_get) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/sideapp/{sideappId} | Get provider/development.sideapp
[**provider_project_development_sideapp_list**](ProviderProjectDevelopmentApi.md#provider_project_development_sideapp_list) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/sideapp | List provider/development.sideapp
[**provider_project_development_sideapp_open**](ProviderProjectDevelopmentApi.md#provider_project_development_sideapp_open) | **POST** /provider/{locationId}/project/{projectId}/development/{developmentId}/sideapp/{sideappId}/actions/open | Open provider/development.sideapp
[**provider_project_development_snapshot_create**](ProviderProjectDevelopmentApi.md#provider_project_development_snapshot_create) | **POST** /provider/{locationId}/project/{projectId}/development/{developmentId}/snapshot | Create provider/development.snapshot
[**provider_project_development_snapshot_delete**](ProviderProjectDevelopmentApi.md#provider_project_development_snapshot_delete) | **DELETE** /provider/{locationId}/project/{projectId}/development/{developmentId}/snapshot/{snapshotId} | Delete provider/development.snapshot
[**provider_project_development_snapshot_download**](ProviderProjectDevelopmentApi.md#provider_project_development_snapshot_download) | **POST** /provider/{locationId}/project/{projectId}/development/{developmentId}/snapshot/{snapshotId}/actions/download | Download provider/development.snapshot
[**provider_project_development_snapshot_get**](ProviderProjectDevelopmentApi.md#provider_project_development_snapshot_get) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/snapshot/{snapshotId} | Get provider/development.snapshot
[**provider_project_development_snapshot_list**](ProviderProjectDevelopmentApi.md#provider_project_development_snapshot_list) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/snapshot | List provider/development.snapshot
[**provider_project_development_start**](ProviderProjectDevelopmentApi.md#provider_project_development_start) | **POST** /provider/{locationId}/project/{projectId}/development/{developmentId}/actions/start | Start provider/development
[**provider_project_development_stop**](ProviderProjectDevelopmentApi.md#provider_project_development_stop) | **POST** /provider/{locationId}/project/{projectId}/development/{developmentId}/actions/stop | Stop provider/development
[**provider_project_development_tag_create**](ProviderProjectDevelopmentApi.md#provider_project_development_tag_create) | **POST** /provider/{locationId}/project/{projectId}/development/{developmentId}/tag | Create provider/development.tag
[**provider_project_development_tag_delete**](ProviderProjectDevelopmentApi.md#provider_project_development_tag_delete) | **DELETE** /provider/{locationId}/project/{projectId}/development/{developmentId}/tag/{tagId} | Delete provider/development.tag
[**provider_project_development_tag_get**](ProviderProjectDevelopmentApi.md#provider_project_development_tag_get) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/tag/{tagId} | Get provider/development.tag
[**provider_project_development_tag_list**](ProviderProjectDevelopmentApi.md#provider_project_development_tag_list) | **GET** /provider/{locationId}/project/{projectId}/development/{developmentId}/tag | List provider/development.tag
[**provider_project_development_tag_put**](ProviderProjectDevelopmentApi.md#provider_project_development_tag_put) | **PUT** /provider/{locationId}/project/{projectId}/development/{developmentId}/tag | Replace provider/development.tag
[**provider_project_development_transfer**](ProviderProjectDevelopmentApi.md#provider_project_development_transfer) | **POST** /provider/{locationId}/project/{projectId}/development/{developmentId}/actions/transfer | Transfer provider/development
[**provider_project_development_update**](ProviderProjectDevelopmentApi.md#provider_project_development_update) | **PATCH** /provider/{locationId}/project/{projectId}/development/{developmentId} | Update provider/development


# **provider_project_development_connect_get**
> ResourceConnect provider_project_development_connect_get(project_id, location_id, development_id, connect_id)

Get provider/development.connect

Get provider/development.connect

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.resource_connect import ResourceConnect
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    connect_id = "connectId_example" # str | connectId

    # example passing only required values which don't have defaults set
    try:
        # Get provider/development.connect
        api_response = api_instance.provider_project_development_connect_get(project_id, location_id, development_id, connect_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_connect_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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

# **provider_project_development_connect_list**
> [ResourceConnect] provider_project_development_connect_list(project_id, location_id, development_id)

List provider/development.connect

List provider/development.connect

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.resource_connect import ResourceConnect
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id

    # example passing only required values which don't have defaults set
    try:
        # List provider/development.connect
        api_response = api_instance.provider_project_development_connect_list(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_connect_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |

### Return type

[**[ResourceConnect]**](ResourceConnect.md)

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

# **provider_project_development_create**
> Development provider_project_development_create(project_id, location_id, provider_project_development_create)

Create provider/development

Create development

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.development import Development
from h1.model.provider_project_development_create import ProviderProjectDevelopmentCreate
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    provider_project_development_create = ProviderProjectDevelopmentCreate(
        name="name_example",
        service="service_example",
        env=[
            ProviderEnv(
                id="id_example",
                name="name_example",
                value="value_example",
            ),
        ],
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # ProviderProjectDevelopmentCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create provider/development
        api_response = api_instance.provider_project_development_create(project_id, location_id, provider_project_development_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create provider/development
        api_response = api_instance.provider_project_development_create(project_id, location_id, provider_project_development_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **provider_project_development_create** | [**ProviderProjectDevelopmentCreate**](ProviderProjectDevelopmentCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Development**](Development.md)

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

# **provider_project_development_credential_create**
> DevelopmentCredential provider_project_development_credential_create(project_id, location_id, development_id, development_credential)

Create provider/development.credential

Create provider/development.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.development_credential import DevelopmentCredential
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    development_credential = DevelopmentCredential(
        id="id_example",
        name="name_example",
        created_by="created_by_example",
        created_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
        type="type_example",
        value="value_example",
        fingerprint="fingerprint_example",
        token="token_example",
    ) # DevelopmentCredential | 

    # example passing only required values which don't have defaults set
    try:
        # Create provider/development.credential
        api_response = api_instance.provider_project_development_credential_create(project_id, location_id, development_id, development_credential)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_credential_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **development_credential** | [**DevelopmentCredential**](DevelopmentCredential.md)|  |

### Return type

[**DevelopmentCredential**](DevelopmentCredential.md)

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

# **provider_project_development_credential_delete**
> Development provider_project_development_credential_delete(project_id, location_id, development_id, credential_id)

Delete provider/development.credential

Delete provider/development.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.development import Development
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Delete provider/development.credential
        api_response = api_instance.provider_project_development_credential_delete(project_id, location_id, development_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_credential_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **credential_id** | **str**| credentialId |

### Return type

[**Development**](Development.md)

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

# **provider_project_development_credential_get**
> DevelopmentCredential provider_project_development_credential_get(project_id, location_id, development_id, credential_id)

Get provider/development.credential

Get provider/development.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.development_credential import DevelopmentCredential
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Get provider/development.credential
        api_response = api_instance.provider_project_development_credential_get(project_id, location_id, development_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_credential_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **credential_id** | **str**| credentialId |

### Return type

[**DevelopmentCredential**](DevelopmentCredential.md)

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

# **provider_project_development_credential_list**
> [DevelopmentCredential] provider_project_development_credential_list(project_id, location_id, development_id)

List provider/development.credential

List provider/development.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.development_credential import DevelopmentCredential
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id

    # example passing only required values which don't have defaults set
    try:
        # List provider/development.credential
        api_response = api_instance.provider_project_development_credential_list(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_credential_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |

### Return type

[**[DevelopmentCredential]**](DevelopmentCredential.md)

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

# **provider_project_development_credential_patch**
> DevelopmentCredential provider_project_development_credential_patch(project_id, location_id, development_id, credential_id, provider_project_development_credential_patch)

Update provider/development.credential

Update provider/development.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_project_development_credential_patch import ProviderProjectDevelopmentCredentialPatch
from h1.model.development_credential import DevelopmentCredential
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    credential_id = "credentialId_example" # str | credentialId
    provider_project_development_credential_patch = ProviderProjectDevelopmentCredentialPatch(
        name="name_example",
    ) # ProviderProjectDevelopmentCredentialPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update provider/development.credential
        api_response = api_instance.provider_project_development_credential_patch(project_id, location_id, development_id, credential_id, provider_project_development_credential_patch)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_credential_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **credential_id** | **str**| credentialId |
 **provider_project_development_credential_patch** | [**ProviderProjectDevelopmentCredentialPatch**](ProviderProjectDevelopmentCredentialPatch.md)|  |

### Return type

[**DevelopmentCredential**](DevelopmentCredential.md)

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

# **provider_project_development_delete**
> provider_project_development_delete(project_id, location_id, development_id)

Delete provider/development

Delete development

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id

    # example passing only required values which don't have defaults set
    try:
        # Delete provider/development
        api_instance.provider_project_development_delete(project_id, location_id, development_id)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |

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

# **provider_project_development_domain_create**
> Domain provider_project_development_domain_create(project_id, location_id, development_id, domain)

Create provider/development.domain

Create provider/development.domain

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.domain import Domain
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    domain = Domain(
        id="id_example",
        value="value_example",
    ) # Domain | 

    # example passing only required values which don't have defaults set
    try:
        # Create provider/development.domain
        api_response = api_instance.provider_project_development_domain_create(project_id, location_id, development_id, domain)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_domain_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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

# **provider_project_development_domain_delete**
> provider_project_development_domain_delete(project_id, location_id, development_id, domain_id)

Delete provider/development.domain

Delete provider/development.domain

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    domain_id = "domainId_example" # str | domainId

    # example passing only required values which don't have defaults set
    try:
        # Delete provider/development.domain
        api_instance.provider_project_development_domain_delete(project_id, location_id, development_id, domain_id)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_domain_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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

# **provider_project_development_domain_get**
> Domain provider_project_development_domain_get(project_id, location_id, development_id, domain_id)

Get provider/development.domain

Get provider/development.domain

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.domain import Domain
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    domain_id = "domainId_example" # str | domainId

    # example passing only required values which don't have defaults set
    try:
        # Get provider/development.domain
        api_response = api_instance.provider_project_development_domain_get(project_id, location_id, development_id, domain_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_domain_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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

# **provider_project_development_domain_list**
> [Domain] provider_project_development_domain_list(project_id, location_id, development_id)

List provider/development.domain

List provider/development.domain

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.domain import Domain
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id

    # example passing only required values which don't have defaults set
    try:
        # List provider/development.domain
        api_response = api_instance.provider_project_development_domain_list(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_domain_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |

### Return type

[**[Domain]**](Domain.md)

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

# **provider_project_development_env_create**
> ProviderEnv provider_project_development_env_create(project_id, location_id, development_id, provider_env)

Create provider/development.env

Create provider/development.env

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_env import ProviderEnv
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    provider_env = ProviderEnv(
        id="id_example",
        name="name_example",
        value="value_example",
    ) # ProviderEnv | 

    # example passing only required values which don't have defaults set
    try:
        # Create provider/development.env
        api_response = api_instance.provider_project_development_env_create(project_id, location_id, development_id, provider_env)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_env_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **provider_env** | [**ProviderEnv**](ProviderEnv.md)|  |

### Return type

[**ProviderEnv**](ProviderEnv.md)

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

# **provider_project_development_env_delete**
> provider_project_development_env_delete(project_id, location_id, development_id, env_id)

Delete provider/development.env

Delete provider/development.env

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    env_id = "envId_example" # str | envId

    # example passing only required values which don't have defaults set
    try:
        # Delete provider/development.env
        api_instance.provider_project_development_env_delete(project_id, location_id, development_id, env_id)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_env_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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

# **provider_project_development_env_get**
> ProviderEnv provider_project_development_env_get(project_id, location_id, development_id, env_id)

Get provider/development.env

Get provider/development.env

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_env import ProviderEnv
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    env_id = "envId_example" # str | envId

    # example passing only required values which don't have defaults set
    try:
        # Get provider/development.env
        api_response = api_instance.provider_project_development_env_get(project_id, location_id, development_id, env_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_env_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **env_id** | **str**| envId |

### Return type

[**ProviderEnv**](ProviderEnv.md)

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

# **provider_project_development_env_list**
> [ProviderEnv] provider_project_development_env_list(project_id, location_id, development_id)

List provider/development.env

List provider/development.env

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_env import ProviderEnv
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id

    # example passing only required values which don't have defaults set
    try:
        # List provider/development.env
        api_response = api_instance.provider_project_development_env_list(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_env_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |

### Return type

[**[ProviderEnv]**](ProviderEnv.md)

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

# **provider_project_development_event_get**
> Event provider_project_development_event_get(project_id, location_id, development_id, event_id)

Get provider/development.event

Get provider/development.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get provider/development.event
        api_response = api_instance.provider_project_development_event_get(project_id, location_id, development_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_event_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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

# **provider_project_development_event_list**
> [Event] provider_project_development_event_list(project_id, location_id, development_id)

List provider/development.event

List provider/development.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List provider/development.event
        api_response = api_instance.provider_project_development_event_list(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List provider/development.event
        api_response = api_instance.provider_project_development_event_list(project_id, location_id, development_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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

# **provider_project_development_get**
> Development provider_project_development_get(project_id, location_id, development_id)

Get provider/development

Returns a single development

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.development import Development
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id

    # example passing only required values which don't have defaults set
    try:
        # Get provider/development
        api_response = api_instance.provider_project_development_get(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |

### Return type

[**Development**](Development.md)

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

# **provider_project_development_link_create**
> ProviderLink provider_project_development_link_create(project_id, location_id, development_id, provider_link)

Create provider/development.link

Create provider/development.link

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_link import ProviderLink
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    provider_link = ProviderLink(
        id="id_example",
        actor="actor_example",
        purpose="logs",
        resource="resource_example",
    ) # ProviderLink | 

    # example passing only required values which don't have defaults set
    try:
        # Create provider/development.link
        api_response = api_instance.provider_project_development_link_create(project_id, location_id, development_id, provider_link)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_link_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **provider_link** | [**ProviderLink**](ProviderLink.md)|  |

### Return type

[**ProviderLink**](ProviderLink.md)

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

# **provider_project_development_link_delete**
> provider_project_development_link_delete(project_id, location_id, development_id, link_id)

Delete provider/development.link

Delete provider/development.link

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    link_id = "linkId_example" # str | linkId

    # example passing only required values which don't have defaults set
    try:
        # Delete provider/development.link
        api_instance.provider_project_development_link_delete(project_id, location_id, development_id, link_id)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_link_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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

# **provider_project_development_link_get**
> ProviderLink provider_project_development_link_get(project_id, location_id, development_id, link_id)

Get provider/development.link

Get provider/development.link

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_link import ProviderLink
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    link_id = "linkId_example" # str | linkId

    # example passing only required values which don't have defaults set
    try:
        # Get provider/development.link
        api_response = api_instance.provider_project_development_link_get(project_id, location_id, development_id, link_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_link_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **link_id** | **str**| linkId |

### Return type

[**ProviderLink**](ProviderLink.md)

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

# **provider_project_development_link_list**
> [ProviderLink] provider_project_development_link_list(project_id, location_id, development_id)

List provider/development.link

List provider/development.link

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_link import ProviderLink
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id

    # example passing only required values which don't have defaults set
    try:
        # List provider/development.link
        api_response = api_instance.provider_project_development_link_list(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_link_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |

### Return type

[**[ProviderLink]**](ProviderLink.md)

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

# **provider_project_development_list**
> [Development] provider_project_development_list(project_id, location_id)

List provider/development

List development

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.development import Development
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List provider/development
        api_response = api_instance.provider_project_development_list(project_id, location_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List provider/development
        api_response = api_instance.provider_project_development_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_list: %s\n" % e)
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

[**[Development]**](Development.md)

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

# **provider_project_development_log_get**
> ProviderLog provider_project_development_log_get(project_id, location_id, development_id, log_id)

Get provider/development.log

Get provider/development.log

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_log import ProviderLog
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    log_id = "logId_example" # str | logId

    # example passing only required values which don't have defaults set
    try:
        # Get provider/development.log
        api_response = api_instance.provider_project_development_log_get(project_id, location_id, development_id, log_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_log_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **log_id** | **str**| logId |

### Return type

[**ProviderLog**](ProviderLog.md)

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

# **provider_project_development_log_list**
> [ProviderLog] provider_project_development_log_list(project_id, location_id, development_id)

List provider/development.log

List provider/development.log

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_log import ProviderLog
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id

    # example passing only required values which don't have defaults set
    try:
        # List provider/development.log
        api_response = api_instance.provider_project_development_log_list(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_log_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |

### Return type

[**[ProviderLog]**](ProviderLog.md)

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

# **provider_project_development_log_read**
> provider_project_development_log_read(project_id, location_id, development_id, log_id)

Read provider/development.log

action read

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    log_id = "logId_example" # str | logId

    # example passing only required values which don't have defaults set
    try:
        # Read provider/development.log
        api_instance.provider_project_development_log_read(project_id, location_id, development_id, log_id)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_log_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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

# **provider_project_development_metric_get**
> Metric provider_project_development_metric_get(project_id, location_id, development_id, metric_id)

Get provider/development.metric

Get provider/development.metric

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.metric import Metric
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    metric_id = "metricId_example" # str | metricId

    # example passing only required values which don't have defaults set
    try:
        # Get provider/development.metric
        api_response = api_instance.provider_project_development_metric_get(project_id, location_id, development_id, metric_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_metric_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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

# **provider_project_development_metric_list**
> [Metric] provider_project_development_metric_list(project_id, location_id, development_id)

List provider/development.metric

List provider/development.metric

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.metric import Metric
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id

    # example passing only required values which don't have defaults set
    try:
        # List provider/development.metric
        api_response = api_instance.provider_project_development_metric_list(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_metric_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |

### Return type

[**[Metric]**](Metric.md)

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

# **provider_project_development_metric_point_list**
> [Point] provider_project_development_metric_point_list(project_id, location_id, development_id, metric_id)

List provider/development.point

List provider/development.point

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.point import Point
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    metric_id = "metricId_example" # str | metricId
    interval = "interval_example" # str | interval (optional)
    timespan = "timespan_example" # str | timespan (optional)

    # example passing only required values which don't have defaults set
    try:
        # List provider/development.point
        api_response = api_instance.provider_project_development_metric_point_list(project_id, location_id, development_id, metric_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_metric_point_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List provider/development.point
        api_response = api_instance.provider_project_development_metric_point_list(project_id, location_id, development_id, metric_id, interval=interval, timespan=timespan)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_metric_point_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **metric_id** | **str**| metricId |
 **interval** | **str**| interval | [optional]
 **timespan** | **str**| timespan | [optional]

### Return type

[**[Point]**](Point.md)

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

# **provider_project_development_restart**
> Development provider_project_development_restart(project_id, location_id, development_id)

Restart provider/development

action restart

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.development import Development
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Restart provider/development
        api_response = api_instance.provider_project_development_restart(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_restart: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Restart provider/development
        api_response = api_instance.provider_project_development_restart(project_id, location_id, development_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_restart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Development**](Development.md)

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

# **provider_project_development_service_get**
> ResourceService provider_project_development_service_get(project_id, location_id, development_id, service_id)

Get provider/development.service

Get provider/development.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get provider/development.service
        api_response = api_instance.provider_project_development_service_get(project_id, location_id, development_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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

# **provider_project_development_service_list**
> [ResourceService] provider_project_development_service_list(project_id, location_id, development_id)

List provider/development.service

List provider/development.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id

    # example passing only required values which don't have defaults set
    try:
        # List provider/development.service
        api_response = api_instance.provider_project_development_service_list(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |

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

# **provider_project_development_sideapp_get**
> ProviderSideapp provider_project_development_sideapp_get(project_id, location_id, development_id, sideapp_id)

Get provider/development.sideapp

Get provider/development.sideapp

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_sideapp import ProviderSideapp
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    sideapp_id = "sideappId_example" # str | sideappId

    # example passing only required values which don't have defaults set
    try:
        # Get provider/development.sideapp
        api_response = api_instance.provider_project_development_sideapp_get(project_id, location_id, development_id, sideapp_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_sideapp_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **sideapp_id** | **str**| sideappId |

### Return type

[**ProviderSideapp**](ProviderSideapp.md)

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

# **provider_project_development_sideapp_list**
> [ProviderSideapp] provider_project_development_sideapp_list(project_id, location_id, development_id)

List provider/development.sideapp

List provider/development.sideapp

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_sideapp import ProviderSideapp
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id

    # example passing only required values which don't have defaults set
    try:
        # List provider/development.sideapp
        api_response = api_instance.provider_project_development_sideapp_list(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_sideapp_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |

### Return type

[**[ProviderSideapp]**](ProviderSideapp.md)

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

# **provider_project_development_sideapp_open**
> provider_project_development_sideapp_open(project_id, location_id, development_id, sideapp_id)

Open provider/development.sideapp

action open

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    sideapp_id = "sideappId_example" # str | sideappId

    # example passing only required values which don't have defaults set
    try:
        # Open provider/development.sideapp
        api_instance.provider_project_development_sideapp_open(project_id, location_id, development_id, sideapp_id)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_sideapp_open: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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
**201** | Request accepted |  * location - Absolute URL <br>  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provider_project_development_snapshot_create**
> ProviderSnapshot provider_project_development_snapshot_create(project_id, location_id, development_id, provider_snapshot)

Create provider/development.snapshot

Create provider/development.snapshot

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_snapshot import ProviderSnapshot
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    provider_snapshot = ProviderSnapshot(
        id="id_example",
        name="name_example",
        creation=dateutil_parser('1970-01-01T00:00:00.00Z'),
        used=3.14,
    ) # ProviderSnapshot | 

    # example passing only required values which don't have defaults set
    try:
        # Create provider/development.snapshot
        api_response = api_instance.provider_project_development_snapshot_create(project_id, location_id, development_id, provider_snapshot)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_snapshot_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **provider_snapshot** | [**ProviderSnapshot**](ProviderSnapshot.md)|  |

### Return type

[**ProviderSnapshot**](ProviderSnapshot.md)

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

# **provider_project_development_snapshot_delete**
> Development provider_project_development_snapshot_delete(project_id, location_id, development_id, snapshot_id)

Delete provider/development.snapshot

Delete provider/development.snapshot

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.development import Development
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    snapshot_id = "snapshotId_example" # str | snapshotId

    # example passing only required values which don't have defaults set
    try:
        # Delete provider/development.snapshot
        api_response = api_instance.provider_project_development_snapshot_delete(project_id, location_id, development_id, snapshot_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_snapshot_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **snapshot_id** | **str**| snapshotId |

### Return type

[**Development**](Development.md)

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

# **provider_project_development_snapshot_download**
> provider_project_development_snapshot_download(project_id, location_id, development_id, snapshot_id, provider_project_development_snapshot_download)

Download provider/development.snapshot

action download

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_project_development_snapshot_download import ProviderProjectDevelopmentSnapshotDownload
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    snapshot_id = "snapshotId_example" # str | snapshotId
    provider_project_development_snapshot_download = ProviderProjectDevelopmentSnapshotDownload(
        incremental="incremental_example",
    ) # ProviderProjectDevelopmentSnapshotDownload | 

    # example passing only required values which don't have defaults set
    try:
        # Download provider/development.snapshot
        api_instance.provider_project_development_snapshot_download(project_id, location_id, development_id, snapshot_id, provider_project_development_snapshot_download)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_snapshot_download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **snapshot_id** | **str**| snapshotId |
 **provider_project_development_snapshot_download** | [**ProviderProjectDevelopmentSnapshotDownload**](ProviderProjectDevelopmentSnapshotDownload.md)|  |

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

# **provider_project_development_snapshot_get**
> ProviderSnapshot provider_project_development_snapshot_get(project_id, location_id, development_id, snapshot_id)

Get provider/development.snapshot

Get provider/development.snapshot

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_snapshot import ProviderSnapshot
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    snapshot_id = "snapshotId_example" # str | snapshotId

    # example passing only required values which don't have defaults set
    try:
        # Get provider/development.snapshot
        api_response = api_instance.provider_project_development_snapshot_get(project_id, location_id, development_id, snapshot_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_snapshot_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **snapshot_id** | **str**| snapshotId |

### Return type

[**ProviderSnapshot**](ProviderSnapshot.md)

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

# **provider_project_development_snapshot_list**
> [ProviderSnapshot] provider_project_development_snapshot_list(project_id, location_id, development_id)

List provider/development.snapshot

List provider/development.snapshot

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_snapshot import ProviderSnapshot
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id

    # example passing only required values which don't have defaults set
    try:
        # List provider/development.snapshot
        api_response = api_instance.provider_project_development_snapshot_list(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_snapshot_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |

### Return type

[**[ProviderSnapshot]**](ProviderSnapshot.md)

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

# **provider_project_development_start**
> Development provider_project_development_start(project_id, location_id, development_id)

Start provider/development

action start

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.development import Development
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start provider/development
        api_response = api_instance.provider_project_development_start(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_start: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start provider/development
        api_response = api_instance.provider_project_development_start(project_id, location_id, development_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_start: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Development**](Development.md)

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

# **provider_project_development_stop**
> Development provider_project_development_stop(project_id, location_id, development_id)

Stop provider/development

action stop

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.development import Development
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Stop provider/development
        api_response = api_instance.provider_project_development_stop(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_stop: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Stop provider/development
        api_response = api_instance.provider_project_development_stop(project_id, location_id, development_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_stop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Development**](Development.md)

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

# **provider_project_development_tag_create**
> Tag provider_project_development_tag_create(project_id, location_id, development_id, tag)

Create provider/development.tag

Create provider/development.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create provider/development.tag
        api_response = api_instance.provider_project_development_tag_create(project_id, location_id, development_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_tag_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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

# **provider_project_development_tag_delete**
> provider_project_development_tag_delete(project_id, location_id, development_id, tag_id)

Delete provider/development.tag

Delete provider/development.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete provider/development.tag
        api_instance.provider_project_development_tag_delete(project_id, location_id, development_id, tag_id)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_tag_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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

# **provider_project_development_tag_get**
> Tag provider_project_development_tag_get(project_id, location_id, development_id, tag_id)

Get provider/development.tag

Get provider/development.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get provider/development.tag
        api_response = api_instance.provider_project_development_tag_get(project_id, location_id, development_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_tag_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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

# **provider_project_development_tag_list**
> [Tag] provider_project_development_tag_list(project_id, location_id, development_id)

List provider/development.tag

List provider/development.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id

    # example passing only required values which don't have defaults set
    try:
        # List provider/development.tag
        api_response = api_instance.provider_project_development_tag_list(project_id, location_id, development_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_tag_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |

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

# **provider_project_development_tag_put**
> [Tag] provider_project_development_tag_put(project_id, location_id, development_id, tag_array)

Replace provider/development.tag

Replace provider/development.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace provider/development.tag
        api_response = api_instance.provider_project_development_tag_put(project_id, location_id, development_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_tag_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
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

# **provider_project_development_transfer**
> Development provider_project_development_transfer(project_id, location_id, development_id, provider_project_development_transfer)

Transfer provider/development

action transfer

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.provider_project_development_transfer import ProviderProjectDevelopmentTransfer
from h1.model.development import Development
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    provider_project_development_transfer = ProviderProjectDevelopmentTransfer(
        project="project_example",
    ) # ProviderProjectDevelopmentTransfer | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Transfer provider/development
        api_response = api_instance.provider_project_development_transfer(project_id, location_id, development_id, provider_project_development_transfer)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_transfer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Transfer provider/development
        api_response = api_instance.provider_project_development_transfer(project_id, location_id, development_id, provider_project_development_transfer, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_transfer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **provider_project_development_transfer** | [**ProviderProjectDevelopmentTransfer**](ProviderProjectDevelopmentTransfer.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Development**](Development.md)

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

# **provider_project_development_update**
> Development provider_project_development_update(project_id, location_id, development_id, provider_project_development_update)

Update provider/development

Returns modified development

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import provider_project_development_api
from h1.model.development import Development
from h1.model.provider_project_development_update import ProviderProjectDevelopmentUpdate
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
    api_instance = provider_project_development_api.ProviderProjectDevelopmentApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    development_id = "developmentId_example" # str | Development Id
    provider_project_development_update = ProviderProjectDevelopmentUpdate(
        name="name_example",
    ) # ProviderProjectDevelopmentUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update provider/development
        api_response = api_instance.provider_project_development_update(project_id, location_id, development_id, provider_project_development_update)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ProviderProjectDevelopmentApi->provider_project_development_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **development_id** | **str**| Development Id |
 **provider_project_development_update** | [**ProviderProjectDevelopmentUpdate**](ProviderProjectDevelopmentUpdate.md)|  |

### Return type

[**Development**](Development.md)

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

