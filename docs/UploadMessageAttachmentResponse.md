# UploadMessageAttachmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chars** | **int** | &#x60;href&#x60; field characters count.  | 
**href** | **str** | This is a relative link to your file. To construct a full link, just add “[https://my.textmagic.com/”](https://my.textmagic.com/%E2%80%9D) to the beginning (like this: [https://my.textmagic.com/click/Zwcj9](https://my.textmagic.com/click/Zwcj9)). For most modern devices, you can omit the “https://” part and write just [my.textmagic.com/click/Zwcj9](https://my.textmagic.com/click/Zwcj9), which will save you 8 characters.  | 
**name** | **str** | File name of the uploaded file.  | 
**size** | **int** | Attachment size in bytes. | 
**resource** | **str** | Internal file name | 

## Example

```python
from TextMagic.models.upload_message_attachment_response import UploadMessageAttachmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadMessageAttachmentResponse from a JSON string
upload_message_attachment_response_instance = UploadMessageAttachmentResponse.from_json(json)
# print the JSON string representation of the object
print(UploadMessageAttachmentResponse.to_json())

# convert the object into a dict
upload_message_attachment_response_dict = upload_message_attachment_response_instance.to_dict()
# create an instance of UploadMessageAttachmentResponse from a dict
upload_message_attachment_response_from_dict = UploadMessageAttachmentResponse.from_dict(upload_message_attachment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


