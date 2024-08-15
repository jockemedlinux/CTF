def only_ints(one, two):
 	if type(one) is int and type(two) is int:
 		return True
 	return False
print(only_ints(1, 2))