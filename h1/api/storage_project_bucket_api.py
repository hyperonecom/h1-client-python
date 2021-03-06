"""
    HyperOne

    HyperOne API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from h1.api_client import ApiClient, Endpoint as _Endpoint
from h1.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from h1.model.bucket import Bucket
from h1.model.inline_response400 import InlineResponse400
from h1.model.storage_object import StorageObject
from h1.model.storage_project_bucket_upload import StorageProjectBucketUpload


class StorageProjectBucketApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __storage_project_bucket_get(
            self,
            project_id,
            location_id,
            bucket_id,
            **kwargs
        ):
            """Get storage/bucket  # noqa: E501

            Returns a single bucket  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.storage_project_bucket_get(project_id, location_id, bucket_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str): Project Id
                location_id (str): Location Id
                bucket_id (str): Bucket Id

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Bucket
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['project_id'] = \
                project_id
            kwargs['location_id'] = \
                location_id
            kwargs['bucket_id'] = \
                bucket_id
            return self.call_with_http_info(**kwargs)

        self.storage_project_bucket_get = _Endpoint(
            settings={
                'response_type': (Bucket,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/storage/{locationId}/project/{projectId}/bucket/{bucketId}',
                'operation_id': 'storage_project_bucket_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'location_id',
                    'bucket_id',
                ],
                'required': [
                    'project_id',
                    'location_id',
                    'bucket_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_id':
                        (str,),
                    'location_id':
                        (str,),
                    'bucket_id':
                        (str,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'location_id': 'locationId',
                    'bucket_id': 'bucketId',
                },
                'location_map': {
                    'project_id': 'path',
                    'location_id': 'path',
                    'bucket_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__storage_project_bucket_get
        )

        def __storage_project_bucket_list(
            self,
            project_id,
            location_id,
            **kwargs
        ):
            """List storage/bucket  # noqa: E501

            List bucket  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.storage_project_bucket_list(project_id, location_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str): Project Id
                location_id (str): Location Id

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [Bucket]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['project_id'] = \
                project_id
            kwargs['location_id'] = \
                location_id
            return self.call_with_http_info(**kwargs)

        self.storage_project_bucket_list = _Endpoint(
            settings={
                'response_type': ([Bucket],),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/storage/{locationId}/project/{projectId}/bucket',
                'operation_id': 'storage_project_bucket_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'location_id',
                ],
                'required': [
                    'project_id',
                    'location_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_id':
                        (str,),
                    'location_id':
                        (str,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'location_id': 'locationId',
                },
                'location_map': {
                    'project_id': 'path',
                    'location_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__storage_project_bucket_list
        )

        def __storage_project_bucket_object_delete(
            self,
            project_id,
            location_id,
            bucket_id,
            object_id,
            **kwargs
        ):
            """Delete storage/bucket.object  # noqa: E501

            Delete storage/bucket.object  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.storage_project_bucket_object_delete(project_id, location_id, bucket_id, object_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str): Project Id
                location_id (str): Location Id
                bucket_id (str): Bucket Id
                object_id (str): objectId

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['project_id'] = \
                project_id
            kwargs['location_id'] = \
                location_id
            kwargs['bucket_id'] = \
                bucket_id
            kwargs['object_id'] = \
                object_id
            return self.call_with_http_info(**kwargs)

        self.storage_project_bucket_object_delete = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/storage/{locationId}/project/{projectId}/bucket/{bucketId}/object/{objectId}',
                'operation_id': 'storage_project_bucket_object_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'location_id',
                    'bucket_id',
                    'object_id',
                ],
                'required': [
                    'project_id',
                    'location_id',
                    'bucket_id',
                    'object_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_id':
                        (str,),
                    'location_id':
                        (str,),
                    'bucket_id':
                        (str,),
                    'object_id':
                        (str,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'location_id': 'locationId',
                    'bucket_id': 'bucketId',
                    'object_id': 'objectId',
                },
                'location_map': {
                    'project_id': 'path',
                    'location_id': 'path',
                    'bucket_id': 'path',
                    'object_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__storage_project_bucket_object_delete
        )

        def __storage_project_bucket_object_download(
            self,
            project_id,
            location_id,
            bucket_id,
            object_id,
            **kwargs
        ):
            """Download storage/bucket.object  # noqa: E501

            action download  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.storage_project_bucket_object_download(project_id, location_id, bucket_id, object_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str): Project Id
                location_id (str): Location Id
                bucket_id (str): Bucket Id
                object_id (str): objectId

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['project_id'] = \
                project_id
            kwargs['location_id'] = \
                location_id
            kwargs['bucket_id'] = \
                bucket_id
            kwargs['object_id'] = \
                object_id
            return self.call_with_http_info(**kwargs)

        self.storage_project_bucket_object_download = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/storage/{locationId}/project/{projectId}/bucket/{bucketId}/object/{objectId}/actions/download',
                'operation_id': 'storage_project_bucket_object_download',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'location_id',
                    'bucket_id',
                    'object_id',
                ],
                'required': [
                    'project_id',
                    'location_id',
                    'bucket_id',
                    'object_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_id':
                        (str,),
                    'location_id':
                        (str,),
                    'bucket_id':
                        (str,),
                    'object_id':
                        (str,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'location_id': 'locationId',
                    'bucket_id': 'bucketId',
                    'object_id': 'objectId',
                },
                'location_map': {
                    'project_id': 'path',
                    'location_id': 'path',
                    'bucket_id': 'path',
                    'object_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__storage_project_bucket_object_download
        )

        def __storage_project_bucket_object_get(
            self,
            project_id,
            location_id,
            bucket_id,
            object_id,
            **kwargs
        ):
            """Get storage/bucket.object  # noqa: E501

            Get storage/bucket.object  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.storage_project_bucket_object_get(project_id, location_id, bucket_id, object_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str): Project Id
                location_id (str): Location Id
                bucket_id (str): Bucket Id
                object_id (str): objectId

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                StorageObject
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['project_id'] = \
                project_id
            kwargs['location_id'] = \
                location_id
            kwargs['bucket_id'] = \
                bucket_id
            kwargs['object_id'] = \
                object_id
            return self.call_with_http_info(**kwargs)

        self.storage_project_bucket_object_get = _Endpoint(
            settings={
                'response_type': (StorageObject,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/storage/{locationId}/project/{projectId}/bucket/{bucketId}/object/{objectId}',
                'operation_id': 'storage_project_bucket_object_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'location_id',
                    'bucket_id',
                    'object_id',
                ],
                'required': [
                    'project_id',
                    'location_id',
                    'bucket_id',
                    'object_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_id':
                        (str,),
                    'location_id':
                        (str,),
                    'bucket_id':
                        (str,),
                    'object_id':
                        (str,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'location_id': 'locationId',
                    'bucket_id': 'bucketId',
                    'object_id': 'objectId',
                },
                'location_map': {
                    'project_id': 'path',
                    'location_id': 'path',
                    'bucket_id': 'path',
                    'object_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__storage_project_bucket_object_get
        )

        def __storage_project_bucket_object_list(
            self,
            project_id,
            location_id,
            bucket_id,
            **kwargs
        ):
            """List storage/bucket.object  # noqa: E501

            List storage/bucket.object  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.storage_project_bucket_object_list(project_id, location_id, bucket_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str): Project Id
                location_id (str): Location Id
                bucket_id (str): Bucket Id

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                [StorageObject]
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['project_id'] = \
                project_id
            kwargs['location_id'] = \
                location_id
            kwargs['bucket_id'] = \
                bucket_id
            return self.call_with_http_info(**kwargs)

        self.storage_project_bucket_object_list = _Endpoint(
            settings={
                'response_type': ([StorageObject],),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/storage/{locationId}/project/{projectId}/bucket/{bucketId}/object',
                'operation_id': 'storage_project_bucket_object_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'location_id',
                    'bucket_id',
                ],
                'required': [
                    'project_id',
                    'location_id',
                    'bucket_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_id':
                        (str,),
                    'location_id':
                        (str,),
                    'bucket_id':
                        (str,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'location_id': 'locationId',
                    'bucket_id': 'bucketId',
                },
                'location_map': {
                    'project_id': 'path',
                    'location_id': 'path',
                    'bucket_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__storage_project_bucket_object_list
        )

        def __storage_project_bucket_upload(
            self,
            project_id,
            location_id,
            bucket_id,
            storage_project_bucket_upload,
            **kwargs
        ):
            """Upload storage/bucket  # noqa: E501

            action upload  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.storage_project_bucket_upload(project_id, location_id, bucket_id, storage_project_bucket_upload, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str): Project Id
                location_id (str): Location Id
                bucket_id (str): Bucket Id
                storage_project_bucket_upload (StorageProjectBucketUpload):

            Keyword Args:
                x_idempotency_key (str): Idempotency key. [optional]
                x_dry_run (str): Dry run. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Bucket
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['project_id'] = \
                project_id
            kwargs['location_id'] = \
                location_id
            kwargs['bucket_id'] = \
                bucket_id
            kwargs['storage_project_bucket_upload'] = \
                storage_project_bucket_upload
            return self.call_with_http_info(**kwargs)

        self.storage_project_bucket_upload = _Endpoint(
            settings={
                'response_type': (Bucket,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/storage/{locationId}/project/{projectId}/bucket/{bucketId}/actions/upload',
                'operation_id': 'storage_project_bucket_upload',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'location_id',
                    'bucket_id',
                    'storage_project_bucket_upload',
                    'x_idempotency_key',
                    'x_dry_run',
                ],
                'required': [
                    'project_id',
                    'location_id',
                    'bucket_id',
                    'storage_project_bucket_upload',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'project_id':
                        (str,),
                    'location_id':
                        (str,),
                    'bucket_id':
                        (str,),
                    'storage_project_bucket_upload':
                        (StorageProjectBucketUpload,),
                    'x_idempotency_key':
                        (str,),
                    'x_dry_run':
                        (str,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'location_id': 'locationId',
                    'bucket_id': 'bucketId',
                    'x_idempotency_key': 'x-idempotency-key',
                    'x_dry_run': 'x-dry-run',
                },
                'location_map': {
                    'project_id': 'path',
                    'location_id': 'path',
                    'bucket_id': 'path',
                    'storage_project_bucket_upload': 'body',
                    'x_idempotency_key': 'header',
                    'x_dry_run': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__storage_project_bucket_upload
        )
