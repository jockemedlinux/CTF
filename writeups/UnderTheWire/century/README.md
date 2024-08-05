# Century

### Challenge #1
```
century1@century.underthewire.tech:century1

Solution(s):
$PSVersionTable
```

### Challenge #2
```
century2@century.underthewire.tech:10.0.14393.6343

Solution(s):
"invoke-webrequest"
```

### Challenge #3
```
century3@century.underthewire.tech:invoke-webrequest443

Solution(s):
Get-ChildItem . -Recurse | Measure-Object | %{$_.Count}
or
(gci).count
```

### Challenge #4
```
century4@century.underthewire.tech:123

Solution(s):
cd '.\Can You Open Me'
```

### Challenge #5
```
century5@century.underthewire.tech:34182

Solution(s):
Get-ADDomain | Select-Object -Property Name
Get-ADDomain | Select-Object -Property NetBIOSName
(Get-ADDomain).Name
```

### Challenge #6
```
century6@century.underthewire.tech:underthewire3347

Solution(s):
Get-ChildItem -Directory | Measure-Object | %{$_.Count}
(gci -Directory).Count
```

### Challenge #7
```
century7@century.underthewire.tech:197

Solution(s):
gci -r -i "Readme*" | type 
```

### Challenge #8
```
century8@century.underthewire.tech:7points

Solution(s):
(gc .\unique.txt | gu).Count
```


### Challenge #9
```
century9@century.underthewire.tech:696

Solution(s):
((gc .\Word_File.txt) -split "\s+")[160]
```

### Challenge #10
```
century10@century.underthewire.tech:pierid

Solution(s):
(((Get-WmiObject Win32_Service -Filter "Name='wuauserv'").Description) -Split '\s+')[9,7] ; (dir).Name
```

### Challenge #11
```
century11@century.underthewire.tech:windowsupdates110

Solution(s):
```

### Challenge #12
```
century12@century.underthewire.tech

Solution(s):
```

### Challenge #13
```
century13@century.underthewire.tech

Solution(s):
```

### Challenge #14
```
century14@century.underthewire.tech

Solution(s):
```

### Challenge #15
```
century15@century.underthewire.tech

Solution(s):
```

### Challenge #16
```
century16@century.underthewire.tech

Solution(s):
```