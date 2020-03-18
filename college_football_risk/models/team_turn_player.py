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


class TeamTurnPlayer(object):
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
        'season': 'int',
        'day': 'int',
        'team': 'str',
        'player': 'str',
        'stars': 'int',
        'mvp': 'bool',
        'territory': 'str',
        'regular_team': 'str'
    }

    attribute_map = {
        'season': 'season',
        'day': 'day',
        'team': 'team',
        'player': 'player',
        'stars': 'stars',
        'mvp': 'mvp',
        'territory': 'territory',
        'regular_team': 'regularTeam'
    }

    def __init__(self, season=None, day=None, team=None, player=None, stars=None, mvp=None, territory=None, regular_team=None, local_vars_configuration=None):  # noqa: E501
        """TeamTurnPlayer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._season = None
        self._day = None
        self._team = None
        self._player = None
        self._stars = None
        self._mvp = None
        self._territory = None
        self._regular_team = None
        self.discriminator = None

        if season is not None:
            self.season = season
        if day is not None:
            self.day = day
        if team is not None:
            self.team = team
        if player is not None:
            self.player = player
        if stars is not None:
            self.stars = stars
        if mvp is not None:
            self.mvp = mvp
        if territory is not None:
            self.territory = territory
        if regular_team is not None:
            self.regular_team = regular_team

    @property
    def season(self):
        """Gets the season of this TeamTurnPlayer.  # noqa: E501


        :return: The season of this TeamTurnPlayer.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this TeamTurnPlayer.


        :param season: The season of this TeamTurnPlayer.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def day(self):
        """Gets the day of this TeamTurnPlayer.  # noqa: E501


        :return: The day of this TeamTurnPlayer.  # noqa: E501
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this TeamTurnPlayer.


        :param day: The day of this TeamTurnPlayer.  # noqa: E501
        :type: int
        """

        self._day = day

    @property
    def team(self):
        """Gets the team of this TeamTurnPlayer.  # noqa: E501


        :return: The team of this TeamTurnPlayer.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this TeamTurnPlayer.


        :param team: The team of this TeamTurnPlayer.  # noqa: E501
        :type: str
        """

        self._team = team

    @property
    def player(self):
        """Gets the player of this TeamTurnPlayer.  # noqa: E501


        :return: The player of this TeamTurnPlayer.  # noqa: E501
        :rtype: str
        """
        return self._player

    @player.setter
    def player(self, player):
        """Sets the player of this TeamTurnPlayer.


        :param player: The player of this TeamTurnPlayer.  # noqa: E501
        :type: str
        """

        self._player = player

    @property
    def stars(self):
        """Gets the stars of this TeamTurnPlayer.  # noqa: E501


        :return: The stars of this TeamTurnPlayer.  # noqa: E501
        :rtype: int
        """
        return self._stars

    @stars.setter
    def stars(self, stars):
        """Sets the stars of this TeamTurnPlayer.


        :param stars: The stars of this TeamTurnPlayer.  # noqa: E501
        :type: int
        """

        self._stars = stars

    @property
    def mvp(self):
        """Gets the mvp of this TeamTurnPlayer.  # noqa: E501


        :return: The mvp of this TeamTurnPlayer.  # noqa: E501
        :rtype: bool
        """
        return self._mvp

    @mvp.setter
    def mvp(self, mvp):
        """Sets the mvp of this TeamTurnPlayer.


        :param mvp: The mvp of this TeamTurnPlayer.  # noqa: E501
        :type: bool
        """

        self._mvp = mvp

    @property
    def territory(self):
        """Gets the territory of this TeamTurnPlayer.  # noqa: E501


        :return: The territory of this TeamTurnPlayer.  # noqa: E501
        :rtype: str
        """
        return self._territory

    @territory.setter
    def territory(self, territory):
        """Sets the territory of this TeamTurnPlayer.


        :param territory: The territory of this TeamTurnPlayer.  # noqa: E501
        :type: str
        """

        self._territory = territory

    @property
    def regular_team(self):
        """Gets the regular_team of this TeamTurnPlayer.  # noqa: E501


        :return: The regular_team of this TeamTurnPlayer.  # noqa: E501
        :rtype: str
        """
        return self._regular_team

    @regular_team.setter
    def regular_team(self, regular_team):
        """Sets the regular_team of this TeamTurnPlayer.


        :param regular_team: The regular_team of this TeamTurnPlayer.  # noqa: E501
        :type: str
        """

        self._regular_team = regular_team

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
        if not isinstance(other, TeamTurnPlayer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamTurnPlayer):
            return True

        return self.to_dict() != other.to_dict()
