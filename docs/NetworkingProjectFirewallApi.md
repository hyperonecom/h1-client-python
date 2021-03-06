# h1.NetworkingProjectFirewallApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**networking_project_firewall_create**](NetworkingProjectFirewallApi.md#networking_project_firewall_create) | **POST** /networking/{locationId}/project/{projectId}/firewall | Create networking/firewall
[**networking_project_firewall_delete**](NetworkingProjectFirewallApi.md#networking_project_firewall_delete) | **DELETE** /networking/{locationId}/project/{projectId}/firewall/{firewallId} | Delete networking/firewall
[**networking_project_firewall_egress_create**](NetworkingProjectFirewallApi.md#networking_project_firewall_egress_create) | **POST** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/egress | Create networking/firewall.egress
[**networking_project_firewall_egress_delete**](NetworkingProjectFirewallApi.md#networking_project_firewall_egress_delete) | **DELETE** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/egress/{egressId} | Delete networking/firewall.egress
[**networking_project_firewall_egress_get**](NetworkingProjectFirewallApi.md#networking_project_firewall_egress_get) | **GET** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/egress/{egressId} | Get networking/firewall.egress
[**networking_project_firewall_egress_list**](NetworkingProjectFirewallApi.md#networking_project_firewall_egress_list) | **GET** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/egress | List networking/firewall.egress
[**networking_project_firewall_egress_put**](NetworkingProjectFirewallApi.md#networking_project_firewall_egress_put) | **PUT** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/egress | Replace networking/firewall.egress
[**networking_project_firewall_event_get**](NetworkingProjectFirewallApi.md#networking_project_firewall_event_get) | **GET** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/event/{eventId} | Get networking/firewall.event
[**networking_project_firewall_event_list**](NetworkingProjectFirewallApi.md#networking_project_firewall_event_list) | **GET** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/event | List networking/firewall.event
[**networking_project_firewall_get**](NetworkingProjectFirewallApi.md#networking_project_firewall_get) | **GET** /networking/{locationId}/project/{projectId}/firewall/{firewallId} | Get networking/firewall
[**networking_project_firewall_ingress_create**](NetworkingProjectFirewallApi.md#networking_project_firewall_ingress_create) | **POST** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/ingress | Create networking/firewall.ingress
[**networking_project_firewall_ingress_delete**](NetworkingProjectFirewallApi.md#networking_project_firewall_ingress_delete) | **DELETE** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/ingress/{ingressId} | Delete networking/firewall.ingress
[**networking_project_firewall_ingress_get**](NetworkingProjectFirewallApi.md#networking_project_firewall_ingress_get) | **GET** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/ingress/{ingressId} | Get networking/firewall.ingress
[**networking_project_firewall_ingress_list**](NetworkingProjectFirewallApi.md#networking_project_firewall_ingress_list) | **GET** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/ingress | List networking/firewall.ingress
[**networking_project_firewall_ingress_put**](NetworkingProjectFirewallApi.md#networking_project_firewall_ingress_put) | **PUT** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/ingress | Replace networking/firewall.ingress
[**networking_project_firewall_list**](NetworkingProjectFirewallApi.md#networking_project_firewall_list) | **GET** /networking/{locationId}/project/{projectId}/firewall | List networking/firewall
[**networking_project_firewall_service_get**](NetworkingProjectFirewallApi.md#networking_project_firewall_service_get) | **GET** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/service/{serviceId} | Get networking/firewall.service
[**networking_project_firewall_service_list**](NetworkingProjectFirewallApi.md#networking_project_firewall_service_list) | **GET** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/service | List networking/firewall.service
[**networking_project_firewall_tag_create**](NetworkingProjectFirewallApi.md#networking_project_firewall_tag_create) | **POST** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/tag | Create networking/firewall.tag
[**networking_project_firewall_tag_delete**](NetworkingProjectFirewallApi.md#networking_project_firewall_tag_delete) | **DELETE** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/tag/{tagId} | Delete networking/firewall.tag
[**networking_project_firewall_tag_get**](NetworkingProjectFirewallApi.md#networking_project_firewall_tag_get) | **GET** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/tag/{tagId} | Get networking/firewall.tag
[**networking_project_firewall_tag_list**](NetworkingProjectFirewallApi.md#networking_project_firewall_tag_list) | **GET** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/tag | List networking/firewall.tag
[**networking_project_firewall_tag_put**](NetworkingProjectFirewallApi.md#networking_project_firewall_tag_put) | **PUT** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/tag | Replace networking/firewall.tag
[**networking_project_firewall_transfer**](NetworkingProjectFirewallApi.md#networking_project_firewall_transfer) | **POST** /networking/{locationId}/project/{projectId}/firewall/{firewallId}/actions/transfer | Transfer networking/firewall
[**networking_project_firewall_update**](NetworkingProjectFirewallApi.md#networking_project_firewall_update) | **PATCH** /networking/{locationId}/project/{projectId}/firewall/{firewallId} | Update networking/firewall


# **networking_project_firewall_create**
> Firewall networking_project_firewall_create(project_id, location_id, networking_project_firewall_create)

Create networking/firewall

Create firewall

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
from h1.model.firewall import Firewall
from h1.model.networking_project_firewall_create import NetworkingProjectFirewallCreate
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    networking_project_firewall_create = NetworkingProjectFirewallCreate(
        name="name_example",
        service="5bacaf7202deee0c100eda3b",
        ingress=NetworkingRuleArray([
            NetworkingRule(
                id="id_example",
                name="name_example",
                action="allow",
                priority=3.14,
                filter=[
                    "filter_example",
                ],
                external=["0.0.0.0/0"],
                internal=["*"],
            ),
        ]),
        egress=NetworkingRuleArray(NetworkingRuleArray),
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # NetworkingProjectFirewallCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create networking/firewall
        api_response = api_instance.networking_project_firewall_create(project_id, location_id, networking_project_firewall_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create networking/firewall
        api_response = api_instance.networking_project_firewall_create(project_id, location_id, networking_project_firewall_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **networking_project_firewall_create** | [**NetworkingProjectFirewallCreate**](NetworkingProjectFirewallCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Firewall**](Firewall.md)

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

# **networking_project_firewall_delete**
> networking_project_firewall_delete(project_id, location_id, firewall_id)

Delete networking/firewall

Delete firewall

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id

    # example passing only required values which don't have defaults set
    try:
        # Delete networking/firewall
        api_instance.networking_project_firewall_delete(project_id, location_id, firewall_id)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |

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

# **networking_project_firewall_egress_create**
> NetworkingRule networking_project_firewall_egress_create(project_id, location_id, firewall_id, networking_rule)

Create networking/firewall.egress

Create networking/firewall.egress

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
from h1.model.networking_rule import NetworkingRule
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    networking_rule = NetworkingRule(
        id="id_example",
        name="name_example",
        action="allow",
        priority=3.14,
        filter=[
            "filter_example",
        ],
        external=["0.0.0.0/0"],
        internal=["*"],
    ) # NetworkingRule | 

    # example passing only required values which don't have defaults set
    try:
        # Create networking/firewall.egress
        api_response = api_instance.networking_project_firewall_egress_create(project_id, location_id, firewall_id, networking_rule)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_egress_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
 **networking_rule** | [**NetworkingRule**](NetworkingRule.md)|  |

### Return type

[**NetworkingRule**](NetworkingRule.md)

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

# **networking_project_firewall_egress_delete**
> networking_project_firewall_egress_delete(project_id, location_id, firewall_id, egress_id)

Delete networking/firewall.egress

Delete networking/firewall.egress

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    egress_id = "egressId_example" # str | egressId

    # example passing only required values which don't have defaults set
    try:
        # Delete networking/firewall.egress
        api_instance.networking_project_firewall_egress_delete(project_id, location_id, firewall_id, egress_id)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_egress_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
 **egress_id** | **str**| egressId |

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

# **networking_project_firewall_egress_get**
> NetworkingRule networking_project_firewall_egress_get(project_id, location_id, firewall_id, egress_id)

Get networking/firewall.egress

Get networking/firewall.egress

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
from h1.model.networking_rule import NetworkingRule
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    egress_id = "egressId_example" # str | egressId

    # example passing only required values which don't have defaults set
    try:
        # Get networking/firewall.egress
        api_response = api_instance.networking_project_firewall_egress_get(project_id, location_id, firewall_id, egress_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_egress_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
 **egress_id** | **str**| egressId |

### Return type

[**NetworkingRule**](NetworkingRule.md)

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

# **networking_project_firewall_egress_list**
> [NetworkingRule] networking_project_firewall_egress_list(project_id, location_id, firewall_id)

List networking/firewall.egress

List networking/firewall.egress

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
from h1.model.networking_rule import NetworkingRule
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id

    # example passing only required values which don't have defaults set
    try:
        # List networking/firewall.egress
        api_response = api_instance.networking_project_firewall_egress_list(project_id, location_id, firewall_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_egress_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |

### Return type

[**[NetworkingRule]**](NetworkingRule.md)

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

# **networking_project_firewall_egress_put**
> [NetworkingRule] networking_project_firewall_egress_put(project_id, location_id, firewall_id, networking_rule_array)

Replace networking/firewall.egress

Replace networking/firewall.egress

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
from h1.model.networking_rule_array import NetworkingRuleArray
from h1.model.networking_rule import NetworkingRule
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    networking_rule_array = NetworkingRuleArray([
        NetworkingRule(
            id="id_example",
            name="name_example",
            action="allow",
            priority=3.14,
            filter=[
                "filter_example",
            ],
            external=["0.0.0.0/0"],
            internal=["*"],
        ),
    ]) # NetworkingRuleArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace networking/firewall.egress
        api_response = api_instance.networking_project_firewall_egress_put(project_id, location_id, firewall_id, networking_rule_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_egress_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
 **networking_rule_array** | [**NetworkingRuleArray**](NetworkingRuleArray.md)|  |

### Return type

[**[NetworkingRule]**](NetworkingRule.md)

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

# **networking_project_firewall_event_get**
> Event networking_project_firewall_event_get(project_id, location_id, firewall_id, event_id)

Get networking/firewall.event

Get networking/firewall.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get networking/firewall.event
        api_response = api_instance.networking_project_firewall_event_get(project_id, location_id, firewall_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_event_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
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

# **networking_project_firewall_event_list**
> [Event] networking_project_firewall_event_list(project_id, location_id, firewall_id)

List networking/firewall.event

List networking/firewall.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List networking/firewall.event
        api_response = api_instance.networking_project_firewall_event_list(project_id, location_id, firewall_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List networking/firewall.event
        api_response = api_instance.networking_project_firewall_event_list(project_id, location_id, firewall_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
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

# **networking_project_firewall_get**
> Firewall networking_project_firewall_get(project_id, location_id, firewall_id)

Get networking/firewall

Returns a single firewall

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
from h1.model.firewall import Firewall
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id

    # example passing only required values which don't have defaults set
    try:
        # Get networking/firewall
        api_response = api_instance.networking_project_firewall_get(project_id, location_id, firewall_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |

### Return type

[**Firewall**](Firewall.md)

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

# **networking_project_firewall_ingress_create**
> NetworkingRule networking_project_firewall_ingress_create(project_id, location_id, firewall_id, networking_rule)

Create networking/firewall.ingress

Create networking/firewall.ingress

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
from h1.model.networking_rule import NetworkingRule
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    networking_rule = NetworkingRule(
        id="id_example",
        name="name_example",
        action="allow",
        priority=3.14,
        filter=[
            "filter_example",
        ],
        external=["0.0.0.0/0"],
        internal=["*"],
    ) # NetworkingRule | 

    # example passing only required values which don't have defaults set
    try:
        # Create networking/firewall.ingress
        api_response = api_instance.networking_project_firewall_ingress_create(project_id, location_id, firewall_id, networking_rule)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_ingress_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
 **networking_rule** | [**NetworkingRule**](NetworkingRule.md)|  |

### Return type

[**NetworkingRule**](NetworkingRule.md)

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

# **networking_project_firewall_ingress_delete**
> networking_project_firewall_ingress_delete(project_id, location_id, firewall_id, ingress_id)

Delete networking/firewall.ingress

Delete networking/firewall.ingress

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    ingress_id = "ingressId_example" # str | ingressId

    # example passing only required values which don't have defaults set
    try:
        # Delete networking/firewall.ingress
        api_instance.networking_project_firewall_ingress_delete(project_id, location_id, firewall_id, ingress_id)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_ingress_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
 **ingress_id** | **str**| ingressId |

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

# **networking_project_firewall_ingress_get**
> NetworkingRule networking_project_firewall_ingress_get(project_id, location_id, firewall_id, ingress_id)

Get networking/firewall.ingress

Get networking/firewall.ingress

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
from h1.model.networking_rule import NetworkingRule
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    ingress_id = "ingressId_example" # str | ingressId

    # example passing only required values which don't have defaults set
    try:
        # Get networking/firewall.ingress
        api_response = api_instance.networking_project_firewall_ingress_get(project_id, location_id, firewall_id, ingress_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_ingress_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
 **ingress_id** | **str**| ingressId |

### Return type

[**NetworkingRule**](NetworkingRule.md)

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

# **networking_project_firewall_ingress_list**
> [NetworkingRule] networking_project_firewall_ingress_list(project_id, location_id, firewall_id)

List networking/firewall.ingress

List networking/firewall.ingress

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
from h1.model.networking_rule import NetworkingRule
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id

    # example passing only required values which don't have defaults set
    try:
        # List networking/firewall.ingress
        api_response = api_instance.networking_project_firewall_ingress_list(project_id, location_id, firewall_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_ingress_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |

### Return type

[**[NetworkingRule]**](NetworkingRule.md)

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

# **networking_project_firewall_ingress_put**
> [NetworkingRule] networking_project_firewall_ingress_put(project_id, location_id, firewall_id, networking_rule_array)

Replace networking/firewall.ingress

Replace networking/firewall.ingress

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
from h1.model.networking_rule_array import NetworkingRuleArray
from h1.model.networking_rule import NetworkingRule
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    networking_rule_array = NetworkingRuleArray([
        NetworkingRule(
            id="id_example",
            name="name_example",
            action="allow",
            priority=3.14,
            filter=[
                "filter_example",
            ],
            external=["0.0.0.0/0"],
            internal=["*"],
        ),
    ]) # NetworkingRuleArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace networking/firewall.ingress
        api_response = api_instance.networking_project_firewall_ingress_put(project_id, location_id, firewall_id, networking_rule_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_ingress_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
 **networking_rule_array** | [**NetworkingRuleArray**](NetworkingRuleArray.md)|  |

### Return type

[**[NetworkingRule]**](NetworkingRule.md)

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

# **networking_project_firewall_list**
> [Firewall] networking_project_firewall_list(project_id, location_id)

List networking/firewall

List firewall

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
from h1.model.firewall import Firewall
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List networking/firewall
        api_response = api_instance.networking_project_firewall_list(project_id, location_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List networking/firewall
        api_response = api_instance.networking_project_firewall_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_list: %s\n" % e)
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

[**[Firewall]**](Firewall.md)

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

# **networking_project_firewall_service_get**
> ResourceService networking_project_firewall_service_get(project_id, location_id, firewall_id, service_id)

Get networking/firewall.service

Get networking/firewall.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get networking/firewall.service
        api_response = api_instance.networking_project_firewall_service_get(project_id, location_id, firewall_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
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

# **networking_project_firewall_service_list**
> [ResourceService] networking_project_firewall_service_list(project_id, location_id, firewall_id)

List networking/firewall.service

List networking/firewall.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id

    # example passing only required values which don't have defaults set
    try:
        # List networking/firewall.service
        api_response = api_instance.networking_project_firewall_service_list(project_id, location_id, firewall_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |

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

# **networking_project_firewall_tag_create**
> Tag networking_project_firewall_tag_create(project_id, location_id, firewall_id, tag)

Create networking/firewall.tag

Create networking/firewall.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create networking/firewall.tag
        api_response = api_instance.networking_project_firewall_tag_create(project_id, location_id, firewall_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_tag_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
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

# **networking_project_firewall_tag_delete**
> networking_project_firewall_tag_delete(project_id, location_id, firewall_id, tag_id)

Delete networking/firewall.tag

Delete networking/firewall.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete networking/firewall.tag
        api_instance.networking_project_firewall_tag_delete(project_id, location_id, firewall_id, tag_id)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_tag_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
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

# **networking_project_firewall_tag_get**
> Tag networking_project_firewall_tag_get(project_id, location_id, firewall_id, tag_id)

Get networking/firewall.tag

Get networking/firewall.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get networking/firewall.tag
        api_response = api_instance.networking_project_firewall_tag_get(project_id, location_id, firewall_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_tag_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
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

# **networking_project_firewall_tag_list**
> [Tag] networking_project_firewall_tag_list(project_id, location_id, firewall_id)

List networking/firewall.tag

List networking/firewall.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id

    # example passing only required values which don't have defaults set
    try:
        # List networking/firewall.tag
        api_response = api_instance.networking_project_firewall_tag_list(project_id, location_id, firewall_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_tag_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |

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

# **networking_project_firewall_tag_put**
> [Tag] networking_project_firewall_tag_put(project_id, location_id, firewall_id, tag_array)

Replace networking/firewall.tag

Replace networking/firewall.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace networking/firewall.tag
        api_response = api_instance.networking_project_firewall_tag_put(project_id, location_id, firewall_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_tag_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
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

# **networking_project_firewall_transfer**
> Firewall networking_project_firewall_transfer(project_id, location_id, firewall_id, networking_project_firewall_transfer)

Transfer networking/firewall

action transfer

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
from h1.model.firewall import Firewall
from h1.model.networking_project_firewall_transfer import NetworkingProjectFirewallTransfer
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    networking_project_firewall_transfer = NetworkingProjectFirewallTransfer(
        project="project_example",
    ) # NetworkingProjectFirewallTransfer | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Transfer networking/firewall
        api_response = api_instance.networking_project_firewall_transfer(project_id, location_id, firewall_id, networking_project_firewall_transfer)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_transfer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Transfer networking/firewall
        api_response = api_instance.networking_project_firewall_transfer(project_id, location_id, firewall_id, networking_project_firewall_transfer, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_transfer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
 **networking_project_firewall_transfer** | [**NetworkingProjectFirewallTransfer**](NetworkingProjectFirewallTransfer.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Firewall**](Firewall.md)

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

# **networking_project_firewall_update**
> Firewall networking_project_firewall_update(project_id, location_id, firewall_id, networking_project_firewall_update)

Update networking/firewall

Returns modified firewall

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import networking_project_firewall_api
from h1.model.firewall import Firewall
from h1.model.networking_project_firewall_update import NetworkingProjectFirewallUpdate
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
    api_instance = networking_project_firewall_api.NetworkingProjectFirewallApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    firewall_id = "firewallId_example" # str | Firewall Id
    networking_project_firewall_update = NetworkingProjectFirewallUpdate(
        name="name_example",
    ) # NetworkingProjectFirewallUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update networking/firewall
        api_response = api_instance.networking_project_firewall_update(project_id, location_id, firewall_id, networking_project_firewall_update)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling NetworkingProjectFirewallApi->networking_project_firewall_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **firewall_id** | **str**| Firewall Id |
 **networking_project_firewall_update** | [**NetworkingProjectFirewallUpdate**](NetworkingProjectFirewallUpdate.md)|  |

### Return type

[**Firewall**](Firewall.md)

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

