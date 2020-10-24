# h1.IamProjectPolicyApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iam_project_policy_actor_create**](IamProjectPolicyApi.md#iam_project_policy_actor_create) | **POST** /iam/project/{projectId}/policy/{policyId}/actor | Create iam/policy.actor
[**iam_project_policy_actor_delete**](IamProjectPolicyApi.md#iam_project_policy_actor_delete) | **DELETE** /iam/project/{projectId}/policy/{policyId}/actor/{actorId} | Delete iam/policy.actor
[**iam_project_policy_actor_get**](IamProjectPolicyApi.md#iam_project_policy_actor_get) | **GET** /iam/project/{projectId}/policy/{policyId}/actor/{actorId} | Get iam/policy.actor
[**iam_project_policy_actor_list**](IamProjectPolicyApi.md#iam_project_policy_actor_list) | **GET** /iam/project/{projectId}/policy/{policyId}/actor | List iam/policy.actor
[**iam_project_policy_create**](IamProjectPolicyApi.md#iam_project_policy_create) | **POST** /iam/project/{projectId}/policy | Create iam/policy
[**iam_project_policy_delete**](IamProjectPolicyApi.md#iam_project_policy_delete) | **DELETE** /iam/project/{projectId}/policy/{policyId} | Delete iam/policy
[**iam_project_policy_event_get**](IamProjectPolicyApi.md#iam_project_policy_event_get) | **GET** /iam/project/{projectId}/policy/{policyId}/event/{eventId} | Get iam/policy.event
[**iam_project_policy_event_list**](IamProjectPolicyApi.md#iam_project_policy_event_list) | **GET** /iam/project/{projectId}/policy/{policyId}/event | List iam/policy.event
[**iam_project_policy_get**](IamProjectPolicyApi.md#iam_project_policy_get) | **GET** /iam/project/{projectId}/policy/{policyId} | Get iam/policy
[**iam_project_policy_list**](IamProjectPolicyApi.md#iam_project_policy_list) | **GET** /iam/project/{projectId}/policy | List iam/policy
[**iam_project_policy_service_get**](IamProjectPolicyApi.md#iam_project_policy_service_get) | **GET** /iam/project/{projectId}/policy/{policyId}/service/{serviceId} | Get iam/policy.service
[**iam_project_policy_service_list**](IamProjectPolicyApi.md#iam_project_policy_service_list) | **GET** /iam/project/{projectId}/policy/{policyId}/service | List iam/policy.service
[**iam_project_policy_tag_create**](IamProjectPolicyApi.md#iam_project_policy_tag_create) | **POST** /iam/project/{projectId}/policy/{policyId}/tag | Create iam/policy.tag
[**iam_project_policy_tag_delete**](IamProjectPolicyApi.md#iam_project_policy_tag_delete) | **DELETE** /iam/project/{projectId}/policy/{policyId}/tag/{tagId} | Delete iam/policy.tag
[**iam_project_policy_tag_get**](IamProjectPolicyApi.md#iam_project_policy_tag_get) | **GET** /iam/project/{projectId}/policy/{policyId}/tag/{tagId} | Get iam/policy.tag
[**iam_project_policy_tag_list**](IamProjectPolicyApi.md#iam_project_policy_tag_list) | **GET** /iam/project/{projectId}/policy/{policyId}/tag | List iam/policy.tag
[**iam_project_policy_tag_put**](IamProjectPolicyApi.md#iam_project_policy_tag_put) | **PUT** /iam/project/{projectId}/policy/{policyId}/tag | Replace iam/policy.tag
[**iam_project_policy_update**](IamProjectPolicyApi.md#iam_project_policy_update) | **PATCH** /iam/project/{projectId}/policy/{policyId} | Update iam/policy


# **iam_project_policy_actor_create**
> IamActor iam_project_policy_actor_create(project_id, policy_id, iam_actor)

Create iam/policy.actor

Create iam/policy.actor

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id
iam_actor = h1.IamActor() # IamActor | 

    try:
        # Create iam/policy.actor
        api_response = api_instance.iam_project_policy_actor_create(project_id, policy_id, iam_actor)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_actor_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 
 **iam_actor** | [**IamActor**](IamActor.md)|  | 

### Return type

[**IamActor**](IamActor.md)

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

# **iam_project_policy_actor_delete**
> IamActor iam_project_policy_actor_delete(project_id, policy_id, actor_id)

Delete iam/policy.actor

Delete iam/policy.actor

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id
actor_id = 'actor_id_example' # str | actorId

    try:
        # Delete iam/policy.actor
        api_response = api_instance.iam_project_policy_actor_delete(project_id, policy_id, actor_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_actor_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 
 **actor_id** | **str**| actorId | 

### Return type

[**IamActor**](IamActor.md)

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

# **iam_project_policy_actor_get**
> IamActor iam_project_policy_actor_get(project_id, policy_id, actor_id)

Get iam/policy.actor

Get iam/policy.actor

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id
actor_id = 'actor_id_example' # str | actorId

    try:
        # Get iam/policy.actor
        api_response = api_instance.iam_project_policy_actor_get(project_id, policy_id, actor_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_actor_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 
 **actor_id** | **str**| actorId | 

### Return type

[**IamActor**](IamActor.md)

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

# **iam_project_policy_actor_list**
> list[IamActor] iam_project_policy_actor_list(project_id, policy_id)

List iam/policy.actor

List iam/policy.actor

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id

    try:
        # List iam/policy.actor
        api_response = api_instance.iam_project_policy_actor_list(project_id, policy_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_actor_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 

### Return type

[**list[IamActor]**](IamActor.md)

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

# **iam_project_policy_create**
> Policy iam_project_policy_create(project_id, iam_project_policy_create, x_idempotency_key=x_idempotency_key)

Create iam/policy

Create policy

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
iam_project_policy_create = h1.IamProjectPolicyCreate() # IamProjectPolicyCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create iam/policy
        api_response = api_instance.iam_project_policy_create(project_id, iam_project_policy_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **iam_project_policy_create** | [**IamProjectPolicyCreate**](IamProjectPolicyCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Policy**](Policy.md)

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

# **iam_project_policy_delete**
> iam_project_policy_delete(project_id, policy_id)

Delete iam/policy

Delete policy

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id

    try:
        # Delete iam/policy
        api_instance.iam_project_policy_delete(project_id, policy_id)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 

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

# **iam_project_policy_event_get**
> Event iam_project_policy_event_get(project_id, policy_id, event_id)

Get iam/policy.event

Get iam/policy.event

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get iam/policy.event
        api_response = api_instance.iam_project_policy_event_get(project_id, policy_id, event_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 
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

# **iam_project_policy_event_list**
> list[Event] iam_project_policy_event_list(project_id, policy_id, limit=limit, skip=skip)

List iam/policy.event

List iam/policy.event

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List iam/policy.event
        api_response = api_instance.iam_project_policy_event_list(project_id, policy_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 
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

# **iam_project_policy_get**
> Policy iam_project_policy_get(project_id, policy_id)

Get iam/policy

Returns a single policy

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id

    try:
        # Get iam/policy
        api_response = api_instance.iam_project_policy_get(project_id, policy_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 

### Return type

[**Policy**](Policy.md)

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

# **iam_project_policy_list**
> list[Policy] iam_project_policy_list(project_id, name=name, tag_value=tag_value, tag_key=tag_key)

List iam/policy

List policy

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
name = 'name_example' # str | Filter by name (optional)
tag_value = 'tag_value_example' # str | Filter by tag.value (optional)
tag_key = 'tag_key_example' # str | Filter by tag.key (optional)

    try:
        # List iam/policy
        api_response = api_instance.iam_project_policy_list(project_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **name** | **str**| Filter by name | [optional] 
 **tag_value** | **str**| Filter by tag.value | [optional] 
 **tag_key** | **str**| Filter by tag.key | [optional] 

### Return type

[**list[Policy]**](Policy.md)

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

# **iam_project_policy_service_get**
> ResourceService iam_project_policy_service_get(project_id, policy_id, service_id)

Get iam/policy.service

Get iam/policy.service

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id
service_id = 'service_id_example' # str | serviceId

    try:
        # Get iam/policy.service
        api_response = api_instance.iam_project_policy_service_get(project_id, policy_id, service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 
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

# **iam_project_policy_service_list**
> list[ResourceService] iam_project_policy_service_list(project_id, policy_id)

List iam/policy.service

List iam/policy.service

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id

    try:
        # List iam/policy.service
        api_response = api_instance.iam_project_policy_service_list(project_id, policy_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 

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

# **iam_project_policy_tag_create**
> Tag iam_project_policy_tag_create(project_id, policy_id, tag)

Create iam/policy.tag

Create iam/policy.tag

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id
tag = h1.Tag() # Tag | 

    try:
        # Create iam/policy.tag
        api_response = api_instance.iam_project_policy_tag_create(project_id, policy_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 
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

# **iam_project_policy_tag_delete**
> iam_project_policy_tag_delete(project_id, policy_id, tag_id)

Delete iam/policy.tag

Delete iam/policy.tag

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Delete iam/policy.tag
        api_instance.iam_project_policy_tag_delete(project_id, policy_id, tag_id)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 
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

# **iam_project_policy_tag_get**
> Tag iam_project_policy_tag_get(project_id, policy_id, tag_id)

Get iam/policy.tag

Get iam/policy.tag

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Get iam/policy.tag
        api_response = api_instance.iam_project_policy_tag_get(project_id, policy_id, tag_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 
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

# **iam_project_policy_tag_list**
> list[Tag] iam_project_policy_tag_list(project_id, policy_id)

List iam/policy.tag

List iam/policy.tag

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id

    try:
        # List iam/policy.tag
        api_response = api_instance.iam_project_policy_tag_list(project_id, policy_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 

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

# **iam_project_policy_tag_put**
> list[Tag] iam_project_policy_tag_put(project_id, policy_id, tag)

Replace iam/policy.tag

Replace iam/policy.tag

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id
tag = [h1.Tag()] # list[Tag] | 

    try:
        # Replace iam/policy.tag
        api_response = api_instance.iam_project_policy_tag_put(project_id, policy_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 
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

# **iam_project_policy_update**
> Policy iam_project_policy_update(project_id, policy_id, iam_project_policy_update)

Update iam/policy

Returns modified policy

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
    api_instance = h1.IamProjectPolicyApi(api_client)
    project_id = 'project_id_example' # str | Project Id
policy_id = 'policy_id_example' # str | Policy Id
iam_project_policy_update = h1.IamProjectPolicyUpdate() # IamProjectPolicyUpdate | 

    try:
        # Update iam/policy
        api_response = api_instance.iam_project_policy_update(project_id, policy_id, iam_project_policy_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectPolicyApi->iam_project_policy_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **policy_id** | **str**| Policy Id | 
 **iam_project_policy_update** | [**IamProjectPolicyUpdate**](IamProjectPolicyUpdate.md)|  | 

### Return type

[**Policy**](Policy.md)

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

