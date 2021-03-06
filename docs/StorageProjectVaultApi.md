# h1.StorageProjectVaultApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_project_vault_connect_get**](StorageProjectVaultApi.md#storage_project_vault_connect_get) | **GET** /storage/{locationId}/project/{projectId}/vault/{vaultId}/connect/{connectId} | Get storage/vault.connect
[**storage_project_vault_connect_list**](StorageProjectVaultApi.md#storage_project_vault_connect_list) | **GET** /storage/{locationId}/project/{projectId}/vault/{vaultId}/connect | List storage/vault.connect
[**storage_project_vault_create**](StorageProjectVaultApi.md#storage_project_vault_create) | **POST** /storage/{locationId}/project/{projectId}/vault | Create storage/vault
[**storage_project_vault_credential_create**](StorageProjectVaultApi.md#storage_project_vault_credential_create) | **POST** /storage/{locationId}/project/{projectId}/vault/{vaultId}/credential | Create storage/vault.credential
[**storage_project_vault_credential_delete**](StorageProjectVaultApi.md#storage_project_vault_credential_delete) | **DELETE** /storage/{locationId}/project/{projectId}/vault/{vaultId}/credential/{credentialId} | Delete storage/vault.credential
[**storage_project_vault_credential_get**](StorageProjectVaultApi.md#storage_project_vault_credential_get) | **GET** /storage/{locationId}/project/{projectId}/vault/{vaultId}/credential/{credentialId} | Get storage/vault.credential
[**storage_project_vault_credential_list**](StorageProjectVaultApi.md#storage_project_vault_credential_list) | **GET** /storage/{locationId}/project/{projectId}/vault/{vaultId}/credential | List storage/vault.credential
[**storage_project_vault_credential_patch**](StorageProjectVaultApi.md#storage_project_vault_credential_patch) | **PATCH** /storage/{locationId}/project/{projectId}/vault/{vaultId}/credential/{credentialId} | Update storage/vault.credential
[**storage_project_vault_delete**](StorageProjectVaultApi.md#storage_project_vault_delete) | **DELETE** /storage/{locationId}/project/{projectId}/vault/{vaultId} | Delete storage/vault
[**storage_project_vault_event_get**](StorageProjectVaultApi.md#storage_project_vault_event_get) | **GET** /storage/{locationId}/project/{projectId}/vault/{vaultId}/event/{eventId} | Get storage/vault.event
[**storage_project_vault_event_list**](StorageProjectVaultApi.md#storage_project_vault_event_list) | **GET** /storage/{locationId}/project/{projectId}/vault/{vaultId}/event | List storage/vault.event
[**storage_project_vault_get**](StorageProjectVaultApi.md#storage_project_vault_get) | **GET** /storage/{locationId}/project/{projectId}/vault/{vaultId} | Get storage/vault
[**storage_project_vault_list**](StorageProjectVaultApi.md#storage_project_vault_list) | **GET** /storage/{locationId}/project/{projectId}/vault | List storage/vault
[**storage_project_vault_resize**](StorageProjectVaultApi.md#storage_project_vault_resize) | **POST** /storage/{locationId}/project/{projectId}/vault/{vaultId}/actions/resize | Resize storage/vault
[**storage_project_vault_service_get**](StorageProjectVaultApi.md#storage_project_vault_service_get) | **GET** /storage/{locationId}/project/{projectId}/vault/{vaultId}/service/{serviceId} | Get storage/vault.service
[**storage_project_vault_service_list**](StorageProjectVaultApi.md#storage_project_vault_service_list) | **GET** /storage/{locationId}/project/{projectId}/vault/{vaultId}/service | List storage/vault.service
[**storage_project_vault_snapshot_create**](StorageProjectVaultApi.md#storage_project_vault_snapshot_create) | **POST** /storage/{locationId}/project/{projectId}/vault/{vaultId}/snapshot | Create storage/vault.snapshot
[**storage_project_vault_snapshot_delete**](StorageProjectVaultApi.md#storage_project_vault_snapshot_delete) | **DELETE** /storage/{locationId}/project/{projectId}/vault/{vaultId}/snapshot/{snapshotId} | Delete storage/vault.snapshot
[**storage_project_vault_snapshot_get**](StorageProjectVaultApi.md#storage_project_vault_snapshot_get) | **GET** /storage/{locationId}/project/{projectId}/vault/{vaultId}/snapshot/{snapshotId} | Get storage/vault.snapshot
[**storage_project_vault_snapshot_list**](StorageProjectVaultApi.md#storage_project_vault_snapshot_list) | **GET** /storage/{locationId}/project/{projectId}/vault/{vaultId}/snapshot | List storage/vault.snapshot
[**storage_project_vault_start**](StorageProjectVaultApi.md#storage_project_vault_start) | **POST** /storage/{locationId}/project/{projectId}/vault/{vaultId}/actions/start | Start storage/vault
[**storage_project_vault_stop**](StorageProjectVaultApi.md#storage_project_vault_stop) | **POST** /storage/{locationId}/project/{projectId}/vault/{vaultId}/actions/stop | Stop storage/vault
[**storage_project_vault_tag_create**](StorageProjectVaultApi.md#storage_project_vault_tag_create) | **POST** /storage/{locationId}/project/{projectId}/vault/{vaultId}/tag | Create storage/vault.tag
[**storage_project_vault_tag_delete**](StorageProjectVaultApi.md#storage_project_vault_tag_delete) | **DELETE** /storage/{locationId}/project/{projectId}/vault/{vaultId}/tag/{tagId} | Delete storage/vault.tag
[**storage_project_vault_tag_get**](StorageProjectVaultApi.md#storage_project_vault_tag_get) | **GET** /storage/{locationId}/project/{projectId}/vault/{vaultId}/tag/{tagId} | Get storage/vault.tag
[**storage_project_vault_tag_list**](StorageProjectVaultApi.md#storage_project_vault_tag_list) | **GET** /storage/{locationId}/project/{projectId}/vault/{vaultId}/tag | List storage/vault.tag
[**storage_project_vault_tag_put**](StorageProjectVaultApi.md#storage_project_vault_tag_put) | **PUT** /storage/{locationId}/project/{projectId}/vault/{vaultId}/tag | Replace storage/vault.tag
[**storage_project_vault_update**](StorageProjectVaultApi.md#storage_project_vault_update) | **PATCH** /storage/{locationId}/project/{projectId}/vault/{vaultId} | Update storage/vault


# **storage_project_vault_connect_get**
> ResourceConnect storage_project_vault_connect_get(project_id, location_id, vault_id, connect_id)

Get storage/vault.connect

Get storage/vault.connect

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.resource_connect import ResourceConnect
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    connect_id = "connectId_example" # str | connectId

    # example passing only required values which don't have defaults set
    try:
        # Get storage/vault.connect
        api_response = api_instance.storage_project_vault_connect_get(project_id, location_id, vault_id, connect_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_connect_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
 **connect_id** | **str**| connectId |

### Return type

[**ResourceConnect**](ResourceConnect.md)

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

# **storage_project_vault_connect_list**
> [ResourceConnect] storage_project_vault_connect_list(project_id, location_id, vault_id)

List storage/vault.connect

List storage/vault.connect

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.resource_connect import ResourceConnect
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id

    # example passing only required values which don't have defaults set
    try:
        # List storage/vault.connect
        api_response = api_instance.storage_project_vault_connect_list(project_id, location_id, vault_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_connect_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |

### Return type

[**[ResourceConnect]**](ResourceConnect.md)

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

# **storage_project_vault_create**
> Vault storage_project_vault_create(project_id, location_id, storage_project_vault_create)

Create storage/vault

Create vault

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.vault import Vault
from h1.model.storage_project_vault_create import StorageProjectVaultCreate
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    storage_project_vault_create = StorageProjectVaultCreate(
        name="name_example",
        service="5a0332c4eb8f4ed95c206a12",
        size=1,
        source="source_example",
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # StorageProjectVaultCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create storage/vault
        api_response = api_instance.storage_project_vault_create(project_id, location_id, storage_project_vault_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create storage/vault
        api_response = api_instance.storage_project_vault_create(project_id, location_id, storage_project_vault_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **storage_project_vault_create** | [**StorageProjectVaultCreate**](StorageProjectVaultCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Vault**](Vault.md)

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

# **storage_project_vault_credential_create**
> VaultCredential storage_project_vault_credential_create(project_id, location_id, vault_id, vault_credential)

Create storage/vault.credential

Create storage/vault.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.vault_credential import VaultCredential
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    vault_credential = VaultCredential(
        id="id_example",
        name="name_example",
        created_by="created_by_example",
        created_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
        type="ssh",
        value="value_example",
        fingerprint="fingerprint_example",
        token="token_example",
    ) # VaultCredential | 

    # example passing only required values which don't have defaults set
    try:
        # Create storage/vault.credential
        api_response = api_instance.storage_project_vault_credential_create(project_id, location_id, vault_id, vault_credential)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_credential_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
 **vault_credential** | [**VaultCredential**](VaultCredential.md)|  |

### Return type

[**VaultCredential**](VaultCredential.md)

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

# **storage_project_vault_credential_delete**
> Vault storage_project_vault_credential_delete(project_id, location_id, vault_id, credential_id)

Delete storage/vault.credential

Delete storage/vault.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.vault import Vault
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Delete storage/vault.credential
        api_response = api_instance.storage_project_vault_credential_delete(project_id, location_id, vault_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_credential_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
 **credential_id** | **str**| credentialId |

### Return type

[**Vault**](Vault.md)

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

# **storage_project_vault_credential_get**
> VaultCredential storage_project_vault_credential_get(project_id, location_id, vault_id, credential_id)

Get storage/vault.credential

Get storage/vault.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.vault_credential import VaultCredential
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Get storage/vault.credential
        api_response = api_instance.storage_project_vault_credential_get(project_id, location_id, vault_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_credential_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
 **credential_id** | **str**| credentialId |

### Return type

[**VaultCredential**](VaultCredential.md)

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

# **storage_project_vault_credential_list**
> [VaultCredential] storage_project_vault_credential_list(project_id, location_id, vault_id)

List storage/vault.credential

List storage/vault.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.vault_credential import VaultCredential
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id

    # example passing only required values which don't have defaults set
    try:
        # List storage/vault.credential
        api_response = api_instance.storage_project_vault_credential_list(project_id, location_id, vault_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_credential_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |

### Return type

[**[VaultCredential]**](VaultCredential.md)

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

# **storage_project_vault_credential_patch**
> VaultCredential storage_project_vault_credential_patch(project_id, location_id, vault_id, credential_id, storage_project_vault_credential_patch)

Update storage/vault.credential

Update storage/vault.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.vault_credential import VaultCredential
from h1.model.storage_project_vault_credential_patch import StorageProjectVaultCredentialPatch
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    credential_id = "credentialId_example" # str | credentialId
    storage_project_vault_credential_patch = StorageProjectVaultCredentialPatch(
        name="name_example",
    ) # StorageProjectVaultCredentialPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update storage/vault.credential
        api_response = api_instance.storage_project_vault_credential_patch(project_id, location_id, vault_id, credential_id, storage_project_vault_credential_patch)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_credential_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
 **credential_id** | **str**| credentialId |
 **storage_project_vault_credential_patch** | [**StorageProjectVaultCredentialPatch**](StorageProjectVaultCredentialPatch.md)|  |

### Return type

[**VaultCredential**](VaultCredential.md)

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

# **storage_project_vault_delete**
> storage_project_vault_delete(project_id, location_id, vault_id, storage_project_vault_delete)

Delete storage/vault

Delete vault

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.storage_project_vault_delete import StorageProjectVaultDelete
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    storage_project_vault_delete = StorageProjectVaultDelete(
        remove_all_snapshots=False,
    ) # StorageProjectVaultDelete | 

    # example passing only required values which don't have defaults set
    try:
        # Delete storage/vault
        api_instance.storage_project_vault_delete(project_id, location_id, vault_id, storage_project_vault_delete)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
 **storage_project_vault_delete** | [**StorageProjectVaultDelete**](StorageProjectVaultDelete.md)|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_project_vault_event_get**
> Event storage_project_vault_event_get(project_id, location_id, vault_id, event_id)

Get storage/vault.event

Get storage/vault.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get storage/vault.event
        api_response = api_instance.storage_project_vault_event_get(project_id, location_id, vault_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_event_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
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

# **storage_project_vault_event_list**
> [Event] storage_project_vault_event_list(project_id, location_id, vault_id)

List storage/vault.event

List storage/vault.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List storage/vault.event
        api_response = api_instance.storage_project_vault_event_list(project_id, location_id, vault_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List storage/vault.event
        api_response = api_instance.storage_project_vault_event_list(project_id, location_id, vault_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
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

# **storage_project_vault_get**
> Vault storage_project_vault_get(project_id, location_id, vault_id)

Get storage/vault

Returns a single vault

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.vault import Vault
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id

    # example passing only required values which don't have defaults set
    try:
        # Get storage/vault
        api_response = api_instance.storage_project_vault_get(project_id, location_id, vault_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |

### Return type

[**Vault**](Vault.md)

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

# **storage_project_vault_list**
> [Vault] storage_project_vault_list(project_id, location_id)

List storage/vault

List vault

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.vault import Vault
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List storage/vault
        api_response = api_instance.storage_project_vault_list(project_id, location_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List storage/vault
        api_response = api_instance.storage_project_vault_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_list: %s\n" % e)
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

[**[Vault]**](Vault.md)

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

# **storage_project_vault_resize**
> Vault storage_project_vault_resize(project_id, location_id, vault_id, storage_project_vault_resize)

Resize storage/vault

action resize

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.vault import Vault
from h1.model.storage_project_vault_resize import StorageProjectVaultResize
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    storage_project_vault_resize = StorageProjectVaultResize(
        size=3.14,
    ) # StorageProjectVaultResize | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Resize storage/vault
        api_response = api_instance.storage_project_vault_resize(project_id, location_id, vault_id, storage_project_vault_resize)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_resize: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Resize storage/vault
        api_response = api_instance.storage_project_vault_resize(project_id, location_id, vault_id, storage_project_vault_resize, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_resize: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
 **storage_project_vault_resize** | [**StorageProjectVaultResize**](StorageProjectVaultResize.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Vault**](Vault.md)

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

# **storage_project_vault_service_get**
> ResourceService storage_project_vault_service_get(project_id, location_id, vault_id, service_id)

Get storage/vault.service

Get storage/vault.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get storage/vault.service
        api_response = api_instance.storage_project_vault_service_get(project_id, location_id, vault_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
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

# **storage_project_vault_service_list**
> [ResourceService] storage_project_vault_service_list(project_id, location_id, vault_id)

List storage/vault.service

List storage/vault.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id

    # example passing only required values which don't have defaults set
    try:
        # List storage/vault.service
        api_response = api_instance.storage_project_vault_service_list(project_id, location_id, vault_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |

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

# **storage_project_vault_snapshot_create**
> StorageSnapshot storage_project_vault_snapshot_create(project_id, location_id, vault_id, storage_project_vault_snapshot_create)

Create storage/vault.snapshot

Create storage/vault.snapshot

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.storage_snapshot import StorageSnapshot
from h1.model.storage_project_vault_snapshot_create import StorageProjectVaultSnapshotCreate
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    storage_project_vault_snapshot_create = StorageProjectVaultSnapshotCreate(
        name="name_example",
    ) # StorageProjectVaultSnapshotCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create storage/vault.snapshot
        api_response = api_instance.storage_project_vault_snapshot_create(project_id, location_id, vault_id, storage_project_vault_snapshot_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_snapshot_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
 **storage_project_vault_snapshot_create** | [**StorageProjectVaultSnapshotCreate**](StorageProjectVaultSnapshotCreate.md)|  |

### Return type

[**StorageSnapshot**](StorageSnapshot.md)

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

# **storage_project_vault_snapshot_delete**
> StorageSnapshot storage_project_vault_snapshot_delete(project_id, location_id, vault_id, snapshot_id)

Delete storage/vault.snapshot

Delete storage/vault.snapshot

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.storage_snapshot import StorageSnapshot
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    snapshot_id = "snapshotId_example" # str | snapshotId

    # example passing only required values which don't have defaults set
    try:
        # Delete storage/vault.snapshot
        api_response = api_instance.storage_project_vault_snapshot_delete(project_id, location_id, vault_id, snapshot_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_snapshot_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
 **snapshot_id** | **str**| snapshotId |

### Return type

[**StorageSnapshot**](StorageSnapshot.md)

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

# **storage_project_vault_snapshot_get**
> StorageSnapshot storage_project_vault_snapshot_get(project_id, location_id, vault_id, snapshot_id)

Get storage/vault.snapshot

Get storage/vault.snapshot

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.storage_snapshot import StorageSnapshot
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    snapshot_id = "snapshotId_example" # str | snapshotId

    # example passing only required values which don't have defaults set
    try:
        # Get storage/vault.snapshot
        api_response = api_instance.storage_project_vault_snapshot_get(project_id, location_id, vault_id, snapshot_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_snapshot_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
 **snapshot_id** | **str**| snapshotId |

### Return type

[**StorageSnapshot**](StorageSnapshot.md)

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

# **storage_project_vault_snapshot_list**
> [StorageSnapshot] storage_project_vault_snapshot_list(project_id, location_id, vault_id)

List storage/vault.snapshot

List storage/vault.snapshot

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.storage_snapshot import StorageSnapshot
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id

    # example passing only required values which don't have defaults set
    try:
        # List storage/vault.snapshot
        api_response = api_instance.storage_project_vault_snapshot_list(project_id, location_id, vault_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_snapshot_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |

### Return type

[**[StorageSnapshot]**](StorageSnapshot.md)

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

# **storage_project_vault_start**
> Vault storage_project_vault_start(project_id, location_id, vault_id)

Start storage/vault

action start

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.vault import Vault
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start storage/vault
        api_response = api_instance.storage_project_vault_start(project_id, location_id, vault_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_start: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start storage/vault
        api_response = api_instance.storage_project_vault_start(project_id, location_id, vault_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_start: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Vault**](Vault.md)

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

# **storage_project_vault_stop**
> Vault storage_project_vault_stop(project_id, location_id, vault_id)

Stop storage/vault

action stop

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.vault import Vault
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Stop storage/vault
        api_response = api_instance.storage_project_vault_stop(project_id, location_id, vault_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_stop: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Stop storage/vault
        api_response = api_instance.storage_project_vault_stop(project_id, location_id, vault_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_stop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Vault**](Vault.md)

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

# **storage_project_vault_tag_create**
> Tag storage_project_vault_tag_create(project_id, location_id, vault_id, tag)

Create storage/vault.tag

Create storage/vault.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create storage/vault.tag
        api_response = api_instance.storage_project_vault_tag_create(project_id, location_id, vault_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_tag_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
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

# **storage_project_vault_tag_delete**
> storage_project_vault_tag_delete(project_id, location_id, vault_id, tag_id)

Delete storage/vault.tag

Delete storage/vault.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete storage/vault.tag
        api_instance.storage_project_vault_tag_delete(project_id, location_id, vault_id, tag_id)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_tag_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
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

# **storage_project_vault_tag_get**
> Tag storage_project_vault_tag_get(project_id, location_id, vault_id, tag_id)

Get storage/vault.tag

Get storage/vault.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get storage/vault.tag
        api_response = api_instance.storage_project_vault_tag_get(project_id, location_id, vault_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_tag_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
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

# **storage_project_vault_tag_list**
> [Tag] storage_project_vault_tag_list(project_id, location_id, vault_id)

List storage/vault.tag

List storage/vault.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id

    # example passing only required values which don't have defaults set
    try:
        # List storage/vault.tag
        api_response = api_instance.storage_project_vault_tag_list(project_id, location_id, vault_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_tag_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |

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

# **storage_project_vault_tag_put**
> [Tag] storage_project_vault_tag_put(project_id, location_id, vault_id, tag_array)

Replace storage/vault.tag

Replace storage/vault.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace storage/vault.tag
        api_response = api_instance.storage_project_vault_tag_put(project_id, location_id, vault_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_tag_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
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

# **storage_project_vault_update**
> Vault storage_project_vault_update(project_id, location_id, vault_id, storage_project_vault_update)

Update storage/vault

Returns modified vault

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import storage_project_vault_api
from h1.model.vault import Vault
from h1.model.storage_project_vault_update import StorageProjectVaultUpdate
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
    api_instance = storage_project_vault_api.StorageProjectVaultApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vault_id = "vaultId_example" # str | Vault Id
    storage_project_vault_update = StorageProjectVaultUpdate(
        name="name_example",
    ) # StorageProjectVaultUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update storage/vault
        api_response = api_instance.storage_project_vault_update(project_id, location_id, vault_id, storage_project_vault_update)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling StorageProjectVaultApi->storage_project_vault_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vault_id** | **str**| Vault Id |
 **storage_project_vault_update** | [**StorageProjectVaultUpdate**](StorageProjectVaultUpdate.md)|  |

### Return type

[**Vault**](Vault.md)

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

