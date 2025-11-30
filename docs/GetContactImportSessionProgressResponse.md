# GetContactImportSessionProgressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | Session status: * **1** - if session has been initialized but not yet started; * **3** - if session is being processed; * **4** - if session has errors; * **5** - if session completed successfully.  | 
**processed** | **int** | How many contacts have been imported? | 

## Example

```python
from TextMagic.models.get_contact_import_session_progress_response import GetContactImportSessionProgressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetContactImportSessionProgressResponse from a JSON string
get_contact_import_session_progress_response_instance = GetContactImportSessionProgressResponse.from_json(json)
# print the JSON string representation of the object
print(GetContactImportSessionProgressResponse.to_json())

# convert the object into a dict
get_contact_import_session_progress_response_dict = get_contact_import_session_progress_response_instance.to_dict()
# create an instance of GetContactImportSessionProgressResponse from a dict
get_contact_import_session_progress_response_from_dict = GetContactImportSessionProgressResponse.from_dict(get_contact_import_session_progress_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


