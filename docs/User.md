# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User ID. | 
**display_time_format** | **str** | User&#39;s prefered format of time display * *12h* - AM/PM format * *24h* - 24 hour clock format  | [optional] 
**username** | **str** | Username. | 
**first_name** | **str** | Account first name. | 
**last_name** | **str** | Account last name. | 
**email** | **str** | User email address. | 
**status** | **str** | Current account status: * **A** for Active * **T** for Trial.  | 
**balance** | **float** | Account balance (in account currency). | 
**phone** | **str** | User phone number | 
**company** | **str** | Account company name. | 
**currency** | [**Currency**](Currency.md) |  | 
**country** | [**Country**](Country.md) |  | 
**timezone** | [**Timezone**](Timezone.md) |  | 
**subaccount_type** | **str** | Type of account: * **P** for Parent User * **A** for Administrator Sub-Account * **U** for Regular User  | 
**email_accepted** | **bool** | Is account has confirmed Email. | 
**phone_accepted** | **bool** | Is account has confirmed Phone number. | 
**avatar** | [**UserImage**](UserImage.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


