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


class NetworkingProjectNetgwCreate(object):
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
        'name': 'str',
        'public': 'NetgwPublic',
        'tag': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'public': 'public',
        'tag': 'tag'
    }

    def __init__(self, name=None, public=None, tag=None, local_vars_configuration=None):  # noqa: E501
        """NetworkingProjectNetgwCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._public = None
        self._tag = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if public is not None:
            self.public = public
        if tag is not None:
            self.tag = tag

    @property
    def name(self):
        """Gets the name of this NetworkingProjectNetgwCreate.  # noqa: E501


        :return: The name of this NetworkingProjectNetgwCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetworkingProjectNetgwCreate.


        :param name: The name of this NetworkingProjectNetgwCreate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def public(self):
        """Gets the public of this NetworkingProjectNetgwCreate.  # noqa: E501


        :return: The public of this NetworkingProjectNetgwCreate.  # noqa: E501
        :rtype: NetgwPublic
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this NetworkingProjectNetgwCreate.


        :param public: The public of this NetworkingProjectNetgwCreate.  # noqa: E501
        :type: NetgwPublic
        """

        self._public = public

    @property
    def tag(self):
        """Gets the tag of this NetworkingProjectNetgwCreate.  # noqa: E501


        :return: The tag of this NetworkingProjectNetgwCreate.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this NetworkingProjectNetgwCreate.


        :param tag: The tag of this NetworkingProjectNetgwCreate.  # noqa: E501
        :type: list[Tag]
        """

        self._tag = tag

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
        if not isinstance(other, NetworkingProjectNetgwCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkingProjectNetgwCreate):
            return True

        return self.to_dict() != other.to_dict()
