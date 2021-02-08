# h1.RecoveryProjectPlanApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recovery_project_plan_create**](RecoveryProjectPlanApi.md#recovery_project_plan_create) | **POST** /recovery/{locationId}/project/{projectId}/plan | Create recovery/plan
[**recovery_project_plan_delete**](RecoveryProjectPlanApi.md#recovery_project_plan_delete) | **DELETE** /recovery/{locationId}/project/{projectId}/plan/{planId} | Delete recovery/plan
[**recovery_project_plan_event_get**](RecoveryProjectPlanApi.md#recovery_project_plan_event_get) | **GET** /recovery/{locationId}/project/{projectId}/plan/{planId}/event/{eventId} | Get recovery/plan.event
[**recovery_project_plan_event_list**](RecoveryProjectPlanApi.md#recovery_project_plan_event_list) | **GET** /recovery/{locationId}/project/{projectId}/plan/{planId}/event | List recovery/plan.event
[**recovery_project_plan_get**](RecoveryProjectPlanApi.md#recovery_project_plan_get) | **GET** /recovery/{locationId}/project/{projectId}/plan/{planId} | Get recovery/plan
[**recovery_project_plan_list**](RecoveryProjectPlanApi.md#recovery_project_plan_list) | **GET** /recovery/{locationId}/project/{projectId}/plan | List recovery/plan
[**recovery_project_plan_service_get**](RecoveryProjectPlanApi.md#recovery_project_plan_service_get) | **GET** /recovery/{locationId}/project/{projectId}/plan/{planId}/service/{serviceId} | Get recovery/plan.service
[**recovery_project_plan_service_list**](RecoveryProjectPlanApi.md#recovery_project_plan_service_list) | **GET** /recovery/{locationId}/project/{projectId}/plan/{planId}/service | List recovery/plan.service
[**recovery_project_plan_tag_create**](RecoveryProjectPlanApi.md#recovery_project_plan_tag_create) | **POST** /recovery/{locationId}/project/{projectId}/plan/{planId}/tag | Create recovery/plan.tag
[**recovery_project_plan_tag_delete**](RecoveryProjectPlanApi.md#recovery_project_plan_tag_delete) | **DELETE** /recovery/{locationId}/project/{projectId}/plan/{planId}/tag/{tagId} | Delete recovery/plan.tag
[**recovery_project_plan_tag_get**](RecoveryProjectPlanApi.md#recovery_project_plan_tag_get) | **GET** /recovery/{locationId}/project/{projectId}/plan/{planId}/tag/{tagId} | Get recovery/plan.tag
[**recovery_project_plan_tag_list**](RecoveryProjectPlanApi.md#recovery_project_plan_tag_list) | **GET** /recovery/{locationId}/project/{projectId}/plan/{planId}/tag | List recovery/plan.tag
[**recovery_project_plan_tag_put**](RecoveryProjectPlanApi.md#recovery_project_plan_tag_put) | **PUT** /recovery/{locationId}/project/{projectId}/plan/{planId}/tag | Replace recovery/plan.tag
[**recovery_project_plan_update**](RecoveryProjectPlanApi.md#recovery_project_plan_update) | **PATCH** /recovery/{locationId}/project/{projectId}/plan/{planId} | Update recovery/plan


# **recovery_project_plan_create**
> Plan recovery_project_plan_create(project_id, location_id, recovery_project_plan_create)

Create recovery/plan

Create plan

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_plan_api
from h1.model.recovery_project_plan_create import RecoveryProjectPlanCreate
from h1.model.inline_response400 import InlineResponse400
from h1.model.plan import Plan
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
    api_instance = recovery_project_plan_api.RecoveryProjectPlanApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    recovery_project_plan_create = RecoveryProjectPlanCreate(
        name="name_example",
        window=[
            RecoveryProjectPlanCreateWindow(
                interval="R/2021-01-01T01:00:00Z/P1D",
            ),
        ],
        retention=[
            RecoveryProjectPlanCreateRetention(
                interval="R/2021-01-01T00:00:00Z/P1D",
                count=1,
            ),
        ],
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # RecoveryProjectPlanCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create recovery/plan
        api_response = api_instance.recovery_project_plan_create(project_id, location_id, recovery_project_plan_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create recovery/plan
        api_response = api_instance.recovery_project_plan_create(project_id, location_id, recovery_project_plan_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **recovery_project_plan_create** | [**RecoveryProjectPlanCreate**](RecoveryProjectPlanCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Plan**](Plan.md)

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

# **recovery_project_plan_delete**
> recovery_project_plan_delete(project_id, location_id, plan_id)

Delete recovery/plan

Delete plan

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_plan_api
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
    api_instance = recovery_project_plan_api.RecoveryProjectPlanApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    plan_id = "planId_example" # str | Plan Id

    # example passing only required values which don't have defaults set
    try:
        # Delete recovery/plan
        api_instance.recovery_project_plan_delete(project_id, location_id, plan_id)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **plan_id** | **str**| Plan Id |

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

# **recovery_project_plan_event_get**
> Event recovery_project_plan_event_get(project_id, location_id, plan_id, event_id)

Get recovery/plan.event

Get recovery/plan.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_plan_api
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
    api_instance = recovery_project_plan_api.RecoveryProjectPlanApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    plan_id = "planId_example" # str | Plan Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get recovery/plan.event
        api_response = api_instance.recovery_project_plan_event_get(project_id, location_id, plan_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **plan_id** | **str**| Plan Id |
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

# **recovery_project_plan_event_list**
> [Event] recovery_project_plan_event_list(project_id, location_id, plan_id)

List recovery/plan.event

List recovery/plan.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_plan_api
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
    api_instance = recovery_project_plan_api.RecoveryProjectPlanApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    plan_id = "planId_example" # str | Plan Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List recovery/plan.event
        api_response = api_instance.recovery_project_plan_event_list(project_id, location_id, plan_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List recovery/plan.event
        api_response = api_instance.recovery_project_plan_event_list(project_id, location_id, plan_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **plan_id** | **str**| Plan Id |
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

# **recovery_project_plan_get**
> Plan recovery_project_plan_get(project_id, location_id, plan_id)

Get recovery/plan

Returns a single plan

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_plan_api
from h1.model.inline_response400 import InlineResponse400
from h1.model.plan import Plan
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
    api_instance = recovery_project_plan_api.RecoveryProjectPlanApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    plan_id = "planId_example" # str | Plan Id

    # example passing only required values which don't have defaults set
    try:
        # Get recovery/plan
        api_response = api_instance.recovery_project_plan_get(project_id, location_id, plan_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **plan_id** | **str**| Plan Id |

### Return type

[**Plan**](Plan.md)

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

# **recovery_project_plan_list**
> [Plan] recovery_project_plan_list(project_id, location_id)

List recovery/plan

List plan

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_plan_api
from h1.model.inline_response400 import InlineResponse400
from h1.model.plan import Plan
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
    api_instance = recovery_project_plan_api.RecoveryProjectPlanApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List recovery/plan
        api_response = api_instance.recovery_project_plan_list(project_id, location_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List recovery/plan
        api_response = api_instance.recovery_project_plan_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_list: %s\n" % e)
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

[**[Plan]**](Plan.md)

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

# **recovery_project_plan_service_get**
> ResourceService recovery_project_plan_service_get(project_id, location_id, plan_id, service_id)

Get recovery/plan.service

Get recovery/plan.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_plan_api
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
    api_instance = recovery_project_plan_api.RecoveryProjectPlanApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    plan_id = "planId_example" # str | Plan Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get recovery/plan.service
        api_response = api_instance.recovery_project_plan_service_get(project_id, location_id, plan_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **plan_id** | **str**| Plan Id |
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

# **recovery_project_plan_service_list**
> [ResourceService] recovery_project_plan_service_list(project_id, location_id, plan_id)

List recovery/plan.service

List recovery/plan.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_plan_api
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
    api_instance = recovery_project_plan_api.RecoveryProjectPlanApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    plan_id = "planId_example" # str | Plan Id

    # example passing only required values which don't have defaults set
    try:
        # List recovery/plan.service
        api_response = api_instance.recovery_project_plan_service_list(project_id, location_id, plan_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **plan_id** | **str**| Plan Id |

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

# **recovery_project_plan_tag_create**
> Tag recovery_project_plan_tag_create(project_id, location_id, plan_id, tag)

Create recovery/plan.tag

Create recovery/plan.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_plan_api
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
    api_instance = recovery_project_plan_api.RecoveryProjectPlanApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    plan_id = "planId_example" # str | Plan Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create recovery/plan.tag
        api_response = api_instance.recovery_project_plan_tag_create(project_id, location_id, plan_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **plan_id** | **str**| Plan Id |
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

# **recovery_project_plan_tag_delete**
> recovery_project_plan_tag_delete(project_id, location_id, plan_id, tag_id)

Delete recovery/plan.tag

Delete recovery/plan.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_plan_api
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
    api_instance = recovery_project_plan_api.RecoveryProjectPlanApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    plan_id = "planId_example" # str | Plan Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete recovery/plan.tag
        api_instance.recovery_project_plan_tag_delete(project_id, location_id, plan_id, tag_id)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **plan_id** | **str**| Plan Id |
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

# **recovery_project_plan_tag_get**
> Tag recovery_project_plan_tag_get(project_id, location_id, plan_id, tag_id)

Get recovery/plan.tag

Get recovery/plan.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_plan_api
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
    api_instance = recovery_project_plan_api.RecoveryProjectPlanApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    plan_id = "planId_example" # str | Plan Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get recovery/plan.tag
        api_response = api_instance.recovery_project_plan_tag_get(project_id, location_id, plan_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **plan_id** | **str**| Plan Id |
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

# **recovery_project_plan_tag_list**
> [Tag] recovery_project_plan_tag_list(project_id, location_id, plan_id)

List recovery/plan.tag

List recovery/plan.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_plan_api
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
    api_instance = recovery_project_plan_api.RecoveryProjectPlanApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    plan_id = "planId_example" # str | Plan Id

    # example passing only required values which don't have defaults set
    try:
        # List recovery/plan.tag
        api_response = api_instance.recovery_project_plan_tag_list(project_id, location_id, plan_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **plan_id** | **str**| Plan Id |

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

# **recovery_project_plan_tag_put**
> [Tag] recovery_project_plan_tag_put(project_id, location_id, plan_id, tag_array)

Replace recovery/plan.tag

Replace recovery/plan.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_plan_api
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
    api_instance = recovery_project_plan_api.RecoveryProjectPlanApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    plan_id = "planId_example" # str | Plan Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace recovery/plan.tag
        api_response = api_instance.recovery_project_plan_tag_put(project_id, location_id, plan_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **plan_id** | **str**| Plan Id |
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

# **recovery_project_plan_update**
> Plan recovery_project_plan_update(project_id, location_id, plan_id, recovery_project_plan_update)

Update recovery/plan

Returns modified plan

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_plan_api
from h1.model.recovery_project_plan_update import RecoveryProjectPlanUpdate
from h1.model.inline_response400 import InlineResponse400
from h1.model.plan import Plan
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
    api_instance = recovery_project_plan_api.RecoveryProjectPlanApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    plan_id = "planId_example" # str | Plan Id
    recovery_project_plan_update = RecoveryProjectPlanUpdate(
        name="name_example",
        plan="plan_example",
    ) # RecoveryProjectPlanUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update recovery/plan
        api_response = api_instance.recovery_project_plan_update(project_id, location_id, plan_id, recovery_project_plan_update)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectPlanApi->recovery_project_plan_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **plan_id** | **str**| Plan Id |
 **recovery_project_plan_update** | [**RecoveryProjectPlanUpdate**](RecoveryProjectPlanUpdate.md)|  |

### Return type

[**Plan**](Plan.md)

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

