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


class Hdd(object):
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
        'maximum_iops': 'float',
        'controller_type': 'str',
        'controller_number': 'str',
        'controller_location': 'float',
        'disk': 'str',
        'id': 'str'
    }

    attribute_map = {
        'maximum_iops': 'maximumIOPS',
        'controller_type': 'controllerType',
        'controller_number': 'controllerNumber',
        'controller_location': 'controllerLocation',
        'disk': 'disk',
        'id': 'id'
    }

    def __init__(self, maximum_iops=None, controller_type=None, controller_number=None, controller_location=None, disk=None, id=None, local_vars_configuration=None):  # noqa: E501
        """Hdd - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._maximum_iops = None
        self._controller_type = None
        self._controller_number = None
        self._controller_location = None
        self._disk = None
        self._id = None
        self.discriminator = None

        if maximum_iops is not None:
            self.maximum_iops = maximum_iops
        if controller_type is not None:
            self.controller_type = controller_type
        if controller_number is not None:
            self.controller_number = controller_number
        if controller_location is not None:
            self.controller_location = controller_location
        if disk is not None:
            self.disk = disk
        if id is not None:
            self.id = id

    @property
    def maximum_iops(self):
        """Gets the maximum_iops of this Hdd.  # noqa: E501


        :return: The maximum_iops of this Hdd.  # noqa: E501
        :rtype: float
        """
        return self._maximum_iops

    @maximum_iops.setter
    def maximum_iops(self, maximum_iops):
        """Sets the maximum_iops of this Hdd.


        :param maximum_iops: The maximum_iops of this Hdd.  # noqa: E501
        :type: float
        """

        self._maximum_iops = maximum_iops

    @property
    def controller_type(self):
        """Gets the controller_type of this Hdd.  # noqa: E501


        :return: The controller_type of this Hdd.  # noqa: E501
        :rtype: str
        """
        return self._controller_type

    @controller_type.setter
    def controller_type(self, controller_type):
        """Sets the controller_type of this Hdd.


        :param controller_type: The controller_type of this Hdd.  # noqa: E501
        :type: str
        """

        self._controller_type = controller_type

    @property
    def controller_number(self):
        """Gets the controller_number of this Hdd.  # noqa: E501


        :return: The controller_number of this Hdd.  # noqa: E501
        :rtype: str
        """
        return self._controller_number

    @controller_number.setter
    def controller_number(self, controller_number):
        """Sets the controller_number of this Hdd.


        :param controller_number: The controller_number of this Hdd.  # noqa: E501
        :type: str
        """

        self._controller_number = controller_number

    @property
    def controller_location(self):
        """Gets the controller_location of this Hdd.  # noqa: E501


        :return: The controller_location of this Hdd.  # noqa: E501
        :rtype: float
        """
        return self._controller_location

    @controller_location.setter
    def controller_location(self, controller_location):
        """Sets the controller_location of this Hdd.


        :param controller_location: The controller_location of this Hdd.  # noqa: E501
        :type: float
        """

        self._controller_location = controller_location

    @property
    def disk(self):
        """Gets the disk of this Hdd.  # noqa: E501


        :return: The disk of this Hdd.  # noqa: E501
        :rtype: str
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this Hdd.


        :param disk: The disk of this Hdd.  # noqa: E501
        :type: str
        """

        self._disk = disk

    @property
    def id(self):
        """Gets the id of this Hdd.  # noqa: E501


        :return: The id of this Hdd.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Hdd.


        :param id: The id of this Hdd.  # noqa: E501
        :type: str
        """

        self._id = id

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
        if not isinstance(other, Hdd):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Hdd):
            return True

        return self.to_dict() != other.to_dict()
