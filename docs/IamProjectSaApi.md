# h1.IamProjectSaApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iam_project_sa_create**](IamProjectSaApi.md#iam_project_sa_create) | **POST** /iam/project/{projectId}/sa | Create iam/sa
[**iam_project_sa_credential_create**](IamProjectSaApi.md#iam_project_sa_credential_create) | **POST** /iam/project/{projectId}/sa/{saId}/credential | Create iam/sa.credential
[**iam_project_sa_credential_delete**](IamProjectSaApi.md#iam_project_sa_credential_delete) | **DELETE** /iam/project/{projectId}/sa/{saId}/credential/{credentialId} | Delete iam/sa.credential
[**iam_project_sa_credential_get**](IamProjectSaApi.md#iam_project_sa_credential_get) | **GET** /iam/project/{projectId}/sa/{saId}/credential/{credentialId} | Get iam/sa.credential
[**iam_project_sa_credential_list**](IamProjectSaApi.md#iam_project_sa_credential_list) | **GET** /iam/project/{projectId}/sa/{saId}/credential | List iam/sa.credential
[**iam_project_sa_credential_patch**](IamProjectSaApi.md#iam_project_sa_credential_patch) | **PATCH** /iam/project/{projectId}/sa/{saId}/credential/{credentialId} | Update iam/sa.credential
[**iam_project_sa_delete**](IamProjectSaApi.md#iam_project_sa_delete) | **DELETE** /iam/project/{projectId}/sa/{saId} | Delete iam/sa
[**iam_project_sa_event_get**](IamProjectSaApi.md#iam_project_sa_event_get) | **GET** /iam/project/{projectId}/sa/{saId}/event/{eventId} | Get iam/sa.event
[**iam_project_sa_event_list**](IamProjectSaApi.md#iam_project_sa_event_list) | **GET** /iam/project/{projectId}/sa/{saId}/event | List iam/sa.event
[**iam_project_sa_get**](IamProjectSaApi.md#iam_project_sa_get) | **GET** /iam/project/{projectId}/sa/{saId} | Get iam/sa
[**iam_project_sa_list**](IamProjectSaApi.md#iam_project_sa_list) | **GET** /iam/project/{projectId}/sa | List iam/sa
[**iam_project_sa_service_get**](IamProjectSaApi.md#iam_project_sa_service_get) | **GET** /iam/project/{projectId}/sa/{saId}/service/{serviceId} | Get iam/sa.service
[**iam_project_sa_service_list**](IamProjectSaApi.md#iam_project_sa_service_list) | **GET** /iam/project/{projectId}/sa/{saId}/service | List iam/sa.service
[**iam_project_sa_tag_create**](IamProjectSaApi.md#iam_project_sa_tag_create) | **POST** /iam/project/{projectId}/sa/{saId}/tag | Create iam/sa.tag
[**iam_project_sa_tag_delete**](IamProjectSaApi.md#iam_project_sa_tag_delete) | **DELETE** /iam/project/{projectId}/sa/{saId}/tag/{tagId} | Delete iam/sa.tag
[**iam_project_sa_tag_get**](IamProjectSaApi.md#iam_project_sa_tag_get) | **GET** /iam/project/{projectId}/sa/{saId}/tag/{tagId} | Get iam/sa.tag
[**iam_project_sa_tag_list**](IamProjectSaApi.md#iam_project_sa_tag_list) | **GET** /iam/project/{projectId}/sa/{saId}/tag | List iam/sa.tag
[**iam_project_sa_tag_put**](IamProjectSaApi.md#iam_project_sa_tag_put) | **PUT** /iam/project/{projectId}/sa/{saId}/tag | Replace iam/sa.tag
[**iam_project_sa_update**](IamProjectSaApi.md#iam_project_sa_update) | **PATCH** /iam/project/{projectId}/sa/{saId} | Update iam/sa


# **iam_project_sa_create**
> Sa iam_project_sa_create(project_id, iam_project_sa_create)

Create iam/sa

Create sa

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
from h1.model.iam_project_sa_create import IamProjectSaCreate
from h1.model.sa import Sa
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    iam_project_sa_create = IamProjectSaCreate(
        name="name_example",
        service="5e5fc76ff1fb3efe1842336a",
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # IamProjectSaCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create iam/sa
        api_response = api_instance.iam_project_sa_create(project_id, iam_project_sa_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create iam/sa
        api_response = api_instance.iam_project_sa_create(project_id, iam_project_sa_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **iam_project_sa_create** | [**IamProjectSaCreate**](IamProjectSaCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Sa**](Sa.md)

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

# **iam_project_sa_credential_create**
> SaCredential iam_project_sa_credential_create(project_id, sa_id, sa_credential)

Create iam/sa.credential

Create iam/sa.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
from h1.model.sa_credential import SaCredential
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id
    sa_credential = SaCredential(
        id="id_example",
        name="name_example",
        created_by="created_by_example",
        created_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
        type="ssh",
        value="value_example",
        fingerprint="fingerprint_example",
        token="token_example",
    ) # SaCredential | 

    # example passing only required values which don't have defaults set
    try:
        # Create iam/sa.credential
        api_response = api_instance.iam_project_sa_credential_create(project_id, sa_id, sa_credential)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_credential_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |
 **sa_credential** | [**SaCredential**](SaCredential.md)|  |

### Return type

[**SaCredential**](SaCredential.md)

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

# **iam_project_sa_credential_delete**
> Sa iam_project_sa_credential_delete(project_id, sa_id, credential_id)

Delete iam/sa.credential

Delete iam/sa.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
from h1.model.sa import Sa
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/sa.credential
        api_response = api_instance.iam_project_sa_credential_delete(project_id, sa_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_credential_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |
 **credential_id** | **str**| credentialId |

### Return type

[**Sa**](Sa.md)

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

# **iam_project_sa_credential_get**
> SaCredential iam_project_sa_credential_get(project_id, sa_id, credential_id)

Get iam/sa.credential

Get iam/sa.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
from h1.model.sa_credential import SaCredential
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/sa.credential
        api_response = api_instance.iam_project_sa_credential_get(project_id, sa_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_credential_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |
 **credential_id** | **str**| credentialId |

### Return type

[**SaCredential**](SaCredential.md)

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

# **iam_project_sa_credential_list**
> [SaCredential] iam_project_sa_credential_list(project_id, sa_id)

List iam/sa.credential

List iam/sa.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
from h1.model.sa_credential import SaCredential
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/sa.credential
        api_response = api_instance.iam_project_sa_credential_list(project_id, sa_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_credential_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |

### Return type

[**[SaCredential]**](SaCredential.md)

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

# **iam_project_sa_credential_patch**
> SaCredential iam_project_sa_credential_patch(project_id, sa_id, credential_id, iam_project_sa_credential_patch)

Update iam/sa.credential

Update iam/sa.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
from h1.model.iam_project_sa_credential_patch import IamProjectSaCredentialPatch
from h1.model.sa_credential import SaCredential
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id
    credential_id = "credentialId_example" # str | credentialId
    iam_project_sa_credential_patch = IamProjectSaCredentialPatch(
        name="name_example",
    ) # IamProjectSaCredentialPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update iam/sa.credential
        api_response = api_instance.iam_project_sa_credential_patch(project_id, sa_id, credential_id, iam_project_sa_credential_patch)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_credential_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |
 **credential_id** | **str**| credentialId |
 **iam_project_sa_credential_patch** | [**IamProjectSaCredentialPatch**](IamProjectSaCredentialPatch.md)|  |

### Return type

[**SaCredential**](SaCredential.md)

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

# **iam_project_sa_delete**
> iam_project_sa_delete(project_id, sa_id)

Delete iam/sa

Delete sa

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/sa
        api_instance.iam_project_sa_delete(project_id, sa_id)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |

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

# **iam_project_sa_event_get**
> Event iam_project_sa_event_get(project_id, sa_id, event_id)

Get iam/sa.event

Get iam/sa.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/sa.event
        api_response = api_instance.iam_project_sa_event_get(project_id, sa_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_event_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |
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

# **iam_project_sa_event_list**
> [Event] iam_project_sa_event_list(project_id, sa_id)

List iam/sa.event

List iam/sa.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List iam/sa.event
        api_response = api_instance.iam_project_sa_event_list(project_id, sa_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/sa.event
        api_response = api_instance.iam_project_sa_event_list(project_id, sa_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |
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

# **iam_project_sa_get**
> Sa iam_project_sa_get(project_id, sa_id)

Get iam/sa

Returns a single sa

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
from h1.model.sa import Sa
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id

    # example passing only required values which don't have defaults set
    try:
        # Get iam/sa
        api_response = api_instance.iam_project_sa_get(project_id, sa_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |

### Return type

[**Sa**](Sa.md)

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

# **iam_project_sa_list**
> [Sa] iam_project_sa_list(project_id)

List iam/sa

List sa

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
from h1.model.sa import Sa
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List iam/sa
        api_response = api_instance.iam_project_sa_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/sa
        api_response = api_instance.iam_project_sa_list(project_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **name** | **str**| Filter by name | [optional]
 **tag_value** | **str**| Filter by tag.value | [optional]
 **tag_key** | **str**| Filter by tag.key | [optional]

### Return type

[**[Sa]**](Sa.md)

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

# **iam_project_sa_service_get**
> ResourceService iam_project_sa_service_get(project_id, sa_id, service_id)

Get iam/sa.service

Get iam/sa.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/sa.service
        api_response = api_instance.iam_project_sa_service_get(project_id, sa_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |
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

# **iam_project_sa_service_list**
> [ResourceService] iam_project_sa_service_list(project_id, sa_id)

List iam/sa.service

List iam/sa.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/sa.service
        api_response = api_instance.iam_project_sa_service_list(project_id, sa_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |

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

# **iam_project_sa_tag_create**
> Tag iam_project_sa_tag_create(project_id, sa_id, tag)

Create iam/sa.tag

Create iam/sa.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create iam/sa.tag
        api_response = api_instance.iam_project_sa_tag_create(project_id, sa_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_tag_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |
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

# **iam_project_sa_tag_delete**
> iam_project_sa_tag_delete(project_id, sa_id, tag_id)

Delete iam/sa.tag

Delete iam/sa.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/sa.tag
        api_instance.iam_project_sa_tag_delete(project_id, sa_id, tag_id)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_tag_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |
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

# **iam_project_sa_tag_get**
> Tag iam_project_sa_tag_get(project_id, sa_id, tag_id)

Get iam/sa.tag

Get iam/sa.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/sa.tag
        api_response = api_instance.iam_project_sa_tag_get(project_id, sa_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_tag_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |
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

# **iam_project_sa_tag_list**
> [Tag] iam_project_sa_tag_list(project_id, sa_id)

List iam/sa.tag

List iam/sa.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/sa.tag
        api_response = api_instance.iam_project_sa_tag_list(project_id, sa_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_tag_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |

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

# **iam_project_sa_tag_put**
> [Tag] iam_project_sa_tag_put(project_id, sa_id, tag_array)

Replace iam/sa.tag

Replace iam/sa.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace iam/sa.tag
        api_response = api_instance.iam_project_sa_tag_put(project_id, sa_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_tag_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |
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

# **iam_project_sa_update**
> Sa iam_project_sa_update(project_id, sa_id, iam_project_sa_update)

Update iam/sa

Returns modified sa

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_project_sa_api
from h1.model.iam_project_sa_update import IamProjectSaUpdate
from h1.model.sa import Sa
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
    api_instance = iam_project_sa_api.IamProjectSaApi(api_client)
    project_id = "projectId_example" # str | Project Id
    sa_id = "saId_example" # str | Sa Id
    iam_project_sa_update = IamProjectSaUpdate(
        name="name_example",
    ) # IamProjectSaUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update iam/sa
        api_response = api_instance.iam_project_sa_update(project_id, sa_id, iam_project_sa_update)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamProjectSaApi->iam_project_sa_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **sa_id** | **str**| Sa Id |
 **iam_project_sa_update** | [**IamProjectSaUpdate**](IamProjectSaUpdate.md)|  |

### Return type

[**Sa**](Sa.md)

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

