**This documentation is automatically generated.**

**Output schemas only represent `data` and not the full output; see output examples and the JSend specification.**

# /api/sawithealth/?

    Content-Type: application/json

## POST


**Input Schema**
```json
{
    "properties": {
        "blok": {
            "items": {
                "type": "string"
            },
            "type": "array"
        }
    },
    "type": "object"
}
```


**Input Example**
```json
{
    "blok": [
        "A10",
        "F03",
        "C25"
    ]
}
```


**Output Schema**
```json
{
    "properties": {
        "dead": {
            "type": "number"
        },
        "encumbrance": {
            "type": "number"
        },
        "new": {
            "type": "number"
        },
        "normal": {
            "type": "number"
        },
        "special": {
            "type": "number"
        },
        "supply": {
            "type": "number"
        },
        "yellow": {
            "type": "number"
        }
    },
    "type": "object"
}
```


**Output Example**
```json
{
    "dead": 0,
    "encumbrance": 1,
    "new": 3,
    "normal": 435,
    "special": 0,
    "supply": 13,
    "yellow": 57
}
```


**Notes**

POST the required parameters
* `blok`: blok


