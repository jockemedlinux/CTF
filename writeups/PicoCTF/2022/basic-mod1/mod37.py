#!/usr/bin/env python3

import string
#print(string.ascii_uppercase)
#print(string.digits)

flag = []

with open("message.txt", "r") as file:
	contents = file.read()
	strings = [int(val) for val in contents.split()]
	for number in strings:
		modulus = number % 37

		if modulus in range(26):
			print(string.ascii_uppercase[modulus], end="")
			flag.append(string.ascii_uppercase[modulus])
		elif modulus in range(26, 36):
			print(string.digits[modulus - 26], end="")
			flag.append(string.digits[modulus - 26])
		else:
			print("_", end="")
			flag.append("_")

print("\n\n\n")
print("picoCTF{%s}" % "".join(flag))

