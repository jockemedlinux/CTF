# BOX NAME: Kioptrix 4

LINK: [https://www.vulnhub.com/entry/kioptrix-level-13-4,25/\[\](https://www.vulnhub.com/entry/kioptrix-2014-5,62/)](https://www.vulnhub.com/entry/kioptrix-level-13-4,25/%5B%5D%28https://www.vulnhub.com/entry/kioptrix-2014-5,62/%29 "https://www.vulnhub.com/entry/kioptrix-level-13-4,25/%5B%5D(https://www.vulnhub.com/entry/kioptrix-2014-5,62/)")

### **IP= 192.168.56.115**

**URL= http://192.168.56.115**

# Credentials:

john:
robert:

```
+----------+-----------------------+
| username | password              |
+----------+-----------------------+
| robert   | ADGAdsafdfwt4gadfga== |
| john     | MyNameIsJohn          |
+----------+-----------------------+
```

```
S-1-22-1-1000 Unix User\loneferret (Local User)
S-1-22-1-1001 Unix User\john (Local User)
S-1-22-1-1002 Unix User\robert (Local User)
```

# Hashes:

# Remote Enumeration & Scan-outputs:

### <ins>Host Discovery</ins>

```
─# netdiscover -r 192.168.56.1/24 -i eth0 -L -N
 192.168.56.1    0a:00:27:00:00:0b      1      60  Unknown vendor
 192.168.56.100  08:00:27:8a:bf:9f      1      60  PCS Systemtechnik GmbH
 192.168.56.115  08:00:27:74:75:8d      1      60  PCS Systemtechnik GmbH
```

### <ins>Nmap scan</ins>

```
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 4.7p1 Debian 8ubuntu1.2 (protocol 2.0)
| ssh-hostkey: 
|   1024 9bad4ff21ec5f23914b9d3a00be84171 (DSA)
|_  2048 8540c6d541260534adf86ef2a76b4f0e (RSA)
80/tcp  open  http        Apache httpd 2.2.8 ((Ubuntu) PHP/5.2.4-2ubuntu5.6 with Suhosin-Patch)
|_http-server-header: Apache/2.2.8 (Ubuntu) PHP/5.2.4-2ubuntu5.6 with Suhosin-Patch
|_http-title: Site doesn't have a title (text/html).
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 3.0.28a (workgroup: WORKGROUP)
MAC Address: 08:00:27:74:75:8D (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 2h30m02s, deviation: 3h32m08s, median: 1s
|_smb2-time: Protocol negotiation failed (SMB2)
|_nbstat: NetBIOS name: KIOPTRIX4, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb-os-discovery: 
|   OS: Unix (Samba 3.0.28a)
|   Computer name: Kioptrix4
|   NetBIOS computer name: 
|   Domain name: localdomain
|   FQDN: Kioptrix4.localdomain
|_  System time: 2023-01-17T13:21:01-05:00

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 53.35 seconds
```

### <ins>Nikto scan</ins>

```
[+]
```

### <ins>Whatweb scan</ins>

```
└─# whatweb $URL -v
WhatWeb report for http://192.168.56.115
Status    : 200 OK
Title     : <None>
IP        : 192.168.56.115
Country   : RESERVED, ZZ

Summary   : Apache[2.2.8], HTTPServer[Ubuntu Linux][Apache/2.2.8 (Ubuntu) PHP/5.2.4-2ubuntu5.6 with Suhosin-Patch], PasswordField[mypassword], PHP[5.2.4-2ubuntu5.6][Suhosin-Patch], X-Powered-By[PHP/5.2.4-2ubuntu5.6]

Detected Plugins:
[ Apache ]
        The Apache HTTP Server Project is an effort to develop and 
        maintain an open-source HTTP server for modern operating 
        systems including UNIX and Windows NT. The goal of this 
        project is to provide a secure, efficient and extensible 
        server that provides HTTP services in sync with the current 
        HTTP standards. 

        Version      : 2.2.8 (from HTTP Server Header)
        Google Dorks: (3)
        Website     : http://httpd.apache.org/

[ HTTPServer ]
        HTTP server header string. This plugin also attempts to 
        identify the operating system from the server header. 

        OS           : Ubuntu Linux
        String       : Apache/2.2.8 (Ubuntu) PHP/5.2.4-2ubuntu5.6 with Suhosin-Patch (from server string)

[ PHP ]
        PHP is a widely-used general-purpose scripting language 
        that is especially suited for Web development and can be 
        embedded into HTML. This plugin identifies PHP errors, 
        modules and versions and extracts the local file path and 
        username if present. 

        Version      : 5.2.4-2ubuntu5.6
        Module       : Suhosin-Patch
        Version      : 5.2.4-2ubuntu5.6
        Google Dorks: (2)
        Website     : http://www.php.net/

[ PasswordField ]
        find password fields 

        String       : mypassword (from field name)

[ X-Powered-By ]
        X-Powered-By HTTP header 

        String       : PHP/5.2.4-2ubuntu5.6 (from x-powered-by string)

HTTP Headers:
        HTTP/1.1 200 OK
        Date: Tue, 17 Jan 2023 18:36:09 GMT
        Server: Apache/2.2.8 (Ubuntu) PHP/5.2.4-2ubuntu5.6 with Suhosin-Patch
        X-Powered-By: PHP/5.2.4-2ubuntu5.6
        Content-Length: 1255
        Connection: close
        Content-Type: text/html
```

### Webfiles

```
logout.php              [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 0ms]
.htaccess               [Status: 403, Size: 331, Words: 24, Lines: 11, Duration: 0ms]
.                       [Status: 200, Size: 1255, Words: 50, Lines: 46, Duration: 1ms]
.html                   [Status: 403, Size: 327, Words: 24, Lines: 11, Duration: 0ms]
.htpasswd               [Status: 403, Size: 331, Words: 24, Lines: 11, Duration: 0ms]
.htm                    [Status: 403, Size: 326, Words: 24, Lines: 11, Duration: 0ms]
checklogin.php          [Status: 200, Size: 109, Words: 9, Lines: 1, Duration: 4ms]
.htpasswds              [Status: 403, Size: 332, Words: 24, Lines: 11, Duration: 2ms]
index.php               [Status: 200, Size: 1255, Words: 50, Lines: 46, Duration: 627ms]
member.php              [Status: 302, Size: 220, Words: 22, Lines: 2, Duration: 633ms]
.htgroup                [Status: 403, Size: 330, Words: 24, Lines: 11, Duration: 0ms]
.htaccess.bak           [Status: 403, Size: 335, Words: 24, Lines: 11, Duration: 0ms]
login_success.php       [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 5ms]
.htuser                 [Status: 403, Size: 329, Words: 24, Lines: 11, Duration: 1ms]
.htc                    [Status: 403, Size: 326, Words: 24, Lines: 11, Duration: 0ms]
.ht                     [Status: 403, Size: 325, Words: 24, Lines: 11, Duration: 0ms]
.htacess                [Status: 403, Size: 330, Words: 24, Lines: 11, Duration: 0ms]
.htaccess.old           [Status: 403, Size: 335, Words: 24, Lines: 11, Duration: 0ms]
```

### Webdirs

```
images                  [Status: 301, Size: 356, Words: 23, Lines: 10, Duration: 0ms]
index                   [Status: 200, Size: 1255, Words: 50, Lines: 46, Duration: 0ms]
john                    [Status: 301, Size: 354, Words: 23, Lines: 10, Duration: 0ms]
server-status           [Status: 403, Size: 334, Words: 24, Lines: 11, Duration: 3ms]
                        [Status: 200, Size: 1255, Words: 50, Lines: 46, Duration: 1ms]
robert                  [Status: 301, Size: 356, Words: 23, Lines: 10, Duration: 0ms]
                        [Status: 200, Size: 1255, Words: 50, Lines: 46, Duration: 1ms]
checklogin              [Status: 200, Size: 109, Words: 9, Lines: 1, Duration: 8ms]
index                   [Status: 200, Size: 1255, Words: 50, Lines: 46, Duration: 1ms]
                        [Status: 200, Size: 1255, Words: 50, Lines: 46, Duration: 4ms]
```

# Hosts and computers:

### **HOSTS:**

\*\*FQDN: \*\*
\*\*COMPUTER NAME: \*\*
**OS:**

# Special searchsploit findings:

\[+\] Port 21 \[FTP\]
\[+\] Port 22 \[SSH\]
\[+\] Port 23 \[TELNET\]
\[+\] Port 25 \[SMTP\]
\[+\] Port 53 \[DNS\]
\[+\] Port 80 \[HTTP\]
\[+\] Port 88 \[Kerberos\]
\[+\] Port 110 \[POP3\]
\[+\] Port 111 \[NFS\]
\[+\] Port 137 \[NETBIOS\]
\[+\] Port 139 \[NETBIOS\]
\[+\] Port 143 \[IMAP\]
\[+\] Port 443 \[HTTPS\]
\[+\] Port 445 \[SAMBA\]
\[+\] Port 464 \[Kerberos\]
\[+\] Port 465 \[SMTP\]
\[+\] Port 631 \[CUPS\]
\[+\] Port 587 \[SMTP /SSL\]
\[+\] Port 993 \[IMAP /SSL\]
\[+\] Port 995 \[POP3 /SSL\]
\[+\] Port 1194 \[OPENVPN\]
\[+\] Port 2049 \[NFS\]
\[+\] Port 3306 \[MySQL\]
\[+\] Port 5432 \[PostgreSQL\]
\[+\] Port 5900 \[VNC\]
\[+\] Port 5901 \[VNC\]
\[+\] Port 6001 \[X-SERVER\]
\[+\] Port 6667 \[IRC\]
\[+\] Port 6668 \[IRC\]
\[+\] Port 6669 \[IRC\]
\[+\] Port 6881 \[TORRENT\]
\[+\] Port 8080 \[HTTP\]

# Local Filesystem Findings:

### **FILES OF INTEREST**

```
[+]
```

**SUID**

```
[+]
```

**SGID**

```
[+]
```

### **Dumps, outputs, other useful information**

**Kernel Info:
*"file /bin/bash ; lsb_release -a ; uname -a"*

```
[+]
```

# Exploits and Payloads:

```
[+]
```

# Writeup:

==REPORT==

```
Started with ...
```

==PROOF==

```
bash-3.2# cat congrats.txt
Congratulations!
You've got root.

There is more then one way to get root on this system. Try and find them.
I've only tested two (2) methods, but it doesn't mean there aren't more.
As always there's an easy way, and a not so easy way to pop this box.
Look for other methods to get root privileges other than running an exploit.

It took a while to make this. For one it's not as easy as it may look, and
also work and family life are my priorities. Hobbies are low on my list.
Really hope you enjoyed this one.

If you haven't already, check out the other VMs available on:
www.kioptrix.com

Thanks for playing,
loneferret
```

![50646bb2c05662e4de7aaebe2a734f51.png](../../_resources/50646bb2c05662e4de7aaebe2a734f51.png)

# TAKEAWAYS

```
1.
2.
3.
```