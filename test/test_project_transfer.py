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
from h1.models.project_transfer import ProjectTransfer  # noqa: E501
from h1.rest import ApiException

class TestProjectTransfer(unittest.TestCase):
    """ProjectTransfer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectTransfer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = h1.models.project_transfer.ProjectTransfer()  # noqa: E501
        if include_optional :
            return ProjectTransfer(
                organisation = '0'
            )
        else :
            return ProjectTransfer(
        )

    def testProjectTransfer(self):
        """Test ProjectTransfer"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
