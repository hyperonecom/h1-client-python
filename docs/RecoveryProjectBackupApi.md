# h1.RecoveryProjectBackupApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recovery_project_backup_create**](RecoveryProjectBackupApi.md#recovery_project_backup_create) | **POST** /recovery/{locationId}/project/{projectId}/backup | Create recovery/backup
[**recovery_project_backup_delete**](RecoveryProjectBackupApi.md#recovery_project_backup_delete) | **DELETE** /recovery/{locationId}/project/{projectId}/backup/{backupId} | Delete recovery/backup
[**recovery_project_backup_event_get**](RecoveryProjectBackupApi.md#recovery_project_backup_event_get) | **GET** /recovery/{locationId}/project/{projectId}/backup/{backupId}/event/{eventId} | Get recovery/backup.event
[**recovery_project_backup_event_list**](RecoveryProjectBackupApi.md#recovery_project_backup_event_list) | **GET** /recovery/{locationId}/project/{projectId}/backup/{backupId}/event | List recovery/backup.event
[**recovery_project_backup_export**](RecoveryProjectBackupApi.md#recovery_project_backup_export) | **POST** /recovery/{locationId}/project/{projectId}/backup/{backupId}/actions/export | Export recovery/backup
[**recovery_project_backup_get**](RecoveryProjectBackupApi.md#recovery_project_backup_get) | **GET** /recovery/{locationId}/project/{projectId}/backup/{backupId} | Get recovery/backup
[**recovery_project_backup_list**](RecoveryProjectBackupApi.md#recovery_project_backup_list) | **GET** /recovery/{locationId}/project/{projectId}/backup | List recovery/backup
[**recovery_project_backup_metric_get**](RecoveryProjectBackupApi.md#recovery_project_backup_metric_get) | **GET** /recovery/{locationId}/project/{projectId}/backup/{backupId}/metric/{metricId} | Get recovery/backup.metric
[**recovery_project_backup_metric_list**](RecoveryProjectBackupApi.md#recovery_project_backup_metric_list) | **GET** /recovery/{locationId}/project/{projectId}/backup/{backupId}/metric | List recovery/backup.metric
[**recovery_project_backup_metric_point_list**](RecoveryProjectBackupApi.md#recovery_project_backup_metric_point_list) | **GET** /recovery/{locationId}/project/{projectId}/backup/{backupId}/metric/{metricId}/point | List recovery/backup.point
[**recovery_project_backup_service_get**](RecoveryProjectBackupApi.md#recovery_project_backup_service_get) | **GET** /recovery/{locationId}/project/{projectId}/backup/{backupId}/service/{serviceId} | Get recovery/backup.service
[**recovery_project_backup_service_list**](RecoveryProjectBackupApi.md#recovery_project_backup_service_list) | **GET** /recovery/{locationId}/project/{projectId}/backup/{backupId}/service | List recovery/backup.service
[**recovery_project_backup_tag_create**](RecoveryProjectBackupApi.md#recovery_project_backup_tag_create) | **POST** /recovery/{locationId}/project/{projectId}/backup/{backupId}/tag | Create recovery/backup.tag
[**recovery_project_backup_tag_delete**](RecoveryProjectBackupApi.md#recovery_project_backup_tag_delete) | **DELETE** /recovery/{locationId}/project/{projectId}/backup/{backupId}/tag/{tagId} | Delete recovery/backup.tag
[**recovery_project_backup_tag_get**](RecoveryProjectBackupApi.md#recovery_project_backup_tag_get) | **GET** /recovery/{locationId}/project/{projectId}/backup/{backupId}/tag/{tagId} | Get recovery/backup.tag
[**recovery_project_backup_tag_list**](RecoveryProjectBackupApi.md#recovery_project_backup_tag_list) | **GET** /recovery/{locationId}/project/{projectId}/backup/{backupId}/tag | List recovery/backup.tag
[**recovery_project_backup_tag_put**](RecoveryProjectBackupApi.md#recovery_project_backup_tag_put) | **PUT** /recovery/{locationId}/project/{projectId}/backup/{backupId}/tag | Replace recovery/backup.tag
[**recovery_project_backup_update**](RecoveryProjectBackupApi.md#recovery_project_backup_update) | **PATCH** /recovery/{locationId}/project/{projectId}/backup/{backupId} | Update recovery/backup


# **recovery_project_backup_create**
> Backup recovery_project_backup_create(project_id, location_id, recovery_project_backup_create)

Create recovery/backup

Create backup

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
from h1.model.backup import Backup
from h1.model.recovery_project_backup_create import RecoveryProjectBackupCreate
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    recovery_project_backup_create = RecoveryProjectBackupCreate(
        name="name_example",
        source="source_example",
        tag=TagArray([
            Tag(
                id="id_example",
                key="key_example",
                value="value_example",
            ),
        ]),
    ) # RecoveryProjectBackupCreate | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create recovery/backup
        api_response = api_instance.recovery_project_backup_create(project_id, location_id, recovery_project_backup_create)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create recovery/backup
        api_response = api_instance.recovery_project_backup_create(project_id, location_id, recovery_project_backup_create, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **recovery_project_backup_create** | [**RecoveryProjectBackupCreate**](RecoveryProjectBackupCreate.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Backup**](Backup.md)

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

# **recovery_project_backup_delete**
> recovery_project_backup_delete(project_id, location_id, backup_id)

Delete recovery/backup

Delete backup

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id

    # example passing only required values which don't have defaults set
    try:
        # Delete recovery/backup
        api_instance.recovery_project_backup_delete(project_id, location_id, backup_id)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |

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

# **recovery_project_backup_event_get**
> Event recovery_project_backup_event_get(project_id, location_id, backup_id, event_id)

Get recovery/backup.event

Get recovery/backup.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id
    event_id = "eventId_example" # str | eventId

    # example passing only required values which don't have defaults set
    try:
        # Get recovery/backup.event
        api_response = api_instance.recovery_project_backup_event_get(project_id, location_id, backup_id, event_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_event_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |
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

# **recovery_project_backup_event_list**
> [Event] recovery_project_backup_event_list(project_id, location_id, backup_id)

List recovery/backup.event

List recovery/backup.event

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id
    limit = 100 # float | $limit (optional) if omitted the server will use the default value of 100
    skip = 3.14 # float | $skip (optional)

    # example passing only required values which don't have defaults set
    try:
        # List recovery/backup.event
        api_response = api_instance.recovery_project_backup_event_list(project_id, location_id, backup_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_event_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List recovery/backup.event
        api_response = api_instance.recovery_project_backup_event_list(project_id, location_id, backup_id, limit=limit, skip=skip)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_event_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |
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

# **recovery_project_backup_export**
> Backup recovery_project_backup_export(project_id, location_id, backup_id, recovery_project_backup_export)

Export recovery/backup

action export

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
from h1.model.backup import Backup
from h1.model.recovery_project_backup_export import RecoveryProjectBackupExport
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id
    recovery_project_backup_export = RecoveryProjectBackupExport(
        bucket="bucket_example",
    ) # RecoveryProjectBackupExport | 
    x_idempotency_key = "x-idempotency-key_example" # str | Idempotency key (optional)
    x_dry_run = "x-dry-run_example" # str | Dry run (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export recovery/backup
        api_response = api_instance.recovery_project_backup_export(project_id, location_id, backup_id, recovery_project_backup_export)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_export: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export recovery/backup
        api_response = api_instance.recovery_project_backup_export(project_id, location_id, backup_id, recovery_project_backup_export, x_idempotency_key=x_idempotency_key, x_dry_run=x_dry_run)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |
 **recovery_project_backup_export** | [**RecoveryProjectBackupExport**](RecoveryProjectBackupExport.md)|  |
 **x_idempotency_key** | **str**| Idempotency key | [optional]
 **x_dry_run** | **str**| Dry run | [optional]

### Return type

[**Backup**](Backup.md)

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

# **recovery_project_backup_get**
> Backup recovery_project_backup_get(project_id, location_id, backup_id)

Get recovery/backup

Returns a single backup

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
from h1.model.backup import Backup
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id

    # example passing only required values which don't have defaults set
    try:
        # Get recovery/backup
        api_response = api_instance.recovery_project_backup_get(project_id, location_id, backup_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |

### Return type

[**Backup**](Backup.md)

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

# **recovery_project_backup_list**
> [Backup] recovery_project_backup_list(project_id, location_id)

List recovery/backup

List backup

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
from h1.model.backup import Backup
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    name = "name_example" # str | Filter by name (optional)
    source = "source_example" # str | Filter by source (optional)
    tag_value = "tag.value_example" # str | Filter by tag.value (optional)
    tag_key = "tag.key_example" # str | Filter by tag.key (optional)

    # example passing only required values which don't have defaults set
    try:
        # List recovery/backup
        api_response = api_instance.recovery_project_backup_list(project_id, location_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List recovery/backup
        api_response = api_instance.recovery_project_backup_list(project_id, location_id, name=name, source=source, tag_value=tag_value, tag_key=tag_key)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **name** | **str**| Filter by name | [optional]
 **source** | **str**| Filter by source | [optional]
 **tag_value** | **str**| Filter by tag.value | [optional]
 **tag_key** | **str**| Filter by tag.key | [optional]

### Return type

[**[Backup]**](Backup.md)

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

# **recovery_project_backup_metric_get**
> Metric recovery_project_backup_metric_get(project_id, location_id, backup_id, metric_id)

Get recovery/backup.metric

Get recovery/backup.metric

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id
    metric_id = "metricId_example" # str | metricId

    # example passing only required values which don't have defaults set
    try:
        # Get recovery/backup.metric
        api_response = api_instance.recovery_project_backup_metric_get(project_id, location_id, backup_id, metric_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_metric_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |
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

# **recovery_project_backup_metric_list**
> [Metric] recovery_project_backup_metric_list(project_id, location_id, backup_id)

List recovery/backup.metric

List recovery/backup.metric

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id

    # example passing only required values which don't have defaults set
    try:
        # List recovery/backup.metric
        api_response = api_instance.recovery_project_backup_metric_list(project_id, location_id, backup_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_metric_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |

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

# **recovery_project_backup_metric_point_list**
> [Point] recovery_project_backup_metric_point_list(project_id, location_id, backup_id, metric_id)

List recovery/backup.point

List recovery/backup.point

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id
    metric_id = "metricId_example" # str | metricId
    interval = "interval_example" # str | interval (optional)
    timespan = "timespan_example" # str | timespan (optional)

    # example passing only required values which don't have defaults set
    try:
        # List recovery/backup.point
        api_response = api_instance.recovery_project_backup_metric_point_list(project_id, location_id, backup_id, metric_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_metric_point_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List recovery/backup.point
        api_response = api_instance.recovery_project_backup_metric_point_list(project_id, location_id, backup_id, metric_id, interval=interval, timespan=timespan)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_metric_point_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |
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

# **recovery_project_backup_service_get**
> ResourceService recovery_project_backup_service_get(project_id, location_id, backup_id, service_id)

Get recovery/backup.service

Get recovery/backup.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id
    service_id = "serviceId_example" # str | serviceId

    # example passing only required values which don't have defaults set
    try:
        # Get recovery/backup.service
        api_response = api_instance.recovery_project_backup_service_get(project_id, location_id, backup_id, service_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_service_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |
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

# **recovery_project_backup_service_list**
> [ResourceService] recovery_project_backup_service_list(project_id, location_id, backup_id)

List recovery/backup.service

List recovery/backup.service

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id

    # example passing only required values which don't have defaults set
    try:
        # List recovery/backup.service
        api_response = api_instance.recovery_project_backup_service_list(project_id, location_id, backup_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_service_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |

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

# **recovery_project_backup_tag_create**
> Tag recovery_project_backup_tag_create(project_id, location_id, backup_id, tag)

Create recovery/backup.tag

Create recovery/backup.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id
    tag = Tag(
        id="id_example",
        key="key_example",
        value="value_example",
    ) # Tag | 

    # example passing only required values which don't have defaults set
    try:
        # Create recovery/backup.tag
        api_response = api_instance.recovery_project_backup_tag_create(project_id, location_id, backup_id, tag)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_tag_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |
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

# **recovery_project_backup_tag_delete**
> recovery_project_backup_tag_delete(project_id, location_id, backup_id, tag_id)

Delete recovery/backup.tag

Delete recovery/backup.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Delete recovery/backup.tag
        api_instance.recovery_project_backup_tag_delete(project_id, location_id, backup_id, tag_id)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_tag_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |
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

# **recovery_project_backup_tag_get**
> Tag recovery_project_backup_tag_get(project_id, location_id, backup_id, tag_id)

Get recovery/backup.tag

Get recovery/backup.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id
    tag_id = "tagId_example" # str | tagId

    # example passing only required values which don't have defaults set
    try:
        # Get recovery/backup.tag
        api_response = api_instance.recovery_project_backup_tag_get(project_id, location_id, backup_id, tag_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_tag_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |
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

# **recovery_project_backup_tag_list**
> [Tag] recovery_project_backup_tag_list(project_id, location_id, backup_id)

List recovery/backup.tag

List recovery/backup.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id

    # example passing only required values which don't have defaults set
    try:
        # List recovery/backup.tag
        api_response = api_instance.recovery_project_backup_tag_list(project_id, location_id, backup_id)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_tag_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |

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

# **recovery_project_backup_tag_put**
> [Tag] recovery_project_backup_tag_put(project_id, location_id, backup_id, tag_array)

Replace recovery/backup.tag

Replace recovery/backup.tag

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id
    tag_array = TagArray([
        Tag(
            id="id_example",
            key="key_example",
            value="value_example",
        ),
    ]) # TagArray | 

    # example passing only required values which don't have defaults set
    try:
        # Replace recovery/backup.tag
        api_response = api_instance.recovery_project_backup_tag_put(project_id, location_id, backup_id, tag_array)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_tag_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |
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

# **recovery_project_backup_update**
> Backup recovery_project_backup_update(project_id, location_id, backup_id, recovery_project_backup_update)

Update recovery/backup

Returns modified backup

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
import time
import h1
from h1.api import recovery_project_backup_api
from h1.model.backup import Backup
from h1.model.recovery_project_backup_update import RecoveryProjectBackupUpdate
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
    api_instance = recovery_project_backup_api.RecoveryProjectBackupApi(api_client)
    project_id = "projectId_example" # str | Project Id
    location_id = "locationId_example" # str | Location Id
    backup_id = "backupId_example" # str | Backup Id
    recovery_project_backup_update = RecoveryProjectBackupUpdate(
        name="name_example",
    ) # RecoveryProjectBackupUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update recovery/backup
        api_response = api_instance.recovery_project_backup_update(project_id, location_id, backup_id, recovery_project_backup_update)
        pprint(api_response)
    except h1.ApiException as e:
        print("Exception when calling RecoveryProjectBackupApi->recovery_project_backup_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id |
 **location_id** | **str**| Location Id |
 **backup_id** | **str**| Backup Id |
 **recovery_project_backup_update** | [**RecoveryProjectBackupUpdate**](RecoveryProjectBackupUpdate.md)|  |

### Return type

[**Backup**](Backup.md)

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

