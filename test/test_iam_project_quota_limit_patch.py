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
from h1.models.iam_project_quota_limit_patch import IamProjectQuotaLimitPatch  # noqa: E501
from h1.rest import ApiException

class TestIamProjectQuotaLimitPatch(unittest.TestCase):
    """IamProjectQuotaLimitPatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IamProjectQuotaLimitPatch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = h1.models.iam_project_quota_limit_patch.IamProjectQuotaLimitPatch()  # noqa: E501
        if include_optional :
            return IamProjectQuotaLimitPatch(
                user = 1.337, 
                effective = 1.337
            )
        else :
            return IamProjectQuotaLimitPatch(
        )

    def testIamProjectQuotaLimitPatch(self):
        """Test IamProjectQuotaLimitPatch"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
