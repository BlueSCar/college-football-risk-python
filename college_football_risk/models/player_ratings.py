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


class PlayerRatings(object):
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
        'overall': 'int',
        'total_turns': 'int',
        'game_turns': 'int',
        'mvps': 'int',
        'streak': 'int',
        'awards': 'int'
    }

    attribute_map = {
        'overall': 'overall',
        'total_turns': 'totalTurns',
        'game_turns': 'gameTurns',
        'mvps': 'mvps',
        'streak': 'streak',
        'awards': 'awards'
    }

    def __init__(self, overall=None, total_turns=None, game_turns=None, mvps=None, streak=None, awards=None, local_vars_configuration=None):  # noqa: E501
        """PlayerRatings - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._overall = None
        self._total_turns = None
        self._game_turns = None
        self._mvps = None
        self._streak = None
        self._awards = None
        self.discriminator = None

        if overall is not None:
            self.overall = overall
        if total_turns is not None:
            self.total_turns = total_turns
        if game_turns is not None:
            self.game_turns = game_turns
        if mvps is not None:
            self.mvps = mvps
        if streak is not None:
            self.streak = streak
        if awards is not None:
            self.awards = awards

    @property
    def overall(self):
        """Gets the overall of this PlayerRatings.  # noqa: E501


        :return: The overall of this PlayerRatings.  # noqa: E501
        :rtype: int
        """
        return self._overall

    @overall.setter
    def overall(self, overall):
        """Sets the overall of this PlayerRatings.


        :param overall: The overall of this PlayerRatings.  # noqa: E501
        :type: int
        """

        self._overall = overall

    @property
    def total_turns(self):
        """Gets the total_turns of this PlayerRatings.  # noqa: E501


        :return: The total_turns of this PlayerRatings.  # noqa: E501
        :rtype: int
        """
        return self._total_turns

    @total_turns.setter
    def total_turns(self, total_turns):
        """Sets the total_turns of this PlayerRatings.


        :param total_turns: The total_turns of this PlayerRatings.  # noqa: E501
        :type: int
        """

        self._total_turns = total_turns

    @property
    def game_turns(self):
        """Gets the game_turns of this PlayerRatings.  # noqa: E501


        :return: The game_turns of this PlayerRatings.  # noqa: E501
        :rtype: int
        """
        return self._game_turns

    @game_turns.setter
    def game_turns(self, game_turns):
        """Sets the game_turns of this PlayerRatings.


        :param game_turns: The game_turns of this PlayerRatings.  # noqa: E501
        :type: int
        """

        self._game_turns = game_turns

    @property
    def mvps(self):
        """Gets the mvps of this PlayerRatings.  # noqa: E501


        :return: The mvps of this PlayerRatings.  # noqa: E501
        :rtype: int
        """
        return self._mvps

    @mvps.setter
    def mvps(self, mvps):
        """Sets the mvps of this PlayerRatings.


        :param mvps: The mvps of this PlayerRatings.  # noqa: E501
        :type: int
        """

        self._mvps = mvps

    @property
    def streak(self):
        """Gets the streak of this PlayerRatings.  # noqa: E501


        :return: The streak of this PlayerRatings.  # noqa: E501
        :rtype: int
        """
        return self._streak

    @streak.setter
    def streak(self, streak):
        """Sets the streak of this PlayerRatings.


        :param streak: The streak of this PlayerRatings.  # noqa: E501
        :type: int
        """

        self._streak = streak

    @property
    def awards(self):
        """Gets the awards of this PlayerRatings.  # noqa: E501


        :return: The awards of this PlayerRatings.  # noqa: E501
        :rtype: int
        """
        return self._awards

    @awards.setter
    def awards(self, awards):
        """Sets the awards of this PlayerRatings.


        :param awards: The awards of this PlayerRatings.  # noqa: E501
        :type: int
        """

        self._awards = awards

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
        if not isinstance(other, PlayerRatings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlayerRatings):
            return True

        return self.to_dict() != other.to_dict()
