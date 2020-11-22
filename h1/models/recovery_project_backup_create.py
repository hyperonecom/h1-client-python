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


class RecoveryProjectBackupCreate(object):
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
        'service': 'str',
        'source': 'str',
        'tag': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'service': 'service',
        'source': 'source',
        'tag': 'tag'
    }

    def __init__(self, name=None, service=None, source=None, tag=None, local_vars_configuration=None):  # noqa: E501
        """RecoveryProjectBackupCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._service = None
        self._source = None
        self._tag = None
        self.discriminator = None

        self.name = name
        self.service = service
        if source is not None:
            self.source = source
        if tag is not None:
            self.tag = tag

    @property
    def name(self):
        """Gets the name of this RecoveryProjectBackupCreate.  # noqa: E501


        :return: The name of this RecoveryProjectBackupCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RecoveryProjectBackupCreate.


        :param name: The name of this RecoveryProjectBackupCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def service(self):
        """Gets the service of this RecoveryProjectBackupCreate.  # noqa: E501


        :return: The service of this RecoveryProjectBackupCreate.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this RecoveryProjectBackupCreate.


        :param service: The service of this RecoveryProjectBackupCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and service is None:  # noqa: E501
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def source(self):
        """Gets the source of this RecoveryProjectBackupCreate.  # noqa: E501


        :return: The source of this RecoveryProjectBackupCreate.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this RecoveryProjectBackupCreate.


        :param source: The source of this RecoveryProjectBackupCreate.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def tag(self):
        """Gets the tag of this RecoveryProjectBackupCreate.  # noqa: E501


        :return: The tag of this RecoveryProjectBackupCreate.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this RecoveryProjectBackupCreate.


        :param tag: The tag of this RecoveryProjectBackupCreate.  # noqa: E501
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
        if not isinstance(other, RecoveryProjectBackupCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RecoveryProjectBackupCreate):
            return True

        return self.to_dict() != other.to_dict()
