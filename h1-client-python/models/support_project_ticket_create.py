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

from h1-client-python.configuration import Configuration


class SupportProjectTicketCreate(object):
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
        'type': 'str',
        'subject': 'str',
        'message': 'str'
    }

    attribute_map = {
        'type': 'type',
        'subject': 'subject',
        'message': 'message'
    }

    def __init__(self, type=None, subject=None, message=None, local_vars_configuration=None):  # noqa: E501
        """SupportProjectTicketCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._subject = None
        self._message = None
        self.discriminator = None

        self.type = type
        self.subject = subject
        self.message = message

    @property
    def type(self):
        """Gets the type of this SupportProjectTicketCreate.  # noqa: E501


        :return: The type of this SupportProjectTicketCreate.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SupportProjectTicketCreate.


        :param type: The type of this SupportProjectTicketCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["sales", "billing", "service support"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def subject(self):
        """Gets the subject of this SupportProjectTicketCreate.  # noqa: E501


        :return: The subject of this SupportProjectTicketCreate.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this SupportProjectTicketCreate.


        :param subject: The subject of this SupportProjectTicketCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and subject is None:  # noqa: E501
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def message(self):
        """Gets the message of this SupportProjectTicketCreate.  # noqa: E501


        :return: The message of this SupportProjectTicketCreate.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this SupportProjectTicketCreate.


        :param message: The message of this SupportProjectTicketCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

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
        if not isinstance(other, SupportProjectTicketCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SupportProjectTicketCreate):
            return True

        return self.to_dict() != other.to_dict()
