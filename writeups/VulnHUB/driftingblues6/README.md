# BOX NAME: DriftingBlues 6
**LINK**: https://www.vulnhub.com/entry/driftingblues-6,672/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. enumerate web til' you find a zip file you need to crack to grab login-credentials.
2. Try some know exploits for authenticated RCE on the box but since the redirect is messed up they won't work unless you patch them or the webserver, which is possible.
3. Get a reverse-shell on the box and start enumerating. No users, no special files, no nothing. There is a get.zip file /var/ which I copied to the webservers files dir, downloaded, and viewed. It's a backup of the textpattern CMS. So I thought there would be a backup-script running. But nada. Kernel?
4. Find the right kernel-exploit and fart a fire.

Quite an easy box but I spent quite some time to "patch" the know RCE-exploits. Eventually I just ended up uploading a PHP-reverse shell, stabalizing it, and executing DirtyCow (CVE 2016–5195) to get root. 
Great stuff!
```
</details>
# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.53
[+] URL:	http://driftingblues.box
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ whatweb $URL --log-verbose=whatweb-db6.log
http://driftingblues.box [200 OK] Apache[2.2.22], Country[RESERVED][ZZ], HTML5, HTTPServer[Debian Linux][Apache/2.2.22 (Debian)], IP[10.77.0.53], Title[driftingblues]
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
└─$ whatweb $URL --log-verbose=whatweb-db6.log
http://driftingblues.box [200 OK] Apache[2.2.22], Country[RESERVED][ZZ], HTML5, HTTPServer[Debian Linux][Apache/2.2.22 (Debian)], IP[10.77.0.53], Title[driftingblues]
```

nikto-scan

```
└─$ nikto -h $IP | tee nikto-db6.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.53
+ Target Hostname:    10.77.0.53
+ Target Port:        80
+ Start Time:         2023-04-27 11:12:17 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.2.22 (Debian)
+ /: Server may leak inodes via ETags, header found with file /, inode: 14067, size: 750, mtime: Mon Mar 15 14:36:18 2021. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/
+ /textpattern/textpattern/: Retrieved x-powered-by header: PHP/5.5.38-1~dotdeb+7.1.
+ /textpattern/textpattern/: Cookie txp_test_cookie created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /robots.txt: Entry '/textpattern/textpattern/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: contains 1 entry which should be manually viewed. See: https://developer.mozilla.org/en-US/docs/Glossary/Robots.txt
+ /index: Uncommon header 'tcn' found, with contents: list.
+ /index: Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. The following alternatives for 'index' were found: index.html. See: http://www.wisec.it/sectou.php?id=4698ebdc59d1
+ Apache/2.2.22 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ OPTIONS: Allowed HTTP Methods: GET, HEAD, POST, OPTIONS .
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /#wp-config.php#: #wp-config.php# file found. This file contains the credentials.
+ 8910 requests: 0 error(s) and 13 item(s) reported on remote host
+ End Time:           2023-04-27 11:12:51 (GMT2) (34 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing

```
User-agent: *
Disallow: 	

dont forget to add .zip extension to your dir-brute
;)

```

```
└─$ ffuf -u $URL/FUZZ -w /base/wordlists/web-fuzz/directory-list-2.3-big.txt -recursion -s -mc 200 -e .zip | tee ffuf-dir-db4.log

/textpattern/textpattern  --> textpattern.version = '4.8.3';
db
index
robots
spammer
spammer.zip
zip2john spammer.zip > ziphash.txt
└─$ john ziphash.txt -w=/base/wordlists/password/rockyou.txt

```
other
```
Upload a reverse shell on the textpattern CMS and execute it here
http://driftingblues.box/textpattern/files/
```

</details>
<details><summary><ins>OTHER</ins></summary>

SSH (Port 22)
```

```

DNS (Port 53)
```

```

</details>


# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```

```

**SUID's**:

```
www-data@driftingblues:/$ find / -perm -u=s -type f 2>/dev/null
/usr/sbin/exim4
/usr/bin/chfn
/usr/bin/passwd
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/lib/eject/dmcrypt-get-device
/usr/lib/pt_chown
/usr/lib/openssh/ssh-keysign
/bin/ping
/bin/mount
/bin/umount
/bin/su
/bin/ping6
```
**SGID's**:

```
www-data@driftingblues:/$ find / -perm -g=s -type f 2>/dev/null
/usr/bin/bsd-write
/usr/bin/wall
/usr/bin/chage
/usr/bin/expiry
/usr/bin/crontab
/usr/bin/ssh-agent
/sbin/unix_chkpwd

```
**OTHERS**:

```
/var/www/textpattern/textpattern/config.php

$txpcfg['user'] = 'drifter';
$txpcfg['pass'] = 'imjustdrifting31';
$txpcfg['host'] = 'localhost';
```
</details>

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
Linux driftingblues 3.2.0-4-amd64 #1 SMP Debian 3.2.78-1 x86_64 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
spammer.zip : myspace4
mayer:lionheart


drifter:imjustdrifting31
```
```
+---------+-------+--------------------------------------------------------------+---------------+----------------------------+-------+---------------------+--------------
| user_id | name  | pass                                                         | RealName      | email                      | privs | last_access         | nonce        
+---------+-------+--------------------------------------------------------------+---------------+----------------------------+-------+---------------------+--------------
|       1 | mayer | $2y$10$vLuVi6USHmoVNQHioadI5OGONW1qXjqKxi4fVYAceKsAo5gzUPmeq | hakan tasiyan | hakanyasiyan@universal.com |     1 | 2023-04-27 05:06:32 | e227d8d7f6146
+---------+-------+--------------------------------------------------------------+---------------+----------------------------+-------+---------------------+--------------
1 row in set (0.00 sec) 
``` 
</details>

<details><summary><ins>EXPLOITS:</ins></summary>

```
Possible candidates:

Linux Kernel 2.6.22 < 3.9 (x86/x64) - 'Dirty COW /proc/self/mem' Race Condition P | linux/local/40616.c
Linux Kernel 2.6.22 < 3.9 - 'Dirty COW /proc/self/mem' Race Condition Privilege E | linux/local/40847.cpp
Linux Kernel 2.6.22 < 3.9 - 'Dirty COW PTRACE_POKEDATA' Race Condition (Write Acc | linux/local/40838.c
Linux Kernel 2.6.22 < 3.9 - 'Dirty COW' 'PTRACE_POKEDATA' Race Condition Privileg | linux/local/40839.c
Linux Kernel 2.6.22 < 3.9 - 'Dirty COW' /proc/self/mem Race Condition (Write Acce | linux/local/40611.c
```
</details>

# Proofs

<details><summary><ins>Proofs</ins></summary>

Final payload:
```
DirtyCow (CVE 2016–5195)
```
```
firefart@driftingblues:~# cat flag.txt

░░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄▄
░░░░░█░░░░░░░░░░░░░░░░░░▀▀▄
░░░░█░░░░░░░░░░░░░░░░░░░░░░█
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█
░▄▀░▄▄▄░░█▀▀▀▀▄▄█░░░██▄▄█░░░░█
█░░█░▄░▀▄▄▄▀░░░░░░░░█░░░░░░░░░█
█░░█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄░█
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
░░░█░░░░██░░▀█▄▄▄█▄▄█▄▄██▄░░█
░░░░█░░░░▀▀▄░█░░░█░█▀█▀█▀██░█
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
░░░░░░░▀▄▄░░░░░░░░░░░░░░░░░░░█
░░▐▌░█░░░░▀▀▄▄░░░░░░░░░░░░░░░█
░░░█▐▌░░░░░░█░▀▄▄▄▄▄░░░░░░░░█
░░███░░░░░▄▄█░▄▄░██▄▄▄▄▄▄▄▄▀
░▐████░░▄▀█▀█▄▄▄▄▄█▀▄▀▄
░░█░░▌░█░░░▀▄░█▀█░▄▀░░░█
░░█░░▌░█░░█░░█░░░█░░█░░█
░░█░░▀▀░░██░░█░░░█░░█░░█
░░░▀▀▄▄▀▀░█░░░▀▄▀▀▀▀█░░█

congratulations!


```
</details>