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


class Sa(object):
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
        'flavour': 'str',
        'modified_on': 'datetime',
        'modified_by': 'str',
        'created_on': 'datetime',
        'created_by': 'str',
        'state': 'str',
        'project': 'str',
        'uri': 'str',
        'tag': 'list[Tag]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'flavour': 'flavour',
        'modified_on': 'modifiedOn',
        'modified_by': 'modifiedBy',
        'created_on': 'createdOn',
        'created_by': 'createdBy',
        'state': 'state',
        'project': 'project',
        'uri': 'uri',
        'tag': 'tag'
    }

    def __init__(self, id=None, name=None, flavour=None, modified_on=None, modified_by=None, created_on=None, created_by=None, state=None, project=None, uri=None, tag=None, local_vars_configuration=None):  # noqa: E501
        """Sa - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._flavour = None
        self._modified_on = None
        self._modified_by = None
        self._created_on = None
        self._created_by = None
        self._state = None
        self._project = None
        self._uri = None
        self._tag = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if flavour is not None:
            self.flavour = flavour
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
        if tag is not None:
            self.tag = tag

    @property
    def id(self):
        """Gets the id of this Sa.  # noqa: E501


        :return: The id of this Sa.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Sa.


        :param id: The id of this Sa.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Sa.  # noqa: E501


        :return: The name of this Sa.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Sa.


        :param name: The name of this Sa.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def flavour(self):
        """Gets the flavour of this Sa.  # noqa: E501


        :return: The flavour of this Sa.  # noqa: E501
        :rtype: str
        """
        return self._flavour

    @flavour.setter
    def flavour(self, flavour):
        """Sets the flavour of this Sa.


        :param flavour: The flavour of this Sa.  # noqa: E501
        :type: str
        """

        self._flavour = flavour

    @property
    def modified_on(self):
        """Gets the modified_on of this Sa.  # noqa: E501


        :return: The modified_on of this Sa.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_on

    @modified_on.setter
    def modified_on(self, modified_on):
        """Sets the modified_on of this Sa.


        :param modified_on: The modified_on of this Sa.  # noqa: E501
        :type: datetime
        """

        self._modified_on = modified_on

    @property
    def modified_by(self):
        """Gets the modified_by of this Sa.  # noqa: E501


        :return: The modified_by of this Sa.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this Sa.


        :param modified_by: The modified_by of this Sa.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def created_on(self):
        """Gets the created_on of this Sa.  # noqa: E501


        :return: The created_on of this Sa.  # noqa: E501
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Sa.


        :param created_on: The created_on of this Sa.  # noqa: E501
        :type: datetime
        """

        self._created_on = created_on

    @property
    def created_by(self):
        """Gets the created_by of this Sa.  # noqa: E501


        :return: The created_by of this Sa.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Sa.


        :param created_by: The created_by of this Sa.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def state(self):
        """Gets the state of this Sa.  # noqa: E501


        :return: The state of this Sa.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Sa.


        :param state: The state of this Sa.  # noqa: E501
        :type: str
        """
        allowed_values = ["Online", "Processing", "NotCreated"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def project(self):
        """Gets the project of this Sa.  # noqa: E501


        :return: The project of this Sa.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Sa.


        :param project: The project of this Sa.  # noqa: E501
        :type: str
        """

        self._project = project

    @property
    def uri(self):
        """Gets the uri of this Sa.  # noqa: E501


        :return: The uri of this Sa.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this Sa.


        :param uri: The uri of this Sa.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def tag(self):
        """Gets the tag of this Sa.  # noqa: E501


        :return: The tag of this Sa.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Sa.


        :param tag: The tag of this Sa.  # noqa: E501
        :type: list[Tag]
        """

        self._tag = tag

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
        if not isinstance(other, Sa):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Sa):
            return True

        return self.to_dict() != other.to_dict()
