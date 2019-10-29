# MessageSession

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Session ID. | 
**start_time** | **str** | Session creation time. | 
**text** | **str** | Session text. If a template was used for the session text (see [Messages: Send](http://docs.textmagictesting.com/#tag/Outbound-Messages) for details), it may contain template tags.  | 
**source** | **str** | *   **O** – for TextMagic Online *   **A** – for API *   **M** – for TextMagic Messenger *   **E** – for [Email to SMS](http://docs.textmagictesting.com/#tag/Send-Email-to-SMS) *   **X** – for [Distribution Lists](http://docs.textmagictesting.com/#tag/Distribution-Lists)  | 
**reference_id** | **str** | Custom reference ID (see [Messages: Send](http://docs.textmagictesting.com/#tag/Send-Email-to-SMS) for details).  | 
**price** | **float** | Session cost (in account currency). | 
**numbers_count** | **int** | Session recipient count. | 
**destination** | **str** | Destination type of a Message Session: * **t** - text SMS * **s** - text-to-speech * **v** - voice broadcast  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


