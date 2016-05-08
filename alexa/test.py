#!/usr/bin/env python
import requests, json
from urlparse import urlparse

#get mac address
from uuid import getnode as get_mac
mac = get_mac()
""""
files = {'0001.flac': open('0001.flac', 'rb')}
r = requests.get(url, auth=(u, p))
print r
payload = {'Content-Type': 'audio/flac', 'Transfer-Encoding': 'chunked'}
#payload = {'header': json.dumps({"Content-Type":'audio/flac','Transfer-Encoding': 'chunked'})}
r = requests.post(url,auth=(u,p),headers=payload,files=files)
print r
print r.text
"""



url1 = "https://www.amazon.com/ap/oa"
payload = {'client_id': 'amzn1.application-oa2-client.39763708be434ca583699141d6d6298c','scope': 'alexa%3Aall','scope_data': {"alexa:all": {"productID": "heyraine","productInstanceAttributes": {"deviceSerialNumber": mac}}},'response_type': 'token','redirect_uri': 'http://google.com'}
r = requests.post(url1, params=json.dumps(payload))
#print(r.url)
token = r.url.rsplit('/', 1)[-1]
print token

url2 = 'https://api.amazon.com/auth/o2/token'
headers = {'Content-Type':'multipart/form-data','Authorization':'Bearer ' + token}

req = requests.post(url2,headers=headers)

print req.content
