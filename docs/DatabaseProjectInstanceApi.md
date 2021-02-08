# h1.DatabaseProjectInstanceApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**database_project_instance_connect_get**](DatabaseProjectInstanceApi.md#database_project_instance_connect_get) | **GET** /database/{locationId}/project/{projectId}/instance/{instanceId}/connect/{connectId} | Get database/instance.connect
[**database_project_instance_connect_list**](DatabaseProjectInstanceApi.md#database_project_instance_connect_list) | **GET** /database/{locationId}/project/{projectId}/instance/{instanceId}/connect | List database/instance.connect
[**database_project_instance_create**](DatabaseProjectInstanceApi.md#database_project_instance_create) | **POST** /database/{locationId}/project/{projectId}/instance | Create database/instance
[**database_project_instance_credential_create**](DatabaseProjectInstanceApi.md#database_project_instance_credential_create) | **POST** /database/{locationId}/project/{projectId}/instance/{instanceId}/credential | Create database/instance.credential
[**database_project_instance_credential_delete**](DatabaseProjectInstanceApi.md#database_project_instance_credential_delete) | **DELETE** /database/{locationId}/project/{projectId}/instance/{instanceId}/credential/{credentialId} | Delete database/instance.credential
[**database_project_instance_credential_get**](DatabaseProjectInstanceApi.md#database_project_instance_credential_get) | **GET** /database/{locationId}/project/{projectId}/instance/{instanceId}/credential/{credentialId} | Get database/instance.credential
[**database_project_instance_credential_list**](DatabaseProjectInstanceApi.md#database_project_instance_credential_list) | **GET** /database/{locationId}/project/{projectId}/instance/{instanceId}/credential | List database/instance.credential
[**database_project_instance_credential_patch**](DatabaseProjectInstanceApi.md#database_project_instance_credential_patch) | **PATCH** /database/{locationId}/project/{projectId}/instance/{instanceId}/credential/{credentialId} | Update database/instance.credential
[**database_project_instance_delete**](DatabaseProjectInstanceApi.md#database_project_instance_delete) | **DELETE** /database/{locationId}/project/{projectId}/instance/{instanceId} | Delete database/instance
[**database_project_instance_event_get**](DatabaseProjectInstanceApi.md#database_project_instance_event_get) | **GET** /database/{locationId}/project/{projectId}/instance/{instanceId}/event/{eventId} | Get database/instance.event
[**database_project_instance_event_list**](DatabaseProjectInstanceApi.md#database_project_instance_event_list) | **GET** /database/{locationId}/project/{projectId}/instance/{instanceId}/event | List database/instance.event
[**database_project_instance_get**](DatabaseProjectInstanceApi.md#database_project_instance_get) | **GET** /database/{locationId}/project/{projectId}/instance/{instanceId} | Get database/instance
[**database_project_instance_list**](DatabaseProjectInstanceApi.md#database_project_instance_list) | **GET** /database/{locationId}/project/{projectId}/instance | List database/instance
[**database_project_instance_service_get**](DatabaseProjectInstanceApi.md#database_project_instance_service_get) | **GET** /database/{locationId}/project/{projectId}/instance/{instanceId}/service/{serviceId} | Get database/instance.service
[**database_project_instance_service_list**](DatabaseProjectInstanceApi.md#database_project_instance_service_list) | **GET** /database/{locationId}/project/{projectId}/instance/{instanceId}/service | List database/instance.service
[**database_project_instance_start**](DatabaseProjectInstanceApi.md#database_project_instance_start) | **POST** /database/{locationId}/project/{projectId}/instance/{instanceId}/actions/start | Start database/instance
[**database_project_instance_stop**](DatabaseProjectInstanceApi.md#database_project_instance_stop) | **POST** /database/{locationId}/project/{projectId}/instance/{instanceId}/actions/stop | Stop database/instance
[**database_project_instance_tag_create**](DatabaseProjectInstanceApi.md#database_project_instance_tag_create) | **POST** /database/{locationId}/project/{projectId}/instance/{instanceId}/tag | Create database/instance.tag
[**database_project_instance_tag_delete**](DatabaseProjectInstanceApi.md#database_project_instance_tag_delete) | **DELETE** /database/{locationId}/project/{projectId}/instance/{instanceId}/tag/{tagId} | Delete database/instance.tag
[**database_project_instance_tag_get**](DatabaseProjectInstanceApi.md#database_project_instance_tag_get) | **GET** /database/{locationId}/project/{projectId}/instance/{instanceId}/tag/{tagId} | Get database/instance.tag
[**database_project_instance_tag_list**](DatabaseProjectInstanceApi.md#database_project_instance_tag_list) | **GET** /database/{locationId}/project/{projectId}/instance/{instanceId}/tag | List database/instance.tag
[**database_project_instance_tag_put**](DatabaseProjectInstanceApi.md#database_project_instance_tag_put) | **PUT** /database/{locationId}/project/{projectId}/instance/{instanceId}/tag | Replace database/instance.tag
[**database_project_instance_transfer**](DatabaseProjectInstanceApi.md#database_project_instance_transfer) | **POST** /database/{locationId}/project/{projectId}/instance/{instanceId}/actions/transfer | Transfer database/instance
[**database_project_instance_update**](DatabaseProjectInstanceApi.md#database_project_instance_update) | **PATCH** /database/{locationId}/project/{projectId}/instance/{instanceId} | Update database/instance


# **database_project_instance_connect_get**
> ResourceConnect database_project_instance_connect_get(project_id, location_id, instance_id, connect_id)

Get database/instance.connect

Get database/instance.connect

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    connect_id = "connectId_example" # str | connectId

    # example passing only required values which don't have defaults set
    try:
        # Get database/instance.connect
        api_response = api_instance.database_project_instance_connect_get(project_id, location_id, instance_id, connect_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_connect_get: %s\n" % e)
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

# **database_project_instance_connect_list**
> [ResourceConnect] database_project_instance_connect_list(project_id, location_id, instance_id)

List database/instance.connect

List database/instance.connect

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # List database/instance.connect
        api_response = api_instance.database_project_instance_connect_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_connect_list: %s\n" % e)
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

# **database_project_instance_create**
> Database database_project_instance_create(project_id, location_id, database_project_instance_create)

Create database/instance

Create instance

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
from h1.model.database_project_instance_create import DatabaseProjectInstanceCreate
from h1.model.database import Database
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    database_project_instance_create = DatabaseProjectInstanceCreate(
        name="name_example",
        service="service_example",
        source="source_example",
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # DatabaseProjectInstanceCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create database/instance
        api_response = api_instance.database_project_instance_create(project_id, location_id, database_project_instance_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create database/instance
        api_response = api_instance.database_project_instance_create(project_id, location_id, database_project_instance_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **database_project_instance_create** | [**DatabaseProjectInstanceCreate**](DatabaseProjectInstanceCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Database**](Database.md)

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

# **database_project_instance_credential_create**
> DatabaseCredential database_project_instance_credential_create(project_id, location_id, instance_id, database_credential)

Create database/instance.credential

Create database/instance.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
from h1.model.database_credential import DatabaseCredential
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    database_credential = DatabaseCredential(
        id="id_example",
        name="name_example",
        created_by="created_by_example",
        created_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
        type="mysql",
        value="value_example",
        fingerprint="fingerprint_example",
        token="token_example",
    ) # DatabaseCredential | 

    # example passing only required values which don't have defaults set
    try:
        # Create database/instance.credential
        api_response = api_instance.database_project_instance_credential_create(project_id, location_id, instance_id, database_credential)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_credential_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |
 **database_credential** | [**DatabaseCredential**](DatabaseCredential.md)|  |

### Return type

[**DatabaseCredential**](DatabaseCredential.md)

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

# **database_project_instance_credential_delete**
> Database database_project_instance_credential_delete(project_id, location_id, instance_id, credential_id)

Delete database/instance.credential

Delete database/instance.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
from h1.model.database import Database
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Delete database/instance.credential
        api_response = api_instance.database_project_instance_credential_delete(project_id, location_id, instance_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_credential_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |
 **credential_id** | **str**| credentialId |

### Return type

[**Database**](Database.md)

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

# **database_project_instance_credential_get**
> DatabaseCredential database_project_instance_credential_get(project_id, location_id, instance_id, credential_id)

Get database/instance.credential

Get database/instance.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
from h1.model.database_credential import DatabaseCredential
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Get database/instance.credential
        api_response = api_instance.database_project_instance_credential_get(project_id, location_id, instance_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_credential_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |
 **credential_id** | **str**| credentialId |

### Return type

[**DatabaseCredential**](DatabaseCredential.md)

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

# **database_project_instance_credential_list**
> [DatabaseCredential] database_project_instance_credential_list(project_id, location_id, instance_id)

List database/instance.credential

List database/instance.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
from h1.model.database_credential import DatabaseCredential
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # List database/instance.credential
        api_response = api_instance.database_project_instance_credential_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_credential_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |

### Return type

[**[DatabaseCredential]**](DatabaseCredential.md)

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

# **database_project_instance_credential_patch**
> DatabaseCredential database_project_instance_credential_patch(project_id, location_id, instance_id, credential_id, database_project_instance_credential_patch)

Update database/instance.credential

Update database/instance.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
from h1.model.database_credential import DatabaseCredential
from h1.model.database_project_instance_credential_patch import DatabaseProjectInstanceCredentialPatch
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    credential_id = "credentialId_example" # str | credentialId
    database_project_instance_credential_patch = DatabaseProjectInstanceCredentialPatch(
        name="name_example",
    ) # DatabaseProjectInstanceCredentialPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update database/instance.credential
        api_response = api_instance.database_project_instance_credential_patch(project_id, location_id, instance_id, credential_id, database_project_instance_credential_patch)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_credential_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |
 **credential_id** | **str**| credentialId |
 **database_project_instance_credential_patch** | [**DatabaseProjectInstanceCredentialPatch**](DatabaseProjectInstanceCredentialPatch.md)|  |

### Return type

[**DatabaseCredential**](DatabaseCredential.md)

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

# **database_project_instance_delete**
> database_project_instance_delete(project_id, location_id, instance_id)

Delete database/instance

Delete instance

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # Delete database/instance
        api_instance.database_project_instance_delete(project_id, location_id, instance_id)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_delete: %s\n" % e)
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

# **database_project_instance_event_get**
> Event database_project_instance_event_get(project_id, location_id, instance_id, event_id)

Get database/instance.event

Get database/instance.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get database/instance.event
        api_response = api_instance.database_project_instance_event_get(project_id, location_id, instance_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_event_get: %s\n" % e)
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

# **database_project_instance_event_list**
> [Event] database_project_instance_event_list(project_id, location_id, instance_id)

List database/instance.event

List database/instance.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List database/instance.event
        api_response = api_instance.database_project_instance_event_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List database/instance.event
        api_response = api_instance.database_project_instance_event_list(project_id, location_id, instance_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_event_list: %s\n" % e)
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

# **database_project_instance_get**
> Database database_project_instance_get(project_id, location_id, instance_id)

Get database/instance

Returns a single instance

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
from h1.model.database import Database
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # Get database/instance
        api_response = api_instance.database_project_instance_get(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |

### Return type

[**Database**](Database.md)

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

# **database_project_instance_list**
> [Database] database_project_instance_list(project_id, location_id)

List database/instance

List instance

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
from h1.model.database import Database
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List database/instance
        api_response = api_instance.database_project_instance_list(project_id, location_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List database/instance
        api_response = api_instance.database_project_instance_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_list: %s\n" % e)
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

[**[Database]**](Database.md)

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

# **database_project_instance_service_get**
> ResourceService database_project_instance_service_get(project_id, location_id, instance_id, service_id)

Get database/instance.service

Get database/instance.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get database/instance.service
        api_response = api_instance.database_project_instance_service_get(project_id, location_id, instance_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_service_get: %s\n" % e)
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

# **database_project_instance_service_list**
> [ResourceService] database_project_instance_service_list(project_id, location_id, instance_id)

List database/instance.service

List database/instance.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # List database/instance.service
        api_response = api_instance.database_project_instance_service_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_service_list: %s\n" % e)
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

# **database_project_instance_start**
> Database database_project_instance_start(project_id, location_id, instance_id)

Start database/instance

action start

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
from h1.model.database import Database
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start database/instance
        api_response = api_instance.database_project_instance_start(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_start: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start database/instance
        api_response = api_instance.database_project_instance_start(project_id, location_id, instance_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_start: %s\n" % e)
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

[**Database**](Database.md)

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

# **database_project_instance_stop**
> Database database_project_instance_stop(project_id, location_id, instance_id)

Stop database/instance

action stop

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
from h1.model.database import Database
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Stop database/instance
        api_response = api_instance.database_project_instance_stop(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_stop: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Stop database/instance
        api_response = api_instance.database_project_instance_stop(project_id, location_id, instance_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_stop: %s\n" % e)
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

[**Database**](Database.md)

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

# **database_project_instance_tag_create**
> Tag database_project_instance_tag_create(project_id, location_id, instance_id, tag)

Create database/instance.tag

Create database/instance.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
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
        # Create database/instance.tag
        api_response = api_instance.database_project_instance_tag_create(project_id, location_id, instance_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_tag_create: %s\n" % e)
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

# **database_project_instance_tag_delete**
> database_project_instance_tag_delete(project_id, location_id, instance_id, tag_id)

Delete database/instance.tag

Delete database/instance.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete database/instance.tag
        api_instance.database_project_instance_tag_delete(project_id, location_id, instance_id, tag_id)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_tag_delete: %s\n" % e)
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

# **database_project_instance_tag_get**
> Tag database_project_instance_tag_get(project_id, location_id, instance_id, tag_id)

Get database/instance.tag

Get database/instance.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get database/instance.tag
        api_response = api_instance.database_project_instance_tag_get(project_id, location_id, instance_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_tag_get: %s\n" % e)
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

# **database_project_instance_tag_list**
> [Tag] database_project_instance_tag_list(project_id, location_id, instance_id)

List database/instance.tag

List database/instance.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id

    # example passing only required values which don't have defaults set
    try:
        # List database/instance.tag
        api_response = api_instance.database_project_instance_tag_list(project_id, location_id, instance_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_tag_list: %s\n" % e)
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

# **database_project_instance_tag_put**
> [Tag] database_project_instance_tag_put(project_id, location_id, instance_id, tag_array)

Replace database/instance.tag

Replace database/instance.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
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
        # Replace database/instance.tag
        api_response = api_instance.database_project_instance_tag_put(project_id, location_id, instance_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_tag_put: %s\n" % e)
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

# **database_project_instance_transfer**
> Database database_project_instance_transfer(project_id, location_id, instance_id, database_project_instance_transfer)

Transfer database/instance

action transfer

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
from h1.model.database import Database
from h1.model.database_project_instance_transfer import DatabaseProjectInstanceTransfer
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    database_project_instance_transfer = DatabaseProjectInstanceTransfer(
        project="project_example",
    ) # DatabaseProjectInstanceTransfer | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Transfer database/instance
        api_response = api_instance.database_project_instance_transfer(project_id, location_id, instance_id, database_project_instance_transfer)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_transfer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Transfer database/instance
        api_response = api_instance.database_project_instance_transfer(project_id, location_id, instance_id, database_project_instance_transfer, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |
 **database_project_instance_transfer** | [**DatabaseProjectInstanceTransfer**](DatabaseProjectInstanceTransfer.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Database**](Database.md)

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

# **database_project_instance_update**
> Database database_project_instance_update(project_id, location_id, instance_id, database_project_instance_update)

Update database/instance

Returns modified instance

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import database_project_instance_api
from h1.model.database import Database
from h1.model.database_project_instance_update import DatabaseProjectInstanceUpdate
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
    api_instance = database_project_instance_api.DatabaseProjectInstanceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    instance_id = "instanceId_example" # str | Instance Id
    database_project_instance_update = DatabaseProjectInstanceUpdate(
        name="name_example",
        plan="plan_example",
    ) # DatabaseProjectInstanceUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update database/instance
        api_response = api_instance.database_project_instance_update(project_id, location_id, instance_id, database_project_instance_update)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **instance_id** | **str**| Instance Id |
 **database_project_instance_update** | [**DatabaseProjectInstanceUpdate**](DatabaseProjectInstanceUpdate.md)|  |

### Return type

[**Database**](Database.md)

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

