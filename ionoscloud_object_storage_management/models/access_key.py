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


class AccessKey(object):
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

        'access_key': 'str',

        'secret_key': 'str',

        'canonical_user_id': 'str',

        'contract_user_id': 'str',
    }

    attribute_map = {

        'description': 'description',

        'access_key': 'accessKey',

        'secret_key': 'secretKey',

        'canonical_user_id': 'canonicalUserId',

        'contract_user_id': 'contractUserId',
    }

    def __init__(self, description=None, access_key=None, secret_key=None, canonical_user_id=None, contract_user_id=None, local_vars_configuration=None):  # noqa: E501
        """AccessKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._description = None
        self._access_key = None
        self._secret_key = None
        self._canonical_user_id = None
        self._contract_user_id = None
        self.discriminator = None

        self.description = description
        self.access_key = access_key
        self.secret_key = secret_key
        if canonical_user_id is not None:
            self.canonical_user_id = canonical_user_id
        if contract_user_id is not None:
            self.contract_user_id = contract_user_id


    @property
    def description(self):
        """Gets the description of this AccessKey.  # noqa: E501

        Description of the Access key.  # noqa: E501

        :return: The description of this AccessKey.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AccessKey.

        Description of the Access key.  # noqa: E501

        :param description: The description of this AccessKey.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def access_key(self):
        """Gets the access_key of this AccessKey.  # noqa: E501

        Access key metadata is a string of 92 characters.  # noqa: E501

        :return: The access_key of this AccessKey.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this AccessKey.

        Access key metadata is a string of 92 characters.  # noqa: E501

        :param access_key: The access_key of this AccessKey.  # noqa: E501
        :type access_key: str
        """
        if self.local_vars_configuration.client_side_validation and access_key is None:  # noqa: E501
            raise ValueError("Invalid value for `access_key`, must not be `None`")  # noqa: E501

        self._access_key = access_key

    @property
    def secret_key(self):
        """Gets the secret_key of this AccessKey.  # noqa: E501

        The secret key of the Access key.  # noqa: E501

        :return: The secret_key of this AccessKey.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this AccessKey.

        The secret key of the Access key.  # noqa: E501

        :param secret_key: The secret_key of this AccessKey.  # noqa: E501
        :type secret_key: str
        """
        if self.local_vars_configuration.client_side_validation and secret_key is None:  # noqa: E501
            raise ValueError("Invalid value for `secret_key`, must not be `None`")  # noqa: E501

        self._secret_key = secret_key

    @property
    def canonical_user_id(self):
        """Gets the canonical_user_id of this AccessKey.  # noqa: E501

        The canonical user ID which is valid for user-owned buckets.  # noqa: E501

        :return: The canonical_user_id of this AccessKey.  # noqa: E501
        :rtype: str
        """
        return self._canonical_user_id

    @canonical_user_id.setter
    def canonical_user_id(self, canonical_user_id):
        """Sets the canonical_user_id of this AccessKey.

        The canonical user ID which is valid for user-owned buckets.  # noqa: E501

        :param canonical_user_id: The canonical_user_id of this AccessKey.  # noqa: E501
        :type canonical_user_id: str
        """

        self._canonical_user_id = canonical_user_id

    @property
    def contract_user_id(self):
        """Gets the contract_user_id of this AccessKey.  # noqa: E501

        The contract user ID which is valid for contract-owned buckets.  # noqa: E501

        :return: The contract_user_id of this AccessKey.  # noqa: E501
        :rtype: str
        """
        return self._contract_user_id

    @contract_user_id.setter
    def contract_user_id(self, contract_user_id):
        """Sets the contract_user_id of this AccessKey.

        The contract user ID which is valid for contract-owned buckets.  # noqa: E501

        :param contract_user_id: The contract_user_id of this AccessKey.  # noqa: E501
        :type contract_user_id: str
        """

        self._contract_user_id = contract_user_id
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
        if not isinstance(other, AccessKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessKey):
            return True

        return self.to_dict() != other.to_dict()
