# coding: utf-8

"""
    College Football Risk API

    Companion API for College Football Risk  # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: admin@collegefootballdata.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from college_football_risk.api_client import ApiClient
from college_football_risk.exceptions import (
    ApiTypeError,
    ApiValueError
)


class TeamsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_player_moves_by_turn(self, season, day, **kwargs):  # noqa: E501
        """Get players moves by turn  # noqa: E501

        Get player moves by turn  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_moves_by_turn(season, day, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int season: Season filter (required)
        :param int day: Day filter (required)
        :param str team: Team name filter
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[TeamTurnPlayer]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_player_moves_by_turn_with_http_info(season, day, **kwargs)  # noqa: E501

    def get_player_moves_by_turn_with_http_info(self, season, day, **kwargs):  # noqa: E501
        """Get players moves by turn  # noqa: E501

        Get player moves by turn  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_moves_by_turn_with_http_info(season, day, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int season: Season filter (required)
        :param int day: Day filter (required)
        :param str team: Team name filter
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[TeamTurnPlayer], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['season', 'day', 'team']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player_moves_by_turn" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'season' is set
        if self.api_client.client_side_validation and ('season' not in local_var_params or  # noqa: E501
                                                        local_var_params['season'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `season` when calling `get_player_moves_by_turn`")  # noqa: E501
        # verify the required parameter 'day' is set
        if self.api_client.client_side_validation and ('day' not in local_var_params or  # noqa: E501
                                                        local_var_params['day'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `day` when calling `get_player_moves_by_turn`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'season' in local_var_params and local_var_params['season'] is not None:  # noqa: E501
            query_params.append(('season', local_var_params['season']))  # noqa: E501
        if 'day' in local_var_params and local_var_params['day'] is not None:  # noqa: E501
            query_params.append(('day', local_var_params['day']))  # noqa: E501
        if 'team' in local_var_params and local_var_params['team'] is not None:  # noqa: E501
            query_params.append(('team', local_var_params['team']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/team/players', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TeamTurnPlayer]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_team_history(self, team, **kwargs):  # noqa: E501
        """Get historical team stats  # noqa: E501

        Historical team statistics  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_history(team, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str team: Team name (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[TeamHistory]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_team_history_with_http_info(team, **kwargs)  # noqa: E501

    def get_team_history_with_http_info(self, team, **kwargs):  # noqa: E501
        """Get historical team stats  # noqa: E501

        Historical team statistics  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_history_with_http_info(team, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str team: Team name (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[TeamHistory], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['team']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_history" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'team' is set
        if self.api_client.client_side_validation and ('team' not in local_var_params or  # noqa: E501
                                                        local_var_params['team'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `team` when calling `get_team_history`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'team' in local_var_params and local_var_params['team'] is not None:  # noqa: E501
            query_params.append(('team', local_var_params['team']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/stats/team/history', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TeamHistory]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_team_odds(self, season, day, team, **kwargs):  # noqa: E501
        """Get team odds per territory  # noqa: E501

        Get team odds per territory  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_odds(season, day, team, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int season: Season filter (required)
        :param int day: Day filter (required)
        :param str team: Team filter (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[TeamOdds]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_team_odds_with_http_info(season, day, team, **kwargs)  # noqa: E501

    def get_team_odds_with_http_info(self, season, day, team, **kwargs):  # noqa: E501
        """Get team odds per territory  # noqa: E501

        Get team odds per territory  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_odds_with_http_info(season, day, team, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int season: Season filter (required)
        :param int day: Day filter (required)
        :param str team: Team filter (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[TeamOdds], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['season', 'day', 'team']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_odds" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'season' is set
        if self.api_client.client_side_validation and ('season' not in local_var_params or  # noqa: E501
                                                        local_var_params['season'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `season` when calling `get_team_odds`")  # noqa: E501
        # verify the required parameter 'day' is set
        if self.api_client.client_side_validation and ('day' not in local_var_params or  # noqa: E501
                                                        local_var_params['day'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `day` when calling `get_team_odds`")  # noqa: E501
        # verify the required parameter 'team' is set
        if self.api_client.client_side_validation and ('team' not in local_var_params or  # noqa: E501
                                                        local_var_params['team'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `team` when calling `get_team_odds`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'season' in local_var_params and local_var_params['season'] is not None:  # noqa: E501
            query_params.append(('season', local_var_params['season']))  # noqa: E501
        if 'day' in local_var_params and local_var_params['day'] is not None:  # noqa: E501
            query_params.append(('day', local_var_params['day']))  # noqa: E501
        if 'team' in local_var_params and local_var_params['team'] is not None:  # noqa: E501
            query_params.append(('team', local_var_params['team']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/team/odds', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TeamOdds]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_team_strength(self, team, **kwargs):  # noqa: E501
        """Get current team strength  # noqa: E501

        Team strength for the most recent turns  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_strength(team, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str team: Team name (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TeamStrength
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_team_strength_with_http_info(team, **kwargs)  # noqa: E501

    def get_team_strength_with_http_info(self, team, **kwargs):  # noqa: E501
        """Get current team strength  # noqa: E501

        Team strength for the most recent turns  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_team_strength_with_http_info(team, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str team: Team name (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TeamStrength, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['team']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_team_strength" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'team' is set
        if self.api_client.client_side_validation and ('team' not in local_var_params or  # noqa: E501
                                                        local_var_params['team'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `team` when calling `get_team_strength`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'team' in local_var_params and local_var_params['team'] is not None:  # noqa: E501
            query_params.append(('team', local_var_params['team']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/stats/team', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TeamStrength',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_teams(self, **kwargs):  # noqa: E501
        """Get list of teams  # noqa: E501

        Teams list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_teams(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[Team]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_teams_with_http_info(**kwargs)  # noqa: E501

    def get_teams_with_http_info(self, **kwargs):  # noqa: E501
        """Get list of teams  # noqa: E501

        Teams list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_teams_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[Team], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_teams" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/teams', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Team]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
