# college_football_risk.StatsApi

All URIs are relative to *https://collegefootballrisk.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_leaderboard**](StatsApi.md#get_leaderboard) | **GET** /stats/leaderboard | Game leaderboard
[**get_turns**](StatsApi.md#get_turns) | **GET** /turns | Get turns list


# **get_leaderboard**
> list[LeaderboardTeam] get_leaderboard(season, day)

Game leaderboard

Game leaderboard

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
    api_instance = college_football_risk.StatsApi(api_client)
    season = 56 # int | Season number
day = 56 # int | Day number

    try:
        # Game leaderboard
        api_response = api_instance.get_leaderboard(season, day)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatsApi->get_leaderboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season number | 
 **day** | **int**| Day number | 

### Return type

[**list[LeaderboardTeam]**](LeaderboardTeam.md)

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

# **get_turns**
> list[Turn] get_turns()

Get turns list

List of turns

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
    api_instance = college_football_risk.StatsApi(api_client)
    
    try:
        # Get turns list
        api_response = api_instance.get_turns()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatsApi->get_turns: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Turn]**](Turn.md)

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

