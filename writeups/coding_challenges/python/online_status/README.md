# Challenge
### Online status

The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

In this case, the number of people online is 2.

Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

Your function should return the number of people who are online.

Solution:
```py
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online"
}

def online_count(database):
    online = 0
    for x in database.values():
        if "online" in x:
            online += 1
    return online

print(online_count(statuses))

```

better way:
```py
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online"
}

def online_count(database):
    online = 0
    for person, status in database.items():
        if status == "online":
            online += 1
    return online

print(online_count(statuses))
```