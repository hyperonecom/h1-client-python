# h1.ContainerProjectRegistryApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**container_project_registry_create**](ContainerProjectRegistryApi.md#container_project_registry_create) | **POST** /container/{locationId}/project/{projectId}/registry | Create container/registry
[**container_project_registry_credential_create**](ContainerProjectRegistryApi.md#container_project_registry_credential_create) | **POST** /container/{locationId}/project/{projectId}/registry/{registryId}/credential | Create container/registry.credential
[**container_project_registry_credential_delete**](ContainerProjectRegistryApi.md#container_project_registry_credential_delete) | **DELETE** /container/{locationId}/project/{projectId}/registry/{registryId}/credential/{credentialId} | Delete container/registry.credential
[**container_project_registry_credential_get**](ContainerProjectRegistryApi.md#container_project_registry_credential_get) | **GET** /container/{locationId}/project/{projectId}/registry/{registryId}/credential/{credentialId} | Get container/registry.credential
[**container_project_registry_credential_list**](ContainerProjectRegistryApi.md#container_project_registry_credential_list) | **GET** /container/{locationId}/project/{projectId}/registry/{registryId}/credential | List container/registry.credential
[**container_project_registry_credential_patch**](ContainerProjectRegistryApi.md#container_project_registry_credential_patch) | **PATCH** /container/{locationId}/project/{projectId}/registry/{registryId}/credential/{credentialId} | Update container/registry.credential
[**container_project_registry_delete**](ContainerProjectRegistryApi.md#container_project_registry_delete) | **DELETE** /container/{locationId}/project/{projectId}/registry/{registryId} | Delete container/registry
[**container_project_registry_domain_create**](ContainerProjectRegistryApi.md#container_project_registry_domain_create) | **POST** /container/{locationId}/project/{projectId}/registry/{registryId}/domain | Create container/registry.domain
[**container_project_registry_domain_delete**](ContainerProjectRegistryApi.md#container_project_registry_domain_delete) | **DELETE** /container/{locationId}/project/{projectId}/registry/{registryId}/domain/{domainId} | Delete container/registry.domain
[**container_project_registry_domain_get**](ContainerProjectRegistryApi.md#container_project_registry_domain_get) | **GET** /container/{locationId}/project/{projectId}/registry/{registryId}/domain/{domainId} | Get container/registry.domain
[**container_project_registry_domain_list**](ContainerProjectRegistryApi.md#container_project_registry_domain_list) | **GET** /container/{locationId}/project/{projectId}/registry/{registryId}/domain | List container/registry.domain
[**container_project_registry_event_get**](ContainerProjectRegistryApi.md#container_project_registry_event_get) | **GET** /container/{locationId}/project/{projectId}/registry/{registryId}/event/{eventId} | Get container/registry.event
[**container_project_registry_event_list**](ContainerProjectRegistryApi.md#container_project_registry_event_list) | **GET** /container/{locationId}/project/{projectId}/registry/{registryId}/event | List container/registry.event
[**container_project_registry_get**](ContainerProjectRegistryApi.md#container_project_registry_get) | **GET** /container/{locationId}/project/{projectId}/registry/{registryId} | Get container/registry
[**container_project_registry_list**](ContainerProjectRegistryApi.md#container_project_registry_list) | **GET** /container/{locationId}/project/{projectId}/registry | List container/registry
[**container_project_registry_repository_get**](ContainerProjectRegistryApi.md#container_project_registry_repository_get) | **GET** /container/{locationId}/project/{projectId}/registry/{registryId}/repository/{repositoryId} | Get container/registry.repository
[**container_project_registry_repository_image_delete**](ContainerProjectRegistryApi.md#container_project_registry_repository_image_delete) | **DELETE** /container/{locationId}/project/{projectId}/registry/{registryId}/repository/{repositoryId}/image/{imageId} | Delete container/registry.image
[**container_project_registry_repository_image_get**](ContainerProjectRegistryApi.md#container_project_registry_repository_image_get) | **GET** /container/{locationId}/project/{projectId}/registry/{registryId}/repository/{repositoryId}/image/{imageId} | Get container/registry.image
[**container_project_registry_repository_image_list**](ContainerProjectRegistryApi.md#container_project_registry_repository_image_list) | **GET** /container/{locationId}/project/{projectId}/registry/{registryId}/repository/{repositoryId}/image | List container/registry.image
[**container_project_registry_repository_list**](ContainerProjectRegistryApi.md#container_project_registry_repository_list) | **GET** /container/{locationId}/project/{projectId}/registry/{registryId}/repository | List container/registry.repository
[**container_project_registry_service_get**](ContainerProjectRegistryApi.md#container_project_registry_service_get) | **GET** /container/{locationId}/project/{projectId}/registry/{registryId}/service/{serviceId} | Get container/registry.service
[**container_project_registry_service_list**](ContainerProjectRegistryApi.md#container_project_registry_service_list) | **GET** /container/{locationId}/project/{projectId}/registry/{registryId}/service | List container/registry.service
[**container_project_registry_start**](ContainerProjectRegistryApi.md#container_project_registry_start) | **POST** /container/{locationId}/project/{projectId}/registry/{registryId}/actions/start | Start container/registry
[**container_project_registry_stop**](ContainerProjectRegistryApi.md#container_project_registry_stop) | **POST** /container/{locationId}/project/{projectId}/registry/{registryId}/actions/stop | Stop container/registry
[**container_project_registry_tag_create**](ContainerProjectRegistryApi.md#container_project_registry_tag_create) | **POST** /container/{locationId}/project/{projectId}/registry/{registryId}/tag | Create container/registry.tag
[**container_project_registry_tag_delete**](ContainerProjectRegistryApi.md#container_project_registry_tag_delete) | **DELETE** /container/{locationId}/project/{projectId}/registry/{registryId}/tag/{tagId} | Delete container/registry.tag
[**container_project_registry_tag_get**](ContainerProjectRegistryApi.md#container_project_registry_tag_get) | **GET** /container/{locationId}/project/{projectId}/registry/{registryId}/tag/{tagId} | Get container/registry.tag
[**container_project_registry_tag_list**](ContainerProjectRegistryApi.md#container_project_registry_tag_list) | **GET** /container/{locationId}/project/{projectId}/registry/{registryId}/tag | List container/registry.tag
[**container_project_registry_tag_put**](ContainerProjectRegistryApi.md#container_project_registry_tag_put) | **PUT** /container/{locationId}/project/{projectId}/registry/{registryId}/tag | Replace container/registry.tag
[**container_project_registry_transfer**](ContainerProjectRegistryApi.md#container_project_registry_transfer) | **POST** /container/{locationId}/project/{projectId}/registry/{registryId}/actions/transfer | Transfer container/registry
[**container_project_registry_update**](ContainerProjectRegistryApi.md#container_project_registry_update) | **PATCH** /container/{locationId}/project/{projectId}/registry/{registryId} | Update container/registry


# **container_project_registry_create**
> Registry container_project_registry_create(project_id, location_id, container_project_registry_create, x_idempotency_key=x_idempotency_key)

Create container/registry

Create registry

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
container_project_registry_create = h1.ContainerProjectRegistryCreate() # ContainerProjectRegistryCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create container/registry
        api_response = api_instance.container_project_registry_create(project_id, location_id, container_project_registry_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **container_project_registry_create** | [**ContainerProjectRegistryCreate**](ContainerProjectRegistryCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Registry**](Registry.md)

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

# **container_project_registry_credential_create**
> RegistryCredential container_project_registry_credential_create(project_id, location_id, registry_id, registry_credential)

Create container/registry.credential

Create container/registry.credential

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
registry_credential = h1.RegistryCredential() # RegistryCredential | 

    try:
        # Create container/registry.credential
        api_response = api_instance.container_project_registry_credential_create(project_id, location_id, registry_id, registry_credential)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_credential_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
 **registry_credential** | [**RegistryCredential**](RegistryCredential.md)|  | 

### Return type

[**RegistryCredential**](RegistryCredential.md)

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

# **container_project_registry_credential_delete**
> Registry container_project_registry_credential_delete(project_id, location_id, registry_id, credential_id)

Delete container/registry.credential

Delete container/registry.credential

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
credential_id = 'credential_id_example' # str | credentialId

    try:
        # Delete container/registry.credential
        api_response = api_instance.container_project_registry_credential_delete(project_id, location_id, registry_id, credential_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_credential_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
 **credential_id** | **str**| credentialId | 

### Return type

[**Registry**](Registry.md)

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

# **container_project_registry_credential_get**
> RegistryCredential container_project_registry_credential_get(project_id, location_id, registry_id, credential_id)

Get container/registry.credential

Get container/registry.credential

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
credential_id = 'credential_id_example' # str | credentialId

    try:
        # Get container/registry.credential
        api_response = api_instance.container_project_registry_credential_get(project_id, location_id, registry_id, credential_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_credential_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
 **credential_id** | **str**| credentialId | 

### Return type

[**RegistryCredential**](RegistryCredential.md)

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

# **container_project_registry_credential_list**
> list[RegistryCredential] container_project_registry_credential_list(project_id, location_id, registry_id)

List container/registry.credential

List container/registry.credential

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id

    try:
        # List container/registry.credential
        api_response = api_instance.container_project_registry_credential_list(project_id, location_id, registry_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_credential_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 

### Return type

[**list[RegistryCredential]**](RegistryCredential.md)

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

# **container_project_registry_credential_patch**
> RegistryCredential container_project_registry_credential_patch(project_id, location_id, registry_id, credential_id, container_project_registry_credential_patch)

Update container/registry.credential

Update container/registry.credential

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
credential_id = 'credential_id_example' # str | credentialId
container_project_registry_credential_patch = h1.ContainerProjectRegistryCredentialPatch() # ContainerProjectRegistryCredentialPatch | 

    try:
        # Update container/registry.credential
        api_response = api_instance.container_project_registry_credential_patch(project_id, location_id, registry_id, credential_id, container_project_registry_credential_patch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_credential_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
 **credential_id** | **str**| credentialId | 
 **container_project_registry_credential_patch** | [**ContainerProjectRegistryCredentialPatch**](ContainerProjectRegistryCredentialPatch.md)|  | 

### Return type

[**RegistryCredential**](RegistryCredential.md)

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

# **container_project_registry_delete**
> container_project_registry_delete(project_id, location_id, registry_id)

Delete container/registry

Delete registry

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id

    try:
        # Delete container/registry
        api_instance.container_project_registry_delete(project_id, location_id, registry_id)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 

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

# **container_project_registry_domain_create**
> Domain container_project_registry_domain_create(project_id, location_id, registry_id, domain)

Create container/registry.domain

Create container/registry.domain

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
domain = h1.Domain() # Domain | 

    try:
        # Create container/registry.domain
        api_response = api_instance.container_project_registry_domain_create(project_id, location_id, registry_id, domain)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_domain_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
 **domain** | [**Domain**](Domain.md)|  | 

### Return type

[**Domain**](Domain.md)

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

# **container_project_registry_domain_delete**
> container_project_registry_domain_delete(project_id, location_id, registry_id, domain_id)

Delete container/registry.domain

Delete container/registry.domain

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
domain_id = 'domain_id_example' # str | domainId

    try:
        # Delete container/registry.domain
        api_instance.container_project_registry_domain_delete(project_id, location_id, registry_id, domain_id)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_domain_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
 **domain_id** | **str**| domainId | 

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

# **container_project_registry_domain_get**
> Domain container_project_registry_domain_get(project_id, location_id, registry_id, domain_id)

Get container/registry.domain

Get container/registry.domain

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
domain_id = 'domain_id_example' # str | domainId

    try:
        # Get container/registry.domain
        api_response = api_instance.container_project_registry_domain_get(project_id, location_id, registry_id, domain_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_domain_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
 **domain_id** | **str**| domainId | 

### Return type

[**Domain**](Domain.md)

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

# **container_project_registry_domain_list**
> list[Domain] container_project_registry_domain_list(project_id, location_id, registry_id)

List container/registry.domain

List container/registry.domain

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id

    try:
        # List container/registry.domain
        api_response = api_instance.container_project_registry_domain_list(project_id, location_id, registry_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_domain_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 

### Return type

[**list[Domain]**](Domain.md)

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

# **container_project_registry_event_get**
> Event container_project_registry_event_get(project_id, location_id, registry_id, event_id)

Get container/registry.event

Get container/registry.event

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get container/registry.event
        api_response = api_instance.container_project_registry_event_get(project_id, location_id, registry_id, event_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
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

# **container_project_registry_event_list**
> list[Event] container_project_registry_event_list(project_id, location_id, registry_id, limit=limit, skip=skip)

List container/registry.event

List container/registry.event

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List container/registry.event
        api_response = api_instance.container_project_registry_event_list(project_id, location_id, registry_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
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

# **container_project_registry_get**
> Registry container_project_registry_get(project_id, location_id, registry_id)

Get container/registry

Returns a single registry

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id

    try:
        # Get container/registry
        api_response = api_instance.container_project_registry_get(project_id, location_id, registry_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 

### Return type

[**Registry**](Registry.md)

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

# **container_project_registry_list**
> list[Registry] container_project_registry_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)

List container/registry

List registry

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
name = 'name_example' # str | Filter by name (optional)
tag_value = 'tag_value_example' # str | Filter by tag.value (optional)
tag_key = 'tag_key_example' # str | Filter by tag.key (optional)

    try:
        # List container/registry
        api_response = api_instance.container_project_registry_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_list: %s\n" % e)
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

[**list[Registry]**](Registry.md)

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

# **container_project_registry_repository_get**
> ContainerRepository container_project_registry_repository_get(project_id, location_id, registry_id, repository_id)

Get container/registry.repository

Get container/registry.repository

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
repository_id = 'repository_id_example' # str | repositoryId

    try:
        # Get container/registry.repository
        api_response = api_instance.container_project_registry_repository_get(project_id, location_id, registry_id, repository_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_repository_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
 **repository_id** | **str**| repositoryId | 

### Return type

[**ContainerRepository**](ContainerRepository.md)

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

# **container_project_registry_repository_image_delete**
> container_project_registry_repository_image_delete(project_id, location_id, registry_id, repository_id, image_id)

Delete container/registry.image

Delete container/registry.image

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
repository_id = 'repository_id_example' # str | repositoryId
image_id = 'image_id_example' # str | imageId

    try:
        # Delete container/registry.image
        api_instance.container_project_registry_repository_image_delete(project_id, location_id, registry_id, repository_id, image_id)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_repository_image_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
 **repository_id** | **str**| repositoryId | 
 **image_id** | **str**| imageId | 

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

# **container_project_registry_repository_image_get**
> ContainerImage container_project_registry_repository_image_get(project_id, location_id, registry_id, repository_id, image_id)

Get container/registry.image

Get container/registry.image

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
repository_id = 'repository_id_example' # str | repositoryId
image_id = 'image_id_example' # str | imageId

    try:
        # Get container/registry.image
        api_response = api_instance.container_project_registry_repository_image_get(project_id, location_id, registry_id, repository_id, image_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_repository_image_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
 **repository_id** | **str**| repositoryId | 
 **image_id** | **str**| imageId | 

### Return type

[**ContainerImage**](ContainerImage.md)

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

# **container_project_registry_repository_image_list**
> list[ContainerImage] container_project_registry_repository_image_list(project_id, location_id, registry_id, repository_id)

List container/registry.image

List container/registry.image

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
repository_id = 'repository_id_example' # str | repositoryId

    try:
        # List container/registry.image
        api_response = api_instance.container_project_registry_repository_image_list(project_id, location_id, registry_id, repository_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_repository_image_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
 **repository_id** | **str**| repositoryId | 

### Return type

[**list[ContainerImage]**](ContainerImage.md)

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

# **container_project_registry_repository_list**
> list[ContainerRepository] container_project_registry_repository_list(project_id, location_id, registry_id)

List container/registry.repository

List container/registry.repository

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id

    try:
        # List container/registry.repository
        api_response = api_instance.container_project_registry_repository_list(project_id, location_id, registry_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_repository_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 

### Return type

[**list[ContainerRepository]**](ContainerRepository.md)

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

# **container_project_registry_service_get**
> ResourceService container_project_registry_service_get(project_id, location_id, registry_id, service_id)

Get container/registry.service

Get container/registry.service

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
service_id = 'service_id_example' # str | serviceId

    try:
        # Get container/registry.service
        api_response = api_instance.container_project_registry_service_get(project_id, location_id, registry_id, service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
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

# **container_project_registry_service_list**
> list[ResourceService] container_project_registry_service_list(project_id, location_id, registry_id)

List container/registry.service

List container/registry.service

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id

    try:
        # List container/registry.service
        api_response = api_instance.container_project_registry_service_list(project_id, location_id, registry_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 

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

# **container_project_registry_start**
> Registry container_project_registry_start(project_id, location_id, registry_id, x_idempotency_key=x_idempotency_key)

Start container/registry

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Start container/registry
        api_response = api_instance.container_project_registry_start(project_id, location_id, registry_id, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Registry**](Registry.md)

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

# **container_project_registry_stop**
> Registry container_project_registry_stop(project_id, location_id, registry_id, x_idempotency_key=x_idempotency_key)

Stop container/registry

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Stop container/registry
        api_response = api_instance.container_project_registry_stop(project_id, location_id, registry_id, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Registry**](Registry.md)

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

# **container_project_registry_tag_create**
> Tag container_project_registry_tag_create(project_id, location_id, registry_id, tag)

Create container/registry.tag

Create container/registry.tag

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
tag = h1.Tag() # Tag | 

    try:
        # Create container/registry.tag
        api_response = api_instance.container_project_registry_tag_create(project_id, location_id, registry_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
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

# **container_project_registry_tag_delete**
> container_project_registry_tag_delete(project_id, location_id, registry_id, tag_id)

Delete container/registry.tag

Delete container/registry.tag

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Delete container/registry.tag
        api_instance.container_project_registry_tag_delete(project_id, location_id, registry_id, tag_id)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
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

# **container_project_registry_tag_get**
> Tag container_project_registry_tag_get(project_id, location_id, registry_id, tag_id)

Get container/registry.tag

Get container/registry.tag

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Get container/registry.tag
        api_response = api_instance.container_project_registry_tag_get(project_id, location_id, registry_id, tag_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
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

# **container_project_registry_tag_list**
> list[Tag] container_project_registry_tag_list(project_id, location_id, registry_id)

List container/registry.tag

List container/registry.tag

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id

    try:
        # List container/registry.tag
        api_response = api_instance.container_project_registry_tag_list(project_id, location_id, registry_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 

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

# **container_project_registry_tag_put**
> list[Tag] container_project_registry_tag_put(project_id, location_id, registry_id, tag)

Replace container/registry.tag

Replace container/registry.tag

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
tag = [h1.Tag()] # list[Tag] | 

    try:
        # Replace container/registry.tag
        api_response = api_instance.container_project_registry_tag_put(project_id, location_id, registry_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
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

# **container_project_registry_transfer**
> Registry container_project_registry_transfer(project_id, location_id, registry_id, container_project_registry_transfer, x_idempotency_key=x_idempotency_key)

Transfer container/registry

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
container_project_registry_transfer = h1.ContainerProjectRegistryTransfer() # ContainerProjectRegistryTransfer | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Transfer container/registry
        api_response = api_instance.container_project_registry_transfer(project_id, location_id, registry_id, container_project_registry_transfer, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
 **container_project_registry_transfer** | [**ContainerProjectRegistryTransfer**](ContainerProjectRegistryTransfer.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Registry**](Registry.md)

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

# **container_project_registry_update**
> Registry container_project_registry_update(project_id, location_id, registry_id, container_project_registry_update)

Update container/registry

Returns modified registry

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
    api_instance = h1.ContainerProjectRegistryApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
registry_id = 'registry_id_example' # str | Registry Id
container_project_registry_update = h1.ContainerProjectRegistryUpdate() # ContainerProjectRegistryUpdate | 

    try:
        # Update container/registry
        api_response = api_instance.container_project_registry_update(project_id, location_id, registry_id, container_project_registry_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **registry_id** | **str**| Registry Id | 
 **container_project_registry_update** | [**ContainerProjectRegistryUpdate**](ContainerProjectRegistryUpdate.md)|  | 

### Return type

[**Registry**](Registry.md)

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

