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
from h1.models.organisation import Organisation  # noqa: E501
from h1.rest import ApiException

class TestOrganisation(unittest.TestCase):
    """Organisation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Organisation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = h1.models.organisation.Organisation()  # noqa: E501
        if include_optional :
            return Organisation(
                id = '0', 
                name = '0', 
                flavour = '0', 
                modified_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                modified_by = '0', 
                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                created_by = '0', 
                state = 'Active', 
                organisation = '0', 
                uri = '0', 
                billing = h1.models.organisation_billing.organisation_billing(
                    currency = '0', 
                    company = '0', 
                    email = '0', 
                    address = h1.models.invoice_seller_address.invoice_seller_address(
                        street = '0', 
                        zipcode = '0', 
                        city = '0', 
                        country = '0', ), 
                    nip = '0', ), 
                transfer = h1.models.organisation_transfer.organisation_transfer(
                    name = '0', 
                    id = '0', ), 
                bank_account = '0', 
                tag = [
                    h1.models.tag.tag(
                        id = '0', 
                        key = '0', 
                        value = '0', )
                    ]
            )
        else :
            return Organisation(
        )

    def testOrganisation(self):
        """Test Organisation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
