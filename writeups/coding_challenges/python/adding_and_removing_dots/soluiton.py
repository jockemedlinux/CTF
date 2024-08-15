def add_dots(string_):
	for letter in string_.split():
		dots = ".".join(letter)
	return dots

def remove_dots(string_):
	removed = string_.replace(".", "")
	return removed

print(add_dots("test"))
print(remove_dots("t.e.s.t"))

print(remove_dots(add_dots("tja...bba"))) #	returns no dots
print(remove_dots(add_dots("tjabba"))) 	  #	returns no dots