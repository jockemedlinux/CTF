# BOX NAME:Thales

LINK: [](https://www.vulnhub.com/entry/kioptrix-2014-5,62/)

### **IP=192.168.56.110**

**URL=http://192.168.56.110**

# Credentials:

thales:vodka06

# Hashes:

# Remote Enumeration & Scan-outputs:

### <ins>Host Discovery</ins>

```
netdiscover -r 192.168.56.1/24 -i eth0
-> 192.168.56.110
```

### <ins>Nmap scan</ins>

```
└─# nmap -sS -sV $IP -p-
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-12 12:12 EST
Nmap scan report for 192.168.56.110
Host is up (0.00014s latency).
Not shown: 65533 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
8080/tcp open  http    Apache Tomcat 9.0.52
MAC Address: 08:00:27:41:C9:37 (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.10 seconds
```

```
└─# nmap -A $IP -n
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-12 12:11 EST
Nmap scan report for 192.168.56.110
Host is up (0.00079s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8c19ab9172a571d86d751d8f65dfe132 (RSA)
|   256 906ea0eed5296cb97b05dbc6825c19bf (ECDSA)
|_  256 544d7be8f97f21343eed0fd9fe93bf00 (ED25519)
8080/tcp open  http    Apache Tomcat 9.0.52
|_http-title: Apache Tomcat/9.0.52
|_http-favicon: Apache Tomcat
MAC Address: 08:00:27:41:C9:37 (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 4.X|5.X
OS CPE: cpe:/o:linux:linux_kernel:4 cpe:/o:linux:linux_kernel:5
OS details: Linux 4.15 - 5.6
Network Distance: 1 hop
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.79 ms 192.168.56.110

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.41 seconds
```

### <ins>Nikto scan</ins>

```
└─# nikto -h $IP --port 8080
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          192.168.56.110
+ Target Hostname:    192.168.56.110
+ Target Port:        8080
+ Start Time:         2023-01-12 12:12:04 (GMT-5)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OSVDB-39272: /favicon.ico file identifies this app/server as: Apache Tomcat (possibly 5.5.26 through 8.0.15), Alfresco Community
+ Allowed HTTP Methods: GET, HEAD, POST, PUT, DELETE, OPTIONS 
+ OSVDB-397: HTTP method ('Allow' Header): 'PUT' method could allow clients to save files on the web server.
+ OSVDB-5646: HTTP method ('Allow' Header): 'DELETE' may allow clients to remove files on the web server.
+ /examples/servlets/index.html: Apache Tomcat default JSP pages present.
+ OSVDB-3720: /examples/jsp/snp/snoop.jsp: Displays information about page retrievals, including other users.
+ /manager/html: Default Tomcat Manager / Host Manager interface found
+ /host-manager/html: Default Tomcat Manager / Host Manager interface found
+ /manager/status: Default Tomcat Server Status interface found
+ 8221 requests: 0 error(s) and 12 item(s) reported on remote host
+ End Time:           2023-01-12 12:12:48 (GMT-5) (44 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

### <ins>Whatweb scan</ins>

```
└─# whatweb $IP:8080 -v
WhatWeb report for http://192.168.56.110:8080
Status    : 200 OK
Title     : Apache Tomcat/9.0.52
IP        : 192.168.56.110
Country   : RESERVED, ZZ

Summary   : HTML5

Detected Plugins:
[ HTML5 ]
        HTML version 5, detected by the doctype declaration 


HTTP Headers:
        HTTP/1.1 200 
        Content-Type: text/html;charset=UTF-8
        Transfer-Encoding: chunked
        Date: Thu, 12 Jan 2023 17:14:20 GMT
        Connection: close
```

# Hosts and computers:

### **HOSTS:**

\*\*FQDN: \*\*  
\*\*COMPUTER NAME: \*\*  
**OS:**

# Special searchsploit findings:

\[+\] Port 22 \[SSH\]

```
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8c19ab9172a571d86d751d8f65dfe132 (RSA)
|   256 906ea0eed5296cb97b05dbc6825c19bf (ECDSA)
|_  256 544d7be8f97f21343eed0fd9fe93bf00 (ED25519)

# BANNER
```

\[+\] Port 8080 \[HTTP\]

```
Apache Tomcat Version 9.0.52
```

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

\*\*Kernel Info:  
\*\**"file /bin/bash | lsb_release -a | uname -a"*

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

==user.txt : a837c0b5d2a8a07225fd9905f5a0e9c4==

==root.txt : 3a1c85bebf8833b0ecae900fb8598b17==