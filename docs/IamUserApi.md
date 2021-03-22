# h1.IamUserApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iam_user_credential_authtoken_delete**](IamUserApi.md#iam_user_credential_authtoken_delete) | **DELETE** /iam/user/{userId}/credential/authtoken/{authtokenId} | Delete iam/user.credential
[**iam_user_credential_authtoken_get**](IamUserApi.md#iam_user_credential_authtoken_get) | **GET** /iam/user/{userId}/credential/authtoken/{authtokenId} | Get iam/user.credential
[**iam_user_credential_authtoken_list**](IamUserApi.md#iam_user_credential_authtoken_list) | **GET** /iam/user/{userId}/credential/authtoken | List iam/user.credential
[**iam_user_credential_create**](IamUserApi.md#iam_user_credential_create) | **POST** /iam/user/{userId}/credential | Create iam/user.credential
[**iam_user_credential_delete**](IamUserApi.md#iam_user_credential_delete) | **DELETE** /iam/user/{userId}/credential/{credentialId} | Delete iam/user.credential
[**iam_user_credential_get**](IamUserApi.md#iam_user_credential_get) | **GET** /iam/user/{userId}/credential/{credentialId} | Get iam/user.credential
[**iam_user_credential_list**](IamUserApi.md#iam_user_credential_list) | **GET** /iam/user/{userId}/credential | List iam/user.credential
[**iam_user_credential_patch**](IamUserApi.md#iam_user_credential_patch) | **PATCH** /iam/user/{userId}/credential/{credentialId} | Update iam/user.credential
[**iam_user_get**](IamUserApi.md#iam_user_get) | **GET** /iam/user/{userId} | Get iam/user
[**iam_user_service_get**](IamUserApi.md#iam_user_service_get) | **GET** /iam/user/{userId}/service/{serviceId} | Get iam/user.service
[**iam_user_service_list**](IamUserApi.md#iam_user_service_list) | **GET** /iam/user/{userId}/service | List iam/user.service
[**iam_user_update**](IamUserApi.md#iam_user_update) | **PATCH** /iam/user/{userId} | Update iam/user


# **iam_user_credential_authtoken_delete**
> iam_user_credential_authtoken_delete(user_id, authtoken_id)

Delete iam/user.credential

Delete iam/user.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_user_api
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
    api_instance = iam_user_api.IamUserApi(api_client)
    user_id = "userId_example" # str | User Id
    authtoken_id = "authtokenId_example" # str | authtokenId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/user.credential
        api_instance.iam_user_credential_authtoken_delete(user_id, authtoken_id)
    except h1.ApiException as e:
        print("Exception when calling IamUserApi->iam_user_credential_authtoken_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id |
 **authtoken_id** | **str**| authtokenId |

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

# **iam_user_credential_authtoken_get**
> AuthToken iam_user_credential_authtoken_get(user_id, authtoken_id)

Get iam/user.credential

Get iam/user.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_user_api
from h1.model.auth_token import AuthToken
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
    api_instance = iam_user_api.IamUserApi(api_client)
    user_id = "userId_example" # str | User Id
    authtoken_id = "authtokenId_example" # str | authtokenId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/user.credential
        api_response = api_instance.iam_user_credential_authtoken_get(user_id, authtoken_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamUserApi->iam_user_credential_authtoken_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id |
 **authtoken_id** | **str**| authtokenId |

### Return type

[**AuthToken**](AuthToken.md)

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

# **iam_user_credential_authtoken_list**
> [AuthToken] iam_user_credential_authtoken_list(user_id)

List iam/user.credential

List iam/user.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_user_api
from h1.model.auth_token import AuthToken
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
    api_instance = iam_user_api.IamUserApi(api_client)
    user_id = "userId_example" # str | User Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/user.credential
        api_response = api_instance.iam_user_credential_authtoken_list(user_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamUserApi->iam_user_credential_authtoken_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id |

### Return type

[**[AuthToken]**](AuthToken.md)

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

# **iam_user_credential_create**
> UserCredential iam_user_credential_create(user_id, user_credential)

Create iam/user.credential

Create iam/user.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_user_api
from h1.model.user_credential import UserCredential
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
    api_instance = iam_user_api.IamUserApi(api_client)
    user_id = "userId_example" # str | User Id
    user_credential = UserCredential(
        id="id_example",
        name="name_example",
        created_by="created_by_example",
        created_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
        type="ssh",
        value="value_example",
        fingerprint="fingerprint_example",
        token="token_example",
    ) # UserCredential | 

    # example passing only required values which don't have defaults set
    try:
        # Create iam/user.credential
        api_response = api_instance.iam_user_credential_create(user_id, user_credential)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamUserApi->iam_user_credential_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id |
 **user_credential** | [**UserCredential**](UserCredential.md)|  |

### Return type

[**UserCredential**](UserCredential.md)

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

# **iam_user_credential_delete**
> User iam_user_credential_delete(user_id, credential_id)

Delete iam/user.credential

Delete iam/user.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_user_api
from h1.model.user import User
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
    api_instance = iam_user_api.IamUserApi(api_client)
    user_id = "userId_example" # str | User Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/user.credential
        api_response = api_instance.iam_user_credential_delete(user_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamUserApi->iam_user_credential_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id |
 **credential_id** | **str**| credentialId |

### Return type

[**User**](User.md)

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

# **iam_user_credential_get**
> UserCredential iam_user_credential_get(user_id, credential_id)

Get iam/user.credential

Get iam/user.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_user_api
from h1.model.user_credential import UserCredential
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
    api_instance = iam_user_api.IamUserApi(api_client)
    user_id = "userId_example" # str | User Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/user.credential
        api_response = api_instance.iam_user_credential_get(user_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamUserApi->iam_user_credential_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id |
 **credential_id** | **str**| credentialId |

### Return type

[**UserCredential**](UserCredential.md)

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

# **iam_user_credential_list**
> [UserCredential] iam_user_credential_list(user_id)

List iam/user.credential

List iam/user.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_user_api
from h1.model.user_credential import UserCredential
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
    api_instance = iam_user_api.IamUserApi(api_client)
    user_id = "userId_example" # str | User Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/user.credential
        api_response = api_instance.iam_user_credential_list(user_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamUserApi->iam_user_credential_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id |

### Return type

[**[UserCredential]**](UserCredential.md)

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

# **iam_user_credential_patch**
> UserCredential iam_user_credential_patch(user_id, credential_id, iam_user_credential_patch)

Update iam/user.credential

Update iam/user.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_user_api
from h1.model.iam_user_credential_patch import IamUserCredentialPatch
from h1.model.user_credential import UserCredential
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
    api_instance = iam_user_api.IamUserApi(api_client)
    user_id = "userId_example" # str | User Id
    credential_id = "credentialId_example" # str | credentialId
    iam_user_credential_patch = IamUserCredentialPatch(
        name="name_example",
    ) # IamUserCredentialPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update iam/user.credential
        api_response = api_instance.iam_user_credential_patch(user_id, credential_id, iam_user_credential_patch)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamUserApi->iam_user_credential_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id |
 **credential_id** | **str**| credentialId |
 **iam_user_credential_patch** | [**IamUserCredentialPatch**](IamUserCredentialPatch.md)|  |

### Return type

[**UserCredential**](UserCredential.md)

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

# **iam_user_get**
> User iam_user_get(user_id)

Get iam/user

Returns a single user

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_user_api
from h1.model.user import User
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
    api_instance = iam_user_api.IamUserApi(api_client)
    user_id = "userId_example" # str | User Id

    # example passing only required values which don't have defaults set
    try:
        # Get iam/user
        api_response = api_instance.iam_user_get(user_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamUserApi->iam_user_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id |

### Return type

[**User**](User.md)

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

# **iam_user_service_get**
> ResourceService iam_user_service_get(user_id, service_id)

Get iam/user.service

Get iam/user.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_user_api
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
    api_instance = iam_user_api.IamUserApi(api_client)
    user_id = "userId_example" # str | User Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/user.service
        api_response = api_instance.iam_user_service_get(user_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamUserApi->iam_user_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id |
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

# **iam_user_service_list**
> [ResourceService] iam_user_service_list(user_id)

List iam/user.service

List iam/user.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_user_api
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
    api_instance = iam_user_api.IamUserApi(api_client)
    user_id = "userId_example" # str | User Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/user.service
        api_response = api_instance.iam_user_service_list(user_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamUserApi->iam_user_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id |

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

# **iam_user_update**
> User iam_user_update(user_id, iam_user_update)

Update iam/user

Returns modified user

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_user_api
from h1.model.iam_user_update import IamUserUpdate
from h1.model.user import User
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
    api_instance = iam_user_api.IamUserApi(api_client)
    user_id = "userId_example" # str | User Id
    iam_user_update = IamUserUpdate(
        phone="phone_example",
        first_name="first_name_example",
        family_name="family_name_example",
        lang="en",
    ) # IamUserUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update iam/user
        api_response = api_instance.iam_user_update(user_id, iam_user_update)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamUserApi->iam_user_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id |
 **iam_user_update** | [**IamUserUpdate**](IamUserUpdate.md)|  |

### Return type

[**User**](User.md)

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

