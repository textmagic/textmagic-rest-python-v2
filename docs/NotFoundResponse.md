# NotFoundResponse

Returned when requested entity was not found.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Error code. Meanings of error codes are similar to [HTTP response codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes). | [optional] 
**message** | **str** | A Brief error message. You could display this message to your user or save it in a log. | [optional] 

## Example

```python
from TextMagic.models.not_found_response import NotFoundResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NotFoundResponse from a JSON string
not_found_response_instance = NotFoundResponse.from_json(json)
# print the JSON string representation of the object
print(NotFoundResponse.to_json())

# convert the object into a dict
not_found_response_dict = not_found_response_instance.to_dict()
# create an instance of NotFoundResponse from a dict
not_found_response_from_dict = NotFoundResponse.from_dict(not_found_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


