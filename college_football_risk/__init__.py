# coding: utf-8

# flake8: noqa

"""
    College Football Risk API

    Companion API for College Football Risk  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: admin@collegefootballdata.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from college_football_risk.api.players_api import PlayersApi
from college_football_risk.api.stats_api import StatsApi
from college_football_risk.api.teams_api import TeamsApi
from college_football_risk.api.territories_api import TerritoriesApi

# import ApiClient
from college_football_risk.api_client import ApiClient
from college_football_risk.configuration import Configuration
from college_football_risk.exceptions import OpenApiException
from college_football_risk.exceptions import ApiTypeError
from college_football_risk.exceptions import ApiValueError
from college_football_risk.exceptions import ApiKeyError
from college_football_risk.exceptions import ApiException
# import models into sdk package
from college_football_risk.models.leaderboard_team import LeaderboardTeam
from college_football_risk.models.player import Player
from college_football_risk.models.player_ratings import PlayerRatings
from college_football_risk.models.player_stats import PlayerStats
from college_football_risk.models.player_team import PlayerTeam
from college_football_risk.models.player_team_colors import PlayerTeamColors
from college_football_risk.models.player_turns import PlayerTurns
from college_football_risk.models.team import Team
from college_football_risk.models.team_history import TeamHistory
from college_football_risk.models.team_history_star_breakdown import TeamHistoryStarBreakdown
from college_football_risk.models.team_strength import TeamStrength
from college_football_risk.models.territory import Territory
from college_football_risk.models.territory_history import TerritoryHistory
from college_football_risk.models.territory_neighbors import TerritoryNeighbors
from college_football_risk.models.territory_turn import TerritoryTurn
from college_football_risk.models.territory_turn_players import TerritoryTurnPlayers
from college_football_risk.models.territory_turn_teams import TerritoryTurnTeams
from college_football_risk.models.turn import Turn
