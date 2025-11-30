# MessageIn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the inbound message. | 
**sender** | **str** | The sender’s phone number. | 
**receiver** | **str** | The receiver’s phone number (i.e. your dedicated or shared reply number). | 
**message_time** | **datetime** | The time when the message reached the Textmagic API endpoint. | 
**text** | **str** | The text from the received message. | 
**contact_id** | **int** | Sender contact ID. | [optional] 
**first_name** | **str** | Sender contact first name. | [optional] 
**last_name** | **str** | Sender contact last name. | [optional] 
**avatar** | **str** |  | 
**email** | **str** | Sender email. | [optional] 
**contact_user_id** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from TextMagic.models.message_in import MessageIn

# TODO update the JSON string below
json = "{}"
# create an instance of MessageIn from a JSON string
message_in_instance = MessageIn.from_json(json)
# print the JSON string representation of the object
print(MessageIn.to_json())

# convert the object into a dict
message_in_dict = message_in_instance.to_dict()
# create an instance of MessageIn from a dict
message_in_from_dict = MessageIn.from_dict(message_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


