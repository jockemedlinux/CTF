#!/usr/bin/env python3

import requests, re

match = "natas"
username = "natas1"
password = 'g9D9cREhslqBKtcA2uocGHPfMZVzeFK6'

url = "http://%s.natas.labs.overthewire.org/" % username

response = requests.get(url, auth= (username, password))
content = response.text

print(re.findall(f'<!--The password for {match}. is (.*) -->', content)[0])