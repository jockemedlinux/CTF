# Challenge
### Middle letter

Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
For example, mid("abc") should return "b" and mid("aaaa") should return "".


```python
def mid(string_):
	lenght = len(string_)
	if lenght % 2 == 0:
		return ""
	else:
		middle = lenght // 2
		return string_[middle]

print(mid("abc"))
```