# Challenge
### Double letters

The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.
Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.

solution:
```py
def double_letters(string_):
	for i in range (len(string_)-1):
		if string_[i] == string_[i+1]:
			return True
	return False

print(double_letters('Tjena mannen'))
```

example solution:
```py
# naive solution
def double_letters(string):
    for i in range(len(string) - 1):
        letter1 = string[i]
        letter2 = string[i+1]
        if letter1 == letter2:
            return True
    return False

```