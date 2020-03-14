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


class TeamHistory(object):
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
        'sequence': 'int',
        'season': 'int',
        'day': 'int',
        'players': 'int',
        'territories': 'int',
        'star_power': 'int',
        'effective_power': 'int',
        'star_breakdown': 'TeamHistoryStarBreakdown'
    }

    attribute_map = {
        'sequence': 'sequence',
        'season': 'season',
        'day': 'day',
        'players': 'players',
        'territories': 'territories',
        'star_power': 'starPower',
        'effective_power': 'effectivePower',
        'star_breakdown': 'starBreakdown'
    }

    def __init__(self, sequence=None, season=None, day=None, players=None, territories=None, star_power=None, effective_power=None, star_breakdown=None, local_vars_configuration=None):  # noqa: E501
        """TeamHistory - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._sequence = None
        self._season = None
        self._day = None
        self._players = None
        self._territories = None
        self._star_power = None
        self._effective_power = None
        self._star_breakdown = None
        self.discriminator = None

        if sequence is not None:
            self.sequence = sequence
        if season is not None:
            self.season = season
        if day is not None:
            self.day = day
        if players is not None:
            self.players = players
        if territories is not None:
            self.territories = territories
        if star_power is not None:
            self.star_power = star_power
        if effective_power is not None:
            self.effective_power = effective_power
        if star_breakdown is not None:
            self.star_breakdown = star_breakdown

    @property
    def sequence(self):
        """Gets the sequence of this TeamHistory.  # noqa: E501


        :return: The sequence of this TeamHistory.  # noqa: E501
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this TeamHistory.


        :param sequence: The sequence of this TeamHistory.  # noqa: E501
        :type: int
        """

        self._sequence = sequence

    @property
    def season(self):
        """Gets the season of this TeamHistory.  # noqa: E501


        :return: The season of this TeamHistory.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this TeamHistory.


        :param season: The season of this TeamHistory.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def day(self):
        """Gets the day of this TeamHistory.  # noqa: E501


        :return: The day of this TeamHistory.  # noqa: E501
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this TeamHistory.


        :param day: The day of this TeamHistory.  # noqa: E501
        :type: int
        """

        self._day = day

    @property
    def players(self):
        """Gets the players of this TeamHistory.  # noqa: E501


        :return: The players of this TeamHistory.  # noqa: E501
        :rtype: int
        """
        return self._players

    @players.setter
    def players(self, players):
        """Sets the players of this TeamHistory.


        :param players: The players of this TeamHistory.  # noqa: E501
        :type: int
        """

        self._players = players

    @property
    def territories(self):
        """Gets the territories of this TeamHistory.  # noqa: E501


        :return: The territories of this TeamHistory.  # noqa: E501
        :rtype: int
        """
        return self._territories

    @territories.setter
    def territories(self, territories):
        """Sets the territories of this TeamHistory.


        :param territories: The territories of this TeamHistory.  # noqa: E501
        :type: int
        """

        self._territories = territories

    @property
    def star_power(self):
        """Gets the star_power of this TeamHistory.  # noqa: E501


        :return: The star_power of this TeamHistory.  # noqa: E501
        :rtype: int
        """
        return self._star_power

    @star_power.setter
    def star_power(self, star_power):
        """Sets the star_power of this TeamHistory.


        :param star_power: The star_power of this TeamHistory.  # noqa: E501
        :type: int
        """

        self._star_power = star_power

    @property
    def effective_power(self):
        """Gets the effective_power of this TeamHistory.  # noqa: E501


        :return: The effective_power of this TeamHistory.  # noqa: E501
        :rtype: int
        """
        return self._effective_power

    @effective_power.setter
    def effective_power(self, effective_power):
        """Sets the effective_power of this TeamHistory.


        :param effective_power: The effective_power of this TeamHistory.  # noqa: E501
        :type: int
        """

        self._effective_power = effective_power

    @property
    def star_breakdown(self):
        """Gets the star_breakdown of this TeamHistory.  # noqa: E501


        :return: The star_breakdown of this TeamHistory.  # noqa: E501
        :rtype: TeamHistoryStarBreakdown
        """
        return self._star_breakdown

    @star_breakdown.setter
    def star_breakdown(self, star_breakdown):
        """Sets the star_breakdown of this TeamHistory.


        :param star_breakdown: The star_breakdown of this TeamHistory.  # noqa: E501
        :type: TeamHistoryStarBreakdown
        """

        self._star_breakdown = star_breakdown

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
        if not isinstance(other, TeamHistory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TeamHistory):
            return True

        return self.to_dict() != other.to_dict()
