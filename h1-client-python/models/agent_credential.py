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


class AgentCredential(object):
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
        'created_by': 'str',
        'created_on': 'datetime',
        'type': 'str',
        'value': 'str',
        'fingerprint': 'str',
        'token': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'type': 'type',
        'value': 'value',
        'fingerprint': 'fingerprint',
        'token': 'token'
    }

    def __init__(self, id=None, name=None, created_by=None, created_on=None, type=None, value=None, fingerprint=None, token=None, local_vars_configuration=None):  # noqa: E501
        """AgentCredential - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._created_by = None
        self._created_on = None
        self._type = None
        self._value = None
        self._fingerprint = None
        self._token = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        self.type = type
        self.value = value
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if token is not None:
            self.token = token

    @property
    def id(self):
        """Gets the id of this AgentCredential.  # noqa: E501


        :return: The id of this AgentCredential.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AgentCredential.


        :param id: The id of this AgentCredential.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AgentCredential.  # noqa: E501


        :return: The name of this AgentCredential.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AgentCredential.


        :param name: The name of this AgentCredential.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def created_by(self):
        """Gets the created_by of this AgentCredential.  # noqa: E501


        :return: The created_by of this AgentCredential.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this AgentCredential.


        :param created_by: The created_by of this AgentCredential.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this AgentCredential.  # noqa: E501


        :return: The created_on of this AgentCredential.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this AgentCredential.


        :param created_on: The created_on of this AgentCredential.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def type(self):
        """Gets the type of this AgentCredential.  # noqa: E501


        :return: The type of this AgentCredential.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AgentCredential.


        :param type: The type of this AgentCredential.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["ssh"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value(self):
        """Gets the value of this AgentCredential.  # noqa: E501


        :return: The value of this AgentCredential.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AgentCredential.


        :param value: The value of this AgentCredential.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def fingerprint(self):
        """Gets the fingerprint of this AgentCredential.  # noqa: E501


        :return: The fingerprint of this AgentCredential.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this AgentCredential.


        :param fingerprint: The fingerprint of this AgentCredential.  # noqa: E501
        :type: str
        """

        self._fingerprint = fingerprint

    @property
    def token(self):
        """Gets the token of this AgentCredential.  # noqa: E501


        :return: The token of this AgentCredential.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AgentCredential.


        :param token: The token of this AgentCredential.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if not isinstance(other, AgentCredential):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AgentCredential):
            return True

        return self.to_dict() != other.to_dict()
