# GetBalanceNotificationOptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_1** | **str** | Contains sign of currency in Unicode hex code. | 
**var_2** | **str** | Contains sign of currency in Unicode hex code. | 
**var_3** | **str** | Contains sign of currency in Unicode hex code. | 
**var_5** | **str** | Contains sign of currency in Unicode hex code. | 
**var_10** | **str** | Contains sign of currency in Unicode hex code. | 
**var_20** | **str** | Contains sign of currency in Unicode hex code. | 
**var_30** | **str** | Contains sign of currency in Unicode hex code. | 
**var_50** | **str** | Contains sign of currency in Unicode hex code. | 
**var_100** | **str** | Contains sign of currency in Unicode hex code. | 
**var_500** | **str** | Contains sign of currency in Unicode hex code. | 
**var_1000** | **str** | Contains sign of currency in Unicode hex code. | 

## Example

```python
from TextMagic.models.get_balance_notification_options_response import GetBalanceNotificationOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBalanceNotificationOptionsResponse from a JSON string
get_balance_notification_options_response_instance = GetBalanceNotificationOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(GetBalanceNotificationOptionsResponse.to_json())

# convert the object into a dict
get_balance_notification_options_response_dict = get_balance_notification_options_response_instance.to_dict()
# create an instance of GetBalanceNotificationOptionsResponse from a dict
get_balance_notification_options_response_from_dict = GetBalanceNotificationOptionsResponse.from_dict(get_balance_notification_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


