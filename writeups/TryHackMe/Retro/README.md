# BOX NAME: Retro
**LINK**: https://tryhackme.com/room/retro

<details open><summary><ins>SUMMARY</ins></summary>

```
1. 
2. 
3. 
4. 
5.

```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.10.144.213
[+] URL:	
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC 10.10.144.213 -p- -oN nmap-retro.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-12 11:08 CEST
Nmap scan report for 10.10.144.213
Host is up (0.052s latency).                                                                                        
Not shown: 65533 filtered tcp ports (no-response)                                                                   
PORT     STATE SERVICE       VERSION                                                                                
80/tcp   open  http          Microsoft IIS httpd 10.0                                                               
| http-methods:                                                                                                     
|_  Potentially risky methods: TRACE                                                                                
|_http-server-header: Microsoft-IIS/10.0                                                                            
|_http-title: IIS Windows Server                                                                                    
3389/tcp open  ms-wbt-server Microsoft Terminal Services                                                            
| ssl-cert: Subject: commonName=RetroWeb                                                                            
| Not valid before: 2023-05-11T08:25:28                                                                             
|_Not valid after:  2023-11-10T08:25:28                                                                             
|_ssl-date: 2023-05-12T09:10:58+00:00; +1s from scanner time.
| rdp-ntlm-info: 
|   Target_Name: RETROWEB
|   NetBIOS_Domain_Name: RETROWEB
|   NetBIOS_Computer_Name: RETROWEB
|   DNS_Domain_Name: RetroWeb
|   DNS_Computer_Name: RetroWeb
|   Product_Version: 10.0.14393
|_  System_Time: 2023-05-12T09:10:53+00:00
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 117.97 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```

```

nikto-scan
```

```

fuzzing
```
/retro [a wordpress site]

```
other
```
|    |\/| [__  |___ |___ |_/  by @r3dhax0r
|___ |  | ___| |___ |___ | \_ Version 1.1.3 K-RONA


 [+]  Deep Scan Results  [+] 

 ┏━Target: 10.10.144.213
 ┃
 ┠── CMS: WordPress
 ┃    │
 ┃    ├── Version: 5.2.1
 ┃    ╰── URL: https://wordpress.org
 ┃
 ┠──[WordPress Deepscan]
 ┃    │
 ┃    ├── Readme file found: http://10.10.144.213/retro//readme.html
 ┃    ├── License file: http://10.10.144.213/retro//license.txt
 ┃    │
 ┃    ├── Themes Enumerated: 1
 ┃    │    │
 ┃    │    ╰── Theme: 90s-retro
 ┃    │        │
 ┃    │        ├── Version: 5.2.1
 ┃    │        ╰── URL: http://10.10.144.213/retro//wp-content/themes/90s-retro
 ┃    │
 ┃    │
 ┃    ├── Usernames harvested: 1
 ┃    │    ╰── wade
 ┃    │
 ┃
 ┠── Result: /home/jockemedlinux/offsec/CONFIGS/Result/10.10.144.213_retro/cms.json
 ┃
 ┗━Scan Completed in 13.59 Seconds, using 45 Requests



 CMSeeK says ~ adieu
                      
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

RDP
```
Remote desktop running on 3389.

```

</details>

<details><summary><ins>Active Directory</ins></summary>

Active Directory
```

```
</details>

<details><summary><ins>SUMMARY REMOTE</ins></summary>

```
1. Found a special note on the wordpres site. Parzival. and a username.
2. The wp-admin login page redirects to a https:localhost interface. We could do some proxymagic but we can already login in the box.
3.
```
</details>

# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**SYSTEMINFO**:
```
Host Name:                 RETROWEB
OS Name:                   Microsoft Windows Server 2016 Standard
OS Version:                10.0.14393 N/A Build 14393
OS Manufacturer:           Microsoft Corporation
OS Configuration:          Standalone Server
OS Build Type:             Multiprocessor Free
Registered Owner:          Windows User
Registered Organization:
Product ID:                00377-60000-00000-AA325
Original Install Date:     12/8/2019, 10:50:43 PM
System Boot Time:          5/12/2023, 1:24:29 AM
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
Time Zone:                 (UTC-08:00) Pacific Time (US & Canada)
Total Physical Memory:     2,048 MB
Available Physical Memory: 901 MB
Virtual Memory: Max Size:  3,200 MB
Virtual Memory: Available: 1,934 MB
Virtual Memory: In Use:    1,266 MB
Page File Location(s):     C:\pagefile.sys
Domain:                    WORKGROUP
Logon Server:              \\RETROWEB
Hotfix(s):                 1 Hotfix(s) Installed.
                           [01]: KB3192137
Network Card(s):           1 NIC(s) Installed.
                           [01]: AWS PV Network Device
                                 Connection Name: Ethernet
                                 DHCP Enabled:    Yes
                                 DHCP Server:     10.10.0.1
                                 IP address(es)
                                 [01]: 10.10.144.213
                                 [02]: fe80::999:ab45:d1b7:ed3f
Hyper-V Requirements:      A hypervisor has been detected. Features required for Hyper-V will not be displayed.

C:\Users\Wade>whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                    State
============================= ============================== ========
SeChangeNotifyPrivilege       Bypass traverse checking       Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set Disabled
```

**FIREWALL / AV**:

```
C:\Users\Wade>sc query windefend

Public Profile Settings:
----------------------------------------------------------------------
State                                 ON
Firewall Policy                       BlockInbound,AllowOutbound
LocalFirewallRules                    N/A (GPO-store only)
LocalConSecRules                      N/A (GPO-store only)
InboundUserNotification               Disable
RemoteManagement                      Disable
UnicastResponseToMulticast            Enable

Logging:
LogAllowedConnections                 Disable
LogDroppedConnections                 Disable
FileName                              %systemroot%\system32\LogFiles\Firewall\pfirewall.log
MaxFileSize                           4096

Ok.
```
**SERVICES**:

```

```
**OTHERS**:

```
 1   exploit/windows/local/bypassuac_sdclt                          Yes                      The target appears to be vulnerable.
 2   exploit/windows/local/cve_2019_1458_wizardopium                Yes                      The target appears to be vulnerable.
 3   exploit/windows/local/cve_2020_1048_printerdemon               Yes                      The target appears to be vulnerable.
 4   exploit/windows/local/cve_2020_1337_printerdemon               Yes                      The target appears to be vulnerable.
 5   exploit/windows/local/cve_2022_21999_spoolfool_privesc         Yes                      The target appears to be vulnerable


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
wade:parzival


wordpressuser567
YSPgW[%C.mQE
```
</details>

<details><summary><ins>HASHES:</ins></summary>

```

```
</details>

# PROOFS

<details><summary><ins>Proofs</ins></summary>

Final payload:
```

```

```
user.txt:3b99fbdc6d430bfb51c72c651a261927
```

```

```

</details>