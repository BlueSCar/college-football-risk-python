# college_football_risk.TeamsApi

All URIs are relative to *https://collegefootballrisk.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player_moves_by_turn**](TeamsApi.md#get_player_moves_by_turn) | **GET** /api/team/players | Get players moves by turn
[**get_team_history**](TeamsApi.md#get_team_history) | **GET** /stats/team/history | Get historical team stats
[**get_team_strength**](TeamsApi.md#get_team_strength) | **GET** /stats/team | Get current team strength
[**get_teams**](TeamsApi.md#get_teams) | **GET** /teams | Get list of teams


# **get_player_moves_by_turn**
> list[TeamTurnPlayer] get_player_moves_by_turn(season, day, team=team)

Get players moves by turn

Get player moves by turn

### Example

```python
from __future__ import print_function
import time
import college_football_risk
from college_football_risk.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with college_football_risk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = college_football_risk.TeamsApi(api_client)
    season = 56 # int | Season filter
day = 56 # int | Day filter
team = 56 # int | Team name filter (optional)

    try:
        # Get players moves by turn
        api_response = api_instance.get_player_moves_by_turn(season, day, team=team)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->get_player_moves_by_turn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season filter | 
 **day** | **int**| Day filter | 
 **team** | **int**| Team name filter | [optional] 

### Return type

[**list[TeamTurnPlayer]**](TeamTurnPlayer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**500** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_history**
> list[TeamHistory] get_team_history(team)

Get historical team stats

Historical team statistics

### Example

```python
from __future__ import print_function
import time
import college_football_risk
from college_football_risk.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with college_football_risk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = college_football_risk.TeamsApi(api_client)
    team = 'team_example' # str | Team name

    try:
        # Get historical team stats
        api_response = api_instance.get_team_history(team)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->get_team_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | **str**| Team name | 

### Return type

[**list[TeamHistory]**](TeamHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**500** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_strength**
> TeamStrength get_team_strength(team)

Get current team strength

Team strength for the most recent turns

### Example

```python
from __future__ import print_function
import time
import college_football_risk
from college_football_risk.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with college_football_risk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = college_football_risk.TeamsApi(api_client)
    team = 'team_example' # str | Team name

    try:
        # Get current team strength
        api_response = api_instance.get_team_strength(team)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->get_team_strength: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | **str**| Team name | 

### Return type

[**TeamStrength**](TeamStrength.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**500** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams**
> list[Team] get_teams()

Get list of teams

Teams list

### Example

```python
from __future__ import print_function
import time
import college_football_risk
from college_football_risk.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with college_football_risk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = college_football_risk.TeamsApi(api_client)
    
    try:
        # Get list of teams
        api_response = api_instance.get_teams()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamsApi->get_teams: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Team]**](Team.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful operation |  -  |
**500** | error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

