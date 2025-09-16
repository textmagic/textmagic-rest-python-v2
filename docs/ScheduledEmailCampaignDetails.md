# ScheduledEmailCampaignDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique scheduled campaign ID. | 
**status** | **str** | Current scheduled campaign status. | 
**email_sender_id** | **int** | Email sender ID used for this campaign. | [optional] 
**start_at** | **datetime** | Scheduled start timestamp (UTC). | 
**end_at** | **datetime** | End timestamp for recurring campaigns (UTC). | [optional] 
**next_send_at** | **datetime** | Next scheduled send timestamp (UTC). | [optional] 
**created_by** | [**UserPersonalInfo**](UserPersonalInfo.md) |  | 
**created_at** | **datetime** | Campaign creation timestamp. | 
**updated_at** | **datetime** | Last update timestamp. | 
**type** | **str** | Campaign recurrence type. | 
**from_name** | **str** | Sender name displayed in recipient&#39;s inbox. | [optional] 
**from_email** | **str** | Sender email address. | 
**reply_to_email** | **str** | Reply-to email address. | 
**subject** | **str** | Email subject line. | 
**html** | **str** | HTML email content. | 
**recipients_count** | **int** | Number of recipients for this campaign. | 
**sending_timezone** | **str** | Timezone for sending the campaign. | 
**rrule** | **str** | RFC 5545 recurrence rule for recurring campaigns. | [optional] 
**occurrence_summary** | **str** | Human-readable schedule description. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


