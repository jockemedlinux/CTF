# Cyborg

### Challenge 0 --> 1
```
cyborg0@cyborg.underthewire.tech

Solution(s):
Find in slack-channel
```

### Challenge 1 --> 2
```
cyborg1@cyborg.underthewire.tech:cyborg1

Solution(s):
(Get-ADUser -Property * -F "GivenName -like 'Chris*'").State
```

### Challenge 2 --> 3
```
cyborg2@cyborg.underthewire.tech:kansas

Solution(s):
Resolve-DnsName CYBORG718W100N -Type A
```

### Challenge 3 --> 4
```
cyborg3@cyborg.underthewire.tech:172.31.45.167_ipv4

Solution(s):
(Get-ADGroupMember -Identity cyborg).SamAccountName.Count
```

### Challenge 4 --> 5
```
cyborg4@cyborg.underthewire.tech:88_objects

Solution(s):
((Get-Module -ListAvailable) | ? -Property Version -Like "8.9.8.9").Name
```

### Challenge 5 --> 6
```
cyborg5@cyborg.underthewire.tech:bacon_eggs

Solution(s):
Get-ADUser -Filter * -Property Surname, LogonHours | ? LogonHours
```

### Challenge 6 --> 7
```
cyborg6@cyborg.underthewire.tech:rowray_timer

Solution(s):
[Text.Encoding]::UTF8.GetString([Convert]::FromBase64String('YwB5AGIAZQByAGcAZQBkAGQAbwBuAA=='))
or
[System.Text.Encoding]::Unicode.GetString([Convert]::FromBase64String((gc '.\cypher.txt')))
```

### Challenge 7 --> 8
```
cyborg7@cyborg.underthewire.tech:cybergeddon

Solution(s):
Get-WmiObject -Class Win32_StartupCommand | Select-Object Name, Command, Location
```

### Challenge 8 --> 9
```
cyborg8@cyborg.underthewire.tech:skynet

Solution(s):

```

### Challenge 9 --> 10
```
cyborg9@cyborg.underthewire.tech:<password>

Solution(s):

```

### Challenge 10 --> 11
```
cyborg10@cyborg.underthewire.tech:<password>

Solution(s):

```

### Challenge 11 --> 12
```
cyborg11@cyborg.underthewire.tech:<password>

Solution(s):

```

### Challenge 12 --> 13
```
cyborg12@cyborg.underthewire.tech:<password>

Solution(s):

```

### Challenge 13 --> 14
```
cyborg13@cyborg.underthewire.tech:<password>

Solution(s):

```

### Challenge 14 --> 15
```
cyborg14@cyborg.underthewire.tech:<password>

Solution(s):

```

### Challenge 15 --> 16
```
cyborg15@cyborg.underthewire.tech:<password>

Solution(s):

```