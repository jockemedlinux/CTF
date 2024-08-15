# Challenge
### Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.
For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

solution:
```python
def capital_indexes(string_):
    indexlist = []
    for index, value in enumerate(string_):
        if value.isupper(): indexlist.append(index)
    print(indexlist)
    return indexlist
            
capital_indexes("HeLlO")
```