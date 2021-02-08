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
from h1.model.inline_response400 import InlineResponse400
from h1.model.service import Service


class BillingProjectServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __billing_project_service_get(
            self,
            project_id,
            service_id,
            **kwargs
        ):
            """Get billing/service  # noqa: E501

            Returns a single service  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.billing_project_service_get(project_id, service_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str): Project Id
                service_id (str): Service Id

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
                Service
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
            kwargs['service_id'] = \
                service_id
            return self.call_with_http_info(**kwargs)

        self.billing_project_service_get = _Endpoint(
            settings={
                'response_type': (Service,),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/billing/project/{projectId}/service/{serviceId}',
                'operation_id': 'billing_project_service_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'service_id',
                ],
                'required': [
                    'project_id',
                    'service_id',
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
                    'service_id':
                        (str,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'service_id': 'serviceId',
                },
                'location_map': {
                    'project_id': 'path',
                    'service_id': 'path',
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
            callable=__billing_project_service_get
        )

        def __billing_project_service_list(
            self,
            project_id,
            **kwargs
        ):
            """List billing/service  # noqa: E501

            List service  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.billing_project_service_list(project_id, async_req=True)
            >>> result = thread.get()

            Args:
                project_id (str): Project Id

            Keyword Args:
                kind (str): Filter by kind. [optional]
                name (str): Filter by name. [optional]
                type (str): Filter by type. [optional]
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
                [Service]
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
            return self.call_with_http_info(**kwargs)

        self.billing_project_service_list = _Endpoint(
            settings={
                'response_type': ([Service],),
                'auth': [
                    'BearerAuth'
                ],
                'endpoint_path': '/billing/project/{projectId}/service',
                'operation_id': 'billing_project_service_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'project_id',
                    'kind',
                    'name',
                    'type',
                ],
                'required': [
                    'project_id',
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
                    'kind':
                        (str,),
                    'name':
                        (str,),
                    'type':
                        (str,),
                },
                'attribute_map': {
                    'project_id': 'projectId',
                    'kind': 'kind',
                    'name': 'name',
                    'type': 'type',
                },
                'location_map': {
                    'project_id': 'path',
                    'kind': 'query',
                    'name': 'query',
                    'type': 'query',
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
            callable=__billing_project_service_list
        )
