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


class ComputeProjectVmCreate(object):
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
        'name': 'str',
        'service': 'str',
        'image': 'str',
        'iso': 'str',
        'username': 'str',
        'user_metadata': 'str',
        'start': 'bool',
        'credential': 'list[ComputeProjectVmCreateCredential]',
        'disk': 'list[ComputeProjectVmCreateDisk]',
        'netadp': 'list[ComputeProjectVmCreateNetadp]',
        'tag': 'list[Tag]'
    }

    attribute_map = {
        'name': 'name',
        'service': 'service',
        'image': 'image',
        'iso': 'iso',
        'username': 'username',
        'user_metadata': 'userMetadata',
        'start': 'start',
        'credential': 'credential',
        'disk': 'disk',
        'netadp': 'netadp',
        'tag': 'tag'
    }

    def __init__(self, name=None, service=None, image=None, iso=None, username=None, user_metadata=None, start=True, credential=None, disk=None, netadp=None, tag=None, local_vars_configuration=None):  # noqa: E501
        """ComputeProjectVmCreate - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._service = None
        self._image = None
        self._iso = None
        self._username = None
        self._user_metadata = None
        self._start = None
        self._credential = None
        self._disk = None
        self._netadp = None
        self._tag = None
        self.discriminator = None

        self.name = name
        self.service = service
        if image is not None:
            self.image = image
        if iso is not None:
            self.iso = iso
        if username is not None:
            self.username = username
        if user_metadata is not None:
            self.user_metadata = user_metadata
        if start is not None:
            self.start = start
        if credential is not None:
            self.credential = credential
        if disk is not None:
            self.disk = disk
        if netadp is not None:
            self.netadp = netadp
        if tag is not None:
            self.tag = tag

    @property
    def name(self):
        """Gets the name of this ComputeProjectVmCreate.  # noqa: E501


        :return: The name of this ComputeProjectVmCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComputeProjectVmCreate.


        :param name: The name of this ComputeProjectVmCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def service(self):
        """Gets the service of this ComputeProjectVmCreate.  # noqa: E501


        :return: The service of this ComputeProjectVmCreate.  # noqa: E501
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this ComputeProjectVmCreate.


        :param service: The service of this ComputeProjectVmCreate.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and service is None:  # noqa: E501
            raise ValueError("Invalid value for `service`, must not be `None`")  # noqa: E501

        self._service = service

    @property
    def image(self):
        """Gets the image of this ComputeProjectVmCreate.  # noqa: E501


        :return: The image of this ComputeProjectVmCreate.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ComputeProjectVmCreate.


        :param image: The image of this ComputeProjectVmCreate.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def iso(self):
        """Gets the iso of this ComputeProjectVmCreate.  # noqa: E501


        :return: The iso of this ComputeProjectVmCreate.  # noqa: E501
        :rtype: str
        """
        return self._iso

    @iso.setter
    def iso(self, iso):
        """Sets the iso of this ComputeProjectVmCreate.


        :param iso: The iso of this ComputeProjectVmCreate.  # noqa: E501
        :type: str
        """

        self._iso = iso

    @property
    def username(self):
        """Gets the username of this ComputeProjectVmCreate.  # noqa: E501


        :return: The username of this ComputeProjectVmCreate.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ComputeProjectVmCreate.


        :param username: The username of this ComputeProjectVmCreate.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def user_metadata(self):
        """Gets the user_metadata of this ComputeProjectVmCreate.  # noqa: E501


        :return: The user_metadata of this ComputeProjectVmCreate.  # noqa: E501
        :rtype: str
        """
        return self._user_metadata

    @user_metadata.setter
    def user_metadata(self, user_metadata):
        """Sets the user_metadata of this ComputeProjectVmCreate.


        :param user_metadata: The user_metadata of this ComputeProjectVmCreate.  # noqa: E501
        :type: str
        """

        self._user_metadata = user_metadata

    @property
    def start(self):
        """Gets the start of this ComputeProjectVmCreate.  # noqa: E501


        :return: The start of this ComputeProjectVmCreate.  # noqa: E501
        :rtype: bool
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ComputeProjectVmCreate.


        :param start: The start of this ComputeProjectVmCreate.  # noqa: E501
        :type: bool
        """

        self._start = start

    @property
    def credential(self):
        """Gets the credential of this ComputeProjectVmCreate.  # noqa: E501


        :return: The credential of this ComputeProjectVmCreate.  # noqa: E501
        :rtype: list[ComputeProjectVmCreateCredential]
        """
        return self._credential

    @credential.setter
    def credential(self, credential):
        """Sets the credential of this ComputeProjectVmCreate.


        :param credential: The credential of this ComputeProjectVmCreate.  # noqa: E501
        :type: list[ComputeProjectVmCreateCredential]
        """

        self._credential = credential

    @property
    def disk(self):
        """Gets the disk of this ComputeProjectVmCreate.  # noqa: E501


        :return: The disk of this ComputeProjectVmCreate.  # noqa: E501
        :rtype: list[ComputeProjectVmCreateDisk]
        """
        return self._disk

    @disk.setter
    def disk(self, disk):
        """Sets the disk of this ComputeProjectVmCreate.


        :param disk: The disk of this ComputeProjectVmCreate.  # noqa: E501
        :type: list[ComputeProjectVmCreateDisk]
        """

        self._disk = disk

    @property
    def netadp(self):
        """Gets the netadp of this ComputeProjectVmCreate.  # noqa: E501


        :return: The netadp of this ComputeProjectVmCreate.  # noqa: E501
        :rtype: list[ComputeProjectVmCreateNetadp]
        """
        return self._netadp

    @netadp.setter
    def netadp(self, netadp):
        """Sets the netadp of this ComputeProjectVmCreate.


        :param netadp: The netadp of this ComputeProjectVmCreate.  # noqa: E501
        :type: list[ComputeProjectVmCreateNetadp]
        """

        self._netadp = netadp

    @property
    def tag(self):
        """Gets the tag of this ComputeProjectVmCreate.  # noqa: E501


        :return: The tag of this ComputeProjectVmCreate.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ComputeProjectVmCreate.


        :param tag: The tag of this ComputeProjectVmCreate.  # noqa: E501
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
        if not isinstance(other, ComputeProjectVmCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComputeProjectVmCreate):
            return True

        return self.to_dict() != other.to_dict()