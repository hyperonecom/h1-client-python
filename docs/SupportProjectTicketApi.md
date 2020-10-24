# h1.SupportProjectTicketApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**support_project_ticket_close**](SupportProjectTicketApi.md#support_project_ticket_close) | **POST** /support/project/{projectId}/ticket/{ticketId}/actions/close | Close support/ticket
[**support_project_ticket_create**](SupportProjectTicketApi.md#support_project_ticket_create) | **POST** /support/project/{projectId}/ticket | Create support/ticket
[**support_project_ticket_get**](SupportProjectTicketApi.md#support_project_ticket_get) | **GET** /support/project/{projectId}/ticket/{ticketId} | Get support/ticket
[**support_project_ticket_list**](SupportProjectTicketApi.md#support_project_ticket_list) | **GET** /support/project/{projectId}/ticket | List support/ticket
[**support_project_ticket_message_create**](SupportProjectTicketApi.md#support_project_ticket_message_create) | **POST** /support/project/{projectId}/ticket/{ticketId}/message | Create support/ticket.message
[**support_project_ticket_message_get**](SupportProjectTicketApi.md#support_project_ticket_message_get) | **GET** /support/project/{projectId}/ticket/{ticketId}/message/{messageId} | Get support/ticket.message
[**support_project_ticket_message_list**](SupportProjectTicketApi.md#support_project_ticket_message_list) | **GET** /support/project/{projectId}/ticket/{ticketId}/message | List support/ticket.message


# **support_project_ticket_close**
> Ticket support_project_ticket_close(project_id, ticket_id, x_idempotency_key=x_idempotency_key)

Close support/ticket

action close

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
    api_instance = h1.SupportProjectTicketApi(api_client)
    project_id = 'project_id_example' # str | Project Id
ticket_id = 'ticket_id_example' # str | Ticket Id
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Close support/ticket
        api_response = api_instance.support_project_ticket_close(project_id, ticket_id, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupportProjectTicketApi->support_project_ticket_close: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **ticket_id** | **str**| Ticket Id | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Ticket**](Ticket.md)

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

# **support_project_ticket_create**
> Ticket support_project_ticket_create(project_id, support_project_ticket_create, x_idempotency_key=x_idempotency_key)

Create support/ticket

Create ticket

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
    api_instance = h1.SupportProjectTicketApi(api_client)
    project_id = 'project_id_example' # str | Project Id
support_project_ticket_create = h1.SupportProjectTicketCreate() # SupportProjectTicketCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create support/ticket
        api_response = api_instance.support_project_ticket_create(project_id, support_project_ticket_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupportProjectTicketApi->support_project_ticket_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **support_project_ticket_create** | [**SupportProjectTicketCreate**](SupportProjectTicketCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Ticket**](Ticket.md)

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

# **support_project_ticket_get**
> Ticket support_project_ticket_get(project_id, ticket_id)

Get support/ticket

Returns a single ticket

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
    api_instance = h1.SupportProjectTicketApi(api_client)
    project_id = 'project_id_example' # str | Project Id
ticket_id = 'ticket_id_example' # str | Ticket Id

    try:
        # Get support/ticket
        api_response = api_instance.support_project_ticket_get(project_id, ticket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupportProjectTicketApi->support_project_ticket_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **ticket_id** | **str**| Ticket Id | 

### Return type

[**Ticket**](Ticket.md)

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

# **support_project_ticket_list**
> list[Ticket] support_project_ticket_list(project_id, state=state)

List support/ticket

List ticket

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
    api_instance = h1.SupportProjectTicketApi(api_client)
    project_id = 'project_id_example' # str | Project Id
state = 'state_example' # str | Filter by state (optional)

    try:
        # List support/ticket
        api_response = api_instance.support_project_ticket_list(project_id, state=state)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupportProjectTicketApi->support_project_ticket_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **state** | **str**| Filter by state | [optional] 

### Return type

[**list[Ticket]**](Ticket.md)

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

# **support_project_ticket_message_create**
> SupportMessage support_project_ticket_message_create(project_id, ticket_id, support_message)

Create support/ticket.message

Create support/ticket.message

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
    api_instance = h1.SupportProjectTicketApi(api_client)
    project_id = 'project_id_example' # str | Project Id
ticket_id = 'ticket_id_example' # str | Ticket Id
support_message = h1.SupportMessage() # SupportMessage | 

    try:
        # Create support/ticket.message
        api_response = api_instance.support_project_ticket_message_create(project_id, ticket_id, support_message)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupportProjectTicketApi->support_project_ticket_message_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **ticket_id** | **str**| Ticket Id | 
 **support_message** | [**SupportMessage**](SupportMessage.md)|  | 

### Return type

[**SupportMessage**](SupportMessage.md)

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

# **support_project_ticket_message_get**
> SupportMessage support_project_ticket_message_get(project_id, ticket_id, message_id)

Get support/ticket.message

Get support/ticket.message

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
    api_instance = h1.SupportProjectTicketApi(api_client)
    project_id = 'project_id_example' # str | Project Id
ticket_id = 'ticket_id_example' # str | Ticket Id
message_id = 'message_id_example' # str | messageId

    try:
        # Get support/ticket.message
        api_response = api_instance.support_project_ticket_message_get(project_id, ticket_id, message_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupportProjectTicketApi->support_project_ticket_message_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **ticket_id** | **str**| Ticket Id | 
 **message_id** | **str**| messageId | 

### Return type

[**SupportMessage**](SupportMessage.md)

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

# **support_project_ticket_message_list**
> list[SupportMessage] support_project_ticket_message_list(project_id, ticket_id)

List support/ticket.message

List support/ticket.message

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
    api_instance = h1.SupportProjectTicketApi(api_client)
    project_id = 'project_id_example' # str | Project Id
ticket_id = 'ticket_id_example' # str | Ticket Id

    try:
        # List support/ticket.message
        api_response = api_instance.support_project_ticket_message_list(project_id, ticket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SupportProjectTicketApi->support_project_ticket_message_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **ticket_id** | **str**| Ticket Id | 

### Return type

[**list[SupportMessage]**](SupportMessage.md)

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

