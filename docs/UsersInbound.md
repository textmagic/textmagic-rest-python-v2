# UsersInbound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Dedicated number ID. | 
**display_time_format** | **str** | Format for representation of time. | [optional] 
**phone** | **str** | Dedicated phone number. | [optional] 
**user** | [**User**](User.md) |  | 
**purchased_at** | **datetime** | Time when the dedicated number was purchased. | 
**expire_at** | **datetime** | Dedicated number subscription expiration time. | 
**status** | **str** | Number status: *   **U** for Unused. No messages have been sent from (or received to) this number; *   **A** for Active.  | 
**country** | [**Country**](Country.md) |  | 

## Example

```python
from TextMagic.models.users_inbound import UsersInbound

# TODO update the JSON string below
json = "{}"
# create an instance of UsersInbound from a JSON string
users_inbound_instance = UsersInbound.from_json(json)
# print the JSON string representation of the object
print(UsersInbound.to_json())

# convert the object into a dict
users_inbound_dict = users_inbound_instance.to_dict()
# create an instance of UsersInbound from a dict
users_inbound_from_dict = UsersInbound.from_dict(users_inbound_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


