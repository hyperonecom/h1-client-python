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


class Proforma(object):
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
        'invoice_no': 'str',
        'seller': 'ProformaSeller',
        'buyer': 'InvoiceBuyer',
        'issue_date': 'datetime',
        'items': 'list[InvoiceItems]',
        'summary': 'str',
        'project': 'str',
        'uri': 'str',
        'array__': 'ProformaArray'
    }

    attribute_map = {
        'id': 'id',
        'invoice_no': 'invoiceNo',
        'seller': 'seller',
        'buyer': 'buyer',
        'issue_date': 'issueDate',
        'items': 'items',
        'summary': 'summary',
        'project': 'project',
        'uri': 'uri',
        'array__': '__array__'
    }

    def __init__(self, id=None, invoice_no=None, seller=None, buyer=None, issue_date=None, items=None, summary=None, project=None, uri=None, array__=None, local_vars_configuration=None):  # noqa: E501
        """Proforma - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._invoice_no = None
        self._seller = None
        self._buyer = None
        self._issue_date = None
        self._items = None
        self._summary = None
        self._project = None
        self._uri = None
        self._array__ = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if invoice_no is not None:
            self.invoice_no = invoice_no
        if seller is not None:
            self.seller = seller
        if buyer is not None:
            self.buyer = buyer
        if issue_date is not None:
            self.issue_date = issue_date
        if items is not None:
            self.items = items
        if summary is not None:
            self.summary = summary
        if project is not None:
            self.project = project
        if uri is not None:
            self.uri = uri
        if array__ is not None:
            self.array__ = array__

    @property
    def id(self):
        """Gets the id of this Proforma.  # noqa: E501


        :return: The id of this Proforma.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Proforma.


        :param id: The id of this Proforma.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def invoice_no(self):
        """Gets the invoice_no of this Proforma.  # noqa: E501


        :return: The invoice_no of this Proforma.  # noqa: E501
        :rtype: str
        """
        return self._invoice_no

    @invoice_no.setter
    def invoice_no(self, invoice_no):
        """Sets the invoice_no of this Proforma.


        :param invoice_no: The invoice_no of this Proforma.  # noqa: E501
        :type: str
        """

        self._invoice_no = invoice_no

    @property
    def seller(self):
        """Gets the seller of this Proforma.  # noqa: E501


        :return: The seller of this Proforma.  # noqa: E501
        :rtype: ProformaSeller
        """
        return self._seller

    @seller.setter
    def seller(self, seller):
        """Sets the seller of this Proforma.


        :param seller: The seller of this Proforma.  # noqa: E501
        :type: ProformaSeller
        """

        self._seller = seller

    @property
    def buyer(self):
        """Gets the buyer of this Proforma.  # noqa: E501


        :return: The buyer of this Proforma.  # noqa: E501
        :rtype: InvoiceBuyer
        """
        return self._buyer

    @buyer.setter
    def buyer(self, buyer):
        """Sets the buyer of this Proforma.


        :param buyer: The buyer of this Proforma.  # noqa: E501
        :type: InvoiceBuyer
        """

        self._buyer = buyer

    @property
    def issue_date(self):
        """Gets the issue_date of this Proforma.  # noqa: E501


        :return: The issue_date of this Proforma.  # noqa: E501
        :rtype: datetime
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this Proforma.


        :param issue_date: The issue_date of this Proforma.  # noqa: E501
        :type: datetime
        """

        self._issue_date = issue_date

    @property
    def items(self):
        """Gets the items of this Proforma.  # noqa: E501


        :return: The items of this Proforma.  # noqa: E501
        :rtype: list[InvoiceItems]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this Proforma.


        :param items: The items of this Proforma.  # noqa: E501
        :type: list[InvoiceItems]
        """

        self._items = items

    @property
    def summary(self):
        """Gets the summary of this Proforma.  # noqa: E501


        :return: The summary of this Proforma.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Proforma.


        :param summary: The summary of this Proforma.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def project(self):
        """Gets the project of this Proforma.  # noqa: E501


        :return: The project of this Proforma.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Proforma.


        :param project: The project of this Proforma.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def uri(self):
        """Gets the uri of this Proforma.  # noqa: E501


        :return: The uri of this Proforma.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Proforma.


        :param uri: The uri of this Proforma.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def array__(self):
        """Gets the array__ of this Proforma.  # noqa: E501


        :return: The array__ of this Proforma.  # noqa: E501
        :rtype: ProformaArray
        """
        return self._array__

    @array__.setter
    def array__(self, array__):
        """Sets the array__ of this Proforma.


        :param array__: The array__ of this Proforma.  # noqa: E501
        :type: ProformaArray
        """

        self._array__ = array__

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
        if not isinstance(other, Proforma):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Proforma):
            return True

        return self.to_dict() != other.to_dict()
