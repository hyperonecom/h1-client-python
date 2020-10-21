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
from h1-client-python.models.event import Event  # noqa: E501
from h1-client-python.rest import ApiException

class TestEvent(unittest.TestCase):
    """Event unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Event
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = h1-client-python.models.event.Event()  # noqa: E501
        if include_optional :
            return Event(
                id = '0', 
                name = '0', 
                created_by = '0', 
                created_on = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                state = 'pending', 
                stage = '0', 
                resource = '0'
            )
        else :
            return Event(
        )

    def testEvent(self):
        """Test Event"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
