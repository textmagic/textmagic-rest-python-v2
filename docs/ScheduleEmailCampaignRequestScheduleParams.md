# ScheduleEmailCampaignRequestScheduleParams

Scheduling configuration for the campaign.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date_time** | **datetime** | When to start sending the campaign (ISO 8601 format). | 
**timezone** | **str** | Timezone for the schedule (e.g., \&quot;America/New_York\&quot;). | 
**rrule** | **str** | RFC 5545 recurrence rule for recurring campaigns. | [optional] 

## Example

```python
from TextMagic.models.schedule_email_campaign_request_schedule_params import ScheduleEmailCampaignRequestScheduleParams

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleEmailCampaignRequestScheduleParams from a JSON string
schedule_email_campaign_request_schedule_params_instance = ScheduleEmailCampaignRequestScheduleParams.from_json(json)
# print the JSON string representation of the object
print(ScheduleEmailCampaignRequestScheduleParams.to_json())

# convert the object into a dict
schedule_email_campaign_request_schedule_params_dict = schedule_email_campaign_request_schedule_params_instance.to_dict()
# create an instance of ScheduleEmailCampaignRequestScheduleParams from a dict
schedule_email_campaign_request_schedule_params_from_dict = ScheduleEmailCampaignRequestScheduleParams.from_dict(schedule_email_campaign_request_schedule_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


