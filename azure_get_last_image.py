#!/usr/bin/env python

from ansible.module_utils.basic import AnsibleModule
import time,datetime,json, os
from distutils.version import StrictVersion
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient


def main():

  result = dict(
    changed=False,
    message=[]
  )

  module = AnsibleModule(
    argument_spec=dict(
       resource_group=dict(required=True),
       name=dict(required=True)
       )
    )

  if module.check_mode:
    return result

  resource_group = module.params.get('resource_group')
  name = module.params.get('name')

  def get_credentials():
    subscription_id = os.environ['AZURE_SUBSCRIPTION_ID']
    credentials = ServicePrincipalCredentials(
        client_id=os.environ['AZURE_CLIENT_ID'],
        secret=os.environ['AZURE_SECRET'],
        tenant=os.environ['AZURE_TENANT']
    )
    return credentials, subscription_id

  def sortVersions(versions_list):
    versions = [s.split('-')[-1] for s in versions_list]
    softname = ''.join(versions_list[0].split('-')[:-1])
    versions.sort(key=StrictVersion)
    sorted_list = ['-'.join([softname, version]) for version in versions]
    return sorted_list


  try:
    credentials, subscription_id = get_credentials()
    compute_client = ComputeManagementClient(credentials, subscription_id)

    images=[]
    vm_images = compute_client.images.list_by_resource_group(resource_group)

    for vm_image in vm_images:
      if name in vm_image.name:
        images.append(vm_image.name)

    sorted = sortVersions(images)
    last = sorted[-1]

    result['message'].append(last)
    module.exit_json(**result)
    return True
  except Exception as e:
    module.fail_json(msg=str(e))
    return False

if __name__ == '__main__':
  main()
