# centrifugo

A module for sending messages to centrifugo.

requires cent module: 
```
pip install cent
```
Example:
```
- name: centrifugo notification
  centrifugo:
    secret: "{{ cent_secret }}"
    channel: "public"
    url: "https://example.com"
    data:
      event: "This is an websocket event, sent from ansible"
      timestamp: "{{ lookup('pipe','date +%s') }}"
```
# azure_get_last_image

A module for getting private images from resource group, filter by name, sort and get latest.

requires azure pypi module - read about azure ansible module.

Example:
```
- azure_list_image:
    name: "{{ filter_string }}"
    resource_group: "{{ resource_group }}"
```

Result:
```
ok: [localhost] => {
    "changed": false, 
    "failed_when_result": false, 
    "invocation": {
        "module_args": {
            "name": "example", 
            "resource_group": "example"
        }
    }, 
    "message": [
        "example-2.8.5"
    ]
}
```
