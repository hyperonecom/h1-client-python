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


class Payment(object):
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
        'modified_on': 'datetime',
        'modified_by': 'str',
        'created_on': 'datetime',
        'created_by': 'str',
        'state': 'str',
        'project': 'str',
        'uri': 'str',
        'credits_free': 'float',
        'credits': 'float',
        'channel': 'str',
        'amount': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'modified_on': 'modifiedOn',
        'modified_by': 'modifiedBy',
        'created_on': 'createdOn',
        'created_by': 'createdBy',
        'state': 'state',
        'project': 'project',
        'uri': 'uri',
        'credits_free': 'creditsFree',
        'credits': 'credits',
        'channel': 'channel',
        'amount': 'amount'
    }

    def __init__(self, id=None, name=None, modified_on=None, modified_by=None, created_on=None, created_by=None, state=None, project=None, uri=None, credits_free=None, credits=None, channel=None, amount=None, local_vars_configuration=None):  # noqa: E501
        """Payment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._modified_on = None
        self._modified_by = None
        self._created_on = None
        self._created_by = None
        self._state = None
        self._project = None
        self._uri = None
        self._credits_free = None
        self._credits = None
        self._channel = None
        self._amount = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if modified_on is not None:
            self.modified_on = modified_on
        if modified_by is not None:
            self.modified_by = modified_by
        if created_on is not None:
            self.created_on = created_on
        if created_by is not None:
            self.created_by = created_by
        if state is not None:
            self.state = state
        if project is not None:
            self.project = project
        if uri is not None:
            self.uri = uri
        if credits_free is not None:
            self.credits_free = credits_free
        if credits is not None:
            self.credits = credits
        if channel is not None:
            self.channel = channel
        if amount is not None:
            self.amount = amount

    @property
    def id(self):
        """Gets the id of this Payment.  # noqa: E501


        :return: The id of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Payment.


        :param id: The id of this Payment.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Payment.  # noqa: E501


        :return: The name of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Payment.


        :param name: The name of this Payment.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def modified_on(self):
        """Gets the modified_on of this Payment.  # noqa: E501


        :return: The modified_on of this Payment.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_on

    @modified_on.setter
    def modified_on(self, modified_on):
        """Sets the modified_on of this Payment.


        :param modified_on: The modified_on of this Payment.  # noqa: E501
        :type: datetime
        """

        self._modified_on = modified_on

    @property
    def modified_by(self):
        """Gets the modified_by of this Payment.  # noqa: E501


        :return: The modified_by of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this Payment.


        :param modified_by: The modified_by of this Payment.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def created_on(self):
        """Gets the created_on of this Payment.  # noqa: E501


        :return: The created_on of this Payment.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Payment.


        :param created_on: The created_on of this Payment.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def created_by(self):
        """Gets the created_by of this Payment.  # noqa: E501


        :return: The created_by of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Payment.


        :param created_by: The created_by of this Payment.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def state(self):
        """Gets the state of this Payment.  # noqa: E501


        :return: The state of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Payment.


        :param state: The state of this Payment.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unallocated", "Allocated", "Expired"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def project(self):
        """Gets the project of this Payment.  # noqa: E501


        :return: The project of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Payment.


        :param project: The project of this Payment.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def uri(self):
        """Gets the uri of this Payment.  # noqa: E501


        :return: The uri of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Payment.


        :param uri: The uri of this Payment.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def credits_free(self):
        """Gets the credits_free of this Payment.  # noqa: E501


        :return: The credits_free of this Payment.  # noqa: E501
        :rtype: float
        """
        return self._credits_free

    @credits_free.setter
    def credits_free(self, credits_free):
        """Sets the credits_free of this Payment.


        :param credits_free: The credits_free of this Payment.  # noqa: E501
        :type: float
        """

        self._credits_free = credits_free

    @property
    def credits(self):
        """Gets the credits of this Payment.  # noqa: E501


        :return: The credits of this Payment.  # noqa: E501
        :rtype: float
        """
        return self._credits

    @credits.setter
    def credits(self, credits):
        """Sets the credits of this Payment.


        :param credits: The credits of this Payment.  # noqa: E501
        :type: float
        """

        self._credits = credits

    @property
    def channel(self):
        """Gets the channel of this Payment.  # noqa: E501


        :return: The channel of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this Payment.


        :param channel: The channel of this Payment.  # noqa: E501
        :type: str
        """
        allowed_values = ["bank", "dotpay", "promo", "paypal", "ecard", "przelewy24"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and channel not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `channel` ({0}), must be one of {1}"  # noqa: E501
                .format(channel, allowed_values)
            )

        self._channel = channel

    @property
    def amount(self):
        """Gets the amount of this Payment.  # noqa: E501


        :return: The amount of this Payment.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Payment.


        :param amount: The amount of this Payment.  # noqa: E501
        :type: float
        """

        self._amount = amount

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
        if not isinstance(other, Payment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Payment):
            return True

        return self.to_dict() != other.to_dict()