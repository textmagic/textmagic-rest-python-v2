# RequestSenderIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender_id** | **str** | The Sender ID that you are applying for. *   11 characters maximum; *   Only Latin based characters and digits are allowed; *   Should contain at least 1 letter.  | [optional] 
**explanation** | **str** | Explanation of why you need this Sender ID. | [optional] 

## Example

```python
from TextMagic.models.request_sender_id_request import RequestSenderIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestSenderIdRequest from a JSON string
request_sender_id_request_instance = RequestSenderIdRequest.from_json(json)
# print the JSON string representation of the object
print(RequestSenderIdRequest.to_json())

# convert the object into a dict
request_sender_id_request_dict = request_sender_id_request_instance.to_dict()
# create an instance of RequestSenderIdRequest from a dict
request_sender_id_request_from_dict = RequestSenderIdRequest.from_dict(request_sender_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


