def double_letters(string_):
	for i in range (len(string_)-1):
		if string_[i] == string_[i+1]:
			return True
	return False

print(double_letters('Tjena mannen'))