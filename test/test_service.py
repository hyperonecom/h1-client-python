"""
    HyperOne

    HyperOne API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import h1
from h1.model.service_billing import ServiceBilling
from h1.model.service_display import ServiceDisplay
globals()['ServiceBilling'] = ServiceBilling
globals()['ServiceDisplay'] = ServiceDisplay
from h1.model.service import Service


class TestService(unittest.TestCase):
    """Service unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testService(self):
        """Test Service"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Service()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
