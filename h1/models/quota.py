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


class Quota(object):
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
        'metric': 'QuotaMetric',
        'usage': 'float',
        'limit': 'QuotaLimit'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'metric': 'metric',
        'usage': 'usage',
        'limit': 'limit'
    }

    def __init__(self, id=None, name=None, metric=None, usage=None, limit=None, local_vars_configuration=None):  # noqa: E501
        """Quota - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._metric = None
        self._usage = None
        self._limit = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if metric is not None:
            self.metric = metric
        if usage is not None:
            self.usage = usage
        if limit is not None:
            self.limit = limit

    @property
    def id(self):
        """Gets the id of this Quota.  # noqa: E501


        :return: The id of this Quota.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Quota.


        :param id: The id of this Quota.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Quota.  # noqa: E501


        :return: The name of this Quota.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Quota.


        :param name: The name of this Quota.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def metric(self):
        """Gets the metric of this Quota.  # noqa: E501


        :return: The metric of this Quota.  # noqa: E501
        :rtype: QuotaMetric
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this Quota.


        :param metric: The metric of this Quota.  # noqa: E501
        :type: QuotaMetric
        """

        self._metric = metric

    @property
    def usage(self):
        """Gets the usage of this Quota.  # noqa: E501


        :return: The usage of this Quota.  # noqa: E501
        :rtype: float
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this Quota.


        :param usage: The usage of this Quota.  # noqa: E501
        :type: float
        """

        self._usage = usage

    @property
    def limit(self):
        """Gets the limit of this Quota.  # noqa: E501


        :return: The limit of this Quota.  # noqa: E501
        :rtype: QuotaLimit
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this Quota.


        :param limit: The limit of this Quota.  # noqa: E501
        :type: QuotaLimit
        """

        self._limit = limit

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
        if not isinstance(other, Quota):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Quota):
            return True

        return self.to_dict() != other.to_dict()
