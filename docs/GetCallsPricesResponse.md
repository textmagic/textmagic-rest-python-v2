# GetCallsPricesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outbound** | **float** | Price for outbound message. | 
**inbound** | **float** | Price for inbound message. | 
**forward** | **float** | Price for forward. | 
**country** | **str** | 2-letter ISO country code for local phone numbers, used when local is  set to true. Default is account country. | 

## Example

```python
from TextMagic.models.get_calls_prices_response import GetCallsPricesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCallsPricesResponse from a JSON string
get_calls_prices_response_instance = GetCallsPricesResponse.from_json(json)
# print the JSON string representation of the object
print(GetCallsPricesResponse.to_json())

# convert the object into a dict
get_calls_prices_response_dict = get_calls_prices_response_instance.to_dict()
# create an instance of GetCallsPricesResponse from a dict
get_calls_prices_response_from_dict = GetCallsPricesResponse.from_dict(get_calls_prices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


