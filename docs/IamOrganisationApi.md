# h1-client-python.IamOrganisationApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iam_organisation_billing_list**](IamOrganisationApi.md#iam_organisation_billing_list) | **GET** /iam/organisation/{organisationId}/billing | List iam/organisation.billing
[**iam_organisation_create**](IamOrganisationApi.md#iam_organisation_create) | **POST** /iam/organisation | Create iam/organisation
[**iam_organisation_delete**](IamOrganisationApi.md#iam_organisation_delete) | **DELETE** /iam/organisation/{organisationId} | Delete iam/organisation
[**iam_organisation_event_get**](IamOrganisationApi.md#iam_organisation_event_get) | **GET** /iam/organisation/{organisationId}/event/{eventId} | Get iam/organisation.event
[**iam_organisation_event_list**](IamOrganisationApi.md#iam_organisation_event_list) | **GET** /iam/organisation/{organisationId}/event | List iam/organisation.event
[**iam_organisation_get**](IamOrganisationApi.md#iam_organisation_get) | **GET** /iam/organisation/{organisationId} | Get iam/organisation
[**iam_organisation_invitation_accept**](IamOrganisationApi.md#iam_organisation_invitation_accept) | **POST** /iam/organisation/{organisationId}/invitation/{invitationId}/actions/accept | Accept iam/organisation.invitation
[**iam_organisation_invitation_delete**](IamOrganisationApi.md#iam_organisation_invitation_delete) | **DELETE** /iam/organisation/{organisationId}/invitation/{invitationId} | Delete iam/organisation.invitation
[**iam_organisation_invitation_get**](IamOrganisationApi.md#iam_organisation_invitation_get) | **GET** /iam/organisation/{organisationId}/invitation/{invitationId} | Get iam/organisation.invitation
[**iam_organisation_invitation_list**](IamOrganisationApi.md#iam_organisation_invitation_list) | **GET** /iam/organisation/{organisationId}/invitation | List iam/organisation.invitation
[**iam_organisation_invoice_download**](IamOrganisationApi.md#iam_organisation_invoice_download) | **POST** /iam/organisation/{organisationId}/invoice/{invoiceId}/actions/download | Download iam/organisation.invoice
[**iam_organisation_invoice_get**](IamOrganisationApi.md#iam_organisation_invoice_get) | **GET** /iam/organisation/{organisationId}/invoice/{invoiceId} | Get iam/organisation.invoice
[**iam_organisation_invoice_list**](IamOrganisationApi.md#iam_organisation_invoice_list) | **GET** /iam/organisation/{organisationId}/invoice | List iam/organisation.invoice
[**iam_organisation_list**](IamOrganisationApi.md#iam_organisation_list) | **GET** /iam/organisation | List iam/organisation
[**iam_organisation_ownership_create**](IamOrganisationApi.md#iam_organisation_ownership_create) | **POST** /iam/organisation/{organisationId}/ownership | Create iam/organisation.ownership
[**iam_organisation_ownership_delete**](IamOrganisationApi.md#iam_organisation_ownership_delete) | **DELETE** /iam/organisation/{organisationId}/ownership/{ownershipId} | Delete iam/organisation.ownership
[**iam_organisation_ownership_get**](IamOrganisationApi.md#iam_organisation_ownership_get) | **GET** /iam/organisation/{organisationId}/ownership/{ownershipId} | Get iam/organisation.ownership
[**iam_organisation_ownership_list**](IamOrganisationApi.md#iam_organisation_ownership_list) | **GET** /iam/organisation/{organisationId}/ownership | List iam/organisation.ownership
[**iam_organisation_payment_allocate**](IamOrganisationApi.md#iam_organisation_payment_allocate) | **POST** /iam/organisation/{organisationId}/payment/{paymentId}/actions/allocate | Allocate iam/organisation.payment
[**iam_organisation_payment_get**](IamOrganisationApi.md#iam_organisation_payment_get) | **GET** /iam/organisation/{organisationId}/payment/{paymentId} | Get iam/organisation.payment
[**iam_organisation_payment_list**](IamOrganisationApi.md#iam_organisation_payment_list) | **GET** /iam/organisation/{organisationId}/payment | List iam/organisation.payment
[**iam_organisation_proforma_create**](IamOrganisationApi.md#iam_organisation_proforma_create) | **POST** /iam/organisation/{organisationId}/proforma | Create iam/organisation.proforma
[**iam_organisation_proforma_download**](IamOrganisationApi.md#iam_organisation_proforma_download) | **POST** /iam/organisation/{organisationId}/proforma/{proformaId}/actions/download | Download iam/organisation.proforma
[**iam_organisation_proforma_get**](IamOrganisationApi.md#iam_organisation_proforma_get) | **GET** /iam/organisation/{organisationId}/proforma/{proformaId} | Get iam/organisation.proforma
[**iam_organisation_proforma_list**](IamOrganisationApi.md#iam_organisation_proforma_list) | **GET** /iam/organisation/{organisationId}/proforma | List iam/organisation.proforma
[**iam_organisation_transfer_accept**](IamOrganisationApi.md#iam_organisation_transfer_accept) | **POST** /iam/organisation/{organisationId}/actions/transfer_accept | Transfer accept iam/organisation
[**iam_organisation_update**](IamOrganisationApi.md#iam_organisation_update) | **PATCH** /iam/organisation/{organisationId} | Update iam/organisation


# **iam_organisation_billing_list**
> list[Billing] iam_organisation_billing_list(organisation_id, start=start, end=end, resource_type=resource_type)

List iam/organisation.billing

List iam/organisation.billing

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
start = '2013-10-20T19:20:30+01:00' # datetime | start (optional)
end = '2013-10-20T19:20:30+01:00' # datetime | end (optional)
resource_type = 'resource_type_example' # str | resource.type (optional)

    try:
        # List iam/organisation.billing
        api_response = api_instance.iam_organisation_billing_list(organisation_id, start=start, end=end, resource_type=resource_type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_billing_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **start** | **datetime**| start | [optional] 
 **end** | **datetime**| end | [optional] 
 **resource_type** | **str**| resource.type | [optional] 

### Return type

[**list[Billing]**](Billing.md)

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

# **iam_organisation_create**
> Organisation iam_organisation_create(iam_organisation_create, x_idempotency_key=x_idempotency_key)

Create iam/organisation

Create organisation

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    iam_organisation_create = h1-client-python.IamOrganisationCreate() # IamOrganisationCreate | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Create iam/organisation
        api_response = api_instance.iam_organisation_create(iam_organisation_create, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iam_organisation_create** | [**IamOrganisationCreate**](IamOrganisationCreate.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Organisation**](Organisation.md)

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

# **iam_organisation_delete**
> iam_organisation_delete(organisation_id)

Delete iam/organisation

Delete organisation

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id

    try:
        # Delete iam/organisation
        api_instance.iam_organisation_delete(organisation_id)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 

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

# **iam_organisation_event_get**
> Event iam_organisation_event_get(organisation_id, event_id)

Get iam/organisation.event

Get iam/organisation.event

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
event_id = 'event_id_example' # str | eventId

    try:
        # Get iam/organisation.event
        api_response = api_instance.iam_organisation_event_get(organisation_id, event_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
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

# **iam_organisation_event_list**
> list[Event] iam_organisation_event_list(organisation_id, limit=limit, skip=skip)

List iam/organisation.event

List iam/organisation.event

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
limit = 100 # float | $limit (optional) (default to 100)
skip = 3.4 # float | $skip (optional)

    try:
        # List iam/organisation.event
        api_response = api_instance.iam_organisation_event_list(organisation_id, limit=limit, skip=skip)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
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

# **iam_organisation_get**
> Organisation iam_organisation_get(organisation_id)

Get iam/organisation

Returns a single organisation

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id

    try:
        # Get iam/organisation
        api_response = api_instance.iam_organisation_get(organisation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 

### Return type

[**Organisation**](Organisation.md)

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

# **iam_organisation_invitation_accept**
> Invitation iam_organisation_invitation_accept(organisation_id, invitation_id, iam_organisation_invitation_accept)

Accept iam/organisation.invitation

action accept

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
invitation_id = 'invitation_id_example' # str | invitationId
iam_organisation_invitation_accept = h1-client-python.IamOrganisationInvitationAccept() # IamOrganisationInvitationAccept | 

    try:
        # Accept iam/organisation.invitation
        api_response = api_instance.iam_organisation_invitation_accept(organisation_id, invitation_id, iam_organisation_invitation_accept)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_invitation_accept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **invitation_id** | **str**| invitationId | 
 **iam_organisation_invitation_accept** | [**IamOrganisationInvitationAccept**](IamOrganisationInvitationAccept.md)|  | 

### Return type

[**Invitation**](Invitation.md)

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

# **iam_organisation_invitation_delete**
> iam_organisation_invitation_delete(organisation_id, invitation_id)

Delete iam/organisation.invitation

Delete iam/organisation.invitation

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
invitation_id = 'invitation_id_example' # str | invitationId

    try:
        # Delete iam/organisation.invitation
        api_instance.iam_organisation_invitation_delete(organisation_id, invitation_id)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_invitation_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **invitation_id** | **str**| invitationId | 

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

# **iam_organisation_invitation_get**
> Invitation iam_organisation_invitation_get(organisation_id, invitation_id)

Get iam/organisation.invitation

Get iam/organisation.invitation

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
invitation_id = 'invitation_id_example' # str | invitationId

    try:
        # Get iam/organisation.invitation
        api_response = api_instance.iam_organisation_invitation_get(organisation_id, invitation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_invitation_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **invitation_id** | **str**| invitationId | 

### Return type

[**Invitation**](Invitation.md)

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

# **iam_organisation_invitation_list**
> list[Invitation] iam_organisation_invitation_list(organisation_id, resource=resource)

List iam/organisation.invitation

List iam/organisation.invitation

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
resource = 'resource_example' # str | resource (optional)

    try:
        # List iam/organisation.invitation
        api_response = api_instance.iam_organisation_invitation_list(organisation_id, resource=resource)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_invitation_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **resource** | **str**| resource | [optional] 

### Return type

[**list[Invitation]**](Invitation.md)

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

# **iam_organisation_invoice_download**
> file iam_organisation_invoice_download(organisation_id, invoice_id)

Download iam/organisation.invoice

action download

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
invoice_id = 'invoice_id_example' # str | invoiceId

    try:
        # Download iam/organisation.invoice
        api_response = api_instance.iam_organisation_invoice_download(organisation_id, invoice_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_invoice_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **invoice_id** | **str**| invoiceId | 

### Return type

**file**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF file |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iam_organisation_invoice_get**
> Proforma iam_organisation_invoice_get(organisation_id, invoice_id)

Get iam/organisation.invoice

Get iam/organisation.invoice

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
invoice_id = 'invoice_id_example' # str | invoiceId

    try:
        # Get iam/organisation.invoice
        api_response = api_instance.iam_organisation_invoice_get(organisation_id, invoice_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_invoice_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **invoice_id** | **str**| invoiceId | 

### Return type

[**Proforma**](Proforma.md)

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

# **iam_organisation_invoice_list**
> list[Invoice] iam_organisation_invoice_list(organisation_id)

List iam/organisation.invoice

List iam/organisation.invoice

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id

    try:
        # List iam/organisation.invoice
        api_response = api_instance.iam_organisation_invoice_list(organisation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_invoice_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 

### Return type

[**list[Invoice]**](Invoice.md)

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

# **iam_organisation_list**
> list[Organisation] iam_organisation_list(name=name, billing_company=billing_company, limit=limit, active=active)

List iam/organisation

List organisation

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    name = 'name_example' # str | Filter by name (optional)
billing_company = 'billing_company_example' # str | Filter by billing.company (optional)
limit = 3.4 # float | Filter by $limit (optional)
active = False # bool | Filter by active (optional) (default to False)

    try:
        # List iam/organisation
        api_response = api_instance.iam_organisation_list(name=name, billing_company=billing_company, limit=limit, active=active)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter by name | [optional] 
 **billing_company** | **str**| Filter by billing.company | [optional] 
 **limit** | **float**| Filter by $limit | [optional] 
 **active** | **bool**| Filter by active | [optional] [default to False]

### Return type

[**list[Organisation]**](Organisation.md)

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

# **iam_organisation_ownership_create**
> Organisation iam_organisation_ownership_create(organisation_id, iam_organisation_ownership_create)

Create iam/organisation.ownership

Create iam/organisation.ownership

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
iam_organisation_ownership_create = h1-client-python.IamOrganisationOwnershipCreate() # IamOrganisationOwnershipCreate | 

    try:
        # Create iam/organisation.ownership
        api_response = api_instance.iam_organisation_ownership_create(organisation_id, iam_organisation_ownership_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_ownership_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **iam_organisation_ownership_create** | [**IamOrganisationOwnershipCreate**](IamOrganisationOwnershipCreate.md)|  | 

### Return type

[**Organisation**](Organisation.md)

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

# **iam_organisation_ownership_delete**
> iam_organisation_ownership_delete(organisation_id, ownership_id)

Delete iam/organisation.ownership

Delete iam/organisation.ownership

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
ownership_id = 'ownership_id_example' # str | ownershipId

    try:
        # Delete iam/organisation.ownership
        api_instance.iam_organisation_ownership_delete(organisation_id, ownership_id)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_ownership_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **ownership_id** | **str**| ownershipId | 

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

# **iam_organisation_ownership_get**
> Ownership iam_organisation_ownership_get(organisation_id, ownership_id)

Get iam/organisation.ownership

Get iam/organisation.ownership

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
ownership_id = 'ownership_id_example' # str | ownershipId

    try:
        # Get iam/organisation.ownership
        api_response = api_instance.iam_organisation_ownership_get(organisation_id, ownership_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_ownership_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **ownership_id** | **str**| ownershipId | 

### Return type

[**Ownership**](Ownership.md)

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

# **iam_organisation_ownership_list**
> list[Ownership] iam_organisation_ownership_list(organisation_id)

List iam/organisation.ownership

List iam/organisation.ownership

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id

    try:
        # List iam/organisation.ownership
        api_response = api_instance.iam_organisation_ownership_list(organisation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_ownership_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 

### Return type

[**list[Ownership]**](Ownership.md)

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

# **iam_organisation_payment_allocate**
> Payment iam_organisation_payment_allocate(organisation_id, payment_id, iam_organisation_payment_allocate)

Allocate iam/organisation.payment

action allocate

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
payment_id = 'payment_id_example' # str | paymentId
iam_organisation_payment_allocate = h1-client-python.IamOrganisationPaymentAllocate() # IamOrganisationPaymentAllocate | 

    try:
        # Allocate iam/organisation.payment
        api_response = api_instance.iam_organisation_payment_allocate(organisation_id, payment_id, iam_organisation_payment_allocate)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_payment_allocate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **payment_id** | **str**| paymentId | 
 **iam_organisation_payment_allocate** | [**IamOrganisationPaymentAllocate**](IamOrganisationPaymentAllocate.md)|  | 

### Return type

[**Payment**](Payment.md)

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

# **iam_organisation_payment_get**
> Payment iam_organisation_payment_get(organisation_id, payment_id)

Get iam/organisation.payment

Get iam/organisation.payment

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
payment_id = 'payment_id_example' # str | paymentId

    try:
        # Get iam/organisation.payment
        api_response = api_instance.iam_organisation_payment_get(organisation_id, payment_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_payment_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **payment_id** | **str**| paymentId | 

### Return type

[**Payment**](Payment.md)

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

# **iam_organisation_payment_list**
> list[Payment] iam_organisation_payment_list(organisation_id)

List iam/organisation.payment

List iam/organisation.payment

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id

    try:
        # List iam/organisation.payment
        api_response = api_instance.iam_organisation_payment_list(organisation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_payment_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 

### Return type

[**list[Payment]**](Payment.md)

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

# **iam_organisation_proforma_create**
> Proforma iam_organisation_proforma_create(organisation_id, iam_organisation_proforma_create)

Create iam/organisation.proforma

Create iam/organisation.proforma

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
iam_organisation_proforma_create = h1-client-python.IamOrganisationProformaCreate() # IamOrganisationProformaCreate | 

    try:
        # Create iam/organisation.proforma
        api_response = api_instance.iam_organisation_proforma_create(organisation_id, iam_organisation_proforma_create)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_proforma_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **iam_organisation_proforma_create** | [**IamOrganisationProformaCreate**](IamOrganisationProformaCreate.md)|  | 

### Return type

[**Proforma**](Proforma.md)

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

# **iam_organisation_proforma_download**
> file iam_organisation_proforma_download(organisation_id, proforma_id)

Download iam/organisation.proforma

action download

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
proforma_id = 'proforma_id_example' # str | proformaId

    try:
        # Download iam/organisation.proforma
        api_response = api_instance.iam_organisation_proforma_download(organisation_id, proforma_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_proforma_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **proforma_id** | **str**| proformaId | 

### Return type

**file**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | PDF file |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **iam_organisation_proforma_get**
> Proforma iam_organisation_proforma_get(organisation_id, proforma_id)

Get iam/organisation.proforma

Get iam/organisation.proforma

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
proforma_id = 'proforma_id_example' # str | proformaId

    try:
        # Get iam/organisation.proforma
        api_response = api_instance.iam_organisation_proforma_get(organisation_id, proforma_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_proforma_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **proforma_id** | **str**| proformaId | 

### Return type

[**Proforma**](Proforma.md)

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

# **iam_organisation_proforma_list**
> list[Proforma] iam_organisation_proforma_list(organisation_id)

List iam/organisation.proforma

List iam/organisation.proforma

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id

    try:
        # List iam/organisation.proforma
        api_response = api_instance.iam_organisation_proforma_list(organisation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_proforma_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 

### Return type

[**list[Proforma]**](Proforma.md)

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

# **iam_organisation_transfer_accept**
> Organisation iam_organisation_transfer_accept(organisation_id, iam_organisation_transfer_accept, x_idempotency_key=x_idempotency_key)

Transfer accept iam/organisation

action transfer_accept

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
iam_organisation_transfer_accept = h1-client-python.IamOrganisationTransferAccept() # IamOrganisationTransferAccept | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Transfer accept iam/organisation
        api_response = api_instance.iam_organisation_transfer_accept(organisation_id, iam_organisation_transfer_accept, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_transfer_accept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **iam_organisation_transfer_accept** | [**IamOrganisationTransferAccept**](IamOrganisationTransferAccept.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Organisation**](Organisation.md)

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

# **iam_organisation_update**
> Organisation iam_organisation_update(organisation_id, iam_organisation_update)

Update iam/organisation

Returns modified organisation

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
    api_instance = h1-client-python.IamOrganisationApi(api_client)
    organisation_id = 'organisation_id_example' # str | Organisation Id
iam_organisation_update = h1-client-python.IamOrganisationUpdate() # IamOrganisationUpdate | 

    try:
        # Update iam/organisation
        api_response = api_instance.iam_organisation_update(organisation_id, iam_organisation_update)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id | 
 **iam_organisation_update** | [**IamOrganisationUpdate**](IamOrganisationUpdate.md)|  | 

### Return type

[**Organisation**](Organisation.md)

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

