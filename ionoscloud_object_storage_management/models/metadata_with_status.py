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


class MetadataWithStatus(object):
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

        'status': 'str',

        'status_message': 'str',

        'administrative': 'bool',
    }

    attribute_map = {

        'created_date': 'createdDate',

        'created_by': 'createdBy',

        'created_by_user_id': 'createdByUserId',

        'last_modified_date': 'lastModifiedDate',

        'last_modified_by': 'lastModifiedBy',

        'last_modified_by_user_id': 'lastModifiedByUserId',

        'resource_urn': 'resourceURN',

        'status': 'status',

        'status_message': 'statusMessage',

        'administrative': 'administrative',
    }

    def __init__(self, created_date=None, created_by=None, created_by_user_id=None, last_modified_date=None, last_modified_by=None, last_modified_by_user_id=None, resource_urn=None, status=None, status_message=None, administrative=None, local_vars_configuration=None):  # noqa: E501
        """MetadataWithStatus - a model defined in OpenAPI"""  # noqa: E501
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
        self._status = None
        self._status_message = None
        self._administrative = None
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
        self.status = status
        if status_message is not None:
            self.status_message = status_message
        if administrative is not None:
            self.administrative = administrative


    @property
    def created_date(self):
        """Gets the created_date of this MetadataWithStatus.  # noqa: E501

        The ISO 8601 creation timestamp.  # noqa: E501

        :return: The created_date of this MetadataWithStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this MetadataWithStatus.

        The ISO 8601 creation timestamp.  # noqa: E501

        :param created_date: The created_date of this MetadataWithStatus.  # noqa: E501
        :type created_date: datetime
        """

        self._created_date = created_date

    @property
    def created_by(self):
        """Gets the created_by of this MetadataWithStatus.  # noqa: E501

        Unique name of the identity that created the resource.  # noqa: E501

        :return: The created_by of this MetadataWithStatus.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this MetadataWithStatus.

        Unique name of the identity that created the resource.  # noqa: E501

        :param created_by: The created_by of this MetadataWithStatus.  # noqa: E501
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this MetadataWithStatus.  # noqa: E501

        Unique id of the identity that created the resource.  # noqa: E501

        :return: The created_by_user_id of this MetadataWithStatus.  # noqa: E501
        :rtype: str
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this MetadataWithStatus.

        Unique id of the identity that created the resource.  # noqa: E501

        :param created_by_user_id: The created_by_user_id of this MetadataWithStatus.  # noqa: E501
        :type created_by_user_id: str
        """

        self._created_by_user_id = created_by_user_id

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this MetadataWithStatus.  # noqa: E501

        The ISO 8601 modified timestamp.  # noqa: E501

        :return: The last_modified_date of this MetadataWithStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this MetadataWithStatus.

        The ISO 8601 modified timestamp.  # noqa: E501

        :param last_modified_date: The last_modified_date of this MetadataWithStatus.  # noqa: E501
        :type last_modified_date: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this MetadataWithStatus.  # noqa: E501

        Unique name of the identity that last modified the resource.  # noqa: E501

        :return: The last_modified_by of this MetadataWithStatus.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this MetadataWithStatus.

        Unique name of the identity that last modified the resource.  # noqa: E501

        :param last_modified_by: The last_modified_by of this MetadataWithStatus.  # noqa: E501
        :type last_modified_by: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_by_user_id(self):
        """Gets the last_modified_by_user_id of this MetadataWithStatus.  # noqa: E501

        Unique id of the identity that last modified the resource.  # noqa: E501

        :return: The last_modified_by_user_id of this MetadataWithStatus.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by_user_id

    @last_modified_by_user_id.setter
    def last_modified_by_user_id(self, last_modified_by_user_id):
        """Sets the last_modified_by_user_id of this MetadataWithStatus.

        Unique id of the identity that last modified the resource.  # noqa: E501

        :param last_modified_by_user_id: The last_modified_by_user_id of this MetadataWithStatus.  # noqa: E501
        :type last_modified_by_user_id: str
        """

        self._last_modified_by_user_id = last_modified_by_user_id

    @property
    def resource_urn(self):
        """Gets the resource_urn of this MetadataWithStatus.  # noqa: E501

        Unique name of the resource.  # noqa: E501

        :return: The resource_urn of this MetadataWithStatus.  # noqa: E501
        :rtype: str
        """
        return self._resource_urn

    @resource_urn.setter
    def resource_urn(self, resource_urn):
        """Sets the resource_urn of this MetadataWithStatus.

        Unique name of the resource.  # noqa: E501

        :param resource_urn: The resource_urn of this MetadataWithStatus.  # noqa: E501
        :type resource_urn: str
        """

        self._resource_urn = resource_urn

    @property
    def status(self):
        """Gets the status of this MetadataWithStatus.  # noqa: E501

        The status of the object. The status can be: * `AVAILABLE` - resource exists and is healthy. * `PROVISIONING` - resource is being created or updated. * `DESTROYING` - delete command was issued, the resource is being deleted. * `FAILED` - resource failed, details in `failureMessage`.   # noqa: E501

        :return: The status of this MetadataWithStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MetadataWithStatus.

        The status of the object. The status can be: * `AVAILABLE` - resource exists and is healthy. * `PROVISIONING` - resource is being created or updated. * `DESTROYING` - delete command was issued, the resource is being deleted. * `FAILED` - resource failed, details in `failureMessage`.   # noqa: E501

        :param status: The status of this MetadataWithStatus.  # noqa: E501
        :type status: str
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["PROVISIONING", "DESTROYING", "AVAILABLE", "FAILED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def status_message(self):
        """Gets the status_message of this MetadataWithStatus.  # noqa: E501

        The message of the failure if the status is `FAILED`.   # noqa: E501

        :return: The status_message of this MetadataWithStatus.  # noqa: E501
        :rtype: str
        """
        return self._status_message

    @status_message.setter
    def status_message(self, status_message):
        """Sets the status_message of this MetadataWithStatus.

        The message of the failure if the status is `FAILED`.   # noqa: E501

        :param status_message: The status_message of this MetadataWithStatus.  # noqa: E501
        :type status_message: str
        """

        self._status_message = status_message

    @property
    def administrative(self):
        """Gets the administrative of this MetadataWithStatus.  # noqa: E501

        Indicates if the key is an administrative key. Administrative keys can create buckets and set bucket policies.   # noqa: E501

        :return: The administrative of this MetadataWithStatus.  # noqa: E501
        :rtype: bool
        """
        return self._administrative

    @administrative.setter
    def administrative(self, administrative):
        """Sets the administrative of this MetadataWithStatus.

        Indicates if the key is an administrative key. Administrative keys can create buckets and set bucket policies.   # noqa: E501

        :param administrative: The administrative of this MetadataWithStatus.  # noqa: E501
        :type administrative: bool
        """

        self._administrative = administrative
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
        if not isinstance(other, MetadataWithStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MetadataWithStatus):
            return True

        return self.to_dict() != other.to_dict()