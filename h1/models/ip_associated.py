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


class IpAssociated(object):
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
        'ip': 'str',
        'fip': 'str',
        'netadp': 'str'
    }

    attribute_map = {
        'ip': 'ip',
        'fip': 'fip',
        'netadp': 'netadp'
    }

    def __init__(self, ip=None, fip=None, netadp=None, local_vars_configuration=None):  # noqa: E501
        """IpAssociated - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ip = None
        self._fip = None
        self._netadp = None
        self.discriminator = None

        if ip is not None:
            self.ip = ip
        if fip is not None:
            self.fip = fip
        if netadp is not None:
            self.netadp = netadp

    @property
    def ip(self):
        """Gets the ip of this IpAssociated.  # noqa: E501


        :return: The ip of this IpAssociated.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this IpAssociated.


        :param ip: The ip of this IpAssociated.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def fip(self):
        """Gets the fip of this IpAssociated.  # noqa: E501


        :return: The fip of this IpAssociated.  # noqa: E501
        :rtype: str
        """
        return self._fip

    @fip.setter
    def fip(self, fip):
        """Sets the fip of this IpAssociated.


        :param fip: The fip of this IpAssociated.  # noqa: E501
        :type: str
        """

        self._fip = fip

    @property
    def netadp(self):
        """Gets the netadp of this IpAssociated.  # noqa: E501


        :return: The netadp of this IpAssociated.  # noqa: E501
        :rtype: str
        """
        return self._netadp

    @netadp.setter
    def netadp(self, netadp):
        """Sets the netadp of this IpAssociated.


        :param netadp: The netadp of this IpAssociated.  # noqa: E501
        :type: str
        """

        self._netadp = netadp

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
        if not isinstance(other, IpAssociated):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IpAssociated):
            return True

        return self.to_dict() != other.to_dict()