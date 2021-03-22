# h1.IamOrganisationApi

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
[**iam_organisation_service_get**](IamOrganisationApi.md#iam_organisation_service_get) | **GET** /iam/organisation/{organisationId}/service/{serviceId} | Get iam/organisation.service
[**iam_organisation_service_list**](IamOrganisationApi.md#iam_organisation_service_list) | **GET** /iam/organisation/{organisationId}/service | List iam/organisation.service
[**iam_organisation_transfer_accept**](IamOrganisationApi.md#iam_organisation_transfer_accept) | **POST** /iam/organisation/{organisationId}/transfer/{transferId}/actions/accept | Accept iam/organisation.transfer
[**iam_organisation_transfer_get**](IamOrganisationApi.md#iam_organisation_transfer_get) | **GET** /iam/organisation/{organisationId}/transfer/{transferId} | Get iam/organisation.transfer
[**iam_organisation_transfer_list**](IamOrganisationApi.md#iam_organisation_transfer_list) | **GET** /iam/organisation/{organisationId}/transfer | List iam/organisation.transfer
[**iam_organisation_update**](IamOrganisationApi.md#iam_organisation_update) | **PATCH** /iam/organisation/{organisationId} | Update iam/organisation


# **iam_organisation_billing_list**
> [Billing] iam_organisation_billing_list(organisation_id)

List iam/organisation.billing

List iam/organisation.billing

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
from h1.model.billing import Billing
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    start = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | start (optional)
    end = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | end (optional)
    resource_type = "resource.type_example" # str | resource.type (optional)

    # example passing only required values which don't have defaults set
    try:
        # List iam/organisation.billing
        api_response = api_instance.iam_organisation_billing_list(organisation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_billing_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/organisation.billing
        api_response = api_instance.iam_organisation_billing_list(organisation_id, start=start, end=end, resource_type=resource_type)
        pprint(api_response)
    except h1.ApiException as e:
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

[**[Billing]**](Billing.md)

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
> Organisation iam_organisation_create(iam_organisation_create)

Create iam/organisation

Create organisation

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
from h1.model.iam_organisation_create import IamOrganisationCreate
from h1.model.organisation import Organisation
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    iam_organisation_create = IamOrganisationCreate(
        name="name_example",
        billing=OrganisationBilling(
            nip="nip_example",
            email="email_example",
            company="company_example",
            currency="PLN",
            address=BillingAddress(
                country="PL",
                city="city_example",
                street="street_example",
                zipcode="zipcode_example",
            ),
        ),
    ) # IamOrganisationCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create iam/organisation
        api_response = api_instance.iam_organisation_create(iam_organisation_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create iam/organisation
        api_response = api_instance.iam_organisation_create(iam_organisation_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **iam_organisation_create** | [**IamOrganisationCreate**](IamOrganisationCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

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
import time
import h1
from h1.api import iam_organisation_api
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/organisation
        api_instance.iam_organisation_delete(organisation_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_organisation_api
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/organisation.event
        api_response = api_instance.iam_organisation_event_get(organisation_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Event] iam_organisation_event_list(organisation_id)

List iam/organisation.event

List iam/organisation.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List iam/organisation.event
        api_response = api_instance.iam_organisation_event_list(organisation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/organisation.event
        api_response = api_instance.iam_organisation_event_list(organisation_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_get**
> Organisation iam_organisation_get(organisation_id)

Get iam/organisation

Returns a single organisation

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
from h1.model.organisation import Organisation
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id

    # example passing only required values which don't have defaults set
    try:
        # Get iam/organisation
        api_response = api_instance.iam_organisation_get(organisation_id)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_organisation_api
from h1.model.iam_organisation_invitation_accept import IamOrganisationInvitationAccept
from h1.model.invitation import Invitation
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    invitation_id = "invitationId_example" # str | invitationId
    iam_organisation_invitation_accept = IamOrganisationInvitationAccept(
        token="token_example",
    ) # IamOrganisationInvitationAccept | 

    # example passing only required values which don't have defaults set
    try:
        # Accept iam/organisation.invitation
        api_response = api_instance.iam_organisation_invitation_accept(organisation_id, invitation_id, iam_organisation_invitation_accept)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_organisation_api
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    invitation_id = "invitationId_example" # str | invitationId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/organisation.invitation
        api_instance.iam_organisation_invitation_delete(organisation_id, invitation_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_organisation_api
from h1.model.invitation import Invitation
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    invitation_id = "invitationId_example" # str | invitationId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/organisation.invitation
        api_response = api_instance.iam_organisation_invitation_get(organisation_id, invitation_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Invitation] iam_organisation_invitation_list(organisation_id)

List iam/organisation.invitation

List iam/organisation.invitation

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
from h1.model.invitation import Invitation
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    resource = "resource_example" # str | resource (optional)

    # example passing only required values which don't have defaults set
    try:
        # List iam/organisation.invitation
        api_response = api_instance.iam_organisation_invitation_list(organisation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_invitation_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/organisation.invitation
        api_response = api_instance.iam_organisation_invitation_list(organisation_id, resource=resource)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_invitation_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **resource** | **str**| resource | [optional]

### Return type

[**[Invitation]**](Invitation.md)

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
> file_type iam_organisation_invoice_download(organisation_id, invoice_id)

Download iam/organisation.invoice

action download

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    invoice_id = "invoiceId_example" # str | invoiceId

    # example passing only required values which don't have defaults set
    try:
        # Download iam/organisation.invoice
        api_response = api_instance.iam_organisation_invoice_download(organisation_id, invoice_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_invoice_download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **invoice_id** | **str**| invoiceId |

### Return type

**file_type**

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
> Invoice iam_organisation_invoice_get(organisation_id, invoice_id)

Get iam/organisation.invoice

Get iam/organisation.invoice

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
from h1.model.invoice import Invoice
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    invoice_id = "invoiceId_example" # str | invoiceId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/organisation.invoice
        api_response = api_instance.iam_organisation_invoice_get(organisation_id, invoice_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_invoice_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **invoice_id** | **str**| invoiceId |

### Return type

[**Invoice**](Invoice.md)

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
> [Invoice] iam_organisation_invoice_list(organisation_id)

List iam/organisation.invoice

List iam/organisation.invoice

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
from h1.model.invoice import Invoice
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/organisation.invoice
        api_response = api_instance.iam_organisation_invoice_list(organisation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_invoice_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |

### Return type

[**[Invoice]**](Invoice.md)

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
> [Organisation] iam_organisation_list()

List iam/organisation

List organisation

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
from h1.model.organisation import Organisation
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    name = "name_example" # str | Filter by name (optional)
    billing_company = "billing.company_example" # str | Filter by billing.company (optional)
    limit = 3.14 # float | Filter by $limit (optional)
    active = False # bool | Filter by active (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List iam/organisation
        api_response = api_instance.iam_organisation_list(name=name, billing_company=billing_company, limit=limit, active=active)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter by name | [optional]
 **billing_company** | **str**| Filter by billing.company | [optional]
 **limit** | **float**| Filter by $limit | [optional]
 **active** | **bool**| Filter by active | [optional] if omitted the server will use the default value of False

### Return type

[**[Organisation]**](Organisation.md)

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
import time
import h1
from h1.api import iam_organisation_api
from h1.model.iam_organisation_ownership_create import IamOrganisationOwnershipCreate
from h1.model.organisation import Organisation
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    iam_organisation_ownership_create = IamOrganisationOwnershipCreate(
        email="email_example",
    ) # IamOrganisationOwnershipCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create iam/organisation.ownership
        api_response = api_instance.iam_organisation_ownership_create(organisation_id, iam_organisation_ownership_create)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_organisation_api
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    ownership_id = "ownershipId_example" # str | ownershipId

    # example passing only required values which don't have defaults set
    try:
        # Delete iam/organisation.ownership
        api_instance.iam_organisation_ownership_delete(organisation_id, ownership_id)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_organisation_api
from h1.model.ownership import Ownership
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    ownership_id = "ownershipId_example" # str | ownershipId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/organisation.ownership
        api_response = api_instance.iam_organisation_ownership_get(organisation_id, ownership_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Ownership] iam_organisation_ownership_list(organisation_id)

List iam/organisation.ownership

List iam/organisation.ownership

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
from h1.model.ownership import Ownership
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/organisation.ownership
        api_response = api_instance.iam_organisation_ownership_list(organisation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_ownership_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |

### Return type

[**[Ownership]**](Ownership.md)

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
import time
import h1
from h1.api import iam_organisation_api
from h1.model.payment import Payment
from h1.model.iam_organisation_payment_allocate import IamOrganisationPaymentAllocate
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    payment_id = "paymentId_example" # str | paymentId
    iam_organisation_payment_allocate = IamOrganisationPaymentAllocate(
        project="project_example",
    ) # IamOrganisationPaymentAllocate | 

    # example passing only required values which don't have defaults set
    try:
        # Allocate iam/organisation.payment
        api_response = api_instance.iam_organisation_payment_allocate(organisation_id, payment_id, iam_organisation_payment_allocate)
        pprint(api_response)
    except h1.ApiException as e:
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
import time
import h1
from h1.api import iam_organisation_api
from h1.model.payment import Payment
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    payment_id = "paymentId_example" # str | paymentId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/organisation.payment
        api_response = api_instance.iam_organisation_payment_get(organisation_id, payment_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Payment] iam_organisation_payment_list(organisation_id)

List iam/organisation.payment

List iam/organisation.payment

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
from h1.model.payment import Payment
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/organisation.payment
        api_response = api_instance.iam_organisation_payment_list(organisation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_payment_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |

### Return type

[**[Payment]**](Payment.md)

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
import time
import h1
from h1.api import iam_organisation_api
from h1.model.proforma import Proforma
from h1.model.iam_organisation_proforma_create import IamOrganisationProformaCreate
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    iam_organisation_proforma_create = IamOrganisationProformaCreate(
        amount=1,
        project="project_example",
    ) # IamOrganisationProformaCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create iam/organisation.proforma
        api_response = api_instance.iam_organisation_proforma_create(organisation_id, iam_organisation_proforma_create)
        pprint(api_response)
    except h1.ApiException as e:
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
> file_type iam_organisation_proforma_download(organisation_id, proforma_id)

Download iam/organisation.proforma

action download

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    proforma_id = "proformaId_example" # str | proformaId

    # example passing only required values which don't have defaults set
    try:
        # Download iam/organisation.proforma
        api_response = api_instance.iam_organisation_proforma_download(organisation_id, proforma_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_proforma_download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **proforma_id** | **str**| proformaId |

### Return type

**file_type**

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
import time
import h1
from h1.api import iam_organisation_api
from h1.model.proforma import Proforma
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    proforma_id = "proformaId_example" # str | proformaId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/organisation.proforma
        api_response = api_instance.iam_organisation_proforma_get(organisation_id, proforma_id)
        pprint(api_response)
    except h1.ApiException as e:
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
> [Proforma] iam_organisation_proforma_list(organisation_id)

List iam/organisation.proforma

List iam/organisation.proforma

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
from h1.model.proforma import Proforma
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/organisation.proforma
        api_response = api_instance.iam_organisation_proforma_list(organisation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_proforma_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |

### Return type

[**[Proforma]**](Proforma.md)

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

# **iam_organisation_service_get**
> ResourceService iam_organisation_service_get(organisation_id, service_id)

Get iam/organisation.service

Get iam/organisation.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/organisation.service
        api_response = api_instance.iam_organisation_service_get(organisation_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
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

# **iam_organisation_service_list**
> [ResourceService] iam_organisation_service_list(organisation_id)

List iam/organisation.service

List iam/organisation.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/organisation.service
        api_response = api_instance.iam_organisation_service_list(organisation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |

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

# **iam_organisation_transfer_accept**
> Transfer iam_organisation_transfer_accept(organisation_id, transfer_id, iam_organisation_transfer_accept)

Accept iam/organisation.transfer

action accept

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
from h1.model.iam_organisation_transfer_accept import IamOrganisationTransferAccept
from h1.model.transfer import Transfer
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    transfer_id = "transferId_example" # str | transferId
    iam_organisation_transfer_accept = IamOrganisationTransferAccept(
        payment="payment_example",
    ) # IamOrganisationTransferAccept | 

    # example passing only required values which don't have defaults set
    try:
        # Accept iam/organisation.transfer
        api_response = api_instance.iam_organisation_transfer_accept(organisation_id, transfer_id, iam_organisation_transfer_accept)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_transfer_accept: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **transfer_id** | **str**| transferId |
 **iam_organisation_transfer_accept** | [**IamOrganisationTransferAccept**](IamOrganisationTransferAccept.md)|  |

### Return type

[**Transfer**](Transfer.md)

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

# **iam_organisation_transfer_get**
> Transfer iam_organisation_transfer_get(organisation_id, transfer_id)

Get iam/organisation.transfer

Get iam/organisation.transfer

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
from h1.model.transfer import Transfer
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    transfer_id = "transferId_example" # str | transferId

    # example passing only required values which don't have defaults set
    try:
        # Get iam/organisation.transfer
        api_response = api_instance.iam_organisation_transfer_get(organisation_id, transfer_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_transfer_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |
 **transfer_id** | **str**| transferId |

### Return type

[**Transfer**](Transfer.md)

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

# **iam_organisation_transfer_list**
> [Transfer] iam_organisation_transfer_list(organisation_id)

List iam/organisation.transfer

List iam/organisation.transfer

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
from h1.model.transfer import Transfer
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id

    # example passing only required values which don't have defaults set
    try:
        # List iam/organisation.transfer
        api_response = api_instance.iam_organisation_transfer_list(organisation_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling IamOrganisationApi->iam_organisation_transfer_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organisation_id** | **str**| Organisation Id |

### Return type

[**[Transfer]**](Transfer.md)

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

# **iam_organisation_update**
> Organisation iam_organisation_update(organisation_id, iam_organisation_update)

Update iam/organisation

Returns modified organisation

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import iam_organisation_api
from h1.model.organisation import Organisation
from h1.model.iam_organisation_update import IamOrganisationUpdate
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
    api_instance = iam_organisation_api.IamOrganisationApi(api_client)
    organisation_id = "organisationId_example" # str | Organisation Id
    iam_organisation_update = IamOrganisationUpdate(
        name="name_example",
        billing=OrganisationBilling1(
            email="email_example",
            company="company_example",
            address=BillingAddress1(
                city="city_example",
                zipcode="zipcode_example",
                street="street_example",
            ),
        ),
    ) # IamOrganisationUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update iam/organisation
        api_response = api_instance.iam_organisation_update(organisation_id, iam_organisation_update)
        pprint(api_response)
    except h1.ApiException as e:
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

