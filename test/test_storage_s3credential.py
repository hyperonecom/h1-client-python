# coding: utf-8

"""
    HyperOne

    HyperOne API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import h1
from h1.models.storage_s3credential import StorageS3credential  # noqa: E501
from h1.rest import ApiException

class TestStorageS3credential(unittest.TestCase):
    """StorageS3credential unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StorageS3credential
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = h1.models.storage_s3credential.StorageS3credential()  # noqa: E501
        if include_optional :
            return StorageS3credential(
                access_key_id = '0', 
                session_token = '0', 
                secret_access_key = '0', 
                endpoint = '0', 
                region = '0', 
                location = '0', 
                bucket = '0', 
                key = '0'
            )
        else :
            return StorageS3credential(
        )

    def testStorageS3credential(self):
        """Test StorageS3credential"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
