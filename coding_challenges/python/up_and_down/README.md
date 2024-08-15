# Challenge
### Up and down

Define a function named up_down that takes a single number as its parameter. Your function return a tuple containing two numbers; the first should be one lower than the parameter, and the second should be one higher.
For example, calling up_down(5) should return (4, 6).


Solution:
```py
def up_down(option):
	higher	= option + 1
	lower	= option - 1
	tuplelist = (lower, higher)
	return tuplelist

print(up_down(5))
```


Example solution:
```py
def up_down(x):
    return (x-1, x+1)
```