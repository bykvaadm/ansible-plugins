# centrifugo-ansible

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
