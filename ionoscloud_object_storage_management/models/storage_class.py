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


class StorageClass(object):
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

        'description': 'str',

        'durability': 'str',

        'availability': 'str',
    }

    attribute_map = {

        'description': 'description',

        'durability': 'durability',

        'availability': 'availability',
    }

    def __init__(self, description=None, durability=None, availability=None, local_vars_configuration=None):  # noqa: E501
        """StorageClass - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._durability = None
        self._availability = None
        self.discriminator = None

        self.description = description
        self.durability = durability
        self.availability = availability


    @property
    def description(self):
        """Gets the description of this StorageClass.  # noqa: E501

        Explains the motivation for the storage class  # noqa: E501

        :return: The description of this StorageClass.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StorageClass.

        Explains the motivation for the storage class  # noqa: E501

        :param description: The description of this StorageClass.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def durability(self):
        """Gets the durability of this StorageClass.  # noqa: E501

        The durability of the storage class  # noqa: E501

        :return: The durability of this StorageClass.  # noqa: E501
        :rtype: str
        """
        return self._durability

    @durability.setter
    def durability(self, durability):
        """Sets the durability of this StorageClass.

        The durability of the storage class  # noqa: E501

        :param durability: The durability of this StorageClass.  # noqa: E501
        :type durability: str
        """
        if self.local_vars_configuration.client_side_validation and durability is None:  # noqa: E501
            raise ValueError("Invalid value for `durability`, must not be `None`")  # noqa: E501

        self._durability = durability

    @property
    def availability(self):
        """Gets the availability of this StorageClass.  # noqa: E501

        The availability of the storage class  # noqa: E501

        :return: The availability of this StorageClass.  # noqa: E501
        :rtype: str
        """
        return self._availability

    @availability.setter
    def availability(self, availability):
        """Sets the availability of this StorageClass.

        The availability of the storage class  # noqa: E501

        :param availability: The availability of this StorageClass.  # noqa: E501
        :type availability: str
        """
        if self.local_vars_configuration.client_side_validation and availability is None:  # noqa: E501
            raise ValueError("Invalid value for `availability`, must not be `None`")  # noqa: E501

        self._availability = availability
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
        if not isinstance(other, StorageClass):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StorageClass):
            return True

        return self.to_dict() != other.to_dict()
