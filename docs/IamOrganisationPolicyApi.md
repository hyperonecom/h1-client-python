# h1.IamOrganisationPolicyApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iam_organisation_policy_actor_create**](IamOrganisationPolicyApi.md#iam_organisation_policy_actor_create) | **POST** /iam/organisation/{organisationId}/policy/{policyId}/actor | Create iam/policy.actor
[**iam_organisation_policy_actor_delete**](IamOrganisationPolicyApi.md#iam_organisation_policy_actor_delete) | **DELETE** /iam/organisation/{organisationId}/policy/{policyId}/actor/{actorId} | Delete iam/policy.actor
[**iam_organisation_policy_actor_get**](IamOrganisationPolicyApi.md#iam_organisation_policy_actor_get) | **GET** /iam/organisation/{organisationId}/policy/{policyId}/actor/{actorId} | Get iam/policy.actor
[**iam_organisation_policy_actor_list**](IamOrganisationPolicyApi.md#iam_organisation_policy_actor_list) | **GET** /iam/organisation/{organisationId}/policy/{policyId}/actor | List iam/policy.actor
[**iam_organisation_policy_create**](IamOrganisationPolicyApi.md#iam_organisation_policy_create) | **POST** /iam/organisation/{organisationId}/policy | Create iam/policy
[**iam_organisation_policy_delete**](IamOrganisationPolicyApi.md#iam_organisation_policy_delete) | **DELETE** /iam/organisation/{organisationId}/policy/{policyId} | Delete iam/policy
[**iam_organisation_policy_event_get**](IamOrganisationPolicyApi.md#iam_organisation_policy_event_get) | **GET** /iam/organisation/{organisationId}/policy/{policyId}/event/{eventId} | Get iam/policy.event
[**iam_organisation_policy_event_list**](IamOrganisationPolicyApi.md#iam_organisation_policy_event_list) | **GET** /iam/organisation/{organisationId}/policy/{policyId}/event | List iam/policy.event
[**iam_organisation_policy_get**](IamOrganisationPolicyApi.md#iam_organisation_policy_get) | **GET** /iam/organisation/{organisationId}/policy/{policyId} | Get iam/policy
[**iam_organisation_policy_list**](IamOrganisationPolicyApi.md#iam_organisation_policy_list) | **GET** /iam/organisation/{organisationId}/policy | List iam/policy
[**iam_organisation_policy_service_get**](IamOrganisationPolicyApi.md#iam_organisation_policy_service_get) | **GET** /iam/organisation/{organisationId}/policy/{policyId}/service/{serviceId} | Get iam/policy.service
[**iam_organisation_policy_service_list**](IamOrganisationPolicyApi.md#iam_organisation_policy_service_list) | **GET** /iam/organisation/{organisationId}/policy/{policyId}/service | List iam/policy.service
[**iam_organisation_policy_tag_create**](IamOrganisationPolicyApi.md#iam_organisation_policy_tag_create) | **POST** /iam/organisation/{organisationId}/policy/{policyId}/tag | Create iam/policy.tag
[**iam_organisation_policy_tag_delete**](IamOrganisationPolicyApi.md#iam_organisation_policy_tag_delete) | **DELETE** /iam/organisation/{organisationId}/policy/{policyId}/tag/{tagId} | Delete iam/policy.tag
[**iam_organisation_policy_tag_get**](IamOrganisationPolicyApi.md#iam_organisation_policy_tag_get) | **GET** /iam/organisation/{organisationId}/policy/{policyId}/tag/{tagId} | Get iam/policy.tag
[**iam_organisation_policy_tag_list**](IamOrganisationPolicyApi.md#iam_organisation_policy_tag_list) | **GET** /iam/organisation/{organisationId}/policy/{policyId}/tag | List iam/policy.tag
[**iam_organisation_policy_tag_put**](IamOrganisationPolicyApi.md#iam_organisation_policy_tag_put) | **PUT** /iam/organisation/{organisationId}/policy/{policyId}/tag | Replace iam/policy.tag
[**iam_organisation_policy_update**](IamOrganisationPolicyApi.md#iam_organisation_policy_update) | **PATCH** /iam/organisation/{organisationId}/policy/{policyId} | Update iam/policy


# **iam_organisation_policy_actor_create**
> IamActor iam_organisation_policy_actor_create(organisation_id, policy_id, iam_actor)

Create iam/policy.actor

Create iam/policy.actor

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
from h1.model.iam_actor import IamActor
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id
    iam_actor = IamActor(
        id="id_example",
        value="value_example",
    ) # IamActor | 

    # example passing only required values which don't have defaults set
    try:
        # Create iam/policy.actor
        api_response = api_instance.iam_organisation_policy_actor_create(organisation_id, policy_id, iam_actor)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_actor_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |
 **iam_actor** | [**IamActor**](IamActor.md)|  |

### Return type

[**IamActor**](IamActor.md)

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

# **iam_organisation_policy_actor_delete**
> IamActor iam_organisation_policy_actor_delete(organisation_id, policy_id, actor_id)

Delete iam/policy.actor

Delete iam/policy.actor

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
from h1.model.iam_actor import IamActor
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id
    actor_id = "actorId_example" # str | actorId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/policy.actor
        api_response = api_instance.iam_organisation_policy_actor_delete(organisation_id, policy_id, actor_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_actor_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |
 **actor_id** | **str**| actorId |

### Return type

[**IamActor**](IamActor.md)

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

# **iam_organisation_policy_actor_get**
> IamActor iam_organisation_policy_actor_get(organisation_id, policy_id, actor_id)

Get iam/policy.actor

Get iam/policy.actor

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
from h1.model.iam_actor import IamActor
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id
    actor_id = "actorId_example" # str | actorId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/policy.actor
        api_response = api_instance.iam_organisation_policy_actor_get(organisation_id, policy_id, actor_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_actor_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |
 **actor_id** | **str**| actorId |

### Return type

[**IamActor**](IamActor.md)

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

# **iam_organisation_policy_actor_list**
> [IamActor] iam_organisation_policy_actor_list(organisation_id, policy_id)

List iam/policy.actor

List iam/policy.actor

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
from h1.model.iam_actor import IamActor
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/policy.actor
        api_response = api_instance.iam_organisation_policy_actor_list(organisation_id, policy_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_actor_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |

### Return type

[**[IamActor]**](IamActor.md)

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

# **iam_organisation_policy_create**
> Policy iam_organisation_policy_create(organisation_id, iam_project_policy_create)

Create iam/policy

Create policy

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
from h1.model.iam_project_policy_create import IamProjectPolicyCreate
from h1.model.policy import Policy
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    iam_project_policy_create = IamProjectPolicyCreate(
        name="name_example",
        role="role_example",
        resource="resource_example",
        actor=[
            IamProjectPolicyCreateActor(
                value="value_example",
            ),
        ],
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # IamProjectPolicyCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create iam/policy
        api_response = api_instance.iam_organisation_policy_create(organisation_id, iam_project_policy_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create iam/policy
        api_response = api_instance.iam_organisation_policy_create(organisation_id, iam_project_policy_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **iam_project_policy_create** | [**IamProjectPolicyCreate**](IamProjectPolicyCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Policy**](Policy.md)

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

# **iam_organisation_policy_delete**
> iam_organisation_policy_delete(organisation_id, policy_id)

Delete iam/policy

Delete policy

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/policy
        api_instance.iam_organisation_policy_delete(organisation_id, policy_id)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |

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

# **iam_organisation_policy_event_get**
> Event iam_organisation_policy_event_get(organisation_id, policy_id, event_id)

Get iam/policy.event

Get iam/policy.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/policy.event
        api_response = api_instance.iam_organisation_policy_event_get(organisation_id, policy_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_event_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |
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

# **iam_organisation_policy_event_list**
> [Event] iam_organisation_policy_event_list(organisation_id, policy_id)

List iam/policy.event

List iam/policy.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List iam/policy.event
        api_response = api_instance.iam_organisation_policy_event_list(organisation_id, policy_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/policy.event
        api_response = api_instance.iam_organisation_policy_event_list(organisation_id, policy_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |
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

# **iam_organisation_policy_get**
> Policy iam_organisation_policy_get(organisation_id, policy_id)

Get iam/policy

Returns a single policy

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
from h1.model.policy import Policy
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        # Get iam/policy
        api_response = api_instance.iam_organisation_policy_get(organisation_id, policy_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |

### Return type

[**Policy**](Policy.md)

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

# **iam_organisation_policy_list**
> [Policy] iam_organisation_policy_list(organisation_id)

List iam/policy

List policy

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
from h1.model.policy import Policy
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    name = "name_example" # str | Filter by name (optional)
    resource = "resource_example" # str | Filter by resource (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List iam/policy
        api_response = api_instance.iam_organisation_policy_list(organisation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/policy
        api_response = api_instance.iam_organisation_policy_list(organisation_id, name=name, resource=resource, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **name** | **str**| Filter by name | [optional]
 **resource** | **str**| Filter by resource | [optional]
 **tag_value** | **str**| Filter by tag.value | [optional]
 **tag_key** | **str**| Filter by tag.key | [optional]

### Return type

[**[Policy]**](Policy.md)

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

# **iam_organisation_policy_service_get**
> ResourceService iam_organisation_policy_service_get(organisation_id, policy_id, service_id)

Get iam/policy.service

Get iam/policy.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/policy.service
        api_response = api_instance.iam_organisation_policy_service_get(organisation_id, policy_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |
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

# **iam_organisation_policy_service_list**
> [ResourceService] iam_organisation_policy_service_list(organisation_id, policy_id)

List iam/policy.service

List iam/policy.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/policy.service
        api_response = api_instance.iam_organisation_policy_service_list(organisation_id, policy_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |

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

# **iam_organisation_policy_tag_create**
> Tag iam_organisation_policy_tag_create(organisation_id, policy_id, tag)

Create iam/policy.tag

Create iam/policy.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create iam/policy.tag
        api_response = api_instance.iam_organisation_policy_tag_create(organisation_id, policy_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_tag_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |
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

# **iam_organisation_policy_tag_delete**
> iam_organisation_policy_tag_delete(organisation_id, policy_id, tag_id)

Delete iam/policy.tag

Delete iam/policy.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/policy.tag
        api_instance.iam_organisation_policy_tag_delete(organisation_id, policy_id, tag_id)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_tag_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |
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

# **iam_organisation_policy_tag_get**
> Tag iam_organisation_policy_tag_get(organisation_id, policy_id, tag_id)

Get iam/policy.tag

Get iam/policy.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/policy.tag
        api_response = api_instance.iam_organisation_policy_tag_get(organisation_id, policy_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_tag_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |
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

# **iam_organisation_policy_tag_list**
> [Tag] iam_organisation_policy_tag_list(organisation_id, policy_id)

List iam/policy.tag

List iam/policy.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/policy.tag
        api_response = api_instance.iam_organisation_policy_tag_list(organisation_id, policy_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_tag_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |

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

# **iam_organisation_policy_tag_put**
> [Tag] iam_organisation_policy_tag_put(organisation_id, policy_id, tag_array)

Replace iam/policy.tag

Replace iam/policy.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace iam/policy.tag
        api_response = api_instance.iam_organisation_policy_tag_put(organisation_id, policy_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_tag_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |
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

# **iam_organisation_policy_update**
> Policy iam_organisation_policy_update(organisation_id, policy_id, iam_project_policy_update)

Update iam/policy

Returns modified policy

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_policy_api
from h1.model.iam_project_policy_update import IamProjectPolicyUpdate
from h1.model.policy import Policy
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
    api_instance = iam_organisation_policy_api.IamOrganisationPolicyApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    policy_id = "policyId_example" # str | Policy Id
    iam_project_policy_update = IamProjectPolicyUpdate(
        name="name_example",
    ) # IamProjectPolicyUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update iam/policy
        api_response = api_instance.iam_organisation_policy_update(organisation_id, policy_id, iam_project_policy_update)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationPolicyApi->iam_organisation_policy_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **policy_id** | **str**| Policy Id |
 **iam_project_policy_update** | [**IamProjectPolicyUpdate**](IamProjectPolicyUpdate.md)|  |

### Return type

[**Policy**](Policy.md)

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

