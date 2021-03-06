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


class IamProjectThresholdCreate(object):
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
        'type': 'str',
        'value': 'float',
        'uri': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'value': 'value',
        'uri': 'uri'
    }

    def __init__(self, id=None, name=None, type=None, value=None, uri=None, local_vars_configuration=None):  # noqa: E501
        """IamProjectThresholdCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._type = None
        self._value = None
        self._uri = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if uri is not None:
            self.uri = uri

    @property
    def id(self):
        """Gets the id of this IamProjectThresholdCreate.  # noqa: E501


        :return: The id of this IamProjectThresholdCreate.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IamProjectThresholdCreate.


        :param id: The id of this IamProjectThresholdCreate.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this IamProjectThresholdCreate.  # noqa: E501


        :return: The name of this IamProjectThresholdCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IamProjectThresholdCreate.


        :param name: The name of this IamProjectThresholdCreate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this IamProjectThresholdCreate.  # noqa: E501


        :return: The type of this IamProjectThresholdCreate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IamProjectThresholdCreate.


        :param type: The type of this IamProjectThresholdCreate.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def value(self):
        """Gets the value of this IamProjectThresholdCreate.  # noqa: E501


        :return: The value of this IamProjectThresholdCreate.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this IamProjectThresholdCreate.


        :param value: The value of this IamProjectThresholdCreate.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def uri(self):
        """Gets the uri of this IamProjectThresholdCreate.  # noqa: E501


        :return: The uri of this IamProjectThresholdCreate.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this IamProjectThresholdCreate.


        :param uri: The uri of this IamProjectThresholdCreate.  # noqa: E501
        :type: str
        """

        self._uri = uri

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
        if not isinstance(other, IamProjectThresholdCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IamProjectThresholdCreate):
            return True

        return self.to_dict() != other.to_dict()
