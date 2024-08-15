# Challenge
### Adding and removing dots

Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".
Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".
If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.
(You may assume that the input to add_dots does not itself contain any dots.)


solution:
```py
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
```

example solution:
```py
def add_dots(string_):
	return ".".join(string_)
	
def remove_dots(string_):
	return string_.replace(".", "")	
```