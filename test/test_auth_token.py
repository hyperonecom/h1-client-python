"""
    HyperOne

    HyperOne API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import h1
from h1.model.auth_token_access import AuthTokenAccess
globals()['AuthTokenAccess'] = AuthTokenAccess
from h1.model.auth_token import AuthToken


class TestAuthToken(unittest.TestCase):
    """AuthToken unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAuthToken(self):
        """Test AuthToken"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AuthToken()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
