#!/usr/bin/env python3

with open("message.txt") as filp:
	contents = filp.read()

for i in range(0, len(contents), 3):
	chunk = contents[i : i +3]

	a, b, c = chunk
	print(c + a + b, end="")