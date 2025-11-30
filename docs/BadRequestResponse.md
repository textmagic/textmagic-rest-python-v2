# BadRequestResponse

Returned when input data validation process has been failed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Error code. Meanings of error codes are similar to [HTTP response codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). | [optional] 
**message** | **str** | Brief error message. You could display this message to your user or save it in a log. | [optional] 
**errors** | [**BadRequestResponseErrors**](BadRequestResponseErrors.md) |  | [optional] 

## Example

```python
from TextMagic.models.bad_request_response import BadRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BadRequestResponse from a JSON string
bad_request_response_instance = BadRequestResponse.from_json(json)
# print the JSON string representation of the object
print(BadRequestResponse.to_json())

# convert the object into a dict
bad_request_response_dict = bad_request_response_instance.to_dict()
# create an instance of BadRequestResponse from a dict
bad_request_response_from_dict = BadRequestResponse.from_dict(bad_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


