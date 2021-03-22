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
> Registry container_project_registry_create(project_id, location_id, container_project_registry_create)

Create container/registry

Create registry

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import container_project_registry_api
from h1.model.registry import Registry
from h1.model.container_project_registry_create import ContainerProjectRegistryCreate
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    container_project_registry_create = ContainerProjectRegistryCreate(
        name="name_example",
        service="service_example",
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # ContainerProjectRegistryCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create container/registry
        api_response = api_instance.container_project_registry_create(project_id, location_id, container_project_registry_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create container/registry
        api_response = api_instance.container_project_registry_create(project_id, location_id, container_project_registry_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **container_project_registry_create** | [**ContainerProjectRegistryCreate**](ContainerProjectRegistryCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import container_project_registry_api
from h1.model.registry_credential import RegistryCredential
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    registry_credential = RegistryCredential(
        id="id_example",
        name="name_example",
        created_by="created_by_example",
        created_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
        type="sha512",
        value="value_example",
        fingerprint="fingerprint_example",
        token="token_example",
    ) # RegistryCredential | 

    # example passing only required values which don't have defaults set
    try:
        # Create container/registry.credential
        api_response = api_instance.container_project_registry_credential_create(project_id, location_id, registry_id, registry_credential)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import container_project_registry_api
from h1.model.registry import Registry
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Delete container/registry.credential
        api_response = api_instance.container_project_registry_credential_delete(project_id, location_id, registry_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import container_project_registry_api
from h1.model.registry_credential import RegistryCredential
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Get container/registry.credential
        api_response = api_instance.container_project_registry_credential_get(project_id, location_id, registry_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [RegistryCredential] container_project_registry_credential_list(project_id, location_id, registry_id)

List container/registry.credential

List container/registry.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import container_project_registry_api
from h1.model.registry_credential import RegistryCredential
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id

    # example passing only required values which don't have defaults set
    try:
        # List container/registry.credential
        api_response = api_instance.container_project_registry_credential_list(project_id, location_id, registry_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_credential_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **registry_id** | **str**| Registry Id |

### Return type

[**[RegistryCredential]**](RegistryCredential.md)

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
import time
import h1
from h1.api import container_project_registry_api
from h1.model.registry_credential import RegistryCredential
from h1.model.container_project_registry_credential_patch import ContainerProjectRegistryCredentialPatch
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    credential_id = "credentialId_example" # str | credentialId
    container_project_registry_credential_patch = ContainerProjectRegistryCredentialPatch(
        name="name_example",
    ) # ContainerProjectRegistryCredentialPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update container/registry.credential
        api_response = api_instance.container_project_registry_credential_patch(project_id, location_id, registry_id, credential_id, container_project_registry_credential_patch)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import container_project_registry_api
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id

    # example passing only required values which don't have defaults set
    try:
        # Delete container/registry
        api_instance.container_project_registry_delete(project_id, location_id, registry_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import container_project_registry_api
from h1.model.domain import Domain
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    domain = Domain(
        id="id_example",
        value="value_example",
    ) # Domain | 

    # example passing only required values which don't have defaults set
    try:
        # Create container/registry.domain
        api_response = api_instance.container_project_registry_domain_create(project_id, location_id, registry_id, domain)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import container_project_registry_api
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    domain_id = "domainId_example" # str | domainId

    # example passing only required values which don't have defaults set
    try:
        # Delete container/registry.domain
        api_instance.container_project_registry_domain_delete(project_id, location_id, registry_id, domain_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import container_project_registry_api
from h1.model.domain import Domain
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    domain_id = "domainId_example" # str | domainId

    # example passing only required values which don't have defaults set
    try:
        # Get container/registry.domain
        api_response = api_instance.container_project_registry_domain_get(project_id, location_id, registry_id, domain_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Domain] container_project_registry_domain_list(project_id, location_id, registry_id)

List container/registry.domain

List container/registry.domain

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import container_project_registry_api
from h1.model.domain import Domain
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id

    # example passing only required values which don't have defaults set
    try:
        # List container/registry.domain
        api_response = api_instance.container_project_registry_domain_list(project_id, location_id, registry_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_domain_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **registry_id** | **str**| Registry Id |

### Return type

[**[Domain]**](Domain.md)

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
import time
import h1
from h1.api import container_project_registry_api
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get container/registry.event
        api_response = api_instance.container_project_registry_event_get(project_id, location_id, registry_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Event] container_project_registry_event_list(project_id, location_id, registry_id)

List container/registry.event

List container/registry.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import container_project_registry_api
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List container/registry.event
        api_response = api_instance.container_project_registry_event_list(project_id, location_id, registry_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List container/registry.event
        api_response = api_instance.container_project_registry_event_list(project_id, location_id, registry_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **registry_id** | **str**| Registry Id |
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

# **container_project_registry_get**
> Registry container_project_registry_get(project_id, location_id, registry_id)

Get container/registry

Returns a single registry

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import container_project_registry_api
from h1.model.registry import Registry
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id

    # example passing only required values which don't have defaults set
    try:
        # Get container/registry
        api_response = api_instance.container_project_registry_get(project_id, location_id, registry_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Registry] container_project_registry_list(project_id, location_id)

List container/registry

List registry

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import container_project_registry_api
from h1.model.registry import Registry
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List container/registry
        api_response = api_instance.container_project_registry_list(project_id, location_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List container/registry
        api_response = api_instance.container_project_registry_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
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

[**[Registry]**](Registry.md)

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
import time
import h1
from h1.api import container_project_registry_api
from h1.model.container_repository import ContainerRepository
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    repository_id = "repositoryId_example" # str | repositoryId

    # example passing only required values which don't have defaults set
    try:
        # Get container/registry.repository
        api_response = api_instance.container_project_registry_repository_get(project_id, location_id, registry_id, repository_id)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import container_project_registry_api
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    repository_id = "repositoryId_example" # str | repositoryId
    image_id = "imageId_example" # str | imageId

    # example passing only required values which don't have defaults set
    try:
        # Delete container/registry.image
        api_instance.container_project_registry_repository_image_delete(project_id, location_id, registry_id, repository_id, image_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import container_project_registry_api
from h1.model.container_image import ContainerImage
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    repository_id = "repositoryId_example" # str | repositoryId
    image_id = "imageId_example" # str | imageId

    # example passing only required values which don't have defaults set
    try:
        # Get container/registry.image
        api_response = api_instance.container_project_registry_repository_image_get(project_id, location_id, registry_id, repository_id, image_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [ContainerImage] container_project_registry_repository_image_list(project_id, location_id, registry_id, repository_id)

List container/registry.image

List container/registry.image

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import container_project_registry_api
from h1.model.container_image import ContainerImage
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    repository_id = "repositoryId_example" # str | repositoryId

    # example passing only required values which don't have defaults set
    try:
        # List container/registry.image
        api_response = api_instance.container_project_registry_repository_image_list(project_id, location_id, registry_id, repository_id)
        pprint(api_response)
    except h1.ApiException as e:
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

[**[ContainerImage]**](ContainerImage.md)

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
> [ContainerRepository] container_project_registry_repository_list(project_id, location_id, registry_id)

List container/registry.repository

List container/registry.repository

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import container_project_registry_api
from h1.model.container_repository import ContainerRepository
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id

    # example passing only required values which don't have defaults set
    try:
        # List container/registry.repository
        api_response = api_instance.container_project_registry_repository_list(project_id, location_id, registry_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_repository_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **registry_id** | **str**| Registry Id |

### Return type

[**[ContainerRepository]**](ContainerRepository.md)

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
import time
import h1
from h1.api import container_project_registry_api
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get container/registry.service
        api_response = api_instance.container_project_registry_service_get(project_id, location_id, registry_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [ResourceService] container_project_registry_service_list(project_id, location_id, registry_id)

List container/registry.service

List container/registry.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import container_project_registry_api
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id

    # example passing only required values which don't have defaults set
    try:
        # List container/registry.service
        api_response = api_instance.container_project_registry_service_list(project_id, location_id, registry_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **registry_id** | **str**| Registry Id |

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

# **container_project_registry_start**
> Registry container_project_registry_start(project_id, location_id, registry_id)

Start container/registry

action start

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import container_project_registry_api
from h1.model.registry import Registry
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start container/registry
        api_response = api_instance.container_project_registry_start(project_id, location_id, registry_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_start: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start container/registry
        api_response = api_instance.container_project_registry_start(project_id, location_id, registry_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_start: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **registry_id** | **str**| Registry Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

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
> Registry container_project_registry_stop(project_id, location_id, registry_id)

Stop container/registry

action stop

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import container_project_registry_api
from h1.model.registry import Registry
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Stop container/registry
        api_response = api_instance.container_project_registry_stop(project_id, location_id, registry_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_stop: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Stop container/registry
        api_response = api_instance.container_project_registry_stop(project_id, location_id, registry_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_stop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **registry_id** | **str**| Registry Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import container_project_registry_api
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create container/registry.tag
        api_response = api_instance.container_project_registry_tag_create(project_id, location_id, registry_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import container_project_registry_api
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete container/registry.tag
        api_instance.container_project_registry_tag_delete(project_id, location_id, registry_id, tag_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import container_project_registry_api
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get container/registry.tag
        api_response = api_instance.container_project_registry_tag_get(project_id, location_id, registry_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Tag] container_project_registry_tag_list(project_id, location_id, registry_id)

List container/registry.tag

List container/registry.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import container_project_registry_api
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id

    # example passing only required values which don't have defaults set
    try:
        # List container/registry.tag
        api_response = api_instance.container_project_registry_tag_list(project_id, location_id, registry_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_tag_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **registry_id** | **str**| Registry Id |

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

# **container_project_registry_tag_put**
> [Tag] container_project_registry_tag_put(project_id, location_id, registry_id, tag_array)

Replace container/registry.tag

Replace container/registry.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import container_project_registry_api
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace container/registry.tag
        api_response = api_instance.container_project_registry_tag_put(project_id, location_id, registry_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_tag_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **registry_id** | **str**| Registry Id |
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

# **container_project_registry_transfer**
> Registry container_project_registry_transfer(project_id, location_id, registry_id, container_project_registry_transfer)

Transfer container/registry

action transfer

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import container_project_registry_api
from h1.model.registry import Registry
from h1.model.container_project_registry_transfer import ContainerProjectRegistryTransfer
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    container_project_registry_transfer = ContainerProjectRegistryTransfer(
        project="project_example",
    ) # ContainerProjectRegistryTransfer | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Transfer container/registry
        api_response = api_instance.container_project_registry_transfer(project_id, location_id, registry_id, container_project_registry_transfer)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ContainerProjectRegistryApi->container_project_registry_transfer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Transfer container/registry
        api_response = api_instance.container_project_registry_transfer(project_id, location_id, registry_id, container_project_registry_transfer, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
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
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import container_project_registry_api
from h1.model.registry import Registry
from h1.model.container_project_registry_update import ContainerProjectRegistryUpdate
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
    api_instance = container_project_registry_api.ContainerProjectRegistryApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    registry_id = "registryId_example" # str | Registry Id
    container_project_registry_update = ContainerProjectRegistryUpdate(
        name="name_example",
    ) # ContainerProjectRegistryUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update container/registry
        api_response = api_instance.container_project_registry_update(project_id, location_id, registry_id, container_project_registry_update)
        pprint(api_response)
    except h1.ApiException as e:
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

