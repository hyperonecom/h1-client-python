"""
    HyperOne

    HyperOne API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import h1
from h1.model.disk_metadata import DiskMetadata
from h1.model.tag import Tag
globals()['DiskMetadata'] = DiskMetadata
globals()['Tag'] = Tag
from h1.model.disk import Disk


class TestDisk(unittest.TestCase):
    """Disk unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDisk(self):
        """Test Disk"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Disk()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
