# -*- coding: utf-8 -*-
import requests

url = 'http://developer.rutoken.ru/rpc/json-rpc/myservice'
response = requests.get(url, auth=('user', 'pass'))

data = response.json()
print(data)