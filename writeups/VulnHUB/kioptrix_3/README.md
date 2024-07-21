# BOX NAME: Kioptrix 3

LINK: [https://www.vulnhub.com/entry/kioptrix-level-12-3,24/\[\](https://www.vulnhub.com/entry/kioptrix-2014-5,62/)](https://www.vulnhub.com/entry/kioptrix-level-12-3,24/%5B%5D%28https://www.vulnhub.com/entry/kioptrix-2014-5,62/%29 "https://www.vulnhub.com/entry/kioptrix-level-12-3,24/%5B%5D(https://www.vulnhub.com/entry/kioptrix-2014-5,62/)")

**IP=192.168.45.112**

**URL=http://192.168.56.112**

# Credentials:

318d8dd409db395f0317efa71b3bad13e1fb9857|administrator|salt = gtZBO2PewhZHR10hGXLaSt0Bc5Ub73  
\[mysql\] root:fuckeyou   
admin | n0t7t1k4

# Hashes:

```
318d8dd409db395f0317efa71b3bad13e1fb9857|administrator
```

![d0ca469c2283af3240495945767a52d4.png](../../_resources/d0ca469c2283af3240495945767a52d4.png)

```
+----+------------+----------------------------------+
| id | username   | password                         |
+----+------------+----------------------------------+
|  1 | dreg       | 0d3eccfb887aabd50f243b3f155c0f85 |  Mast3r
|  2 | loneferret | 5badcaf789d3d1d09794d8f021f40f0e |  starwars
+----+------------+----------------------------------+
```

# Remote Enumeration & Scan-outputs:

### <ins>Host Discovery</ins>

```
[+]
```

### <ins>Nmap scan</ins>

```bash
└─# nmap -n 192.168.56.112 -sS -sC -sV -p-
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-14 14:19 EST
Nmap scan report for 192.168.56.112
Host is up (0.00022s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 4.7p1 Debian 8ubuntu1.2 (protocol 2.0)
| ssh-hostkey: 
|   1024 30e3f6dc2e225d17ac460239ad71cb49 (DSA)
|_  2048 9a82e696e47ed6a6d74544cb19aaecdd (RSA)
80/tcp open  http    Apache httpd 2.2.8 ((Ubuntu) PHP/5.2.4-2ubuntu5.6 with Suhosin-Patch)
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: Ligoat Security - Got Goat? Security ...
|_http-server-header: Apache/2.2.8 (Ubuntu) PHP/5.2.4-2ubuntu5.6 with Suhosin-Patch
MAC Address: 08:00:27:70:50:04 (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### <ins>Nikto scan</ins>

```bash
└─# nikto -h $IP 
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          192.168.56.112
+ Target Hostname:    192.168.56.112
+ Target Port:        80
+ Start Time:         2023-01-14 14:28:35 (GMT-5)
---------------------------------------------------------------------------
+ Server: Apache/2.2.8 (Ubuntu) PHP/5.2.4-2ubuntu5.6 with Suhosin-Patch
+ Retrieved x-powered-by header: PHP/5.2.4-2ubuntu5.6
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Cookie PHPSESSID created without the httponly flag
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ PHP/5.2.4-2ubuntu5.6 appears to be outdated (current is at least 7.2.12). PHP 5.6.33, 7.0.27, 7.1.13, 7.2.1 may also current release for each branch.
+ Apache/2.2.8 appears to be outdated (current is at least Apache/2.4.37). Apache 2.2.34 is the EOL for the 2.x branch.
+ Server may leak inodes via ETags, header found with file /favicon.ico, inode: 631780, size: 23126, mtime: Fri Jun  5 15:22:00 2009
+ Web Server returns a valid response with junk HTTP methods, this may cause false positives.
+ OSVDB-877: HTTP TRACE method is active, suggesting the host is vulnerable to XST
+ OSVDB-12184: /?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings.
+ OSVDB-12184: /?=PHPE9568F36-D428-11d2-A769-00AA001ACF42: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings.
+ OSVDB-12184: /?=PHPE9568F34-D428-11d2-A769-00AA001ACF42: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings.
+ OSVDB-12184: /?=PHPE9568F35-D428-11d2-A769-00AA001ACF42: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings.
+ OSVDB-3092: /phpmyadmin/changelog.php: phpMyAdmin is for managing MySQL databases, and should be protected or limited to authorized hosts.
+ OSVDB-3268: /icons/: Directory indexing found.
+ OSVDB-3233: /icons/README: Apache default file found.
+ /phpmyadmin/: phpMyAdmin directory found
+ OSVDB-3092: /phpmyadmin/Documentation.html: phpMyAdmin is for managing MySQL databases, and should be protected or limited to authorized hosts.
+ 7914 requests: 0 error(s) and 19 item(s) reported on remote host
+ End Time:           2023-01-14 14:29:11 (GMT-5) (36 seconds)
```

### <ins>Whatweb scan</ins>

```bash
└─# whatweb $URL -v
WhatWeb report for http://kioptrix3.com
Status    : 200 OK
Title     : Ligoat Security - Got Goat? Security ...
IP        : 192.168.56.112
Country   : RESERVED, ZZ

Summary   : Apache[2.2.8], Cookies[PHPSESSID], HTTPServer[Ubuntu Linux][Apache/2.2.8 (Ubuntu) PHP/5.2.4-2ubuntu5.6 with Suhosin-Patch], maybe LotusCMS, Meta-Author[name of author - Manjeet Singh Sawhney   www.manjeetss.com], PHP[5.2.4-2ubuntu5.6][Suhosin-Patch], X-Powered-By[PHP/5.2.4-2ubuntu5.6]

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

[ Cookies ]
        Display the names of cookies in the HTTP headers. The                                                                                                              
        values are not returned to save on space.                                                                                                                          

        String       : PHPSESSID

[ HTTPServer ]
        HTTP server header string. This plugin also attempts to 
        identify the operating system from the server header. 

        OS           : Ubuntu Linux
        String       : Apache/2.2.8 (Ubuntu) PHP/5.2.4-2ubuntu5.6 with Suhosin-Patch (from server string)

[ LotusCMS ]
        LotusCMS (previously ArboroianCMS) brings to the forefront 
        design and design integration into one of the most 
        neglected CMS niches - Databaseless Web-Design and 
        Development. 

        Certainty    : maybe
        Google Dorks: (1)
        Website     : http://www.lotuscms.org/

[ Meta-Author ]
        This plugin retrieves the author name from the meta name 
        tag - info: 
        http://www.webmarketingnow.com/tips/meta-tags-uncovered.html
        #author

        String       : name of author - Manjeet Singh Sawhney   www.manjeetss.com

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

[ X-Powered-By ]
        X-Powered-By HTTP header 

        String       : PHP/5.2.4-2ubuntu5.6 (from x-powered-by string)

HTTP Headers:
        HTTP/1.1 200 OK
        Date: Sat, 14 Jan 2023 19:30:25 GMT
        Server: Apache/2.2.8 (Ubuntu) PHP/5.2.4-2ubuntu5.6 with Suhosin-Patch
        X-Powered-By: PHP/5.2.4-2ubuntu5.6
        Set-Cookie: PHPSESSID=7d3954a71519e25f23740882dbf546d9; path=/
        Expires: Thu, 19 Nov 1981 08:52:00 GMT                                                                                                                             
        Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
        Pragma: no-cache
        Content-Length: 1819
        Connection: close                                                                                                                                                  
        Content-Type: text/html
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

```
Good for you for getting here.
Regardless of the matter (staying within the spirit of the game of course)
you got here, congratulations are in order. Wasn't that bad now was it.

Went in a different direction with this VM. Exploit based challenges are
nice. Helps workout that information gathering part, but sometimes we
need to get our hands dirty in other things as well.
Again, these VMs are beginner and not intented for everyone. 
Difficulty is relative, keep that in mind.

The object is to learn, do some research and have a little (legal)
fun in the process.


I hope you enjoyed this third challenge.

Steven McElrea
aka loneferret
http://www.kioptrix.com


Credit needs to be given to the creators of the gallery webapp and CMS used
for the building of the Kioptrix VM3 site.

Main page CMS: 
http://www.lotuscms.org

Gallery application: 
Gallarific 2.1 - Free Version released October 10, 2009
http://www.gallarific.com
Vulnerable version of this application can be downloaded
from the Exploit-DB website:
http://www.exploit-db.com/exploits/15891/

The HT Editor can be found here:
http://hte.sourceforge.net/downloads.html
And the vulnerable version on Exploit-DB here:
http://www.exploit-db.com/exploits/17083/


Also, all pictures were taken from Google Images, so being part of the
public domain I used them.
```

![e385f7c3e8909853ee89379aa8993027.png](../../_resources/e385f7c3e8909853ee89379aa8993027.png)