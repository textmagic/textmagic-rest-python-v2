# TextMagic.TextMagicApi

All URIs are relative to *https://rest.textmagic.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_contacts_to_list**](TextMagicApi.md#assign_contacts_to_list) | **PUT** /api/v2/lists/{id}/contacts | Assign contacts to a list
[**block_contact**](TextMagicApi.md#block_contact) | **POST** /api/v2/contacts/block | Block a contact by phone number
[**buy_dedicated_number**](TextMagicApi.md#buy_dedicated_number) | **POST** /api/v2/numbers | Buy a dedicated number
[**clear_and_assign_contacts_to_list**](TextMagicApi.md#clear_and_assign_contacts_to_list) | **POST** /api/v2/lists/{id}/contacts | Reset list members to the specified contacts
[**close_chats_bulk**](TextMagicApi.md#close_chats_bulk) | **POST** /api/v2/chats/close/bulk | Close chats (bulk)
[**close_read_chats**](TextMagicApi.md#close_read_chats) | **POST** /api/v2/chats/close/read | Close read chats
[**create_contact**](TextMagicApi.md#create_contact) | **POST** /api/v2/contacts/normalized | Add a new contact
[**create_contact_note**](TextMagicApi.md#create_contact_note) | **POST** /api/v2/contacts/{id}/notes | Create a new contact note
[**create_custom_field**](TextMagicApi.md#create_custom_field) | **POST** /api/v2/customfields | Add a new custom field
[**create_email_campaign**](TextMagicApi.md#create_email_campaign) | **POST** /api/v2/email-campaigns | Send email campaign
[**create_list**](TextMagicApi.md#create_list) | **POST** /api/v2/lists | Create a new list
[**create_tag**](TextMagicApi.md#create_tag) | **POST** /api/v2/tags | Create tag
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
[**get_email_senders**](TextMagicApi.md#get_email_senders) | **GET** /api/v2/email-campaigns/email-senders | Get list of email senders
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
[**get_template**](TextMagicApi.md#get_template) | **GET** /api/v2/templates/{id} | Get a template&#x60;s details
[**get_timezones**](TextMagicApi.md#get_timezones) | **GET** /api/v2/timezones | Get timezones
[**get_unread_messages_total**](TextMagicApi.md#get_unread_messages_total) | **GET** /api/v2/chats/unread/count | Get unread messages number
[**get_unsubscribed_contact**](TextMagicApi.md#get_unsubscribed_contact) | **GET** /api/v2/unsubscribers/{id} | Get the details of a specific unsubscribed contact
[**get_unsubscribers**](TextMagicApi.md#get_unsubscribers) | **GET** /api/v2/unsubscribers | Get all unsubscribed contacts
[**get_user_dedicated_numbers**](TextMagicApi.md#get_user_dedicated_numbers) | **GET** /api/v2/numbers | Get all your dedicated numbers
[**import_contacts**](TextMagicApi.md#import_contacts) | **POST** /api/v2/contacts/import/normalized | Import contacts
[**mark_chats_read_bulk**](TextMagicApi.md#mark_chats_read_bulk) | **POST** /api/v2/chats/read/bulk | Mark chats as read (bulk)
[**mark_chats_unread_bulk**](TextMagicApi.md#mark_chats_unread_bulk) | **POST** /api/v2/chats/unread/bulk | Mark chats as unread (bulk)
[**mute_chat**](TextMagicApi.md#mute_chat) | **POST** /api/v2/chats/mute | Mute chat sounds
[**mute_chats_bulk**](TextMagicApi.md#mute_chats_bulk) | **POST** /api/v2/chats/mute/bulk | Mute chats (bulk)
[**ping**](TextMagicApi.md#ping) | **GET** /api/v2/ping | Ping
[**reopen_chats_bulk**](TextMagicApi.md#reopen_chats_bulk) | **POST** /api/v2/chats/reopen/bulk | Reopen chats (bulk)
[**request_sender_id**](TextMagicApi.md#request_sender_id) | **POST** /api/v2/senderids | Apply for a new Sender ID
[**schedule_email_campaign**](TextMagicApi.md#schedule_email_campaign) | **POST** /api/v2/email-campaigns/schedule | Schedule new email campaign
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
[**upload_message_mms_attachment**](TextMagicApi.md#upload_message_mms_attachment) | **POST** /api/v2/messages/mms/attachment | Upload message mms attachment


# **assign_contacts_to_list**
> ResourceLinkResponse assign_contacts_to_list(id, assign_contacts_to_list_input_object)

Assign contacts to a list

> Unlike all other PUT requests, this command does not need old contact IDs to be submitted. For example, if you have a list with contacts 150, 151 and 152 and you want to add contact ID 153, you only need to submit 153 as a parameter of PUT /api/v2/lists/{id}/contacts.


### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.assign_contacts_to_list_request import AssignContactsToListRequest
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    assign_contacts_to_list_input_object = TextMagic.AssignContactsToListRequest() # AssignContactsToListRequest | 

    try:
        # Assign contacts to a list
        api_response = api_instance.assign_contacts_to_list(id, assign_contacts_to_list_input_object)
        print("The response of TextMagicApi->assign_contacts_to_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->assign_contacts_to_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **assign_contacts_to_list_input_object** | [**AssignContactsToListRequest**](AssignContactsToListRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Returned when trying to edit a list shared to the current user. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **block_contact**
> ResourceLinkResponse block_contact(block_contact_input_object)

Block a contact by phone number

Block a contact from inbound and outbound communication by phone number.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.block_contact_request import BlockContactRequest
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    block_contact_input_object = TextMagic.BlockContactRequest() # BlockContactRequest | 

    try:
        # Block a contact by phone number
        api_response = api_instance.block_contact(block_contact_input_object)
        print("The response of TextMagicApi->block_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->block_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **block_contact_input_object** | [**BlockContactRequest**](BlockContactRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when updated with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **buy_dedicated_number**
> buy_dedicated_number(buy_dedicated_number_input_object)

Buy a dedicated number

To buy a dedicated number, you first need to find an available number matching your criteria using the `/api/v2/numbers/available` command described above.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.buy_dedicated_number_request import BuyDedicatedNumberRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    buy_dedicated_number_input_object = TextMagic.BuyDedicatedNumberRequest() # BuyDedicatedNumberRequest | 

    try:
        # Buy a dedicated number
        api_instance.buy_dedicated_number(buy_dedicated_number_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->buy_dedicated_number: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **buy_dedicated_number_input_object** | [**BuyDedicatedNumberRequest**](BuyDedicatedNumberRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Number has been bought with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_and_assign_contacts_to_list**
> ResourceLinkResponse clear_and_assign_contacts_to_list(id, clear_and_assign_contacts_to_list_input_object)

Reset list members to the specified contacts

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.clear_and_assign_contacts_to_list_request import ClearAndAssignContactsToListRequest
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    clear_and_assign_contacts_to_list_input_object = TextMagic.ClearAndAssignContactsToListRequest() # ClearAndAssignContactsToListRequest | 

    try:
        # Reset list members to the specified contacts
        api_response = api_instance.clear_and_assign_contacts_to_list(id, clear_and_assign_contacts_to_list_input_object)
        print("The response of TextMagicApi->clear_and_assign_contacts_to_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->clear_and_assign_contacts_to_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **clear_and_assign_contacts_to_list_input_object** | [**ClearAndAssignContactsToListRequest**](ClearAndAssignContactsToListRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Returned when trying to edit a list shared to the current user. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_chats_bulk**
> close_chats_bulk(close_chats_bulk_input_object)

Close chats (bulk)

Close chats by chat IDs or close all chats

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.mark_chats_unread_bulk_request import MarkChatsUnreadBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    close_chats_bulk_input_object = TextMagic.MarkChatsUnreadBulkRequest() # MarkChatsUnreadBulkRequest | 

    try:
        # Close chats (bulk)
        api_instance.close_chats_bulk(close_chats_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->close_chats_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **close_chats_bulk_input_object** | [**MarkChatsUnreadBulkRequest**](MarkChatsUnreadBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_read_chats**
> close_read_chats()

Close read chats

Close all chats that have no unread messages.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)

    try:
        # Close read chats
        api_instance.close_read_chats()
    except Exception as e:
        print("Exception when calling TextMagicApi->close_read_chats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact**
> ResourceLinkResponse create_contact(create_contact_input_object)

Add a new contact

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.create_contact_request import CreateContactRequest
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    create_contact_input_object = TextMagic.CreateContactRequest() # CreateContactRequest | 

    try:
        # Add a new contact
        api_response = api_instance.create_contact(create_contact_input_object)
        print("The response of TextMagicApi->create_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->create_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_contact_input_object** | [**CreateContactRequest**](CreateContactRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Contact has been created with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_contact_note**
> ResourceLinkResponse create_contact_note(id, create_contact_note_input_object)

Create a new contact note

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.create_contact_note_request import CreateContactNoteRequest
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    create_contact_note_input_object = TextMagic.CreateContactNoteRequest() # CreateContactNoteRequest | 

    try:
        # Create a new contact note
        api_response = api_instance.create_contact_note(id, create_contact_note_input_object)
        print("The response of TextMagicApi->create_contact_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->create_contact_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **create_contact_note_input_object** | [**CreateContactNoteRequest**](CreateContactNoteRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when created with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_field**
> ResourceLinkResponse create_custom_field(create_custom_field_input_object)

Add a new custom field

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.create_custom_field_request import CreateCustomFieldRequest
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    create_custom_field_input_object = TextMagic.CreateCustomFieldRequest() # CreateCustomFieldRequest | 

    try:
        # Add a new custom field
        api_response = api_instance.create_custom_field(create_custom_field_input_object)
        print("The response of TextMagicApi->create_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->create_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_custom_field_input_object** | [**CreateCustomFieldRequest**](CreateCustomFieldRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Contact has been created with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_email_campaign**
> CreateEmailCampaignResponse create_email_campaign(create_email_campaign_input_object)

Send email campaign

Creates a new email campaign and sends it to the specified recipients.

This endpoint allows you to create and immediately send an email marketing campaign to your contacts, groups, or direct email addresses. The campaign will be processed asynchronously, and you'll receive a campaign object with tracking information.

## Request Requirements

- **Email Sender ID**: Must be a valid, configured email sender from your account
- **Recipients**: At least one recipient type must be specified (contacts, groups, or emails)
- **Content**: Subject and HTML message content are required
- **Balance**: Sufficient account balance for the estimated campaign cost

## Recipient Types

You can target multiple recipient types in a single campaign:

- **Contact IDs**: Send to specific contacts from your contact list
- **Group IDs**: Send to all contacts within specified groups  
- **Direct Emails**: Send to email addresses not in your contact list

## Content Guidelines

- **Subject**: Maximum 998 characters, should be engaging and relevant
- **Message**: HTML content supported, including images, links, and formatting
- **From Name**: Optional custom sender name (max 500 characters)
- **Reply-To**: Optional custom reply-to email address

## Cost and Balance

The API automatically calculates campaign costs based on:
- Total number of unique recipients across all specified groups, contacts, and emails
- Your account's email pricing tier
- Any additional features or premium content

If your account balance is insufficient, the request will be rejected with a low balance error.

## Response Information

Successful campaigns return:
- Campaign ID for tracking and analytics
- Current campaign status and progress
- Cost breakdown and recipient counts
- Sender information and content preview
- Statistical totals and engagement metrics

## Error Scenarios

Common error conditions include:
- **Validation Errors**: Invalid email addresses, missing required fields, or content that exceeds limits
- **Insufficient Balance**: Account balance too low for campaign cost
- **Invalid Recipients**: Non-existent contact/group IDs or invalid email formats
- **Sender Configuration**: Invalid or unconfigured email sender ID
- **No Recipients**: All recipient arrays are empty or invalid


### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.create_email_campaign_request import CreateEmailCampaignRequest
from TextMagic.models.create_email_campaign_response import CreateEmailCampaignResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    create_email_campaign_input_object = TextMagic.CreateEmailCampaignRequest() # CreateEmailCampaignRequest | 

    try:
        # Send email campaign
        api_response = api_instance.create_email_campaign(create_email_campaign_input_object)
        print("The response of TextMagicApi->create_email_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->create_email_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_email_campaign_input_object** | [**CreateEmailCampaignRequest**](CreateEmailCampaignRequest.md)|  | 

### Return type

[**CreateEmailCampaignResponse**](CreateEmailCampaignResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Email campaign created successfully. |  -  |
**400** | Bad request - validation errors or insufficient balance. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Forbidden - insufficient permissions (requires ComposeEmail access). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_list**
> ResourceLinkResponse create_list(create_list_input_object)

Create a new list

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.create_list_request import CreateListRequest
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    create_list_input_object = TextMagic.CreateListRequest() # CreateListRequest | 

    try:
        # Create a new list
        api_response = api_instance.create_list(create_list_input_object)
        print("The response of TextMagicApi->create_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->create_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_list_input_object** | [**CreateListRequest**](CreateListRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tag**
> CreateTagResponse create_tag(create_tag_input_object)

Create tag

Creates a new tag for organizing and categorizing contacts.

This endpoint allows you to create a custom tag that can be used to segment and organize your contact database. Tags provide a flexible way to categorize contacts for better contact management.

## Request Requirements

- **Title**: Required field, must be between 1 and 50 characters
- **Uniqueness**: Tag titles must be unique within your account
- **Authentication**: Valid API credentials required

## Common Use Cases

Create tags for various organizational purposes:

- **Customer Types**: "VIP Customer", "New Lead", "Active Subscriber"
- **Geographic Segments**: "North Region", "Europe", "Local Customers"
- **Engagement Levels**: "Highly Engaged", "Inactive", "Recent Purchase"
- **Campaign Categories**: "Summer Promotion", "Newsletter Subscriber", "Event Attendee"
- **Custom Segments**: Any custom categorization that fits your business needs

## Response Information

Successful tag creation returns:
- **Tag ID**: Unique identifier for the newly created tag
- **Title**: The tag name as provided in the request

Use the returned tag ID to assign this tag to contacts or reference it in other API operations.

## Error Scenarios

Common error conditions include:
- **Validation Errors**: Title exceeds 50 characters or is empty
- **Duplicate Tag**: A tag with the same title already exists in your account
- **Authentication Errors**: Invalid or missing API credentials

## Next Steps

After creating a tag:
1. Use the tag ID to assign it to contacts via contact management endpoints
2. Reference the tag when filtering contacts
3. Manage and update tags through other Tags API endpoints


### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.create_tag_request import CreateTagRequest
from TextMagic.models.create_tag_response import CreateTagResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    create_tag_input_object = TextMagic.CreateTagRequest() # CreateTagRequest | 

    try:
        # Create tag
        api_response = api_instance.create_tag(create_tag_input_object)
        print("The response of TextMagicApi->create_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->create_tag: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tag_input_object** | [**CreateTagRequest**](CreateTagRequest.md)|  | 

### Return type

[**CreateTagResponse**](CreateTagResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Tag created successfully. |  -  |
**400** | Bad request - validation errors (e.g. invalid title format or tag already exists). |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_template**
> ResourceLinkResponse create_template(create_template_input_object)

Create a template

There are times when creating a new template makes sense (such as when targeting specific clients or improving your business strategies). 
You can create new SMS templates for marketing purposes or SMS templates for business campaigns.


### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.create_template_request import CreateTemplateRequest
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    create_template_input_object = TextMagic.CreateTemplateRequest() # CreateTemplateRequest | 

    try:
        # Create a template
        api_response = api_instance.create_template(create_template_input_object)
        print("The response of TextMagicApi->create_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->create_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_template_input_object** | [**CreateTemplateRequest**](CreateTemplateRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when successful. |  -  |
**400** | Returned when the form has errors. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_contacts**
> delete_all_contacts()

Delete contacts (bulk)

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)

    try:
        # Delete contacts (bulk)
        api_instance.delete_all_contacts()
    except Exception as e:
        print("Exception when calling TextMagicApi->delete_all_contacts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_outbound_messages**
> delete_all_outbound_messages()

Delete all messages

Delete all messages.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)

    try:
        # Delete all messages
        api_instance.delete_all_outbound_messages()
    except Exception as e:
        print("Exception when calling TextMagicApi->delete_all_outbound_messages: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_avatar**
> delete_avatar()

Delete an avatar

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)

    try:
        # Delete an avatar
        api_instance.delete_avatar()
    except Exception as e:
        print("Exception when calling TextMagicApi->delete_avatar: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Avatar deleted with success. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chat_messages**
> delete_chat_messages(id, delete_chat_messages_bulk_input_object)

Delete chat messages by ID(s)

Delete messages from chat by given message IDs.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.delete_chat_messages_request import DeleteChatMessagesRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    delete_chat_messages_bulk_input_object = TextMagic.DeleteChatMessagesRequest() # DeleteChatMessagesRequest | 

    try:
        # Delete chat messages by ID(s)
        api_instance.delete_chat_messages(id, delete_chat_messages_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->delete_chat_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **delete_chat_messages_bulk_input_object** | [**DeleteChatMessagesRequest**](DeleteChatMessagesRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chats_bulk**
> delete_chats_bulk(delete_chats_bulk_input_object)

Delete chats (bulk)

Delete chats by given IDs or delete all chats.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.delete_chats_bulk_request import DeleteChatsBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    delete_chats_bulk_input_object = TextMagic.DeleteChatsBulkRequest() # DeleteChatsBulkRequest | 

    try:
        # Delete chats (bulk)
        api_instance.delete_chats_bulk(delete_chats_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->delete_chats_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_chats_bulk_input_object** | [**DeleteChatsBulkRequest**](DeleteChatsBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact**
> delete_contact(id)

Delete a contact

> This command removes your contact completely. If it was assigned or saved to a shared list, it will disappear from there too. If you only need to remove a contact from selected lists, use the Contact assignment command in the Lists section instead, rather than deleting the contact.


### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Delete a contact
        api_instance.delete_contact(id)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Returned when trying to delete a contact shared to a current user. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_avatar**
> delete_contact_avatar(id)

Delete an avatar

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Delete an avatar
        api_instance.delete_contact_avatar(id)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Returned when trying to delete a contact shared to a current user. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_note**
> delete_contact_note(id)

Delete a contact note

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Delete a contact note
        api_instance.delete_contact_note(id)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contact_notes_bulk**
> delete_contact_notes_bulk(id, delete_contact_notes_bulk_input_object)

Delete contact notes (bulk)

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.delete_contact_notes_bulk_request import DeleteContactNotesBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    delete_contact_notes_bulk_input_object = TextMagic.DeleteContactNotesBulkRequest() # DeleteContactNotesBulkRequest | 

    try:
        # Delete contact notes (bulk)
        api_instance.delete_contact_notes_bulk(id, delete_contact_notes_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->delete_contact_notes_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **delete_contact_notes_bulk_input_object** | [**DeleteContactNotesBulkRequest**](DeleteContactNotesBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contacts_by_ids**
> delete_contacts_by_ids(delete_contacts_by_ids_input_object)

Delete contacts by IDs (bulk)

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.delete_contacts_by_ids_request import DeleteContactsByIdsRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    delete_contacts_by_ids_input_object = TextMagic.DeleteContactsByIdsRequest() # DeleteContactsByIdsRequest | 

    try:
        # Delete contacts by IDs (bulk)
        api_instance.delete_contacts_by_ids(delete_contacts_by_ids_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->delete_contacts_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_contacts_by_ids_input_object** | [**DeleteContactsByIdsRequest**](DeleteContactsByIdsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_contacts_from_list**
> delete_contacts_from_list(id, delete_contacs_from_list_object)

Unassign contacts from a list

> When you remove contacts from a specific list, they will be deleted permanently, unless they are first saved in another list.


### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.delete_contacts_from_list_request import DeleteContactsFromListRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    delete_contacs_from_list_object = TextMagic.DeleteContactsFromListRequest() # DeleteContactsFromListRequest | 

    try:
        # Unassign contacts from a list
        api_instance.delete_contacts_from_list(id, delete_contacs_from_list_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->delete_contacts_from_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **delete_contacs_from_list_object** | [**DeleteContactsFromListRequest**](DeleteContactsFromListRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Returned when trying to edit a list shared to the current user. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_field**
> delete_custom_field(id)

Delete a custom field

> When a custom field is deleted, all the information that was added to contacts under this custom field will also be lost.


### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Delete a custom field
        api_instance.delete_custom_field(id)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Returned when deleted with success. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dedicated_number**
> delete_dedicated_number(id)

Cancel a dedicated number subscription

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Cancel a dedicated number subscription
        api_instance.delete_dedicated_number(id)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The Dedicated number has been deleted with success. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inbound_message**
> delete_inbound_message(id)

Delete a single inbound message

> Note: deleted inbound messages will disappear from TextMagic Online, chats, and any other place they are referenced.  So, be careful!


### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | The unique numeric ID for the inbound message.

    try:
        # Delete a single inbound message
        api_instance.delete_inbound_message(id)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_inbound_messages_bulk**
> delete_inbound_messages_bulk(delete_inbound_messages_bulk_input_object)

Delete inbound messages (bulk)

> Note: deleted inbound messages will disappear from TextMagic Online, chats, and any other place they are referenced.  So, be careful!


### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.delete_lists_bulk_request import DeleteListsBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    delete_inbound_messages_bulk_input_object = TextMagic.DeleteListsBulkRequest() # DeleteListsBulkRequest | 

    try:
        # Delete inbound messages (bulk)
        api_instance.delete_inbound_messages_bulk(delete_inbound_messages_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->delete_inbound_messages_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_inbound_messages_bulk_input_object** | [**DeleteListsBulkRequest**](DeleteListsBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list**
> delete_list(id)

Delete a list

This command has no parameters. If successful, this command will return the standard delete response (204 No Content); otherwise, a standard error response will be returned.

When you delete a list, the contacts in it are deleted as well, unless they were saved in another list.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Delete a list
        api_instance.delete_list(id)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Returned when trying to remove a list associated with a signup form. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Returned when trying to remove a list shared to you. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list_avatar**
> delete_list_avatar(id)

Delete an avatar for a list

Delete an avatar for a list

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Delete an avatar for a list
        api_instance.delete_list_avatar(id)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Avatar has been deleted with success. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Returned when trying to edit a list shared to the current user. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_list_contacts_bulk**
> delete_list_contacts_bulk(id, delete_list_contacts_bulk_input_object)

Delete contacts from a list (bulk)

Delete contacts from a list (bulk)

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.unblock_contacts_bulk_request import UnblockContactsBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    delete_list_contacts_bulk_input_object = TextMagic.UnblockContactsBulkRequest() # UnblockContactsBulkRequest | 

    try:
        # Delete contacts from a list (bulk)
        api_instance.delete_list_contacts_bulk(id, delete_list_contacts_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->delete_list_contacts_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **delete_list_contacts_bulk_input_object** | [**UnblockContactsBulkRequest**](UnblockContactsBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lists_bulk**
> delete_lists_bulk(delete_lists_bulk_input_object)

Delete lists (bulk)

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.delete_lists_bulk_request import DeleteListsBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    delete_lists_bulk_input_object = TextMagic.DeleteListsBulkRequest() # DeleteListsBulkRequest | 

    try:
        # Delete lists (bulk)
        api_instance.delete_lists_bulk(delete_lists_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->delete_lists_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_lists_bulk_input_object** | [**DeleteListsBulkRequest**](DeleteListsBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message_session**
> delete_message_session(id)

Delete a session

Delete a message session, together with all nested messages.
> You will not be refunded for any deleted sent sessions.


### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Delete a session
        api_instance.delete_message_session(id)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_message_sessions_bulk**
> delete_message_sessions_bulk(delete_message_sessions_bulk_input_object)

Delete sessions (bulk)

Delete message sessions, together with all nested messages, by given ID(s) or delete all message sessions.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.delete_lists_bulk_request import DeleteListsBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    delete_message_sessions_bulk_input_object = TextMagic.DeleteListsBulkRequest() # DeleteListsBulkRequest | 

    try:
        # Delete sessions (bulk)
        api_instance.delete_message_sessions_bulk(delete_message_sessions_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->delete_message_sessions_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_message_sessions_bulk_input_object** | [**DeleteListsBulkRequest**](DeleteListsBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_outbound_message**
> delete_outbound_message(id)

Delete message

Delete a single message.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Delete message
        api_instance.delete_outbound_message(id)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_outbound_messages_bulk**
> delete_outbound_messages_bulk(delete_outbound_messages_bulk_input_object)

Delete messages (bulk)

Delete outbound messages by the given ID(s) or delete all outbound messages.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.delete_outbound_messages_bulk_request import DeleteOutboundMessagesBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    delete_outbound_messages_bulk_input_object = TextMagic.DeleteOutboundMessagesBulkRequest() # DeleteOutboundMessagesBulkRequest | 

    try:
        # Delete messages (bulk)
        api_instance.delete_outbound_messages_bulk(delete_outbound_messages_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->delete_outbound_messages_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_outbound_messages_bulk_input_object** | [**DeleteOutboundMessagesBulkRequest**](DeleteOutboundMessagesBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_message**
> delete_scheduled_message(id)

Delete a single scheduled message

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Delete a single scheduled message
        api_instance.delete_scheduled_message(id)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scheduled_messages_bulk**
> delete_scheduled_messages_bulk(delete_scheduled_messages_bulk_input_object)

Delete scheduled messages (bulk)

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.delete_scheduled_messages_bulk_request import DeleteScheduledMessagesBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    delete_scheduled_messages_bulk_input_object = TextMagic.DeleteScheduledMessagesBulkRequest() # DeleteScheduledMessagesBulkRequest | 

    try:
        # Delete scheduled messages (bulk)
        api_instance.delete_scheduled_messages_bulk(delete_scheduled_messages_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->delete_scheduled_messages_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_scheduled_messages_bulk_input_object** | [**DeleteScheduledMessagesBulkRequest**](DeleteScheduledMessagesBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sender_id**
> delete_sender_id(id)

Delete a Sender ID

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Delete a Sender ID
        api_instance.delete_sender_id(id)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful delete chat. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_template**
> delete_template(id)

Delete a template

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Delete a template
        api_instance.delete_template(id)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_templates_bulk**
> delete_templates_bulk(delete_templates_bulk_input_object)

Delete templates (bulk)

Delete templates by given IDs or delete all templates.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.delete_contact_notes_bulk_request import DeleteContactNotesBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    delete_templates_bulk_input_object = TextMagic.DeleteContactNotesBulkRequest() # DeleteContactNotesBulkRequest | 

    try:
        # Delete templates (bulk)
        api_instance.delete_templates_bulk(delete_templates_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->delete_templates_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_templates_bulk_input_object** | [**DeleteContactNotesBulkRequest**](DeleteContactNotesBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_carrier_lookup**
> DoCarrierLookupResponse do_carrier_lookup(phone, country=country)

Carrier Lookup

This API call allows you to retrieve additional information about a phone number: region-specific phone number formatting, carrier, phone type (landline/mobile) and country information.

> Numbers must be checked one by one. You cannot check multiple numbers in one request.
 


### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.do_carrier_lookup_response import DoCarrierLookupResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    phone = '447860021130' # str | Phone number in [E.164 format](https://en.wikipedia.org/wiki/E.164) or in [National format](https://en.wikipedia.org/wiki/National_conventions_for_writing_telephone_numbers). 
    country = 'GB' # str | This option must be specified only if the phone number is in a **[National format](https://en.wikipedia.org/wiki/National_conventions_for_writing_telephone_numbers)**.  (optional)

    try:
        # Carrier Lookup
        api_response = api_instance.do_carrier_lookup(phone, country=country)
        print("The response of TextMagicApi->do_carrier_lookup:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**429** | Returned when the number of queries per second is too high. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **do_email_lookup**
> DoEmailLookupResponse do_email_lookup(email)

Email Lookup

To get more details about an email address or to check whether it is a valid email or not, you can use the Email Lookup command. To upload and check emails in bulk, please use our [Web app](https://my.textmagic.com/online/email-lookup/).

This API call allows you to retrieve additional information about an email address, such as mailbox detection, syntax checks, DNS validation, deliverability status, and many more helpful values (see the table below).

> Emails must be checked one by one. You cannot check multiple emails in one request. To upload and check emails in bulk, please use our [Web app](https://my.textmagic.com/online/email-lookup/).

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.do_email_lookup_response import DoEmailLookupResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    email = 'john@sample.com' # str | Email address.

    try:
        # Email Lookup
        api_response = api_instance.do_email_lookup(email)
        print("The response of TextMagicApi->do_email_lookup:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_bulk_sessions**
> GetAllBulkSessionsPaginatedResponse get_all_bulk_sessions(page=page, limit=limit)

Get all bulk sessions

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_all_bulk_sessions_paginated_response import GetAllBulkSessionsPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)

    try:
        # Get all bulk sessions
        api_response = api_instance.get_all_bulk_sessions(page=page, limit=limit)
        print("The response of TextMagicApi->get_all_bulk_sessions:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_chats**
> GetAllChatsPaginatedResponse get_all_chats(status=status, page=page, limit=limit, order_by=order_by, voice=voice, flat=flat)

Get all chats

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_all_chats_paginated_response import GetAllChatsPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    status = 'a' # str | Fetch only (a)ctive, (c)losed or (d)eleted chats. (optional)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    order_by = id # str | Order results by some field. Default is id. (optional) (default to id)
    voice = 0 # int | Fetch results with voice calls. (optional) (default to 0)
    flat = 0 # int | Should additional contact info be included? (optional) (default to 0)

    try:
        # Get all chats
        api_response = api_instance.get_all_chats(status=status, page=page, limit=limit, order_by=order_by, voice=voice, flat=flat)
        print("The response of TextMagicApi->get_all_chats:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_inbound_messages**
> GetAllInboundMessagesPaginatedResponse get_all_inbound_messages(page=page, limit=limit, order_by=order_by, direction=direction)

Get all inbound messages

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_all_inbound_messages_paginated_response import GetAllInboundMessagesPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    order_by = id # str | Order results by some field. Default is id. (optional) (default to id)
    direction = desc # str | Order direction. Default is desc. (optional) (default to desc)

    try:
        # Get all inbound messages
        api_response = api_instance.get_all_inbound_messages(page=page, limit=limit, order_by=order_by, direction=direction)
        print("The response of TextMagicApi->get_all_inbound_messages:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_message_sessions**
> GetAllMessageSessionsPaginatedResponse get_all_message_sessions(page=page, limit=limit)

Get all sessions

Get all message sending sessions.
> This list contains all of your sessions, including those which were sent but not via API


### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_all_message_sessions_paginated_response import GetAllMessageSessionsPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)

    try:
        # Get all sessions
        api_response = api_instance.get_all_message_sessions(page=page, limit=limit)
        print("The response of TextMagicApi->get_all_message_sessions:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_outbound_messages**
> GetAllOutboundMessagesPaginatedResponse get_all_outbound_messages(page=page, limit=limit, last_id=last_id)

Get all messages

Get all user oubound messages.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_all_outbound_messages_paginated_response import GetAllOutboundMessagesPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    last_id = 56 # int | Filter results by ID, selecting all values lesser than the specified ID. Note that the \\'page\\' parameter is ignored when \\'lastId\\' is specified. (optional)

    try:
        # Get all messages
        api_response = api_instance.get_all_outbound_messages(page=page, limit=limit, last_id=last_id)
        print("The response of TextMagicApi->get_all_outbound_messages:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_scheduled_messages**
> GetAllScheduledMessagesPaginatedResponse get_all_scheduled_messages(page=page, limit=limit, status=status, order_by=order_by, direction=direction)

Get all scheduled messages

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_all_scheduled_messages_paginated_response import GetAllScheduledMessagesPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    status = x # str | Fetch schedules with a specific status: a - actual, c - completed, x - all. (optional) (default to x)
    order_by = id # str | Order results by some field. Default is id. (optional) (default to id)
    direction = desc # str | Order direction. Default is desc. (optional) (default to desc)

    try:
        # Get all scheduled messages
        api_response = api_instance.get_all_scheduled_messages(page=page, limit=limit, status=status, order_by=order_by, direction=direction)
        print("The response of TextMagicApi->get_all_scheduled_messages:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_templates**
> GetAllTemplatesPaginatedResponse get_all_templates(page=page, limit=limit)

Get all templates

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_all_templates_paginated_response import GetAllTemplatesPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional)
    limit = 10 # int | The number of results per page. (optional)

    try:
        # Get all templates
        api_response = api_instance.get_all_templates(page=page, limit=limit)
        print("The response of TextMagicApi->get_all_templates:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_dedicated_numbers**
> GetAvailableDedicatedNumbersResponse get_available_dedicated_numbers(country, prefix=prefix, tollfree=tollfree)

Find dedicated numbers available for purchase

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_available_dedicated_numbers_response import GetAvailableDedicatedNumbersResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    country = 'GB' # str | The 2-letter dedicated number country ISO code.
    prefix = 447155 # int | Desired number prefix. Should include the country code (i.e. 447 for UK phone number format). Leave blank to get all the available numbers for the specified country. (optional)
    tollfree = 0 # int | Should we show only tollfree numbers (tollfree available only for US). (optional) (default to 0)

    try:
        # Find dedicated numbers available for purchase
        api_response = api_instance.get_available_dedicated_numbers(country, prefix=prefix, tollfree=tollfree)
        print("The response of TextMagicApi->get_available_dedicated_numbers:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of available to buy dedicated numbers. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_sender_setting_options**
> GetAvailableSenderSettingOptionsResponse get_available_sender_setting_options(country=country)

Get available sender settings

Get all available sender setting options which can be used in the "from" parameter of the POST messages method.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_available_sender_setting_options_response import GetAvailableSenderSettingOptionsResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    country = 'US' # str | The 2-letter ISO country ID. If not specified, it returns all the available sender settings. (optional)

    try:
        # Get available sender settings
        api_response = api_instance.get_available_sender_setting_options(country=country)
        print("The response of TextMagicApi->get_available_sender_setting_options:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Available sender setting options returned with success. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_notification_options**
> GetBalanceNotificationOptionsResponse get_balance_notification_options()

Returns the list of available balance options which can be used as a bound to determine when to send email to user with low balance notification. See https://my.textmagic.com/online/account/notifications/balance

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_balance_notification_options_response import GetBalanceNotificationOptionsResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)

    try:
        # Returns the list of available balance options which can be used as a bound to determine when to send email to user with low balance notification. See https://my.textmagic.com/online/account/notifications/balance
        api_response = api_instance.get_balance_notification_options()
        print("The response of TextMagicApi->get_balance_notification_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->get_balance_notification_options: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetBalanceNotificationOptionsResponse**](GetBalanceNotificationOptionsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when the list of available balance options have been received with success. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balance_notification_settings**
> GetBalanceNotificationSettingsResponse get_balance_notification_settings()

Get balance notification settings

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_balance_notification_settings_response import GetBalanceNotificationSettingsResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)

    try:
        # Get balance notification settings
        api_response = api_instance.get_balance_notification_settings()
        print("The response of TextMagicApi->get_balance_notification_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->get_balance_notification_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetBalanceNotificationSettingsResponse**](GetBalanceNotificationSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_blocked_contacts**
> GetBlockedContactsPaginatedResponse get_blocked_contacts(page=page, limit=limit, query=query, order_by=order_by, direction=direction)

Get blocked contacts

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_blocked_contacts_paginated_response import GetBlockedContactsPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    query = 'query_example' # str | Find blocked contacts by specified search query. (optional)
    order_by = id # str | Order results by some field. Default is id. (optional) (default to id)
    direction = desc # str | Order direction. Default is desc. (optional) (default to desc)

    try:
        # Get blocked contacts
        api_response = api_instance.get_blocked_contacts(page=page, limit=limit, query=query, order_by=order_by, direction=direction)
        print("The response of TextMagicApi->get_blocked_contacts:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bulk_session**
> BulkSession get_bulk_session(id)

Get bulk session status

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.bulk_session import BulkSession
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Get bulk session status
        api_response = api_instance.get_bulk_session(id)
        print("The response of TextMagicApi->get_bulk_session:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_callback_settings**
> GetCallbackSettingsResponse get_callback_settings()

Fetch callback URL settings

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_callback_settings_response import GetCallbackSettingsResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)

    try:
        # Fetch callback URL settings
        api_response = api_instance.get_callback_settings()
        print("The response of TextMagicApi->get_callback_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->get_callback_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetCallbackSettingsResponse**](GetCallbackSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Callback settings has been returned with success. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat**
> Chat get_chat(id)

Get a single chat

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.chat import Chat
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Get a single chat
        api_response = api_instance.get_chat(id)
        print("The response of TextMagicApi->get_chat:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_by_phone**
> Chat get_chat_by_phone(phone, upsert=upsert, reopen=reopen)

Find chats by phone

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.chat import Chat
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    phone = '447860021130' # str | 
    upsert = 0 # int | Create a new chat if not found. (optional) (default to 0)
    reopen = 0 # int | Reopen chat if found or do not change status. (optional) (default to 0)

    try:
        # Find chats by phone
        api_response = api_instance.get_chat_by_phone(phone, upsert=upsert, reopen=reopen)
        print("The response of TextMagicApi->get_chat_by_phone:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat_messages**
> GetChatMessagesPaginatedResponse get_chat_messages(id, page=page, limit=limit, query=query, start=start, end=end, direction=direction, voice=voice, include_notes=include_notes)

Get chat messages

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_chat_messages_paginated_response import GetChatMessagesPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    query = 'query_example' # str | Find messages by specified search query. (optional)
    start = 'start_example' # str | Return messages since specified timestamp only. Required when `end` parameter specified. (optional)
    end = 'end_example' # str | Return messages up to specified timestamp only. Required when `start` parameter specified. (optional)
    direction = desc # str | Order direction. Default is desc. (optional) (default to desc)
    voice = 0 # int | Fetch results with voice calls. (optional) (default to 0)
    include_notes = 0 # int | Fetch results with messenger notes. (optional) (default to 0)

    try:
        # Get chat messages
        api_response = api_instance.get_chat_messages(id, page=page, limit=limit, query=query, start=start, end=end, direction=direction, voice=voice, include_notes=include_notes)
        print("The response of TextMagicApi->get_chat_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->get_chat_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Fetch specified results page. | [optional] [default to 1]
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **query** | **str**| Find messages by specified search query. | [optional] 
 **start** | **str**| Return messages since specified timestamp only. Required when &#x60;end&#x60; parameter specified. | [optional] 
 **end** | **str**| Return messages up to specified timestamp only. Required when &#x60;start&#x60; parameter specified. | [optional] 
 **direction** | **str**| Order direction. Default is desc. | [optional] [default to desc]
 **voice** | **int**| Fetch results with voice calls. | [optional] [default to 0]
 **include_notes** | **int**| Fetch results with messenger notes. | [optional] [default to 0]

### Return type

[**GetChatMessagesPaginatedResponse**](GetChatMessagesPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**400** | Returned when invalid phone number specified. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact**
> Contact get_contact(id)

Get the details of a specific contact

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.contact import Contact
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | Contact ID.

    try:
        # Get the details of a specific contact
        api_response = api_instance.get_contact(id)
        print("The response of TextMagicApi->get_contact:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact data received with success. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_by_phone**
> Contact get_contact_by_phone(phone)

Get the details of a specific contact by phone number

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.contact import Contact
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    phone = '447860021130' # str | 

    try:
        # Get the details of a specific contact by phone number
        api_response = api_instance.get_contact_by_phone(phone)
        print("The response of TextMagicApi->get_contact_by_phone:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contact data has been returned with success. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_if_blocked**
> Contact get_contact_if_blocked(phone)

Check if a phone number is blocked

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.contact import Contact
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    phone = '447860021130' # str | Phone number to check.

    try:
        # Check if a phone number is blocked
        api_response = api_instance.get_contact_if_blocked(phone)
        print("The response of TextMagicApi->get_contact_if_blocked:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when contact is blocked. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | When the contact is not blocked. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_import_session_progress**
> GetContactImportSessionProgressResponse get_contact_import_session_progress(id)

Check import progress

Get contact import session progress.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_contact_import_session_progress_response import GetContactImportSessionProgressResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Check import progress
        api_response = api_instance.get_contact_import_session_progress(id)
        print("The response of TextMagicApi->get_contact_import_session_progress:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_note**
> ContactNote get_contact_note(id)

Get a contact note

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.contact_note import ContactNote
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Get a contact note
        api_response = api_instance.get_contact_note(id)
        print("The response of TextMagicApi->get_contact_note:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contact_notes**
> GetContactNotesPaginatedResponse get_contact_notes(id, page=page, limit=limit)

Fetch notes assigned to a given contact

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_contact_notes_paginated_response import GetContactNotesPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)

    try:
        # Fetch notes assigned to a given contact
        api_response = api_instance.get_contact_notes(id, page=page, limit=limit)
        print("The response of TextMagicApi->get_contact_notes:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts**
> GetContactsPaginatedResponse get_contacts(page=page, limit=limit, shared=shared, order_by=order_by, direction=direction)

Get all contacts

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_contacts_paginated_response import GetContactsPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    shared = 0 # int | Should shared contacts be included? (optional) (default to 0)
    order_by = id # str | Order results by some field. Default is id. (optional) (default to id)
    direction = desc # str | Order direction. Default is desc. (optional) (default to desc)

    try:
        # Get all contacts
        api_response = api_instance.get_contacts(page=page, limit=limit, shared=shared, order_by=order_by, direction=direction)
        print("The response of TextMagicApi->get_contacts:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested contacts have been returned with success. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts_autocomplete**
> List[GetContactsAutocompleteResponseItem] get_contacts_autocomplete(query, limit=limit, lists=lists)

Get contacts autocomplete suggestions

Get contacts autocomplete suggestions by given search terms.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_contacts_autocomplete_response_item import GetContactsAutocompleteResponseItem
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    query = 'A' # str | Find recipients by specified search query.
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    lists = 0 # int | Should lists be returned or not? (optional) (default to 0)

    try:
        # Get contacts autocomplete suggestions
        api_response = api_instance.get_contacts_autocomplete(query, limit=limit, lists=lists)
        print("The response of TextMagicApi->get_contacts_autocomplete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->get_contacts_autocomplete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Find recipients by specified search query. | 
 **limit** | **int**| The number of results per page. | [optional] [default to 10]
 **lists** | **int**| Should lists be returned or not? | [optional] [default to 0]

### Return type

[**List[GetContactsAutocompleteResponseItem]**](GetContactsAutocompleteResponseItem.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Autocomplete data has been returned with success. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contacts_by_list_id**
> GetContactsByListIdPaginatedResponse get_contacts_by_list_id(id, page=page, limit=limit, order_by=order_by, direction=direction)

Get all contacts in a list

A useful synonym for the "contacts/search" command with the provided "listId" parameter.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_contacts_by_list_id_paginated_response import GetContactsByListIdPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | Given group ID.
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    order_by = id # str | Order results by some field. Default is id. (optional) (default to id)
    direction = desc # str | Order direction. Default is desc. (optional) (default to desc)

    try:
        # Get all contacts in a list
        api_response = api_instance.get_contacts_by_list_id(id, page=page, limit=limit, order_by=order_by, direction=direction)
        print("The response of TextMagicApi->get_contacts_by_list_id:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries**
> List[Country] get_countries()

Get countries

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.country import Country
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)

    try:
        # Get countries
        api_response = api_instance.get_countries()
        print("The response of TextMagicApi->get_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->get_countries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Country]**](Country.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user**
> User get_current_user()

Get current account information

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.user import User
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)

    try:
        # Get current account information
        api_response = api_instance.get_current_user()
        print("The response of TextMagicApi->get_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->get_current_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_field**
> UserCustomField get_custom_field(id)

Get the details of a specific custom field

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.user_custom_field import UserCustomField
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Get the details of a specific custom field
        api_response = api_instance.get_custom_field(id)
        print("The response of TextMagicApi->get_custom_field:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_fields**
> GetCustomFieldsPaginatedResponse get_custom_fields(page=page, limit=limit)

Get all custom fields

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_custom_fields_paginated_response import GetCustomFieldsPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)

    try:
        # Get all custom fields
        api_response = api_instance.get_custom_fields(page=page, limit=limit)
        print("The response of TextMagicApi->get_custom_fields:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested custom fields have been returned with success. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dedicated_number**
> UsersInbound get_dedicated_number(id)

Get the details of a specific dedicated number

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.users_inbound import UsersInbound
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Get the details of a specific dedicated number
        api_response = api_instance.get_dedicated_number(id)
        print("The response of TextMagicApi->get_dedicated_number:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested dedicated number data returned with success. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_senders**
> GetEmailSendersResponse get_email_senders(domain_id=domain_id)

Get list of email senders

Retrieves a list of configured email senders available for creating email campaigns.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_email_senders_response import GetEmailSendersResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    domain_id = 56 # int | Filter email senders by specific domain ID. (optional)

    try:
        # Get list of email senders
        api_response = api_instance.get_email_senders(domain_id=domain_id)
        print("The response of TextMagicApi->get_email_senders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->get_email_senders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **int**| Filter email senders by specific domain ID. | [optional] 

### Return type

[**GetEmailSendersResponse**](GetEmailSendersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Email senders retrieved successfully. |  -  |
**400** | Bad request - invalid query parameters. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_favorites**
> GetFavoritesPaginatedResponse get_favorites(page=page, limit=limit, query=query)

Get favorite contacts and lists

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_favorites_paginated_response import GetFavoritesPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    query = 'A' # str | Find contacts or lists by specified search query. (optional)

    try:
        # Get favorite contacts and lists
        api_response = api_instance.get_favorites(page=page, limit=limit, query=query)
        print("The response of TextMagicApi->get_favorites:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Favorite entities have been returned with success. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_message**
> MessageIn get_inbound_message(id)

Get a single inbound message

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.message_in import MessageIn
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1782832 # int | The unique numeric ID for the inbound message.

    try:
        # Get a single inbound message
        api_response = api_instance.get_inbound_message(id)
        print("The response of TextMagicApi->get_inbound_message:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inbound_messages_notification_settings**
> GetInboundMessagesNotificationSettingsResponse get_inbound_messages_notification_settings()

Get inbound messages notification settings

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_inbound_messages_notification_settings_response import GetInboundMessagesNotificationSettingsResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)

    try:
        # Get inbound messages notification settings
        api_response = api_instance.get_inbound_messages_notification_settings()
        print("The response of TextMagicApi->get_inbound_messages_notification_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->get_inbound_messages_notification_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetInboundMessagesNotificationSettingsResponse**](GetInboundMessagesNotificationSettingsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when success. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> GetInvoicesPaginatedResponse get_invoices(page=page, limit=limit)

Get all invoices

With the TextMagic API, you can check the invoices and transactions for your account.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_invoices_paginated_response import GetInvoicesPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)

    try:
        # Get all invoices
        api_response = api_instance.get_invoices(page=page, limit=limit)
        print("The response of TextMagicApi->get_invoices:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Returned when the current user is not allowed to manage invoices. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list**
> List get_list(id)

Get the details of a specific list

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.list import List
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Get the details of a specific list
        api_response = api_instance.get_list(id)
        print("The response of TextMagicApi->get_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->get_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**List**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_contacts_ids**
> List[int] get_list_contacts_ids(id)

Get all contact IDs in a list

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Get all contact IDs in a list
        api_response = api_instance.get_list_contacts_ids(id)
        print("The response of TextMagicApi->get_list_contacts_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->get_list_contacts_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**List[int]**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lists**
> GetListsPaginatedResponse get_lists(page=page, limit=limit, order_by=order_by, direction=direction, favorite_only=favorite_only, only_mine=only_mine)

Get all lists

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_lists_paginated_response import GetListsPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | The current fetched page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    order_by = id # str | Order results by some field. Default is id. (optional) (default to id)
    direction = desc # str | Order direction. Default is desc. (optional) (default to desc)
    favorite_only = 0 # int | Return only favorited lists. (optional) (default to 0)
    only_mine = 0 # int | Return only current user lists. (optional) (default to 0)

    try:
        # Get all lists
        api_response = api_instance.get_lists(page=page, limit=limit, order_by=order_by, direction=direction, favorite_only=favorite_only, only_mine=only_mine)
        print("The response of TextMagicApi->get_lists:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lists_of_contact**
> GetListsOfContactPaginatedResponse get_lists_of_contact(id, page=page, limit=limit)

Get a contact's lists

Get all the lists in which a contact is included.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_lists_of_contact_paginated_response import GetListsOfContactPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)

    try:
        # Get a contact's lists
        api_response = api_instance.get_lists_of_contact(id, page=page, limit=limit)
        print("The response of TextMagicApi->get_lists_of_contact:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_preview**
> GetMessagePreviewResponse get_message_preview(text=text, template_id=template_id, sending_time=sending_time, sending_date_time=sending_date_time, sending_timezone=sending_timezone, contacts=contacts, lists=lists, phones=phones, cut_extra=cut_extra, parts_count=parts_count, reference_id=reference_id, var_from=var_from, rule=rule, create_chat=create_chat, tts=tts, local=local, local_country=local_country)

Preview message

Get a messages preview (with dynamic fields merged) of up to 100 messages per session.


### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_message_preview_response import GetMessagePreviewResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    text = 'Test message test' # str | Message text. Required if **template_id** is not set. (optional)
    template_id = 1 # int | Template used instead of message text. Required if **text** is not set. (optional)
    sending_time = 1565606455 # int | DEPRECATED, consider using sendingDateTime and sendingTimezone parameters instead: Optional (required with rrule set). Message sending time is in unix timestamp format. Default is now. (optional)
    sending_date_time = '2020-05-27 13:02:33' # str | Sending time is in Y-m-d H:i:s format (e.g. 2016-05-27 13:02:33). This time is relative to the sendingTimezone. (optional)
    sending_timezone = 'America/Buenos_Aires' # str | The ID or ISO-name of the timezone used for sending when the sendingDateTime parameter is set, e.g. if you specify sendingDateTime = \\\"2016-05-27 13:02:33\\\" and sendingTimezone = \\\"America/Buenos_Aires\\\", your message will be sent on May 27, 2016 13:02:33 Buenos Aires time, or 16:02:33 UTC. Default is the account timezone. (optional)
    contacts = '1,2,3,4' # str | Comma-separated array of contact resources id message will be sent to. (optional)
    lists = '1,2,3,4' # str | Comma-separated array of list resources id message will be sent to. (optional)
    phones = '447860021130,447860021131' # str | Comma-separated array of E.164 phone numbers message will be sent to. (optional)
    cut_extra = 0 # int | Should sending method cut extra characters which not fit supplied partsCount or return 400 Bad request response instead. (optional) (default to 0)
    parts_count = 6 # int | Maximum message parts count (Textmagic allows sending of 1 to 6 message parts). (optional) (default to 6)
    reference_id = 1 # int | Custom message reference id which can be used in your application infrastructure. (optional)
    var_from = 'Test Sender ID' # str | One of the allowed Sender ID (phone number or alphanumeric sender ID). If the specified Sender ID is not allowed for some destinations, a fallback default Sender ID will be used to ensure delivery. See [Get timezones](https://docs.textmagic.com/#tag/Sender-IDs). (optional)
    rule = 'FREQ=YEARLY;BYMONTH=1;BYMONTHDAY=1;COUNT=1' # str | An iCal RRULE parameter to create recurrent scheduled messages. When used, sendingTime is mandatory as the start point of sending. See https://www.textmagic.com/free-tools/rrule-generator for format details. (optional)
    create_chat = 0 # int | Should the sending method try to create new Chat(if not exist) with specified recipients? (optional) (default to 0)
    tts = 0 # int | Send Text-to-Speech message. (optional) (default to 0)
    local = 0 # int | Treat phone numbers passed in the \\'phones\\' field as local. (optional) (default to 0)
    local_country = 'US' # str | The 2-letter ISO country code for local phone numbers, used when \\'local\\' is set to true. Default is the account country. (optional)

    try:
        # Preview message
        api_response = api_instance.get_message_preview(text=text, template_id=template_id, sending_time=sending_time, sending_date_time=sending_date_time, sending_timezone=sending_timezone, contacts=contacts, lists=lists, phones=phones, cut_extra=cut_extra, parts_count=parts_count, reference_id=reference_id, var_from=var_from, rule=rule, create_chat=create_chat, tts=tts, local=local, local_country=local_country)
        print("The response of TextMagicApi->get_message_preview:\n")
        pprint(api_response)
    except Exception as e:
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
 **parts_count** | **int**| Maximum message parts count (Textmagic allows sending of 1 to 6 message parts). | [optional] [default to 6]
 **reference_id** | **int**| Custom message reference id which can be used in your application infrastructure. | [optional] 
 **var_from** | **str**| One of the allowed Sender ID (phone number or alphanumeric sender ID). If the specified Sender ID is not allowed for some destinations, a fallback default Sender ID will be used to ensure delivery. See [Get timezones](https://docs.textmagic.com/#tag/Sender-IDs). | [optional] 
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_price**
> GetMessagePriceResponse get_message_price(include_blocked=include_blocked, text=text, template_id=template_id, sending_time=sending_time, sending_date_time=sending_date_time, sending_timezone=sending_timezone, contacts=contacts, lists=lists, phones=phones, cut_extra=cut_extra, parts_count=parts_count, reference_id=reference_id, var_from=var_from, rule=rule, create_chat=create_chat, tts=tts, local=local, local_country=local_country)

Check message price

Check pricing for a new outbound message.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_message_price_response import GetMessagePriceResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    include_blocked = 0 # int | Should we show the pricing for blocked contacts? (optional) (default to 0)
    text = 'Test message test' # str | Message text. Required if the **template_id** is not set. (optional)
    template_id = 1 # int | Template used instead of message text. Required if the **text** is not set. (optional)
    sending_time = 1565606455 # int | DEPRECATED, consider using the sendingDateTime and sendingTimezone parameters instead: optional (required with rrule set). Message sending time is in unix timestamp format. Default is now. (optional)
    sending_date_time = '2020-05-27 13:02:33' # str | Sending time is in Y-m-d H:i:s format (e.g. 2016-05-27 13:02:33). This time is relative to the sendingTimezone. (optional)
    sending_timezone = 'America/Buenos_Aires' # str | The ID or ISO-name of the timezone used for sending when sendingDateTime parameter is set, e.g. if you specify sendingDateTime = \\\"2016-05-27 13:02:33\\\" and sendingTimezone = \\\"America/Buenos_Aires\\\", your message will be sent on May 27, 2016 13:02:33 Buenos Aires time, or 16:02:33 UTC. Default is the account timezone. (optional)
    contacts = '1,2,3,4' # str | Comma-separated array of contact resources id message will be sent to. (optional)
    lists = '1,2,3,4' # str | Comma-separated array of list resources id message will be sent to. (optional)
    phones = '447860021130,447860021131' # str | Comma-separated array of E.164 phone numbers message will be sent to. (optional)
    cut_extra = 0 # int | Should sending method cut extra characters which not fit supplied partsCount or return 400 Bad request response instead. (optional) (default to 0)
    parts_count = 6 # int | Maximum message parts count (Textmagic allows sending 1 to 6 message parts). (optional) (default to 6)
    reference_id = 1 # int | Custom message reference id which can be used in your application infrastructure. (optional)
    var_from = 'Test Sender ID' # str | One of the allowed Sender ID (phone number or alphanumeric sender ID). If the specified Sender ID is not allowed for some destinations, a fallback default Sender ID will be used to ensure delivery. See [Get timezones](https://docs.textmagic.com/#tag/Sender-IDs). (optional)
    rule = 'FREQ=YEARLY;BYMONTH=1;BYMONTHDAY=1;COUNT=1' # str | An iCal RRULE parameter to create recurrent scheduled messages. When used, sendingTime is mandatory as the start point of sending. See https://www.textmagic.com/free-tools/rrule-generator for format details. (optional)
    create_chat = 0 # int | Should the sending method try to create new Chat (if not exist) with specified recipients? (optional) (default to 0)
    tts = 0 # int | Send a Text-to-Speech message. (optional) (default to 0)
    local = 0 # int | Treat phone numbers passed in the \\'phones\\' field as local. (optional) (default to 0)
    local_country = 'US' # str | The 2-letter ISO country code for local phone numbers, used when \\'local\\' is set to true. Default is the account country. (optional)

    try:
        # Check message price
        api_response = api_instance.get_message_price(include_blocked=include_blocked, text=text, template_id=template_id, sending_time=sending_time, sending_date_time=sending_date_time, sending_timezone=sending_timezone, contacts=contacts, lists=lists, phones=phones, cut_extra=cut_extra, parts_count=parts_count, reference_id=reference_id, var_from=var_from, rule=rule, create_chat=create_chat, tts=tts, local=local, local_country=local_country)
        print("The response of TextMagicApi->get_message_price:\n")
        pprint(api_response)
    except Exception as e:
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
 **parts_count** | **int**| Maximum message parts count (Textmagic allows sending 1 to 6 message parts). | [optional] [default to 6]
 **reference_id** | **int**| Custom message reference id which can be used in your application infrastructure. | [optional] 
 **var_from** | **str**| One of the allowed Sender ID (phone number or alphanumeric sender ID). If the specified Sender ID is not allowed for some destinations, a fallback default Sender ID will be used to ensure delivery. See [Get timezones](https://docs.textmagic.com/#tag/Sender-IDs). | [optional] 
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_session**
> MessageSession get_message_session(id)

Get a session`s details

Get a specific session’s details.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.message_session import MessageSession
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | Session ID.

    try:
        # Get a session`s details
        api_response = api_instance.get_message_session(id)
        print("The response of TextMagicApi->get_message_session:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_session_stat**
> GetMessageSessionStatResponse get_message_session_stat(id, include_deleted=include_deleted)

Get a session`s statistics

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_message_session_stat_response import GetMessageSessionStatResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    include_deleted = 0 # int | Search also in deleted messages. (optional) (default to 0)

    try:
        # Get a session`s statistics
        api_response = api_instance.get_message_session_stat(id, include_deleted=include_deleted)
        print("The response of TextMagicApi->get_message_session_stat:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages_by_session_id**
> GetMessagesBySessionIdPaginatedResponse get_messages_by_session_id(id, page=page, limit=limit, statuses=statuses, include_deleted=include_deleted)

Get a session`s messages

A useful synonym for the "messages/search" command with the provided "sessionId" parameter.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_messages_by_session_id_paginated_response import GetMessagesBySessionIdPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    statuses = 'statuses_example' # str | Find messages by status. (optional)
    include_deleted = 0 # int | Search also in deleted messages. (optional) (default to 0)

    try:
        # Get a session`s messages
        api_response = api_instance.get_messages_by_session_id(id, page=page, limit=limit, statuses=statuses, include_deleted=include_deleted)
        print("The response of TextMagicApi->get_messages_by_session_id:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messaging_counters**
> GetMessagingCountersResponse get_messaging_counters()

Get sent/received messages counters values

Get total contacts, sent messages and received messages counters values.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_messaging_counters_response import GetMessagingCountersResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)

    try:
        # Get sent/received messages counters values
        api_response = api_instance.get_messaging_counters()
        print("The response of TextMagicApi->get_messaging_counters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->get_messaging_counters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetMessagingCountersResponse**](GetMessagingCountersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messaging_stat**
> List[MessagingStatItem] get_messaging_stat(by=by, start=start, end=end)

Get messaging statistics

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.messaging_stat_item import MessagingStatItem
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    by = off # str | *   **off** - to get total values per specified time interval; *   **day** - to show values grouped by day; *   **month** - to show values grouped by month; *   **year** - to show values grouped by year.  (optional) (default to off)
    start = 1430438400 # int | Time period start in [UNIX timestamp](https://en.wikipedia.org/wiki/Unix_time) format. The default is 7 days prior.  (optional)
    end = 1431648000 # int | Time period start in [UNIX timestamp](https://en.wikipedia.org/wiki/Unix_time) format. The default is today.  (optional)

    try:
        # Get messaging statistics
        api_response = api_instance.get_messaging_stat(by=by, start=start, end=end)
        print("The response of TextMagicApi->get_messaging_stat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->get_messaging_stat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **by** | **str**| *   **off** - to get total values per specified time interval; *   **day** - to show values grouped by day; *   **month** - to show values grouped by month; *   **year** - to show values grouped by year.  | [optional] [default to off]
 **start** | **int**| Time period start in [UNIX timestamp](https://en.wikipedia.org/wiki/Unix_time) format. The default is 7 days prior.  | [optional] 
 **end** | **int**| Time period start in [UNIX timestamp](https://en.wikipedia.org/wiki/Unix_time) format. The default is today.  | [optional] 

### Return type

[**List[MessagingStatItem]**](MessagingStatItem.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_message**
> MessageOut get_outbound_message(id)

Get a single message

Get a single outgoing message.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.message_out import MessageOut
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Get a single message
        api_response = api_instance.get_outbound_message(id)
        print("The response of TextMagicApi->get_outbound_message:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_outbound_messages_history**
> GetOutboundMessagesHistoryPaginatedResponse get_outbound_messages_history(limit=limit, last_id=last_id, query=query, order_by=order_by, direction=direction)

Get history

Get the outbound messages history.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_outbound_messages_history_paginated_response import GetOutboundMessagesHistoryPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    last_id = 56 # int | Filter results by ID, selecting all values lesser than the specified ID. (optional)
    query = 'query_example' # str | Find message by specified search query. (optional)
    order_by = id # str | Order results by some field. Default is id. (optional) (default to id)
    direction = desc # str | Order direction. Default is desc. (optional) (default to desc)

    try:
        # Get history
        api_response = api_instance.get_outbound_messages_history(limit=limit, last_id=last_id, query=query, order_by=order_by, direction=direction)
        print("The response of TextMagicApi->get_outbound_messages_history:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scheduled_message**
> MessagesIcs get_scheduled_message(id)

Get a single scheduled message

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.messages_ics import MessagesIcs
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Get a single scheduled message
        api_response = api_instance.get_scheduled_message(id)
        print("The response of TextMagicApi->get_scheduled_message:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender_id**
> SenderId get_sender_id(id)

Get the details of a specific Sender ID

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.sender_id import SenderId
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Get the details of a specific Sender ID
        api_response = api_instance.get_sender_id(id)
        print("The response of TextMagicApi->get_sender_id:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sender ID data returned with success. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender_ids**
> GetSenderIdsPaginatedResponse get_sender_ids(page=page, limit=limit)

Get all your approved Sender IDs

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_sender_ids_paginated_response import GetSenderIdsPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)

    try:
        # Get all your approved Sender IDs
        api_response = api_instance.get_sender_ids(page=page, limit=limit)
        print("The response of TextMagicApi->get_sender_ids:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sender IDs of the current user returned with success. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender_settings**
> GetSenderSettingsResponse get_sender_settings(country=country)

Get current sender settings

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_sender_settings_response import GetSenderSettingsResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    country = 'US' # str | Return sender settings enabled for sending to a specified country. Should be 2 upper-case characters. (optional)

    try:
        # Get current sender settings
        api_response = api_instance.get_sender_settings(country=country)
        print("The response of TextMagicApi->get_sender_settings:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sender settings returned with success. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spending_stat**
> GetSpendingStatPaginatedResponse get_spending_stat(page=page, limit=limit, start=start, end=end)

Get spending statistics

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_spending_stat_paginated_response import GetSpendingStatPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    start = '2018-11-11 11:11' # str | Time period start in [UNIX timestamp](https://en.wikipedia.org/wiki/Unix_time) format. The default is 7 days prior.  (optional)
    end = '2019-11-11 11:11' # str | Time period start in [UNIX timestamp](https://en.wikipedia.org/wiki/Unix_time) format. The default is today.  (optional)

    try:
        # Get spending statistics
        api_response = api_instance.get_spending_stat(page=page, limit=limit, start=start, end=end)
        print("The response of TextMagicApi->get_spending_stat:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_template**
> MessageTemplate get_template(id)

Get a template`s details

Get a single template.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.message_template import MessageTemplate
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Get a template`s details
        api_response = api_instance.get_template(id)
        print("The response of TextMagicApi->get_template:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_timezones**
> object get_timezones(full=full)

Get timezones

Return all available timezone IDs

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    full = 0 # int | Return full info about timezones in array (0 or 1). Default is 0. (optional) (default to 0)

    try:
        # Get timezones
        api_response = api_instance.get_timezones(full=full)
        print("The response of TextMagicApi->get_timezones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->get_timezones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **full** | **int**| Return full info about timezones in array (0 or 1). Default is 0. | [optional] [default to 0]

### Return type

**object**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unread_messages_total**
> GetUnreadMessagesTotalResponse get_unread_messages_total()

Get unread messages number

Get the total amount of unread messages in the current user chats.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_unread_messages_total_response import GetUnreadMessagesTotalResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)

    try:
        # Get unread messages number
        api_response = api_instance.get_unread_messages_total()
        print("The response of TextMagicApi->get_unread_messages_total:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->get_unread_messages_total: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetUnreadMessagesTotalResponse**](GetUnreadMessagesTotalResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unsubscribed_contact**
> UnsubscribedContact get_unsubscribed_contact(id)

Get the details of a specific unsubscribed contact

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.unsubscribed_contact import UnsubscribedContact
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 

    try:
        # Get the details of a specific unsubscribed contact
        api_response = api_instance.get_unsubscribed_contact(id)
        print("The response of TextMagicApi->get_unsubscribed_contact:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unsubscribers**
> GetUnsubscribersPaginatedResponse get_unsubscribers(page=page, limit=limit)

Get all unsubscribed contacts

When one of your message recipients sends a request with one of the [STOP-words](https://www.textmagic.com/sms-stop-command/), they will be immediately opted-out of your send lists and their contact status will change to an unsubscribed contact. To retrieve information on all contacts who have unsubscribed status, use:


### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_unsubscribers_paginated_response import GetUnsubscribersPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)

    try:
        # Get all unsubscribed contacts
        api_response = api_instance.get_unsubscribers(page=page, limit=limit)
        print("The response of TextMagicApi->get_unsubscribers:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_dedicated_numbers**
> GetUserDedicatedNumbersPaginatedResponse get_user_dedicated_numbers(page=page, limit=limit, survey_id=survey_id)

Get all your dedicated numbers

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.get_user_dedicated_numbers_paginated_response import GetUserDedicatedNumbersPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    survey_id = 56 # int | Fetch only those numbers that are ready for the survey. (optional)

    try:
        # Get all your dedicated numbers
        api_response = api_instance.get_user_dedicated_numbers(page=page, limit=limit, survey_id=survey_id)
        print("The response of TextMagicApi->get_user_dedicated_numbers:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested data returned with success. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_contacts**
> ResourceLinkResponse import_contacts(column, file, list_id=list_id, list_name=list_name)

Import contacts

Import contacts from the CSV, XLS or XLSX file.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    column = '0:firstName;1:lastName;3:phone;4:email' # str | Import file column mapping. The string must contain sub-strings of mapping in format `columnNumber:field` glued by `;`. For example: `0:firstName;1:lastName;3:phone;4:email` where the value before `:` is a number of the column in the file, and the value after `:` is a field of the newly created contact or the ID of a custom field. Numbers of columns begin from zero. Allowed built-in contact fields are: `firstName`, `lastName`, `phone`, `email`. Existing of `phone` mapping is required. 
    file = None # bytearray | File containing contacts in csv or xls(x) formats.
    list_id = 443 # int | List that ID contacts will be imported to. Ignored if `listName` is specified.  (optional)
    list_name = 'A new list' # str | List name. This list will be created during import. If such name is already taken, an ordinal (1, 2, ...) will be added to the end. Ignored if `listId` is specified.  (optional)

    try:
        # Import contacts
        api_response = api_instance.import_contacts(column, file, list_id=list_id, list_name=list_name)
        print("The response of TextMagicApi->import_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->import_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **column** | **str**| Import file column mapping. The string must contain sub-strings of mapping in format &#x60;columnNumber:field&#x60; glued by &#x60;;&#x60;. For example: &#x60;0:firstName;1:lastName;3:phone;4:email&#x60; where the value before &#x60;:&#x60; is a number of the column in the file, and the value after &#x60;:&#x60; is a field of the newly created contact or the ID of a custom field. Numbers of columns begin from zero. Allowed built-in contact fields are: &#x60;firstName&#x60;, &#x60;lastName&#x60;, &#x60;phone&#x60;, &#x60;email&#x60;. Existing of &#x60;phone&#x60; mapping is required.  | 
 **file** | **bytearray**| File containing contacts in csv or xls(x) formats. | 
 **list_id** | **int**| List that ID contacts will be imported to. Ignored if &#x60;listName&#x60; is specified.  | [optional] 
 **list_name** | **str**| List name. This list will be created during import. If such name is already taken, an ordinal (1, 2, ...) will be added to the end. Ignored if &#x60;listId&#x60; is specified.  | [optional] 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_chats_read_bulk**
> mark_chats_read_bulk(mark_chats_read_bulk_input_object)

Mark chats as read (bulk)

Mark several chats as read by chat IDs or mark all chats as read

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.mark_chats_unread_bulk_request import MarkChatsUnreadBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    mark_chats_read_bulk_input_object = TextMagic.MarkChatsUnreadBulkRequest() # MarkChatsUnreadBulkRequest | 

    try:
        # Mark chats as read (bulk)
        api_instance.mark_chats_read_bulk(mark_chats_read_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->mark_chats_read_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mark_chats_read_bulk_input_object** | [**MarkChatsUnreadBulkRequest**](MarkChatsUnreadBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mark_chats_unread_bulk**
> mark_chats_unread_bulk(mark_chats_unread_bulk_input_object)

Mark chats as unread (bulk)

Mark several chats as UNread by chat IDs or mark all chats as UNread

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.mark_chats_unread_bulk_request import MarkChatsUnreadBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    mark_chats_unread_bulk_input_object = TextMagic.MarkChatsUnreadBulkRequest() # MarkChatsUnreadBulkRequest | 

    try:
        # Mark chats as unread (bulk)
        api_instance.mark_chats_unread_bulk(mark_chats_unread_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->mark_chats_unread_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mark_chats_unread_bulk_input_object** | [**MarkChatsUnreadBulkRequest**](MarkChatsUnreadBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mute_chat**
> ResourceLinkResponse mute_chat(mute_chat_input_object)

Mute chat sounds

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.mute_chat_request import MuteChatRequest
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    mute_chat_input_object = TextMagic.MuteChatRequest() # MuteChatRequest | 

    try:
        # Mute chat sounds
        api_response = api_instance.mute_chat(mute_chat_input_object)
        print("The response of TextMagicApi->mute_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->mute_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mute_chat_input_object** | [**MuteChatRequest**](MuteChatRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mute_chats_bulk**
> mute_chats_bulk(mute_chats_bulk_input_object)

Mute chats (bulk)

Mute several chats by chat ids or mute all chats.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.mute_chats_bulk_request import MuteChatsBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    mute_chats_bulk_input_object = TextMagic.MuteChatsBulkRequest() # MuteChatsBulkRequest | 

    try:
        # Mute chats (bulk)
        api_instance.mute_chats_bulk(mute_chats_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->mute_chats_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mute_chats_bulk_input_object** | [**MuteChatsBulkRequest**](MuteChatsBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping**
> PingResponse ping()

Ping

Make a simple ping request.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.ping_response import PingResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)

    try:
        # Ping
        api_response = api_instance.ping()
        print("The response of TextMagicApi->ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**PingResponse**](PingResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reopen_chats_bulk**
> reopen_chats_bulk(reopen_chats_bulk_input_object)

Reopen chats (bulk)

Reopen chats by chat IDs or reopen all chats

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.mark_chats_unread_bulk_request import MarkChatsUnreadBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    reopen_chats_bulk_input_object = TextMagic.MarkChatsUnreadBulkRequest() # MarkChatsUnreadBulkRequest | 

    try:
        # Reopen chats (bulk)
        api_instance.reopen_chats_bulk(reopen_chats_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->reopen_chats_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reopen_chats_bulk_input_object** | [**MarkChatsUnreadBulkRequest**](MarkChatsUnreadBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_sender_id**
> ResourceLinkResponse request_sender_id(request_sender_id_input_object)

Apply for a new Sender ID

> Sender IDs are shared among all of your sub-accounts.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.request_sender_id_request import RequestSenderIdRequest
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    request_sender_id_input_object = TextMagic.RequestSenderIdRequest() # RequestSenderIdRequest | 

    try:
        # Apply for a new Sender ID
        api_response = api_instance.request_sender_id(request_sender_id_input_object)
        print("The response of TextMagicApi->request_sender_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->request_sender_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_sender_id_input_object** | [**RequestSenderIdRequest**](RequestSenderIdRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Sender ID request has been created with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_email_campaign**
> ScheduleEmailCampaignResponse schedule_email_campaign(schedule_email_campaign_input_object)

Schedule new email campaign

Creates a new scheduled email campaign that will be sent at a specified time or according to a recurring schedule.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.schedule_email_campaign_request import ScheduleEmailCampaignRequest
from TextMagic.models.schedule_email_campaign_response import ScheduleEmailCampaignResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    schedule_email_campaign_input_object = TextMagic.ScheduleEmailCampaignRequest() # ScheduleEmailCampaignRequest | 

    try:
        # Schedule new email campaign
        api_response = api_instance.schedule_email_campaign(schedule_email_campaign_input_object)
        print("The response of TextMagicApi->schedule_email_campaign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->schedule_email_campaign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_email_campaign_input_object** | [**ScheduleEmailCampaignRequest**](ScheduleEmailCampaignRequest.md)|  | 

### Return type

[**ScheduleEmailCampaignResponse**](ScheduleEmailCampaignResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Email campaign scheduled successfully. |  -  |
**400** | Bad request - validation errors, invalid schedule, or insufficient balance. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Forbidden - insufficient permissions (requires ComposeEmail access). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_chats**
> SearchChatsPaginatedResponse search_chats(page=page, limit=limit, query=query)

Find chats by message text

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.search_chats_paginated_response import SearchChatsPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    query = 'query_example' # str | Find chats by specified search query. (optional)

    try:
        # Find chats by message text
        api_response = api_instance.search_chats(page=page, limit=limit, query=query)
        print("The response of TextMagicApi->search_chats:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_chats_by_ids**
> SearchChatsByIdsPaginatedResponse search_chats_by_ids(page=page, limit=limit, ids=ids)

Find chats (bulk)

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.search_chats_by_ids_paginated_response import SearchChatsByIdsPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    ids = 'ids_example' # str | Find chats by ID(s). (optional)

    try:
        # Find chats (bulk)
        api_response = api_instance.search_chats_by_ids(page=page, limit=limit, ids=ids)
        print("The response of TextMagicApi->search_chats_by_ids:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_chats_by_receipent**
> SearchChatsByReceipentPaginatedResponse search_chats_by_receipent(page=page, limit=limit, query=query, order_by=order_by)

Find chats by recipient

Find chats by recipient (contact, list name or phone number).

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.search_chats_by_receipent_paginated_response import SearchChatsByReceipentPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    query = 'query_example' # str | Find chats by specified search query. (optional)
    order_by = id # str | Order results by some field. Default is id. (optional) (default to id)

    try:
        # Find chats by recipient
        api_response = api_instance.search_chats_by_receipent(page=page, limit=limit, query=query, order_by=order_by)
        print("The response of TextMagicApi->search_chats_by_receipent:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_contacts**
> SearchContactsPaginatedResponse search_contacts(page=page, limit=limit, shared=shared, ids=ids, list_id=list_id, include_blocked=include_blocked, query=query, local=local, exact_match=exact_match, country=country, order_by=order_by, direction=direction, tag_ids=tag_ids)

Find contacts by given criteria

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.search_contacts_paginated_response import SearchContactsPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    shared = 0 # int | Should shared contacts be included? (optional) (default to 0)
    ids = 'ids_example' # str | Find contacts by IDs. (optional)
    list_id = 56 # int | Find contacts by List ID. (optional)
    include_blocked = 56 # int | Should blocked contacts be included? (optional)
    query = 'query_example' # str | Find contacts by specified search query. (optional)
    local = 0 # int | Treat phone number passed in the \"query\" field as local. Default is 0. (optional) (default to 0)
    exact_match = 0 # int | Return only exactly matching contacts. Default is 0. (optional) (default to 0)
    country = 'country_example' # str | The 2-letter ISO country code for local phone numbers, used when \"local\" is set to true. Default is the account country. (optional)
    order_by = id # str | Order results by some field. Default is id. (optional) (default to id)
    direction = desc # str | Order direction. Default is desc. (optional) (default to desc)
    tag_ids = 'tag_ids_example' # str | Find contacts by tag ID(s). Multiple IDs can be separated by comma. (optional)

    try:
        # Find contacts by given criteria
        api_response = api_instance.search_contacts(page=page, limit=limit, shared=shared, ids=ids, list_id=list_id, include_blocked=include_blocked, query=query, local=local, exact_match=exact_match, country=country, order_by=order_by, direction=direction, tag_ids=tag_ids)
        print("The response of TextMagicApi->search_contacts:\n")
        pprint(api_response)
    except Exception as e:
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
 **exact_match** | **int**| Return only exactly matching contacts. Default is 0. | [optional] [default to 0]
 **country** | **str**| The 2-letter ISO country code for local phone numbers, used when \&quot;local\&quot; is set to true. Default is the account country. | [optional] 
 **order_by** | **str**| Order results by some field. Default is id. | [optional] [default to id]
 **direction** | **str**| Order direction. Default is desc. | [optional] [default to desc]
 **tag_ids** | **str**| Find contacts by tag ID(s). Multiple IDs can be separated by comma. | [optional] 

### Return type

[**SearchContactsPaginatedResponse**](SearchContactsPaginatedResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Found contacts have been returned with success. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_inbound_messages**
> SearchInboundMessagesPaginatedResponse search_inbound_messages(page=page, limit=limit, ids=ids, query=query, order_by=order_by, direction=direction, expand=expand)

Find inbound messages

Find inbound messages by given parameters.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.search_inbound_messages_paginated_response import SearchInboundMessagesPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    ids = 'ids_example' # str | Find message by ID(s). (optional)
    query = 'query_example' # str | Find recipients by specified search query. (optional)
    order_by = id # str | Order results by some field. Default is id. (optional) (default to id)
    direction = desc # str | Order direction. Default is desc. (optional) (default to desc)
    expand = 0 # int | Expand by adding firstName, lastName and contactId. (optional) (default to 0)

    try:
        # Find inbound messages
        api_response = api_instance.search_inbound_messages(page=page, limit=limit, ids=ids, query=query, order_by=order_by, direction=direction, expand=expand)
        print("The response of TextMagicApi->search_inbound_messages:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_lists**
> SearchListsPaginatedResponse search_lists(page=page, limit=limit, ids=ids, query=query, only_mine=only_mine, only_default=only_default, order_by=order_by, direction=direction)

Find lists by given criteria

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.search_lists_paginated_response import SearchListsPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    ids = '1,2,3,4' # str | Find lists by IDs. (optional)
    query = 'A' # str | Find lists by specified search query. (optional)
    only_mine = 0 # int | Return only current user lists. (optional) (default to 0)
    only_default = 0 # int | Return only default lists. (optional) (default to 0)
    order_by = id # str | Order results by some field. Default is id. (optional) (default to id)
    direction = desc # str | Order direction. Default is desc. (optional) (default to desc)

    try:
        # Find lists by given criteria
        api_response = api_instance.search_lists(page=page, limit=limit, ids=ids, query=query, only_mine=only_mine, only_default=only_default, order_by=order_by, direction=direction)
        print("The response of TextMagicApi->search_lists:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_outbound_messages**
> SearchOutboundMessagesPaginatedResponse search_outbound_messages(page=page, limit=limit, last_id=last_id, ids=ids, session_id=session_id, statuses=statuses, include_deleted=include_deleted, query=query)

Find messages

Find outbound messages by given parameters.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.search_outbound_messages_paginated_response import SearchOutboundMessagesPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    last_id = 56 # int | Filter results by ID, selecting all values lesser than the specified ID. Note that the \\'page\\' parameter is ignored when \\'lastId\\' is specified. (optional)
    ids = 'ids_example' # str | Find message by ID(s). (optional)
    session_id = 56 # int | Find messages by session ID. (optional)
    statuses = 'q' # str | Find messages by status. (optional)
    include_deleted = 0 # int | Search also in deleted messages. (optional) (default to 0)
    query = 'query_example' # str | Find messages by specified search query. (optional)

    try:
        # Find messages
        api_response = api_instance.search_outbound_messages(page=page, limit=limit, last_id=last_id, ids=ids, session_id=session_id, statuses=statuses, include_deleted=include_deleted, query=query)
        print("The response of TextMagicApi->search_outbound_messages:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_scheduled_messages**
> SearchScheduledMessagesPaginatedResponse search_scheduled_messages(page=page, limit=limit, query=query, ids=ids, status=status, order_by=order_by, direction=direction)

Find scheduled messages

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.search_scheduled_messages_paginated_response import SearchScheduledMessagesPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    query = 'query_example' # str | Find messages by specified search query. (optional)
    ids = 'ids_example' # str | Find schedules by ID(s). (optional)
    status = x # str | Fetch schedules with a specific status: a - actual, c - completed, x - all. (optional) (default to x)
    order_by = id # str | Order results by some field. Default is id. (optional) (default to id)
    direction = desc # str | Order direction. Default is desc. (optional) (default to desc)

    try:
        # Find scheduled messages
        api_response = api_instance.search_scheduled_messages(page=page, limit=limit, query=query, ids=ids, status=status, order_by=order_by, direction=direction)
        print("The response of TextMagicApi->search_scheduled_messages:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_templates**
> SearchTemplatesPaginatedResponse search_templates(page=page, limit=limit, ids=ids, name=name, content=content)

Find templates by criteria

Find user templates by given parameters.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.search_templates_paginated_response import SearchTemplatesPaginatedResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    page = 1 # int | Fetch specified results page. (optional) (default to 1)
    limit = 10 # int | The number of results per page. (optional) (default to 10)
    ids = 'ids_example' # str | Find template by ID(s). (optional)
    name = 'name_example' # str | Find template by name. (optional)
    content = 'content_example' # str | Find template by content. (optional)

    try:
        # Find templates by criteria
        api_response = api_instance.search_templates(page=page, limit=limit, ids=ids, name=name, content=content)
        print("The response of TextMagicApi->search_templates:\n")
        pprint(api_response)
    except Exception as e:
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returned when successful. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message**
> SendMessageResponse send_message(send_message_input_object)

Send message

This is the main entrypoint to send messages. See the examples above for the reference.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.send_message_request import SendMessageRequest
from TextMagic.models.send_message_response import SendMessageResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    send_message_input_object = TextMagic.SendMessageRequest() # SendMessageRequest | 

    try:
        # Send message
        api_response = api_instance.send_message(send_message_input_object)
        print("The response of TextMagicApi->send_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->send_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_message_input_object** | [**SendMessageRequest**](SendMessageRequest.md)|  | 

### Return type

[**SendMessageResponse**](SendMessageResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when successful. |  -  |
**202** | Returned when a bulk session has been created. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_chat_status**
> ResourceLinkResponse set_chat_status(set_chat_status_input_object)

Change chat status

Set the status of the chat given by ID.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.models.set_chat_status_request import SetChatStatusRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    set_chat_status_input_object = TextMagic.SetChatStatusRequest() # SetChatStatusRequest | 

    try:
        # Change chat status
        api_response = api_instance.set_chat_status(set_chat_status_input_object)
        print("The response of TextMagicApi->set_chat_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->set_chat_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_chat_status_input_object** | [**SetChatStatusRequest**](SetChatStatusRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unblock_contact**
> unblock_contact(unblock_contact_input_object)

Unblock a contact by phone number

Unblock a contact by phone number

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.block_contact_request import BlockContactRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    unblock_contact_input_object = TextMagic.BlockContactRequest() # BlockContactRequest | 

    try:
        # Unblock a contact by phone number
        api_instance.unblock_contact(unblock_contact_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->unblock_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unblock_contact_input_object** | [**BlockContactRequest**](BlockContactRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unblock_contacts_bulk**
> unblock_contacts_bulk(unblock_contacts_bulk_input_object)

Unblock contacts (bulk)

Unblock several contacts by blocked contact IDs or unblock all contacts.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.unblock_contacts_bulk_request import UnblockContactsBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    unblock_contacts_bulk_input_object = TextMagic.UnblockContactsBulkRequest() # UnblockContactsBulkRequest | 

    try:
        # Unblock contacts (bulk)
        api_instance.unblock_contacts_bulk(unblock_contacts_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->unblock_contacts_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unblock_contacts_bulk_input_object** | [**UnblockContactsBulkRequest**](UnblockContactsBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmute_chats_bulk**
> unmute_chats_bulk(unmute_chats_bulk_input_object)

Unmute chats (bulk)

Unmute several chats by chat ids or unmute all chats.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.unmute_chats_bulk_request import UnmuteChatsBulkRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    unmute_chats_bulk_input_object = TextMagic.UnmuteChatsBulkRequest() # UnmuteChatsBulkRequest | 

    try:
        # Unmute chats (bulk)
        api_instance.unmute_chats_bulk(unmute_chats_bulk_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->unmute_chats_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unmute_chats_bulk_input_object** | [**UnmuteChatsBulkRequest**](UnmuteChatsBulkRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unsubscribe_contact**
> ResourceLinkResponse unsubscribe_contact(unsubscribe_contact_input_object)

Manually unsubscribe a contact

> Please note, if you unsubscribe a contact, this action cannot be reversed.


### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.models.unsubscribe_contact_request import UnsubscribeContactRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    unsubscribe_contact_input_object = TextMagic.UnsubscribeContactRequest() # UnsubscribeContactRequest | 

    try:
        # Manually unsubscribe a contact
        api_response = api_instance.unsubscribe_contact(unsubscribe_contact_input_object)
        print("The response of TextMagicApi->unsubscribe_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->unsubscribe_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unsubscribe_contact_input_object** | [**UnsubscribeContactRequest**](UnsubscribeContactRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when updated with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_balance_notification_settings**
> update_balance_notification_settings(update_balance_notification_settings_input_object)

Update balance notification settings

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.update_balance_notification_settings_request import UpdateBalanceNotificationSettingsRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    update_balance_notification_settings_input_object = TextMagic.UpdateBalanceNotificationSettingsRequest() # UpdateBalanceNotificationSettingsRequest | 

    try:
        # Update balance notification settings
        api_instance.update_balance_notification_settings(update_balance_notification_settings_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->update_balance_notification_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_balance_notification_settings_input_object** | [**UpdateBalanceNotificationSettingsRequest**](UpdateBalanceNotificationSettingsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_callback_settings**
> update_callback_settings(update_callback_settings_input_object)

Update callback URL settings

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.update_callback_settings_request import UpdateCallbackSettingsRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    update_callback_settings_input_object = TextMagic.UpdateCallbackSettingsRequest() # UpdateCallbackSettingsRequest | 

    try:
        # Update callback URL settings
        api_instance.update_callback_settings(update_callback_settings_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->update_callback_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_callback_settings_input_object** | [**UpdateCallbackSettingsRequest**](UpdateCallbackSettingsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_chat_desktop_notification_settings**
> update_chat_desktop_notification_settings(update_chat_desktop_notification_settings_input_object)

Update chat desktop notification settings

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.update_chat_desktop_notification_settings_request import UpdateChatDesktopNotificationSettingsRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    update_chat_desktop_notification_settings_input_object = TextMagic.UpdateChatDesktopNotificationSettingsRequest() # UpdateChatDesktopNotificationSettingsRequest | 

    try:
        # Update chat desktop notification settings
        api_instance.update_chat_desktop_notification_settings(update_chat_desktop_notification_settings_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->update_chat_desktop_notification_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_chat_desktop_notification_settings_input_object** | [**UpdateChatDesktopNotificationSettingsRequest**](UpdateChatDesktopNotificationSettingsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact**
> ResourceLinkResponse update_contact(id, update_contact_input_object)

Edit a contact

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.models.update_contact_request import UpdateContactRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    update_contact_input_object = TextMagic.UpdateContactRequest() # UpdateContactRequest | 

    try:
        # Edit a contact
        api_response = api_instance.update_contact(id, update_contact_input_object)
        print("The response of TextMagicApi->update_contact:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->update_contact: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_contact_input_object** | [**UpdateContactRequest**](UpdateContactRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The contact has been created with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_contact_note**
> ResourceLinkResponse update_contact_note(id, update_contact_note_input_object)

Update a contact note

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.models.update_contact_note_request import UpdateContactNoteRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    update_contact_note_input_object = TextMagic.UpdateContactNoteRequest() # UpdateContactNoteRequest | 

    try:
        # Update a contact note
        api_response = api_instance.update_contact_note(id, update_contact_note_input_object)
        print("The response of TextMagicApi->update_contact_note:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->update_contact_note: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_contact_note_input_object** | [**UpdateContactNoteRequest**](UpdateContactNoteRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Returned when trying to edit a contact note shared to a current user. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_current_user**
> UpdateCurrentUserResponse update_current_user(update_current_user_input_object)

Edit current account info

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.update_current_user_request import UpdateCurrentUserRequest
from TextMagic.models.update_current_user_response import UpdateCurrentUserResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    update_current_user_input_object = TextMagic.UpdateCurrentUserRequest() # UpdateCurrentUserRequest | 

    try:
        # Edit current account info
        api_response = api_instance.update_current_user(update_current_user_input_object)
        print("The response of TextMagicApi->update_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->update_current_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_current_user_input_object** | [**UpdateCurrentUserRequest**](UpdateCurrentUserRequest.md)|  | 

### Return type

[**UpdateCurrentUserResponse**](UpdateCurrentUserResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Updated with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field**
> ResourceLinkResponse update_custom_field(id, update_custom_field_input_object)

Edit a custom field

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.create_custom_field_request import CreateCustomFieldRequest
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    update_custom_field_input_object = TextMagic.CreateCustomFieldRequest() # CreateCustomFieldRequest | 

    try:
        # Edit a custom field
        api_response = api_instance.update_custom_field(id, update_custom_field_input_object)
        print("The response of TextMagicApi->update_custom_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->update_custom_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_custom_field_input_object** | [**CreateCustomFieldRequest**](CreateCustomFieldRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when updated with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_field_value**
> ResourceLinkResponse update_custom_field_value(id, update_custom_field_value_input_object)

Edit the custom field value of a specified contact

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.models.update_custom_field_value_request import UpdateCustomFieldValueRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 554 # int | 
    update_custom_field_value_input_object = TextMagic.UpdateCustomFieldValueRequest() # UpdateCustomFieldValueRequest | 

    try:
        # Edit the custom field value of a specified contact
        api_response = api_instance.update_custom_field_value(id, update_custom_field_value_input_object)
        print("The response of TextMagicApi->update_custom_field_value:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->update_custom_field_value: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_custom_field_value_input_object** | [**UpdateCustomFieldValueRequest**](UpdateCustomFieldValueRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when updated with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_inbound_messages_notification_settings**
> update_inbound_messages_notification_settings(update_inbound_messages_notification_settings_input_object)

Update inbound messages notification settings

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.update_inbound_messages_notification_settings_request import UpdateInboundMessagesNotificationSettingsRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    update_inbound_messages_notification_settings_input_object = TextMagic.UpdateInboundMessagesNotificationSettingsRequest() # UpdateInboundMessagesNotificationSettingsRequest | 

    try:
        # Update inbound messages notification settings
        api_instance.update_inbound_messages_notification_settings(update_inbound_messages_notification_settings_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->update_inbound_messages_notification_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_inbound_messages_notification_settings_input_object** | [**UpdateInboundMessagesNotificationSettingsRequest**](UpdateInboundMessagesNotificationSettingsRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Request executed with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_list**
> ResourceLinkResponse update_list(id, update_list_object=update_list_object)

Edit a list

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.models.update_list_request import UpdateListRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    update_list_object = TextMagic.UpdateListRequest() # UpdateListRequest |  (optional)

    try:
        # Edit a list
        api_response = api_instance.update_list(id, update_list_object=update_list_object)
        print("The response of TextMagicApi->update_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->update_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_list_object** | [**UpdateListRequest**](UpdateListRequest.md)|  | [optional] 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when successful. |  -  |
**400** | Returned when the form has errors. |  -  |
**403** | Returned when trying to edit a list shared to a current user. |  -  |
**404** | Returned when no list found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sender_setting**
> update_sender_setting(update_sender_setting_input_object)

Change sender settings

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.update_sender_setting_request import UpdateSenderSettingRequest
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    update_sender_setting_input_object = TextMagic.UpdateSenderSettingRequest() # UpdateSenderSettingRequest | 

    try:
        # Change sender settings
        api_instance.update_sender_setting(update_sender_setting_input_object)
    except Exception as e:
        print("Exception when calling TextMagicApi->update_sender_setting: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_sender_setting_input_object** | [**UpdateSenderSettingRequest**](UpdateSenderSettingRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Sender settings have been updated with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> ResourceLinkResponse update_template(id, update_template_input_object)

Update a template

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.create_template_request import CreateTemplateRequest
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    update_template_input_object = TextMagic.CreateTemplateRequest() # CreateTemplateRequest | 

    try:
        # Update a template
        api_response = api_instance.update_template(id, update_template_input_object)
        print("The response of TextMagicApi->update_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->update_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **update_template_input_object** | [**CreateTemplateRequest**](CreateTemplateRequest.md)|  | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when successful. |  -  |
**400** | Returned when the form has errors. |  -  |
**401** | Unauthorized request. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_avatar**
> upload_avatar(image)

Upload an avatar

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    image = None # bytearray | User avatar. Should be a PNG or JPG file not more than 10 MB.

    try:
        # Upload an avatar
        api_instance.upload_avatar(image)
    except Exception as e:
        print("Exception when calling TextMagicApi->upload_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **bytearray**| User avatar. Should be a PNG or JPG file not more than 10 MB. | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_contact_avatar**
> ResourceLinkResponse upload_contact_avatar(id, image)

Upload an avatar

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    image = None # bytearray | Contact avatar. Should be a PNG or JPG file not more than 10 MB.

    try:
        # Upload an avatar
        api_response = api_instance.upload_contact_avatar(id, image)
        print("The response of TextMagicApi->upload_contact_avatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->upload_contact_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **image** | **bytearray**| Contact avatar. Should be a PNG or JPG file not more than 10 MB. | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Returned when successful. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Returned when trying to edit a contact shared to a current user. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_list_avatar**
> ResourceLinkResponse upload_list_avatar(id, image)

Add an avatar for a list

Add an avatar for a list

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.resource_link_response import ResourceLinkResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    id = 1 # int | 
    image = None # bytearray | List avatar. Should be a PNG or JPG file not more than 10 MB.

    try:
        # Add an avatar for a list
        api_response = api_instance.upload_list_avatar(id, image)
        print("The response of TextMagicApi->upload_list_avatar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->upload_list_avatar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **image** | **bytearray**| List avatar. Should be a PNG or JPG file not more than 10 MB. | 

### Return type

[**ResourceLinkResponse**](ResourceLinkResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Avatar uploaded with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |
**403** | Returned when trying to edit a list shared to the current user. |  -  |
**404** | Request data not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_message_attachment**
> UploadMessageAttachmentResponse upload_message_attachment(file)

Upload message attachment

Upload a new file to insert it as a link.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.upload_message_attachment_response import UploadMessageAttachmentResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    file = None # bytearray | Attachment. Supports .jpg, .gif, .png, .pdf, .txt, .csv, .doc, .docx, .xls, .xlsx, .ppt, .pptx & .vcf file formats.

    try:
        # Upload message attachment
        api_response = api_instance.upload_message_attachment(file)
        print("The response of TextMagicApi->upload_message_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->upload_message_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| Attachment. Supports .jpg, .gif, .png, .pdf, .txt, .csv, .doc, .docx, .xls, .xlsx, .ppt, .pptx &amp; .vcf file formats. | 

### Return type

[**UploadMessageAttachmentResponse**](UploadMessageAttachmentResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File uploaded with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_message_mms_attachment**
> UploadMessageAttachmentResponse upload_message_mms_attachment(file)

Upload message mms attachment

Upload a new file to mms.

### Example

* Basic Authentication (BasicAuth):

```python
import TextMagic
from TextMagic.models.upload_message_attachment_response import UploadMessageAttachmentResponse
from TextMagic.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.textmagic.com
# See configuration.py for a list of all supported configuration parameters.
configuration = TextMagic.Configuration(
    host = "https://rest.textmagic.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = TextMagic.TextMagicApi(api_client)
    file = None # bytearray | Attachment. Supports .jpg, .gif, .png, .pdf, .txt, .csv, .doc, .docx, .xls, .xlsx, .ppt, .pptx & .vcf file formats.

    try:
        # Upload message mms attachment
        api_response = api_instance.upload_message_mms_attachment(file)
        print("The response of TextMagicApi->upload_message_mms_attachment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TextMagicApi->upload_message_mms_attachment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| Attachment. Supports .jpg, .gif, .png, .pdf, .txt, .csv, .doc, .docx, .xls, .xlsx, .ppt, .pptx &amp; .vcf file formats. | 

### Return type

[**UploadMessageAttachmentResponse**](UploadMessageAttachmentResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File uploaded with success. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

