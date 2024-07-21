#!/usr/bin/env python3

import requests, re

match = "natas"
username = "natas6"
password = 'fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR'

url = "http://%s.natas.labs.overthewire.org/" % username
secret = "FOEIUWGHFEEUHOFUOIU"

#response = requests.post(url, auth= (username, password), data=secret)
response = requests.post(url, auth= (username, password), data = { "secret" : "FOEIUWGHFEEUHOFUOIU", "submit" : "submit" })
print(response.text)

# cookies = { "loggedin" : "1" }
# response = requests.post(url, auth= (username, password), cookies = cookies )
# pagecookies = response.cookies.get_dict()
# print(f"The cookies: {pagecookies}\n") 
# print("The page: \n")
# print(response.text)