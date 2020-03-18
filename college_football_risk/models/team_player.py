# coding: utf-8

"""
    College Football Risk API

    Companion API for College Football Risk  # noqa: E501

    The version of the OpenAPI document: 1.2.1
    Contact: admin@collegefootballdata.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from college_football_risk.configuration import Configuration


class TeamPlayer(object):
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
        'turns_played': 'int',
        'mvps': 'int',
        'last_turn': 'TeamPlayerLastTurn'
    }

    attribute_map = {
        'team': 'team',
        'player': 'player',
        'turns_played': 'turnsPlayed',
        'mvps': 'mvps',
        'last_turn': 'lastTurn'
    }

    def __init__(self, team=None, player=None, turns_played=None, mvps=None, last_turn=None, local_vars_configuration=None):  # noqa: E501
        """TeamPlayer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._team = None
        self._player = None
        self._turns_played = None
        self._mvps = None
        self._last_turn = None
        self.discriminator = None

        if team is not None:
            self.team = team
        if player is not None:
            self.player = player
        if turns_played is not None:
            self.turns_played = turns_played
        if mvps is not None:
            self.mvps = mvps
        if last_turn is not None:
            self.last_turn = last_turn

    @property
    def team(self):
        """Gets the team of this TeamPlayer.  # noqa: E501


        :return: The team of this TeamPlayer.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this TeamPlayer.


        :param team: The team of this TeamPlayer.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def player(self):
        """Gets the player of this TeamPlayer.  # noqa: E501


        :return: The player of this TeamPlayer.  # noqa: E501
        :rtype: str
        """
        return self._player

    @player.setter
    def player(self, player):
        """Sets the player of this TeamPlayer.


        :param player: The player of this TeamPlayer.  # noqa: E501
        :type: str
        """

        self._player = player

    @property
    def turns_played(self):
        """Gets the turns_played of this TeamPlayer.  # noqa: E501


        :return: The turns_played of this TeamPlayer.  # noqa: E501
        :rtype: int
        """
        return self._turns_played

    @turns_played.setter
    def turns_played(self, turns_played):
        """Sets the turns_played of this TeamPlayer.


        :param turns_played: The turns_played of this TeamPlayer.  # noqa: E501
        :type: int
        """

        self._turns_played = turns_played

    @property
    def mvps(self):
        """Gets the mvps of this TeamPlayer.  # noqa: E501


        :return: The mvps of this TeamPlayer.  # noqa: E501
        :rtype: int
        """
        return self._mvps

    @mvps.setter
    def mvps(self, mvps):
        """Sets the mvps of this TeamPlayer.


        :param mvps: The mvps of this TeamPlayer.  # noqa: E501
        :type: int
        """

        self._mvps = mvps

    @property
    def last_turn(self):
        """Gets the last_turn of this TeamPlayer.  # noqa: E501


        :return: The last_turn of this TeamPlayer.  # noqa: E501
        :rtype: TeamPlayerLastTurn
        """
        return self._last_turn

    @last_turn.setter
    def last_turn(self, last_turn):
        """Sets the last_turn of this TeamPlayer.


        :param last_turn: The last_turn of this TeamPlayer.  # noqa: E501
        :type: TeamPlayerLastTurn
        """

        self._last_turn = last_turn

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
        if not isinstance(other, TeamPlayer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamPlayer):
            return True

        return self.to_dict() != other.to_dict()
