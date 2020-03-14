# coding: utf-8

"""
    College Football Risk API

    Companion API for College Football Risk  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: admin@collegefootballdata.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from college_football_risk.configuration import Configuration


class TerritoryTurnTeams(object):
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
        'color': 'str',
        'secondary_color': 'str',
        'players': 'int',
        'power': 'int',
        'chance': 'float',
        'breakdown': 'TeamHistoryStarBreakdown'
    }

    attribute_map = {
        'team': 'team',
        'color': 'color',
        'secondary_color': 'secondaryColor',
        'players': 'players',
        'power': 'power',
        'chance': 'chance',
        'breakdown': 'breakdown'
    }

    def __init__(self, team=None, color=None, secondary_color=None, players=None, power=None, chance=None, breakdown=None, local_vars_configuration=None):  # noqa: E501
        """TerritoryTurnTeams - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._team = None
        self._color = None
        self._secondary_color = None
        self._players = None
        self._power = None
        self._chance = None
        self._breakdown = None
        self.discriminator = None

        if team is not None:
            self.team = team
        if color is not None:
            self.color = color
        if secondary_color is not None:
            self.secondary_color = secondary_color
        if players is not None:
            self.players = players
        if power is not None:
            self.power = power
        if chance is not None:
            self.chance = chance
        if breakdown is not None:
            self.breakdown = breakdown

    @property
    def team(self):
        """Gets the team of this TerritoryTurnTeams.  # noqa: E501


        :return: The team of this TerritoryTurnTeams.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this TerritoryTurnTeams.


        :param team: The team of this TerritoryTurnTeams.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def color(self):
        """Gets the color of this TerritoryTurnTeams.  # noqa: E501


        :return: The color of this TerritoryTurnTeams.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this TerritoryTurnTeams.


        :param color: The color of this TerritoryTurnTeams.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def secondary_color(self):
        """Gets the secondary_color of this TerritoryTurnTeams.  # noqa: E501


        :return: The secondary_color of this TerritoryTurnTeams.  # noqa: E501
        :rtype: str
        """
        return self._secondary_color

    @secondary_color.setter
    def secondary_color(self, secondary_color):
        """Sets the secondary_color of this TerritoryTurnTeams.


        :param secondary_color: The secondary_color of this TerritoryTurnTeams.  # noqa: E501
        :type: str
        """

        self._secondary_color = secondary_color

    @property
    def players(self):
        """Gets the players of this TerritoryTurnTeams.  # noqa: E501


        :return: The players of this TerritoryTurnTeams.  # noqa: E501
        :rtype: int
        """
        return self._players

    @players.setter
    def players(self, players):
        """Sets the players of this TerritoryTurnTeams.


        :param players: The players of this TerritoryTurnTeams.  # noqa: E501
        :type: int
        """

        self._players = players

    @property
    def power(self):
        """Gets the power of this TerritoryTurnTeams.  # noqa: E501


        :return: The power of this TerritoryTurnTeams.  # noqa: E501
        :rtype: int
        """
        return self._power

    @power.setter
    def power(self, power):
        """Sets the power of this TerritoryTurnTeams.


        :param power: The power of this TerritoryTurnTeams.  # noqa: E501
        :type: int
        """

        self._power = power

    @property
    def chance(self):
        """Gets the chance of this TerritoryTurnTeams.  # noqa: E501


        :return: The chance of this TerritoryTurnTeams.  # noqa: E501
        :rtype: float
        """
        return self._chance

    @chance.setter
    def chance(self, chance):
        """Sets the chance of this TerritoryTurnTeams.


        :param chance: The chance of this TerritoryTurnTeams.  # noqa: E501
        :type: float
        """

        self._chance = chance

    @property
    def breakdown(self):
        """Gets the breakdown of this TerritoryTurnTeams.  # noqa: E501


        :return: The breakdown of this TerritoryTurnTeams.  # noqa: E501
        :rtype: TeamHistoryStarBreakdown
        """
        return self._breakdown

    @breakdown.setter
    def breakdown(self, breakdown):
        """Sets the breakdown of this TerritoryTurnTeams.


        :param breakdown: The breakdown of this TerritoryTurnTeams.  # noqa: E501
        :type: TeamHistoryStarBreakdown
        """

        self._breakdown = breakdown

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
        if not isinstance(other, TerritoryTurnTeams):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TerritoryTurnTeams):
            return True

        return self.to_dict() != other.to_dict()