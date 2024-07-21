# BOX NAME: Year Of The Fox
**LINK**: https://tryhackme.com/room/yotf

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
[+] IP:	10.10.141.20
[+] URL: http://year-of-the-fox.lan
[+] FQDN: year-of-the-fox.lan
[+] WORKGRP: YEAROFTHEFOX
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap.log
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-22 12:31 CET
Nmap scan report for 10.10.141.20
Host is up (0.080s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT    STATE SERVICE     VERSION
80/tcp  open  http        Apache httpd 2.4.29
|_http-title: 401 Unauthorized
| http-auth: 
| HTTP/1.1 401 Unauthorized\x0D
|_  Basic realm=You want in? Gotta guess the password!
|_http-server-header: Apache/2.4.29 (Ubuntu)
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: YEAROFTHEFOX)
445/tcp open  netbios-ssn Samba smbd 4.7.6-Ubuntu (workgroup: YEAROFTHEFOX)
Service Info: Hosts: year-of-the-fox.lan, YEAR-OF-THE-FOX

Host script results:
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported                                                                                   
|_  message_signing: disabled (dangerous, but default)                                                              
| smb2-time:                                                                                                        
|   date: 2023-12-22T11:32:01                                                                                       
|_  start_date: N/A                                                                                                 
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.7.6-Ubuntu)
|   Computer name: year-of-the-fox
|   NetBIOS computer name: YEAR-OF-THE-FOX\x00
|   Domain name: lan
|   FQDN: year-of-the-fox.lan
|_  System time: 2023-12-22T11:32:02+00:00
|_nbstat: NetBIOS name: YEAR-OF-THE-FOX, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required
|_clock-skew: mean: 0s, deviation: 1s, median: 0s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 18.39 seconds

----------------------------------------------------------------


└─$ sudo nmap -sU $IP -F
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-22 14:23 CET
Nmap scan report for year-of-the-fox.lan (10.10.141.20)
Host is up (0.052s latency).
Not shown: 97 closed udp ports (port-unreach)
PORT    STATE         SERVICE
68/udp  open|filtered dhcpc
137/udp open          netbios-ns
138/udp open|filtered netbios-dgm

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
└─$ whatweb $IP -v
WhatWeb report for http://10.10.141.20
Status    : 401 Unauthorized
Title     : 401 Unauthorized
IP        : 10.10.141.20
Country   : RESERVED, ZZ

Summary   : Apache[2.4.29], HTTPServer[Ubuntu Linux][Apache/2.4.29 (Ubuntu)], WWW-Authenticate[You want in? Gotta guess the password!][Basic]

Detected Plugins:
[ Apache ]
        The Apache HTTP Server Project is an effort to develop and 
        maintain an open-source HTTP server for modern operating 
        systems including UNIX and Windows NT. The goal of this 
        project is to provide a secure, efficient and extensible 
        server that provides HTTP services in sync with the current 
        HTTP standards. 

        Version      : 2.4.29 (from HTTP Server Header)
        Google Dorks: (3)
        Website     : http://httpd.apache.org/

[ HTTPServer ]
        HTTP server header string. This plugin also attempts to 
        identify the operating system from the server header. 

        OS           : Ubuntu Linux
        String       : Apache/2.4.29 (Ubuntu) (from server string)

[ WWW-Authenticate ]
        This plugin identifies the WWW-Authenticate HTTP header and 
        extracts the authentication method and realm. 

        Module       : Basic
        String       : You want in? Gotta guess the password!

HTTP Headers:                                                                                                                                                                                                                           
        HTTP/1.1 401 Unauthorized                                                                                                                                                                                                       
        Date: Fri, 22 Dec 2023 11:31:56 GMT                                                                                                                                                                                             
        Server: Apache/2.4.29 (Ubuntu)                                                                                                                                                                                                  
        WWW-Authenticate: Basic realm="You want in? Gotta guess the password!"                                                                                                                                                                                                                                       
        Content-Length: 459                                                                                                                                                                                                                                                                                          
        Connection: close                                                                                                                                                                                                                                                                                            
        Content-Type: text/html; charset=iso-8859-1      
```

nikto-scan
```
└─$ nikto -h $URL
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.10.141.20
+ Target Hostname:    year-of-the-fox.lan
+ Target Port:        80
+ Start Time:         2023-12-22 12:35:28 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ / - Requires Authentication for realm 'You want in? Gotta guess the password!'
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.29 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 8113 requests: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2023-12-22 12:43:23 (GMT1) (475 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing
```
http://year-of-the-fox.lan - Basic Auth. Possible usernames = fox+rascal
```
other
```

```

</details>

<details><summary><ins>SERVICES</ins></summary>

SMB
```
└─$ smbclient -L $IP

Password for [WORKGROUP\jml]:

        Sharename       Type      Comment
        ---------       ----      -------
        yotf            Disk      Fox's Stuff -- keep out!
        IPC$            IPC       IPC Service (year-of-the-fox server (Samba, Ubuntu))Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        YEAROFTHEFOX         YEAR-OF-THE-FOX
```

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

**SUID's**:

```

```
**SGID's**:

```

```
**OTHERS**:

```
└─$ cat cipher.txt | tr -d '\n' | base32 -d | tr -d '\n' | base64 -d | tr -d '\n' | xxd -r -p
5c8d7f5eaa6208803b7866d9cbf0ea8a30198a2f8f4426cbe5a4267b272e90a8

└─$ cat creds1.txt | tr -d '\n' | base32 -d | tr -d '\n' | base64 -d | tr -d '\n' | xxd -r -p
d6ccfee53c53d3bf1e2e6f6a078c60b56db6adc2ab92441f5773bde8afe3fbca

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

fox:taurus
rascal:

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

```

```

```

</details>