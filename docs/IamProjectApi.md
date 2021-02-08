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
[**iam_project_transfer**](IamProjectApi.md#iam_project_transfer) | **POST** /iam/project/{projectId}/actions/transfer | Transfer iam/project
[**iam_project_update**](IamProjectApi.md#iam_project_update) | **PATCH** /iam/project/{projectId} | Update iam/project


# **iam_project_billing_list**
> [Billing] iam_project_billing_list(project_id)

List iam/project.billing

List iam/project.billing

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
from h1.model.billing import Billing
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    start = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | start (optional)
    end = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | end (optional)
    resource_type = "resource.type_example" # str | resource.type (optional)

    # example passing only required values which don't have defaults set
    try:
        # List iam/project.billing
        api_response = api_instance.iam_project_billing_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_billing_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/project.billing
        api_response = api_instance.iam_project_billing_list(project_id, start=start, end=end, resource_type=resource_type)
        pprint(api_response)
    except h1.ApiException as e:
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

[**[Billing]**](Billing.md)

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
> Project iam_project_create(iam_project_create)

Create iam/project

Create project

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
from h1.model.project import Project
from h1.model.inline_response400 import InlineResponse400
from h1.model.iam_project_create import IamProjectCreate
from pprint import pprint
# Defining the host is optional and defaults to https://api.hyperone.com/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = h1.Configuration(
    host = "https://api.hyperone.com/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = h1.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with h1.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iam_project_api.IamProjectApi(api_client)
    iam_project_create = IamProjectCreate(
        name="name_example",
        organisation="organisation_example",
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # IamProjectCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create iam/project
        api_response = api_instance.iam_project_create(iam_project_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create iam/project
        api_response = api_instance.iam_project_create(iam_project_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iam_project_create** | [**IamProjectCreate**](IamProjectCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import iam_project_api
from h1.model.project_credential import ProjectCredential
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    project_credential = ProjectCredential(
        id="id_example",
        name="name_example",
        created_by="created_by_example",
        created_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
        type="ssh",
        value="value_example",
        fingerprint="fingerprint_example",
        token="token_example",
    ) # ProjectCredential | 

    # example passing only required values which don't have defaults set
    try:
        # Create iam/project.credentialStore
        api_response = api_instance.iam_project_credential_store_create(project_id, project_credential)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_project_api
from h1.model.project import Project
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    credential_store_id = "credentialStoreId_example" # str | credentialStoreId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/project.credentialStore
        api_response = api_instance.iam_project_credential_store_delete(project_id, credential_store_id)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_project_api
from h1.model.project_credential import ProjectCredential
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    credential_store_id = "credentialStoreId_example" # str | credentialStoreId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/project.credentialStore
        api_response = api_instance.iam_project_credential_store_get(project_id, credential_store_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [ProjectCredential] iam_project_credential_store_list(project_id)

List iam/project.credentialStore

List iam/project.credentialStore

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
from h1.model.project_credential import ProjectCredential
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/project.credentialStore
        api_response = api_instance.iam_project_credential_store_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_credential_store_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |

### Return type

[**[ProjectCredential]**](ProjectCredential.md)

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
import time
import h1
from h1.api import iam_project_api
from h1.model.project_credential import ProjectCredential
from h1.model.iam_project_credential_store_patch import IamProjectCredentialStorePatch
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    credential_store_id = "credentialStoreId_example" # str | credentialStoreId
    iam_project_credential_store_patch = IamProjectCredentialStorePatch(
        name="name_example",
    ) # IamProjectCredentialStorePatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update iam/project.credentialStore
        api_response = api_instance.iam_project_credential_store_patch(project_id, credential_store_id, iam_project_credential_store_patch)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_project_api
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/project
        api_instance.iam_project_delete(project_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_project_api
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/project.event
        api_response = api_instance.iam_project_event_get(project_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Event] iam_project_event_list(project_id)

List iam/project.event

List iam/project.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List iam/project.event
        api_response = api_instance.iam_project_event_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/project.event
        api_response = api_instance.iam_project_event_list(project_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
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

# **iam_project_get**
> Project iam_project_get(project_id)

Get iam/project

Returns a single project

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
from h1.model.project import Project
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id

    # example passing only required values which don't have defaults set
    try:
        # Get iam/project
        api_response = api_instance.iam_project_get(project_id)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_project_api
from h1.model.iam_project_invitation_accept import IamProjectInvitationAccept
from h1.model.invitation import Invitation
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    invitation_id = "invitationId_example" # str | invitationId
    iam_project_invitation_accept = IamProjectInvitationAccept(
        token="token_example",
    ) # IamProjectInvitationAccept | 

    # example passing only required values which don't have defaults set
    try:
        # Accept iam/project.invitation
        api_response = api_instance.iam_project_invitation_accept(project_id, invitation_id, iam_project_invitation_accept)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_project_api
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    invitation_id = "invitationId_example" # str | invitationId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/project.invitation
        api_instance.iam_project_invitation_delete(project_id, invitation_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_project_api
from h1.model.invitation import Invitation
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    invitation_id = "invitationId_example" # str | invitationId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/project.invitation
        api_response = api_instance.iam_project_invitation_get(project_id, invitation_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Invitation] iam_project_invitation_list(project_id)

List iam/project.invitation

List iam/project.invitation

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
from h1.model.invitation import Invitation
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    resource = "resource_example" # str | resource (optional)

    # example passing only required values which don't have defaults set
    try:
        # List iam/project.invitation
        api_response = api_instance.iam_project_invitation_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_invitation_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/project.invitation
        api_response = api_instance.iam_project_invitation_list(project_id, resource=resource)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_invitation_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **resource** | **str**| resource | [optional]

### Return type

[**[Invitation]**](Invitation.md)

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
> [Invoice] iam_project_invoice_list(project_id)

List iam/project.invoice

List iam/project.invoice

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
from h1.model.invoice import Invoice
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/project.invoice
        api_response = api_instance.iam_project_invoice_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_invoice_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |

### Return type

[**[Invoice]**](Invoice.md)

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
> [Project] iam_project_list()

List iam/project

List project

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
from h1.model.project import Project
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    name = "name_example" # str | Filter by name (optional)
    limit = 3.14 # float | Filter by $limit (optional)
    active = False # bool | Filter by active (optional) if omitted the server will use the default value of False
    organisation = "organisation_example" # str | Filter by organisation (optional)
    lean = False # bool | return a lightweight version of the resource (optional) if omitted the server will use the default value of False
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/project
        api_response = api_instance.iam_project_list(name=name, limit=limit, active=active, organisation=organisation, lean=lean, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter by name | [optional]
 **limit** | **float**| Filter by $limit | [optional]
 **active** | **bool**| Filter by active | [optional] if omitted the server will use the default value of False
 **organisation** | **str**| Filter by organisation | [optional]
 **lean** | **bool**| return a lightweight version of the resource | [optional] if omitted the server will use the default value of False
 **tag_value** | **str**| Filter by tag.value | [optional]
 **tag_key** | **str**| Filter by tag.key | [optional]

### Return type

[**[Project]**](Project.md)

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
import time
import h1
from h1.api import iam_project_api
from h1.model.project import Project
from h1.model.iam_project_ownership_create import IamProjectOwnershipCreate
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    iam_project_ownership_create = IamProjectOwnershipCreate(
        email="email_example",
    ) # IamProjectOwnershipCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create iam/project.ownership
        api_response = api_instance.iam_project_ownership_create(project_id, iam_project_ownership_create)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_project_api
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    ownership_id = "ownershipId_example" # str | ownershipId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/project.ownership
        api_instance.iam_project_ownership_delete(project_id, ownership_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_project_api
from h1.model.ownership import Ownership
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    ownership_id = "ownershipId_example" # str | ownershipId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/project.ownership
        api_response = api_instance.iam_project_ownership_get(project_id, ownership_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Ownership] iam_project_ownership_list(project_id)

List iam/project.ownership

List iam/project.ownership

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
from h1.model.ownership import Ownership
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/project.ownership
        api_response = api_instance.iam_project_ownership_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_ownership_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |

### Return type

[**[Ownership]**](Ownership.md)

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
> [Payment] iam_project_payment_list(project_id)

List iam/project.payment

List iam/project.payment

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
from h1.model.payment import Payment
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/project.payment
        api_response = api_instance.iam_project_payment_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_payment_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |

### Return type

[**[Payment]**](Payment.md)

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
> [Proforma] iam_project_proforma_list(project_id)

List iam/project.proforma

List iam/project.proforma

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
from h1.model.proforma import Proforma
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/project.proforma
        api_response = api_instance.iam_project_proforma_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_proforma_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |

### Return type

[**[Proforma]**](Proforma.md)

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
import time
import h1
from h1.api import iam_project_api
from h1.model.quota import Quota
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    quota_id = "quotaId_example" # str | quotaId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/project.quota
        api_response = api_instance.iam_project_quota_get(project_id, quota_id)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_project_api
from h1.model.iam_project_quota_limit_patch import IamProjectQuotaLimitPatch
from h1.model.quota_limit import QuotaLimit
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    quota_id = "quotaId_example" # str | quotaId
    iam_project_quota_limit_patch = IamProjectQuotaLimitPatch(
        user=3.14,
    ) # IamProjectQuotaLimitPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update iam/project.limit
        api_response = api_instance.iam_project_quota_limit_patch(project_id, quota_id, iam_project_quota_limit_patch)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Quota] iam_project_quota_list(project_id)

List iam/project.quota

List iam/project.quota

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
from h1.model.quota import Quota
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/project.quota
        api_response = api_instance.iam_project_quota_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_quota_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |

### Return type

[**[Quota]**](Quota.md)

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
import time
import h1
from h1.api import iam_project_api
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/project.service
        api_response = api_instance.iam_project_service_get(project_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [ResourceService] iam_project_service_list(project_id)

List iam/project.service

List iam/project.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/project.service
        api_response = api_instance.iam_project_service_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |

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

# **iam_project_tag_create**
> Tag iam_project_tag_create(project_id, tag)

Create iam/project.tag

Create iam/project.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create iam/project.tag
        api_response = api_instance.iam_project_tag_create(project_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_project_api
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/project.tag
        api_instance.iam_project_tag_delete(project_id, tag_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_project_api
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/project.tag
        api_response = api_instance.iam_project_tag_get(project_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Tag] iam_project_tag_list(project_id)

List iam/project.tag

List iam/project.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/project.tag
        api_response = api_instance.iam_project_tag_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |

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

# **iam_project_tag_put**
> [Tag] iam_project_tag_put(project_id, tag_array)

Replace iam/project.tag

Replace iam/project.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace iam/project.tag
        api_response = api_instance.iam_project_tag_put(project_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
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

# **iam_project_threshold_create**
> ProjectThreshold iam_project_threshold_create(project_id, iam_project_threshold_create)

Create iam/project.threshold

Create iam/project.threshold

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
from h1.model.iam_project_threshold_create import IamProjectThresholdCreate
from h1.model.project_threshold import ProjectThreshold
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    iam_project_threshold_create = IamProjectThresholdCreate(
        id="id_example",
        name="name_example",
        type="type_example",
        value=3.14,
        uri="uri_example",
    ) # IamProjectThresholdCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create iam/project.threshold
        api_response = api_instance.iam_project_threshold_create(project_id, iam_project_threshold_create)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_project_api
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    threshold_id = "thresholdId_example" # str | thresholdId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/project.threshold
        api_instance.iam_project_threshold_delete(project_id, threshold_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_project_api
from h1.model.project_threshold import ProjectThreshold
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    threshold_id = "thresholdId_example" # str | thresholdId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/project.threshold
        api_response = api_instance.iam_project_threshold_get(project_id, threshold_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [ProjectThreshold] iam_project_threshold_list(project_id)

List iam/project.threshold

List iam/project.threshold

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
from h1.model.project_threshold import ProjectThreshold
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/project.threshold
        api_response = api_instance.iam_project_threshold_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_threshold_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |

### Return type

[**[ProjectThreshold]**](ProjectThreshold.md)

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

# **iam_project_transfer**
> Project iam_project_transfer(project_id, iam_project_transfer)

Transfer iam/project

action transfer

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
from h1.model.project import Project
from h1.model.iam_project_transfer import IamProjectTransfer
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    iam_project_transfer = IamProjectTransfer(
        organisation="organisation_example",
    ) # IamProjectTransfer | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Transfer iam/project
        api_response = api_instance.iam_project_transfer(project_id, iam_project_transfer)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_transfer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Transfer iam/project
        api_response = api_instance.iam_project_transfer(project_id, iam_project_transfer, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectApi->iam_project_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **iam_project_transfer** | [**IamProjectTransfer**](IamProjectTransfer.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

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

# **iam_project_update**
> Project iam_project_update(project_id, iam_project_update)

Update iam/project

Returns modified project

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_api
from h1.model.project import Project
from h1.model.iam_project_update import IamProjectUpdate
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
    api_instance = iam_project_api.IamProjectApi(api_client)
    project_id = "projectId_example" # str | Project Id
    iam_project_update = IamProjectUpdate(
        name="name_example",
    ) # IamProjectUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update iam/project
        api_response = api_instance.iam_project_update(project_id, iam_project_update)
        pprint(api_response)
    except h1.ApiException as e:
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

