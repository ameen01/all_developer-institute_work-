import time as t
import requests
import json
import os
url = 'https://jsonplaceholder.typicode.com/posts'
resp = requests.get(url)
json_data = resp.text
decode = json.loads(json_data)
fil = open('ameen.text', 'a')
json.dump(decode, fil)
fil.close()

fails = os.scandir()
for f in fails:
    fils= f.path
