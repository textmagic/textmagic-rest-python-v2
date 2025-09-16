# CreateEmailCampaignResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique campaign ID. | 
**status** | **str** | Current campaign status. | 
**email_sender_id** | **int** | Email sender ID used for this campaign. | [optional] 
**start_at** | **datetime** | Campaign start timestamp. | 
**created_by** | [**UserPersonalInfo**](UserPersonalInfo.md) |  | 
**from_name** | **str** | Sender name displayed in recipient&#39;s inbox. | [optional] 
**from_email** | **str** | Sender email address. | 
**reply_to_email** | **str** | Reply-to email address. | 
**subject** | **str** | Email subject line. | 
**html** | **str** | HTML email content. | 
**cost** | **float** | Total campaign cost. | 
**totals** | [**EmailCampaignStatisticTotals**](EmailCampaignStatisticTotals.md) |  | 
**outbound_email** | [**OutboundEmailResponse**](OutboundEmailResponse.md) |  | [optional] 
**failed_reason** | **str** | Reason for campaign failure if applicable. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


