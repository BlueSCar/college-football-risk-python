# coding: utf-8

"""
    College Football Risk API

    Companion API for College Football Risk  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Contact: admin@collegefootballdata.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from college_football_risk.configuration import Configuration


class TerritoryTurnPlayers(object):
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
        'team': 'str',
        'player': 'str',
        'stars': 'int',
        'weight': 'int',
        'multiplier': 'float',
        'mvp': 'bool',
        'power': 'float'
    }

    attribute_map = {
        'team': 'team',
        'player': 'player',
        'stars': 'stars',
        'weight': 'weight',
        'multiplier': 'multiplier',
        'mvp': 'mvp',
        'power': 'power'
    }

    def __init__(self, team=None, player=None, stars=None, weight=None, multiplier=None, mvp=None, power=None, local_vars_configuration=None):  # noqa: E501
        """TerritoryTurnPlayers - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._team = None
        self._player = None
        self._stars = None
        self._weight = None
        self._multiplier = None
        self._mvp = None
        self._power = None
        self.discriminator = None

        if team is not None:
            self.team = team
        if player is not None:
            self.player = player
        if stars is not None:
            self.stars = stars
        if weight is not None:
            self.weight = weight
        if multiplier is not None:
            self.multiplier = multiplier
        if mvp is not None:
            self.mvp = mvp
        if power is not None:
            self.power = power

    @property
    def team(self):
        """Gets the team of this TerritoryTurnPlayers.  # noqa: E501


        :return: The team of this TerritoryTurnPlayers.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this TerritoryTurnPlayers.


        :param team: The team of this TerritoryTurnPlayers.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def player(self):
        """Gets the player of this TerritoryTurnPlayers.  # noqa: E501


        :return: The player of this TerritoryTurnPlayers.  # noqa: E501
        :rtype: str
        """
        return self._player

    @player.setter
    def player(self, player):
        """Sets the player of this TerritoryTurnPlayers.


        :param player: The player of this TerritoryTurnPlayers.  # noqa: E501
        :type: str
        """

        self._player = player

    @property
    def stars(self):
        """Gets the stars of this TerritoryTurnPlayers.  # noqa: E501


        :return: The stars of this TerritoryTurnPlayers.  # noqa: E501
        :rtype: int
        """
        return self._stars

    @stars.setter
    def stars(self, stars):
        """Sets the stars of this TerritoryTurnPlayers.


        :param stars: The stars of this TerritoryTurnPlayers.  # noqa: E501
        :type: int
        """

        self._stars = stars

    @property
    def weight(self):
        """Gets the weight of this TerritoryTurnPlayers.  # noqa: E501


        :return: The weight of this TerritoryTurnPlayers.  # noqa: E501
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this TerritoryTurnPlayers.


        :param weight: The weight of this TerritoryTurnPlayers.  # noqa: E501
        :type: int
        """

        self._weight = weight

    @property
    def multiplier(self):
        """Gets the multiplier of this TerritoryTurnPlayers.  # noqa: E501


        :return: The multiplier of this TerritoryTurnPlayers.  # noqa: E501
        :rtype: float
        """
        return self._multiplier

    @multiplier.setter
    def multiplier(self, multiplier):
        """Sets the multiplier of this TerritoryTurnPlayers.


        :param multiplier: The multiplier of this TerritoryTurnPlayers.  # noqa: E501
        :type: float
        """

        self._multiplier = multiplier

    @property
    def mvp(self):
        """Gets the mvp of this TerritoryTurnPlayers.  # noqa: E501


        :return: The mvp of this TerritoryTurnPlayers.  # noqa: E501
        :rtype: bool
        """
        return self._mvp

    @mvp.setter
    def mvp(self, mvp):
        """Sets the mvp of this TerritoryTurnPlayers.


        :param mvp: The mvp of this TerritoryTurnPlayers.  # noqa: E501
        :type: bool
        """

        self._mvp = mvp

    @property
    def power(self):
        """Gets the power of this TerritoryTurnPlayers.  # noqa: E501


        :return: The power of this TerritoryTurnPlayers.  # noqa: E501
        :rtype: float
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this TerritoryTurnPlayers.


        :param power: The power of this TerritoryTurnPlayers.  # noqa: E501
        :type: float
        """

        self._power = power

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
        if not isinstance(other, TerritoryTurnPlayers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TerritoryTurnPlayers):
            return True

        return self.to_dict() != other.to_dict()
