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


class StorageProjectIsoDetach(object):
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
        'vm': 'str'
    }

    attribute_map = {
        'vm': 'vm'
    }

    def __init__(self, vm=None, local_vars_configuration=None):  # noqa: E501
        """StorageProjectIsoDetach - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._vm = None
        self.discriminator = None

        self.vm = vm

    @property
    def vm(self):
        """Gets the vm of this StorageProjectIsoDetach.  # noqa: E501


        :return: The vm of this StorageProjectIsoDetach.  # noqa: E501
        :rtype: str
        """
        return self._vm

    @vm.setter
    def vm(self, vm):
        """Sets the vm of this StorageProjectIsoDetach.


        :param vm: The vm of this StorageProjectIsoDetach.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and vm is None:  # noqa: E501
            raise ValueError("Invalid value for `vm`, must not be `None`")  # noqa: E501

        self._vm = vm

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
        if not isinstance(other, StorageProjectIsoDetach):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageProjectIsoDetach):
            return True

        return self.to_dict() != other.to_dict()
