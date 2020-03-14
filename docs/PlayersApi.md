# college_football_risk.PlayersApi

All URIs are relative to *https://collegefootballrisk.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player**](PlayersApi.md#get_player) | **GET** /player | Player information


# **get_player**
> Player get_player(player)

Player information

Player information

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
    api_instance = college_football_risk.PlayersApi(api_client)
    player = 'player_example' # str | Player username without the \"u/\" (e.g. \"u/BlueSCar\" would just be \"BlueSCar\")

    try:
        # Player information
        api_response = api_instance.get_player(player)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PlayersApi->get_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player** | **str**| Player username without the \&quot;u/\&quot; (e.g. \&quot;u/BlueSCar\&quot; would just be \&quot;BlueSCar\&quot;) | 

### Return type

[**Player**](Player.md)

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

