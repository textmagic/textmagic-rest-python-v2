# Contact

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Contact ID. | 
**favorited** | **bool** | Is the Contact favorite? [Favorite list](https://docs.textmagic.com/#operation/getFavorites). | 
**blocked** | **bool** | Is the Contact blocked? [Blocked contacts](https://docs.textmagic.com/#operation/getBlockedContacts). | 
**first_name** | **str** | Contact first name. | 
**last_name** | **str** | Contact last name. | 
**company_name** | **str** | Company name. | 
**phone** | **str** | Phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164). | 
**email** | **str** | Contact email address. | 
**country** | [**Country**](Country.md) | Contact country. | 
**custom_fields** | [**list[ContactCustomField]**](ContactCustomField.md) | See the [Custom Fields](https://docs.textmagic.com/#tag/Custom-Fields) section. | 
**user** | [**User**](User.md) |  | 
**lists** | [**list[List]**](List.md) |  | 
**phone_type** | **str** | Phone number type: * **0** if it is fixed-line; * **1** if it is mobile; * **2** if it is mobile or fixed-line (in case we cannot distingush between fixed-line or mobile); * **3** if it is toll-free; * **4** if it is a premium rate phone; * **5** if it is a shared cost phone; * **6** if it is a VoIP; * **7** if it is a [Personal Number](); * **8** if it is a pager; * **9** if it is a Universal Access Number; * **10** if the phone type is unknown; * **-1** if the phone type is not yet processed or cannot be determined.  | 
**avatar** | [**ContactImage**](ContactImage.md) |  | 
**notes** | [**list[ContactNote]**](ContactNote.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


