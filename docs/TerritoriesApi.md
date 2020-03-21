# college_football_risk.TerritoriesApi

All URIs are relative to *https://collegefootballrisk.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_territories**](TerritoriesApi.md#get_territories) | **GET** /territories | Get list of territories, including ownership status for the given turn
[**get_territory_history**](TerritoriesApi.md#get_territory_history) | **GET** /territory/history | Get historical territory data
[**get_territory_turn**](TerritoriesApi.md#get_territory_turn) | **GET** /territory/turn | Get teritory statistics for a specific turn


# **get_territories**
> list[Territory] get_territories(season=season, day=day)

Get list of territories, including ownership status for the given turn

Territories list

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
    api_instance = college_football_risk.TerritoriesApi(api_client)
    season = 56 # int | Season filter (optional)
day = 56 # int | Day filter (optional)

    try:
        # Get list of territories, including ownership status for the given turn
        api_response = api_instance.get_territories(season=season, day=day)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TerritoriesApi->get_territories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **season** | **int**| Season filter | [optional] 
 **day** | **int**| Day filter | [optional] 

### Return type

[**list[Territory]**](Territory.md)

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

# **get_territory_history**
> list[TerritoryHistory] get_territory_history(territory, season)

Get historical territory data

Historical territory data

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
    api_instance = college_football_risk.TerritoriesApi(api_client)
    territory = 'territory_example' # str | Territory name
season = 56 # int | Season

    try:
        # Get historical territory data
        api_response = api_instance.get_territory_history(territory, season)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TerritoriesApi->get_territory_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **territory** | **str**| Territory name | 
 **season** | **int**| Season | 

### Return type

[**list[TerritoryHistory]**](TerritoryHistory.md)

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

# **get_territory_turn**
> list[TerritoryTurn] get_territory_turn(territory, season, day)

Get teritory statistics for a specific turn

Teritory statistics for a specific turn

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
    api_instance = college_football_risk.TerritoriesApi(api_client)
    territory = 'territory_example' # str | Territory name
season = 56 # int | Season
day = 56 # int | Day

    try:
        # Get teritory statistics for a specific turn
        api_response = api_instance.get_territory_turn(territory, season, day)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TerritoriesApi->get_territory_turn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **territory** | **str**| Territory name | 
 **season** | **int**| Season | 
 **day** | **int**| Day | 

### Return type

[**list[TerritoryTurn]**](TerritoryTurn.md)

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

