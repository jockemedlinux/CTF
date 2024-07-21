# BOX NAME: Nagini
**LINK**: https://www.vulnhub.com/entry/harrypotter-nagini,689/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate box to find an HTTP3 resource.
2. Manipulate backend DB with a public tool through SSRF.
3. 
4. 
5.


This box had me stumped. I though for sure you'd find some interesting files or would be able to load som remote webserver to perform some kind of RFI trough the internalresourcefether. 
So I had to lookup some writeups and tools as I'm not superfamiliar with SSRF's. well, I still couldn't get the box to do what everybody else did. So I (probably) broke something or did something wrong.
I'll come back to this box sometime and try to figure it out.

```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.81
[+] URL:	http://nagini.com
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-nagini.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-11 21:34 CEST
Nmap scan report for nagini.com (10.77.0.81)
Host is up (0.00045s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 48df48372594c4746b2c6273bfb49fa9 (RSA)
|   256 1e3418175e17958f702f80a6d5b4173e (ECDSA)
|_  256 3e795f55553b127596b43ee3837a5494 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Site doesn't have a title (text/html).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.68 seconds

└─$ jml-scanner -u $IP -p 65535          

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|J|M|L|-|P|O|R|T|S|C|A|N|N|E|R|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

[+] Port 22 is open.
[+] Port 80 is open.

[+] A total of 2 found ports open
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
└─$ whatweb http://nagini.com --log-verbose=whatweb-nagini.log                                 
http://nagini.com [200 OK] Apache[2.4.38], Country[RESERVED][ZZ], HTTPServer[Debian Linux][Apache/2.4.38 (Debian)], IP[10.77.0.81]

```

nikto-scan
```
└─$ nikto -h $URL | tee nikto-nagini.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.81
+ Target Hostname:    nagini.com
+ Target Port:        80
+ Start Time:         2023-06-11 21:35:00 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.38 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.38 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Server may leak inodes via ETags, header found with file /, inode: 61, size: 5befef8ab2764, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ OPTIONS: Allowed HTTP Methods: GET, POST, OPTIONS, HEAD .
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 7962 requests: 0 error(s) and 6 item(s) reported on remote host
+ End Time:           2023-06-11 21:35:25 (GMT2) (25 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing
```   public $helpurl = 'https://help.joomla.org/proxy?keyref=Help{major}{minor}:{keyref}&lang={langcode}';

/note.txt
http://quic.nagini.hogwarts/internalResourceFeTcher.php?url=
```

other
```
 ___ _  _ ____ ____ ____ _  _
|    |\/| [__  |___ |___ |_/  by @r3dhax0r
|___ |  | ___| |___ |___ | \_ Version 1.1.3 K-RONA


 [+]  Deep Scan Results  [+] 

[✔] Target: http://nagini.com/joomla
[✔] Detected CMS: Joomla
[✔] CMS URL: https://joomla.org
[✔] Joomla Version: 3.9.25
[✔] Readme file: http://nagini.com/joomla/README.txt
[✔] Admin URL: http://nagini.com/joomlaadministrator


[✔] Open directories: 5
[*] Open directory url: 
   [>] http://nagini.com/joomlaadministrator/templates
   [>] http://nagini.com/joomlaimages/banners
   [>] http://nagini.com/joomlatmp
   [>] http://nagini.com/joomlaadministrator/modules
   [>] http://nagini.com/joomlaadministrator/components


[✔] Found potential Config file: 1
[*] Config URLs: 
   [c] http://nagini.com/joomla/configuration.php.bak


[x] Core vulnerability database not found!



 CMSeeK says ~ aloha
```

```
http://quic.nagini.hogwarts/internalResourceFeTcher.php?url=file:///etc/passwd
```
GOPHERUS
```
└─$ gopherus                                           

                                                                                                                    
  ________              .__                                                                                         
 /  _____/  ____ ______ |  |__   ___________ __ __  ______                                                          
/   \  ___ /  _ \\____ \|  |  \_/ __ \_  __ \  |  \/  ___/                                                          
\    \_\  (  <_> )  |_> >   Y  \  ___/|  | \/  |  /\___ \                                                           
 \______  /\____/|   __/|___|  /\___  >__|  |____//____  >                                                          
        \/       |__|        \/     \/                 \/                                                           
                                                                                                                    
                author: $_SpyD3r_$                                                                                  
                                                                                                                    
usage: gopherus [-h] [--exploit EXPLOIT]

optional arguments:
  -h, --help         show this help message and exit
  --exploit EXPLOIT  mysql, postgresql, fastcgi, redis, smtp, zabbix,
                     pymemcache, rbmemcache, phpmemcache, dmpmemcache


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
username:password

site_admin@nagini.hogwarts


        public $dbtype = 'mysqli';
        public $host = 'localhost';
        public $user = 'goblin';
        public $password = '';
        public $db = 'joomla';
        public $dbprefix = 'joomla_';
        public $live_site = '';
        public $secret = 'ILhwP6HTYKcN7qMh';

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