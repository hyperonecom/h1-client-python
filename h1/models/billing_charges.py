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


class BillingCharges(object):
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
        'value': 'float',
        'start': 'str',
        'end': 'str',
        'price': 'float',
        'quantity': 'float',
        'paid_from': 'str',
        'paid_on': 'str'
    }

    attribute_map = {
        'id': 'id',
        'value': 'value',
        'start': 'start',
        'end': 'end',
        'price': 'price',
        'quantity': 'quantity',
        'paid_from': 'paidFrom',
        'paid_on': 'paidOn'
    }

    def __init__(self, id=None, value=None, start=None, end=None, price=None, quantity=None, paid_from=None, paid_on=None, local_vars_configuration=None):  # noqa: E501
        """BillingCharges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._value = None
        self._start = None
        self._end = None
        self._price = None
        self._quantity = None
        self._paid_from = None
        self._paid_on = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if value is not None:
            self.value = value
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if price is not None:
            self.price = price
        if quantity is not None:
            self.quantity = quantity
        if paid_from is not None:
            self.paid_from = paid_from
        if paid_on is not None:
            self.paid_on = paid_on

    @property
    def id(self):
        """Gets the id of this BillingCharges.  # noqa: E501


        :return: The id of this BillingCharges.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BillingCharges.


        :param id: The id of this BillingCharges.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def value(self):
        """Gets the value of this BillingCharges.  # noqa: E501


        :return: The value of this BillingCharges.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BillingCharges.


        :param value: The value of this BillingCharges.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def start(self):
        """Gets the start of this BillingCharges.  # noqa: E501


        :return: The start of this BillingCharges.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this BillingCharges.


        :param start: The start of this BillingCharges.  # noqa: E501
        :type: str
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this BillingCharges.  # noqa: E501


        :return: The end of this BillingCharges.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this BillingCharges.


        :param end: The end of this BillingCharges.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def price(self):
        """Gets the price of this BillingCharges.  # noqa: E501


        :return: The price of this BillingCharges.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this BillingCharges.


        :param price: The price of this BillingCharges.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def quantity(self):
        """Gets the quantity of this BillingCharges.  # noqa: E501


        :return: The quantity of this BillingCharges.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this BillingCharges.


        :param quantity: The quantity of this BillingCharges.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def paid_from(self):
        """Gets the paid_from of this BillingCharges.  # noqa: E501


        :return: The paid_from of this BillingCharges.  # noqa: E501
        :rtype: str
        """
        return self._paid_from

    @paid_from.setter
    def paid_from(self, paid_from):
        """Sets the paid_from of this BillingCharges.


        :param paid_from: The paid_from of this BillingCharges.  # noqa: E501
        :type: str
        """

        self._paid_from = paid_from

    @property
    def paid_on(self):
        """Gets the paid_on of this BillingCharges.  # noqa: E501


        :return: The paid_on of this BillingCharges.  # noqa: E501
        :rtype: str
        """
        return self._paid_on

    @paid_on.setter
    def paid_on(self, paid_on):
        """Sets the paid_on of this BillingCharges.


        :param paid_on: The paid_on of this BillingCharges.  # noqa: E501
        :type: str
        """

        self._paid_on = paid_on

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
        if not isinstance(other, BillingCharges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BillingCharges):
            return True

        return self.to_dict() != other.to_dict()
