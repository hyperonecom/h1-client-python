# coding: utf-8

"""
    HyperOne

    HyperOne API  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from h1.configuration import Configuration


class NetworkingRule(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'action': 'str',
        'priority': 'float',
        'filter': 'list[str]',
        'external': 'list[str]',
        'internal': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'action': 'action',
        'priority': 'priority',
        'filter': 'filter',
        'external': 'external',
        'internal': 'internal'
    }

    def __init__(self, id=None, name=None, action=None, priority=None, filter=None, external=["0.0.0.0/0"], internal=["*"], local_vars_configuration=None):  # noqa: E501
        """NetworkingRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._action = None
        self._priority = None
        self._filter = None
        self._external = None
        self._internal = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.action = action
        self.priority = priority
        self.filter = filter
        if external is not None:
            self.external = external
        if internal is not None:
            self.internal = internal

    @property
    def id(self):
        """Gets the id of this NetworkingRule.  # noqa: E501


        :return: The id of this NetworkingRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetworkingRule.


        :param id: The id of this NetworkingRule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NetworkingRule.  # noqa: E501


        :return: The name of this NetworkingRule.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetworkingRule.


        :param name: The name of this NetworkingRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def action(self):
        """Gets the action of this NetworkingRule.  # noqa: E501


        :return: The action of this NetworkingRule.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this NetworkingRule.


        :param action: The action of this NetworkingRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and action is None:  # noqa: E501
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501
        allowed_values = ["allow", "deny"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and action not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def priority(self):
        """Gets the priority of this NetworkingRule.  # noqa: E501


        :return: The priority of this NetworkingRule.  # noqa: E501
        :rtype: float
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this NetworkingRule.


        :param priority: The priority of this NetworkingRule.  # noqa: E501
        :type: float
        """
        if self.local_vars_configuration.client_side_validation and priority is None:  # noqa: E501
            raise ValueError("Invalid value for `priority`, must not be `None`")  # noqa: E501

        self._priority = priority

    @property
    def filter(self):
        """Gets the filter of this NetworkingRule.  # noqa: E501


        :return: The filter of this NetworkingRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this NetworkingRule.


        :param filter: The filter of this NetworkingRule.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and filter is None:  # noqa: E501
            raise ValueError("Invalid value for `filter`, must not be `None`")  # noqa: E501

        self._filter = filter

    @property
    def external(self):
        """Gets the external of this NetworkingRule.  # noqa: E501


        :return: The external of this NetworkingRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._external

    @external.setter
    def external(self, external):
        """Sets the external of this NetworkingRule.


        :param external: The external of this NetworkingRule.  # noqa: E501
        :type: list[str]
        """

        self._external = external

    @property
    def internal(self):
        """Gets the internal of this NetworkingRule.  # noqa: E501


        :return: The internal of this NetworkingRule.  # noqa: E501
        :rtype: list[str]
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this NetworkingRule.


        :param internal: The internal of this NetworkingRule.  # noqa: E501
        :type: list[str]
        """

        self._internal = internal

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NetworkingRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkingRule):
            return True

        return self.to_dict() != other.to_dict()
