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


class WebsiteProjectInstanceSnapshotDownload(object):
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
        'incremental': 'str'
    }

    attribute_map = {
        'incremental': 'incremental'
    }

    def __init__(self, incremental=None, local_vars_configuration=None):  # noqa: E501
        """WebsiteProjectInstanceSnapshotDownload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._incremental = None
        self.discriminator = None

        if incremental is not None:
            self.incremental = incremental

    @property
    def incremental(self):
        """Gets the incremental of this WebsiteProjectInstanceSnapshotDownload.  # noqa: E501


        :return: The incremental of this WebsiteProjectInstanceSnapshotDownload.  # noqa: E501
        :rtype: str
        """
        return self._incremental

    @incremental.setter
    def incremental(self, incremental):
        """Sets the incremental of this WebsiteProjectInstanceSnapshotDownload.


        :param incremental: The incremental of this WebsiteProjectInstanceSnapshotDownload.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                incremental is not None and not re.search(r'^[\w-]+$', incremental)):  # noqa: E501
            raise ValueError(r"Invalid value for `incremental`, must be a follow pattern or equal to `/^[\w-]+$/`")  # noqa: E501

        self._incremental = incremental

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
        if not isinstance(other, WebsiteProjectInstanceSnapshotDownload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebsiteProjectInstanceSnapshotDownload):
            return True

        return self.to_dict() != other.to_dict()