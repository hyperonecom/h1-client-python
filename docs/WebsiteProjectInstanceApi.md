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
[**website_project_instance_sideapp_get**](WebsiteProjectInstanceApi.md#website_project_instance_sideapp_get) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/sideapp/{sideappId} | Get website/instance.sideapp
[**website_project_instance_sideapp_list**](WebsiteProjectInstanceApi.md#website_project_instance_sideapp_list) | **GET** /website/{locationId}/project/{projectId}/instance/{instanceId}/sideapp | List website/instance.sideapp
[**website_project_instance_sideapp_open**](WebsiteProjectInstanceApi.md#website_project_instance_sideapp_open) | **POST** /website/{locationId}/project/{projectId}/instance/{instanceId}/sideapp/{sideappId}/actions/open | Open website/instance.sideapp
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
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    connect_id = "connectId_example" # str | connectId

    # example passing only required values which don't have defaults set
    try:
        # Get website/instance.connect
        api_response = api_instance.website_project_instance_connect_get(project_id, location_id, instance_id, connect_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [ResourceConnect] website_project_instance_connect_list(project_id, location_id, instance_id)

List website/instance.connect

List website/instance.connect

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # List website/instance.connect
        api_response = api_instance.website_project_instance_connect_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_connect_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |

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

# **website_project_instance_create**
> Website website_project_instance_create(project_id, location_id, website_project_instance_create)

Create website/instance

Create instance

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website import Website
from h1.model.website_project_instance_create import WebsiteProjectInstanceCreate
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    website_project_instance_create = WebsiteProjectInstanceCreate(
        name="name_example",
        service="service_example",
        image="image_example",
        source="source_example",
        env=[
            WebsiteEnv(
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
    ) # WebsiteProjectInstanceCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create website/instance
        api_response = api_instance.website_project_instance_create(project_id, location_id, website_project_instance_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create website/instance
        api_response = api_instance.website_project_instance_create(project_id, location_id, website_project_instance_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **website_project_instance_create** | [**WebsiteProjectInstanceCreate**](WebsiteProjectInstanceCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_credential import WebsiteCredential
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    website_credential = WebsiteCredential(
        id="id_example",
        name="name_example",
        created_by="created_by_example",
        created_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
        type="ssh",
        value="value_example",
        fingerprint="fingerprint_example",
        token="token_example",
    ) # WebsiteCredential | 

    # example passing only required values which don't have defaults set
    try:
        # Create website/instance.credential
        api_response = api_instance.website_project_instance_credential_create(project_id, location_id, instance_id, website_credential)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website import Website
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Delete website/instance.credential
        api_response = api_instance.website_project_instance_credential_delete(project_id, location_id, instance_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_credential import WebsiteCredential
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Get website/instance.credential
        api_response = api_instance.website_project_instance_credential_get(project_id, location_id, instance_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [WebsiteCredential] website_project_instance_credential_list(project_id, location_id, instance_id)

List website/instance.credential

List website/instance.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_credential import WebsiteCredential
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # List website/instance.credential
        api_response = api_instance.website_project_instance_credential_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_credential_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |

### Return type

[**[WebsiteCredential]**](WebsiteCredential.md)

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
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_project_instance_credential_patch import WebsiteProjectInstanceCredentialPatch
from h1.model.website_credential import WebsiteCredential
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    credential_id = "credentialId_example" # str | credentialId
    website_project_instance_credential_patch = WebsiteProjectInstanceCredentialPatch(
        name="name_example",
    ) # WebsiteProjectInstanceCredentialPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update website/instance.credential
        api_response = api_instance.website_project_instance_credential_patch(project_id, location_id, instance_id, credential_id, website_project_instance_credential_patch)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # Delete website/instance
        api_instance.website_project_instance_delete(project_id, location_id, instance_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    domain = Domain(
        id="id_example",
        value="value_example",
    ) # Domain | 

    # example passing only required values which don't have defaults set
    try:
        # Create website/instance.domain
        api_response = api_instance.website_project_instance_domain_create(project_id, location_id, instance_id, domain)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    domain_id = "domainId_example" # str | domainId

    # example passing only required values which don't have defaults set
    try:
        # Delete website/instance.domain
        api_instance.website_project_instance_domain_delete(project_id, location_id, instance_id, domain_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    domain_id = "domainId_example" # str | domainId

    # example passing only required values which don't have defaults set
    try:
        # Get website/instance.domain
        api_response = api_instance.website_project_instance_domain_get(project_id, location_id, instance_id, domain_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Domain] website_project_instance_domain_list(project_id, location_id, instance_id)

List website/instance.domain

List website/instance.domain

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # List website/instance.domain
        api_response = api_instance.website_project_instance_domain_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_domain_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |

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

# **website_project_instance_env_create**
> WebsiteEnv website_project_instance_env_create(project_id, location_id, instance_id, website_env)

Create website/instance.env

Create website/instance.env

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_env import WebsiteEnv
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    website_env = WebsiteEnv(
        id="id_example",
        name="name_example",
        value="value_example",
    ) # WebsiteEnv | 

    # example passing only required values which don't have defaults set
    try:
        # Create website/instance.env
        api_response = api_instance.website_project_instance_env_create(project_id, location_id, instance_id, website_env)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    env_id = "envId_example" # str | envId

    # example passing only required values which don't have defaults set
    try:
        # Delete website/instance.env
        api_instance.website_project_instance_env_delete(project_id, location_id, instance_id, env_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_env import WebsiteEnv
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    env_id = "envId_example" # str | envId

    # example passing only required values which don't have defaults set
    try:
        # Get website/instance.env
        api_response = api_instance.website_project_instance_env_get(project_id, location_id, instance_id, env_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [WebsiteEnv] website_project_instance_env_list(project_id, location_id, instance_id)

List website/instance.env

List website/instance.env

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_env import WebsiteEnv
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # List website/instance.env
        api_response = api_instance.website_project_instance_env_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_env_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |

### Return type

[**[WebsiteEnv]**](WebsiteEnv.md)

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
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get website/instance.event
        api_response = api_instance.website_project_instance_event_get(project_id, location_id, instance_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Event] website_project_instance_event_list(project_id, location_id, instance_id)

List website/instance.event

List website/instance.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List website/instance.event
        api_response = api_instance.website_project_instance_event_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List website/instance.event
        api_response = api_instance.website_project_instance_event_list(project_id, location_id, instance_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |
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

# **website_project_instance_get**
> Website website_project_instance_get(project_id, location_id, instance_id)

Get website/instance

Returns a single instance

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website import Website
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # Get website/instance
        api_response = api_instance.website_project_instance_get(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_link import WebsiteLink
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    website_link = WebsiteLink(
        id="id_example",
        actor="actor_example",
        purpose="logs",
        resource="resource_example",
    ) # WebsiteLink | 

    # example passing only required values which don't have defaults set
    try:
        # Create website/instance.link
        api_response = api_instance.website_project_instance_link_create(project_id, location_id, instance_id, website_link)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    link_id = "linkId_example" # str | linkId

    # example passing only required values which don't have defaults set
    try:
        # Delete website/instance.link
        api_instance.website_project_instance_link_delete(project_id, location_id, instance_id, link_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_link import WebsiteLink
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    link_id = "linkId_example" # str | linkId

    # example passing only required values which don't have defaults set
    try:
        # Get website/instance.link
        api_response = api_instance.website_project_instance_link_get(project_id, location_id, instance_id, link_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [WebsiteLink] website_project_instance_link_list(project_id, location_id, instance_id)

List website/instance.link

List website/instance.link

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_link import WebsiteLink
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # List website/instance.link
        api_response = api_instance.website_project_instance_link_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_link_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |

### Return type

[**[WebsiteLink]**](WebsiteLink.md)

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
> [Website] website_project_instance_list(project_id, location_id)

List website/instance

List instance

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website import Website
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List website/instance
        api_response = api_instance.website_project_instance_list(project_id, location_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List website/instance
        api_response = api_instance.website_project_instance_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
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

[**[Website]**](Website.md)

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
import time
import h1
from h1.api import website_project_instance_api
from h1.model.log import Log
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    log_id = "logId_example" # str | logId

    # example passing only required values which don't have defaults set
    try:
        # Get website/instance.log
        api_response = api_instance.website_project_instance_log_get(project_id, location_id, instance_id, log_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Log] website_project_instance_log_list(project_id, location_id, instance_id)

List website/instance.log

List website/instance.log

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
from h1.model.log import Log
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # List website/instance.log
        api_response = api_instance.website_project_instance_log_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_log_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |

### Return type

[**[Log]**](Log.md)

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
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    log_id = "logId_example" # str | logId

    # example passing only required values which don't have defaults set
    try:
        # Read website/instance.log
        api_instance.website_project_instance_log_read(project_id, location_id, instance_id, log_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    metric_id = "metricId_example" # str | metricId

    # example passing only required values which don't have defaults set
    try:
        # Get website/instance.metric
        api_response = api_instance.website_project_instance_metric_get(project_id, location_id, instance_id, metric_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Metric] website_project_instance_metric_list(project_id, location_id, instance_id)

List website/instance.metric

List website/instance.metric

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # List website/instance.metric
        api_response = api_instance.website_project_instance_metric_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_metric_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |

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

# **website_project_instance_metric_point_list**
> [Point] website_project_instance_metric_point_list(project_id, location_id, instance_id, metric_id)

List website/instance.point

List website/instance.point

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    metric_id = "metricId_example" # str | metricId
    interval = "interval_example" # str | interval (optional)
    timespan = "timespan_example" # str | timespan (optional)

    # example passing only required values which don't have defaults set
    try:
        # List website/instance.point
        api_response = api_instance.website_project_instance_metric_point_list(project_id, location_id, instance_id, metric_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_metric_point_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List website/instance.point
        api_response = api_instance.website_project_instance_metric_point_list(project_id, location_id, instance_id, metric_id, interval=interval, timespan=timespan)
        pprint(api_response)
    except h1.ApiException as e:
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

# **website_project_instance_restart**
> Website website_project_instance_restart(project_id, location_id, instance_id)

Restart website/instance

action restart

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website import Website
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Restart website/instance
        api_response = api_instance.website_project_instance_restart(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_restart: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Restart website/instance
        api_response = api_instance.website_project_instance_restart(project_id, location_id, instance_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_restart: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get website/instance.service
        api_response = api_instance.website_project_instance_service_get(project_id, location_id, instance_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [ResourceService] website_project_instance_service_list(project_id, location_id, instance_id)

List website/instance.service

List website/instance.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # List website/instance.service
        api_response = api_instance.website_project_instance_service_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |

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

# **website_project_instance_sideapp_get**
> WebsiteSideapp website_project_instance_sideapp_get(project_id, location_id, instance_id, sideapp_id)

Get website/instance.sideapp

Get website/instance.sideapp

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_sideapp import WebsiteSideapp
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    sideapp_id = "sideappId_example" # str | sideappId

    # example passing only required values which don't have defaults set
    try:
        # Get website/instance.sideapp
        api_response = api_instance.website_project_instance_sideapp_get(project_id, location_id, instance_id, sideapp_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [WebsiteSideapp] website_project_instance_sideapp_list(project_id, location_id, instance_id)

List website/instance.sideapp

List website/instance.sideapp

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_sideapp import WebsiteSideapp
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # List website/instance.sideapp
        api_response = api_instance.website_project_instance_sideapp_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_sideapp_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |

### Return type

[**[WebsiteSideapp]**](WebsiteSideapp.md)

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

# **website_project_instance_sideapp_open**
> website_project_instance_sideapp_open(project_id, location_id, instance_id, sideapp_id)

Open website/instance.sideapp

action open

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    sideapp_id = "sideappId_example" # str | sideappId

    # example passing only required values which don't have defaults set
    try:
        # Open website/instance.sideapp
        api_instance.website_project_instance_sideapp_open(project_id, location_id, instance_id, sideapp_id)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_sideapp_open: %s\n" % e)
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
**201** | Request accepted |  * location - Absolute URL <br>  |
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
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_snapshot import WebsiteSnapshot
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    website_snapshot = WebsiteSnapshot(
        id="id_example",
        name="name_example",
        creation=dateutil_parser('1970-01-01T00:00:00.00Z'),
        used=3.14,
    ) # WebsiteSnapshot | 

    # example passing only required values which don't have defaults set
    try:
        # Create website/instance.snapshot
        api_response = api_instance.website_project_instance_snapshot_create(project_id, location_id, instance_id, website_snapshot)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website import Website
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    snapshot_id = "snapshotId_example" # str | snapshotId

    # example passing only required values which don't have defaults set
    try:
        # Delete website/instance.snapshot
        api_response = api_instance.website_project_instance_snapshot_delete(project_id, location_id, instance_id, snapshot_id)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_project_instance_snapshot_download import WebsiteProjectInstanceSnapshotDownload
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    snapshot_id = "snapshotId_example" # str | snapshotId
    website_project_instance_snapshot_download = WebsiteProjectInstanceSnapshotDownload(
        incremental="incremental_example",
    ) # WebsiteProjectInstanceSnapshotDownload | 

    # example passing only required values which don't have defaults set
    try:
        # Download website/instance.snapshot
        api_instance.website_project_instance_snapshot_download(project_id, location_id, instance_id, snapshot_id, website_project_instance_snapshot_download)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_snapshot import WebsiteSnapshot
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    snapshot_id = "snapshotId_example" # str | snapshotId

    # example passing only required values which don't have defaults set
    try:
        # Get website/instance.snapshot
        api_response = api_instance.website_project_instance_snapshot_get(project_id, location_id, instance_id, snapshot_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [WebsiteSnapshot] website_project_instance_snapshot_list(project_id, location_id, instance_id)

List website/instance.snapshot

List website/instance.snapshot

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website_snapshot import WebsiteSnapshot
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # List website/instance.snapshot
        api_response = api_instance.website_project_instance_snapshot_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_snapshot_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |

### Return type

[**[WebsiteSnapshot]**](WebsiteSnapshot.md)

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
> Website website_project_instance_start(project_id, location_id, instance_id)

Start website/instance

action start

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website import Website
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start website/instance
        api_response = api_instance.website_project_instance_start(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_start: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start website/instance
        api_response = api_instance.website_project_instance_start(project_id, location_id, instance_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

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
> Website website_project_instance_stop(project_id, location_id, instance_id)

Stop website/instance

action stop

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website import Website
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Stop website/instance
        api_response = api_instance.website_project_instance_stop(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_stop: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Stop website/instance
        api_response = api_instance.website_project_instance_stop(project_id, location_id, instance_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create website/instance.tag
        api_response = api_instance.website_project_instance_tag_create(project_id, location_id, instance_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete website/instance.tag
        api_instance.website_project_instance_tag_delete(project_id, location_id, instance_id, tag_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get website/instance.tag
        api_response = api_instance.website_project_instance_tag_get(project_id, location_id, instance_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Tag] website_project_instance_tag_list(project_id, location_id, instance_id)

List website/instance.tag

List website/instance.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # List website/instance.tag
        api_response = api_instance.website_project_instance_tag_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |

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

# **website_project_instance_tag_put**
> [Tag] website_project_instance_tag_put(project_id, location_id, instance_id, tag_array)

Replace website/instance.tag

Replace website/instance.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace website/instance.tag
        api_response = api_instance.website_project_instance_tag_put(project_id, location_id, instance_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |
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

# **website_project_instance_transfer**
> Website website_project_instance_transfer(project_id, location_id, instance_id, website_project_instance_transfer)

Transfer website/instance

action transfer

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website import Website
from h1.model.website_project_instance_transfer import WebsiteProjectInstanceTransfer
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    website_project_instance_transfer = WebsiteProjectInstanceTransfer(
        project="project_example",
    ) # WebsiteProjectInstanceTransfer | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Transfer website/instance
        api_response = api_instance.website_project_instance_transfer(project_id, location_id, instance_id, website_project_instance_transfer)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling WebsiteProjectInstanceApi->website_project_instance_transfer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Transfer website/instance
        api_response = api_instance.website_project_instance_transfer(project_id, location_id, instance_id, website_project_instance_transfer, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
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
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import website_project_instance_api
from h1.model.website import Website
from h1.model.website_project_instance_update import WebsiteProjectInstanceUpdate
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
    api_instance = website_project_instance_api.WebsiteProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    website_project_instance_update = WebsiteProjectInstanceUpdate(
        name="name_example",
        image="image_example",
        plan="plan_example",
    ) # WebsiteProjectInstanceUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update website/instance
        api_response = api_instance.website_project_instance_update(project_id, location_id, instance_id, website_project_instance_update)
        pprint(api_response)
    except h1.ApiException as e:
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

