# h1.StorageProjectBucketApi

All URIs are relative to *https://api.hyperone.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storage_project_bucket_get**](StorageProjectBucketApi.md#storage_project_bucket_get) | **GET** /storage/{locationId}/project/{projectId}/bucket/{bucketId} | Get storage/bucket
[**storage_project_bucket_list**](StorageProjectBucketApi.md#storage_project_bucket_list) | **GET** /storage/{locationId}/project/{projectId}/bucket | List storage/bucket
[**storage_project_bucket_object_delete**](StorageProjectBucketApi.md#storage_project_bucket_object_delete) | **DELETE** /storage/{locationId}/project/{projectId}/bucket/{bucketId}/object/{objectId} | Delete storage/bucket.object
[**storage_project_bucket_object_download**](StorageProjectBucketApi.md#storage_project_bucket_object_download) | **POST** /storage/{locationId}/project/{projectId}/bucket/{bucketId}/object/{objectId}/actions/download | Download storage/bucket.object
[**storage_project_bucket_object_get**](StorageProjectBucketApi.md#storage_project_bucket_object_get) | **GET** /storage/{locationId}/project/{projectId}/bucket/{bucketId}/object/{objectId} | Get storage/bucket.object
[**storage_project_bucket_object_list**](StorageProjectBucketApi.md#storage_project_bucket_object_list) | **GET** /storage/{locationId}/project/{projectId}/bucket/{bucketId}/object | List storage/bucket.object
[**storage_project_bucket_upload**](StorageProjectBucketApi.md#storage_project_bucket_upload) | **POST** /storage/{locationId}/project/{projectId}/bucket/{bucketId}/actions/upload | Upload storage/bucket


# **storage_project_bucket_get**
> Bucket storage_project_bucket_get(project_id, location_id, bucket_id)

Get storage/bucket

Returns a single bucket

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.StorageProjectBucketApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
bucket_id = 'bucket_id_example' # str | Bucket Id

    try:
        # Get storage/bucket
        api_response = api_instance.storage_project_bucket_get(project_id, location_id, bucket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectBucketApi->storage_project_bucket_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **bucket_id** | **str**| Bucket Id | 

### Return type

[**Bucket**](Bucket.md)

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

# **storage_project_bucket_list**
> list[Bucket] storage_project_bucket_list(project_id, location_id)

List storage/bucket

List bucket

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.StorageProjectBucketApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id

    try:
        # List storage/bucket
        api_response = api_instance.storage_project_bucket_list(project_id, location_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectBucketApi->storage_project_bucket_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 

### Return type

[**list[Bucket]**](Bucket.md)

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

# **storage_project_bucket_object_delete**
> storage_project_bucket_object_delete(project_id, location_id, bucket_id, object_id)

Delete storage/bucket.object

Delete storage/bucket.object

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.StorageProjectBucketApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
bucket_id = 'bucket_id_example' # str | Bucket Id
object_id = 'object_id_example' # str | objectId

    try:
        # Delete storage/bucket.object
        api_instance.storage_project_bucket_object_delete(project_id, location_id, bucket_id, object_id)
    except ApiException as e:
        print("Exception when calling StorageProjectBucketApi->storage_project_bucket_object_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **bucket_id** | **str**| Bucket Id | 
 **object_id** | **str**| objectId | 

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

# **storage_project_bucket_object_download**
> storage_project_bucket_object_download(project_id, location_id, bucket_id, object_id)

Download storage/bucket.object

action download

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.StorageProjectBucketApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
bucket_id = 'bucket_id_example' # str | Bucket Id
object_id = 'object_id_example' # str | objectId

    try:
        # Download storage/bucket.object
        api_instance.storage_project_bucket_object_download(project_id, location_id, bucket_id, object_id)
    except ApiException as e:
        print("Exception when calling StorageProjectBucketApi->storage_project_bucket_object_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **bucket_id** | **str**| Bucket Id | 
 **object_id** | **str**| objectId | 

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
**201** | Download request accepted |  * location - Absolute URL <br>  |
**400** | Bad Request |  -  |
**401** | Access token is missing or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_project_bucket_object_get**
> StorageObject storage_project_bucket_object_get(project_id, location_id, bucket_id, object_id)

Get storage/bucket.object

Get storage/bucket.object

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.StorageProjectBucketApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
bucket_id = 'bucket_id_example' # str | Bucket Id
object_id = 'object_id_example' # str | objectId

    try:
        # Get storage/bucket.object
        api_response = api_instance.storage_project_bucket_object_get(project_id, location_id, bucket_id, object_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectBucketApi->storage_project_bucket_object_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **bucket_id** | **str**| Bucket Id | 
 **object_id** | **str**| objectId | 

### Return type

[**StorageObject**](StorageObject.md)

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

# **storage_project_bucket_object_list**
> list[StorageObject] storage_project_bucket_object_list(project_id, location_id, bucket_id)

List storage/bucket.object

List storage/bucket.object

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.StorageProjectBucketApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
bucket_id = 'bucket_id_example' # str | Bucket Id

    try:
        # List storage/bucket.object
        api_response = api_instance.storage_project_bucket_object_list(project_id, location_id, bucket_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectBucketApi->storage_project_bucket_object_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **bucket_id** | **str**| Bucket Id | 

### Return type

[**list[StorageObject]**](StorageObject.md)

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

# **storage_project_bucket_upload**
> Bucket storage_project_bucket_upload(project_id, location_id, bucket_id, storage_project_bucket_upload, x_idempotency_key=x_idempotency_key)

Upload storage/bucket

action upload

### Example

* Bearer (JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import h1
from h1.rest import ApiException
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
    api_instance = h1.StorageProjectBucketApi(api_client)
    project_id = 'project_id_example' # str | Project Id
location_id = 'location_id_example' # str | Location Id
bucket_id = 'bucket_id_example' # str | Bucket Id
storage_project_bucket_upload = h1.StorageProjectBucketUpload() # StorageProjectBucketUpload | 
x_idempotency_key = 'x_idempotency_key_example' # str | Idempotency key (optional)

    try:
        # Upload storage/bucket
        api_response = api_instance.storage_project_bucket_upload(project_id, location_id, bucket_id, storage_project_bucket_upload, x_idempotency_key=x_idempotency_key)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StorageProjectBucketApi->storage_project_bucket_upload: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project Id | 
 **location_id** | **str**| Location Id | 
 **bucket_id** | **str**| Bucket Id | 
 **storage_project_bucket_upload** | [**StorageProjectBucketUpload**](StorageProjectBucketUpload.md)|  | 
 **x_idempotency_key** | **str**| Idempotency key | [optional] 

### Return type

[**Bucket**](Bucket.md)

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

