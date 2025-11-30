# ScheduleEmailCampaignRequestRecipients

Campaign recipients configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_ids** | **List[int]** | Array of contact IDs to send to. | 
**emails** | **List[str]** | Array of email addresses to send to. | 
**group_ids** | **List[int]** | Array of group IDs to send to. | 

## Example

```python
from TextMagic.models.schedule_email_campaign_request_recipients import ScheduleEmailCampaignRequestRecipients

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduleEmailCampaignRequestRecipients from a JSON string
schedule_email_campaign_request_recipients_instance = ScheduleEmailCampaignRequestRecipients.from_json(json)
# print the JSON string representation of the object
print(ScheduleEmailCampaignRequestRecipients.to_json())

# convert the object into a dict
schedule_email_campaign_request_recipients_dict = schedule_email_campaign_request_recipients_instance.to_dict()
# create an instance of ScheduleEmailCampaignRequestRecipients from a dict
schedule_email_campaign_request_recipients_from_dict = ScheduleEmailCampaignRequestRecipients.from_dict(schedule_email_campaign_request_recipients_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


