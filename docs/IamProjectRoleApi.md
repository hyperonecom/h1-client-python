# h1.IamProjectRoleApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iam_project_role_create**](IamProjectRoleApi.md#iam_project_role_create) | **POST** /iam/project/{projectId}/role | Create iam/role
[**iam_project_role_delete**](IamProjectRoleApi.md#iam_project_role_delete) | **DELETE** /iam/project/{projectId}/role/{roleId} | Delete iam/role
[**iam_project_role_event_get**](IamProjectRoleApi.md#iam_project_role_event_get) | **GET** /iam/project/{projectId}/role/{roleId}/event/{eventId} | Get iam/role.event
[**iam_project_role_event_list**](IamProjectRoleApi.md#iam_project_role_event_list) | **GET** /iam/project/{projectId}/role/{roleId}/event | List iam/role.event
[**iam_project_role_get**](IamProjectRoleApi.md#iam_project_role_get) | **GET** /iam/project/{projectId}/role/{roleId} | Get iam/role
[**iam_project_role_list**](IamProjectRoleApi.md#iam_project_role_list) | **GET** /iam/project/{projectId}/role | List iam/role
[**iam_project_role_permission_create**](IamProjectRoleApi.md#iam_project_role_permission_create) | **POST** /iam/project/{projectId}/role/{roleId}/permission | Create iam/role.permission
[**iam_project_role_permission_delete**](IamProjectRoleApi.md#iam_project_role_permission_delete) | **DELETE** /iam/project/{projectId}/role/{roleId}/permission/{permissionId} | Delete iam/role.permission
[**iam_project_role_permission_get**](IamProjectRoleApi.md#iam_project_role_permission_get) | **GET** /iam/project/{projectId}/role/{roleId}/permission/{permissionId} | Get iam/role.permission
[**iam_project_role_permission_list**](IamProjectRoleApi.md#iam_project_role_permission_list) | **GET** /iam/project/{projectId}/role/{roleId}/permission | List iam/role.permission
[**iam_project_role_permission_put**](IamProjectRoleApi.md#iam_project_role_permission_put) | **PUT** /iam/project/{projectId}/role/{roleId}/permission | Replace iam/role.permission
[**iam_project_role_service_get**](IamProjectRoleApi.md#iam_project_role_service_get) | **GET** /iam/project/{projectId}/role/{roleId}/service/{serviceId} | Get iam/role.service
[**iam_project_role_service_list**](IamProjectRoleApi.md#iam_project_role_service_list) | **GET** /iam/project/{projectId}/role/{roleId}/service | List iam/role.service
[**iam_project_role_tag_create**](IamProjectRoleApi.md#iam_project_role_tag_create) | **POST** /iam/project/{projectId}/role/{roleId}/tag | Create iam/role.tag
[**iam_project_role_tag_delete**](IamProjectRoleApi.md#iam_project_role_tag_delete) | **DELETE** /iam/project/{projectId}/role/{roleId}/tag/{tagId} | Delete iam/role.tag
[**iam_project_role_tag_get**](IamProjectRoleApi.md#iam_project_role_tag_get) | **GET** /iam/project/{projectId}/role/{roleId}/tag/{tagId} | Get iam/role.tag
[**iam_project_role_tag_list**](IamProjectRoleApi.md#iam_project_role_tag_list) | **GET** /iam/project/{projectId}/role/{roleId}/tag | List iam/role.tag
[**iam_project_role_tag_put**](IamProjectRoleApi.md#iam_project_role_tag_put) | **PUT** /iam/project/{projectId}/role/{roleId}/tag | Replace iam/role.tag
[**iam_project_role_update**](IamProjectRoleApi.md#iam_project_role_update) | **PATCH** /iam/project/{projectId}/role/{roleId} | Update iam/role


# **iam_project_role_create**
> Role iam_project_role_create(project_id, iam_project_role_create)

Create iam/role

Create role

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
from h1.model.iam_project_role_create import IamProjectRoleCreate
from h1.model.role import Role
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    iam_project_role_create = IamProjectRoleCreate(
        name="name_example",
        service="5e679c282b39c4353cd86f34",
        description="description_example",
        permission=IamPermissionArray([
            IamPermission(
                id="id_example",
                value="value_example",
            ),
        ]),
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # IamProjectRoleCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create iam/role
        api_response = api_instance.iam_project_role_create(project_id, iam_project_role_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create iam/role
        api_response = api_instance.iam_project_role_create(project_id, iam_project_role_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **iam_project_role_create** | [**IamProjectRoleCreate**](IamProjectRoleCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Role**](Role.md)

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

# **iam_project_role_delete**
> iam_project_role_delete(project_id, role_id)

Delete iam/role

Delete role

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/role
        api_instance.iam_project_role_delete(project_id, role_id)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |

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

# **iam_project_role_event_get**
> Event iam_project_role_event_get(project_id, role_id, event_id)

Get iam/role.event

Get iam/role.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/role.event
        api_response = api_instance.iam_project_role_event_get(project_id, role_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_event_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |
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

# **iam_project_role_event_list**
> [Event] iam_project_role_event_list(project_id, role_id)

List iam/role.event

List iam/role.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List iam/role.event
        api_response = api_instance.iam_project_role_event_list(project_id, role_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/role.event
        api_response = api_instance.iam_project_role_event_list(project_id, role_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |
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

# **iam_project_role_get**
> Role iam_project_role_get(project_id, role_id)

Get iam/role

Returns a single role

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
from h1.model.role import Role
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id

    # example passing only required values which don't have defaults set
    try:
        # Get iam/role
        api_response = api_instance.iam_project_role_get(project_id, role_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |

### Return type

[**Role**](Role.md)

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

# **iam_project_role_list**
> [Role] iam_project_role_list(project_id)

List iam/role

List role

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
from h1.model.role import Role
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List iam/role
        api_response = api_instance.iam_project_role_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/role
        api_response = api_instance.iam_project_role_list(project_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **name** | **str**| Filter by name | [optional]
 **tag_value** | **str**| Filter by tag.value | [optional]
 **tag_key** | **str**| Filter by tag.key | [optional]

### Return type

[**[Role]**](Role.md)

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

# **iam_project_role_permission_create**
> IamPermission iam_project_role_permission_create(project_id, role_id, iam_permission)

Create iam/role.permission

Create iam/role.permission

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
from h1.model.iam_permission import IamPermission
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id
    iam_permission = IamPermission(
        id="id_example",
        value="value_example",
    ) # IamPermission | 

    # example passing only required values which don't have defaults set
    try:
        # Create iam/role.permission
        api_response = api_instance.iam_project_role_permission_create(project_id, role_id, iam_permission)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_permission_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |
 **iam_permission** | [**IamPermission**](IamPermission.md)|  |

### Return type

[**IamPermission**](IamPermission.md)

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

# **iam_project_role_permission_delete**
> IamPermission iam_project_role_permission_delete(project_id, role_id, permission_id)

Delete iam/role.permission

Delete iam/role.permission

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
from h1.model.iam_permission import IamPermission
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id
    permission_id = "permissionId_example" # str | permissionId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/role.permission
        api_response = api_instance.iam_project_role_permission_delete(project_id, role_id, permission_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_permission_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |
 **permission_id** | **str**| permissionId |

### Return type

[**IamPermission**](IamPermission.md)

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

# **iam_project_role_permission_get**
> IamPermission iam_project_role_permission_get(project_id, role_id, permission_id)

Get iam/role.permission

Get iam/role.permission

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
from h1.model.iam_permission import IamPermission
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id
    permission_id = "permissionId_example" # str | permissionId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/role.permission
        api_response = api_instance.iam_project_role_permission_get(project_id, role_id, permission_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_permission_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |
 **permission_id** | **str**| permissionId |

### Return type

[**IamPermission**](IamPermission.md)

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

# **iam_project_role_permission_list**
> [IamPermission] iam_project_role_permission_list(project_id, role_id)

List iam/role.permission

List iam/role.permission

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
from h1.model.iam_permission import IamPermission
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/role.permission
        api_response = api_instance.iam_project_role_permission_list(project_id, role_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_permission_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |

### Return type

[**[IamPermission]**](IamPermission.md)

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

# **iam_project_role_permission_put**
> [IamPermission] iam_project_role_permission_put(project_id, role_id, iam_permission_array)

Replace iam/role.permission

Replace iam/role.permission

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
from h1.model.iam_permission import IamPermission
from h1.model.iam_permission_array import IamPermissionArray
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id
    iam_permission_array = IamPermissionArray([
        IamPermission(
            id="id_example",
            value="value_example",
        ),
    ]) # IamPermissionArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace iam/role.permission
        api_response = api_instance.iam_project_role_permission_put(project_id, role_id, iam_permission_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_permission_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |
 **iam_permission_array** | [**IamPermissionArray**](IamPermissionArray.md)|  |

### Return type

[**[IamPermission]**](IamPermission.md)

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

# **iam_project_role_service_get**
> ResourceService iam_project_role_service_get(project_id, role_id, service_id)

Get iam/role.service

Get iam/role.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/role.service
        api_response = api_instance.iam_project_role_service_get(project_id, role_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |
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

# **iam_project_role_service_list**
> [ResourceService] iam_project_role_service_list(project_id, role_id)

List iam/role.service

List iam/role.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/role.service
        api_response = api_instance.iam_project_role_service_list(project_id, role_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |

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

# **iam_project_role_tag_create**
> Tag iam_project_role_tag_create(project_id, role_id, tag)

Create iam/role.tag

Create iam/role.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create iam/role.tag
        api_response = api_instance.iam_project_role_tag_create(project_id, role_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_tag_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |
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

# **iam_project_role_tag_delete**
> iam_project_role_tag_delete(project_id, role_id, tag_id)

Delete iam/role.tag

Delete iam/role.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/role.tag
        api_instance.iam_project_role_tag_delete(project_id, role_id, tag_id)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_tag_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |
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

# **iam_project_role_tag_get**
> Tag iam_project_role_tag_get(project_id, role_id, tag_id)

Get iam/role.tag

Get iam/role.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/role.tag
        api_response = api_instance.iam_project_role_tag_get(project_id, role_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_tag_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |
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

# **iam_project_role_tag_list**
> [Tag] iam_project_role_tag_list(project_id, role_id)

List iam/role.tag

List iam/role.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/role.tag
        api_response = api_instance.iam_project_role_tag_list(project_id, role_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_tag_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |

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

# **iam_project_role_tag_put**
> [Tag] iam_project_role_tag_put(project_id, role_id, tag_array)

Replace iam/role.tag

Replace iam/role.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace iam/role.tag
        api_response = api_instance.iam_project_role_tag_put(project_id, role_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_tag_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |
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

# **iam_project_role_update**
> Role iam_project_role_update(project_id, role_id, iam_project_role_update)

Update iam/role

Returns modified role

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_role_api
from h1.model.iam_project_role_update import IamProjectRoleUpdate
from h1.model.role import Role
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
    api_instance = iam_project_role_api.IamProjectRoleApi(api_client)
    project_id = "projectId_example" # str | Project Id
    role_id = "roleId_example" # str | Role Id
    iam_project_role_update = IamProjectRoleUpdate(
        name="name_example",
        description="description_example",
    ) # IamProjectRoleUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update iam/role
        api_response = api_instance.iam_project_role_update(project_id, role_id, iam_project_role_update)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **role_id** | **str**| Role Id |
 **iam_project_role_update** | [**IamProjectRoleUpdate**](IamProjectRoleUpdate.md)|  |

### Return type

[**Role**](Role.md)

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

