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
from h1.models.iam_organisation_update import IamOrganisationUpdate  # noqa: E501
from h1.rest import ApiException

class TestIamOrganisationUpdate(unittest.TestCase):
    """IamOrganisationUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test IamOrganisationUpdate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = h1.models.iam_organisation_update.IamOrganisationUpdate()  # noqa: E501
        if include_optional :
            return IamOrganisationUpdate(
                name = '0', 
                billing = h1.models.organisation_billing_1.Organisation_billing_1(
                    email = '0', 
                    company = '0', 
                    address = h1.models.billing_address_1.Billing_address_1(
                        city = '0', 
                        zipcode = '0', 
                        street = '0', ), )
            )
        else :
            return IamOrganisationUpdate(
        )

    def testIamOrganisationUpdate(self):
        """Test IamOrganisationUpdate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
