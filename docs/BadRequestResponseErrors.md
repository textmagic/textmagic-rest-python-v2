# BadRequestResponseErrors

If it was a **POST** or **PUT** request (and the **message** returned is `Validation Failed`), this field may contain **errors** that describe the errors grouped by the input parameter name. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common** | **List[str]** | Array of messages with errors related to the entire request. For example, you did not specify either the **text** or the **templateId** when [sending the message](https://docs.textmagic.com/#tag/Outbound-Messages).  | [optional] 
**fields** | **object** | Associative array. The keys are the POST/PUT parameter names and the values are arrays with error messages for these parameters.  | [optional] 

## Example

```python
from TextMagic.models.bad_request_response_errors import BadRequestResponseErrors

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestResponseErrors from a JSON string
bad_request_response_errors_instance = BadRequestResponseErrors.from_json(json)
# print the JSON string representation of the object
print(BadRequestResponseErrors.to_json())

# convert the object into a dict
bad_request_response_errors_dict = bad_request_response_errors_instance.to_dict()
# create an instance of BadRequestResponseErrors from a dict
bad_request_response_errors_from_dict = BadRequestResponseErrors.from_dict(bad_request_response_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


