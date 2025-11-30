# SurveyRecipient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone** | **str** |  | 

## Example

```python
from TextMagic.models.survey_recipient import SurveyRecipient

# TODO update the JSON string below
json = "{}"
# create an instance of SurveyRecipient from a JSON string
survey_recipient_instance = SurveyRecipient.from_json(json)
# print the JSON string representation of the object
print(SurveyRecipient.to_json())

# convert the object into a dict
survey_recipient_dict = survey_recipient_instance.to_dict()
# create an instance of SurveyRecipient from a dict
survey_recipient_from_dict = SurveyRecipient.from_dict(survey_recipient_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


