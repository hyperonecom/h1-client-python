# h1.ComputeProjectVmApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compute_project_vm_connect_get**](ComputeProjectVmApi.md#compute_project_vm_connect_get) | **GET** /compute/{locationId}/project/{projectId}/vm/{vmId}/connect/{connectId} | Get compute/vm.connect
[**compute_project_vm_connect_list**](ComputeProjectVmApi.md#compute_project_vm_connect_list) | **GET** /compute/{locationId}/project/{projectId}/vm/{vmId}/connect | List compute/vm.connect
[**compute_project_vm_connect_open**](ComputeProjectVmApi.md#compute_project_vm_connect_open) | **POST** /compute/{locationId}/project/{projectId}/vm/{vmId}/connect/{connectId}/actions/open | Open compute/vm.connect
[**compute_project_vm_create**](ComputeProjectVmApi.md#compute_project_vm_create) | **POST** /compute/{locationId}/project/{projectId}/vm | Create compute/vm
[**compute_project_vm_delete**](ComputeProjectVmApi.md#compute_project_vm_delete) | **DELETE** /compute/{locationId}/project/{projectId}/vm/{vmId} | Delete compute/vm
[**compute_project_vm_disk_create**](ComputeProjectVmApi.md#compute_project_vm_disk_create) | **POST** /compute/{locationId}/project/{projectId}/vm/{vmId}/disk | Create compute/vm.disk
[**compute_project_vm_disk_list**](ComputeProjectVmApi.md#compute_project_vm_disk_list) | **GET** /compute/{locationId}/project/{projectId}/vm/{vmId}/disk | List compute/vm.disk
[**compute_project_vm_event_get**](ComputeProjectVmApi.md#compute_project_vm_event_get) | **GET** /compute/{locationId}/project/{projectId}/vm/{vmId}/event/{eventId} | Get compute/vm.event
[**compute_project_vm_event_list**](ComputeProjectVmApi.md#compute_project_vm_event_list) | **GET** /compute/{locationId}/project/{projectId}/vm/{vmId}/event | List compute/vm.event
[**compute_project_vm_flavour**](ComputeProjectVmApi.md#compute_project_vm_flavour) | **POST** /compute/{locationId}/project/{projectId}/vm/{vmId}/actions/flavour | Flavour compute/vm
[**compute_project_vm_get**](ComputeProjectVmApi.md#compute_project_vm_get) | **GET** /compute/{locationId}/project/{projectId}/vm/{vmId} | Get compute/vm
[**compute_project_vm_iso_create**](ComputeProjectVmApi.md#compute_project_vm_iso_create) | **POST** /compute/{locationId}/project/{projectId}/vm/{vmId}/iso | Create compute/vm.iso
[**compute_project_vm_iso_list**](ComputeProjectVmApi.md#compute_project_vm_iso_list) | **GET** /compute/{locationId}/project/{projectId}/vm/{vmId}/iso | List compute/vm.iso
[**compute_project_vm_list**](ComputeProjectVmApi.md#compute_project_vm_list) | **GET** /compute/{locationId}/project/{projectId}/vm | List compute/vm
[**compute_project_vm_metric_get**](ComputeProjectVmApi.md#compute_project_vm_metric_get) | **GET** /compute/{locationId}/project/{projectId}/vm/{vmId}/metric/{metricId} | Get compute/vm.metric
[**compute_project_vm_metric_list**](ComputeProjectVmApi.md#compute_project_vm_metric_list) | **GET** /compute/{locationId}/project/{projectId}/vm/{vmId}/metric | List compute/vm.metric
[**compute_project_vm_metric_point_list**](ComputeProjectVmApi.md#compute_project_vm_metric_point_list) | **GET** /compute/{locationId}/project/{projectId}/vm/{vmId}/metric/{metricId}/point | List compute/vm.point
[**compute_project_vm_password_reset**](ComputeProjectVmApi.md#compute_project_vm_password_reset) | **POST** /compute/{locationId}/project/{projectId}/vm/{vmId}/actions/password_reset | Password reset compute/vm
[**compute_project_vm_restart**](ComputeProjectVmApi.md#compute_project_vm_restart) | **POST** /compute/{locationId}/project/{projectId}/vm/{vmId}/actions/restart | Restart compute/vm
[**compute_project_vm_serialport**](ComputeProjectVmApi.md#compute_project_vm_serialport) | **POST** /compute/{locationId}/project/{projectId}/vm/{vmId}/actions/serialport | Serialport compute/vm
[**compute_project_vm_service_get**](ComputeProjectVmApi.md#compute_project_vm_service_get) | **GET** /compute/{locationId}/project/{projectId}/vm/{vmId}/service/{serviceId} | Get compute/vm.service
[**compute_project_vm_service_list**](ComputeProjectVmApi.md#compute_project_vm_service_list) | **GET** /compute/{locationId}/project/{projectId}/vm/{vmId}/service | List compute/vm.service
[**compute_project_vm_start**](ComputeProjectVmApi.md#compute_project_vm_start) | **POST** /compute/{locationId}/project/{projectId}/vm/{vmId}/actions/start | Start compute/vm
[**compute_project_vm_stop**](ComputeProjectVmApi.md#compute_project_vm_stop) | **POST** /compute/{locationId}/project/{projectId}/vm/{vmId}/actions/stop | Stop compute/vm
[**compute_project_vm_tag_create**](ComputeProjectVmApi.md#compute_project_vm_tag_create) | **POST** /compute/{locationId}/project/{projectId}/vm/{vmId}/tag | Create compute/vm.tag
[**compute_project_vm_tag_delete**](ComputeProjectVmApi.md#compute_project_vm_tag_delete) | **DELETE** /compute/{locationId}/project/{projectId}/vm/{vmId}/tag/{tagId} | Delete compute/vm.tag
[**compute_project_vm_tag_get**](ComputeProjectVmApi.md#compute_project_vm_tag_get) | **GET** /compute/{locationId}/project/{projectId}/vm/{vmId}/tag/{tagId} | Get compute/vm.tag
[**compute_project_vm_tag_list**](ComputeProjectVmApi.md#compute_project_vm_tag_list) | **GET** /compute/{locationId}/project/{projectId}/vm/{vmId}/tag | List compute/vm.tag
[**compute_project_vm_tag_put**](ComputeProjectVmApi.md#compute_project_vm_tag_put) | **PUT** /compute/{locationId}/project/{projectId}/vm/{vmId}/tag | Replace compute/vm.tag
[**compute_project_vm_turnoff**](ComputeProjectVmApi.md#compute_project_vm_turnoff) | **POST** /compute/{locationId}/project/{projectId}/vm/{vmId}/actions/turnoff | Turnoff compute/vm
[**compute_project_vm_update**](ComputeProjectVmApi.md#compute_project_vm_update) | **PATCH** /compute/{locationId}/project/{projectId}/vm/{vmId} | Update compute/vm


# **compute_project_vm_connect_get**
> Connect compute_project_vm_connect_get(project_id, location_id, vm_id, connect_id)

Get compute/vm.connect

Get compute/vm.connect

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.connect import Connect
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    connect_id = "connectId_example" # str | connectId

    # example passing only required values which don't have defaults set
    try:
        # Get compute/vm.connect
        api_response = api_instance.compute_project_vm_connect_get(project_id, location_id, vm_id, connect_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_connect_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
 **connect_id** | **str**| connectId |

### Return type

[**Connect**](Connect.md)

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

# **compute_project_vm_connect_list**
> [Connect] compute_project_vm_connect_list(project_id, location_id, vm_id)

List compute/vm.connect

List compute/vm.connect

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.connect import Connect
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id

    # example passing only required values which don't have defaults set
    try:
        # List compute/vm.connect
        api_response = api_instance.compute_project_vm_connect_list(project_id, location_id, vm_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_connect_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |

### Return type

[**[Connect]**](Connect.md)

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

# **compute_project_vm_connect_open**
> compute_project_vm_connect_open(project_id, location_id, vm_id, connect_id, compute_project_vm_connect_open)

Open compute/vm.connect

action open

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.compute_project_vm_connect_open import ComputeProjectVmConnectOpen
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    connect_id = "connectId_example" # str | connectId
    compute_project_vm_connect_open = ComputeProjectVmConnectOpen(
        protocol="http",
    ) # ComputeProjectVmConnectOpen | 

    # example passing only required values which don't have defaults set
    try:
        # Open compute/vm.connect
        api_instance.compute_project_vm_connect_open(project_id, location_id, vm_id, connect_id, compute_project_vm_connect_open)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_connect_open: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
 **connect_id** | **str**| connectId |
 **compute_project_vm_connect_open** | [**ComputeProjectVmConnectOpen**](ComputeProjectVmConnectOpen.md)|  |

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Console request accepted |  * location - Absolute URL <br>  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_project_vm_create**
> Vm compute_project_vm_create(project_id, location_id, compute_project_vm_create)

Create compute/vm

Create vm

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.vm import Vm
from h1.model.compute_project_vm_create import ComputeProjectVmCreate
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    compute_project_vm_create = ComputeProjectVmCreate(
        name="name_example",
        service="service_example",
        image="image_example",
        iso="iso_example",
        username="username_example",
        user_metadata="user_metadata_example",
        start=True,
        credential=[
            ComputeProjectVmCreateCredential(
                type="ssh",
                value="value_example",
            ),
        ],
        disk=[
            ComputeProjectVmCreateDisk(
                name="name_example",
                service="service_example",
                size=3.14,
            ),
        ],
        netadp=[
            ComputeProjectVmCreateNetadp(
                network="network_example",
                firewall="firewall_example",
                ip=[
                    "ip_example",
                ],
            ),
        ],
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # ComputeProjectVmCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create compute/vm
        api_response = api_instance.compute_project_vm_create(project_id, location_id, compute_project_vm_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create compute/vm
        api_response = api_instance.compute_project_vm_create(project_id, location_id, compute_project_vm_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **compute_project_vm_create** | [**ComputeProjectVmCreate**](ComputeProjectVmCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Vm**](Vm.md)

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

# **compute_project_vm_delete**
> compute_project_vm_delete(project_id, location_id, vm_id)

Delete compute/vm

Delete vm

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id

    # example passing only required values which don't have defaults set
    try:
        # Delete compute/vm
        api_instance.compute_project_vm_delete(project_id, location_id, vm_id)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |

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

# **compute_project_vm_disk_create**
> Disk compute_project_vm_disk_create(project_id, location_id, vm_id, compute_project_vm_disk_create)

Create compute/vm.disk

Create compute/vm.disk

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.compute_project_vm_disk_create import ComputeProjectVmDiskCreate
from h1.model.disk import Disk
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    compute_project_vm_disk_create = ComputeProjectVmDiskCreate(
        disk="disk_example",
    ) # ComputeProjectVmDiskCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create compute/vm.disk
        api_response = api_instance.compute_project_vm_disk_create(project_id, location_id, vm_id, compute_project_vm_disk_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_disk_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
 **compute_project_vm_disk_create** | [**ComputeProjectVmDiskCreate**](ComputeProjectVmDiskCreate.md)|  |

### Return type

[**Disk**](Disk.md)

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

# **compute_project_vm_disk_list**
> [Disk] compute_project_vm_disk_list(project_id, location_id, vm_id)

List compute/vm.disk

List compute/vm.disk

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.disk import Disk
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id

    # example passing only required values which don't have defaults set
    try:
        # List compute/vm.disk
        api_response = api_instance.compute_project_vm_disk_list(project_id, location_id, vm_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_disk_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |

### Return type

[**[Disk]**](Disk.md)

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

# **compute_project_vm_event_get**
> Event compute_project_vm_event_get(project_id, location_id, vm_id, event_id)

Get compute/vm.event

Get compute/vm.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get compute/vm.event
        api_response = api_instance.compute_project_vm_event_get(project_id, location_id, vm_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_event_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
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

# **compute_project_vm_event_list**
> [Event] compute_project_vm_event_list(project_id, location_id, vm_id)

List compute/vm.event

List compute/vm.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List compute/vm.event
        api_response = api_instance.compute_project_vm_event_list(project_id, location_id, vm_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List compute/vm.event
        api_response = api_instance.compute_project_vm_event_list(project_id, location_id, vm_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_event_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
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

# **compute_project_vm_flavour**
> Vm compute_project_vm_flavour(project_id, location_id, vm_id, compute_project_vm_flavour)

Flavour compute/vm

action flavour

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.vm import Vm
from h1.model.compute_project_vm_flavour import ComputeProjectVmFlavour
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    compute_project_vm_flavour = ComputeProjectVmFlavour(
        service="service_example",
    ) # ComputeProjectVmFlavour | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Flavour compute/vm
        api_response = api_instance.compute_project_vm_flavour(project_id, location_id, vm_id, compute_project_vm_flavour)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_flavour: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Flavour compute/vm
        api_response = api_instance.compute_project_vm_flavour(project_id, location_id, vm_id, compute_project_vm_flavour, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_flavour: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
 **compute_project_vm_flavour** | [**ComputeProjectVmFlavour**](ComputeProjectVmFlavour.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Vm**](Vm.md)

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

# **compute_project_vm_get**
> Vm compute_project_vm_get(project_id, location_id, vm_id)

Get compute/vm

Returns a single vm

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.vm import Vm
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id

    # example passing only required values which don't have defaults set
    try:
        # Get compute/vm
        api_response = api_instance.compute_project_vm_get(project_id, location_id, vm_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |

### Return type

[**Vm**](Vm.md)

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

# **compute_project_vm_iso_create**
> Iso compute_project_vm_iso_create(project_id, location_id, vm_id, compute_project_vm_iso_create)

Create compute/vm.iso

Create compute/vm.iso

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.compute_project_vm_iso_create import ComputeProjectVmIsoCreate
from h1.model.iso import Iso
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    compute_project_vm_iso_create = ComputeProjectVmIsoCreate(
        iso="iso_example",
    ) # ComputeProjectVmIsoCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create compute/vm.iso
        api_response = api_instance.compute_project_vm_iso_create(project_id, location_id, vm_id, compute_project_vm_iso_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_iso_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
 **compute_project_vm_iso_create** | [**ComputeProjectVmIsoCreate**](ComputeProjectVmIsoCreate.md)|  |

### Return type

[**Iso**](Iso.md)

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

# **compute_project_vm_iso_list**
> [Iso] compute_project_vm_iso_list(project_id, location_id, vm_id)

List compute/vm.iso

List compute/vm.iso

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.iso import Iso
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id

    # example passing only required values which don't have defaults set
    try:
        # List compute/vm.iso
        api_response = api_instance.compute_project_vm_iso_list(project_id, location_id, vm_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_iso_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |

### Return type

[**[Iso]**](Iso.md)

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

# **compute_project_vm_list**
> [Vm] compute_project_vm_list(project_id, location_id)

List compute/vm

List vm

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.vm import Vm
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    name = "name_example" # str | Filter by name (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List compute/vm
        api_response = api_instance.compute_project_vm_list(project_id, location_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List compute/vm
        api_response = api_instance.compute_project_vm_list(project_id, location_id, name=name, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_list: %s\n" % e)
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

[**[Vm]**](Vm.md)

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

# **compute_project_vm_metric_get**
> Metric compute_project_vm_metric_get(project_id, location_id, vm_id, metric_id)

Get compute/vm.metric

Get compute/vm.metric

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.metric import Metric
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    metric_id = "metricId_example" # str | metricId

    # example passing only required values which don't have defaults set
    try:
        # Get compute/vm.metric
        api_response = api_instance.compute_project_vm_metric_get(project_id, location_id, vm_id, metric_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_metric_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
 **metric_id** | **str**| metricId |

### Return type

[**Metric**](Metric.md)

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

# **compute_project_vm_metric_list**
> [Metric] compute_project_vm_metric_list(project_id, location_id, vm_id)

List compute/vm.metric

List compute/vm.metric

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.metric import Metric
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id

    # example passing only required values which don't have defaults set
    try:
        # List compute/vm.metric
        api_response = api_instance.compute_project_vm_metric_list(project_id, location_id, vm_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_metric_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |

### Return type

[**[Metric]**](Metric.md)

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

# **compute_project_vm_metric_point_list**
> [Point] compute_project_vm_metric_point_list(project_id, location_id, vm_id, metric_id)

List compute/vm.point

List compute/vm.point

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.point import Point
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    metric_id = "metricId_example" # str | metricId
    interval = "interval_example" # str | interval (optional)
    timespan = "timespan_example" # str | timespan (optional)

    # example passing only required values which don't have defaults set
    try:
        # List compute/vm.point
        api_response = api_instance.compute_project_vm_metric_point_list(project_id, location_id, vm_id, metric_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_metric_point_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List compute/vm.point
        api_response = api_instance.compute_project_vm_metric_point_list(project_id, location_id, vm_id, metric_id, interval=interval, timespan=timespan)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_metric_point_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
 **metric_id** | **str**| metricId |
 **interval** | **str**| interval | [optional]
 **timespan** | **str**| timespan | [optional]

### Return type

[**[Point]**](Point.md)

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

# **compute_project_vm_password_reset**
> Vm compute_project_vm_password_reset(project_id, location_id, vm_id, compute_project_vm_password_reset)

Password reset compute/vm

action password_reset

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.vm import Vm
from h1.model.inline_response400 import InlineResponse400
from h1.model.compute_project_vm_password_reset import ComputeProjectVmPasswordReset
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    compute_project_vm_password_reset = ComputeProjectVmPasswordReset(
        user_name="user_name_example",
        modulus="modulus_example",
        exponent="exponent_example",
    ) # ComputeProjectVmPasswordReset | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Password reset compute/vm
        api_response = api_instance.compute_project_vm_password_reset(project_id, location_id, vm_id, compute_project_vm_password_reset)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_password_reset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Password reset compute/vm
        api_response = api_instance.compute_project_vm_password_reset(project_id, location_id, vm_id, compute_project_vm_password_reset, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_password_reset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
 **compute_project_vm_password_reset** | [**ComputeProjectVmPasswordReset**](ComputeProjectVmPasswordReset.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Vm**](Vm.md)

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

# **compute_project_vm_restart**
> Vm compute_project_vm_restart(project_id, location_id, vm_id)

Restart compute/vm

action restart

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.vm import Vm
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Restart compute/vm
        api_response = api_instance.compute_project_vm_restart(project_id, location_id, vm_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_restart: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Restart compute/vm
        api_response = api_instance.compute_project_vm_restart(project_id, location_id, vm_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_restart: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Vm**](Vm.md)

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

# **compute_project_vm_serialport**
> file_type compute_project_vm_serialport(project_id, location_id, vm_id, compute_project_vm_serialport)

Serialport compute/vm

action serialport

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.compute_project_vm_serialport import ComputeProjectVmSerialport
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    compute_project_vm_serialport = ComputeProjectVmSerialport(
        number="1",
    ) # ComputeProjectVmSerialport | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Serialport compute/vm
        api_response = api_instance.compute_project_vm_serialport(project_id, location_id, vm_id, compute_project_vm_serialport)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_serialport: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Serialport compute/vm
        api_response = api_instance.compute_project_vm_serialport(project_id, location_id, vm_id, compute_project_vm_serialport, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_serialport: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
 **compute_project_vm_serialport** | [**ComputeProjectVmSerialport**](ComputeProjectVmSerialport.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

**file_type**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | serial port buffer |  -  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_project_vm_service_get**
> ResourceService compute_project_vm_service_get(project_id, location_id, vm_id, service_id)

Get compute/vm.service

Get compute/vm.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get compute/vm.service
        api_response = api_instance.compute_project_vm_service_get(project_id, location_id, vm_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_service_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
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

# **compute_project_vm_service_list**
> [ResourceService] compute_project_vm_service_list(project_id, location_id, vm_id)

List compute/vm.service

List compute/vm.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id

    # example passing only required values which don't have defaults set
    try:
        # List compute/vm.service
        api_response = api_instance.compute_project_vm_service_list(project_id, location_id, vm_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_service_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |

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

# **compute_project_vm_start**
> Vm compute_project_vm_start(project_id, location_id, vm_id)

Start compute/vm

action start

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.vm import Vm
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start compute/vm
        api_response = api_instance.compute_project_vm_start(project_id, location_id, vm_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_start: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start compute/vm
        api_response = api_instance.compute_project_vm_start(project_id, location_id, vm_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_start: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Vm**](Vm.md)

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

# **compute_project_vm_stop**
> Vm compute_project_vm_stop(project_id, location_id, vm_id)

Stop compute/vm

action stop

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.vm import Vm
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Stop compute/vm
        api_response = api_instance.compute_project_vm_stop(project_id, location_id, vm_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_stop: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Stop compute/vm
        api_response = api_instance.compute_project_vm_stop(project_id, location_id, vm_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_stop: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Vm**](Vm.md)

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

# **compute_project_vm_tag_create**
> Tag compute_project_vm_tag_create(project_id, location_id, vm_id, tag)

Create compute/vm.tag

Create compute/vm.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create compute/vm.tag
        api_response = api_instance.compute_project_vm_tag_create(project_id, location_id, vm_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_tag_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
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

# **compute_project_vm_tag_delete**
> compute_project_vm_tag_delete(project_id, location_id, vm_id, tag_id)

Delete compute/vm.tag

Delete compute/vm.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete compute/vm.tag
        api_instance.compute_project_vm_tag_delete(project_id, location_id, vm_id, tag_id)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_tag_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
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

# **compute_project_vm_tag_get**
> Tag compute_project_vm_tag_get(project_id, location_id, vm_id, tag_id)

Get compute/vm.tag

Get compute/vm.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get compute/vm.tag
        api_response = api_instance.compute_project_vm_tag_get(project_id, location_id, vm_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_tag_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
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

# **compute_project_vm_tag_list**
> [Tag] compute_project_vm_tag_list(project_id, location_id, vm_id)

List compute/vm.tag

List compute/vm.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id

    # example passing only required values which don't have defaults set
    try:
        # List compute/vm.tag
        api_response = api_instance.compute_project_vm_tag_list(project_id, location_id, vm_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_tag_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |

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

# **compute_project_vm_tag_put**
> [Tag] compute_project_vm_tag_put(project_id, location_id, vm_id, tag_array)

Replace compute/vm.tag

Replace compute/vm.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace compute/vm.tag
        api_response = api_instance.compute_project_vm_tag_put(project_id, location_id, vm_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_tag_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
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

# **compute_project_vm_turnoff**
> Vm compute_project_vm_turnoff(project_id, location_id, vm_id)

Turnoff compute/vm

action turnoff

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.vm import Vm
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Turnoff compute/vm
        api_response = api_instance.compute_project_vm_turnoff(project_id, location_id, vm_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_turnoff: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Turnoff compute/vm
        api_response = api_instance.compute_project_vm_turnoff(project_id, location_id, vm_id, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_turnoff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Vm**](Vm.md)

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

# **compute_project_vm_update**
> Vm compute_project_vm_update(project_id, location_id, vm_id, compute_project_vm_update)

Update compute/vm

Returns modified vm

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import compute_project_vm_api
from h1.model.vm import Vm
from h1.model.compute_project_vm_update import ComputeProjectVmUpdate
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
    api_instance = compute_project_vm_api.ComputeProjectVmApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    vm_id = "vmId_example" # str | Vm Id
    compute_project_vm_update = ComputeProjectVmUpdate(
        user_metadata="user_metadata_example",
        name="name_example",
    ) # ComputeProjectVmUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update compute/vm
        api_response = api_instance.compute_project_vm_update(project_id, location_id, vm_id, compute_project_vm_update)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling ComputeProjectVmApi->compute_project_vm_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **vm_id** | **str**| Vm Id |
 **compute_project_vm_update** | [**ComputeProjectVmUpdate**](ComputeProjectVmUpdate.md)|  |

### Return type

[**Vm**](Vm.md)

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

