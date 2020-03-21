# coding: utf-8

"""
    College Football Risk API

    Companion API for College Football Risk  # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: admin@collegefootballdata.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from college_football_risk.configuration import Configuration


class PlayerTeamColors(object):
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
        'primary': 'str',
        'secondary': 'str'
    }

    attribute_map = {
        'primary': 'primary',
        'secondary': 'secondary'
    }

    def __init__(self, primary=None, secondary=None, local_vars_configuration=None):  # noqa: E501
        """PlayerTeamColors - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._primary = None
        self._secondary = None
        self.discriminator = None

        if primary is not None:
            self.primary = primary
        if secondary is not None:
            self.secondary = secondary

    @property
    def primary(self):
        """Gets the primary of this PlayerTeamColors.  # noqa: E501


        :return: The primary of this PlayerTeamColors.  # noqa: E501
        :rtype: str
        """
        return self._primary

    @primary.setter
    def primary(self, primary):
        """Sets the primary of this PlayerTeamColors.


        :param primary: The primary of this PlayerTeamColors.  # noqa: E501
        :type: str
        """

        self._primary = primary

    @property
    def secondary(self):
        """Gets the secondary of this PlayerTeamColors.  # noqa: E501


        :return: The secondary of this PlayerTeamColors.  # noqa: E501
        :rtype: str
        """
        return self._secondary

    @secondary.setter
    def secondary(self, secondary):
        """Sets the secondary of this PlayerTeamColors.


        :param secondary: The secondary of this PlayerTeamColors.  # noqa: E501
        :type: str
        """

        self._secondary = secondary

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
        if not isinstance(other, PlayerTeamColors):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlayerTeamColors):
            return True

        return self.to_dict() != other.to_dict()
