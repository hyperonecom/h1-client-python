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


class AuthToken(object):
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
        'expiry': 'datetime',
        'created_by': 'str',
        'created_on': 'datetime',
        'access': 'list[AuthTokenAccess]',
        'name': 'str',
        'client_ip': 'str',
        'user_agent': 'str'
    }

    attribute_map = {
        'id': 'id',
        'expiry': 'expiry',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'access': 'access',
        'name': 'name',
        'client_ip': 'clientIp',
        'user_agent': 'userAgent'
    }

    def __init__(self, id=None, expiry=None, created_by=None, created_on=None, access=None, name=None, client_ip=None, user_agent=None, local_vars_configuration=None):  # noqa: E501
        """AuthToken - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._expiry = None
        self._created_by = None
        self._created_on = None
        self._access = None
        self._name = None
        self._client_ip = None
        self._user_agent = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if expiry is not None:
            self.expiry = expiry
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if access is not None:
            self.access = access
        if name is not None:
            self.name = name
        if client_ip is not None:
            self.client_ip = client_ip
        if user_agent is not None:
            self.user_agent = user_agent

    @property
    def id(self):
        """Gets the id of this AuthToken.  # noqa: E501


        :return: The id of this AuthToken.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthToken.


        :param id: The id of this AuthToken.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def expiry(self):
        """Gets the expiry of this AuthToken.  # noqa: E501


        :return: The expiry of this AuthToken.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this AuthToken.


        :param expiry: The expiry of this AuthToken.  # noqa: E501
        :type: datetime
        """

        self._expiry = expiry

    @property
    def created_by(self):
        """Gets the created_by of this AuthToken.  # noqa: E501


        :return: The created_by of this AuthToken.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this AuthToken.


        :param created_by: The created_by of this AuthToken.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this AuthToken.  # noqa: E501


        :return: The created_on of this AuthToken.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this AuthToken.


        :param created_on: The created_on of this AuthToken.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def access(self):
        """Gets the access of this AuthToken.  # noqa: E501


        :return: The access of this AuthToken.  # noqa: E501
        :rtype: list[AuthTokenAccess]
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this AuthToken.


        :param access: The access of this AuthToken.  # noqa: E501
        :type: list[AuthTokenAccess]
        """

        self._access = access

    @property
    def name(self):
        """Gets the name of this AuthToken.  # noqa: E501


        :return: The name of this AuthToken.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthToken.


        :param name: The name of this AuthToken.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def client_ip(self):
        """Gets the client_ip of this AuthToken.  # noqa: E501


        :return: The client_ip of this AuthToken.  # noqa: E501
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        """Sets the client_ip of this AuthToken.


        :param client_ip: The client_ip of this AuthToken.  # noqa: E501
        :type: str
        """

        self._client_ip = client_ip

    @property
    def user_agent(self):
        """Gets the user_agent of this AuthToken.  # noqa: E501


        :return: The user_agent of this AuthToken.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this AuthToken.


        :param user_agent: The user_agent of this AuthToken.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

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
        if not isinstance(other, AuthToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthToken):
            return True

        return self.to_dict() != other.to_dict()
