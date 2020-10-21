# h1-client-python.BillingProjectReservationApi

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
> Reservation billing_project_reservation_assign(project_id, reservation_id, billing_project_reservation_assign, x_idempotency_key=x_idempotency_key)

Assign billing/reservation

action assign

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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
reservation_id = 'reservation_id_example' # str | Reservation Id
billing_project_reservation_assign = h1-client-python.BillingProjectReservationAssign() # BillingProjectReservationAssign | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Assign billing/reservation
        api_response = api_instance.billing_project_reservation_assign(project_id, reservation_id, billing_project_reservation_assign, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_assign: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **reservation_id** | **str**| Reservation Id | 
 **billing_project_reservation_assign** | [**BillingProjectReservationAssign**](BillingProjectReservationAssign.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

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
> Reservation billing_project_reservation_create(project_id, billing_project_reservation_create, x_idempotency_key=x_idempotency_key)

Create billing/reservation

Create reservation

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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
billing_project_reservation_create = h1-client-python.BillingProjectReservationCreate() # BillingProjectReservationCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create billing/reservation
        api_response = api_instance.billing_project_reservation_create(project_id, billing_project_reservation_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **billing_project_reservation_create** | [**BillingProjectReservationCreate**](BillingProjectReservationCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
reservation_id = 'reservation_id_example' # str | Reservation Id

    try:
        # Delete billing/reservation
        api_instance.billing_project_reservation_delete(project_id, reservation_id)
    except ApiException as e:
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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
reservation_id = 'reservation_id_example' # str | Reservation Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get billing/reservation.event
        api_response = api_instance.billing_project_reservation_event_get(project_id, reservation_id, event_id)
        pprint(api_response)
    except ApiException as e:
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
> list[Event] billing_project_reservation_event_list(project_id, reservation_id, limit=limit, skip=skip)

List billing/reservation.event

List billing/reservation.event

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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
reservation_id = 'reservation_id_example' # str | Reservation Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List billing/reservation.event
        api_response = api_instance.billing_project_reservation_event_list(project_id, reservation_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **reservation_id** | **str**| Reservation Id | 
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

# **billing_project_reservation_extend**
> Reservation billing_project_reservation_extend(project_id, reservation_id, x_idempotency_key=x_idempotency_key)

Extend billing/reservation

action extend

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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
reservation_id = 'reservation_id_example' # str | Reservation Id
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Extend billing/reservation
        api_response = api_instance.billing_project_reservation_extend(project_id, reservation_id, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_extend: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **reservation_id** | **str**| Reservation Id | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
reservation_id = 'reservation_id_example' # str | Reservation Id

    try:
        # Get billing/reservation
        api_response = api_instance.billing_project_reservation_get(project_id, reservation_id)
        pprint(api_response)
    except ApiException as e:
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
> list[Reservation] billing_project_reservation_list(project_id, name=name, tag_value=tag_value, tag_key=tag_key)

List billing/reservation

List reservation

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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
name = 'name_example' # str | Filter by name (optional)
tag_value = 'tag_value_example' # str | Filter by tag.value (optional)
tag_key = 'tag_key_example' # str | Filter by tag.key (optional)

    try:
        # List billing/reservation
        api_response = api_instance.billing_project_reservation_list(project_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except ApiException as e:
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

[**list[Reservation]**](Reservation.md)

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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
reservation_id = 'reservation_id_example' # str | Reservation Id
service_id = 'service_id_example' # str | serviceId

    try:
        # Get billing/reservation.service
        api_response = api_instance.billing_project_reservation_service_get(project_id, reservation_id, service_id)
        pprint(api_response)
    except ApiException as e:
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
> list[ResourceService] billing_project_reservation_service_list(project_id, reservation_id)

List billing/reservation.service

List billing/reservation.service

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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
reservation_id = 'reservation_id_example' # str | Reservation Id

    try:
        # List billing/reservation.service
        api_response = api_instance.billing_project_reservation_service_list(project_id, reservation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **reservation_id** | **str**| Reservation Id | 

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

# **billing_project_reservation_tag_create**
> Tag billing_project_reservation_tag_create(project_id, reservation_id, tag)

Create billing/reservation.tag

Create billing/reservation.tag

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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
reservation_id = 'reservation_id_example' # str | Reservation Id
tag = h1-client-python.Tag() # Tag | 

    try:
        # Create billing/reservation.tag
        api_response = api_instance.billing_project_reservation_tag_create(project_id, reservation_id, tag)
        pprint(api_response)
    except ApiException as e:
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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
reservation_id = 'reservation_id_example' # str | Reservation Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Delete billing/reservation.tag
        api_instance.billing_project_reservation_tag_delete(project_id, reservation_id, tag_id)
    except ApiException as e:
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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
reservation_id = 'reservation_id_example' # str | Reservation Id
tag_id = 'tag_id_example' # str | tagId

    try:
        # Get billing/reservation.tag
        api_response = api_instance.billing_project_reservation_tag_get(project_id, reservation_id, tag_id)
        pprint(api_response)
    except ApiException as e:
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
> list[Tag] billing_project_reservation_tag_list(project_id, reservation_id)

List billing/reservation.tag

List billing/reservation.tag

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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
reservation_id = 'reservation_id_example' # str | Reservation Id

    try:
        # List billing/reservation.tag
        api_response = api_instance.billing_project_reservation_tag_list(project_id, reservation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **reservation_id** | **str**| Reservation Id | 

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

# **billing_project_reservation_tag_put**
> list[Tag] billing_project_reservation_tag_put(project_id, reservation_id, tag)

Replace billing/reservation.tag

Replace billing/reservation.tag

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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
reservation_id = 'reservation_id_example' # str | Reservation Id
tag = [h1-client-python.Tag()] # list[Tag] | 

    try:
        # Replace billing/reservation.tag
        api_response = api_instance.billing_project_reservation_tag_put(project_id, reservation_id, tag)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BillingProjectReservationApi->billing_project_reservation_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **reservation_id** | **str**| Reservation Id | 
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

# **billing_project_reservation_update**
> Reservation billing_project_reservation_update(project_id, reservation_id, billing_project_reservation_update)

Update billing/reservation

Returns modified reservation

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
    api_instance = h1-client-python.BillingProjectReservationApi(api_client)
    project_id = 'project_id_example' # str | Project Id
reservation_id = 'reservation_id_example' # str | Reservation Id
billing_project_reservation_update = h1-client-python.BillingProjectReservationUpdate() # BillingProjectReservationUpdate | 

    try:
        # Update billing/reservation
        api_response = api_instance.billing_project_reservation_update(project_id, reservation_id, billing_project_reservation_update)
        pprint(api_response)
    except ApiException as e:
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

