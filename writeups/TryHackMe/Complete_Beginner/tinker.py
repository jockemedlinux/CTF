#!/usr/bin/python3

i = 0
with open("numbers.txt", "a") as file:
	while i < 2000:
		file.write(str(i))
		file.write("\n")
		i += 1
	file.close()
exit()