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


class PlayerTurns(object):
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
        'stars': 'int',
        'mvp': 'bool',
        'territory': 'str',
        'team': 'str'
    }

    attribute_map = {
        'season': 'season',
        'day': 'day',
        'stars': 'stars',
        'mvp': 'mvp',
        'territory': 'territory',
        'team': 'team'
    }

    def __init__(self, season=None, day=None, stars=None, mvp=None, territory=None, team=None, local_vars_configuration=None):  # noqa: E501
        """PlayerTurns - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._season = None
        self._day = None
        self._stars = None
        self._mvp = None
        self._territory = None
        self._team = None
        self.discriminator = None

        if season is not None:
            self.season = season
        if day is not None:
            self.day = day
        if stars is not None:
            self.stars = stars
        if mvp is not None:
            self.mvp = mvp
        if territory is not None:
            self.territory = territory
        if team is not None:
            self.team = team

    @property
    def season(self):
        """Gets the season of this PlayerTurns.  # noqa: E501


        :return: The season of this PlayerTurns.  # noqa: E501
        :rtype: int
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this PlayerTurns.


        :param season: The season of this PlayerTurns.  # noqa: E501
        :type: int
        """

        self._season = season

    @property
    def day(self):
        """Gets the day of this PlayerTurns.  # noqa: E501


        :return: The day of this PlayerTurns.  # noqa: E501
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this PlayerTurns.


        :param day: The day of this PlayerTurns.  # noqa: E501
        :type: int
        """

        self._day = day

    @property
    def stars(self):
        """Gets the stars of this PlayerTurns.  # noqa: E501


        :return: The stars of this PlayerTurns.  # noqa: E501
        :rtype: int
        """
        return self._stars

    @stars.setter
    def stars(self, stars):
        """Sets the stars of this PlayerTurns.


        :param stars: The stars of this PlayerTurns.  # noqa: E501
        :type: int
        """

        self._stars = stars

    @property
    def mvp(self):
        """Gets the mvp of this PlayerTurns.  # noqa: E501


        :return: The mvp of this PlayerTurns.  # noqa: E501
        :rtype: bool
        """
        return self._mvp

    @mvp.setter
    def mvp(self, mvp):
        """Sets the mvp of this PlayerTurns.


        :param mvp: The mvp of this PlayerTurns.  # noqa: E501
        :type: bool
        """

        self._mvp = mvp

    @property
    def territory(self):
        """Gets the territory of this PlayerTurns.  # noqa: E501


        :return: The territory of this PlayerTurns.  # noqa: E501
        :rtype: str
        """
        return self._territory

    @territory.setter
    def territory(self, territory):
        """Sets the territory of this PlayerTurns.


        :param territory: The territory of this PlayerTurns.  # noqa: E501
        :type: str
        """

        self._territory = territory

    @property
    def team(self):
        """Gets the team of this PlayerTurns.  # noqa: E501


        :return: The team of this PlayerTurns.  # noqa: E501
        :rtype: str
        """
        return self._team

    @team.setter
    def team(self, team):
        """Sets the team of this PlayerTurns.


        :param team: The team of this PlayerTurns.  # noqa: E501
        :type: str
        """

        self._team = team

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
        if not isinstance(other, PlayerTurns):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlayerTurns):
            return True

        return self.to_dict() != other.to_dict()
