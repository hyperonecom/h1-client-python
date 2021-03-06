# h1.BillingProjectServiceApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**billing_project_service_get**](BillingProjectServiceApi.md#billing_project_service_get) | **GET** /billing/project/{projectId}/service/{serviceId} | Get billing/service
[**billing_project_service_list**](BillingProjectServiceApi.md#billing_project_service_list) | **GET** /billing/project/{projectId}/service | List billing/service


# **billing_project_service_get**
> Service billing_project_service_get(project_id, service_id)

Get billing/service

Returns a single service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_service_api
from h1.model.service import Service
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
    api_instance = billing_project_service_api.BillingProjectServiceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    service_id = "serviceId_example" # str | Service Id

    # example passing only required values which don't have defaults set
    try:
        # Get billing/service
        api_response = api_instance.billing_project_service_get(project_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectServiceApi->billing_project_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **service_id** | **str**| Service Id |

### Return type

[**Service**](Service.md)

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

# **billing_project_service_list**
> [Service] billing_project_service_list(project_id)

List billing/service

List service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import billing_project_service_api
from h1.model.service import Service
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
    api_instance = billing_project_service_api.BillingProjectServiceApi(api_client)
    project_id = "projectId_example" # str | Project Id
    kind = "kind_example" # str | Filter by kind (optional)
    name = "name_example" # str | Filter by name (optional)
    type = "type_example" # str | Filter by type (optional)

    # example passing only required values which don't have defaults set
    try:
        # List billing/service
        api_response = api_instance.billing_project_service_list(project_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectServiceApi->billing_project_service_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List billing/service
        api_response = api_instance.billing_project_service_list(project_id, kind=kind, name=name, type=type)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling BillingProjectServiceApi->billing_project_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **kind** | **str**| Filter by kind | [optional]
 **name** | **str**| Filter by name | [optional]
 **type** | **str**| Filter by type | [optional]

### Return type

[**[Service]**](Service.md)

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

