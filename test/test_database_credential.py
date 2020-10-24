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
from h1.models.database_credential import DatabaseCredential  # noqa: E501
from h1.rest import ApiException

class TestDatabaseCredential(unittest.TestCase):
    """DatabaseCredential unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DatabaseCredential
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = h1.models.database_credential.DatabaseCredential()  # noqa: E501
        if include_optional :
            return DatabaseCredential(
                id = '0', 
                name = '0', 
                created_by = '0', 
                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                type = 'mysql', 
                value = '0', 
                fingerprint = '0', 
                token = '0'
            )
        else :
            return DatabaseCredential(
                name = '0',
                type = 'mysql',
                value = '0',
        )

    def testDatabaseCredential(self):
        """Test DatabaseCredential"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
