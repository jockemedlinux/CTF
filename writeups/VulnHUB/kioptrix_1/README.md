### BOX NAME: Kioptrix 1

### LINK:  [https://www.vulnhub.com/entry/kioptrix-level-1-1,22/\[\](https://www.vulnhub.com/entry/kioptrix-2014-5,62/)](https://www.vulnhub.com/entry/kioptrix-level-1-1,22/%5B%5D%28https://www.vulnhub.com/entry/kioptrix-2014-5,62/%29 "https://www.vulnhub.com/entry/kioptrix-level-1-1,22/%5B%5D(https://www.vulnhub.com/entry/kioptrix-2014-5,62/)")

### **IP=192.168.56.111**

### **URL=http://192.168.56.111**

# Credentials:

<span style="color: #ff0000;">username:password</span>

# Hashes:

# Remote Enumeration & Scan-outputs:

### <ins>Host Discovery</ins>

```bash
└─# netdiscover -r 192.168.56.1/24 -i eth0 -L -N
 192.168.56.1    0a:00:27:00:00:0b      1      60  Unknown vendor
 192.168.56.100  08:00:27:8d:88:af      1      60  PCS Systemtechnik GmbH

-- Active scan completed, 2 Hosts found. Continuing to listen passively.

 192.168.56.111  08:00:27:70:50:04      1      60  PCS Systemtechnik GmbH
```

### <ins>Nmap scan</ins>

```bash
└─# nmap -n -sS -sC -sV --version-all $IP -p-
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-14 09:15 EST
Nmap scan report for 192.168.56.111
Host is up (0.00022s latency).
Not shown: 65529 closed tcp ports (reset)
PORT      STATE SERVICE     VERSION
22/tcp    open  ssh         OpenSSH 2.9p2 (protocol 1.99)
|_sshv1: Server supports SSHv1
| ssh-hostkey: 
|   1024 b8746cdbfd8be666e92a2bdf5e6f6486 (RSA1)
|   1024 8f8e5b81ed21abc180e157a33c85c471 (DSA)
|_  1024 ed4ea94a0614ff1514ceda3a80dbe281 (RSA)
80/tcp    open  http        Apache httpd 1.3.20 ((Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b)
|_http-server-header: Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-title: Test Page for the Apache Web Server on Red Hat Linux
111/tcp   open  rpcbind     2 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2            111/tcp   rpcbind
|   100000  2            111/udp   rpcbind
|   100024  1          32768/tcp   status
|_  100024  1          32768/udp   status
139/tcp   open  netbios-ssn Samba smbd (workgroup: MYGROUP)
443/tcp   open  ssl/https   Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b
|_http-server-header: Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b
|_ssl-date: 2023-01-14T19:15:35+00:00; +4h59m59s from scanner time.
| ssl-cert: Subject: commonName=localhost.localdomain/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--
| Not valid before: 2009-09-26T09:32:06
|_Not valid after:  2010-09-26T09:32:06
| sslv2: 
|   SSLv2 supported
|   ciphers: 
|     SSL2_RC4_128_WITH_MD5
|     SSL2_DES_192_EDE3_CBC_WITH_MD5
|     SSL2_DES_64_CBC_WITH_MD5
|     SSL2_RC4_64_WITH_MD5
|     SSL2_RC4_128_EXPORT40_WITH_MD5
|     SSL2_RC2_128_CBC_EXPORT40_WITH_MD5
|_    SSL2_RC2_128_CBC_WITH_MD5
|_http-title: 400 Bad Request
32768/tcp open  status      1 (RPC #100024)
MAC Address: 08:00:27:70:50:04 (Oracle VirtualBox virtual NIC)

Host script results:
|_smb2-time: Protocol negotiation failed (SMB2)
|_clock-skew: 4h59m58s
|_nbstat: NetBIOS name: KIOPTRIX, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
```

### <ins>Nikto scan</ins>

```bash
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          192.168.56.111
+ Target Hostname:    192.168.56.111
+ Target Port:        80
+ Start Time:         2023-01-14 09:24:49 (GMT-5)
---------------------------------------------------------------------------
+ Server: Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b
+ Server may leak inodes via ETags, header found with file /, inode: 34821, size: 2890, mtime: Wed Sep  5 23:12:46 2001
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ OSVDB-27487: Apache is vulnerable to XSS via the Expect header
+ OpenSSL/0.9.6b appears to be outdated (current is at least 1.1.1). OpenSSL 1.0.0o and 0.9.8zc are also current.
+ mod_ssl/2.8.4 appears to be outdated (current is at least 2.8.31) (may depend on server version)
+ Apache/1.3.20 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ OSVDB-838: Apache/1.3.20 - Apache 1.x up 1.2.34 are vulnerable to a remote DoS and possible code execution. CAN-2002-0392.
+ OSVDB-4552: Apache/1.3.20 - Apache 1.3 below 1.3.27 are vulnerable to a local buffer overflow which allows attackers to kill any process on the system. CAN-2002-0839.
+ OSVDB-2733: Apache/1.3.20 - Apache 1.3 below 1.3.29 are vulnerable to overflows in mod_rewrite and mod_cgi. CAN-2003-0542.
+ mod_ssl/2.8.4 - mod_ssl 2.8.7 and lower are vulnerable to a remote buffer overflow which may allow a remote shell. http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2002-0082, OSVDB-756.
+ Allowed HTTP Methods: GET, HEAD, OPTIONS, TRACE 
+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ ///etc/hosts: The server install allows reading of any system file by adding an extra '/' to the URL.
+ OSVDB-682: /usage/: Webalizer may be installed. Versions lower than 2.01-09 vulnerable to Cross Site Scripting (XSS).
+ OSVDB-3268: /manual/: Directory indexing found.
+ OSVDB-3092: /manual/: Web server manual found.
+ OSVDB-3268: /icons/: Directory indexing found.
+ OSVDB-3233: /icons/README: Apache default file found.
+ OSVDB-3092: /test.php: This might be interesting...
+ /wp-content/themes/twentyeleven/images/headers/server.php?filesrc=/etc/hosts: A PHP backdoor file manager was found.
+ /wordpresswp-content/themes/twentyeleven/images/headers/server.php?filesrc=/etc/hosts: A PHP backdoor file manager was found.
+ /wp-includes/Requests/Utility/content-post.php?filesrc=/etc/hosts: A PHP backdoor file manager was found.
+ /wordpresswp-includes/Requests/Utility/content-post.php?filesrc=/etc/hosts: A PHP backdoor file manager was found.
+ /wp-includes/js/tinymce/themes/modern/Meuhy.php?filesrc=/etc/hosts: A PHP backdoor file manager was found.
+ /wordpresswp-includes/js/tinymce/themes/modern/Meuhy.php?filesrc=/etc/hosts: A PHP backdoor file manager was found.
+ /assets/mobirise/css/meta.php?filesrc=: A PHP backdoor file manager was found.
+ /login.cgi?cli=aa%20aa%27cat%20/etc/hosts: Some D-Link router remote command execution.
+ /shell?cat+/etc/hosts: A backdoor was identified.
+ 8724 requests: 0 error(s) and 30 item(s) reported on remote host
+ End Time:           2023-01-14 09:25:15 (GMT-5) (26 seconds)
```

### <ins>Whatweb scan</ins>

```bash
WhatWeb report for http://192.168.56.111
Status    : 200 OK
Title     : Test Page for the Apache Web Server on Red Hat Linux
IP        : 192.168.56.111
Country   : RESERVED, ZZ

Summary   : Apache[1.3.20][mod_ssl/2.8.4], Email[webmaster@example.com], HTTPServer[Red Hat Linux][Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b], OpenSSL[0.9.6b]

Detected Plugins:
[ Apache ]
        The Apache HTTP Server Project is an effort to develop and 
        maintain an open-source HTTP server for modern operating 
        systems including UNIX and Windows NT. The goal of this 
        project is to provide a secure, efficient and extensible 
        server that provides HTTP services in sync with the current 
        HTTP standards. 

        Version      : 1.3.20 (from HTTP Server Header)
        Module       : mod_ssl/2.8.4
        Google Dorks: (3)
        Website     : http://httpd.apache.org/

[ Email ]
        Extract email addresses. Find valid email address and 
        syntactically invalid email addresses from mailto: link 
        tags. We match syntactically invalid links containing 
        mailto: to catch anti-spam email addresses, eg. bob at 
        gmail.com. This uses the simplified email regular 
        expression from 
        http://www.regular-expressions.info/email.html for valid 
        email address matching. 

        String       : webmaster@example.com

[ HTTPServer ]
        HTTP server header string. This plugin also attempts to 
        identify the operating system from the server header. 

        OS           : Red Hat Linux
        String       : Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b (from server string)

[ OpenSSL ]
        The OpenSSL Project is a collaborative effort to develop a 
        robust, commercial-grade, full-featured, and Open Source 
        toolkit implementing the Secure Sockets Layer (SSL v2/v3) 
        and Transport Layer Security (TLS v1) protocols as well as 
        a full-strength general purpose cryptography library. 

        Version      : 0.9.6b
        Website     : http://www.openssl.org/

HTTP Headers:
        HTTP/1.1 200 OK
        Date: Sat, 14 Jan 2023 19:21:26 GMT
        Server: Apache/1.3.20 (Unix)  (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b
        Last-Modified: Thu, 06 Sep 2001 03:12:46 GMT
        ETag: "8805-b4a-3b96e9ae"
        Accept-Ranges: bytes
        Content-Length: 2890
        Connection: close
        Content-Type: text/html
```

# Hosts and computers:

### **HOSTS:**

\*\*FQDN: \*\*  
\*\*COMPUTER NAME: \*\*  
**OS:**

# Special searchsploit findings:

\[+\] Port 22 \[SSH\]  
<span style="color: #ff0000;">\->> Look for credz and keys. Old SSH. Searchsploit?  
OpenSSH 2.9p2 (protocol 1.99)</span>

\[+\] Port 80 \[HTTP\]  
<span style="color: #ff0000;">\->> Nikto, ffuf, feroxbuster. Old Apache. Searchsploit?  
Apache httpd 1.3.20 ((Unix) (Red-Hat/Linux) mod_ssl/2.8.4 OpenSSL/0.9.6b)  
\->> /cgi-bin/</span>

\[+\] Port 111, 139, 443 \[NFS\]  
<span style="color: #ff0000;">\->> nmap smb scriptscan, enum4linux, nbtscan  
</span>

\[+\] OTHERS

`curl http://127.0.0.1:1080/mrtg --proxy 192.168.56.111:80 -k -L -v | html2text`

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
linux/samba/trans2open
mod_ssl (OpenFuck Exploit)
```

# Writeup:

==REPORT==

```
Started with ...
```

==PROOF==

![a3350e0dc49fd7ff3b171c51c1fdd420.png](../../_resources/a3350e0dc49fd7ff3b171c51c1fdd420.png)