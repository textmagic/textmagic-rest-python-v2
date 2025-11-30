# SenderId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Numeric sender ID. | 
**display_time_format** | **str** | Format for representation of time. | [optional] 
**sender_id** | **str** | Alphanumeric ID. | 
**user** | [**User**](User.md) |  | 
**status** | **str** | *   **P** for Pending - this Sender ID is being reviewed by our support team; *   **R** for Rejected - our support team rejected your application for this Sender ID; *   **A** for Active.  | 

## Example

```python
from TextMagic.models.sender_id import SenderId

# TODO update the JSON string below
json = "{}"
# create an instance of SenderId from a JSON string
sender_id_instance = SenderId.from_json(json)
# print the JSON string representation of the object
print(SenderId.to_json())

# convert the object into a dict
sender_id_dict = sender_id_instance.to_dict()
# create an instance of SenderId from a dict
sender_id_from_dict = SenderId.from_dict(sender_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


