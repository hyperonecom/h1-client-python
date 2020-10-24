# h1.IamProjectApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iam_project_billing_list**](IamProjectApi.md#iam_project_billing_list) | **GET** /iam/project/{projectId}/billing | List iam/project.billing
[**iam_project_create**](IamProjectApi.md#iam_project_create) | **POST** /iam/project | Create iam/project
[**iam_project_credential_store_create**](IamProjectApi.md#iam_project_credential_store_create) | **POST** /iam/project/{projectId}/credentialStore | Create iam/project.credentialStore
[**iam_project_credential_store_delete**](IamProjectApi.md#iam_project_credential_store_delete) | **DELETE** /iam/project/{projectId}/credentialStore/{credentialStoreId} | Delete iam/project.credentialStore
[**iam_project_credential_store_get**](IamProjectApi.md#iam_project_credential_store_get) | **GET** /iam/project/{projectId}/credentialStore/{credentialStoreId} | Get iam/project.credentialStore
[**iam_project_credential_store_list**](IamProjectApi.md#iam_project_credential_store_list) | **GET** /iam/project/{projectId}/credentialStore | List iam/project.credentialStore
[**iam_project_credential_store_patch**](IamProjectApi.md#iam_project_credential_store_patch) | **PATCH** /iam/project/{projectId}/credentialStore/{credentialStoreId} | Update iam/project.credentialStore
[**iam_project_delete**](IamProjectApi.md#iam_project_delete) | **DELETE** /iam/project/{projectId} | Delete iam/project
[**iam_project_event_get**](IamProjectApi.md#iam_project_event_get) | **GET** /iam/project/{projectId}/event/{eventId} | Get iam/project.event
[**iam_project_event_list**](IamProjectApi.md#iam_project_event_list) | **GET** /iam/project/{projectId}/event | List iam/project.event
[**iam_project_get**](IamProjectApi.md#iam_project_get) | **GET** /iam/project/{projectId} | Get iam/project
[**iam_project_invitation_accept**](IamProjectApi.md#iam_project_invitation_accept) | **POST** /iam/project/{projectId}/invitation/{invitationId}/actions/accept | Accept iam/project.invitation
[**iam_project_invitation_delete**](IamProjectApi.md#iam_project_invitation_delete) | **DELETE** /iam/project/{projectId}/invitation/{invitationId} | Delete iam/project.invitation
[**iam_project_invitation_get**](IamProjectApi.md#iam_project_invitation_get) | **GET** /iam/project/{projectId}/invitation/{invitationId} | Get iam/project.invitation
[**iam_project_invitation_list**](IamProjectApi.md#iam_project_invitation_list) | **GET** /iam/project/{projectId}/invitation | List iam/project.invitation
[**iam_project_invoice_list**](IamProjectApi.md#iam_project_invoice_list) | **GET** /iam/project/{projectId}/invoice | List iam/project.invoice
[**iam_project_list**](IamProjectApi.md#iam_project_list) | **GET** /iam/project | List iam/project
[**iam_project_ownership_create**](IamProjectApi.md#iam_project_ownership_create) | **POST** /iam/project/{projectId}/ownership | Create iam/project.ownership
[**iam_project_ownership_delete**](IamProjectApi.md#iam_project_ownership_delete) | **DELETE** /iam/project/{projectId}/ownership/{ownershipId} | Delete iam/project.ownership
[**iam_project_ownership_get**](IamProjectApi.md#iam_project_ownership_get) | **GET** /iam/project/{projectId}/ownership/{ownershipId} | Get iam/project.ownership
[**iam_project_ownership_list**](IamProjectApi.md#iam_project_ownership_list) | **GET** /iam/project/{projectId}/ownership | List iam/project.ownership
[**iam_project_payment_list**](IamProjectApi.md#iam_project_payment_list) | **GET** /iam/project/{projectId}/payment | List iam/project.payment
[**iam_project_proforma_list**](IamProjectApi.md#iam_project_proforma_list) | **GET** /iam/project/{projectId}/proforma | List iam/project.proforma
[**iam_project_quota_get**](IamProjectApi.md#iam_project_quota_get) | **GET** /iam/project/{projectId}/quota/{quotaId} | Get iam/project.quota
[**iam_project_quota_limit_patch**](IamProjectApi.md#iam_project_quota_limit_patch) | **PATCH** /iam/project/{projectId}/quota/{quotaId}/limit | Update iam/project.limit
[**iam_project_quota_list**](IamProjectApi.md#iam_project_quota_list) | **GET** /iam/project/{projectId}/quota | List iam/project.quota
[**iam_project_service_get**](IamProjectApi.md#iam_project_service_get) | **GET** /iam/project/{projectId}/service/{serviceId} | Get iam/project.service
[**iam_project_service_list**](IamProjectApi.md#iam_project_service_list) | **GET** /iam/project/{projectId}/service | List iam/project.service
[**iam_project_tag_create**](IamProjectApi.md#iam_project_tag_create) | **POST** /iam/project/{projectId}/tag | Create iam/project.tag
[**iam_project_tag_delete**](IamProjectApi.md#iam_project_tag_delete) | **DELETE** /iam/project/{projectId}/tag/{tagId} | Delete iam/project.tag
[**iam_project_tag_get**](IamProjectApi.md#iam_project_tag_get) | **GET** /iam/project/{projectId}/tag/{tagId} | Get iam/project.tag
[**iam_project_tag_list**](IamProjectApi.md#iam_project_tag_list) | **GET** /iam/project/{projectId}/tag | List iam/project.tag
[**iam_project_tag_put**](IamProjectApi.md#iam_project_tag_put) | **PUT** /iam/project/{projectId}/tag | Replace iam/project.tag
[**iam_project_threshold_create**](IamProjectApi.md#iam_project_threshold_create) | **POST** /iam/project/{projectId}/threshold | Create iam/project.threshold
[**iam_project_threshold_delete**](IamProjectApi.md#iam_project_threshold_delete) | **DELETE** /iam/project/{projectId}/threshold/{thresholdId} | Delete iam/project.threshold
[**iam_project_threshold_get**](IamProjectApi.md#iam_project_threshold_get) | **GET** /iam/project/{projectId}/threshold/{thresholdId} | Get iam/project.threshold
[**iam_project_threshold_list**](IamProjectApi.md#iam_project_threshold_list) | **GET** /iam/project/{projectId}/threshold | List iam/project.threshold
[**iam_project_update**](IamProjectApi.md#iam_project_update) | **PATCH** /iam/project/{projectId} | Update iam/project


# **iam_project_billing_list**
> list[Billing] iam_project_billing_list(project_id, start=start, end=end, resource_type=resource_type)

List iam/project.billing

List iam/project.billing

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
start = '2013-10-20T19:20:30+01:00' # datetime | start (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | end (optional)
resource_type = 'resource_type_example' # str | resource.type (optional)

    try:
        # List iam/project.billing
        api_response = api_instance.iam_project_billing_list(project_id, start=start, end=end, resource_type=resource_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_billing_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **start** | **datetime**| start | [optional] 
 **end** | **datetime**| end | [optional] 
 **resource_type** | **str**| resource.type | [optional] 

### Return type

[**list[Billing]**](Billing.md)

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

# **iam_project_create**
> Project iam_project_create(iam_project_create, x_idempotency_key=x_idempotency_key)

Create iam/project

Create project

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
    api_instance = h1.IamProjectApi(api_client)
    iam_project_create = h1.IamProjectCreate() # IamProjectCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create iam/project
        api_response = api_instance.iam_project_create(iam_project_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iam_project_create** | [**IamProjectCreate**](IamProjectCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Project**](Project.md)

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

# **iam_project_credential_store_create**
> ProjectCredential iam_project_credential_store_create(project_id, project_credential)

Create iam/project.credentialStore

Create iam/project.credentialStore

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
project_credential = h1.ProjectCredential() # ProjectCredential | 

    try:
        # Create iam/project.credentialStore
        api_response = api_instance.iam_project_credential_store_create(project_id, project_credential)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_credential_store_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **project_credential** | [**ProjectCredential**](ProjectCredential.md)|  | 

### Return type

[**ProjectCredential**](ProjectCredential.md)

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

# **iam_project_credential_store_delete**
> Project iam_project_credential_store_delete(project_id, credential_store_id)

Delete iam/project.credentialStore

Delete iam/project.credentialStore

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
credential_store_id = 'credential_store_id_example' # str | credentialStoreId

    try:
        # Delete iam/project.credentialStore
        api_response = api_instance.iam_project_credential_store_delete(project_id, credential_store_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_credential_store_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **credential_store_id** | **str**| credentialStoreId | 

### Return type

[**Project**](Project.md)

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

# **iam_project_credential_store_get**
> ProjectCredential iam_project_credential_store_get(project_id, credential_store_id)

Get iam/project.credentialStore

Get iam/project.credentialStore

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
credential_store_id = 'credential_store_id_example' # str | credentialStoreId

    try:
        # Get iam/project.credentialStore
        api_response = api_instance.iam_project_credential_store_get(project_id, credential_store_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_credential_store_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **credential_store_id** | **str**| credentialStoreId | 

### Return type

[**ProjectCredential**](ProjectCredential.md)

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

# **iam_project_credential_store_list**
> list[ProjectCredential] iam_project_credential_store_list(project_id)

List iam/project.credentialStore

List iam/project.credentialStore

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id

    try:
        # List iam/project.credentialStore
        api_response = api_instance.iam_project_credential_store_list(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_credential_store_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

### Return type

[**list[ProjectCredential]**](ProjectCredential.md)

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

# **iam_project_credential_store_patch**
> ProjectCredential iam_project_credential_store_patch(project_id, credential_store_id, iam_project_credential_store_patch)

Update iam/project.credentialStore

Update iam/project.credentialStore

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
credential_store_id = 'credential_store_id_example' # str | credentialStoreId
iam_project_credential_store_patch = h1.IamProjectCredentialStorePatch() # IamProjectCredentialStorePatch | 

    try:
        # Update iam/project.credentialStore
        api_response = api_instance.iam_project_credential_store_patch(project_id, credential_store_id, iam_project_credential_store_patch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_credential_store_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **credential_store_id** | **str**| credentialStoreId | 
 **iam_project_credential_store_patch** | [**IamProjectCredentialStorePatch**](IamProjectCredentialStorePatch.md)|  | 

### Return type

[**ProjectCredential**](ProjectCredential.md)

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

# **iam_project_delete**
> iam_project_delete(project_id)

Delete iam/project

Delete project

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id

    try:
        # Delete iam/project
        api_instance.iam_project_delete(project_id)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

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

# **iam_project_event_get**
> Event iam_project_event_get(project_id, event_id)

Get iam/project.event

Get iam/project.event

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get iam/project.event
        api_response = api_instance.iam_project_event_get(project_id, event_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
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

# **iam_project_event_list**
> list[Event] iam_project_event_list(project_id, limit=limit, skip=skip)

List iam/project.event

List iam/project.event

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List iam/project.event
        api_response = api_instance.iam_project_event_list(project_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
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

# **iam_project_get**
> Project iam_project_get(project_id)

Get iam/project

Returns a single project

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id

    try:
        # Get iam/project
        api_response = api_instance.iam_project_get(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

### Return type

[**Project**](Project.md)

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

# **iam_project_invitation_accept**
> Invitation iam_project_invitation_accept(project_id, invitation_id, iam_project_invitation_accept)

Accept iam/project.invitation

action accept

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
invitation_id = 'invitation_id_example' # str | invitationId
iam_project_invitation_accept = h1.IamProjectInvitationAccept() # IamProjectInvitationAccept | 

    try:
        # Accept iam/project.invitation
        api_response = api_instance.iam_project_invitation_accept(project_id, invitation_id, iam_project_invitation_accept)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_invitation_accept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **invitation_id** | **str**| invitationId | 
 **iam_project_invitation_accept** | [**IamProjectInvitationAccept**](IamProjectInvitationAccept.md)|  | 

### Return type

[**Invitation**](Invitation.md)

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

# **iam_project_invitation_delete**
> iam_project_invitation_delete(project_id, invitation_id)

Delete iam/project.invitation

Delete iam/project.invitation

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
invitation_id = 'invitation_id_example' # str | invitationId

    try:
        # Delete iam/project.invitation
        api_instance.iam_project_invitation_delete(project_id, invitation_id)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_invitation_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **invitation_id** | **str**| invitationId | 

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

# **iam_project_invitation_get**
> Invitation iam_project_invitation_get(project_id, invitation_id)

Get iam/project.invitation

Get iam/project.invitation

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
invitation_id = 'invitation_id_example' # str | invitationId

    try:
        # Get iam/project.invitation
        api_response = api_instance.iam_project_invitation_get(project_id, invitation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_invitation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **invitation_id** | **str**| invitationId | 

### Return type

[**Invitation**](Invitation.md)

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

# **iam_project_invitation_list**
> list[Invitation] iam_project_invitation_list(project_id, resource=resource)

List iam/project.invitation

List iam/project.invitation

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
resource = 'resource_example' # str | resource (optional)

    try:
        # List iam/project.invitation
        api_response = api_instance.iam_project_invitation_list(project_id, resource=resource)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_invitation_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **resource** | **str**| resource | [optional] 

### Return type

[**list[Invitation]**](Invitation.md)

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

# **iam_project_invoice_list**
> list[Invoice] iam_project_invoice_list(project_id)

List iam/project.invoice

List iam/project.invoice

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id

    try:
        # List iam/project.invoice
        api_response = api_instance.iam_project_invoice_list(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_invoice_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

### Return type

[**list[Invoice]**](Invoice.md)

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

# **iam_project_list**
> list[Project] iam_project_list(name=name, limit=limit, active=active, organisation=organisation, lean=lean, tag_value=tag_value, tag_key=tag_key)

List iam/project

List project

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
    api_instance = h1.IamProjectApi(api_client)
    name = 'name_example' # str | Filter by name (optional)
limit = 3.4 # float | Filter by $limit (optional)
active = False # bool | Filter by active (optional) (default to False)
organisation = 'organisation_example' # str | Filter by organisation (optional)
lean = False # bool | return a lightweight version of the resource (optional) (default to False)
tag_value = 'tag_value_example' # str | Filter by tag.value (optional)
tag_key = 'tag_key_example' # str | Filter by tag.key (optional)

    try:
        # List iam/project
        api_response = api_instance.iam_project_list(name=name, limit=limit, active=active, organisation=organisation, lean=lean, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter by name | [optional] 
 **limit** | **float**| Filter by $limit | [optional] 
 **active** | **bool**| Filter by active | [optional] [default to False]
 **organisation** | **str**| Filter by organisation | [optional] 
 **lean** | **bool**| return a lightweight version of the resource | [optional] [default to False]
 **tag_value** | **str**| Filter by tag.value | [optional] 
 **tag_key** | **str**| Filter by tag.key | [optional] 

### Return type

[**list[Project]**](Project.md)

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

# **iam_project_ownership_create**
> Project iam_project_ownership_create(project_id, iam_project_ownership_create)

Create iam/project.ownership

Create iam/project.ownership

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
iam_project_ownership_create = h1.IamProjectOwnershipCreate() # IamProjectOwnershipCreate | 

    try:
        # Create iam/project.ownership
        api_response = api_instance.iam_project_ownership_create(project_id, iam_project_ownership_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_ownership_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **iam_project_ownership_create** | [**IamProjectOwnershipCreate**](IamProjectOwnershipCreate.md)|  | 

### Return type

[**Project**](Project.md)

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

# **iam_project_ownership_delete**
> iam_project_ownership_delete(project_id, ownership_id)

Delete iam/project.ownership

Delete iam/project.ownership

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
ownership_id = 'ownership_id_example' # str | ownershipId

    try:
        # Delete iam/project.ownership
        api_instance.iam_project_ownership_delete(project_id, ownership_id)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_ownership_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **ownership_id** | **str**| ownershipId | 

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

# **iam_project_ownership_get**
> Ownership iam_project_ownership_get(project_id, ownership_id)

Get iam/project.ownership

Get iam/project.ownership

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
ownership_id = 'ownership_id_example' # str | ownershipId

    try:
        # Get iam/project.ownership
        api_response = api_instance.iam_project_ownership_get(project_id, ownership_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_ownership_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **ownership_id** | **str**| ownershipId | 

### Return type

[**Ownership**](Ownership.md)

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

# **iam_project_ownership_list**
> list[Ownership] iam_project_ownership_list(project_id)

List iam/project.ownership

List iam/project.ownership

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id

    try:
        # List iam/project.ownership
        api_response = api_instance.iam_project_ownership_list(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_ownership_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

### Return type

[**list[Ownership]**](Ownership.md)

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

# **iam_project_payment_list**
> list[Payment] iam_project_payment_list(project_id)

List iam/project.payment

List iam/project.payment

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id

    try:
        # List iam/project.payment
        api_response = api_instance.iam_project_payment_list(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_payment_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

### Return type

[**list[Payment]**](Payment.md)

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

# **iam_project_proforma_list**
> list[Proforma] iam_project_proforma_list(project_id)

List iam/project.proforma

List iam/project.proforma

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id

    try:
        # List iam/project.proforma
        api_response = api_instance.iam_project_proforma_list(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_proforma_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

### Return type

[**list[Proforma]**](Proforma.md)

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

# **iam_project_quota_get**
> Quota iam_project_quota_get(project_id, quota_id)

Get iam/project.quota

Get iam/project.quota

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
quota_id = 'quota_id_example' # str | quotaId

    try:
        # Get iam/project.quota
        api_response = api_instance.iam_project_quota_get(project_id, quota_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_quota_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **quota_id** | **str**| quotaId | 

### Return type

[**Quota**](Quota.md)

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

# **iam_project_quota_limit_patch**
> QuotaLimit iam_project_quota_limit_patch(project_id, quota_id, iam_project_quota_limit_patch)

Update iam/project.limit

Update iam/project.limit

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
quota_id = 'quota_id_example' # str | quotaId
iam_project_quota_limit_patch = h1.IamProjectQuotaLimitPatch() # IamProjectQuotaLimitPatch | 

    try:
        # Update iam/project.limit
        api_response = api_instance.iam_project_quota_limit_patch(project_id, quota_id, iam_project_quota_limit_patch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_quota_limit_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **quota_id** | **str**| quotaId | 
 **iam_project_quota_limit_patch** | [**IamProjectQuotaLimitPatch**](IamProjectQuotaLimitPatch.md)|  | 

### Return type

[**QuotaLimit**](QuotaLimit.md)

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

# **iam_project_quota_list**
> list[Quota] iam_project_quota_list(project_id)

List iam/project.quota

List iam/project.quota

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id

    try:
        # List iam/project.quota
        api_response = api_instance.iam_project_quota_list(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_quota_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

### Return type

[**list[Quota]**](Quota.md)

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

# **iam_project_service_get**
> ResourceService iam_project_service_get(project_id, service_id)

Get iam/project.service

Get iam/project.service

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
service_id = 'service_id_example' # str | serviceId

    try:
        # Get iam/project.service
        api_response = api_instance.iam_project_service_get(project_id, service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
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

# **iam_project_service_list**
> list[ResourceService] iam_project_service_list(project_id)

List iam/project.service

List iam/project.service

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id

    try:
        # List iam/project.service
        api_response = api_instance.iam_project_service_list(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

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

# **iam_project_tag_create**
> Tag iam_project_tag_create(project_id, tag)

Create iam/project.tag

Create iam/project.tag

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
tag = h1.Tag() # Tag | 

    try:
        # Create iam/project.tag
        api_response = api_instance.iam_project_tag_create(project_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
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

# **iam_project_tag_delete**
> iam_project_tag_delete(project_id, tag_id)

Delete iam/project.tag

Delete iam/project.tag

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Delete iam/project.tag
        api_instance.iam_project_tag_delete(project_id, tag_id)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
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

# **iam_project_tag_get**
> Tag iam_project_tag_get(project_id, tag_id)

Get iam/project.tag

Get iam/project.tag

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Get iam/project.tag
        api_response = api_instance.iam_project_tag_get(project_id, tag_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
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

# **iam_project_tag_list**
> list[Tag] iam_project_tag_list(project_id)

List iam/project.tag

List iam/project.tag

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id

    try:
        # List iam/project.tag
        api_response = api_instance.iam_project_tag_list(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

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

# **iam_project_tag_put**
> list[Tag] iam_project_tag_put(project_id, tag)

Replace iam/project.tag

Replace iam/project.tag

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
tag = [h1.Tag()] # list[Tag] | 

    try:
        # Replace iam/project.tag
        api_response = api_instance.iam_project_tag_put(project_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
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

# **iam_project_threshold_create**
> ProjectThreshold iam_project_threshold_create(project_id, iam_project_threshold_create)

Create iam/project.threshold

Create iam/project.threshold

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
iam_project_threshold_create = h1.IamProjectThresholdCreate() # IamProjectThresholdCreate | 

    try:
        # Create iam/project.threshold
        api_response = api_instance.iam_project_threshold_create(project_id, iam_project_threshold_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_threshold_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **iam_project_threshold_create** | [**IamProjectThresholdCreate**](IamProjectThresholdCreate.md)|  | 

### Return type

[**ProjectThreshold**](ProjectThreshold.md)

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

# **iam_project_threshold_delete**
> iam_project_threshold_delete(project_id, threshold_id)

Delete iam/project.threshold

Delete iam/project.threshold

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
threshold_id = 'threshold_id_example' # str | thresholdId

    try:
        # Delete iam/project.threshold
        api_instance.iam_project_threshold_delete(project_id, threshold_id)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_threshold_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **threshold_id** | **str**| thresholdId | 

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

# **iam_project_threshold_get**
> ProjectThreshold iam_project_threshold_get(project_id, threshold_id)

Get iam/project.threshold

Get iam/project.threshold

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
threshold_id = 'threshold_id_example' # str | thresholdId

    try:
        # Get iam/project.threshold
        api_response = api_instance.iam_project_threshold_get(project_id, threshold_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_threshold_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **threshold_id** | **str**| thresholdId | 

### Return type

[**ProjectThreshold**](ProjectThreshold.md)

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

# **iam_project_threshold_list**
> list[ProjectThreshold] iam_project_threshold_list(project_id)

List iam/project.threshold

List iam/project.threshold

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id

    try:
        # List iam/project.threshold
        api_response = api_instance.iam_project_threshold_list(project_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_threshold_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 

### Return type

[**list[ProjectThreshold]**](ProjectThreshold.md)

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

# **iam_project_update**
> Project iam_project_update(project_id, iam_project_update)

Update iam/project

Returns modified project

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
    api_instance = h1.IamProjectApi(api_client)
    project_id = 'project_id_example' # str | Project Id
iam_project_update = h1.IamProjectUpdate() # IamProjectUpdate | 

    try:
        # Update iam/project
        api_response = api_instance.iam_project_update(project_id, iam_project_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **iam_project_update** | [**IamProjectUpdate**](IamProjectUpdate.md)|  | 

### Return type

[**Project**](Project.md)

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

