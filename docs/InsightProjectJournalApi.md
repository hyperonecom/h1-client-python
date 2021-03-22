# h1.InsightProjectJournalApi

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
> Journal insight_project_journal_create(project_id, location_id, insight_project_journal_create)

Create insight/journal

Create journal

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import insight_project_journal_api
from h1.model.journal import Journal
from h1.model.insight_project_journal_create import InsightProjectJournalCreate
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    insight_project_journal_create = InsightProjectJournalCreate(
        name="name_example",
        service="5c9cc2d0255c16c3e899a4ea",
        retention=3.14,
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # InsightProjectJournalCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create insight/journal
        api_response = api_instance.insight_project_journal_create(project_id, location_id, insight_project_journal_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create insight/journal
        api_response = api_instance.insight_project_journal_create(project_id, location_id, insight_project_journal_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **insight_project_journal_create** | [**InsightProjectJournalCreate**](InsightProjectJournalCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import insight_project_journal_api
from h1.model.journal_credential import JournalCredential
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id
    journal_credential = JournalCredential(
        id="id_example",
        name="name_example",
        created_by="created_by_example",
        created_on=dateutil_parser('1970-01-01T00:00:00.00Z'),
        type="sha512",
        value="value_example",
        fingerprint="fingerprint_example",
        token="token_example",
    ) # JournalCredential | 

    # example passing only required values which don't have defaults set
    try:
        # Create insight/journal.credential
        api_response = api_instance.insight_project_journal_credential_create(project_id, location_id, journal_id, journal_credential)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import insight_project_journal_api
from h1.model.journal import Journal
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Delete insight/journal.credential
        api_response = api_instance.insight_project_journal_credential_delete(project_id, location_id, journal_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import insight_project_journal_api
from h1.model.journal_credential import JournalCredential
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id
    credential_id = "credentialId_example" # str | credentialId

    # example passing only required values which don't have defaults set
    try:
        # Get insight/journal.credential
        api_response = api_instance.insight_project_journal_credential_get(project_id, location_id, journal_id, credential_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [JournalCredential] insight_project_journal_credential_list(project_id, location_id, journal_id)

List insight/journal.credential

List insight/journal.credential

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import insight_project_journal_api
from h1.model.journal_credential import JournalCredential
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id

    # example passing only required values which don't have defaults set
    try:
        # List insight/journal.credential
        api_response = api_instance.insight_project_journal_credential_list(project_id, location_id, journal_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_credential_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **journal_id** | **str**| Journal Id |

### Return type

[**[JournalCredential]**](JournalCredential.md)

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
import time
import h1
from h1.api import insight_project_journal_api
from h1.model.journal_credential import JournalCredential
from h1.model.insight_project_journal_credential_patch import InsightProjectJournalCredentialPatch
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id
    credential_id = "credentialId_example" # str | credentialId
    insight_project_journal_credential_patch = InsightProjectJournalCredentialPatch(
        name="name_example",
    ) # InsightProjectJournalCredentialPatch | 

    # example passing only required values which don't have defaults set
    try:
        # Update insight/journal.credential
        api_response = api_instance.insight_project_journal_credential_patch(project_id, location_id, journal_id, credential_id, insight_project_journal_credential_patch)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import insight_project_journal_api
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id

    # example passing only required values which don't have defaults set
    try:
        # Delete insight/journal
        api_instance.insight_project_journal_delete(project_id, location_id, journal_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import insight_project_journal_api
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get insight/journal.event
        api_response = api_instance.insight_project_journal_event_get(project_id, location_id, journal_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Event] insight_project_journal_event_list(project_id, location_id, journal_id)

List insight/journal.event

List insight/journal.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import insight_project_journal_api
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List insight/journal.event
        api_response = api_instance.insight_project_journal_event_list(project_id, location_id, journal_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List insight/journal.event
        api_response = api_instance.insight_project_journal_event_list(project_id, location_id, journal_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **journal_id** | **str**| Journal Id |
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

# **insight_project_journal_get**
> Journal insight_project_journal_get(project_id, location_id, journal_id)

Get insight/journal

Returns a single journal

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import insight_project_journal_api
from h1.model.journal import Journal
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id

    # example passing only required values which don't have defaults set
    try:
        # Get insight/journal
        api_response = api_instance.insight_project_journal_get(project_id, location_id, journal_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Journal] insight_project_journal_list(project_id, location_id)

List insight/journal

List journal

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import insight_project_journal_api
from h1.model.journal import Journal
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List insight/journal
        api_response = api_instance.insight_project_journal_list(project_id, location_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List insight/journal
        api_response = api_instance.insight_project_journal_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
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

[**[Journal]**](Journal.md)

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
> insight_project_journal_log_get(project_id, location_id, journal_id)

Get insight/journal.log

websocket is also supported

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import insight_project_journal_api
from h1.model.tag_array import TagArray
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id
    since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | since (optional)
    until = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | until (optional)
    follow = False # bool | follow (optional) if omitted the server will use the default value of False
    tail = 3.14 # float | tail (optional)
    tag = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | tag (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get insight/journal.log
        api_instance.insight_project_journal_log_get(project_id, location_id, journal_id)
    except h1.ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_log_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get insight/journal.log
        api_instance.insight_project_journal_log_get(project_id, location_id, journal_id, since=since, until=until, follow=follow, tail=tail, tag=tag)
    except h1.ApiException as e:
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
 **follow** | **bool**| follow | [optional] if omitted the server will use the default value of False
 **tail** | **float**| tail | [optional]
 **tag** | **TagArray**| tag | [optional]

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
import time
import h1
from h1.api import insight_project_journal_api
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get insight/journal.service
        api_response = api_instance.insight_project_journal_service_get(project_id, location_id, journal_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [ResourceService] insight_project_journal_service_list(project_id, location_id, journal_id)

List insight/journal.service

List insight/journal.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import insight_project_journal_api
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id

    # example passing only required values which don't have defaults set
    try:
        # List insight/journal.service
        api_response = api_instance.insight_project_journal_service_list(project_id, location_id, journal_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **journal_id** | **str**| Journal Id |

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

# **insight_project_journal_tag_create**
> Tag insight_project_journal_tag_create(project_id, location_id, journal_id, tag)

Create insight/journal.tag

Create insight/journal.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import insight_project_journal_api
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create insight/journal.tag
        api_response = api_instance.insight_project_journal_tag_create(project_id, location_id, journal_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import insight_project_journal_api
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete insight/journal.tag
        api_instance.insight_project_journal_tag_delete(project_id, location_id, journal_id, tag_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import insight_project_journal_api
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get insight/journal.tag
        api_response = api_instance.insight_project_journal_tag_get(project_id, location_id, journal_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Tag] insight_project_journal_tag_list(project_id, location_id, journal_id)

List insight/journal.tag

List insight/journal.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import insight_project_journal_api
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id

    # example passing only required values which don't have defaults set
    try:
        # List insight/journal.tag
        api_response = api_instance.insight_project_journal_tag_list(project_id, location_id, journal_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_tag_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **journal_id** | **str**| Journal Id |

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

# **insight_project_journal_tag_put**
> [Tag] insight_project_journal_tag_put(project_id, location_id, journal_id, tag_array)

Replace insight/journal.tag

Replace insight/journal.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import insight_project_journal_api
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace insight/journal.tag
        api_response = api_instance.insight_project_journal_tag_put(project_id, location_id, journal_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_tag_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **journal_id** | **str**| Journal Id |
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

# **insight_project_journal_transfer**
> Journal insight_project_journal_transfer(project_id, location_id, journal_id, insight_project_journal_transfer)

Transfer insight/journal

action transfer

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import insight_project_journal_api
from h1.model.journal import Journal
from h1.model.insight_project_journal_transfer import InsightProjectJournalTransfer
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id
    insight_project_journal_transfer = InsightProjectJournalTransfer(
        project="project_example",
    ) # InsightProjectJournalTransfer | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Transfer insight/journal
        api_response = api_instance.insight_project_journal_transfer(project_id, location_id, journal_id, insight_project_journal_transfer)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling InsightProjectJournalApi->insight_project_journal_transfer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Transfer insight/journal
        api_response = api_instance.insight_project_journal_transfer(project_id, location_id, journal_id, insight_project_journal_transfer, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
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
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import insight_project_journal_api
from h1.model.journal import Journal
from h1.model.insight_project_journal_update import InsightProjectJournalUpdate
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
    api_instance = insight_project_journal_api.InsightProjectJournalApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    journal_id = "journalId_example" # str | Journal Id
    insight_project_journal_update = InsightProjectJournalUpdate(
        name="name_example",
        retention=3.14,
    ) # InsightProjectJournalUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update insight/journal
        api_response = api_instance.insight_project_journal_update(project_id, location_id, journal_id, insight_project_journal_update)
        pprint(api_response)
    except h1.ApiException as e:
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

