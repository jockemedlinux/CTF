def count(string_):
	syllables = 1
	for x in string_:
		if "-" in x:
			syllables += 1
	return syllables
		
print(count("cat"))