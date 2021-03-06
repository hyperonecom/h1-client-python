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
from h1.models.agent_resource_event import AgentResourceEvent  # noqa: E501
from h1.rest import ApiException

class TestAgentResourceEvent(unittest.TestCase):
    """AgentResourceEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AgentResourceEvent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = h1.models.agent_resource_event.AgentResourceEvent()  # noqa: E501
        if include_optional :
            return AgentResourceEvent(
                id = '0', 
                name = '0', 
                state = '0', 
                created_on = '0', 
                project = '0'
            )
        else :
            return AgentResourceEvent(
        )

    def testAgentResourceEvent(self):
        """Test AgentResourceEvent"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
