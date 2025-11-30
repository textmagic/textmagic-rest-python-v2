# GetMessagePriceResponseCountriesItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | The 2-letter ISO country code. | 
**country_name** | **str** | Country name. | 
**allow_dedicated** | **bool** | Is allowed to use a dedicated number? | 
**count** | **float** | Parts count to send. | 
**max** | **float** | Maximum parts to send. | 
**sum** | **str** | Total price to send. | 
**landline** | **float** | Is this a landline number? | 

## Example

```python
from TextMagic.models.get_message_price_response_countries_item import GetMessagePriceResponseCountriesItem

# TODO update the JSON string below
json = "{}"
# create an instance of GetMessagePriceResponseCountriesItem from a JSON string
get_message_price_response_countries_item_instance = GetMessagePriceResponseCountriesItem.from_json(json)
# print the JSON string representation of the object
print(GetMessagePriceResponseCountriesItem.to_json())

# convert the object into a dict
get_message_price_response_countries_item_dict = get_message_price_response_countries_item_instance.to_dict()
# create an instance of GetMessagePriceResponseCountriesItem from a dict
get_message_price_response_countries_item_from_dict = GetMessagePriceResponseCountriesItem.from_dict(get_message_price_response_countries_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


