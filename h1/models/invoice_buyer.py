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


class InvoiceBuyer(object):
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
        'company': 'str',
        'address': 'InvoiceBuyerAddress',
        'nip': 'str',
        'email': 'str'
    }

    attribute_map = {
        'company': 'company',
        'address': 'address',
        'nip': 'nip',
        'email': 'email'
    }

    def __init__(self, company=None, address=None, nip=None, email=None, local_vars_configuration=None):  # noqa: E501
        """InvoiceBuyer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._company = None
        self._address = None
        self._nip = None
        self._email = None
        self.discriminator = None

        self.company = company
        if address is not None:
            self.address = address
        if nip is not None:
            self.nip = nip
        if email is not None:
            self.email = email

    @property
    def company(self):
        """Gets the company of this InvoiceBuyer.  # noqa: E501


        :return: The company of this InvoiceBuyer.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this InvoiceBuyer.


        :param company: The company of this InvoiceBuyer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and company is None:  # noqa: E501
            raise ValueError("Invalid value for `company`, must not be `None`")  # noqa: E501

        self._company = company

    @property
    def address(self):
        """Gets the address of this InvoiceBuyer.  # noqa: E501


        :return: The address of this InvoiceBuyer.  # noqa: E501
        :rtype: InvoiceBuyerAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this InvoiceBuyer.


        :param address: The address of this InvoiceBuyer.  # noqa: E501
        :type: InvoiceBuyerAddress
        """

        self._address = address

    @property
    def nip(self):
        """Gets the nip of this InvoiceBuyer.  # noqa: E501


        :return: The nip of this InvoiceBuyer.  # noqa: E501
        :rtype: str
        """
        return self._nip

    @nip.setter
    def nip(self, nip):
        """Sets the nip of this InvoiceBuyer.


        :param nip: The nip of this InvoiceBuyer.  # noqa: E501
        :type: str
        """

        self._nip = nip

    @property
    def email(self):
        """Gets the email of this InvoiceBuyer.  # noqa: E501


        :return: The email of this InvoiceBuyer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InvoiceBuyer.


        :param email: The email of this InvoiceBuyer.  # noqa: E501
        :type: str
        """

        self._email = email

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
        if not isinstance(other, InvoiceBuyer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InvoiceBuyer):
            return True

        return self.to_dict() != other.to_dict()
