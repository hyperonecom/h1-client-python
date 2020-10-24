# h1.DatabaseProjectInstanceApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
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


# **database_project_instance_create**
> Database database_project_instance_create(project_id, location_id, database_project_instance_create, x_idempotency_key=x_idempotency_key)

Create database/instance

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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
database_project_instance_create = h1.DatabaseProjectInstanceCreate() # DatabaseProjectInstanceCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create database/instance
        api_response = api_instance.database_project_instance_create(project_id, location_id, database_project_instance_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **database_project_instance_create** | [**DatabaseProjectInstanceCreate**](DatabaseProjectInstanceCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
database_credential = h1.DatabaseCredential() # DatabaseCredential | 

    try:
        # Create database/instance.credential
        api_response = api_instance.database_project_instance_credential_create(project_id, location_id, instance_id, database_credential)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
credential_id = 'credential_id_example' # str | credentialId

    try:
        # Delete database/instance.credential
        api_response = api_instance.database_project_instance_credential_delete(project_id, location_id, instance_id, credential_id)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
credential_id = 'credential_id_example' # str | credentialId

    try:
        # Get database/instance.credential
        api_response = api_instance.database_project_instance_credential_get(project_id, location_id, instance_id, credential_id)
        pprint(api_response)
    except ApiException as e:
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
> list[DatabaseCredential] database_project_instance_credential_list(project_id, location_id, instance_id)

List database/instance.credential

List database/instance.credential

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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List database/instance.credential
        api_response = api_instance.database_project_instance_credential_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_credential_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 

### Return type

[**list[DatabaseCredential]**](DatabaseCredential.md)

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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
credential_id = 'credential_id_example' # str | credentialId
database_project_instance_credential_patch = h1.DatabaseProjectInstanceCredentialPatch() # DatabaseProjectInstanceCredentialPatch | 

    try:
        # Update database/instance.credential
        api_response = api_instance.database_project_instance_credential_patch(project_id, location_id, instance_id, credential_id, database_project_instance_credential_patch)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # Delete database/instance
        api_instance.database_project_instance_delete(project_id, location_id, instance_id)
    except ApiException as e:
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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get database/instance.event
        api_response = api_instance.database_project_instance_event_get(project_id, location_id, instance_id, event_id)
        pprint(api_response)
    except ApiException as e:
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
> list[Event] database_project_instance_event_list(project_id, location_id, instance_id, limit=limit, skip=skip)

List database/instance.event

List database/instance.event

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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List database/instance.event
        api_response = api_instance.database_project_instance_event_list(project_id, location_id, instance_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_event_list: %s\n" % e)
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

# **database_project_instance_get**
> Database database_project_instance_get(project_id, location_id, instance_id)

Get database/instance

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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # Get database/instance
        api_response = api_instance.database_project_instance_get(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
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
> list[Database] database_project_instance_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)

List database/instance

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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
name = 'name_example' # str | Filter by name (optional)
tag_value = 'tag_value_example' # str | Filter by tag.value (optional)
tag_key = 'tag_key_example' # str | Filter by tag.key (optional)

    try:
        # List database/instance
        api_response = api_instance.database_project_instance_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except ApiException as e:
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

[**list[Database]**](Database.md)

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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
service_id = 'service_id_example' # str | serviceId

    try:
        # Get database/instance.service
        api_response = api_instance.database_project_instance_service_get(project_id, location_id, instance_id, service_id)
        pprint(api_response)
    except ApiException as e:
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
> list[ResourceService] database_project_instance_service_list(project_id, location_id, instance_id)

List database/instance.service

List database/instance.service

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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List database/instance.service
        api_response = api_instance.database_project_instance_service_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_service_list: %s\n" % e)
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

# **database_project_instance_start**
> Database database_project_instance_start(project_id, location_id, instance_id, x_idempotency_key=x_idempotency_key)

Start database/instance

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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Start database/instance
        api_response = api_instance.database_project_instance_start(project_id, location_id, instance_id, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

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
> Database database_project_instance_stop(project_id, location_id, instance_id, x_idempotency_key=x_idempotency_key)

Stop database/instance

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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Stop database/instance
        api_response = api_instance.database_project_instance_stop(project_id, location_id, instance_id, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **instance_id** | **str**| Instance Id | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
tag = h1.Tag() # Tag | 

    try:
        # Create database/instance.tag
        api_response = api_instance.database_project_instance_tag_create(project_id, location_id, instance_id, tag)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Delete database/instance.tag
        api_instance.database_project_instance_tag_delete(project_id, location_id, instance_id, tag_id)
    except ApiException as e:
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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Get database/instance.tag
        api_response = api_instance.database_project_instance_tag_get(project_id, location_id, instance_id, tag_id)
        pprint(api_response)
    except ApiException as e:
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
> list[Tag] database_project_instance_tag_list(project_id, location_id, instance_id)

List database/instance.tag

List database/instance.tag

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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id

    try:
        # List database/instance.tag
        api_response = api_instance.database_project_instance_tag_list(project_id, location_id, instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_tag_list: %s\n" % e)
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

# **database_project_instance_tag_put**
> list[Tag] database_project_instance_tag_put(project_id, location_id, instance_id, tag)

Replace database/instance.tag

Replace database/instance.tag

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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
tag = [h1.Tag()] # list[Tag] | 

    try:
        # Replace database/instance.tag
        api_response = api_instance.database_project_instance_tag_put(project_id, location_id, instance_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DatabaseProjectInstanceApi->database_project_instance_tag_put: %s\n" % e)
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

# **database_project_instance_transfer**
> Database database_project_instance_transfer(project_id, location_id, instance_id, database_project_instance_transfer, x_idempotency_key=x_idempotency_key)

Transfer database/instance

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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
database_project_instance_transfer = h1.DatabaseProjectInstanceTransfer() # DatabaseProjectInstanceTransfer | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Transfer database/instance
        api_response = api_instance.database_project_instance_transfer(project_id, location_id, instance_id, database_project_instance_transfer, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = h1.DatabaseProjectInstanceApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
instance_id = 'instance_id_example' # str | Instance Id
database_project_instance_update = h1.DatabaseProjectInstanceUpdate() # DatabaseProjectInstanceUpdate | 

    try:
        # Update database/instance
        api_response = api_instance.database_project_instance_update(project_id, location_id, instance_id, database_project_instance_update)
        pprint(api_response)
    except ApiException as e:
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

