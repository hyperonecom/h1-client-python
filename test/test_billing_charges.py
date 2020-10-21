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

import h1-client-python
from h1-client-python.models.billing_charges import BillingCharges  # noqa: E501
from h1-client-python.rest import ApiException

class TestBillingCharges(unittest.TestCase):
    """BillingCharges unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BillingCharges
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = h1-client-python.models.billing_charges.BillingCharges()  # noqa: E501
        if include_optional :
            return BillingCharges(
                id = '0', 
                value = 1.337, 
                start = '0', 
                end = '0', 
                price = 1.337, 
                quantity = 1.337, 
                paid_from = '0', 
                paid_on = '0'
            )
        else :
            return BillingCharges(
        )

    def testBillingCharges(self):
        """Test BillingCharges"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()