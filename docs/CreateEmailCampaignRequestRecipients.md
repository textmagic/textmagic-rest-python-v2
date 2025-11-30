# CreateEmailCampaignRequestRecipients

Campaign recipients configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_ids** | **List[int]** | Array of contact IDs to send to. | 
**emails** | **List[str]** | Array of email addresses to send to. | 
**group_ids** | **List[int]** | Array of group IDs to send to. | 

## Example

```python
from TextMagic.models.create_email_campaign_request_recipients import CreateEmailCampaignRequestRecipients

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEmailCampaignRequestRecipients from a JSON string
create_email_campaign_request_recipients_instance = CreateEmailCampaignRequestRecipients.from_json(json)
# print the JSON string representation of the object
print(CreateEmailCampaignRequestRecipients.to_json())

# convert the object into a dict
create_email_campaign_request_recipients_dict = create_email_campaign_request_recipients_instance.to_dict()
# create an instance of CreateEmailCampaignRequestRecipients from a dict
create_email_campaign_request_recipients_from_dict = CreateEmailCampaignRequestRecipients.from_dict(create_email_campaign_request_recipients_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


