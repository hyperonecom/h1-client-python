"""
    HyperOne

    HyperOne API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import h1
from h1.model.invoice_buyer import InvoiceBuyer
from h1.model.invoice_duplicate import InvoiceDuplicate
from h1.model.invoice_items import InvoiceItems
from h1.model.invoice_seller import InvoiceSeller
globals()['InvoiceBuyer'] = InvoiceBuyer
globals()['InvoiceDuplicate'] = InvoiceDuplicate
globals()['InvoiceItems'] = InvoiceItems
globals()['InvoiceSeller'] = InvoiceSeller
from h1.model.invoice import Invoice


class TestInvoice(unittest.TestCase):
    """Invoice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInvoice(self):
        """Test Invoice"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Invoice()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
