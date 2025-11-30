# MessagePriceItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Country name. | 
**price** | **str** | Price to send message to desired country. | 
**country** | **str** | The 2-letter ISO country code of the recipient&#39;s phone number. | 

## Example

```python
from TextMagic.models.message_price_item import MessagePriceItem

# TODO update the JSON string below
json = "{}"
# create an instance of MessagePriceItem from a JSON string
message_price_item_instance = MessagePriceItem.from_json(json)
# print the JSON string representation of the object
print(MessagePriceItem.to_json())

# convert the object into a dict
message_price_item_dict = message_price_item_instance.to_dict()
# create an instance of MessagePriceItem from a dict
message_price_item_from_dict = MessagePriceItem.from_dict(message_price_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


