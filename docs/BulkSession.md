# BulkSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Bulk Session ID. | 
**status** | **str** | * **n** – bulk session is just created * **w** - work in progress * **f** - failed * **c** - completed with success * **s** - suspended  | 
**items_processed** | **int** | Amount of messages already processed. | 
**items_total** | **int** | Total amount of messages to be processed. | 
**created_at** | **datetime** | Creation date and time of a Bulk Session. | 
**session** | [**MessageSession**](MessageSession.md) |  | 
**text** | **str** | Message text of a Bulk Session. | 

## Example

```python
from TextMagic.models.bulk_session import BulkSession

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSession from a JSON string
bulk_session_instance = BulkSession.from_json(json)
# print the JSON string representation of the object
print(BulkSession.to_json())

# convert the object into a dict
bulk_session_dict = bulk_session_instance.to_dict()
# create an instance of BulkSession from a dict
bulk_session_from_dict = BulkSession.from_dict(bulk_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


