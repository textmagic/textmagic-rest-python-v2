# Survey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**status** | **str** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**receipents** | [**List[SurveyRecipient]**](SurveyRecipient.md) |  | [optional] 
**countries** | [**List[SurveySenderCountries]**](SurveySenderCountries.md) |  | [optional] 

## Example

```python
from TextMagic.models.survey import Survey

# TODO update the JSON string below
json = "{}"
# create an instance of Survey from a JSON string
survey_instance = Survey.from_json(json)
# print the JSON string representation of the object
print(Survey.to_json())

# convert the object into a dict
survey_dict = survey_instance.to_dict()
# create an instance of Survey from a dict
survey_from_dict = Survey.from_dict(survey_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


