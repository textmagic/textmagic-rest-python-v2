# ScheduleEmailCampaignResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign** | [**ScheduledEmailCampaignDetails**](ScheduledEmailCampaignDetails.md) |  | 
**cost** | **float** | Estimated cost for sending this campaign. | 

## Example

```python
from TextMagic.models.schedule_email_campaign_response import ScheduleEmailCampaignResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleEmailCampaignResponse from a JSON string
schedule_email_campaign_response_instance = ScheduleEmailCampaignResponse.from_json(json)
# print the JSON string representation of the object
print(ScheduleEmailCampaignResponse.to_json())

# convert the object into a dict
schedule_email_campaign_response_dict = schedule_email_campaign_response_instance.to_dict()
# create an instance of ScheduleEmailCampaignResponse from a dict
schedule_email_campaign_response_from_dict = ScheduleEmailCampaignResponse.from_dict(schedule_email_campaign_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


