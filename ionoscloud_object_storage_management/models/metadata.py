# coding: utf-8

"""
    IONOS Cloud - Object Storage Management API

    Object Storage Management API is a RESTful API that manages the object storage service configuration for IONOS Cloud.   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ionoscloud_object_storage_management.configuration import Configuration


class Metadata(object):
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

        'created_date': 'datetime',

        'created_by': 'str',

        'created_by_user_id': 'str',

        'last_modified_date': 'datetime',

        'last_modified_by': 'str',

        'last_modified_by_user_id': 'str',

        'resource_urn': 'str',
    }

    attribute_map = {

        'created_date': 'createdDate',

        'created_by': 'createdBy',

        'created_by_user_id': 'createdByUserId',

        'last_modified_date': 'lastModifiedDate',

        'last_modified_by': 'lastModifiedBy',

        'last_modified_by_user_id': 'lastModifiedByUserId',

        'resource_urn': 'resourceURN',
    }

    def __init__(self, created_date=None, created_by=None, created_by_user_id=None, last_modified_date=None, last_modified_by=None, last_modified_by_user_id=None, resource_urn=None, local_vars_configuration=None):  # noqa: E501
        """Metadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._created_date = None
        self._created_by = None
        self._created_by_user_id = None
        self._last_modified_date = None
        self._last_modified_by = None
        self._last_modified_by_user_id = None
        self._resource_urn = None
        self.discriminator = None

        if created_date is not None:
            self.created_date = created_date
        if created_by is not None:
            self.created_by = created_by
        if created_by_user_id is not None:
            self.created_by_user_id = created_by_user_id
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if last_modified_by_user_id is not None:
            self.last_modified_by_user_id = last_modified_by_user_id
        if resource_urn is not None:
            self.resource_urn = resource_urn


    @property
    def created_date(self):
        """Gets the created_date of this Metadata.  # noqa: E501

        The ISO 8601 creation timestamp.  # noqa: E501

        :return: The created_date of this Metadata.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this Metadata.

        The ISO 8601 creation timestamp.  # noqa: E501

        :param created_date: The created_date of this Metadata.  # noqa: E501
        :type created_date: datetime
        """

        self._created_date = created_date

    @property
    def created_by(self):
        """Gets the created_by of this Metadata.  # noqa: E501

        Unique name of the identity that created the resource.  # noqa: E501

        :return: The created_by of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Metadata.

        Unique name of the identity that created the resource.  # noqa: E501

        :param created_by: The created_by of this Metadata.  # noqa: E501
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this Metadata.  # noqa: E501

        Unique id of the identity that created the resource.  # noqa: E501

        :return: The created_by_user_id of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this Metadata.

        Unique id of the identity that created the resource.  # noqa: E501

        :param created_by_user_id: The created_by_user_id of this Metadata.  # noqa: E501
        :type created_by_user_id: str
        """

        self._created_by_user_id = created_by_user_id

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this Metadata.  # noqa: E501

        The ISO 8601 modified timestamp.  # noqa: E501

        :return: The last_modified_date of this Metadata.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this Metadata.

        The ISO 8601 modified timestamp.  # noqa: E501

        :param last_modified_date: The last_modified_date of this Metadata.  # noqa: E501
        :type last_modified_date: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this Metadata.  # noqa: E501

        Unique name of the identity that last modified the resource.  # noqa: E501

        :return: The last_modified_by of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this Metadata.

        Unique name of the identity that last modified the resource.  # noqa: E501

        :param last_modified_by: The last_modified_by of this Metadata.  # noqa: E501
        :type last_modified_by: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_by_user_id(self):
        """Gets the last_modified_by_user_id of this Metadata.  # noqa: E501

        Unique id of the identity that last modified the resource.  # noqa: E501

        :return: The last_modified_by_user_id of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by_user_id

    @last_modified_by_user_id.setter
    def last_modified_by_user_id(self, last_modified_by_user_id):
        """Sets the last_modified_by_user_id of this Metadata.

        Unique id of the identity that last modified the resource.  # noqa: E501

        :param last_modified_by_user_id: The last_modified_by_user_id of this Metadata.  # noqa: E501
        :type last_modified_by_user_id: str
        """

        self._last_modified_by_user_id = last_modified_by_user_id

    @property
    def resource_urn(self):
        """Gets the resource_urn of this Metadata.  # noqa: E501

        Unique name of the resource.  # noqa: E501

        :return: The resource_urn of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._resource_urn

    @resource_urn.setter
    def resource_urn(self, resource_urn):
        """Sets the resource_urn of this Metadata.

        Unique name of the resource.  # noqa: E501

        :param resource_urn: The resource_urn of this Metadata.  # noqa: E501
        :type resource_urn: str
        """

        self._resource_urn = resource_urn
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
        if not isinstance(other, Metadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Metadata):
            return True

        return self.to_dict() != other.to_dict()
