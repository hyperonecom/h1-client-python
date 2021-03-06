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


class ContainerImage(object):
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
        'digest': 'str',
        'created_on': 'datetime',
        'modified_on': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'digest': 'digest',
        'created_on': 'createdOn',
        'modified_on': 'modifiedOn'
    }

    def __init__(self, id=None, name=None, digest=None, created_on=None, modified_on=None, local_vars_configuration=None):  # noqa: E501
        """ContainerImage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._digest = None
        self._created_on = None
        self._modified_on = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.digest = digest
        self.created_on = created_on
        self.modified_on = modified_on

    @property
    def id(self):
        """Gets the id of this ContainerImage.  # noqa: E501


        :return: The id of this ContainerImage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ContainerImage.


        :param id: The id of this ContainerImage.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ContainerImage.  # noqa: E501


        :return: The name of this ContainerImage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ContainerImage.


        :param name: The name of this ContainerImage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def digest(self):
        """Gets the digest of this ContainerImage.  # noqa: E501


        :return: The digest of this ContainerImage.  # noqa: E501
        :rtype: str
        """
        return self._digest

    @digest.setter
    def digest(self, digest):
        """Sets the digest of this ContainerImage.


        :param digest: The digest of this ContainerImage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and digest is None:  # noqa: E501
            raise ValueError("Invalid value for `digest`, must not be `None`")  # noqa: E501

        self._digest = digest

    @property
    def created_on(self):
        """Gets the created_on of this ContainerImage.  # noqa: E501


        :return: The created_on of this ContainerImage.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ContainerImage.


        :param created_on: The created_on of this ContainerImage.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and created_on is None:  # noqa: E501
            raise ValueError("Invalid value for `created_on`, must not be `None`")  # noqa: E501

        self._created_on = created_on

    @property
    def modified_on(self):
        """Gets the modified_on of this ContainerImage.  # noqa: E501


        :return: The modified_on of this ContainerImage.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_on

    @modified_on.setter
    def modified_on(self, modified_on):
        """Sets the modified_on of this ContainerImage.


        :param modified_on: The modified_on of this ContainerImage.  # noqa: E501
        :type: datetime
        """
        if self.local_vars_configuration.client_side_validation and modified_on is None:  # noqa: E501
            raise ValueError("Invalid value for `modified_on`, must not be `None`")  # noqa: E501

        self._modified_on = modified_on

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
        if not isinstance(other, ContainerImage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ContainerImage):
            return True

        return self.to_dict() != other.to_dict()
