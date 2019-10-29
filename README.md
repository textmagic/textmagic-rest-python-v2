[comment]: <> (HEAD)
# TextMagic Python SDK
This library provides you with an easy way of sending SMS and receiving replies by integrating the TextMagic SMS Gateway into your Python application.

## What Is TextMagic?
TextMagic’s application programming interface (API) provides the communication link between your application and TextMagic’s SMS Gateway, allowing you to send and receive text messages and to check the delivery status of text messages you’ve already sent.


[comment]: <> (/HEAD)
## Requirements
Python 2.7 and 3.4+

## Installation

```shell
pip install git+https://github.com/textmagic/textmagic-rest-python-v2.git@v2.0.808
```

## Usage Example

```python
import TextMagic
from TextMagic.rest import ApiException

# Configure HTTP basic authorization: BasicAuth
configuration = TextMagic.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = TextMagic.TextMagicApi(TextMagic.ApiClient(configuration))

# Simple ping request example
try:
    response = api_instance.ping()
    print(response.ping)
except ApiException as e:
    print("Exception when calling TextMagicApi->ping: %s\n" % e)

# Send a new message request example
send_message_input_object = TextMagic.SendMessageInputObject()
send_message_input_object.text = "I love TextMagic!"
send_message_input_object.phones = "+79998887766"

try:
    response = api_instance.send_message(send_message_input_object)
    print(response.id)
except ApiException as e:
    print("Exception when calling TextMagicApi->send_message: %s\n" % e)

# Get all outgoing messages request example
try:
    response = api_instance.get_all_outbound_messages(page=1, limit=200)
    print(response.resources[0].text)
except ApiException as e:
    print("Exception when calling TextMagicApi->get_all_outbound_messages: %s\n" % e)

# Upload a new list (contacts group) avatar request example. 3223 here is a test list id
try:
    response = api_instance.upload_list_avatar('test.png', 3223)
    print(response.id)
except ApiException as e:
    print("Exception when calling TextMagicApi->upload_list_avatar: %s\n" % e)

```

[comment]: <> (FOOTER)
## License
The library is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

[comment]: <> (/FOOTER)