# h1.IamOrganisationRoleApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iam_organisation_role_create**](IamOrganisationRoleApi.md#iam_organisation_role_create) | **POST** /iam/organisation/{organisationId}/role | Create iam/role
[**iam_organisation_role_delete**](IamOrganisationRoleApi.md#iam_organisation_role_delete) | **DELETE** /iam/organisation/{organisationId}/role/{roleId} | Delete iam/role
[**iam_organisation_role_event_get**](IamOrganisationRoleApi.md#iam_organisation_role_event_get) | **GET** /iam/organisation/{organisationId}/role/{roleId}/event/{eventId} | Get iam/role.event
[**iam_organisation_role_event_list**](IamOrganisationRoleApi.md#iam_organisation_role_event_list) | **GET** /iam/organisation/{organisationId}/role/{roleId}/event | List iam/role.event
[**iam_organisation_role_get**](IamOrganisationRoleApi.md#iam_organisation_role_get) | **GET** /iam/organisation/{organisationId}/role/{roleId} | Get iam/role
[**iam_organisation_role_list**](IamOrganisationRoleApi.md#iam_organisation_role_list) | **GET** /iam/organisation/{organisationId}/role | List iam/role
[**iam_organisation_role_permission_create**](IamOrganisationRoleApi.md#iam_organisation_role_permission_create) | **POST** /iam/organisation/{organisationId}/role/{roleId}/permission | Create iam/role.permission
[**iam_organisation_role_permission_delete**](IamOrganisationRoleApi.md#iam_organisation_role_permission_delete) | **DELETE** /iam/organisation/{organisationId}/role/{roleId}/permission/{permissionId} | Delete iam/role.permission
[**iam_organisation_role_permission_get**](IamOrganisationRoleApi.md#iam_organisation_role_permission_get) | **GET** /iam/organisation/{organisationId}/role/{roleId}/permission/{permissionId} | Get iam/role.permission
[**iam_organisation_role_permission_list**](IamOrganisationRoleApi.md#iam_organisation_role_permission_list) | **GET** /iam/organisation/{organisationId}/role/{roleId}/permission | List iam/role.permission
[**iam_organisation_role_permission_put**](IamOrganisationRoleApi.md#iam_organisation_role_permission_put) | **PUT** /iam/organisation/{organisationId}/role/{roleId}/permission | Replace iam/role.permission
[**iam_organisation_role_service_get**](IamOrganisationRoleApi.md#iam_organisation_role_service_get) | **GET** /iam/organisation/{organisationId}/role/{roleId}/service/{serviceId} | Get iam/role.service
[**iam_organisation_role_service_list**](IamOrganisationRoleApi.md#iam_organisation_role_service_list) | **GET** /iam/organisation/{organisationId}/role/{roleId}/service | List iam/role.service
[**iam_organisation_role_tag_create**](IamOrganisationRoleApi.md#iam_organisation_role_tag_create) | **POST** /iam/organisation/{organisationId}/role/{roleId}/tag | Create iam/role.tag
[**iam_organisation_role_tag_delete**](IamOrganisationRoleApi.md#iam_organisation_role_tag_delete) | **DELETE** /iam/organisation/{organisationId}/role/{roleId}/tag/{tagId} | Delete iam/role.tag
[**iam_organisation_role_tag_get**](IamOrganisationRoleApi.md#iam_organisation_role_tag_get) | **GET** /iam/organisation/{organisationId}/role/{roleId}/tag/{tagId} | Get iam/role.tag
[**iam_organisation_role_tag_list**](IamOrganisationRoleApi.md#iam_organisation_role_tag_list) | **GET** /iam/organisation/{organisationId}/role/{roleId}/tag | List iam/role.tag
[**iam_organisation_role_tag_put**](IamOrganisationRoleApi.md#iam_organisation_role_tag_put) | **PUT** /iam/organisation/{organisationId}/role/{roleId}/tag | Replace iam/role.tag
[**iam_organisation_role_update**](IamOrganisationRoleApi.md#iam_organisation_role_update) | **PATCH** /iam/organisation/{organisationId}/role/{roleId} | Update iam/role


# **iam_organisation_role_create**
> Role iam_organisation_role_create(organisation_id, iam_project_role_create)

Create iam/role

Create role

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
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
        api_response = api_instance.iam_organisation_role_create(organisation_id, iam_project_role_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create iam/role
        api_response = api_instance.iam_organisation_role_create(organisation_id, iam_project_role_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_delete**
> iam_organisation_role_delete(organisation_id, role_id)

Delete iam/role

Delete role

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    role_id = "roleId_example" # str | Role Id

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/role
        api_instance.iam_organisation_role_delete(organisation_id, role_id)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_event_get**
> Event iam_organisation_role_event_get(organisation_id, role_id, event_id)

Get iam/role.event

Get iam/role.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    role_id = "roleId_example" # str | Role Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/role.event
        api_response = api_instance.iam_organisation_role_event_get(organisation_id, role_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_event_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_event_list**
> [Event] iam_organisation_role_event_list(organisation_id, role_id)

List iam/role.event

List iam/role.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    role_id = "roleId_example" # str | Role Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List iam/role.event
        api_response = api_instance.iam_organisation_role_event_list(organisation_id, role_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/role.event
        api_response = api_instance.iam_organisation_role_event_list(organisation_id, role_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_get**
> Role iam_organisation_role_get(organisation_id, role_id)

Get iam/role

Returns a single role

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    role_id = "roleId_example" # str | Role Id

    # example passing only required values which don't have defaults set
    try:
        # Get iam/role
        api_response = api_instance.iam_organisation_role_get(organisation_id, role_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_list**
> [Role] iam_organisation_role_list(organisation_id)

List iam/role

List role

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List iam/role
        api_response = api_instance.iam_organisation_role_list(organisation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/role
        api_response = api_instance.iam_organisation_role_list(organisation_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_permission_create**
> IamPermission iam_organisation_role_permission_create(organisation_id, role_id, iam_permission)

Create iam/role.permission

Create iam/role.permission

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    role_id = "roleId_example" # str | Role Id
    iam_permission = IamPermission(
        id="id_example",
        value="value_example",
    ) # IamPermission | 

    # example passing only required values which don't have defaults set
    try:
        # Create iam/role.permission
        api_response = api_instance.iam_organisation_role_permission_create(organisation_id, role_id, iam_permission)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_permission_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_permission_delete**
> IamPermission iam_organisation_role_permission_delete(organisation_id, role_id, permission_id)

Delete iam/role.permission

Delete iam/role.permission

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    role_id = "roleId_example" # str | Role Id
    permission_id = "permissionId_example" # str | permissionId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/role.permission
        api_response = api_instance.iam_organisation_role_permission_delete(organisation_id, role_id, permission_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_permission_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_permission_get**
> IamPermission iam_organisation_role_permission_get(organisation_id, role_id, permission_id)

Get iam/role.permission

Get iam/role.permission

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    role_id = "roleId_example" # str | Role Id
    permission_id = "permissionId_example" # str | permissionId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/role.permission
        api_response = api_instance.iam_organisation_role_permission_get(organisation_id, role_id, permission_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_permission_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_permission_list**
> [IamPermission] iam_organisation_role_permission_list(organisation_id, role_id)

List iam/role.permission

List iam/role.permission

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    role_id = "roleId_example" # str | Role Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/role.permission
        api_response = api_instance.iam_organisation_role_permission_list(organisation_id, role_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_permission_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_permission_put**
> [IamPermission] iam_organisation_role_permission_put(organisation_id, role_id, iam_permission_array)

Replace iam/role.permission

Replace iam/role.permission

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
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
        api_response = api_instance.iam_organisation_role_permission_put(organisation_id, role_id, iam_permission_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_permission_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_service_get**
> ResourceService iam_organisation_role_service_get(organisation_id, role_id, service_id)

Get iam/role.service

Get iam/role.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    role_id = "roleId_example" # str | Role Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/role.service
        api_response = api_instance.iam_organisation_role_service_get(organisation_id, role_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_service_list**
> [ResourceService] iam_organisation_role_service_list(organisation_id, role_id)

List iam/role.service

List iam/role.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    role_id = "roleId_example" # str | Role Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/role.service
        api_response = api_instance.iam_organisation_role_service_list(organisation_id, role_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_tag_create**
> Tag iam_organisation_role_tag_create(organisation_id, role_id, tag)

Create iam/role.tag

Create iam/role.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    role_id = "roleId_example" # str | Role Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create iam/role.tag
        api_response = api_instance.iam_organisation_role_tag_create(organisation_id, role_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_tag_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_tag_delete**
> iam_organisation_role_tag_delete(organisation_id, role_id, tag_id)

Delete iam/role.tag

Delete iam/role.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    role_id = "roleId_example" # str | Role Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/role.tag
        api_instance.iam_organisation_role_tag_delete(organisation_id, role_id, tag_id)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_tag_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_tag_get**
> Tag iam_organisation_role_tag_get(organisation_id, role_id, tag_id)

Get iam/role.tag

Get iam/role.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    role_id = "roleId_example" # str | Role Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/role.tag
        api_response = api_instance.iam_organisation_role_tag_get(organisation_id, role_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_tag_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_tag_list**
> [Tag] iam_organisation_role_tag_list(organisation_id, role_id)

List iam/role.tag

List iam/role.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    role_id = "roleId_example" # str | Role Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/role.tag
        api_response = api_instance.iam_organisation_role_tag_list(organisation_id, role_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_tag_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_tag_put**
> [Tag] iam_organisation_role_tag_put(organisation_id, role_id, tag_array)

Replace iam/role.tag

Replace iam/role.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
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
        api_response = api_instance.iam_organisation_role_tag_put(organisation_id, role_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_tag_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_role_update**
> Role iam_organisation_role_update(organisation_id, role_id, iam_project_role_update)

Update iam/role

Returns modified role

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_role_api
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
    api_instance = iam_organisation_role_api.IamOrganisationRoleApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    role_id = "roleId_example" # str | Role Id
    iam_project_role_update = IamProjectRoleUpdate(
        name="name_example",
        description="description_example",
    ) # IamProjectRoleUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update iam/role
        api_response = api_instance.iam_organisation_role_update(organisation_id, role_id, iam_project_role_update)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationRoleApi->iam_organisation_role_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

