def mid(string_):
	lenght = len(string_)
	if lenght % 2 == 0:
		return ""
	else:
		middle = lenght // 2
		return string_[middle]

print(mid("abc"))