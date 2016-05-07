#!/usr/bin/env python
import urllib2
import requests
import json
u='0166ce54-cf01-4de3-91e9-38163bd3d9d6'
p='ct4zakIyeOO8'
url='https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?timestamps=true&word_alternatives_threshold=0.9'

"""
curl -u <username>:<password> -X POST
--header "Content-Type: audio/flac"
--header "Transfer-Encoding: chunked"
--data-binary @<path>0001.flac
'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?continuous=true'
"""
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
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1


speech_to_text = SpeechToTextV1(
    username=u,
    password=p)

print(json.dumps(speech_to_text.models(), indent=2))

with open(join(dirname(__file__), '0001.flac'), 'rb') as audio_file:
    print(json.dumps(speech_to_text.recognize(
        audio_file, content_type='audio/flac'), indent=2))
"""
# simple wrapper function to encode the username & pass
def encodeUserData(user, password):
    return (user + ":" + password).encode("base64").rstrip()

f = open("0001.flac", "rb")
data = f.read()
print data
# create the request object and set some headers
req = urllib2.Request(url)
req.add_header('Content-Type', 'audio/flac')
req.add_header("Transfer-Encoding", "chunked")
req.add_header('Authorization', encodeUserData(u, p))
req.add_data(data)
# make the request and print the results
res = urllib2.urlopen(req)
print res.read()
f.close()
"""
