# DoEmailLookupResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The email address passed to the call. | 
**status** | **str** | The email is &#x60;valid&#x60; or &#x60;invalid&#x60;. | 
**deliverability** | **str** | The delivery status of the email address is&#x60;deliverable&#x60;, &#x60;undeliverable&#x60;. or &#x60;unknown&#x60;. | 
**reason** | **str** | The reason why the checked email is invalid/undeliverable. | 
**risk** | **str** | The risk score of the email is&#x60;high&#x60;, &#x60;medium&#x60;, &#x60;low&#x60; or &#x60;null&#x60;. | 
**address_type** | **str** | The email address type (domain) is &#x60;free&#x60; or &#x60;corporate&#x60;. | 
**is_disposable_address** | **bool** | This is &#x60;true&#x60; if the domain is in the list of disposable email addresses; otherwise, it returns as &#x60;false&#x60;. | 
**suggestion** | **str** | Null if nothing is suggested; however, if there is a potential typo in the email address, the closest suggestion is provided. | 
**email_role** | **str** | Checks the mailbox part of the email to see whether it matches a specific role type (‘admin’, ‘sales’, ‘webmaster’). | 
**local_part** | **str** | The local part of the email address. | 
**domain_part** | **str** | The domain part of the email address. | 
**exchange** | **str** | Email exchange server domain name (MX record value). | 
**preference** | **int** | MX record preference. | 
**is_in_white_list** | **bool** | &#x60;true&#x60; if the email address exists in the TextMagic whitelist.  | 
**is_in_black_list** | **bool** | &#x60;true&#x60; if the email address exists in the TextMagic blacklist.  | 
**has_mx** | **bool** | &#x60;true&#x60; if the email address domain has an MX record.  | 
**has_aa** | **bool** | &#x60;true&#x60; if the email address domain has an A record (IPv4).  | 
**has_aaaa** | **bool** | &#x60;true&#x60; if the email address domain has an AAAA record (IPv6).  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


