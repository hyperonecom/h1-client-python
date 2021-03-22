# h1.BillingProjectReservationApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_project_reservation_assign**](BillingProjectReservationApi.md#billing_project_reservation_assign) | **POST** /billing/project/{projectId}/reservation/{reservationId}/actions/assign | Assign billing/reservation
[**billing_project_reservation_create**](BillingProjectReservationApi.md#billing_project_reservation_create) | **POST** /billing/project/{projectId}/reservation | Create billing/reservation
[**billing_project_reservation_delete**](BillingProjectReservationApi.md#billing_project_reservation_delete) | **DELETE** /billing/project/{projectId}/reservation/{reservationId} | Delete billing/reservation
[**billing_project_reservation_event_get**](BillingProjectReservationApi.md#billing_project_reservation_event_get) | **GET** /billing/project/{projectId}/reservation/{reservationId}/event/{eventId} | Get billing/reservation.event
[**billing_project_reservation_event_list**](BillingProjectReservationApi.md#billing_project_reservation_event_list) | **GET** /billing/project/{projectId}/reservation/{reservationId}/event | List billing/reservation.event
[**billing_project_reservation_extend**](BillingProjectReservationApi.md#billing_project_reservation_extend) | **POST** /billing/project/{projectId}/reservation/{reservationId}/actions/extend | Extend billing/reservation
[**billing_project_reservation_get**](BillingProjectReservationApi.md#billing_project_reservation_get) | **GET** /billing/project/{projectId}/reservation/{reservationId} | Get billing/reservation
[**billing_project_reservation_list**](BillingProjectReservationApi.md#billing_project_reservation_list) | **GET** /billing/project/{projectId}/reservation | List billing/reservation
[**billing_project_reservation_service_get**](BillingProjectReservationApi.md#billing_project_reservation_service_get) | **GET** /billing/project/{projectId}/reservation/{reservationId}/service/{serviceId} | Get billing/reservation.service
[**billing_project_reservation_service_list**](BillingProjectReservationApi.md#billing_project_reservation_service_list) | **GET** /billing/project/{projectId}/reservation/{reservationId}/service | List billing/reservation.service
[**billing_project_reservation_tag_create**](BillingProjectReservationApi.md#billing_project_reservation_tag_create) | **POST** /billing/project/{projectId}/reservation/{reservationId}/tag | Create billing/reservation.tag
[**billing_project_reservation_tag_delete**](BillingProjectReservationApi.md#billing_project_reservation_tag_delete) | **DELETE** /billing/project/{projectId}/reservation/{reservationId}/tag/{tagId} | Delete billing/reservation.tag
[**billing_project_reservation_tag_get**](BillingProjectReservationApi.md#billing_project_reservation_tag_get) | **GET** /billing/project/{projectId}/reservation/{reservationId}/tag/{tagId} | Get billing/reservation.tag
[**billing_project_reservation_tag_list**](BillingProjectReservationApi.md#billing_project_reservation_tag_list) | **GET** /billing/project/{projectId}/reservation/{reservationId}/tag | List billing/reservation.tag
[**billing_project_reservation_tag_put**](BillingProjectReservationApi.md#billing_project_reservation_tag_put) | **PUT** /billing/project/{projectId}/reservation/{reservationId}/tag | Replace billing/reservation.tag
[**billing_project_reservation_update**](BillingProjectReservationApi.md#billing_project_reservation_update) | **PATCH** /billing/project/{projectId}/reservation/{reservationId} | Update billing/reservation


# **billing_project_reservation_assign**
> Reservation billing_project_reservation_assign(project_id, reservation_id, billing_project_reservation_assign)

Assign billing/reservation

action assign

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
from h1.model.reservation import Reservation
from h1.model.billing_project_reservation_assign import BillingProjectReservationAssign
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    reservation_id = "reservationId_example" # str | Reservation Id
    billing_project_reservation_assign = BillingProjectReservationAssign(
        resource="resource_example",
    ) # BillingProjectReservationAssign | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Assign billing/reservation
        api_response = api_instance.billing_project_reservation_assign(project_id, reservation_id, billing_project_reservation_assign)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_assign: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Assign billing/reservation
        api_response = api_instance.billing_project_reservation_assign(project_id, reservation_id, billing_project_reservation_assign, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_assign: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **reservation_id** | **str**| Reservation Id |
 **billing_project_reservation_assign** | [**BillingProjectReservationAssign**](BillingProjectReservationAssign.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Reservation**](Reservation.md)

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

# **billing_project_reservation_create**
> Reservation billing_project_reservation_create(project_id, billing_project_reservation_create)

Create billing/reservation

Create reservation

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
from h1.model.reservation import Reservation
from h1.model.billing_project_reservation_create import BillingProjectReservationCreate
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    billing_project_reservation_create = BillingProjectReservationCreate(
        name="name_example",
        service="service_example",
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # BillingProjectReservationCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create billing/reservation
        api_response = api_instance.billing_project_reservation_create(project_id, billing_project_reservation_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create billing/reservation
        api_response = api_instance.billing_project_reservation_create(project_id, billing_project_reservation_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **billing_project_reservation_create** | [**BillingProjectReservationCreate**](BillingProjectReservationCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Reservation**](Reservation.md)

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

# **billing_project_reservation_delete**
> billing_project_reservation_delete(project_id, reservation_id)

Delete billing/reservation

Delete reservation

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    reservation_id = "reservationId_example" # str | Reservation Id

    # example passing only required values which don't have defaults set
    try:
        # Delete billing/reservation
        api_instance.billing_project_reservation_delete(project_id, reservation_id)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **reservation_id** | **str**| Reservation Id |

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

# **billing_project_reservation_event_get**
> Event billing_project_reservation_event_get(project_id, reservation_id, event_id)

Get billing/reservation.event

Get billing/reservation.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    reservation_id = "reservationId_example" # str | Reservation Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get billing/reservation.event
        api_response = api_instance.billing_project_reservation_event_get(project_id, reservation_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_event_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **reservation_id** | **str**| Reservation Id |
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

# **billing_project_reservation_event_list**
> [Event] billing_project_reservation_event_list(project_id, reservation_id)

List billing/reservation.event

List billing/reservation.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    reservation_id = "reservationId_example" # str | Reservation Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List billing/reservation.event
        api_response = api_instance.billing_project_reservation_event_list(project_id, reservation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List billing/reservation.event
        api_response = api_instance.billing_project_reservation_event_list(project_id, reservation_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **reservation_id** | **str**| Reservation Id |
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

# **billing_project_reservation_extend**
> Reservation billing_project_reservation_extend(project_id, reservation_id)

Extend billing/reservation

action extend

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
from h1.model.reservation import Reservation
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    reservation_id = "reservationId_example" # str | Reservation Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Extend billing/reservation
        api_response = api_instance.billing_project_reservation_extend(project_id, reservation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_extend: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Extend billing/reservation
        api_response = api_instance.billing_project_reservation_extend(project_id, reservation_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_extend: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **reservation_id** | **str**| Reservation Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Reservation**](Reservation.md)

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

# **billing_project_reservation_get**
> Reservation billing_project_reservation_get(project_id, reservation_id)

Get billing/reservation

Returns a single reservation

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
from h1.model.reservation import Reservation
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    reservation_id = "reservationId_example" # str | Reservation Id

    # example passing only required values which don't have defaults set
    try:
        # Get billing/reservation
        api_response = api_instance.billing_project_reservation_get(project_id, reservation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **reservation_id** | **str**| Reservation Id |

### Return type

[**Reservation**](Reservation.md)

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

# **billing_project_reservation_list**
> [Reservation] billing_project_reservation_list(project_id)

List billing/reservation

List reservation

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
from h1.model.reservation import Reservation
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List billing/reservation
        api_response = api_instance.billing_project_reservation_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List billing/reservation
        api_response = api_instance.billing_project_reservation_list(project_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **name** | **str**| Filter by name | [optional]
 **tag_value** | **str**| Filter by tag.value | [optional]
 **tag_key** | **str**| Filter by tag.key | [optional]

### Return type

[**[Reservation]**](Reservation.md)

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

# **billing_project_reservation_service_get**
> ResourceService billing_project_reservation_service_get(project_id, reservation_id, service_id)

Get billing/reservation.service

Get billing/reservation.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    reservation_id = "reservationId_example" # str | Reservation Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get billing/reservation.service
        api_response = api_instance.billing_project_reservation_service_get(project_id, reservation_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **reservation_id** | **str**| Reservation Id |
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

# **billing_project_reservation_service_list**
> [ResourceService] billing_project_reservation_service_list(project_id, reservation_id)

List billing/reservation.service

List billing/reservation.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    reservation_id = "reservationId_example" # str | Reservation Id

    # example passing only required values which don't have defaults set
    try:
        # List billing/reservation.service
        api_response = api_instance.billing_project_reservation_service_list(project_id, reservation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **reservation_id** | **str**| Reservation Id |

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

# **billing_project_reservation_tag_create**
> Tag billing_project_reservation_tag_create(project_id, reservation_id, tag)

Create billing/reservation.tag

Create billing/reservation.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    reservation_id = "reservationId_example" # str | Reservation Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create billing/reservation.tag
        api_response = api_instance.billing_project_reservation_tag_create(project_id, reservation_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_tag_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **reservation_id** | **str**| Reservation Id |
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

# **billing_project_reservation_tag_delete**
> billing_project_reservation_tag_delete(project_id, reservation_id, tag_id)

Delete billing/reservation.tag

Delete billing/reservation.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    reservation_id = "reservationId_example" # str | Reservation Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete billing/reservation.tag
        api_instance.billing_project_reservation_tag_delete(project_id, reservation_id, tag_id)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_tag_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **reservation_id** | **str**| Reservation Id |
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

# **billing_project_reservation_tag_get**
> Tag billing_project_reservation_tag_get(project_id, reservation_id, tag_id)

Get billing/reservation.tag

Get billing/reservation.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    reservation_id = "reservationId_example" # str | Reservation Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get billing/reservation.tag
        api_response = api_instance.billing_project_reservation_tag_get(project_id, reservation_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_tag_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **reservation_id** | **str**| Reservation Id |
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

# **billing_project_reservation_tag_list**
> [Tag] billing_project_reservation_tag_list(project_id, reservation_id)

List billing/reservation.tag

List billing/reservation.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    reservation_id = "reservationId_example" # str | Reservation Id

    # example passing only required values which don't have defaults set
    try:
        # List billing/reservation.tag
        api_response = api_instance.billing_project_reservation_tag_list(project_id, reservation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_tag_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **reservation_id** | **str**| Reservation Id |

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

# **billing_project_reservation_tag_put**
> [Tag] billing_project_reservation_tag_put(project_id, reservation_id, tag_array)

Replace billing/reservation.tag

Replace billing/reservation.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    reservation_id = "reservationId_example" # str | Reservation Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace billing/reservation.tag
        api_response = api_instance.billing_project_reservation_tag_put(project_id, reservation_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_tag_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **reservation_id** | **str**| Reservation Id |
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

# **billing_project_reservation_update**
> Reservation billing_project_reservation_update(project_id, reservation_id, billing_project_reservation_update)

Update billing/reservation

Returns modified reservation

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_reservation_api
from h1.model.reservation import Reservation
from h1.model.billing_project_reservation_update import BillingProjectReservationUpdate
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
    api_instance = billing_project_reservation_api.BillingProjectReservationApi(api_client)
    project_id = "projectId_example" # str | Project Id
    reservation_id = "reservationId_example" # str | Reservation Id
    billing_project_reservation_update = BillingProjectReservationUpdate(
        name="name_example",
    ) # BillingProjectReservationUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update billing/reservation
        api_response = api_instance.billing_project_reservation_update(project_id, reservation_id, billing_project_reservation_update)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **reservation_id** | **str**| Reservation Id |
 **billing_project_reservation_update** | [**BillingProjectReservationUpdate**](BillingProjectReservationUpdate.md)|  |

### Return type

[**Reservation**](Reservation.md)

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

