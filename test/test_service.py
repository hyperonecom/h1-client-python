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
from h1.models.service import Service  # noqa: E501
from h1.rest import ApiException

class TestService(unittest.TestCase):
    """Service unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Service
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = h1.models.service.Service()  # noqa: E501
        if include_optional :
            return Service(
                id = '0', 
                resource = '0', 
                type = '0', 
                billing = h1.models.service_billing.service_billing(
                    price = h1.models.service_billing_price.service_billing_price(
                        pln = 1.337, 
                        eur = 1.337, 
                        usd = 1.337, 
                        gbp = 1.337, ), 
                    period = '0', 
                    quantity = 1.337, 
                    one_time = True, 
                    reservations = h1.models.service_billing_reservations.service_billing_reservations(
                        id = '0', 
                        period = '0', 
                        resource_price = h1.models.service_billing_price.service_billing_price(
                            pln = 1.337, 
                            eur = 1.337, 
                            usd = 1.337, 
                            gbp = 1.337, ), ), ), 
                display = h1.models.service_display.service_display(
                    unit = h1.models.service_display_unit.service_display_unit(
                        usage = '0', 
                        billing = '0', ), ), 
                data = {
                    'key' : '0'
                    }, 
                name = '0', 
                available_services = [
                    '0'
                    ], 
                uri = '0'
            )
        else :
            return Service(
        )

    def testService(self):
        """Test Service"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
