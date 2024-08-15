def flatten(string_):
	result = []
	for x in string_:
		for y in x:
			result.append(y)
	return result


print(flatten([[1, 2], [3, 4], [5, 8]]))
