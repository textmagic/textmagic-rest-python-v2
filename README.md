[comment]: <> (HEAD)
# TextMagic Python SDK

[![PyPI version](https://badge.fury.io/py/TextMagic.svg)](https://badge.fury.io/py/TextMagic)
[![Python Versions](https://img.shields.io/pypi/pyversions/TextMagic.svg)](https://pypi.org/project/TextMagic/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This library provides you with an easy way of sending SMS and receiving replies by integrating the TextMagic SMS Gateway into your Python application.

## What Is TextMagic?
TextMagic’s application programming interface (API) provides the communication link between your application and TextMagic’s SMS Gateway, allowing you to send and receive text messages and to check the delivery status of text messages you’ve already sent.


[comment]: <> (/HEAD)
## Requirements

- **Python** >= 3.9
- **urllib3** >= 2.1.0, < 3.0.0,
- **python-dateutil** >= 2.8.2,
- **pydantic** >= 2,
- **typing-extensions** >= 4.7.1,

## Installation

### Install from PyPI (Recommended)

```bash
pip install TextMagic
```

### Install from GitHub

```bash
pip install git+https://github.com/textmagic/textmagic-rest-python-v2.git@v3.0.50053
```

### Install from source

```bash
git clone https://github.com/textmagic/textmagic-rest-python-v2.git
cd textmagic-rest-python-v2
python setup.py install
```

## Quick Start

### Basic Usage

```python
import TextMagic
from TextMagic.rest import ApiException

# Configure API credentials
# Get your credentials from https://app.textmagic.com/settings/api
configuration = TextMagic.Configuration(
    username='YOUR_USERNAME',
    password='YOUR_API_KEY'
)

# Create API client
with TextMagic.ApiClient(configuration) as api_client:
    # Create API instance
    api = TextMagic.TextMagicApi(api_client)

    # Test connection
    try:
        response = api.ping()
        print(f"✅ Connected! Server time: {response.ping}")
    except ApiException as e:
        print(f"❌ Error: {e}")
```

### Sending Messages

```python
import TextMagic
from TextMagic.rest import ApiException

configuration = TextMagic.Configuration(
    username='YOUR_USERNAME',
    password='YOUR_API_KEY'
)

with TextMagic.ApiClient(configuration) as api_client:
    api = TextMagic.TextMagicApi(api_client)

    # Send SMS to a single number
    try:
        send_message = TextMagic.SendMessageInputObject(
            text="Hello from TextMagic Python SDK!",
            phones="+1234567890"
        )
        response = api.send_message(send_message)
        print(f"✅ Message sent! ID: {response.id}")
        print(f"   Session ID: {response.session_id}")
    except ApiException as e:
        print(f"❌ Error sending message: {e}")

    # Send SMS to multiple numbers
    try:
        send_message = TextMagic.SendMessageInputObject(
            text="Bulk message",
            phones="+1234567890,+0987654321"  # Comma-separated
        )
        response = api.send_message(send_message)
        print(f"✅ Bulk message sent! Session ID: {response.session_id}")
    except ApiException as e:
        print(f"❌ Error: {e}")
```

### Getting Outgoing Messages

```python
import TextMagic
from TextMagic.rest import ApiException

configuration = TextMagic.Configuration(
    username='YOUR_USERNAME',
    password='YOUR_API_KEY'
)

with TextMagic.ApiClient(configuration) as api_client:
    api = TextMagic.TextMagicApi(api_client)

    try:
        # Get recent outgoing messages
        response = api.get_all_outbound_messages(page=1, limit=10)

        print(f"Total messages: {response.page.total}")
        for message in response.resources:
            print(f"- [{message.id}] {message.text[:50]}... → {message.receiver}")
            print(f"  Status: {message.status}, Sent: {message.created_at}")
    except ApiException as e:
        print(f"❌ Error: {e}")
```

### Uploading Files

```python
import TextMagic
from TextMagic.rest import ApiException

configuration = TextMagic.Configuration(
    username='YOUR_USERNAME',
    password='YOUR_API_KEY'
)

with TextMagic.ApiClient(configuration) as api_client:
    api = TextMagic.TextMagicApi(api_client)

    # Upload list avatar
    try:
        response = api.upload_list_avatar(
            file='path/to/avatar.png',
            id=12345  # List ID
        )
        print(f"✅ Avatar uploaded! Resource ID: {response.id}")
    except ApiException as e:
        print(f"❌ Error: {e}")
```

### Error Handling

```python
import TextMagic
from TextMagic.rest import ApiException

configuration = TextMagic.Configuration(
    username='YOUR_USERNAME',
    password='YOUR_API_KEY'
)

with TextMagic.ApiClient(configuration) as api_client:
    api = TextMagic.TextMagicApi(api_client)

    try:
        response = api.send_message(
            TextMagic.SendMessageInputObject(
                text="Test message",
                phones="+1234567890"
            )
        )
        print(f"✅ Success: {response.id}")
    except ApiException as e:
        print(f"❌ API Exception:")
        print(f"   Status: {e.status}")
        print(f"   Reason: {e.reason}")
        print(f"   Body: {e.body}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
```

## API Documentation

For detailed API documentation, including all available methods and parameters, please visit:

- **REST API Documentation:** https://docs.textmagic.com/

### Available Methods

The SDK provides access to all TextMagic API endpoints, including:

- **Messages:** Send, receive, and manage SMS messages
- **Contacts:** Manage your contact lists
- **Templates:** Create and use message templates
- **Chats:** Manage conversations
- **Bulk Messaging:** Send messages to multiple recipients
- **Sender IDs:** Manage sender names
- **Account:** Check balance and account information
- **Statistics:** Get messaging statistics and reports

## Migration Guide

### Migrating from v2.x to v3.x

#### Breaking Changes

1. **Python Version Requirements:**
   - v2.x: Python 2.7+ and 3.4+
   - v3.x: Python 3.9+ only

2. **Configuration (More Pythonic):**
   ```python
   # v2.x
   configuration = TextMagic.Configuration()
   configuration.username = 'username'
   configuration.password = 'api_key'

   # v3.x (constructor with parameters)
   configuration = TextMagic.Configuration(
       username='username',
       password='api_key'
   )
   ```

3. **Context Manager Support (New in v3.x):**
   ```python
   # v2.x (manual resource management)
   api_client = TextMagic.ApiClient(configuration)
   api = TextMagic.TextMagicApi(api_client)
   response = api.ping()

   # v3.x (context managers - recommended)
   with TextMagic.ApiClient(configuration) as api_client:
       api = TextMagic.TextMagicApi(api_client)
       response = api.ping()
   ```

#### What Stays the Same

- ✅ Package name: `TextMagic` (unchanged)
- ✅ Import statements: `import TextMagic` (unchanged)
- ✅ API method names and signatures
- ✅ Response objects structure
- ✅ Authentication mechanism
- ✅ Error handling with `ApiException`

## Development

### Running Tests

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/

# Run tests with coverage
pytest --cov=TextMagic tests/
```

### Building from Source

```bash
git clone https://github.com/textmagic/textmagic-rest-python-v2.git
cd textmagic-rest-python-v2
python setup.py sdist bdist_wheel
```

## Need Help?

- **Documentation:** https://docs.textmagic.com/
- **Support:** https://www.textmagic.com/support/
- **GitHub Issues:** https://github.com/textmagic/textmagic-rest-python-v2/issues

[comment]: <> (FOOTER)
## License
The library is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).

[comment]: <> (/FOOTER)
