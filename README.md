# itop_client

Python interface to interacte with iTop REST API

## Features

- Check for credentials
- Get objects
- Update objects
- Create objects

## Usage

Here is an example usage of the check credentials feature :
```python
from itop_client import ITopClient

client = ITopClient(BASE_URL, USER, PASS, VERIFY_TLS)

is_valid = client.check_credentials()
```

Look for tests to see other examples.

## Fields to create ticket

```json
{
        # Basic fields
        "title": "test",
        "description": "test",
        # Ticket services fields
        "servicedomain_id": 29,
        "servicefamily_id": 173,
        "service_id": 621,
        "servicesubcategory_id": 2109,
        "beneficiary_id": 24925
    }
```