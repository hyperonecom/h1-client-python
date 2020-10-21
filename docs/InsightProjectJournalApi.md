# h1-client-python.InsightProjectJournalApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**insight_project_journal_create**](InsightProjectJournalApi.md#insight_project_journal_create) | **POST** /insight/{locationId}/project/{projectId}/journal | Create insight/journal
[**insight_project_journal_credential_create**](InsightProjectJournalApi.md#insight_project_journal_credential_create) | **POST** /insight/{locationId}/project/{projectId}/journal/{journalId}/credential | Create insight/journal.credential
[**insight_project_journal_credential_delete**](InsightProjectJournalApi.md#insight_project_journal_credential_delete) | **DELETE** /insight/{locationId}/project/{projectId}/journal/{journalId}/credential/{credentialId} | Delete insight/journal.credential
[**insight_project_journal_credential_get**](InsightProjectJournalApi.md#insight_project_journal_credential_get) | **GET** /insight/{locationId}/project/{projectId}/journal/{journalId}/credential/{credentialId} | Get insight/journal.credential
[**insight_project_journal_credential_list**](InsightProjectJournalApi.md#insight_project_journal_credential_list) | **GET** /insight/{locationId}/project/{projectId}/journal/{journalId}/credential | List insight/journal.credential
[**insight_project_journal_credential_patch**](InsightProjectJournalApi.md#insight_project_journal_credential_patch) | **PATCH** /insight/{locationId}/project/{projectId}/journal/{journalId}/credential/{credentialId} | Update insight/journal.credential
[**insight_project_journal_delete**](InsightProjectJournalApi.md#insight_project_journal_delete) | **DELETE** /insight/{locationId}/project/{projectId}/journal/{journalId} | Delete insight/journal
[**insight_project_journal_event_get**](InsightProjectJournalApi.md#insight_project_journal_event_get) | **GET** /insight/{locationId}/project/{projectId}/journal/{journalId}/event/{eventId} | Get insight/journal.event
[**insight_project_journal_event_list**](InsightProjectJournalApi.md#insight_project_journal_event_list) | **GET** /insight/{locationId}/project/{projectId}/journal/{journalId}/event | List insight/journal.event
[**insight_project_journal_get**](InsightProjectJournalApi.md#insight_project_journal_get) | **GET** /insight/{locationId}/project/{projectId}/journal/{journalId} | Get insight/journal
[**insight_project_journal_list**](InsightProjectJournalApi.md#insight_project_journal_list) | **GET** /insight/{locationId}/project/{projectId}/journal | List insight/journal
[**insight_project_journal_log_get**](InsightProjectJournalApi.md#insight_project_journal_log_get) | **GET** /insight/{locationId}/project/{projectId}/journal/{journalId}/log | Get insight/journal.log
[**insight_project_journal_service_get**](InsightProjectJournalApi.md#insight_project_journal_service_get) | **GET** /insight/{locationId}/project/{projectId}/journal/{journalId}/service/{serviceId} | Get insight/journal.service
[**insight_project_journal_service_list**](InsightProjectJournalApi.md#insight_project_journal_service_list) | **GET** /insight/{locationId}/project/{projectId}/journal/{journalId}/service | List insight/journal.service
[**insight_project_journal_tag_create**](InsightProjectJournalApi.md#insight_project_journal_tag_create) | **POST** /insight/{locationId}/project/{projectId}/journal/{journalId}/tag | Create insight/journal.tag
[**insight_project_journal_tag_delete**](InsightProjectJournalApi.md#insight_project_journal_tag_delete) | **DELETE** /insight/{locationId}/project/{projectId}/journal/{journalId}/tag/{tagId} | Delete insight/journal.tag
[**insight_project_journal_tag_get**](InsightProjectJournalApi.md#insight_project_journal_tag_get) | **GET** /insight/{locationId}/project/{projectId}/journal/{journalId}/tag/{tagId} | Get insight/journal.tag
[**insight_project_journal_tag_list**](InsightProjectJournalApi.md#insight_project_journal_tag_list) | **GET** /insight/{locationId}/project/{projectId}/journal/{journalId}/tag | List insight/journal.tag
[**insight_project_journal_tag_put**](InsightProjectJournalApi.md#insight_project_journal_tag_put) | **PUT** /insight/{locationId}/project/{projectId}/journal/{journalId}/tag | Replace insight/journal.tag
[**insight_project_journal_transfer**](InsightProjectJournalApi.md#insight_project_journal_transfer) | **POST** /insight/{locationId}/project/{projectId}/journal/{journalId}/actions/transfer | Transfer insight/journal
[**insight_project_journal_update**](InsightProjectJournalApi.md#insight_project_journal_update) | **PATCH** /insight/{locationId}/project/{projectId}/journal/{journalId} | Update insight/journal


# **insight_project_journal_create**
> Journal insight_project_journal_create(project_id, location_id, insight_project_journal_create, x_idempotency_key=x_idempotency_key)

Create insight/journal

Create journal

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
insight_project_journal_create = h1-client-python.InsightProjectJournalCreate() # InsightProjectJournalCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create insight/journal
        api_response = api_instance.insight_project_journal_create(project_id, location_id, insight_project_journal_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **insight_project_journal_create** | [**InsightProjectJournalCreate**](InsightProjectJournalCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Journal**](Journal.md)

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

# **insight_project_journal_credential_create**
> JournalCredential insight_project_journal_credential_create(project_id, location_id, journal_id, journal_credential)

Create insight/journal.credential

Create insight/journal.credential

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id
journal_credential = h1-client-python.JournalCredential() # JournalCredential | 

    try:
        # Create insight/journal.credential
        api_response = api_instance.insight_project_journal_credential_create(project_id, location_id, journal_id, journal_credential)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_credential_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 
 **journal_credential** | [**JournalCredential**](JournalCredential.md)|  | 

### Return type

[**JournalCredential**](JournalCredential.md)

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

# **insight_project_journal_credential_delete**
> Journal insight_project_journal_credential_delete(project_id, location_id, journal_id, credential_id)

Delete insight/journal.credential

Delete insight/journal.credential

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id
credential_id = 'credential_id_example' # str | credentialId

    try:
        # Delete insight/journal.credential
        api_response = api_instance.insight_project_journal_credential_delete(project_id, location_id, journal_id, credential_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_credential_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 
 **credential_id** | **str**| credentialId | 

### Return type

[**Journal**](Journal.md)

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

# **insight_project_journal_credential_get**
> JournalCredential insight_project_journal_credential_get(project_id, location_id, journal_id, credential_id)

Get insight/journal.credential

Get insight/journal.credential

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id
credential_id = 'credential_id_example' # str | credentialId

    try:
        # Get insight/journal.credential
        api_response = api_instance.insight_project_journal_credential_get(project_id, location_id, journal_id, credential_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_credential_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 
 **credential_id** | **str**| credentialId | 

### Return type

[**JournalCredential**](JournalCredential.md)

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

# **insight_project_journal_credential_list**
> list[JournalCredential] insight_project_journal_credential_list(project_id, location_id, journal_id)

List insight/journal.credential

List insight/journal.credential

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id

    try:
        # List insight/journal.credential
        api_response = api_instance.insight_project_journal_credential_list(project_id, location_id, journal_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_credential_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 

### Return type

[**list[JournalCredential]**](JournalCredential.md)

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

# **insight_project_journal_credential_patch**
> JournalCredential insight_project_journal_credential_patch(project_id, location_id, journal_id, credential_id, insight_project_journal_credential_patch)

Update insight/journal.credential

Update insight/journal.credential

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id
credential_id = 'credential_id_example' # str | credentialId
insight_project_journal_credential_patch = h1-client-python.InsightProjectJournalCredentialPatch() # InsightProjectJournalCredentialPatch | 

    try:
        # Update insight/journal.credential
        api_response = api_instance.insight_project_journal_credential_patch(project_id, location_id, journal_id, credential_id, insight_project_journal_credential_patch)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_credential_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 
 **credential_id** | **str**| credentialId | 
 **insight_project_journal_credential_patch** | [**InsightProjectJournalCredentialPatch**](InsightProjectJournalCredentialPatch.md)|  | 

### Return type

[**JournalCredential**](JournalCredential.md)

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

# **insight_project_journal_delete**
> insight_project_journal_delete(project_id, location_id, journal_id)

Delete insight/journal

Delete journal

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id

    try:
        # Delete insight/journal
        api_instance.insight_project_journal_delete(project_id, location_id, journal_id)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 

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

# **insight_project_journal_event_get**
> Event insight_project_journal_event_get(project_id, location_id, journal_id, event_id)

Get insight/journal.event

Get insight/journal.event

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get insight/journal.event
        api_response = api_instance.insight_project_journal_event_get(project_id, location_id, journal_id, event_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 
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

# **insight_project_journal_event_list**
> list[Event] insight_project_journal_event_list(project_id, location_id, journal_id, limit=limit, skip=skip)

List insight/journal.event

List insight/journal.event

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List insight/journal.event
        api_response = api_instance.insight_project_journal_event_list(project_id, location_id, journal_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 
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

# **insight_project_journal_get**
> Journal insight_project_journal_get(project_id, location_id, journal_id)

Get insight/journal

Returns a single journal

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id

    try:
        # Get insight/journal
        api_response = api_instance.insight_project_journal_get(project_id, location_id, journal_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 

### Return type

[**Journal**](Journal.md)

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

# **insight_project_journal_list**
> list[Journal] insight_project_journal_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)

List insight/journal

List journal

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
name = 'name_example' # str | Filter by name (optional)
tag_value = 'tag_value_example' # str | Filter by tag.value (optional)
tag_key = 'tag_key_example' # str | Filter by tag.key (optional)

    try:
        # List insight/journal
        api_response = api_instance.insight_project_journal_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_list: %s\n" % e)
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

[**list[Journal]**](Journal.md)

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

# **insight_project_journal_log_get**
> insight_project_journal_log_get(project_id, location_id, journal_id, since=since, until=until, follow=follow, tail=tail, tag=tag)

Get insight/journal.log

websocket is also supported

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id
since = '2013-10-20T19:20:30+01:00' # datetime | since (optional)
until = '2013-10-20T19:20:30+01:00' # datetime | until (optional)
follow = False # bool | follow (optional) (default to False)
tail = 3.4 # float | tail (optional)
tag = [h1-client-python.Tag()] # list[Tag] | tag (optional)

    try:
        # Get insight/journal.log
        api_instance.insight_project_journal_log_get(project_id, location_id, journal_id, since=since, until=until, follow=follow, tail=tail, tag=tag)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_log_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 
 **since** | **datetime**| since | [optional] 
 **until** | **datetime**| until | [optional] 
 **follow** | **bool**| follow | [optional] [default to False]
 **tail** | **float**| tail | [optional] 
 **tag** | [**list[Tag]**](Tag.md)| tag | [optional] 

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
**302** | Redirect to the provider with a claim |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **insight_project_journal_service_get**
> ResourceService insight_project_journal_service_get(project_id, location_id, journal_id, service_id)

Get insight/journal.service

Get insight/journal.service

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id
service_id = 'service_id_example' # str | serviceId

    try:
        # Get insight/journal.service
        api_response = api_instance.insight_project_journal_service_get(project_id, location_id, journal_id, service_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 
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

# **insight_project_journal_service_list**
> list[ResourceService] insight_project_journal_service_list(project_id, location_id, journal_id)

List insight/journal.service

List insight/journal.service

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id

    try:
        # List insight/journal.service
        api_response = api_instance.insight_project_journal_service_list(project_id, location_id, journal_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 

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

# **insight_project_journal_tag_create**
> Tag insight_project_journal_tag_create(project_id, location_id, journal_id, tag)

Create insight/journal.tag

Create insight/journal.tag

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id
tag = h1-client-python.Tag() # Tag | 

    try:
        # Create insight/journal.tag
        api_response = api_instance.insight_project_journal_tag_create(project_id, location_id, journal_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 
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

# **insight_project_journal_tag_delete**
> insight_project_journal_tag_delete(project_id, location_id, journal_id, tag_id)

Delete insight/journal.tag

Delete insight/journal.tag

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Delete insight/journal.tag
        api_instance.insight_project_journal_tag_delete(project_id, location_id, journal_id, tag_id)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 
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

# **insight_project_journal_tag_get**
> Tag insight_project_journal_tag_get(project_id, location_id, journal_id, tag_id)

Get insight/journal.tag

Get insight/journal.tag

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Get insight/journal.tag
        api_response = api_instance.insight_project_journal_tag_get(project_id, location_id, journal_id, tag_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 
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

# **insight_project_journal_tag_list**
> list[Tag] insight_project_journal_tag_list(project_id, location_id, journal_id)

List insight/journal.tag

List insight/journal.tag

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id

    try:
        # List insight/journal.tag
        api_response = api_instance.insight_project_journal_tag_list(project_id, location_id, journal_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 

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

# **insight_project_journal_tag_put**
> list[Tag] insight_project_journal_tag_put(project_id, location_id, journal_id, tag)

Replace insight/journal.tag

Replace insight/journal.tag

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id
tag = [h1-client-python.Tag()] # list[Tag] | 

    try:
        # Replace insight/journal.tag
        api_response = api_instance.insight_project_journal_tag_put(project_id, location_id, journal_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 
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

# **insight_project_journal_transfer**
> Journal insight_project_journal_transfer(project_id, location_id, journal_id, insight_project_journal_transfer, x_idempotency_key=x_idempotency_key)

Transfer insight/journal

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id
insight_project_journal_transfer = h1-client-python.InsightProjectJournalTransfer() # InsightProjectJournalTransfer | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Transfer insight/journal
        api_response = api_instance.insight_project_journal_transfer(project_id, location_id, journal_id, insight_project_journal_transfer, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 
 **insight_project_journal_transfer** | [**InsightProjectJournalTransfer**](InsightProjectJournalTransfer.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Journal**](Journal.md)

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

# **insight_project_journal_update**
> Journal insight_project_journal_update(project_id, location_id, journal_id, insight_project_journal_update)

Update insight/journal

Returns modified journal

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
    api_instance = h1-client-python.InsightProjectJournalApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
journal_id = 'journal_id_example' # str | Journal Id
insight_project_journal_update = h1-client-python.InsightProjectJournalUpdate() # InsightProjectJournalUpdate | 

    try:
        # Update insight/journal
        api_response = api_instance.insight_project_journal_update(project_id, location_id, journal_id, insight_project_journal_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **journal_id** | **str**| Journal Id | 
 **insight_project_journal_update** | [**InsightProjectJournalUpdate**](InsightProjectJournalUpdate.md)|  | 

### Return type

[**Journal**](Journal.md)

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

