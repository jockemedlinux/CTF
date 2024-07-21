#!/usr/bin/env python3

import string
#print(string.ascii_uppercase)
#print(string.digits)

flag = []

with open("message.txt", "r") as file:
	contents = file.read()
	strings = [int(val) for val in contents.split()]

	for number in strings:
		modulus = pow(number, -1, 41)
		print(modulus)

		if modulus in range(1, 27):
			flag.append(string.ascii_uppercase[modulus - 1])

		elif modulus in range(27, 37):
			flag.append(string.digits[modulus - 27])
		else:
			flag.append("_")

print("\n\n\n")
print("picoCTF{%s}" % "".join(flag))

