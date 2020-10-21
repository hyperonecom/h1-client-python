# h1-client-python.IamProjectRoleApi

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
> Role iam_project_role_create(project_id, iam_project_role_create, x_idempotency_key=x_idempotency_key)

Create iam/role

Create role

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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
iam_project_role_create = h1-client-python.IamProjectRoleCreate() # IamProjectRoleCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create iam/role
        api_response = api_instance.iam_project_role_create(project_id, iam_project_role_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **iam_project_role_create** | [**IamProjectRoleCreate**](IamProjectRoleCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id

    try:
        # Delete iam/role
        api_instance.iam_project_role_delete(project_id, role_id)
    except ApiException as e:
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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get iam/role.event
        api_response = api_instance.iam_project_role_event_get(project_id, role_id, event_id)
        pprint(api_response)
    except ApiException as e:
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
> list[Event] iam_project_role_event_list(project_id, role_id, limit=limit, skip=skip)

List iam/role.event

List iam/role.event

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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List iam/role.event
        api_response = api_instance.iam_project_role_event_list(project_id, role_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **role_id** | **str**| Role Id | 
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

# **iam_project_role_get**
> Role iam_project_role_get(project_id, role_id)

Get iam/role

Returns a single role

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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id

    try:
        # Get iam/role
        api_response = api_instance.iam_project_role_get(project_id, role_id)
        pprint(api_response)
    except ApiException as e:
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
> list[Role] iam_project_role_list(project_id, name=name, tag_value=tag_value, tag_key=tag_key)

List iam/role

List role

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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
name = 'name_example' # str | Filter by name (optional)
tag_value = 'tag_value_example' # str | Filter by tag.value (optional)
tag_key = 'tag_key_example' # str | Filter by tag.key (optional)

    try:
        # List iam/role
        api_response = api_instance.iam_project_role_list(project_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except ApiException as e:
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

[**list[Role]**](Role.md)

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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id
iam_permission = h1-client-python.IamPermission() # IamPermission | 

    try:
        # Create iam/role.permission
        api_response = api_instance.iam_project_role_permission_create(project_id, role_id, iam_permission)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id
permission_id = 'permission_id_example' # str | permissionId

    try:
        # Delete iam/role.permission
        api_response = api_instance.iam_project_role_permission_delete(project_id, role_id, permission_id)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id
permission_id = 'permission_id_example' # str | permissionId

    try:
        # Get iam/role.permission
        api_response = api_instance.iam_project_role_permission_get(project_id, role_id, permission_id)
        pprint(api_response)
    except ApiException as e:
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
> list[IamPermission] iam_project_role_permission_list(project_id, role_id)

List iam/role.permission

List iam/role.permission

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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id

    try:
        # List iam/role.permission
        api_response = api_instance.iam_project_role_permission_list(project_id, role_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_permission_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **role_id** | **str**| Role Id | 

### Return type

[**list[IamPermission]**](IamPermission.md)

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
> list[IamPermission] iam_project_role_permission_put(project_id, role_id, iam_permission)

Replace iam/role.permission

Replace iam/role.permission

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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id
iam_permission = [h1-client-python.IamPermission()] # list[IamPermission] | 

    try:
        # Replace iam/role.permission
        api_response = api_instance.iam_project_role_permission_put(project_id, role_id, iam_permission)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_permission_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **role_id** | **str**| Role Id | 
 **iam_permission** | [**list[IamPermission]**](IamPermission.md)|  | 

### Return type

[**list[IamPermission]**](IamPermission.md)

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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id
service_id = 'service_id_example' # str | serviceId

    try:
        # Get iam/role.service
        api_response = api_instance.iam_project_role_service_get(project_id, role_id, service_id)
        pprint(api_response)
    except ApiException as e:
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
> list[ResourceService] iam_project_role_service_list(project_id, role_id)

List iam/role.service

List iam/role.service

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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id

    try:
        # List iam/role.service
        api_response = api_instance.iam_project_role_service_list(project_id, role_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **role_id** | **str**| Role Id | 

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

# **iam_project_role_tag_create**
> Tag iam_project_role_tag_create(project_id, role_id, tag)

Create iam/role.tag

Create iam/role.tag

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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id
tag = h1-client-python.Tag() # Tag | 

    try:
        # Create iam/role.tag
        api_response = api_instance.iam_project_role_tag_create(project_id, role_id, tag)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Delete iam/role.tag
        api_instance.iam_project_role_tag_delete(project_id, role_id, tag_id)
    except ApiException as e:
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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Get iam/role.tag
        api_response = api_instance.iam_project_role_tag_get(project_id, role_id, tag_id)
        pprint(api_response)
    except ApiException as e:
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
> list[Tag] iam_project_role_tag_list(project_id, role_id)

List iam/role.tag

List iam/role.tag

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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id

    try:
        # List iam/role.tag
        api_response = api_instance.iam_project_role_tag_list(project_id, role_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **role_id** | **str**| Role Id | 

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

# **iam_project_role_tag_put**
> list[Tag] iam_project_role_tag_put(project_id, role_id, tag)

Replace iam/role.tag

Replace iam/role.tag

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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id
tag = [h1-client-python.Tag()] # list[Tag] | 

    try:
        # Replace iam/role.tag
        api_response = api_instance.iam_project_role_tag_put(project_id, role_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectRoleApi->iam_project_role_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **role_id** | **str**| Role Id | 
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

# **iam_project_role_update**
> Role iam_project_role_update(project_id, role_id, iam_project_role_update)

Update iam/role

Returns modified role

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
    api_instance = h1-client-python.IamProjectRoleApi(api_client)
    project_id = 'project_id_example' # str | Project Id
role_id = 'role_id_example' # str | Role Id
iam_project_role_update = h1-client-python.IamProjectRoleUpdate() # IamProjectRoleUpdate | 

    try:
        # Update iam/role
        api_response = api_instance.iam_project_role_update(project_id, role_id, iam_project_role_update)
        pprint(api_response)
    except ApiException as e:
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

