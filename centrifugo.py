#!/usr/bin/env python

#from googleapiclient import discovery
#from oauth2client.service_account import ServiceAccountCredentials
from ansible.module_utils.basic import AnsibleModule
#from dateutil import parser
import time,datetime,json
from cent import Client

def main():

  result = dict(
    changed=False,
    message=[]
  )

  module = AnsibleModule(
    argument_spec=dict(
       url=dict(required=True),
       secret=dict(required=True),
       data=dict(required=True),
       channel=dict(required=True)
       )
    )

  if module.check_mode:
    return result

  url = module.params.get('url')
  secret = module.params.get('secret')
  data = module.params.get('data')
  data = json.loads(data.replace("'", '"'))
  channel = module.params.get('channel')

  client = Client(url, secret, timeout=1)

  try:
    response = client.publish(channel, data)
    result['message'].append(response)

    module.exit_json(**result)
    return True
  except Exception as e:
    module.fail_json(msg=str(e))
    return False

if __name__ == '__main__':
  main()
