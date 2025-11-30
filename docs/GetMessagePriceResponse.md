# GetMessagePriceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** | Total price of the message. | 
**parts** | **int** | Message parts (multiples of 160 characters) count. | 
**countries** | [**List[GetMessagePriceResponseCountriesItem]**](GetMessagePriceResponseCountriesItem.md) |  | 

## Example

```python
from TextMagic.models.get_message_price_response import GetMessagePriceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessagePriceResponse from a JSON string
get_message_price_response_instance = GetMessagePriceResponse.from_json(json)
# print the JSON string representation of the object
print(GetMessagePriceResponse.to_json())

# convert the object into a dict
get_message_price_response_dict = get_message_price_response_instance.to_dict()
# create an instance of GetMessagePriceResponse from a dict
get_message_price_response_from_dict = GetMessagePriceResponse.from_dict(get_message_price_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


