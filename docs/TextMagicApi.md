# TextMagic.TextMagicApi

All URIs are relative to *https://rest.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_contacts_to_list**](TextMagicApi.md#assign_contacts_to_list) | **PUT** /api/v2/lists/{id}/contacts | Assign contacts to a list
[**block_contact**](TextMagicApi.md#block_contact) | **POST** /api/v2/contacts/block | Block a contact by phone number
[**buy_dedicated_number**](TextMagicApi.md#buy_dedicated_number) | **POST** /api/v2/numbers | Buy a dedicated number
[**cancel_verification**](TextMagicApi.md#cancel_verification) | **DELETE** /api/v2/verify/{verifyId} | Cancel verification process
[**check_phone_verification_code_tfa**](TextMagicApi.md#check_phone_verification_code_tfa) | **PUT** /api/v2/verify | Step 2: Check the verification code 
[**clear_and_assign_contacts_to_list**](TextMagicApi.md#clear_and_assign_contacts_to_list) | **POST** /api/v2/lists/{id}/contacts | Reset list members to the specified contacts
[**close_chats_bulk**](TextMagicApi.md#close_chats_bulk) | **POST** /api/v2/chats/close/bulk | Close chats (bulk)
[**close_read_chats**](TextMagicApi.md#close_read_chats) | **POST** /api/v2/chats/close/read | Close read chats
[**close_subaccount**](TextMagicApi.md#close_subaccount) | **DELETE** /api/v2/subaccounts/{id} | Close sub-account
[**create_contact**](TextMagicApi.md#create_contact) | **POST** /api/v2/contacts/normalized | Add a new contact
[**create_contact_note**](TextMagicApi.md#create_contact_note) | **POST** /api/v2/contacts/{id}/notes | Create a new contact note
[**create_custom_field**](TextMagicApi.md#create_custom_field) | **POST** /api/v2/customfields | Add a new custom field
[**create_list**](TextMagicApi.md#create_list) | **POST** /api/v2/lists | Create a new list
[**create_template**](TextMagicApi.md#create_template) | **POST** /api/v2/templates | Create a template
[**delete_all_contacts**](TextMagicApi.md#delete_all_contacts) | **DELETE** /api/v2/contact/all | Delete contacts (bulk)
[**delete_all_outbound_messages**](TextMagicApi.md#delete_all_outbound_messages) | **DELETE** /api/v2/message/all | Delete all messages
[**delete_avatar**](TextMagicApi.md#delete_avatar) | **DELETE** /api/v2/user/avatar | Delete an avatar
[**delete_chat_messages**](TextMagicApi.md#delete_chat_messages) | **POST** /api/v2/chats/{id}/messages/delete | Delete chat messages by ID(s)
[**delete_chats_bulk**](TextMagicApi.md#delete_chats_bulk) | **POST** /api/v2/chats/delete | Delete chats (bulk)
[**delete_contact**](TextMagicApi.md#delete_contact) | **DELETE** /api/v2/contacts/{id} | Delete a contact
[**delete_contact_avatar**](TextMagicApi.md#delete_contact_avatar) | **DELETE** /api/v2/contacts/{id}/avatar | Delete an avatar
[**delete_contact_note**](TextMagicApi.md#delete_contact_note) | **DELETE** /api/v2/notes/{id} | Delete a contact note
[**delete_contact_notes_bulk**](TextMagicApi.md#delete_contact_notes_bulk) | **POST** /api/v2/contacts/{id}/notes/delete | Delete contact notes (bulk)
[**delete_contacts_by_ids**](TextMagicApi.md#delete_contacts_by_ids) | **POST** /api/v2/contacts/delete | Delete contacts by IDs (bulk)
[**delete_contacts_from_list**](TextMagicApi.md#delete_contacts_from_list) | **DELETE** /api/v2/lists/{id}/contacts | Unassign contacts from a list
[**delete_custom_field**](TextMagicApi.md#delete_custom_field) | **DELETE** /api/v2/customfields/{id} | Delete a custom field
[**delete_dedicated_number**](TextMagicApi.md#delete_dedicated_number) | **DELETE** /api/v2/numbers/{id} | Cancel a dedicated number subscription
[**delete_inbound_message**](TextMagicApi.md#delete_inbound_message) | **DELETE** /api/v2/replies/{id} | Delete a single inbound message
[**delete_inbound_messages_bulk**](TextMagicApi.md#delete_inbound_messages_bulk) | **POST** /api/v2/replies/delete | Delete inbound messages (bulk)
[**delete_list**](TextMagicApi.md#delete_list) | **DELETE** /api/v2/lists/{id} | Delete a list
[**delete_list_avatar**](TextMagicApi.md#delete_list_avatar) | **DELETE** /api/v2/lists/{id}/avatar | Delete an avatar for a list
[**delete_list_contacts_bulk**](TextMagicApi.md#delete_list_contacts_bulk) | **POST** /api/v2/lists/{id}/contacts/delete | Delete contacts from a list (bulk)
[**delete_lists_bulk**](TextMagicApi.md#delete_lists_bulk) | **POST** /api/v2/lists/delete | Delete lists (bulk)
[**delete_message_session**](TextMagicApi.md#delete_message_session) | **DELETE** /api/v2/sessions/{id} | Delete a session
[**delete_message_sessions_bulk**](TextMagicApi.md#delete_message_sessions_bulk) | **POST** /api/v2/sessions/delete | Delete sessions (bulk)
[**delete_outbound_message**](TextMagicApi.md#delete_outbound_message) | **DELETE** /api/v2/messages/{id} | Delete message
[**delete_outbound_messages_bulk**](TextMagicApi.md#delete_outbound_messages_bulk) | **POST** /api/v2/messages/delete | Delete messages (bulk)
[**delete_scheduled_message**](TextMagicApi.md#delete_scheduled_message) | **DELETE** /api/v2/schedules/{id} | Delete a single scheduled message
[**delete_scheduled_messages_bulk**](TextMagicApi.md#delete_scheduled_messages_bulk) | **POST** /api/v2/schedules/delete | Delete scheduled messages (bulk)
[**delete_sender_id**](TextMagicApi.md#delete_sender_id) | **DELETE** /api/v2/senderids/{id} | Delete a Sender ID
[**delete_template**](TextMagicApi.md#delete_template) | **DELETE** /api/v2/templates/{id} | Delete a template
[**delete_templates_bulk**](TextMagicApi.md#delete_templates_bulk) | **POST** /api/v2/templates/delete | Delete templates (bulk)
[**do_carrier_lookup**](TextMagicApi.md#do_carrier_lookup) | **GET** /api/v2/lookups/{phone} | Carrier Lookup
[**do_email_lookup**](TextMagicApi.md#do_email_lookup) | **GET** /api/v2/email-lookups/{email} | Email Lookup
[**get_all_bulk_sessions**](TextMagicApi.md#get_all_bulk_sessions) | **GET** /api/v2/bulks | Get all bulk sessions
[**get_all_chats**](TextMagicApi.md#get_all_chats) | **GET** /api/v2/chats | Get all chats
[**get_all_inbound_messages**](TextMagicApi.md#get_all_inbound_messages) | **GET** /api/v2/replies | Get all inbound messages
[**get_all_message_sessions**](TextMagicApi.md#get_all_message_sessions) | **GET** /api/v2/sessions | Get all sessions
[**get_all_outbound_messages**](TextMagicApi.md#get_all_outbound_messages) | **GET** /api/v2/messages | Get all messages
[**get_all_scheduled_messages**](TextMagicApi.md#get_all_scheduled_messages) | **GET** /api/v2/schedules | Get all scheduled messages
[**get_all_templates**](TextMagicApi.md#get_all_templates) | **GET** /api/v2/templates | Get all templates
[**get_available_dedicated_numbers**](TextMagicApi.md#get_available_dedicated_numbers) | **GET** /api/v2/numbers/available | Find dedicated numbers available for purchase
[**get_available_sender_setting_options**](TextMagicApi.md#get_available_sender_setting_options) | **GET** /api/v2/sources | Get available sender settings
[**get_balance_notification_options**](TextMagicApi.md#get_balance_notification_options) | **GET** /api/v2/user/notification/balance/bundles | Returns the list of available balance options which can be used as a bound to determine when to send email to user with low balance notification. See https://my.textmagic.com/online/account/notifications/balance
[**get_balance_notification_settings**](TextMagicApi.md#get_balance_notification_settings) | **GET** /api/v2/user/notification/balance | Get balance notification settings
[**get_blocked_contacts**](TextMagicApi.md#get_blocked_contacts) | **GET** /api/v2/contacts/block/list | Get blocked contacts
[**get_bulk_session**](TextMagicApi.md#get_bulk_session) | **GET** /api/v2/bulks/{id} | Get bulk session status
[**get_callback_settings**](TextMagicApi.md#get_callback_settings) | **GET** /api/v2/callback/settings | Fetch callback URL settings
[**get_chat**](TextMagicApi.md#get_chat) | **GET** /api/v2/chats/{id} | Get a single chat
[**get_chat_by_phone**](TextMagicApi.md#get_chat_by_phone) | **GET** /api/v2/chats/{phone}/by/phone | Find chats by phone
[**get_chat_messages**](TextMagicApi.md#get_chat_messages) | **GET** /api/v2/chats/{id}/message | Get chat messages
[**get_contact**](TextMagicApi.md#get_contact) | **GET** /api/v2/contacts/{id} | Get the details of a specific contact
[**get_contact_by_phone**](TextMagicApi.md#get_contact_by_phone) | **GET** /api/v2/contacts/phone/{phone} | Get the details of a specific contact by phone number
[**get_contact_if_blocked**](TextMagicApi.md#get_contact_if_blocked) | **GET** /api/v2/contacts/block/phone | Check if a phone number is blocked
[**get_contact_import_session_progress**](TextMagicApi.md#get_contact_import_session_progress) | **GET** /api/v2/contacts/import/progress/{id} | Check import progress
[**get_contact_note**](TextMagicApi.md#get_contact_note) | **GET** /api/v2/notes/{id} | Get a contact note
[**get_contact_notes**](TextMagicApi.md#get_contact_notes) | **GET** /api/v2/contacts/{id}/notes | Fetch notes assigned to a given contact
[**get_contacts**](TextMagicApi.md#get_contacts) | **GET** /api/v2/contacts | Get all contacts
[**get_contacts_autocomplete**](TextMagicApi.md#get_contacts_autocomplete) | **GET** /api/v2/contacts/autocomplete | Get contacts autocomplete suggestions
[**get_contacts_by_list_id**](TextMagicApi.md#get_contacts_by_list_id) | **GET** /api/v2/lists/{id}/contacts | Get all contacts in a list
[**get_countries**](TextMagicApi.md#get_countries) | **GET** /api/v2/countries | Get countries
[**get_current_user**](TextMagicApi.md#get_current_user) | **GET** /api/v2/user | Get current account information
[**get_custom_field**](TextMagicApi.md#get_custom_field) | **GET** /api/v2/customfields/{id} | Get the details of a specific custom field
[**get_custom_fields**](TextMagicApi.md#get_custom_fields) | **GET** /api/v2/customfields | Get all custom fields
[**get_dedicated_number**](TextMagicApi.md#get_dedicated_number) | **GET** /api/v2/numbers/{id} | Get the details of a specific dedicated number
[**get_favorites**](TextMagicApi.md#get_favorites) | **GET** /api/v2/contacts/favorite | Get favorite contacts and lists
[**get_inbound_message**](TextMagicApi.md#get_inbound_message) | **GET** /api/v2/replies/{id} | Get a single inbound message
[**get_inbound_messages_notification_settings**](TextMagicApi.md#get_inbound_messages_notification_settings) | **GET** /api/v2/user/notification/inbound | Get inbound messages notification settings
[**get_invoices**](TextMagicApi.md#get_invoices) | **GET** /api/v2/invoices | Get all invoices
[**get_list**](TextMagicApi.md#get_list) | **GET** /api/v2/lists/{id} | Get the details of a specific list
[**get_list_contacts_ids**](TextMagicApi.md#get_list_contacts_ids) | **GET** /api/v2/lists/{id}/contacts/ids | Get all contact IDs in a list
[**get_lists**](TextMagicApi.md#get_lists) | **GET** /api/v2/lists | Get all lists
[**get_lists_of_contact**](TextMagicApi.md#get_lists_of_contact) | **GET** /api/v2/contacts/{id}/lists | Get a contact&#39;s lists
[**get_message_preview**](TextMagicApi.md#get_message_preview) | **GET** /api/v2/messages/preview | Preview message
[**get_message_price**](TextMagicApi.md#get_message_price) | **GET** /api/v2/messages/price/normalized | Check message price
[**get_message_session**](TextMagicApi.md#get_message_session) | **GET** /api/v2/sessions/{id} | Get a session&#x60;s details
[**get_message_session_stat**](TextMagicApi.md#get_message_session_stat) | **GET** /api/v2/sessions/{id}/stat | Get a session&#x60;s statistics
[**get_messages_by_session_id**](TextMagicApi.md#get_messages_by_session_id) | **GET** /api/v2/sessions/{id}/messages | Get a session&#x60;s messages
[**get_messaging_counters**](TextMagicApi.md#get_messaging_counters) | **GET** /api/v2/stats/messaging/data | Get sent/received messages counters values
[**get_messaging_stat**](TextMagicApi.md#get_messaging_stat) | **GET** /api/v2/stats/messaging | Get messaging statistics
[**get_outbound_message**](TextMagicApi.md#get_outbound_message) | **GET** /api/v2/messages/{id} | Get a single message
[**get_outbound_messages_history**](TextMagicApi.md#get_outbound_messages_history) | **GET** /api/v2/history | Get history
[**get_scheduled_message**](TextMagicApi.md#get_scheduled_message) | **GET** /api/v2/schedules/{id} | Get a single scheduled message
[**get_sender_id**](TextMagicApi.md#get_sender_id) | **GET** /api/v2/senderids/{id} | Get the details of a specific Sender ID
[**get_sender_ids**](TextMagicApi.md#get_sender_ids) | **GET** /api/v2/senderids | Get all your approved Sender IDs
[**get_sender_settings**](TextMagicApi.md#get_sender_settings) | **GET** /api/v2/sender/settings/normalized | Get current sender settings
[**get_spending_stat**](TextMagicApi.md#get_spending_stat) | **GET** /api/v2/stats/spending | Get spending statistics
[**get_subaccount**](TextMagicApi.md#get_subaccount) | **GET** /api/v2/subaccounts/{id} | Get sub-account information
[**get_subaccounts**](TextMagicApi.md#get_subaccounts) | **GET** /api/v2/subaccounts | Get a sub-accounts list
[**get_subaccounts_with_tokens**](TextMagicApi.md#get_subaccounts_with_tokens) | **POST** /api/v2/subaccounts/tokens/list | Get all sub-accounts with their REST API tokens associated with a specified app name
[**get_template**](TextMagicApi.md#get_template) | **GET** /api/v2/templates/{id} | Get a template&#x60;s details
[**get_timezones**](TextMagicApi.md#get_timezones) | **GET** /api/v2/timezones | Get timezones
[**get_unread_messages_total**](TextMagicApi.md#get_unread_messages_total) | **GET** /api/v2/chats/unread/count | Get unread messages number
[**get_unsubscribed_contact**](TextMagicApi.md#get_unsubscribed_contact) | **GET** /api/v2/unsubscribers/{id} | Get the details of a specific unsubscribed contact
[**get_unsubscribers**](TextMagicApi.md#get_unsubscribers) | **GET** /api/v2/unsubscribers | Get all unsubscribed contacts
[**get_user_dedicated_numbers**](TextMagicApi.md#get_user_dedicated_numbers) | **GET** /api/v2/numbers | Get all your dedicated numbers
[**import_contacts**](TextMagicApi.md#import_contacts) | **POST** /api/v2/contacts/import/normalized | Import contacts
[**invite_subaccount**](TextMagicApi.md#invite_subaccount) | **POST** /api/v2/subaccounts | Invite a new sub-account
[**mark_chats_read_bulk**](TextMagicApi.md#mark_chats_read_bulk) | **POST** /api/v2/chats/read/bulk | Mark chats as read (bulk)
[**mark_chats_unread_bulk**](TextMagicApi.md#mark_chats_unread_bulk) | **POST** /api/v2/chats/unread/bulk | Mark chats as unread (bulk)
[**mute_chat**](TextMagicApi.md#mute_chat) | **POST** /api/v2/chats/mute | Mute chat sounds
[**mute_chats_bulk**](TextMagicApi.md#mute_chats_bulk) | **POST** /api/v2/chats/mute/bulk | Mute chats (bulk)
[**ping**](TextMagicApi.md#ping) | **GET** /api/v2/ping | Ping
[**reopen_chats_bulk**](TextMagicApi.md#reopen_chats_bulk) | **POST** /api/v2/chats/reopen/bulk | Reopen chats (bulk)
[**request_new_subaccount_token**](TextMagicApi.md#request_new_subaccount_token) | **POST** /api/v2/subaccounts/tokens | Request a new REST API token for sub-account
[**request_sender_id**](TextMagicApi.md#request_sender_id) | **POST** /api/v2/senderids | Apply for a new Sender ID
[**search_chats**](TextMagicApi.md#search_chats) | **GET** /api/v2/chats/search | Find chats by message text
[**search_chats_by_ids**](TextMagicApi.md#search_chats_by_ids) | **GET** /api/v2/chats/search/ids | Find chats (bulk)
[**search_chats_by_receipent**](TextMagicApi.md#search_chats_by_receipent) | **GET** /api/v2/chats/search/recipients | Find chats by recipient
[**search_contacts**](TextMagicApi.md#search_contacts) | **GET** /api/v2/contacts/search | Find contacts by given criteria
[**search_inbound_messages**](TextMagicApi.md#search_inbound_messages) | **GET** /api/v2/replies/search | Find inbound messages
[**search_lists**](TextMagicApi.md#search_lists) | **GET** /api/v2/lists/search | Find lists by given criteria
[**search_outbound_messages**](TextMagicApi.md#search_outbound_messages) | **GET** /api/v2/messages/search | Find messages
[**search_scheduled_messages**](TextMagicApi.md#search_scheduled_messages) | **GET** /api/v2/schedules/search | Find scheduled messages
[**search_templates**](TextMagicApi.md#search_templates) | **GET** /api/v2/templates/search | Find templates by criteria
[**send_message**](TextMagicApi.md#send_message) | **POST** /api/v2/messages | Send message
[**send_phone_verification_code_tfa**](TextMagicApi.md#send_phone_verification_code_tfa) | **POST** /api/v2/verify | Step 1: Send a verification code 
[**set_chat_status**](TextMagicApi.md#set_chat_status) | **POST** /api/v2/chats/status | Change chat status
[**unblock_contact**](TextMagicApi.md#unblock_contact) | **POST** /api/v2/contacts/unblock | Unblock a contact by phone number
[**unblock_contacts_bulk**](TextMagicApi.md#unblock_contacts_bulk) | **POST** /api/v2/contacts/unblock/bulk | Unblock contacts (bulk)
[**unmute_chats_bulk**](TextMagicApi.md#unmute_chats_bulk) | **POST** /api/v2/chats/unmute/bulk | Unmute chats (bulk)
[**unsubscribe_contact**](TextMagicApi.md#unsubscribe_contact) | **POST** /api/v2/unsubscribers | Manually unsubscribe a contact
[**update_balance_notification_settings**](TextMagicApi.md#update_balance_notification_settings) | **PUT** /api/v2/user/notification/balance | Update balance notification settings
[**update_callback_settings**](TextMagicApi.md#update_callback_settings) | **PUT** /api/v2/callback/settings | Update callback URL settings
[**update_chat_desktop_notification_settings**](TextMagicApi.md#update_chat_desktop_notification_settings) | **PUT** /api/v2/user/desktop/notification | Update chat desktop notification settings
[**update_contact**](TextMagicApi.md#update_contact) | **PUT** /api/v2/contacts/{id}/normalized | Edit a contact
[**update_contact_note**](TextMagicApi.md#update_contact_note) | **PUT** /api/v2/notes/{id} | Update a contact note
[**update_current_user**](TextMagicApi.md#update_current_user) | **PUT** /api/v2/user | Edit current account info
[**update_custom_field**](TextMagicApi.md#update_custom_field) | **PUT** /api/v2/customfields/{id} | Edit a custom field
[**update_custom_field_value**](TextMagicApi.md#update_custom_field_value) | **PUT** /api/v2/customfields/{id}/update | Edit the custom field value of a specified contact
[**update_inbound_messages_notification_settings**](TextMagicApi.md#update_inbound_messages_notification_settings) | **PUT** /api/v2/user/notification/inbound | Update inbound messages notification settings
[**update_list**](TextMagicApi.md#update_list) | **PUT** /api/v2/lists/{id} | Edit a list
[**update_sender_setting**](TextMagicApi.md#update_sender_setting) | **PUT** /api/v2/sender/settings | Change sender settings
[**update_template**](TextMagicApi.md#update_template) | **PUT** /api/v2/templates/{id} | Update a template
[**upload_avatar**](TextMagicApi.md#upload_avatar) | **POST** /api/v2/user/avatar | Upload an avatar
[**upload_contact_avatar**](TextMagicApi.md#upload_contact_avatar) | **POST** /api/v2/contacts/{id}/avatar | Upload an avatar
[**upload_list_avatar**](TextMagicApi.md#upload_list_avatar) | **POST** /api/v2/lists/{id}/avatar | Add an avatar for a list
[**upload_message_attachment**](TextMagicApi.md#upload_message_attachment) | **POST** /api/v2/messages/attachment | Upload message attachment


# **assign_contacts_to_list**
> ResourceLinkResponse assign_contacts_to_list(assign_contacts_to_list_input_object, id)

Assign contacts to a list

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/assignContactsToList\" target=\"_blank\">Try in sandbox</a><br>> Unlike all other PUT requests, this command does not need old contact IDs to be submitted. For example, if you have a list with contacts 150, 151 and 152 and you want to add contact ID 153, you only need to submit 153 as a parameter of PUT /api/v2/lists/{id}/contacts. 

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
assign_contacts_to_list_input_object = TextMagic.AssignContactsToListInputObject() # AssignContactsToListInputObject | 
id = 1 # int | 

try:
    # Assign contacts to a list
    api_response = api_instance.assign_contacts_to_list(assign_contacts_to_list_input_object, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->assign_contacts_to_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assign_contacts_to_list_input_object** | [**AssignContactsToListInputObject**](AssignContactsToListInputObject.md)|  | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **block_contact**
> ResourceLinkResponse block_contact(block_contact_input_object)

Block a contact by phone number

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/blockContact\" target=\"_blank\">Try in sandbox</a><br>Block a contact from inbound and outbound communication by phone number.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
block_contact_input_object = TextMagic.BlockContactInputObject() # BlockContactInputObject | 

try:
    # Block a contact by phone number
    api_response = api_instance.block_contact(block_contact_input_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->block_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_contact_input_object** | [**BlockContactInputObject**](BlockContactInputObject.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buy_dedicated_number**
> buy_dedicated_number(buy_dedicated_number_input_object)

Buy a dedicated number

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/undefined/buyDedicatedNumber\" target=\"_blank\">Try in sandbox</a><br>To buy a dedicated number, you first need to find an available number matching your criteria using the `/api/v2/numbers/available` command described above.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
buy_dedicated_number_input_object = TextMagic.BuyDedicatedNumberInputObject() # BuyDedicatedNumberInputObject | 

try:
    # Buy a dedicated number
    api_instance.buy_dedicated_number(buy_dedicated_number_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->buy_dedicated_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buy_dedicated_number_input_object** | [**BuyDedicatedNumberInputObject**](BuyDedicatedNumberInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_verification**
> cancel_verification(verify_id)

Cancel verification process

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Two-factor%20authentication/cancelVerification\" target=\"_blank\">Try in sandbox</a><br>You can cancel the verification not earlier than 30 seconds after the initial request.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
verify_id = '\"123e4567-e89b-12d3-a456-426655440000\"' # str | The verifyId that you received in Step 1.

try:
    # Cancel verification process
    api_instance.cancel_verification(verify_id)
except ApiException as e:
    print("Exception when calling TextMagicApi->cancel_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_id** | **str**| The verifyId that you received in Step 1. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_phone_verification_code_tfa**
> check_phone_verification_code_tfa(check_phone_verification_code_input_object)

Step 2: Check the verification code 

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Two-factor%20authentication/checkPhoneVerificationCodeTFA\" target=\"_blank\">Try in sandbox</a><br>Check received code from user with the code which was actually sent.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
check_phone_verification_code_input_object = TextMagic.CheckPhoneVerificationCodeInputObject() # CheckPhoneVerificationCodeInputObject | 

try:
    # Step 2: Check the verification code 
    api_instance.check_phone_verification_code_tfa(check_phone_verification_code_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->check_phone_verification_code_tfa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_phone_verification_code_input_object** | [**CheckPhoneVerificationCodeInputObject**](CheckPhoneVerificationCodeInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_and_assign_contacts_to_list**
> ResourceLinkResponse clear_and_assign_contacts_to_list(clear_and_assign_contacts_to_list_input_object, id)

Reset list members to the specified contacts

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/clearAndAssignContactsToList\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
clear_and_assign_contacts_to_list_input_object = TextMagic.ClearAndAssignContactsToListInputObject() # ClearAndAssignContactsToListInputObject | 
id = 1 # int | 

try:
    # Reset list members to the specified contacts
    api_response = api_instance.clear_and_assign_contacts_to_list(clear_and_assign_contacts_to_list_input_object, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->clear_and_assign_contacts_to_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clear_and_assign_contacts_to_list_input_object** | [**ClearAndAssignContactsToListInputObject**](ClearAndAssignContactsToListInputObject.md)|  | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_chats_bulk**
> close_chats_bulk(close_chats_bulk_input_object)

Close chats (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/closeChatsBulk\" target=\"_blank\">Try in sandbox</a><br>Close chats by chat IDs or close all chats

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
close_chats_bulk_input_object = TextMagic.CloseChatsBulkInputObject() # CloseChatsBulkInputObject | 

try:
    # Close chats (bulk)
    api_instance.close_chats_bulk(close_chats_bulk_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->close_chats_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **close_chats_bulk_input_object** | [**CloseChatsBulkInputObject**](CloseChatsBulkInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_read_chats**
> close_read_chats()

Close read chats

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/closeReadChats\" target=\"_blank\">Try in sandbox</a><br>Close all chats that have no unread messages.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Close read chats
    api_instance.close_read_chats()
except ApiException as e:
    print("Exception when calling TextMagicApi->close_read_chats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_subaccount**
> close_subaccount(id)

Close sub-account

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sub-Accounts/closeSubaccount\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Close sub-account
    api_instance.close_subaccount(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->close_subaccount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact**
> ResourceLinkResponse create_contact(create_contact_input_object)

Add a new contact

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/createContact\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
create_contact_input_object = TextMagic.CreateContactInputObject() # CreateContactInputObject | 

try:
    # Add a new contact
    api_response = api_instance.create_contact(create_contact_input_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->create_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contact_input_object** | [**CreateContactInputObject**](CreateContactInputObject.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact_note**
> ResourceLinkResponse create_contact_note(create_contact_note_input_object, id)

Create a new contact note

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contact%20Notes/createContactNote\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
create_contact_note_input_object = TextMagic.CreateContactNoteInputObject() # CreateContactNoteInputObject | 
id = 1 # int | 

try:
    # Create a new contact note
    api_response = api_instance.create_contact_note(create_contact_note_input_object, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->create_contact_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contact_note_input_object** | [**CreateContactNoteInputObject**](CreateContactNoteInputObject.md)|  | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_field**
> ResourceLinkResponse create_custom_field(create_custom_field_input_object)

Add a new custom field

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Custom%20Fields/createCustomField\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
create_custom_field_input_object = TextMagic.CreateCustomFieldInputObject() # CreateCustomFieldInputObject | 

try:
    # Add a new custom field
    api_response = api_instance.create_custom_field(create_custom_field_input_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->create_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_custom_field_input_object** | [**CreateCustomFieldInputObject**](CreateCustomFieldInputObject.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_list**
> ResourceLinkResponse create_list(create_list_input_object)

Create a new list

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/createList\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
create_list_input_object = TextMagic.CreateListInputObject() # CreateListInputObject | 

try:
    # Create a new list
    api_response = api_instance.create_list(create_list_input_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->create_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_list_input_object** | [**CreateListInputObject**](CreateListInputObject.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template**
> ResourceLinkResponse create_template(create_template_input_object)

Create a template

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Templates/createTemplate\" target=\"_blank\">Try in sandbox</a><br>There are times when creating a new template makes sense (such as when targeting specific clients or improving your business strategies).  You can create new SMS templates for marketing purposes or SMS templates for business campaigns. 

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
create_template_input_object = TextMagic.CreateTemplateInputObject() # CreateTemplateInputObject | 

try:
    # Create a template
    api_response = api_instance.create_template(create_template_input_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->create_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_template_input_object** | [**CreateTemplateInputObject**](CreateTemplateInputObject.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_contacts**
> delete_all_contacts()

Delete contacts (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/deleteAllContacts\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Delete contacts (bulk)
    api_instance.delete_all_contacts()
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_all_contacts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_outbound_messages**
> delete_all_outbound_messages()

Delete all messages

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Send%0A/deleteAllOutboundMessages\" target=\"_blank\">Try in sandbox</a><br>Delete all messages.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Delete all messages
    api_instance.delete_all_outbound_messages()
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_all_outbound_messages: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_avatar**
> delete_avatar()

Delete an avatar

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Account/deleteAvatar\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Delete an avatar
    api_instance.delete_avatar()
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_avatar: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chat_messages**
> delete_chat_messages(delete_chat_messages_bulk_input_object, id)

Delete chat messages by ID(s)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/deleteChatMessages\" target=\"_blank\">Try in sandbox</a><br>Delete messages from chat by given message IDs.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_chat_messages_bulk_input_object = TextMagic.DeleteChatMessagesBulkInputObject() # DeleteChatMessagesBulkInputObject | 
id = 1 # int | 

try:
    # Delete chat messages by ID(s)
    api_instance.delete_chat_messages(delete_chat_messages_bulk_input_object, id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_chat_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_chat_messages_bulk_input_object** | [**DeleteChatMessagesBulkInputObject**](DeleteChatMessagesBulkInputObject.md)|  | 
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chats_bulk**
> delete_chats_bulk(delete_chats_bulk_input_object)

Delete chats (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/deleteChatsBulk\" target=\"_blank\">Try in sandbox</a><br>Delete chats by given IDs or delete all chats.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_chats_bulk_input_object = TextMagic.DeleteChatsBulkInputObject() # DeleteChatsBulkInputObject | 

try:
    # Delete chats (bulk)
    api_instance.delete_chats_bulk(delete_chats_bulk_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_chats_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_chats_bulk_input_object** | [**DeleteChatsBulkInputObject**](DeleteChatsBulkInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> delete_contact(id)

Delete a contact

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/deleteContact\" target=\"_blank\">Try in sandbox</a><br>> This command removes your contact completely. If it was assigned or saved to a shared list, it will disappear from there too. If you only need to remove a contact from selected lists, use the Contact assignment command in the Lists section instead, rather than deleting the contact. 

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a contact
    api_instance.delete_contact(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_avatar**
> delete_contact_avatar(id)

Delete an avatar

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/deleteContactAvatar\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete an avatar
    api_instance.delete_contact_avatar(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_contact_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_note**
> delete_contact_note(id)

Delete a contact note

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contact%20Notes/deleteContactNote\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a contact note
    api_instance.delete_contact_note(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_contact_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_notes_bulk**
> delete_contact_notes_bulk(id, delete_contact_notes_bulk_input_object)

Delete contact notes (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contact%20Notes/deleteContactNotesBulk\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
delete_contact_notes_bulk_input_object = TextMagic.DeleteContactNotesBulkInputObject() # DeleteContactNotesBulkInputObject | 

try:
    # Delete contact notes (bulk)
    api_instance.delete_contact_notes_bulk(id, delete_contact_notes_bulk_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_contact_notes_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **delete_contact_notes_bulk_input_object** | [**DeleteContactNotesBulkInputObject**](DeleteContactNotesBulkInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contacts_by_ids**
> delete_contacts_by_ids(delete_contacts_by_ids_input_object)

Delete contacts by IDs (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/deleteContactsByIds\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_contacts_by_ids_input_object = TextMagic.DeleteContactsByIdsInputObject() # DeleteContactsByIdsInputObject | 

try:
    # Delete contacts by IDs (bulk)
    api_instance.delete_contacts_by_ids(delete_contacts_by_ids_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_contacts_by_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_contacts_by_ids_input_object** | [**DeleteContactsByIdsInputObject**](DeleteContactsByIdsInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contacts_from_list**
> delete_contacts_from_list(delete_contacs_from_list_object, id)

Unassign contacts from a list

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/deleteContactsFromList\" target=\"_blank\">Try in sandbox</a><br>> When you remove contacts from a specific list, they will be deleted permanently, unless they are first saved in another list. 

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_contacs_from_list_object = TextMagic.DeleteContacsFromListObject() # DeleteContacsFromListObject | 
id = 1 # int | 

try:
    # Unassign contacts from a list
    api_instance.delete_contacts_from_list(delete_contacs_from_list_object, id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_contacts_from_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_contacs_from_list_object** | [**DeleteContacsFromListObject**](DeleteContacsFromListObject.md)|  | 
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field**
> delete_custom_field(id)

Delete a custom field

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Custom%20Fields/deleteCustomField\" target=\"_blank\">Try in sandbox</a><br>> When a custom field is deleted, all the information that was added to contacts under this custom field will also be lost. 

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a custom field
    api_instance.delete_custom_field(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dedicated_number**
> delete_dedicated_number(id)

Cancel a dedicated number subscription

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/undefined/deleteDedicatedNumber\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Cancel a dedicated number subscription
    api_instance.delete_dedicated_number(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_dedicated_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inbound_message**
> delete_inbound_message(id)

Delete a single inbound message

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Receive%0A/deleteInboundMessage\" target=\"_blank\">Try in sandbox</a><br>> Note: deleted inbound messages will disappear from TextMagic Online, chats, and any other place they are referenced.  So, be careful! 

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | The unique numeric ID for the inbound message.

try:
    # Delete a single inbound message
    api_instance.delete_inbound_message(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_inbound_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique numeric ID for the inbound message. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inbound_messages_bulk**
> delete_inbound_messages_bulk(delete_inbound_messages_bulk_input_object)

Delete inbound messages (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Receive%0A/deleteInboundMessagesBulk\" target=\"_blank\">Try in sandbox</a><br>> Note: deleted inbound messages will disappear from TextMagic Online, chats, and any other place they are referenced.  So, be careful! 

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_inbound_messages_bulk_input_object = TextMagic.DeleteInboundMessagesBulkInputObject() # DeleteInboundMessagesBulkInputObject | 

try:
    # Delete inbound messages (bulk)
    api_instance.delete_inbound_messages_bulk(delete_inbound_messages_bulk_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_inbound_messages_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_inbound_messages_bulk_input_object** | [**DeleteInboundMessagesBulkInputObject**](DeleteInboundMessagesBulkInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list**
> delete_list(id)

Delete a list

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/deleteList\" target=\"_blank\">Try in sandbox</a><br>This command has no parameters. If successful, this command will return the standard delete response (204 No Content); otherwise, a standard error response will be returned.  When you delete a list, the contacts in it are deleted as well, unless they were saved in another list.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a list
    api_instance.delete_list(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list_avatar**
> delete_list_avatar(id)

Delete an avatar for a list

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/deleteListAvatar\" target=\"_blank\">Try in sandbox</a><br>Delete an avatar for a list

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete an avatar for a list
    api_instance.delete_list_avatar(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_list_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list_contacts_bulk**
> delete_list_contacts_bulk(delete_list_contacts_bulk_input_object, id)

Delete contacts from a list (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/deleteListContactsBulk\" target=\"_blank\">Try in sandbox</a><br>Delete contacts from a list (bulk)

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_list_contacts_bulk_input_object = TextMagic.DeleteListContactsBulkInputObject() # DeleteListContactsBulkInputObject | 
id = 1 # int | 

try:
    # Delete contacts from a list (bulk)
    api_instance.delete_list_contacts_bulk(delete_list_contacts_bulk_input_object, id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_list_contacts_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_list_contacts_bulk_input_object** | [**DeleteListContactsBulkInputObject**](DeleteListContactsBulkInputObject.md)|  | 
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lists_bulk**
> delete_lists_bulk(delete_lists_bulk_input_object)

Delete lists (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/deleteListsBulk\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_lists_bulk_input_object = TextMagic.DeleteListsBulkInputObject() # DeleteListsBulkInputObject | 

try:
    # Delete lists (bulk)
    api_instance.delete_lists_bulk(delete_lists_bulk_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_lists_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_lists_bulk_input_object** | [**DeleteListsBulkInputObject**](DeleteListsBulkInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message_session**
> delete_message_session(id)

Delete a session

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sessions/deleteMessageSession\" target=\"_blank\">Try in sandbox</a><br>Delete a message session, together with all nested messages. > You will not be refunded for any deleted sent sessions. 

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a session
    api_instance.delete_message_session(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_message_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message_sessions_bulk**
> delete_message_sessions_bulk(delete_message_sessions_bulk_input_object)

Delete sessions (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sessions/deleteMessageSessionsBulk\" target=\"_blank\">Try in sandbox</a><br>Delete message sessions, together with all nested messages, by given ID(s) or delete all message sessions.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_message_sessions_bulk_input_object = TextMagic.DeleteMessageSessionsBulkInputObject() # DeleteMessageSessionsBulkInputObject | 

try:
    # Delete sessions (bulk)
    api_instance.delete_message_sessions_bulk(delete_message_sessions_bulk_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_message_sessions_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_message_sessions_bulk_input_object** | [**DeleteMessageSessionsBulkInputObject**](DeleteMessageSessionsBulkInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_outbound_message**
> delete_outbound_message(id)

Delete message

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Send%0A/deleteOutboundMessage\" target=\"_blank\">Try in sandbox</a><br>Delete a single message.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete message
    api_instance.delete_outbound_message(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_outbound_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_outbound_messages_bulk**
> delete_outbound_messages_bulk(delete_outbound_messages_bulk_input_object)

Delete messages (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Send%0A/deleteOutboundMessagesBulk\" target=\"_blank\">Try in sandbox</a><br>Delete outbound messages by the given ID(s) or delete all outbound messages.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_outbound_messages_bulk_input_object = TextMagic.DeleteOutboundMessagesBulkInputObject() # DeleteOutboundMessagesBulkInputObject | 

try:
    # Delete messages (bulk)
    api_instance.delete_outbound_messages_bulk(delete_outbound_messages_bulk_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_outbound_messages_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_outbound_messages_bulk_input_object** | [**DeleteOutboundMessagesBulkInputObject**](DeleteOutboundMessagesBulkInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_message**
> delete_scheduled_message(id)

Delete a single scheduled message

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Schedule%0A/deleteScheduledMessage\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a single scheduled message
    api_instance.delete_scheduled_message(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_scheduled_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_messages_bulk**
> delete_scheduled_messages_bulk(delete_scheduled_messages_bulk_input_object)

Delete scheduled messages (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Schedule%0A/deleteScheduledMessagesBulk\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_scheduled_messages_bulk_input_object = TextMagic.DeleteScheduledMessagesBulkInputObject() # DeleteScheduledMessagesBulkInputObject | 

try:
    # Delete scheduled messages (bulk)
    api_instance.delete_scheduled_messages_bulk(delete_scheduled_messages_bulk_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_scheduled_messages_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_scheduled_messages_bulk_input_object** | [**DeleteScheduledMessagesBulkInputObject**](DeleteScheduledMessagesBulkInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sender_id**
> delete_sender_id(id)

Delete a Sender ID

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sender%20IDs/deleteSenderId\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a Sender ID
    api_instance.delete_sender_id(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_sender_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> delete_template(id)

Delete a template

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Templates/deleteTemplate\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Delete a template
    api_instance.delete_template(id)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_templates_bulk**
> delete_templates_bulk(delete_templates_bulk_input_object)

Delete templates (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Templates/deleteTemplatesBulk\" target=\"_blank\">Try in sandbox</a><br>Delete templates by given IDs or delete all templates.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
delete_templates_bulk_input_object = TextMagic.DeleteTemplatesBulkInputObject() # DeleteTemplatesBulkInputObject | 

try:
    # Delete templates (bulk)
    api_instance.delete_templates_bulk(delete_templates_bulk_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->delete_templates_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_templates_bulk_input_object** | [**DeleteTemplatesBulkInputObject**](DeleteTemplatesBulkInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_carrier_lookup**
> DoCarrierLookupResponse do_carrier_lookup(phone, country=country)

Carrier Lookup

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lookup/doCarrierLookup\" target=\"_blank\">Try in sandbox</a><br>This API call allows you to retrieve additional information about a phone number: region-specific phone number formatting, carrier, phone type (landline/mobile) and country information.  > Numbers must be checked one by one. You cannot check multiple numbers in one request.   

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
phone = '\"447860021130\"' # str | Phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) or in [National format](https://en.wikipedia.org/wiki/National_conventions_for_writing_telephone_numbers). 
country = '\"GB\"' # str | This option must be specified only if the phone number is in a **[National format](https://en.wikipedia.org/wiki/National_conventions_for_writing_telephone_numbers)**.  (optional)

try:
    # Carrier Lookup
    api_response = api_instance.do_carrier_lookup(phone, country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->do_carrier_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**| Phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) or in [National format](https://en.wikipedia.org/wiki/National_conventions_for_writing_telephone_numbers).  | 
 **country** | **str**| This option must be specified only if the phone number is in a **[National format](https://en.wikipedia.org/wiki/National_conventions_for_writing_telephone_numbers)**.  | [optional] 

### Return type

[**DoCarrierLookupResponse**](DoCarrierLookupResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_email_lookup**
> DoEmailLookupResponse do_email_lookup(email)

Email Lookup

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lookup/doEmailLookup\" target=\"_blank\">Try in sandbox</a><br>To get more details about an email address or to check whether it is a valid email or not, you can use the Email Lookup command. To upload and check emails in bulk, please use our [Web app](https://my.textmagic.com/online/email-lookup/).  This API call allows you to retrieve additional information about an email address, such as mailbox detection, syntax checks, DNS validation, deliverability status, and many more helpful values (see the table below).  > Emails must be checked one by one. You cannot check multiple emails in one request. To upload and check emails in bulk, please use our [Web app](https://my.textmagic.com/online/email-lookup/).

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
email = '\"john@sample.com\"' # str | Email address.

try:
    # Email Lookup
    api_response = api_instance.do_email_lookup(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->do_email_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email address. | 

### Return type

[**DoEmailLookupResponse**](DoEmailLookupResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_bulk_sessions**
> GetAllBulkSessionsPaginatedResponse get_all_bulk_sessions(page=page, limit=limit)

Get all bulk sessions

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Send%0A/getAllBulkSessions\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)

try:
    # Get all bulk sessions
    api_response = api_instance.get_all_bulk_sessions(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_all_bulk_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]

### Return type

[**GetAllBulkSessionsPaginatedResponse**](GetAllBulkSessionsPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_chats**
> GetAllChatsPaginatedResponse get_all_chats(status=status, page=page, limit=limit, order_by=order_by, voice=voice, flat=flat)

Get all chats

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/getAllChats\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
status = '\"a\"' # str | Fetch only (a)ctive, (c)losed or (d)eleted chats. (optional)
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
order_by = 'id' # str | Order results by some field. Default is id. (optional) (default to id)
voice = 0 # int | Fetch results with voice calls. (optional) (default to 0)
flat = 0 # int | Should additional contact info be included? (optional) (default to 0)

try:
    # Get all chats
    api_response = api_instance.get_all_chats(status=status, page=page, limit=limit, order_by=order_by, voice=voice, flat=flat)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_all_chats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Fetch only (a)ctive, (c)losed or (d)eleted chats. | [optional] 
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **order_by** | **str**| Order results by some field. Default is id. | [optional] [default to id]
 **voice** | **int**| Fetch results with voice calls. | [optional] [default to 0]
 **flat** | **int**| Should additional contact info be included? | [optional] [default to 0]

### Return type

[**GetAllChatsPaginatedResponse**](GetAllChatsPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_inbound_messages**
> GetAllInboundMessagesPaginatedResponse get_all_inbound_messages(page=page, limit=limit, order_by=order_by, direction=direction)

Get all inbound messages

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Receive%0A/getAllInboundMessages\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
order_by = 'id' # str | Order results by some field. Default is id. (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc. (optional) (default to desc)

try:
    # Get all inbound messages
    api_response = api_instance.get_all_inbound_messages(page=page, limit=limit, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_all_inbound_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **order_by** | **str**| Order results by some field. Default is id. | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc. | [optional] [default to desc]

### Return type

[**GetAllInboundMessagesPaginatedResponse**](GetAllInboundMessagesPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_message_sessions**
> GetAllMessageSessionsPaginatedResponse get_all_message_sessions(page=page, limit=limit)

Get all sessions

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sessions/getAllMessageSessions\" target=\"_blank\">Try in sandbox</a><br>Get all message sending sessions. > This list contains all of your sessions, including those which were sent but not via API 

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)

try:
    # Get all sessions
    api_response = api_instance.get_all_message_sessions(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_all_message_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]

### Return type

[**GetAllMessageSessionsPaginatedResponse**](GetAllMessageSessionsPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_outbound_messages**
> GetAllOutboundMessagesPaginatedResponse get_all_outbound_messages(page=page, limit=limit, last_id=last_id)

Get all messages

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Send%0A/getAllOutboundMessages\" target=\"_blank\">Try in sandbox</a><br>Get all user oubound messages.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
last_id = 56 # int | Filter results by ID, selecting all values lesser than the specified ID. Note that the \\'page\\' parameter is ignored when \\'lastId\\' is specified. (optional)

try:
    # Get all messages
    api_response = api_instance.get_all_outbound_messages(page=page, limit=limit, last_id=last_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_all_outbound_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **last_id** | **int**| Filter results by ID, selecting all values lesser than the specified ID. Note that the \\&#39;page\\&#39; parameter is ignored when \\&#39;lastId\\&#39; is specified. | [optional] 

### Return type

[**GetAllOutboundMessagesPaginatedResponse**](GetAllOutboundMessagesPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_scheduled_messages**
> GetAllScheduledMessagesPaginatedResponse get_all_scheduled_messages(page=page, limit=limit, status=status, order_by=order_by, direction=direction)

Get all scheduled messages

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Schedule%0A/getAllScheduledMessages\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
status = 'x' # str | Fetch schedules with a specific status: a - actual, c - completed, x - all. (optional) (default to x)
order_by = 'id' # str | Order results by some field. Default is id. (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc. (optional) (default to desc)

try:
    # Get all scheduled messages
    api_response = api_instance.get_all_scheduled_messages(page=page, limit=limit, status=status, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_all_scheduled_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **status** | **str**| Fetch schedules with a specific status: a - actual, c - completed, x - all. | [optional] [default to x]
 **order_by** | **str**| Order results by some field. Default is id. | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc. | [optional] [default to desc]

### Return type

[**GetAllScheduledMessagesPaginatedResponse**](GetAllScheduledMessagesPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_templates**
> GetAllTemplatesPaginatedResponse get_all_templates(page=page, limit=limit)

Get all templates

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Templates/getAllTemplates\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional)
limit = 10 # int | The number of results per page. (optional)

try:
    # Get all templates
    api_response = api_instance.get_all_templates(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_all_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] 
 **limit** | **int**| The number of results per page. | [optional] 

### Return type

[**GetAllTemplatesPaginatedResponse**](GetAllTemplatesPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_dedicated_numbers**
> GetAvailableDedicatedNumbersResponse get_available_dedicated_numbers(country, prefix=prefix, tollfree=tollfree)

Find dedicated numbers available for purchase

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/undefined/getAvailableDedicatedNumbers\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
country = '\"GB\"' # str | The 2-letter dedicated number country ISO code.
prefix = 447155 # int | Desired number prefix. Should include the country code (i.e. 447 for UK phone number format). Leave blank to get all the available numbers for the specified country. (optional)
tollfree = 0 # int | Should we show only tollfree numbers (tollfree available only for US). (optional) (default to 0)

try:
    # Find dedicated numbers available for purchase
    api_response = api_instance.get_available_dedicated_numbers(country, prefix=prefix, tollfree=tollfree)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_available_dedicated_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| The 2-letter dedicated number country ISO code. | 
 **prefix** | **int**| Desired number prefix. Should include the country code (i.e. 447 for UK phone number format). Leave blank to get all the available numbers for the specified country. | [optional] 
 **tollfree** | **int**| Should we show only tollfree numbers (tollfree available only for US). | [optional] [default to 0]

### Return type

[**GetAvailableDedicatedNumbersResponse**](GetAvailableDedicatedNumbersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_sender_setting_options**
> GetAvailableSenderSettingOptionsResponse get_available_sender_setting_options(country=country)

Get available sender settings

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Overview/getAvailableSenderSettingOptions\" target=\"_blank\">Try in sandbox</a><br>Get all available sender setting options which can be used in the \"from\" parameter of the POST messages method.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
country = '\"US\"' # str | The 2-letter ISO country ID. If not specified, it returns all the available sender settings. (optional)

try:
    # Get available sender settings
    api_response = api_instance.get_available_sender_setting_options(country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_available_sender_setting_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| The 2-letter ISO country ID. If not specified, it returns all the available sender settings. | [optional] 

### Return type

[**GetAvailableSenderSettingOptionsResponse**](GetAvailableSenderSettingOptionsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_notification_options**
> GetBalanceNotificationOptionsResponse get_balance_notification_options()

Returns the list of available balance options which can be used as a bound to determine when to send email to user with low balance notification. See https://my.textmagic.com/online/account/notifications/balance

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/undefined/getBalanceNotificationOptions\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Returns the list of available balance options which can be used as a bound to determine when to send email to user with low balance notification. See https://my.textmagic.com/online/account/notifications/balance
    api_response = api_instance.get_balance_notification_options()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_balance_notification_options: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBalanceNotificationOptionsResponse**](GetBalanceNotificationOptionsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_notification_settings**
> GetBalanceNotificationSettingsResponse get_balance_notification_settings()

Get balance notification settings

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/undefined/getBalanceNotificationSettings\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Get balance notification settings
    api_response = api_instance.get_balance_notification_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_balance_notification_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBalanceNotificationSettingsResponse**](GetBalanceNotificationSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blocked_contacts**
> GetBlockedContactsPaginatedResponse get_blocked_contacts(page=page, limit=limit, query=query, order_by=order_by, direction=direction)

Get blocked contacts

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/getBlockedContacts\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
query = 'query_example' # str | Find blocked contacts by specified search query. (optional)
order_by = 'id' # str | Order results by some field. Default is id. (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc. (optional) (default to desc)

try:
    # Get blocked contacts
    api_response = api_instance.get_blocked_contacts(page=page, limit=limit, query=query, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_blocked_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **query** | **str**| Find blocked contacts by specified search query. | [optional] 
 **order_by** | **str**| Order results by some field. Default is id. | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc. | [optional] [default to desc]

### Return type

[**GetBlockedContactsPaginatedResponse**](GetBlockedContactsPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bulk_session**
> BulkSession get_bulk_session(id)

Get bulk session status

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Send%0A/getBulkSession\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get bulk session status
    api_response = api_instance.get_bulk_session(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_bulk_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**BulkSession**](BulkSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_callback_settings**
> GetCallbackSettingsResponse get_callback_settings()

Fetch callback URL settings

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/undefined/getCallbackSettings\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Fetch callback URL settings
    api_response = api_instance.get_callback_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_callback_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetCallbackSettingsResponse**](GetCallbackSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat**
> Chat get_chat(id)

Get a single chat

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/getChat\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single chat
    api_response = api_instance.get_chat(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Chat**](Chat.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_by_phone**
> Chat get_chat_by_phone(phone, upsert=upsert, reopen=reopen)

Find chats by phone

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/getChatByPhone\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
phone = '\"447860021130\"' # str | 
upsert = 0 # int | Create a new chat if not found. (optional) (default to 0)
reopen = 0 # int | Reopen chat if found or do not change status. (optional) (default to 0)

try:
    # Find chats by phone
    api_response = api_instance.get_chat_by_phone(phone, upsert=upsert, reopen=reopen)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_chat_by_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  | 
 **upsert** | **int**| Create a new chat if not found. | [optional] [default to 0]
 **reopen** | **int**| Reopen chat if found or do not change status. | [optional] [default to 0]

### Return type

[**Chat**](Chat.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_messages**
> GetChatMessagesPaginatedResponse get_chat_messages(id, page=page, limit=limit, query=query, start=start, end=end, direction=direction, voice=voice)

Get chat messages

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/getChatMessages\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
query = 'query_example' # str | Find messages by specified search query. (optional)
start = 56 # int | Return messages since specified timestamp only. (optional)
end = 56 # int | Return messages up to specified timestamp only. (optional)
direction = 'desc' # str | Order direction. Default is desc. (optional) (default to desc)
voice = 0 # int | Fetch results with voice calls. (optional) (default to 0)

try:
    # Get chat messages
    api_response = api_instance.get_chat_messages(id, page=page, limit=limit, query=query, start=start, end=end, direction=direction, voice=voice)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_chat_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **query** | **str**| Find messages by specified search query. | [optional] 
 **start** | **int**| Return messages since specified timestamp only. | [optional] 
 **end** | **int**| Return messages up to specified timestamp only. | [optional] 
 **direction** | **str**| Order direction. Default is desc. | [optional] [default to desc]
 **voice** | **int**| Fetch results with voice calls. | [optional] [default to 0]

### Return type

[**GetChatMessagesPaginatedResponse**](GetChatMessagesPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact**
> Contact get_contact(id)

Get the details of a specific contact

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/getContact\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | Contact ID.

try:
    # Get the details of a specific contact
    api_response = api_instance.get_contact(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Contact ID. | 

### Return type

[**Contact**](Contact.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_by_phone**
> Contact get_contact_by_phone(phone)

Get the details of a specific contact by phone number

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/getContactByPhone\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
phone = '\"447860021130\"' # str | 

try:
    # Get the details of a specific contact by phone number
    api_response = api_instance.get_contact_by_phone(phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contact_by_phone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**|  | 

### Return type

[**Contact**](Contact.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_if_blocked**
> Contact get_contact_if_blocked(phone)

Check if a phone number is blocked

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/getContactIfBlocked\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
phone = '\"447860021130\"' # str | Phone number to check.

try:
    # Check if a phone number is blocked
    api_response = api_instance.get_contact_if_blocked(phone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contact_if_blocked: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phone** | **str**| Phone number to check. | 

### Return type

[**Contact**](Contact.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_import_session_progress**
> GetContactImportSessionProgressResponse get_contact_import_session_progress(id)

Check import progress

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/getContactImportSessionProgress\" target=\"_blank\">Try in sandbox</a><br>Get contact import session progress.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Check import progress
    api_response = api_instance.get_contact_import_session_progress(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contact_import_session_progress: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetContactImportSessionProgressResponse**](GetContactImportSessionProgressResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_note**
> ContactNote get_contact_note(id)

Get a contact note

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contact%20Notes/getContactNote\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a contact note
    api_response = api_instance.get_contact_note(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contact_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ContactNote**](ContactNote.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_notes**
> GetContactNotesPaginatedResponse get_contact_notes(id, page=page, limit=limit)

Fetch notes assigned to a given contact

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contact%20Notes/getContactNotes\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)

try:
    # Fetch notes assigned to a given contact
    api_response = api_instance.get_contact_notes(id, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contact_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]

### Return type

[**GetContactNotesPaginatedResponse**](GetContactNotesPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts**
> GetContactsPaginatedResponse get_contacts(page=page, limit=limit, shared=shared, order_by=order_by, direction=direction)

Get all contacts

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/getContacts\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
shared = 0 # int | Should shared contacts be included? (optional) (default to 0)
order_by = 'id' # str | Order results by some field. Default is id. (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc. (optional) (default to desc)

try:
    # Get all contacts
    api_response = api_instance.get_contacts(page=page, limit=limit, shared=shared, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **shared** | **int**| Should shared contacts be included? | [optional] [default to 0]
 **order_by** | **str**| Order results by some field. Default is id. | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc. | [optional] [default to desc]

### Return type

[**GetContactsPaginatedResponse**](GetContactsPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts_autocomplete**
> GetContactsAutocompleteResponse get_contacts_autocomplete(query, limit=limit, lists=lists)

Get contacts autocomplete suggestions

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/getContactsAutocomplete\" target=\"_blank\">Try in sandbox</a><br>Get contacts autocomplete suggestions by given search terms.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
query = '\"A\"' # str | Find recipients by specified search query.
limit = 10 # int | The number of results per page. (optional) (default to 10)
lists = 0 # int | Should lists be returned or not? (optional) (default to 0)

try:
    # Get contacts autocomplete suggestions
    api_response = api_instance.get_contacts_autocomplete(query, limit=limit, lists=lists)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contacts_autocomplete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Find recipients by specified search query. | 
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **lists** | **int**| Should lists be returned or not? | [optional] [default to 0]

### Return type

[**GetContactsAutocompleteResponse**](GetContactsAutocompleteResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts_by_list_id**
> GetContactsByListIdPaginatedResponse get_contacts_by_list_id(id, page=page, limit=limit, order_by=order_by, direction=direction)

Get all contacts in a list

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/getContactsByListId\" target=\"_blank\">Try in sandbox</a><br>A useful synonym for the \"contacts/search\" command with the provided \"listId\" parameter.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | Given group ID.
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
order_by = 'id' # str | Order results by some field. Default is id. (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc. (optional) (default to desc)

try:
    # Get all contacts in a list
    api_response = api_instance.get_contacts_by_list_id(id, page=page, limit=limit, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_contacts_by_list_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Given group ID. | 
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **order_by** | **str**| Order results by some field. Default is id. | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc. | [optional] [default to desc]

### Return type

[**GetContactsByListIdPaginatedResponse**](GetContactsByListIdPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries**
> GetCountriesResponse get_countries()

Get countries

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Timezones%20and%20Countries/getCountries\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Get countries
    api_response = api_instance.get_countries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_countries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetCountriesResponse**](GetCountriesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> User get_current_user()

Get current account information

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Account/getCurrentUser\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Get current account information
    api_response = api_instance.get_current_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_current_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field**
> UserCustomField get_custom_field(id)

Get the details of a specific custom field

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Custom%20Fields/getCustomField\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get the details of a specific custom field
    api_response = api_instance.get_custom_field(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UserCustomField**](UserCustomField.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_fields**
> GetCustomFieldsPaginatedResponse get_custom_fields(page=page, limit=limit)

Get all custom fields

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Custom%20Fields/getCustomFields\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)

try:
    # Get all custom fields
    api_response = api_instance.get_custom_fields(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_custom_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]

### Return type

[**GetCustomFieldsPaginatedResponse**](GetCustomFieldsPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dedicated_number**
> UsersInbound get_dedicated_number(id)

Get the details of a specific dedicated number

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/undefined/getDedicatedNumber\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get the details of a specific dedicated number
    api_response = api_instance.get_dedicated_number(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_dedicated_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UsersInbound**](UsersInbound.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorites**
> GetFavoritesPaginatedResponse get_favorites(page=page, limit=limit, query=query)

Get favorite contacts and lists

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/getFavorites\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
query = '\"A\"' # str | Find contacts or lists by specified search query. (optional)

try:
    # Get favorite contacts and lists
    api_response = api_instance.get_favorites(page=page, limit=limit, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_favorites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **query** | **str**| Find contacts or lists by specified search query. | [optional] 

### Return type

[**GetFavoritesPaginatedResponse**](GetFavoritesPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_message**
> MessageIn get_inbound_message(id)

Get a single inbound message

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Receive%0A/getInboundMessage\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1782832 # int | The unique numeric ID for the inbound message.

try:
    # Get a single inbound message
    api_response = api_instance.get_inbound_message(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_inbound_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The unique numeric ID for the inbound message. | 

### Return type

[**MessageIn**](MessageIn.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_messages_notification_settings**
> GetInboundMessagesNotificationSettingsResponse get_inbound_messages_notification_settings()

Get inbound messages notification settings

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/undefined/getInboundMessagesNotificationSettings\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Get inbound messages notification settings
    api_response = api_instance.get_inbound_messages_notification_settings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_inbound_messages_notification_settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetInboundMessagesNotificationSettingsResponse**](GetInboundMessagesNotificationSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> GetInvoicesPaginatedResponse get_invoices(page=page, limit=limit)

Get all invoices

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Invoices/getInvoices\" target=\"_blank\">Try in sandbox</a><br>With the TextMagic API, you can check the invoices and transactions for your account.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)

try:
    # Get all invoices
    api_response = api_instance.get_invoices(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_invoices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]

### Return type

[**GetInvoicesPaginatedResponse**](GetInvoicesPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list**
> List get_list(id)

Get the details of a specific list

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/getList\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get the details of a specific list
    api_response = api_instance.get_list(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**List**](List.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_contacts_ids**
> GetListContactsIdsResponse get_list_contacts_ids(id)

Get all contact IDs in a list

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/getListContactsIds\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get all contact IDs in a list
    api_response = api_instance.get_list_contacts_ids(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_list_contacts_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**GetListContactsIdsResponse**](GetListContactsIdsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lists**
> GetListsPaginatedResponse get_lists(page=page, limit=limit, order_by=order_by, direction=direction, favorite_only=favorite_only, only_mine=only_mine)

Get all lists

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/getLists\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | The current fetched page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
order_by = 'id' # str | Order results by some field. Default is id. (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc. (optional) (default to desc)
favorite_only = 0 # int | Return only favorited lists. (optional) (default to 0)
only_mine = 0 # int | Return only current user lists. (optional) (default to 0)

try:
    # Get all lists
    api_response = api_instance.get_lists(page=page, limit=limit, order_by=order_by, direction=direction, favorite_only=favorite_only, only_mine=only_mine)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The current fetched page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **order_by** | **str**| Order results by some field. Default is id. | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc. | [optional] [default to desc]
 **favorite_only** | **int**| Return only favorited lists. | [optional] [default to 0]
 **only_mine** | **int**| Return only current user lists. | [optional] [default to 0]

### Return type

[**GetListsPaginatedResponse**](GetListsPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lists_of_contact**
> GetListsOfContactPaginatedResponse get_lists_of_contact(id, page=page, limit=limit)

Get a contact's lists

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/getListsOfContact\" target=\"_blank\">Try in sandbox</a><br>Get all the lists in which a contact is included.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)

try:
    # Get a contact's lists
    api_response = api_instance.get_lists_of_contact(id, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_lists_of_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]

### Return type

[**GetListsOfContactPaginatedResponse**](GetListsOfContactPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_preview**
> GetMessagePreviewResponse get_message_preview(text=text, template_id=template_id, sending_time=sending_time, sending_date_time=sending_date_time, sending_timezone=sending_timezone, contacts=contacts, lists=lists, phones=phones, cut_extra=cut_extra, parts_count=parts_count, reference_id=reference_id, _from=_from, rule=rule, create_chat=create_chat, tts=tts, local=local, local_country=local_country)

Preview message

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Send%0A/getMessagePreview\" target=\"_blank\">Try in sandbox</a><br>Get a messages preview (with tags merged) of up to 100 messages per session.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
text = '\"Test message test\"' # str | Message text. Required if **template_id** is not set. (optional)
template_id = 1 # int | Template used instead of message text. Required if **text** is not set. (optional)
sending_time = 1565606455 # int | DEPRECATED, consider using sendingDateTime and sendingTimezone parameters instead: Optional (required with rrule set). Message sending time is in unix timestamp format. Default is now. (optional)
sending_date_time = '\"2020-05-27 13:02:33\"' # str | Sending time is in Y-m-d H:i:s format (e.g. 2016-05-27 13:02:33). This time is relative to the sendingTimezone. (optional)
sending_timezone = '\"America/Buenos_Aires\"' # str | The ID or ISO-name of the timezone used for sending when the sendingDateTime parameter is set, e.g. if you specify sendingDateTime = \\\"2016-05-27 13:02:33\\\" and sendingTimezone = \\\"America/Buenos_Aires\\\", your message will be sent on May 27, 2016 13:02:33 Buenos Aires time, or 16:02:33 UTC. Default is the account timezone. (optional)
contacts = '\"1,2,3,4\"' # str | Comma-separated array of contact resources id message will be sent to. (optional)
lists = '\"1,2,3,4\"' # str | Comma-separated array of list resources id message will be sent to. (optional)
phones = '\"447860021130,447860021131\"' # str | Comma-separated array of E.164 phone numbers message will be sent to. (optional)
cut_extra = 0 # int | Should sending method cut extra characters which not fit supplied partsCount or return 400 Bad request response instead. (optional) (default to 0)
parts_count = 6 # int | Maximum message parts count (TextMagic allows sending of 1 to 6 message parts). (optional) (default to 6)
reference_id = 1 # int | Custom message reference id which can be used in your application infrastructure. (optional)
_from = '\"Test Sender ID\"' # str | One of the allowed Sender ID (phone number or alphanumeric sender ID). If the specified Sender ID is not allowed for some destinations, a fallback default Sender ID will be used to ensure delivery. See [Get timezones](http://docs.textmagictesting.com/#tag/Sender-IDs). (optional)
rule = '\"FREQ=YEARLY;BYMONTH=1;BYMONTHDAY=1;COUNT=1\"' # str | An iCal RRULE parameter to create recurrent scheduled messages. When used, sendingTime is mandatory as the start point of sending. See https://www.textmagic.com/free-tools/rrule-generator for format details. (optional)
create_chat = 0 # int | Should the sending method try to create new Chat(if not exist) with specified recipients? (optional) (default to 0)
tts = 0 # int | Send Text-to-Speech message. (optional) (default to 0)
local = 0 # int | Treat phone numbers passed in the \\'phones\\' field as local. (optional) (default to 0)
local_country = '\"US\"' # str | The 2-letter ISO country code for local phone numbers, used when \\'local\\' is set to true. Default is the account country. (optional)

try:
    # Preview message
    api_response = api_instance.get_message_preview(text=text, template_id=template_id, sending_time=sending_time, sending_date_time=sending_date_time, sending_timezone=sending_timezone, contacts=contacts, lists=lists, phones=phones, cut_extra=cut_extra, parts_count=parts_count, reference_id=reference_id, _from=_from, rule=rule, create_chat=create_chat, tts=tts, local=local, local_country=local_country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_message_preview: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| Message text. Required if **template_id** is not set. | [optional] 
 **template_id** | **int**| Template used instead of message text. Required if **text** is not set. | [optional] 
 **sending_time** | **int**| DEPRECATED, consider using sendingDateTime and sendingTimezone parameters instead: Optional (required with rrule set). Message sending time is in unix timestamp format. Default is now. | [optional] 
 **sending_date_time** | **str**| Sending time is in Y-m-d H:i:s format (e.g. 2016-05-27 13:02:33). This time is relative to the sendingTimezone. | [optional] 
 **sending_timezone** | **str**| The ID or ISO-name of the timezone used for sending when the sendingDateTime parameter is set, e.g. if you specify sendingDateTime &#x3D; \\\&quot;2016-05-27 13:02:33\\\&quot; and sendingTimezone &#x3D; \\\&quot;America/Buenos_Aires\\\&quot;, your message will be sent on May 27, 2016 13:02:33 Buenos Aires time, or 16:02:33 UTC. Default is the account timezone. | [optional] 
 **contacts** | **str**| Comma-separated array of contact resources id message will be sent to. | [optional] 
 **lists** | **str**| Comma-separated array of list resources id message will be sent to. | [optional] 
 **phones** | **str**| Comma-separated array of E.164 phone numbers message will be sent to. | [optional] 
 **cut_extra** | **int**| Should sending method cut extra characters which not fit supplied partsCount or return 400 Bad request response instead. | [optional] [default to 0]
 **parts_count** | **int**| Maximum message parts count (TextMagic allows sending of 1 to 6 message parts). | [optional] [default to 6]
 **reference_id** | **int**| Custom message reference id which can be used in your application infrastructure. | [optional] 
 **_from** | **str**| One of the allowed Sender ID (phone number or alphanumeric sender ID). If the specified Sender ID is not allowed for some destinations, a fallback default Sender ID will be used to ensure delivery. See [Get timezones](http://docs.textmagictesting.com/#tag/Sender-IDs). | [optional] 
 **rule** | **str**| An iCal RRULE parameter to create recurrent scheduled messages. When used, sendingTime is mandatory as the start point of sending. See https://www.textmagic.com/free-tools/rrule-generator for format details. | [optional] 
 **create_chat** | **int**| Should the sending method try to create new Chat(if not exist) with specified recipients? | [optional] [default to 0]
 **tts** | **int**| Send Text-to-Speech message. | [optional] [default to 0]
 **local** | **int**| Treat phone numbers passed in the \\&#39;phones\\&#39; field as local. | [optional] [default to 0]
 **local_country** | **str**| The 2-letter ISO country code for local phone numbers, used when \\&#39;local\\&#39; is set to true. Default is the account country. | [optional] 

### Return type

[**GetMessagePreviewResponse**](GetMessagePreviewResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_price**
> GetMessagePriceResponse get_message_price(include_blocked=include_blocked, text=text, template_id=template_id, sending_time=sending_time, sending_date_time=sending_date_time, sending_timezone=sending_timezone, contacts=contacts, lists=lists, phones=phones, cut_extra=cut_extra, parts_count=parts_count, reference_id=reference_id, _from=_from, rule=rule, create_chat=create_chat, tts=tts, local=local, local_country=local_country)

Check message price

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Send%0A/getMessagePrice\" target=\"_blank\">Try in sandbox</a><br>Check pricing for a new outbound message.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
include_blocked = 0 # int | Should we show the pricing for blocked contacts? (optional) (default to 0)
text = '\"Test message test\"' # str | Message text. Required if the **template_id** is not set. (optional)
template_id = 1 # int | Template used instead of message text. Required if the **text** is not set. (optional)
sending_time = 1565606455 # int | DEPRECATED, consider using the sendingDateTime and sendingTimezone parameters instead: optional (required with rrule set). Message sending time is in unix timestamp format. Default is now. (optional)
sending_date_time = '\"2020-05-27 13:02:33\"' # str | Sending time is in Y-m-d H:i:s format (e.g. 2016-05-27 13:02:33). This time is relative to the sendingTimezone. (optional)
sending_timezone = '\"America/Buenos_Aires\"' # str | The ID or ISO-name of the timezone used for sending when sendingDateTime parameter is set, e.g. if you specify sendingDateTime = \\\"2016-05-27 13:02:33\\\" and sendingTimezone = \\\"America/Buenos_Aires\\\", your message will be sent on May 27, 2016 13:02:33 Buenos Aires time, or 16:02:33 UTC. Default is the account timezone. (optional)
contacts = '\"1,2,3,4\"' # str | Comma-separated array of contact resources id message will be sent to. (optional)
lists = '\"1,2,3,4\"' # str | Comma-separated array of list resources id message will be sent to. (optional)
phones = '\"447860021130,447860021131\"' # str | Comma-separated array of E.164 phone numbers message will be sent to. (optional)
cut_extra = 0 # int | Should sending method cut extra characters which not fit supplied partsCount or return 400 Bad request response instead. (optional) (default to 0)
parts_count = 6 # int | Maximum message parts count (TextMagic allows sending 1 to 6 message parts). (optional) (default to 6)
reference_id = 1 # int | Custom message reference id which can be used in your application infrastructure. (optional)
_from = '\"Test Sender ID\"' # str | One of the allowed Sender ID (phone number or alphanumeric sender ID). If the specified Sender ID is not allowed for some destinations, a fallback default Sender ID will be used to ensure delivery. See [Get timezones](http://docs.textmagictesting.com/#tag/Sender-IDs). (optional)
rule = '\"FREQ=YEARLY;BYMONTH=1;BYMONTHDAY=1;COUNT=1\"' # str | An iCal RRULE parameter to create recurrent scheduled messages. When used, sendingTime is mandatory as the start point of sending. See https://www.textmagic.com/free-tools/rrule-generator for format details. (optional)
create_chat = 0 # int | Should the sending method try to create new Chat (if not exist) with specified recipients? (optional) (default to 0)
tts = 0 # int | Send a Text-to-Speech message. (optional) (default to 0)
local = 0 # int | Treat phone numbers passed in the \\'phones\\' field as local. (optional) (default to 0)
local_country = '\"US\"' # str | The 2-letter ISO country code for local phone numbers, used when \\'local\\' is set to true. Default is the account country. (optional)

try:
    # Check message price
    api_response = api_instance.get_message_price(include_blocked=include_blocked, text=text, template_id=template_id, sending_time=sending_time, sending_date_time=sending_date_time, sending_timezone=sending_timezone, contacts=contacts, lists=lists, phones=phones, cut_extra=cut_extra, parts_count=parts_count, reference_id=reference_id, _from=_from, rule=rule, create_chat=create_chat, tts=tts, local=local, local_country=local_country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_message_price: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_blocked** | **int**| Should we show the pricing for blocked contacts? | [optional] [default to 0]
 **text** | **str**| Message text. Required if the **template_id** is not set. | [optional] 
 **template_id** | **int**| Template used instead of message text. Required if the **text** is not set. | [optional] 
 **sending_time** | **int**| DEPRECATED, consider using the sendingDateTime and sendingTimezone parameters instead: optional (required with rrule set). Message sending time is in unix timestamp format. Default is now. | [optional] 
 **sending_date_time** | **str**| Sending time is in Y-m-d H:i:s format (e.g. 2016-05-27 13:02:33). This time is relative to the sendingTimezone. | [optional] 
 **sending_timezone** | **str**| The ID or ISO-name of the timezone used for sending when sendingDateTime parameter is set, e.g. if you specify sendingDateTime &#x3D; \\\&quot;2016-05-27 13:02:33\\\&quot; and sendingTimezone &#x3D; \\\&quot;America/Buenos_Aires\\\&quot;, your message will be sent on May 27, 2016 13:02:33 Buenos Aires time, or 16:02:33 UTC. Default is the account timezone. | [optional] 
 **contacts** | **str**| Comma-separated array of contact resources id message will be sent to. | [optional] 
 **lists** | **str**| Comma-separated array of list resources id message will be sent to. | [optional] 
 **phones** | **str**| Comma-separated array of E.164 phone numbers message will be sent to. | [optional] 
 **cut_extra** | **int**| Should sending method cut extra characters which not fit supplied partsCount or return 400 Bad request response instead. | [optional] [default to 0]
 **parts_count** | **int**| Maximum message parts count (TextMagic allows sending 1 to 6 message parts). | [optional] [default to 6]
 **reference_id** | **int**| Custom message reference id which can be used in your application infrastructure. | [optional] 
 **_from** | **str**| One of the allowed Sender ID (phone number or alphanumeric sender ID). If the specified Sender ID is not allowed for some destinations, a fallback default Sender ID will be used to ensure delivery. See [Get timezones](http://docs.textmagictesting.com/#tag/Sender-IDs). | [optional] 
 **rule** | **str**| An iCal RRULE parameter to create recurrent scheduled messages. When used, sendingTime is mandatory as the start point of sending. See https://www.textmagic.com/free-tools/rrule-generator for format details. | [optional] 
 **create_chat** | **int**| Should the sending method try to create new Chat (if not exist) with specified recipients? | [optional] [default to 0]
 **tts** | **int**| Send a Text-to-Speech message. | [optional] [default to 0]
 **local** | **int**| Treat phone numbers passed in the \\&#39;phones\\&#39; field as local. | [optional] [default to 0]
 **local_country** | **str**| The 2-letter ISO country code for local phone numbers, used when \\&#39;local\\&#39; is set to true. Default is the account country. | [optional] 

### Return type

[**GetMessagePriceResponse**](GetMessagePriceResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_session**
> MessageSession get_message_session(id)

Get a session`s details

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sessions/getMessageSession\" target=\"_blank\">Try in sandbox</a><br>Get a specific session’s details.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | Session ID.

try:
    # Get a session`s details
    api_response = api_instance.get_message_session(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_message_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Session ID. | 

### Return type

[**MessageSession**](MessageSession.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_session_stat**
> GetMessageSessionStatResponse get_message_session_stat(id, include_deleted=include_deleted)

Get a session`s statistics

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sessions/getMessageSessionStat\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
include_deleted = 0 # int | Search also in deleted messages. (optional) (default to 0)

try:
    # Get a session`s statistics
    api_response = api_instance.get_message_session_stat(id, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_message_session_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **include_deleted** | **int**| Search also in deleted messages. | [optional] [default to 0]

### Return type

[**GetMessageSessionStatResponse**](GetMessageSessionStatResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages_by_session_id**
> GetMessagesBySessionIdPaginatedResponse get_messages_by_session_id(id, page=page, limit=limit, statuses=statuses, include_deleted=include_deleted)

Get a session`s messages

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sessions/getMessagesBySessionId\" target=\"_blank\">Try in sandbox</a><br>A useful synonym for the \"messages/search\" command with the provided \"sessionId\" parameter.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
statuses = 'statuses_example' # str | Find messages by status. (optional)
include_deleted = 0 # int | Search also in deleted messages. (optional) (default to 0)

try:
    # Get a session`s messages
    api_response = api_instance.get_messages_by_session_id(id, page=page, limit=limit, statuses=statuses, include_deleted=include_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_messages_by_session_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **statuses** | **str**| Find messages by status. | [optional] 
 **include_deleted** | **int**| Search also in deleted messages. | [optional] [default to 0]

### Return type

[**GetMessagesBySessionIdPaginatedResponse**](GetMessagesBySessionIdPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messaging_counters**
> GetMessagingCountersResponse get_messaging_counters()

Get sent/received messages counters values

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Statistics/getMessagingCounters\" target=\"_blank\">Try in sandbox</a><br>Get total contacts, sent messages and received messages counters values.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Get sent/received messages counters values
    api_response = api_instance.get_messaging_counters()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_messaging_counters: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMessagingCountersResponse**](GetMessagingCountersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messaging_stat**
> GetMessagingStatResponse get_messaging_stat(by=by, start=start, end=end)

Get messaging statistics

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Statistics/getMessagingStat\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
by = 'off' # str | *   **off** - to get total values per specified time interval; *   **day** - to show values grouped by day; *   **month** - to show values grouped by month; *   **year** - to show values grouped by year.  (optional) (default to off)
start = 1430438400 # int | Time period start in [UNIX timestamp](https://en.wikipedia.org/wiki/Unix_time) format. The default is 7 days prior.  (optional)
end = 1431648000 # int | Time period start in [UNIX timestamp](https://en.wikipedia.org/wiki/Unix_time) format. The default is today.  (optional)

try:
    # Get messaging statistics
    api_response = api_instance.get_messaging_stat(by=by, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_messaging_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **by** | **str**| *   **off** - to get total values per specified time interval; *   **day** - to show values grouped by day; *   **month** - to show values grouped by month; *   **year** - to show values grouped by year.  | [optional] [default to off]
 **start** | **int**| Time period start in [UNIX timestamp](https://en.wikipedia.org/wiki/Unix_time) format. The default is 7 days prior.  | [optional] 
 **end** | **int**| Time period start in [UNIX timestamp](https://en.wikipedia.org/wiki/Unix_time) format. The default is today.  | [optional] 

### Return type

[**GetMessagingStatResponse**](GetMessagingStatResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_message**
> MessageOut get_outbound_message(id)

Get a single message

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Send%0A/getOutboundMessage\" target=\"_blank\">Try in sandbox</a><br>Get a single outgoing message.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single message
    api_response = api_instance.get_outbound_message(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_outbound_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MessageOut**](MessageOut.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_messages_history**
> GetOutboundMessagesHistoryPaginatedResponse get_outbound_messages_history(limit=limit, last_id=last_id, query=query, order_by=order_by, direction=direction)

Get history

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Send%0A/getOutboundMessagesHistory\" target=\"_blank\">Try in sandbox</a><br>Get the outbound messages history.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
limit = 10 # int | The number of results per page. (optional) (default to 10)
last_id = 56 # int | Filter results by ID, selecting all values lesser than the specified ID. (optional)
query = 'query_example' # str | Find message by specified search query. (optional)
order_by = 'id' # str | Order results by some field. Default is id. (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc. (optional) (default to desc)

try:
    # Get history
    api_response = api_instance.get_outbound_messages_history(limit=limit, last_id=last_id, query=query, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_outbound_messages_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **last_id** | **int**| Filter results by ID, selecting all values lesser than the specified ID. | [optional] 
 **query** | **str**| Find message by specified search query. | [optional] 
 **order_by** | **str**| Order results by some field. Default is id. | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc. | [optional] [default to desc]

### Return type

[**GetOutboundMessagesHistoryPaginatedResponse**](GetOutboundMessagesHistoryPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_message**
> MessagesIcs get_scheduled_message(id)

Get a single scheduled message

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Schedule%0A/getScheduledMessage\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a single scheduled message
    api_response = api_instance.get_scheduled_message(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_scheduled_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MessagesIcs**](MessagesIcs.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender_id**
> SenderId get_sender_id(id)

Get the details of a specific Sender ID

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sender%20IDs/getSenderId\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get the details of a specific Sender ID
    api_response = api_instance.get_sender_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_sender_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**SenderId**](SenderId.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender_ids**
> GetSenderIdsPaginatedResponse get_sender_ids(page=page, limit=limit)

Get all your approved Sender IDs

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sender%20IDs/getSenderIds\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)

try:
    # Get all your approved Sender IDs
    api_response = api_instance.get_sender_ids(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_sender_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]

### Return type

[**GetSenderIdsPaginatedResponse**](GetSenderIdsPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender_settings**
> GetSenderSettingsResponse get_sender_settings(country=country)

Get current sender settings

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Overview/getSenderSettings\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
country = '\"US\"' # str | Return sender settings enabled for sending to a specified country. Should be 2 upper-case characters. (optional)

try:
    # Get current sender settings
    api_response = api_instance.get_sender_settings(country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_sender_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Return sender settings enabled for sending to a specified country. Should be 2 upper-case characters. | [optional] 

### Return type

[**GetSenderSettingsResponse**](GetSenderSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spending_stat**
> GetSpendingStatPaginatedResponse get_spending_stat(page=page, limit=limit, start=start, end=end)

Get spending statistics

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Statistics/getSpendingStat\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
start = '\"2018-11-11 11:11\"' # str | Time period start in [UNIX timestamp](https://en.wikipedia.org/wiki/Unix_time) format. The default is 7 days prior.  (optional)
end = '\"2019-11-11 11:11\"' # str | Time period start in [UNIX timestamp](https://en.wikipedia.org/wiki/Unix_time) format. The default is today.  (optional)

try:
    # Get spending statistics
    api_response = api_instance.get_spending_stat(page=page, limit=limit, start=start, end=end)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_spending_stat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **start** | **str**| Time period start in [UNIX timestamp](https://en.wikipedia.org/wiki/Unix_time) format. The default is 7 days prior.  | [optional] 
 **end** | **str**| Time period start in [UNIX timestamp](https://en.wikipedia.org/wiki/Unix_time) format. The default is today.  | [optional] 

### Return type

[**GetSpendingStatPaginatedResponse**](GetSpendingStatPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subaccount**
> User get_subaccount(id)

Get sub-account information

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sub-Accounts/getSubaccount\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get sub-account information
    api_response = api_instance.get_subaccount(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_subaccount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subaccounts**
> User get_subaccounts(page=page, limit=limit)

Get a sub-accounts list

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sub-Accounts/getSubaccounts\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)

try:
    # Get a sub-accounts list
    api_response = api_instance.get_subaccounts(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_subaccounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subaccounts_with_tokens**
> GetSubaccountsWithTokensResponse get_subaccounts_with_tokens(get_subaccounts_with_tokens_input_object, page=page, limit=limit)

Get all sub-accounts with their REST API tokens associated with a specified app name

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sub-Accounts/getSubaccountsWithTokens\" target=\"_blank\">Try in sandbox</a><br>Get all sub-accounts with their REST API tokens associated with specified app name. When more than one token related to app name, last key will be returned.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
get_subaccounts_with_tokens_input_object = TextMagic.GetSubaccountsWithTokensInputObject() # GetSubaccountsWithTokensInputObject | 
page = 1 # float | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)

try:
    # Get all sub-accounts with their REST API tokens associated with a specified app name
    api_response = api_instance.get_subaccounts_with_tokens(get_subaccounts_with_tokens_input_object, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_subaccounts_with_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_subaccounts_with_tokens_input_object** | [**GetSubaccountsWithTokensInputObject**](GetSubaccountsWithTokensInputObject.md)|  | 
 **page** | **float**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]

### Return type

[**GetSubaccountsWithTokensResponse**](GetSubaccountsWithTokensResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> MessageTemplate get_template(id)

Get a template`s details

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Templates/getTemplate\" target=\"_blank\">Try in sandbox</a><br>Get a single template.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get a template`s details
    api_response = api_instance.get_template(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**MessageTemplate**](MessageTemplate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timezones**
> GetTimezonesResponse get_timezones(full=full)

Get timezones

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Timezones%20and%20Countries/getTimezones\" target=\"_blank\">Try in sandbox</a><br>Return all available timezone IDs

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
full = 0 # int | Return full info about timezones in array (0 or 1). Default is 0. (optional) (default to 0)

try:
    # Get timezones
    api_response = api_instance.get_timezones(full=full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_timezones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full** | **int**| Return full info about timezones in array (0 or 1). Default is 0. | [optional] [default to 0]

### Return type

[**GetTimezonesResponse**](GetTimezonesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unread_messages_total**
> GetUnreadMessagesTotalResponse get_unread_messages_total()

Get unread messages number

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/getUnreadMessagesTotal\" target=\"_blank\">Try in sandbox</a><br>Get the total amount of unread messages in the current user chats.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Get unread messages number
    api_response = api_instance.get_unread_messages_total()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_unread_messages_total: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetUnreadMessagesTotalResponse**](GetUnreadMessagesTotalResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unsubscribed_contact**
> UnsubscribedContact get_unsubscribed_contact(id)

Get the details of a specific unsubscribed contact

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/getUnsubscribedContact\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 

try:
    # Get the details of a specific unsubscribed contact
    api_response = api_instance.get_unsubscribed_contact(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_unsubscribed_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**UnsubscribedContact**](UnsubscribedContact.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unsubscribers**
> GetUnsubscribersPaginatedResponse get_unsubscribers(page=page, limit=limit)

Get all unsubscribed contacts

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/getUnsubscribers\" target=\"_blank\">Try in sandbox</a><br>When one of your message recipients sends a request with one of the [STOP-words](https://www.textmagic.com/sms-stop-command/), they will be immediately opted-out of your send lists and their contact status will change to an unsubscribed contact. To retrieve information on all contacts who have unsubscribed status, use: 

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)

try:
    # Get all unsubscribed contacts
    api_response = api_instance.get_unsubscribers(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_unsubscribers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]

### Return type

[**GetUnsubscribersPaginatedResponse**](GetUnsubscribersPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_dedicated_numbers**
> GetUserDedicatedNumbersPaginatedResponse get_user_dedicated_numbers(page=page, limit=limit, survey_id=survey_id)

Get all your dedicated numbers

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/undefined/getUserDedicatedNumbers\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
survey_id = 56 # int | Fetch only those numbers that are ready for the survey. (optional)

try:
    # Get all your dedicated numbers
    api_response = api_instance.get_user_dedicated_numbers(page=page, limit=limit, survey_id=survey_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_user_dedicated_numbers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **survey_id** | **int**| Fetch only those numbers that are ready for the survey. | [optional] 

### Return type

[**GetUserDedicatedNumbersPaginatedResponse**](GetUserDedicatedNumbersPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_contacts**
> ResourceLinkResponse import_contacts(file, column, list_id=list_id, list_name=list_name)

Import contacts

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/importContacts\" target=\"_blank\">Try in sandbox</a><br>Import contacts from the CSV, XLS or XLSX file.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
file = '/path/to/file.txt' # file | File containing contacts in csv or xls(x) formats.
column = '\"0:firstName;1:lastName;3:phone;4:email\"' # str | Import file column mapping. The string must contain sub-strings of mapping in format `columnNumber:field` glued by `;`. For example: `0:firstName;1:lastName;3:phone;4:email` where the value before `:` is a number of the column in the file, and the value after `:` is a field of the newly created contact or the ID of a custom field. Numbers of columns begin from zero. Allowed built-in contact fields are: `firstName`, `lastName`, `phone`, `email`. Existing of `phone` mapping is required. 
list_id = 443 # int | List that ID contacts will be imported to. Ignored if `listName` is specified.  (optional)
list_name = '\"A new list\"' # str | List name. This list will be created during import. If such name is already taken, an ordinal (1, 2, ...) will be added to the end. Ignored if `listId` is specified.  (optional)

try:
    # Import contacts
    api_response = api_instance.import_contacts(file, column, list_id=list_id, list_name=list_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->import_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| File containing contacts in csv or xls(x) formats. | 
 **column** | **str**| Import file column mapping. The string must contain sub-strings of mapping in format &#x60;columnNumber:field&#x60; glued by &#x60;;&#x60;. For example: &#x60;0:firstName;1:lastName;3:phone;4:email&#x60; where the value before &#x60;:&#x60; is a number of the column in the file, and the value after &#x60;:&#x60; is a field of the newly created contact or the ID of a custom field. Numbers of columns begin from zero. Allowed built-in contact fields are: &#x60;firstName&#x60;, &#x60;lastName&#x60;, &#x60;phone&#x60;, &#x60;email&#x60;. Existing of &#x60;phone&#x60; mapping is required.  | 
 **list_id** | **int**| List that ID contacts will be imported to. Ignored if &#x60;listName&#x60; is specified.  | [optional] 
 **list_name** | **str**| List name. This list will be created during import. If such name is already taken, an ordinal (1, 2, ...) will be added to the end. Ignored if &#x60;listId&#x60; is specified.  | [optional] 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_subaccount**
> invite_subaccount(invite_subaccount_input_object)

Invite a new sub-account

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sub-Accounts/inviteSubaccount\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
invite_subaccount_input_object = TextMagic.InviteSubaccountInputObject() # InviteSubaccountInputObject | 

try:
    # Invite a new sub-account
    api_instance.invite_subaccount(invite_subaccount_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->invite_subaccount: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_subaccount_input_object** | [**InviteSubaccountInputObject**](InviteSubaccountInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_chats_read_bulk**
> mark_chats_read_bulk(mark_chats_read_bulk_input_object)

Mark chats as read (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/markChatsReadBulk\" target=\"_blank\">Try in sandbox</a><br>Mark several chats as read by chat IDs or mark all chats as read

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
mark_chats_read_bulk_input_object = TextMagic.MarkChatsReadBulkInputObject() # MarkChatsReadBulkInputObject | 

try:
    # Mark chats as read (bulk)
    api_instance.mark_chats_read_bulk(mark_chats_read_bulk_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->mark_chats_read_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mark_chats_read_bulk_input_object** | [**MarkChatsReadBulkInputObject**](MarkChatsReadBulkInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_chats_unread_bulk**
> mark_chats_unread_bulk(mark_chats_unread_bulk_input_object)

Mark chats as unread (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/markChatsUnreadBulk\" target=\"_blank\">Try in sandbox</a><br>Mark several chats as UNread by chat IDs or mark all chats as UNread

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
mark_chats_unread_bulk_input_object = TextMagic.MarkChatsUnreadBulkInputObject() # MarkChatsUnreadBulkInputObject | 

try:
    # Mark chats as unread (bulk)
    api_instance.mark_chats_unread_bulk(mark_chats_unread_bulk_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->mark_chats_unread_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mark_chats_unread_bulk_input_object** | [**MarkChatsUnreadBulkInputObject**](MarkChatsUnreadBulkInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mute_chat**
> ResourceLinkResponse mute_chat(mute_chat_input_object)

Mute chat sounds

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/muteChat\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
mute_chat_input_object = TextMagic.MuteChatInputObject() # MuteChatInputObject | 

try:
    # Mute chat sounds
    api_response = api_instance.mute_chat(mute_chat_input_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->mute_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mute_chat_input_object** | [**MuteChatInputObject**](MuteChatInputObject.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mute_chats_bulk**
> mute_chats_bulk(mute_chats_bulk_input_object)

Mute chats (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/muteChatsBulk\" target=\"_blank\">Try in sandbox</a><br>Mute several chats by chat ids or mute all chats.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
mute_chats_bulk_input_object = TextMagic.MuteChatsBulkInputObject() # MuteChatsBulkInputObject | 

try:
    # Mute chats (bulk)
    api_instance.mute_chats_bulk(mute_chats_bulk_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->mute_chats_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mute_chats_bulk_input_object** | [**MuteChatsBulkInputObject**](MuteChatsBulkInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping**
> PingResponse ping()

Ping

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Timezones%20and%20Countries/ping\" target=\"_blank\">Try in sandbox</a><br>Make a simple ping request.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

try:
    # Ping
    api_response = api_instance.ping()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->ping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PingResponse**](PingResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reopen_chats_bulk**
> reopen_chats_bulk(reopen_chats_bulk_input_object)

Reopen chats (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/reopenChatsBulk\" target=\"_blank\">Try in sandbox</a><br>Reopen chats by chat IDs or reopen all chats

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
reopen_chats_bulk_input_object = TextMagic.ReopenChatsBulkInputObject() # ReopenChatsBulkInputObject | 

try:
    # Reopen chats (bulk)
    api_instance.reopen_chats_bulk(reopen_chats_bulk_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->reopen_chats_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reopen_chats_bulk_input_object** | [**ReopenChatsBulkInputObject**](ReopenChatsBulkInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_new_subaccount_token**
> User request_new_subaccount_token(request_new_subaccount_token_input_object)

Request a new REST API token for sub-account

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sub-Accounts/requestNewSubaccountToken\" target=\"_blank\">Try in sandbox</a><br>Returning user object, key and app name.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
request_new_subaccount_token_input_object = TextMagic.RequestNewSubaccountTokenInputObject() # RequestNewSubaccountTokenInputObject | 

try:
    # Request a new REST API token for sub-account
    api_response = api_instance.request_new_subaccount_token(request_new_subaccount_token_input_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->request_new_subaccount_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_new_subaccount_token_input_object** | [**RequestNewSubaccountTokenInputObject**](RequestNewSubaccountTokenInputObject.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_sender_id**
> ResourceLinkResponse request_sender_id(request_sender_id_input_object)

Apply for a new Sender ID

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Sender%20IDs/requestSenderId\" target=\"_blank\">Try in sandbox</a><br>> Sender IDs are shared among all of your sub-accounts.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
request_sender_id_input_object = TextMagic.RequestSenderIdInputObject() # RequestSenderIdInputObject | 

try:
    # Apply for a new Sender ID
    api_response = api_instance.request_sender_id(request_sender_id_input_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->request_sender_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_sender_id_input_object** | [**RequestSenderIdInputObject**](RequestSenderIdInputObject.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_chats**
> SearchChatsPaginatedResponse search_chats(page=page, limit=limit, query=query)

Find chats by message text

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/searchChats\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
query = 'query_example' # str | Find chats by specified search query. (optional)

try:
    # Find chats by message text
    api_response = api_instance.search_chats(page=page, limit=limit, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_chats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **query** | **str**| Find chats by specified search query. | [optional] 

### Return type

[**SearchChatsPaginatedResponse**](SearchChatsPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_chats_by_ids**
> SearchChatsByIdsPaginatedResponse search_chats_by_ids(page=page, limit=limit, ids=ids)

Find chats (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/searchChatsByIds\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
ids = 'ids_example' # str | Find chats by ID(s). (optional)

try:
    # Find chats (bulk)
    api_response = api_instance.search_chats_by_ids(page=page, limit=limit, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_chats_by_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **ids** | **str**| Find chats by ID(s). | [optional] 

### Return type

[**SearchChatsByIdsPaginatedResponse**](SearchChatsByIdsPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_chats_by_receipent**
> SearchChatsByReceipentPaginatedResponse search_chats_by_receipent(page=page, limit=limit, query=query, order_by=order_by)

Find chats by recipient

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/searchChatsByReceipent\" target=\"_blank\">Try in sandbox</a><br>Find chats by recipient (contact, list name or phone number).

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
query = 'query_example' # str | Find chats by specified search query. (optional)
order_by = 'id' # str | Order results by some field. Default is id. (optional) (default to id)

try:
    # Find chats by recipient
    api_response = api_instance.search_chats_by_receipent(page=page, limit=limit, query=query, order_by=order_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_chats_by_receipent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **query** | **str**| Find chats by specified search query. | [optional] 
 **order_by** | **str**| Order results by some field. Default is id. | [optional] [default to id]

### Return type

[**SearchChatsByReceipentPaginatedResponse**](SearchChatsByReceipentPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_contacts**
> SearchContactsPaginatedResponse search_contacts(page=page, limit=limit, shared=shared, ids=ids, list_id=list_id, include_blocked=include_blocked, query=query, local=local, country=country, order_by=order_by, direction=direction)

Find contacts by given criteria

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/searchContacts\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
shared = 0 # int | Should shared contacts be included? (optional) (default to 0)
ids = 'ids_example' # str | Find contacts by IDs. (optional)
list_id = 56 # int | Find contacts by List ID. (optional)
include_blocked = 56 # int | Should blocked contacts be included? (optional)
query = 'query_example' # str | Find contacts by specified search query. (optional)
local = 0 # int | Treat phone number passed in the \"query\" field as local. Default is 0. (optional) (default to 0)
country = 'country_example' # str | The 2-letter ISO country code for local phone numbers, used when \"local\" is set to true. Default is the account country. (optional)
order_by = 'id' # str | Order results by some field. Default is id. (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc. (optional) (default to desc)

try:
    # Find contacts by given criteria
    api_response = api_instance.search_contacts(page=page, limit=limit, shared=shared, ids=ids, list_id=list_id, include_blocked=include_blocked, query=query, local=local, country=country, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_contacts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **shared** | **int**| Should shared contacts be included? | [optional] [default to 0]
 **ids** | **str**| Find contacts by IDs. | [optional] 
 **list_id** | **int**| Find contacts by List ID. | [optional] 
 **include_blocked** | **int**| Should blocked contacts be included? | [optional] 
 **query** | **str**| Find contacts by specified search query. | [optional] 
 **local** | **int**| Treat phone number passed in the \&quot;query\&quot; field as local. Default is 0. | [optional] [default to 0]
 **country** | **str**| The 2-letter ISO country code for local phone numbers, used when \&quot;local\&quot; is set to true. Default is the account country. | [optional] 
 **order_by** | **str**| Order results by some field. Default is id. | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc. | [optional] [default to desc]

### Return type

[**SearchContactsPaginatedResponse**](SearchContactsPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_inbound_messages**
> SearchInboundMessagesPaginatedResponse search_inbound_messages(page=page, limit=limit, ids=ids, query=query, order_by=order_by, direction=direction, expand=expand)

Find inbound messages

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Receive%0A/searchInboundMessages\" target=\"_blank\">Try in sandbox</a><br>Find inbound messages by given parameters.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
ids = 'ids_example' # str | Find message by ID(s). (optional)
query = 'query_example' # str | Find recipients by specified search query. (optional)
order_by = 'id' # str | Order results by some field. Default is id. (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc. (optional) (default to desc)
expand = 0 # int | Expand by adding firstName, lastName and contactId. (optional) (default to 0)

try:
    # Find inbound messages
    api_response = api_instance.search_inbound_messages(page=page, limit=limit, ids=ids, query=query, order_by=order_by, direction=direction, expand=expand)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_inbound_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **ids** | **str**| Find message by ID(s). | [optional] 
 **query** | **str**| Find recipients by specified search query. | [optional] 
 **order_by** | **str**| Order results by some field. Default is id. | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc. | [optional] [default to desc]
 **expand** | **int**| Expand by adding firstName, lastName and contactId. | [optional] [default to 0]

### Return type

[**SearchInboundMessagesPaginatedResponse**](SearchInboundMessagesPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_lists**
> SearchListsPaginatedResponse search_lists(page=page, limit=limit, ids=ids, query=query, only_mine=only_mine, only_default=only_default, order_by=order_by, direction=direction)

Find lists by given criteria

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/searchLists\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
ids = '\"1,2,3,4\"' # str | Find lists by IDs. (optional)
query = '\"A\"' # str | Find lists by specified search query. (optional)
only_mine = 0 # int | Return only current user lists. (optional) (default to 0)
only_default = 0 # int | Return only default lists. (optional) (default to 0)
order_by = 'id' # str | Order results by some field. Default is id. (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc. (optional) (default to desc)

try:
    # Find lists by given criteria
    api_response = api_instance.search_lists(page=page, limit=limit, ids=ids, query=query, only_mine=only_mine, only_default=only_default, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **ids** | **str**| Find lists by IDs. | [optional] 
 **query** | **str**| Find lists by specified search query. | [optional] 
 **only_mine** | **int**| Return only current user lists. | [optional] [default to 0]
 **only_default** | **int**| Return only default lists. | [optional] [default to 0]
 **order_by** | **str**| Order results by some field. Default is id. | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc. | [optional] [default to desc]

### Return type

[**SearchListsPaginatedResponse**](SearchListsPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_outbound_messages**
> SearchOutboundMessagesPaginatedResponse search_outbound_messages(page=page, limit=limit, last_id=last_id, ids=ids, session_id=session_id, statuses=statuses, include_deleted=include_deleted, query=query)

Find messages

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Send%0A/searchOutboundMessages\" target=\"_blank\">Try in sandbox</a><br>Find outbound messages by given parameters.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
last_id = 56 # int | Filter results by ID, selecting all values lesser than the specified ID. Note that the \\'page\\' parameter is ignored when \\'lastId\\' is specified. (optional)
ids = 'ids_example' # str | Find message by ID(s). (optional)
session_id = 56 # int | Find messages by session ID. (optional)
statuses = '\"q\"' # str | Find messages by status. (optional)
include_deleted = 0 # int | Search also in deleted messages. (optional) (default to 0)
query = 'query_example' # str | Find messages by specified search query. (optional)

try:
    # Find messages
    api_response = api_instance.search_outbound_messages(page=page, limit=limit, last_id=last_id, ids=ids, session_id=session_id, statuses=statuses, include_deleted=include_deleted, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_outbound_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **last_id** | **int**| Filter results by ID, selecting all values lesser than the specified ID. Note that the \\&#39;page\\&#39; parameter is ignored when \\&#39;lastId\\&#39; is specified. | [optional] 
 **ids** | **str**| Find message by ID(s). | [optional] 
 **session_id** | **int**| Find messages by session ID. | [optional] 
 **statuses** | **str**| Find messages by status. | [optional] 
 **include_deleted** | **int**| Search also in deleted messages. | [optional] [default to 0]
 **query** | **str**| Find messages by specified search query. | [optional] 

### Return type

[**SearchOutboundMessagesPaginatedResponse**](SearchOutboundMessagesPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_scheduled_messages**
> SearchScheduledMessagesPaginatedResponse search_scheduled_messages(page=page, limit=limit, query=query, ids=ids, status=status, order_by=order_by, direction=direction)

Find scheduled messages

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Schedule%0A/searchScheduledMessages\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
query = 'query_example' # str | Find messages by specified search query. (optional)
ids = 'ids_example' # str | Find schedules by ID(s). (optional)
status = 'x' # str | Fetch schedules with a specific status: a - actual, c - completed, x - all. (optional) (default to x)
order_by = 'id' # str | Order results by some field. Default is id. (optional) (default to id)
direction = 'desc' # str | Order direction. Default is desc. (optional) (default to desc)

try:
    # Find scheduled messages
    api_response = api_instance.search_scheduled_messages(page=page, limit=limit, query=query, ids=ids, status=status, order_by=order_by, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_scheduled_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **query** | **str**| Find messages by specified search query. | [optional] 
 **ids** | **str**| Find schedules by ID(s). | [optional] 
 **status** | **str**| Fetch schedules with a specific status: a - actual, c - completed, x - all. | [optional] [default to x]
 **order_by** | **str**| Order results by some field. Default is id. | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc. | [optional] [default to desc]

### Return type

[**SearchScheduledMessagesPaginatedResponse**](SearchScheduledMessagesPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_templates**
> SearchTemplatesPaginatedResponse search_templates(page=page, limit=limit, ids=ids, name=name, content=content)

Find templates by criteria

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Templates/searchTemplates\" target=\"_blank\">Try in sandbox</a><br>Find user templates by given parameters.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
page = 1 # int | Fetch specified results page. (optional) (default to 1)
limit = 10 # int | The number of results per page. (optional) (default to 10)
ids = 'ids_example' # str | Find template by ID(s). (optional)
name = 'name_example' # str | Find template by name. (optional)
content = 'content_example' # str | Find template by content. (optional)

try:
    # Find templates by criteria
    api_response = api_instance.search_templates(page=page, limit=limit, ids=ids, name=name, content=content)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->search_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **ids** | **str**| Find template by ID(s). | [optional] 
 **name** | **str**| Find template by name. | [optional] 
 **content** | **str**| Find template by content. | [optional] 

### Return type

[**SearchTemplatesPaginatedResponse**](SearchTemplatesPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message**
> SendMessageResponse send_message(send_message_input_object)

Send message

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Send%0A/sendMessage\" target=\"_blank\">Try in sandbox</a><br>This is the main entrypoint to send messages. See the examples above for the reference.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
send_message_input_object = TextMagic.SendMessageInputObject() # SendMessageInputObject | 

try:
    # Send message
    api_response = api_instance.send_message(send_message_input_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->send_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_message_input_object** | [**SendMessageInputObject**](SendMessageInputObject.md)|  | 

### Return type

[**SendMessageResponse**](SendMessageResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_phone_verification_code_tfa**
> SendPhoneVerificationCodeResponse send_phone_verification_code_tfa(send_phone_verification_code_input_object)

Step 1: Send a verification code 

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Two-factor%20authentication/sendPhoneVerificationCodeTFA\" target=\"_blank\">Try in sandbox</a><br>Sends a verification code to a specified phone number.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
send_phone_verification_code_input_object = TextMagic.SendPhoneVerificationCodeInputObject() # SendPhoneVerificationCodeInputObject | 

try:
    # Step 1: Send a verification code 
    api_response = api_instance.send_phone_verification_code_tfa(send_phone_verification_code_input_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->send_phone_verification_code_tfa: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_phone_verification_code_input_object** | [**SendPhoneVerificationCodeInputObject**](SendPhoneVerificationCodeInputObject.md)|  | 

### Return type

[**SendPhoneVerificationCodeResponse**](SendPhoneVerificationCodeResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_chat_status**
> ResourceLinkResponse set_chat_status(set_chat_status_input_object)

Change chat status

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/setChatStatus\" target=\"_blank\">Try in sandbox</a><br>Set the status of the chat given by ID.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
set_chat_status_input_object = TextMagic.SetChatStatusInputObject() # SetChatStatusInputObject | 

try:
    # Change chat status
    api_response = api_instance.set_chat_status(set_chat_status_input_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->set_chat_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_chat_status_input_object** | [**SetChatStatusInputObject**](SetChatStatusInputObject.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unblock_contact**
> unblock_contact(unblock_contact_input_object)

Unblock a contact by phone number

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/unblockContact\" target=\"_blank\">Try in sandbox</a><br>Unblock a contact by phone number

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
unblock_contact_input_object = TextMagic.UnblockContactInputObject() # UnblockContactInputObject | 

try:
    # Unblock a contact by phone number
    api_instance.unblock_contact(unblock_contact_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->unblock_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unblock_contact_input_object** | [**UnblockContactInputObject**](UnblockContactInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unblock_contacts_bulk**
> unblock_contacts_bulk(unblock_contacts_bulk_input_object)

Unblock contacts (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/unblockContactsBulk\" target=\"_blank\">Try in sandbox</a><br>Unblock several contacts by blocked contact IDs or unblock all contacts.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
unblock_contacts_bulk_input_object = TextMagic.UnblockContactsBulkInputObject() # UnblockContactsBulkInputObject | 

try:
    # Unblock contacts (bulk)
    api_instance.unblock_contacts_bulk(unblock_contacts_bulk_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->unblock_contacts_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unblock_contacts_bulk_input_object** | [**UnblockContactsBulkInputObject**](UnblockContactsBulkInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmute_chats_bulk**
> unmute_chats_bulk(unmute_chats_bulk_input_object)

Unmute chats (bulk)

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Chats/unmuteChatsBulk\" target=\"_blank\">Try in sandbox</a><br>Unmute several chats by chat ids or unmute all chats.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
unmute_chats_bulk_input_object = TextMagic.UnmuteChatsBulkInputObject() # UnmuteChatsBulkInputObject | 

try:
    # Unmute chats (bulk)
    api_instance.unmute_chats_bulk(unmute_chats_bulk_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->unmute_chats_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unmute_chats_bulk_input_object** | [**UnmuteChatsBulkInputObject**](UnmuteChatsBulkInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_contact**
> ResourceLinkResponse unsubscribe_contact(unsubscribe_contact_input_object)

Manually unsubscribe a contact

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/unsubscribeContact\" target=\"_blank\">Try in sandbox</a><br>> Please note, if you unsubscribe a contact, this action cannot be reversed. 

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
unsubscribe_contact_input_object = TextMagic.UnsubscribeContactInputObject() # UnsubscribeContactInputObject | 

try:
    # Manually unsubscribe a contact
    api_response = api_instance.unsubscribe_contact(unsubscribe_contact_input_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->unsubscribe_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unsubscribe_contact_input_object** | [**UnsubscribeContactInputObject**](UnsubscribeContactInputObject.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_balance_notification_settings**
> update_balance_notification_settings(update_balance_notification_settings_input_object)

Update balance notification settings

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/undefined/updateBalanceNotificationSettings\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_balance_notification_settings_input_object = TextMagic.UpdateBalanceNotificationSettingsInputObject() # UpdateBalanceNotificationSettingsInputObject | 

try:
    # Update balance notification settings
    api_instance.update_balance_notification_settings(update_balance_notification_settings_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_balance_notification_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_balance_notification_settings_input_object** | [**UpdateBalanceNotificationSettingsInputObject**](UpdateBalanceNotificationSettingsInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_callback_settings**
> update_callback_settings(update_callback_settings_input_object)

Update callback URL settings

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/undefined/updateCallbackSettings\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_callback_settings_input_object = TextMagic.UpdateCallbackSettingsInputObject() # UpdateCallbackSettingsInputObject | 

try:
    # Update callback URL settings
    api_instance.update_callback_settings(update_callback_settings_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_callback_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_callback_settings_input_object** | [**UpdateCallbackSettingsInputObject**](UpdateCallbackSettingsInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_chat_desktop_notification_settings**
> update_chat_desktop_notification_settings(update_chat_desktop_notification_settings_input_object)

Update chat desktop notification settings

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/undefined/updateChatDesktopNotificationSettings\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_chat_desktop_notification_settings_input_object = TextMagic.UpdateChatDesktopNotificationSettingsInputObject() # UpdateChatDesktopNotificationSettingsInputObject | 

try:
    # Update chat desktop notification settings
    api_instance.update_chat_desktop_notification_settings(update_chat_desktop_notification_settings_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_chat_desktop_notification_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_chat_desktop_notification_settings_input_object** | [**UpdateChatDesktopNotificationSettingsInputObject**](UpdateChatDesktopNotificationSettingsInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> ResourceLinkResponse update_contact(update_contact_input_object, id)

Edit a contact

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/updateContact\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_contact_input_object = TextMagic.UpdateContactInputObject() # UpdateContactInputObject | 
id = 1 # int | 

try:
    # Edit a contact
    api_response = api_instance.update_contact(update_contact_input_object, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_contact_input_object** | [**UpdateContactInputObject**](UpdateContactInputObject.md)|  | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact_note**
> ResourceLinkResponse update_contact_note(update_contact_note_input_object, id)

Update a contact note

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contact%20Notes/updateContactNote\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_contact_note_input_object = TextMagic.UpdateContactNoteInputObject() # UpdateContactNoteInputObject | 
id = 1 # int | 

try:
    # Update a contact note
    api_response = api_instance.update_contact_note(update_contact_note_input_object, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_contact_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_contact_note_input_object** | [**UpdateContactNoteInputObject**](UpdateContactNoteInputObject.md)|  | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_current_user**
> UpdateCurrentUserResponse update_current_user(update_current_user_input_object)

Edit current account info

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Account/updateCurrentUser\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_current_user_input_object = TextMagic.UpdateCurrentUserInputObject() # UpdateCurrentUserInputObject | 

try:
    # Edit current account info
    api_response = api_instance.update_current_user(update_current_user_input_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_current_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_current_user_input_object** | [**UpdateCurrentUserInputObject**](UpdateCurrentUserInputObject.md)|  | 

### Return type

[**UpdateCurrentUserResponse**](UpdateCurrentUserResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field**
> ResourceLinkResponse update_custom_field(update_custom_field_input_object, id)

Edit a custom field

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Custom%20Fields/updateCustomField\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_custom_field_input_object = TextMagic.UpdateCustomFieldInputObject() # UpdateCustomFieldInputObject | 
id = 1 # int | 

try:
    # Edit a custom field
    api_response = api_instance.update_custom_field(update_custom_field_input_object, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_custom_field: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_custom_field_input_object** | [**UpdateCustomFieldInputObject**](UpdateCustomFieldInputObject.md)|  | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field_value**
> ResourceLinkResponse update_custom_field_value(update_custom_field_value_input_object, id)

Edit the custom field value of a specified contact

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Custom%20Fields/updateCustomFieldValue\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_custom_field_value_input_object = TextMagic.UpdateCustomFieldValueInputObject() # UpdateCustomFieldValueInputObject | 
id = 554 # int | 

try:
    # Edit the custom field value of a specified contact
    api_response = api_instance.update_custom_field_value(update_custom_field_value_input_object, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_custom_field_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_custom_field_value_input_object** | [**UpdateCustomFieldValueInputObject**](UpdateCustomFieldValueInputObject.md)|  | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inbound_messages_notification_settings**
> update_inbound_messages_notification_settings(update_inbound_messages_notification_settings_input_object)

Update inbound messages notification settings

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/undefined/updateInboundMessagesNotificationSettings\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_inbound_messages_notification_settings_input_object = TextMagic.UpdateInboundMessagesNotificationSettingsInputObject() # UpdateInboundMessagesNotificationSettingsInputObject | 

try:
    # Update inbound messages notification settings
    api_instance.update_inbound_messages_notification_settings(update_inbound_messages_notification_settings_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_inbound_messages_notification_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_inbound_messages_notification_settings_input_object** | [**UpdateInboundMessagesNotificationSettingsInputObject**](UpdateInboundMessagesNotificationSettingsInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_list**
> ResourceLinkResponse update_list(id, update_list_object=update_list_object)

Edit a list

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/updateList\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
id = 1 # int | 
update_list_object = TextMagic.UpdateListObject() # UpdateListObject |  (optional)

try:
    # Edit a list
    api_response = api_instance.update_list(id, update_list_object=update_list_object)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_list_object** | [**UpdateListObject**](UpdateListObject.md)|  | [optional] 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sender_setting**
> update_sender_setting(update_sender_setting_input_object)

Change sender settings

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Overview/updateSenderSetting\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_sender_setting_input_object = TextMagic.UpdateSenderSettingInputObject() # UpdateSenderSettingInputObject | 

try:
    # Change sender settings
    api_instance.update_sender_setting(update_sender_setting_input_object)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_sender_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_sender_setting_input_object** | [**UpdateSenderSettingInputObject**](UpdateSenderSettingInputObject.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> ResourceLinkResponse update_template(update_template_input_object, id)

Update a template

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Templates/updateTemplate\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
update_template_input_object = TextMagic.UpdateTemplateInputObject() # UpdateTemplateInputObject | 
id = 1 # int | 

try:
    # Update a template
    api_response = api_instance.update_template(update_template_input_object, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->update_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_template_input_object** | [**UpdateTemplateInputObject**](UpdateTemplateInputObject.md)|  | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_avatar**
> upload_avatar(image)

Upload an avatar

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Account/uploadAvatar\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
image = '/path/to/file.txt' # file | User avatar. Should be a PNG or JPG file not more than 10 MB.

try:
    # Upload an avatar
    api_instance.upload_avatar(image)
except ApiException as e:
    print("Exception when calling TextMagicApi->upload_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **file**| User avatar. Should be a PNG or JPG file not more than 10 MB. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_contact_avatar**
> ResourceLinkResponse upload_contact_avatar(image, id)

Upload an avatar

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Contacts/uploadContactAvatar\" target=\"_blank\">Try in sandbox</a><br>

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
image = '/path/to/file.txt' # file | Contact avatar. Should be a PNG or JPG file not more than 10 MB.
id = 1 # int | 

try:
    # Upload an avatar
    api_response = api_instance.upload_contact_avatar(image, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->upload_contact_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **file**| Contact avatar. Should be a PNG or JPG file not more than 10 MB. | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_list_avatar**
> ResourceLinkResponse upload_list_avatar(image, id)

Add an avatar for a list

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Lists/uploadListAvatar\" target=\"_blank\">Try in sandbox</a><br>Add an avatar for a list

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
image = '/path/to/file.txt' # file | List avatar. Should be a PNG or JPG file not more than 10 MB.
id = 1 # int | 

try:
    # Add an avatar for a list
    api_response = api_instance.upload_list_avatar(image, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->upload_list_avatar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **file**| List avatar. Should be a PNG or JPG file not more than 10 MB. | 
 **id** | **int**|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_message_attachment**
> UploadMessageAttachmentResponse upload_message_attachment(file)

Upload message attachment

<a class=\"try-sandbox-link\" href=\"http://sandbox.textmagictesting.com/#/Messages%3A%20Send%0A/uploadMessageAttachment\" target=\"_blank\">Try in sandbox</a><br>Upload a new file to insert it as a link.

### Example
```python
from __future__ import print_function
import time
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))
file = '/path/to/file.txt' # file | Attachment. Supports .jpg, .gif, .png, .pdf, .txt, .csv, .doc, .docx, .xls, .xlsx, .ppt, .pptx & .vcf file formats.

try:
    # Upload message attachment
    api_response = api_instance.upload_message_attachment(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TextMagicApi->upload_message_attachment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| Attachment. Supports .jpg, .gif, .png, .pdf, .txt, .csv, .doc, .docx, .xls, .xlsx, .ppt, .pptx &amp; .vcf file formats. | 

### Return type

[**UploadMessageAttachmentResponse**](UploadMessageAttachmentResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

