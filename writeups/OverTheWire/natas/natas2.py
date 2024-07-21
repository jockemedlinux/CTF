#!/usr/bin/env python3

import requests, re

match = "natas"
username = "natas2"
password = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'

url = "http://%s.natas.labs.overthewire.org/files/users.txt" % username

response = requests.get(url, auth= (username, password))
content = response.text
print(content)
#print(re.findall(f'<!--The password for {match}. is (.*) -->', content)[0])