# GetSubaccountsWithTokensRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** | Application name. | [optional] 
**password** | **str** | Your account password. | [optional] 

## Example

```python
from TextMagic.models.get_subaccounts_with_tokens_request import GetSubaccountsWithTokensRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubaccountsWithTokensRequest from a JSON string
get_subaccounts_with_tokens_request_instance = GetSubaccountsWithTokensRequest.from_json(json)
# print the JSON string representation of the object
print(GetSubaccountsWithTokensRequest.to_json())

# convert the object into a dict
get_subaccounts_with_tokens_request_dict = get_subaccounts_with_tokens_request_instance.to_dict()
# create an instance of GetSubaccountsWithTokensRequest from a dict
get_subaccounts_with_tokens_request_from_dict = GetSubaccountsWithTokensRequest.from_dict(get_subaccounts_with_tokens_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


