#!/usr/bin/env python3

import base64

with open("/base/wordlists/password/john-password.txt") as passwords:
	for line in passwords:
		username = "fox:"
		string = base64.b64encode((username+line).encode('UTF-8'))
		output = print(string.decode().strip())