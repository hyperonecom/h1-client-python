# h1-client-python.ProviderProjectAgentApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**provider_project_agent_create**](ProviderProjectAgentApi.md#provider_project_agent_create) | **POST** /provider/{locationId}/project/{projectId}/agent | Create provider/agent
[**provider_project_agent_credential_create**](ProviderProjectAgentApi.md#provider_project_agent_credential_create) | **POST** /provider/{locationId}/project/{projectId}/agent/{agentId}/credential | Create provider/agent.credential
[**provider_project_agent_credential_delete**](ProviderProjectAgentApi.md#provider_project_agent_credential_delete) | **DELETE** /provider/{locationId}/project/{projectId}/agent/{agentId}/credential/{credentialId} | Delete provider/agent.credential
[**provider_project_agent_credential_get**](ProviderProjectAgentApi.md#provider_project_agent_credential_get) | **GET** /provider/{locationId}/project/{projectId}/agent/{agentId}/credential/{credentialId} | Get provider/agent.credential
[**provider_project_agent_credential_list**](ProviderProjectAgentApi.md#provider_project_agent_credential_list) | **GET** /provider/{locationId}/project/{projectId}/agent/{agentId}/credential | List provider/agent.credential
[**provider_project_agent_credential_patch**](ProviderProjectAgentApi.md#provider_project_agent_credential_patch) | **PATCH** /provider/{locationId}/project/{projectId}/agent/{agentId}/credential/{credentialId} | Update provider/agent.credential
[**provider_project_agent_delete**](ProviderProjectAgentApi.md#provider_project_agent_delete) | **DELETE** /provider/{locationId}/project/{projectId}/agent/{agentId} | Delete provider/agent
[**provider_project_agent_enabled_service_create**](ProviderProjectAgentApi.md#provider_project_agent_enabled_service_create) | **POST** /provider/{locationId}/project/{projectId}/agent/{agentId}/enabledService | Create provider/agent.enabledService
[**provider_project_agent_enabled_service_delete**](ProviderProjectAgentApi.md#provider_project_agent_enabled_service_delete) | **DELETE** /provider/{locationId}/project/{projectId}/agent/{agentId}/enabledService/{enabledServiceId} | Delete provider/agent.enabledService
[**provider_project_agent_enabled_service_get**](ProviderProjectAgentApi.md#provider_project_agent_enabled_service_get) | **GET** /provider/{locationId}/project/{projectId}/agent/{agentId}/enabledService/{enabledServiceId} | Get provider/agent.enabledService
[**provider_project_agent_enabled_service_list**](ProviderProjectAgentApi.md#provider_project_agent_enabled_service_list) | **GET** /provider/{locationId}/project/{projectId}/agent/{agentId}/enabledService | List provider/agent.enabledService
[**provider_project_agent_event_get**](ProviderProjectAgentApi.md#provider_project_agent_event_get) | **GET** /provider/{locationId}/project/{projectId}/agent/{agentId}/event/{eventId} | Get provider/agent.event
[**provider_project_agent_event_list**](ProviderProjectAgentApi.md#provider_project_agent_event_list) | **GET** /provider/{locationId}/project/{projectId}/agent/{agentId}/event | List provider/agent.event
[**provider_project_agent_get**](ProviderProjectAgentApi.md#provider_project_agent_get) | **GET** /provider/{locationId}/project/{projectId}/agent/{agentId} | Get provider/agent
[**provider_project_agent_inspect**](ProviderProjectAgentApi.md#provider_project_agent_inspect) | **POST** /provider/{locationId}/project/{projectId}/agent/{agentId}/actions/inspect | Inspect provider/agent
[**provider_project_agent_list**](ProviderProjectAgentApi.md#provider_project_agent_list) | **GET** /provider/{locationId}/project/{projectId}/agent | List provider/agent
[**provider_project_agent_resource_event_list**](ProviderProjectAgentApi.md#provider_project_agent_resource_event_list) | **GET** /provider/{locationId}/project/{projectId}/agent/{agentId}/resource/{resourceId}/event | List provider/agent.event
[**provider_project_agent_resource_inspect**](ProviderProjectAgentApi.md#provider_project_agent_resource_inspect) | **POST** /provider/{locationId}/project/{projectId}/agent/{agentId}/resource/{resourceId}/actions/inspect | Inspect provider/agent.resource
[**provider_project_agent_resource_list**](ProviderProjectAgentApi.md#provider_project_agent_resource_list) | **GET** /provider/{locationId}/project/{projectId}/agent/{agentId}/resource | List provider/agent.resource
[**provider_project_agent_resource_recreate**](ProviderProjectAgentApi.md#provider_project_agent_resource_recreate) | **POST** /provider/{locationId}/project/{projectId}/agent/{agentId}/resource/{resourceId}/actions/recreate | Recreate provider/agent.resource
[**provider_project_agent_service_get**](ProviderProjectAgentApi.md#provider_project_agent_service_get) | **GET** /provider/{locationId}/project/{projectId}/agent/{agentId}/service/{serviceId} | Get provider/agent.service
[**provider_project_agent_service_list**](ProviderProjectAgentApi.md#provider_project_agent_service_list) | **GET** /provider/{locationId}/project/{projectId}/agent/{agentId}/service | List provider/agent.service
[**provider_project_agent_start**](ProviderProjectAgentApi.md#provider_project_agent_start) | **POST** /provider/{locationId}/project/{projectId}/agent/{agentId}/actions/start | Start provider/agent
[**provider_project_agent_suspend**](ProviderProjectAgentApi.md#provider_project_agent_suspend) | **POST** /provider/{locationId}/project/{projectId}/agent/{agentId}/actions/suspend | Suspend provider/agent
[**provider_project_agent_tag_create**](ProviderProjectAgentApi.md#provider_project_agent_tag_create) | **POST** /provider/{locationId}/project/{projectId}/agent/{agentId}/tag | Create provider/agent.tag
[**provider_project_agent_tag_delete**](ProviderProjectAgentApi.md#provider_project_agent_tag_delete) | **DELETE** /provider/{locationId}/project/{projectId}/agent/{agentId}/tag/{tagId} | Delete provider/agent.tag
[**provider_project_agent_tag_get**](ProviderProjectAgentApi.md#provider_project_agent_tag_get) | **GET** /provider/{locationId}/project/{projectId}/agent/{agentId}/tag/{tagId} | Get provider/agent.tag
[**provider_project_agent_tag_list**](ProviderProjectAgentApi.md#provider_project_agent_tag_list) | **GET** /provider/{locationId}/project/{projectId}/agent/{agentId}/tag | List provider/agent.tag
[**provider_project_agent_tag_put**](ProviderProjectAgentApi.md#provider_project_agent_tag_put) | **PUT** /provider/{locationId}/project/{projectId}/agent/{agentId}/tag | Replace provider/agent.tag
[**provider_project_agent_transfer**](ProviderProjectAgentApi.md#provider_project_agent_transfer) | **POST** /provider/{locationId}/project/{projectId}/agent/{agentId}/actions/transfer | Transfer provider/agent
[**provider_project_agent_update**](ProviderProjectAgentApi.md#provider_project_agent_update) | **PATCH** /provider/{locationId}/project/{projectId}/agent/{agentId} | Update provider/agent


# **provider_project_agent_create**
> Agent provider_project_agent_create(project_id, location_id, provider_project_agent_create, x_idempotency_key=x_idempotency_key)

Create provider/agent

Create agent

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
provider_project_agent_create = h1-client-python.ProviderProjectAgentCreate() # ProviderProjectAgentCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create provider/agent
        api_response = api_instance.provider_project_agent_create(project_id, location_id, provider_project_agent_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **provider_project_agent_create** | [**ProviderProjectAgentCreate**](ProviderProjectAgentCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Agent**](Agent.md)

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

# **provider_project_agent_credential_create**
> AgentCredential provider_project_agent_credential_create(project_id, location_id, agent_id, agent_credential)

Create provider/agent.credential

Create provider/agent.credential

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
agent_credential = h1-client-python.AgentCredential() # AgentCredential | 

    try:
        # Create provider/agent.credential
        api_response = api_instance.provider_project_agent_credential_create(project_id, location_id, agent_id, agent_credential)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_credential_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
 **agent_credential** | [**AgentCredential**](AgentCredential.md)|  | 

### Return type

[**AgentCredential**](AgentCredential.md)

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

# **provider_project_agent_credential_delete**
> Agent provider_project_agent_credential_delete(project_id, location_id, agent_id, credential_id)

Delete provider/agent.credential

Delete provider/agent.credential

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
credential_id = 'credential_id_example' # str | credentialId

    try:
        # Delete provider/agent.credential
        api_response = api_instance.provider_project_agent_credential_delete(project_id, location_id, agent_id, credential_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_credential_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
 **credential_id** | **str**| credentialId | 

### Return type

[**Agent**](Agent.md)

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

# **provider_project_agent_credential_get**
> AgentCredential provider_project_agent_credential_get(project_id, location_id, agent_id, credential_id)

Get provider/agent.credential

Get provider/agent.credential

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
credential_id = 'credential_id_example' # str | credentialId

    try:
        # Get provider/agent.credential
        api_response = api_instance.provider_project_agent_credential_get(project_id, location_id, agent_id, credential_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_credential_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
 **credential_id** | **str**| credentialId | 

### Return type

[**AgentCredential**](AgentCredential.md)

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

# **provider_project_agent_credential_list**
> list[AgentCredential] provider_project_agent_credential_list(project_id, location_id, agent_id)

List provider/agent.credential

List provider/agent.credential

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id

    try:
        # List provider/agent.credential
        api_response = api_instance.provider_project_agent_credential_list(project_id, location_id, agent_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_credential_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 

### Return type

[**list[AgentCredential]**](AgentCredential.md)

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

# **provider_project_agent_credential_patch**
> AgentCredential provider_project_agent_credential_patch(project_id, location_id, agent_id, credential_id, provider_project_agent_credential_patch)

Update provider/agent.credential

Update provider/agent.credential

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
credential_id = 'credential_id_example' # str | credentialId
provider_project_agent_credential_patch = h1-client-python.ProviderProjectAgentCredentialPatch() # ProviderProjectAgentCredentialPatch | 

    try:
        # Update provider/agent.credential
        api_response = api_instance.provider_project_agent_credential_patch(project_id, location_id, agent_id, credential_id, provider_project_agent_credential_patch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_credential_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
 **credential_id** | **str**| credentialId | 
 **provider_project_agent_credential_patch** | [**ProviderProjectAgentCredentialPatch**](ProviderProjectAgentCredentialPatch.md)|  | 

### Return type

[**AgentCredential**](AgentCredential.md)

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

# **provider_project_agent_delete**
> provider_project_agent_delete(project_id, location_id, agent_id)

Delete provider/agent

Delete agent

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id

    try:
        # Delete provider/agent
        api_instance.provider_project_agent_delete(project_id, location_id, agent_id)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 

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

# **provider_project_agent_enabled_service_create**
> EnabledService provider_project_agent_enabled_service_create(project_id, location_id, agent_id, enabled_service)

Create provider/agent.enabledService

Create provider/agent.enabledService

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
enabled_service = h1-client-python.EnabledService() # EnabledService | 

    try:
        # Create provider/agent.enabledService
        api_response = api_instance.provider_project_agent_enabled_service_create(project_id, location_id, agent_id, enabled_service)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_enabled_service_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
 **enabled_service** | [**EnabledService**](EnabledService.md)|  | 

### Return type

[**EnabledService**](EnabledService.md)

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

# **provider_project_agent_enabled_service_delete**
> Agent provider_project_agent_enabled_service_delete(project_id, location_id, agent_id, enabled_service_id)

Delete provider/agent.enabledService

Delete provider/agent.enabledService

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
enabled_service_id = 'enabled_service_id_example' # str | enabledServiceId

    try:
        # Delete provider/agent.enabledService
        api_response = api_instance.provider_project_agent_enabled_service_delete(project_id, location_id, agent_id, enabled_service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_enabled_service_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
 **enabled_service_id** | **str**| enabledServiceId | 

### Return type

[**Agent**](Agent.md)

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

# **provider_project_agent_enabled_service_get**
> EnabledService provider_project_agent_enabled_service_get(project_id, location_id, agent_id, enabled_service_id)

Get provider/agent.enabledService

Get provider/agent.enabledService

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
enabled_service_id = 'enabled_service_id_example' # str | enabledServiceId

    try:
        # Get provider/agent.enabledService
        api_response = api_instance.provider_project_agent_enabled_service_get(project_id, location_id, agent_id, enabled_service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_enabled_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
 **enabled_service_id** | **str**| enabledServiceId | 

### Return type

[**EnabledService**](EnabledService.md)

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

# **provider_project_agent_enabled_service_list**
> list[EnabledService] provider_project_agent_enabled_service_list(project_id, location_id, agent_id)

List provider/agent.enabledService

List provider/agent.enabledService

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id

    try:
        # List provider/agent.enabledService
        api_response = api_instance.provider_project_agent_enabled_service_list(project_id, location_id, agent_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_enabled_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 

### Return type

[**list[EnabledService]**](EnabledService.md)

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

# **provider_project_agent_event_get**
> Event provider_project_agent_event_get(project_id, location_id, agent_id, event_id)

Get provider/agent.event

Get provider/agent.event

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get provider/agent.event
        api_response = api_instance.provider_project_agent_event_get(project_id, location_id, agent_id, event_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
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

# **provider_project_agent_event_list**
> list[Event] provider_project_agent_event_list(project_id, location_id, agent_id, limit=limit, skip=skip)

List provider/agent.event

List provider/agent.event

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List provider/agent.event
        api_response = api_instance.provider_project_agent_event_list(project_id, location_id, agent_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
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

# **provider_project_agent_get**
> Agent provider_project_agent_get(project_id, location_id, agent_id)

Get provider/agent

Returns a single agent

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id

    try:
        # Get provider/agent
        api_response = api_instance.provider_project_agent_get(project_id, location_id, agent_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 

### Return type

[**Agent**](Agent.md)

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

# **provider_project_agent_inspect**
> Agent provider_project_agent_inspect(project_id, location_id, agent_id, x_idempotency_key=x_idempotency_key)

Inspect provider/agent

action inspect

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Inspect provider/agent
        api_response = api_instance.provider_project_agent_inspect(project_id, location_id, agent_id, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Agent**](Agent.md)

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

# **provider_project_agent_list**
> list[Agent] provider_project_agent_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)

List provider/agent

List agent

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
name = 'name_example' # str | Filter by name (optional)
tag_value = 'tag_value_example' # str | Filter by tag.value (optional)
tag_key = 'tag_key_example' # str | Filter by tag.key (optional)

    try:
        # List provider/agent
        api_response = api_instance.provider_project_agent_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_list: %s\n" % e)
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

[**list[Agent]**](Agent.md)

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

# **provider_project_agent_resource_event_list**
> list[AgentResourceEvent] provider_project_agent_resource_event_list(project_id, location_id, agent_id, resource_id, limit=limit, skip=skip)

List provider/agent.event

List provider/agent.event

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
resource_id = 'resource_id_example' # str | resourceId
limit = 3.4 # float | $limit (optional)
skip = 3.4 # float | $skip (optional)

    try:
        # List provider/agent.event
        api_response = api_instance.provider_project_agent_resource_event_list(project_id, location_id, agent_id, resource_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_resource_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
 **resource_id** | **str**| resourceId | 
 **limit** | **float**| $limit | [optional] 
 **skip** | **float**| $skip | [optional] 

### Return type

[**list[AgentResourceEvent]**](AgentResourceEvent.md)

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

# **provider_project_agent_resource_inspect**
> object provider_project_agent_resource_inspect(project_id, location_id, agent_id, resource_id)

Inspect provider/agent.resource

action inspect

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
resource_id = 'resource_id_example' # str | resourceId

    try:
        # Inspect provider/agent.resource
        api_response = api_instance.provider_project_agent_resource_inspect(project_id, location_id, agent_id, resource_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_resource_inspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
 **resource_id** | **str**| resourceId | 

### Return type

**object**

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

# **provider_project_agent_resource_list**
> list[AgentResource] provider_project_agent_resource_list(project_id, location_id, agent_id)

List provider/agent.resource

List provider/agent.resource

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id

    try:
        # List provider/agent.resource
        api_response = api_instance.provider_project_agent_resource_list(project_id, location_id, agent_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_resource_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 

### Return type

[**list[AgentResource]**](AgentResource.md)

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

# **provider_project_agent_resource_recreate**
> AgentResource provider_project_agent_resource_recreate(project_id, location_id, agent_id, resource_id)

Recreate provider/agent.resource

action recreate

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
resource_id = 'resource_id_example' # str | resourceId

    try:
        # Recreate provider/agent.resource
        api_response = api_instance.provider_project_agent_resource_recreate(project_id, location_id, agent_id, resource_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_resource_recreate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
 **resource_id** | **str**| resourceId | 

### Return type

[**AgentResource**](AgentResource.md)

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

# **provider_project_agent_service_get**
> ResourceService provider_project_agent_service_get(project_id, location_id, agent_id, service_id)

Get provider/agent.service

Get provider/agent.service

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
service_id = 'service_id_example' # str | serviceId

    try:
        # Get provider/agent.service
        api_response = api_instance.provider_project_agent_service_get(project_id, location_id, agent_id, service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
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

# **provider_project_agent_service_list**
> list[ResourceService] provider_project_agent_service_list(project_id, location_id, agent_id)

List provider/agent.service

List provider/agent.service

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id

    try:
        # List provider/agent.service
        api_response = api_instance.provider_project_agent_service_list(project_id, location_id, agent_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 

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

# **provider_project_agent_start**
> Agent provider_project_agent_start(project_id, location_id, agent_id, x_idempotency_key=x_idempotency_key)

Start provider/agent

action start

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Start provider/agent
        api_response = api_instance.provider_project_agent_start(project_id, location_id, agent_id, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Agent**](Agent.md)

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

# **provider_project_agent_suspend**
> Agent provider_project_agent_suspend(project_id, location_id, agent_id, x_idempotency_key=x_idempotency_key)

Suspend provider/agent

action suspend

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Suspend provider/agent
        api_response = api_instance.provider_project_agent_suspend(project_id, location_id, agent_id, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_suspend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Agent**](Agent.md)

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

# **provider_project_agent_tag_create**
> Tag provider_project_agent_tag_create(project_id, location_id, agent_id, tag)

Create provider/agent.tag

Create provider/agent.tag

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
tag = h1-client-python.Tag() # Tag | 

    try:
        # Create provider/agent.tag
        api_response = api_instance.provider_project_agent_tag_create(project_id, location_id, agent_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
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

# **provider_project_agent_tag_delete**
> provider_project_agent_tag_delete(project_id, location_id, agent_id, tag_id)

Delete provider/agent.tag

Delete provider/agent.tag

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Delete provider/agent.tag
        api_instance.provider_project_agent_tag_delete(project_id, location_id, agent_id, tag_id)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
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

# **provider_project_agent_tag_get**
> Tag provider_project_agent_tag_get(project_id, location_id, agent_id, tag_id)

Get provider/agent.tag

Get provider/agent.tag

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Get provider/agent.tag
        api_response = api_instance.provider_project_agent_tag_get(project_id, location_id, agent_id, tag_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
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

# **provider_project_agent_tag_list**
> list[Tag] provider_project_agent_tag_list(project_id, location_id, agent_id)

List provider/agent.tag

List provider/agent.tag

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id

    try:
        # List provider/agent.tag
        api_response = api_instance.provider_project_agent_tag_list(project_id, location_id, agent_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 

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

# **provider_project_agent_tag_put**
> list[Tag] provider_project_agent_tag_put(project_id, location_id, agent_id, tag)

Replace provider/agent.tag

Replace provider/agent.tag

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
tag = [h1-client-python.Tag()] # list[Tag] | 

    try:
        # Replace provider/agent.tag
        api_response = api_instance.provider_project_agent_tag_put(project_id, location_id, agent_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
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

# **provider_project_agent_transfer**
> Agent provider_project_agent_transfer(project_id, location_id, agent_id, provider_project_agent_transfer, x_idempotency_key=x_idempotency_key)

Transfer provider/agent

action transfer

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
provider_project_agent_transfer = h1-client-python.ProviderProjectAgentTransfer() # ProviderProjectAgentTransfer | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Transfer provider/agent
        api_response = api_instance.provider_project_agent_transfer(project_id, location_id, agent_id, provider_project_agent_transfer, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
 **provider_project_agent_transfer** | [**ProviderProjectAgentTransfer**](ProviderProjectAgentTransfer.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Agent**](Agent.md)

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

# **provider_project_agent_update**
> Agent provider_project_agent_update(project_id, location_id, agent_id, provider_project_agent_update)

Update provider/agent

Returns modified agent

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
    api_instance = h1-client-python.ProviderProjectAgentApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
agent_id = 'agent_id_example' # str | Agent Id
provider_project_agent_update = h1-client-python.ProviderProjectAgentUpdate() # ProviderProjectAgentUpdate | 

    try:
        # Update provider/agent
        api_response = api_instance.provider_project_agent_update(project_id, location_id, agent_id, provider_project_agent_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ProviderProjectAgentApi->provider_project_agent_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **agent_id** | **str**| Agent Id | 
 **provider_project_agent_update** | [**ProviderProjectAgentUpdate**](ProviderProjectAgentUpdate.md)|  | 

### Return type

[**Agent**](Agent.md)

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

