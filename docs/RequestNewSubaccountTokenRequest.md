# RequestNewSubaccountTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | Sub-account ID. | [optional] 
**password** | **str** | Your account password. | [optional] 
**app_name** | **str** | Application name. | [optional] 

## Example

```python
from TextMagic.models.request_new_subaccount_token_request import RequestNewSubaccountTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestNewSubaccountTokenRequest from a JSON string
request_new_subaccount_token_request_instance = RequestNewSubaccountTokenRequest.from_json(json)
# print the JSON string representation of the object
print(RequestNewSubaccountTokenRequest.to_json())

# convert the object into a dict
request_new_subaccount_token_request_dict = request_new_subaccount_token_request_instance.to_dict()
# create an instance of RequestNewSubaccountTokenRequest from a dict
request_new_subaccount_token_request_from_dict = RequestNewSubaccountTokenRequest.from_dict(request_new_subaccount_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


