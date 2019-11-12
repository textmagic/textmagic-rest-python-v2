# MessagingStatItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reply_rate** | **float** | The number of incoming messages divided by the number of total messages. | 
**_date** | **datetime** | Time interval start: empty if the **by** parameter was set to **off**.  | 
**delivery_rate** | **float** | Message delivery rate:the number of delivered messages divided by the number of total messages. | 
**costs** | **float** | Cost for sent messages during this period. The costs are in the [Account](https://docs.textmagic.com/#tag/User) currency.  | 
**messages_received** | **int** | Total received messages count. | 
**messages_sent_delivered** | **int** | Delivered messages count. As messages are retried for up to 48 hours, this value could change. | 
**messages_sent_accepted** | **int** | Messages accepted for delivery (in queue) but not yet delivered. | 
**messages_sent_buffered** | **int** | Messages buffered by endpoint cell phone operators. | 
**messages_sent_failed** | **int** | Messages that have failed for whatever reason, e.g. the destination phone was switched off for 48 hours or the recipient&#39;s phone account is out of service. | 
**messages_sent_rejected** | **int** | Messages that were rejected: invalid Sender ID used (e.g. you cannot use the Sender ID or your own mobile number when sending to the United States and Canada.)  | 
**messages_sent_parts** | **int** | Total sent messages **parts** count. Note that this is not equal to the sent messages count, because one message could consist of 1 to 6 parts and users are charged per part, not per message. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


