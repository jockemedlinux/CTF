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