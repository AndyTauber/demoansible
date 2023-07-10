#!/usr/bin/python

import requests, sys
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ip = sys.argv[1]
user = ('svc_k8s')
password = sys.argv[2]
url = ('https://infoblox.acme.com/wapi/v2.5/')
obj= ('lease?address='+ip)
func=('&_return_fields=')
state = ('&_return_fields=binding_state')
getresponse = requests.get(url+obj+func,auth=HTTPBasicAuth(user,password), verify = False)
getstate = requests.get(url+obj+state,auth=HTTPBasicAuth(user,password), verify = False)
print getstate.text
ref = getresponse.text[25:-9]
requests.delete(url+ref,auth=HTTPBasicAuth(user,password), verify = False)
print "The lease has been removed"
getstate = requests.get(url+obj+state,auth=HTTPBasicAuth(user,password), verify = False)
print getstate.text
