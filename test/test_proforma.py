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
from h1-client-python.models.proforma import Proforma  # noqa: E501
from h1-client-python.rest import ApiException

class TestProforma(unittest.TestCase):
    """Proforma unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Proforma
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = h1-client-python.models.proforma.Proforma()  # noqa: E501
        if include_optional :
            return Proforma(
                id = '0', 
                invoice_no = '0', 
                seller = h1-client-python.models.proforma_seller.proforma_seller(
                    company = '0', 
                    address = h1-client-python.models.invoice_seller_address.invoice_seller_address(
                        street = '0', 
                        zipcode = '0', 
                        city = '0', 
                        country = '0', ), 
                    nip = '0', 
                    iban = '0', ), 
                buyer = h1-client-python.models.invoice_buyer.invoice_buyer(
                    company = '0', 
                    address = h1-client-python.models.invoice_buyer_address.invoice_buyer_address(
                        street = '0', 
                        zipcode = '0', 
                        city = '0', 
                        country = '0', ), 
                    nip = '0', 
                    email = '0', ), 
                issue_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                items = [
                    h1-client-python.models.invoice_items.invoice_items(
                        name = '0', 
                        price = '0', 
                        netto = '0', 
                        brutto = '0', 
                        vat_amount = '0', 
                        vat_rate = '0', 
                        quantity = 1.337, )
                    ], 
                summary = '0', 
                project = '0', 
                uri = '0', 
                array__ = h1-client-python.models.proforma___array__.proforma___array__(
                    id = '0', 
                    invoice_no = '0', 
                    issue_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    summary = '0', 
                    project = '0', 
                    uri = '0', )
            )
        else :
            return Proforma(
        )

    def testProforma(self):
        """Test Proforma"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
