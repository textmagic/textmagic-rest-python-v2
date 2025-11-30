# BuyDedicatedNumberRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** | Dedicated phone number. | [optional] 
**country** | **str** | Country code phone number. | [optional] 
**user_id** | **int** | Assigned dedicated number. This number will be available for this account only. You cannot transfer numbers between sub-accounts.  | [optional] 

## Example

```python
from TextMagic.models.buy_dedicated_number_request import BuyDedicatedNumberRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BuyDedicatedNumberRequest from a JSON string
buy_dedicated_number_request_instance = BuyDedicatedNumberRequest.from_json(json)
# print the JSON string representation of the object
print(BuyDedicatedNumberRequest.to_json())

# convert the object into a dict
buy_dedicated_number_request_dict = buy_dedicated_number_request_instance.to_dict()
# create an instance of BuyDedicatedNumberRequest from a dict
buy_dedicated_number_request_from_dict = BuyDedicatedNumberRequest.from_dict(buy_dedicated_number_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


