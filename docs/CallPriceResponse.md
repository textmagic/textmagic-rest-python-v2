# CallPriceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outbound** | **float** | Price for outbound message. | 
**inbound** | **float** | Price for inbound message. | 
**forward** | **float** | Price for forward. | 
**country** | **str** | The 2-letter ISO country code for local phone numbers, used when local is  set to true. Default is account country. | 

## Example

```python
from TextMagic.models.call_price_response import CallPriceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CallPriceResponse from a JSON string
call_price_response_instance = CallPriceResponse.from_json(json)
# print the JSON string representation of the object
print(CallPriceResponse.to_json())

# convert the object into a dict
call_price_response_dict = call_price_response_instance.to_dict()
# create an instance of CallPriceResponse from a dict
call_price_response_from_dict = CallPriceResponse.from_dict(call_price_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


