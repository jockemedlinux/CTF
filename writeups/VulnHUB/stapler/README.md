# BOX NAME: stapler
**LINK**: https://www.vulnhub.com/entry/stapler-1,150/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate box - PULL HAIR! this box was so sneaky..
2. bruteforce logins on usernames found via enum4linux
3. find passwd in history-file
4. become root via sudo
5. profit.

My god, this box was so sneaky. There's an internal script that configures a webroot at "/var/www/https" on a port that doesnt show up on nmap.
You can't curl it with a normal user and there's nothing indicating that its running https from outside the box.
I figured when I saw the wordpress-backup and that the localhost webserv running as root was the way to root but i couldn't figure it out until I was actually on the box.

This box was hella fun and quite tricky with all the custom settings. Hats off to g0tm1lk!
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.78
[+] URL:	http://stapler.com
[+]	URL:	https://10.77.0.78:12380/
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -p- $IP -oN nmap-stapler.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-07 09:34 CEST
Nmap scan report for stapler.com (10.77.0.78)
Host is up (0.0012s latency).
Not shown: 65523 filtered tcp ports (no-response)
PORT      STATE  SERVICE     VERSION
20/tcp    closed ftp-data
21/tcp    open   ftp         vsftpd 2.0.8 or later
22/tcp    open   ssh         OpenSSH 7.2p2 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
53/tcp    open   domain      dnsmasq 2.75
80/tcp    open   http        PHP cli server 5.5 or later
123/tcp   closed ntp
137/tcp   closed netbios-ns
138/tcp   closed netbios-dgm
139/tcp   open   netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
666/tcp   open   doom?
3306/tcp  open   mysql       MySQL 5.7.12-0ubuntu1
12380/tcp open   http        Apache httpd 2.4.18 ((Ubuntu))
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port666-TCP:V=7.93%I=7%D=6/7%Time=64803387%P=x86_64-pc-linux-gnu%r(NULL
SF:,2D58,"PK\x03\x04\x14\0\x02\0\x08\0d\x80\xc3Hp\xdf\x15\x81\xaa,\0\0\x15
SF:2\0\0\x0c\0\x1c\0message2\.jpgUT\t\0\x03\+\x9cQWJ\x9cQWux\x0b\0\x01\x04
SF:\xf5\x01\0\0\x04\x14\0\0\0\xadz\x0bT\x13\xe7\xbe\xefP\x94\x88\x88A@\xa2
SF:\x20\x19\xabUT\xc4T\x11\xa9\x102>\x8a\xd4RDK\x15\x85Jj\xa9\"DL\[E\xa2\x
SF:0c\x19\x140<\xc4\xb4\xb5\xca\xaen\x89\x8a\x8aV\x11\x91W\xc5H\x20\x0f\xb
SF:2\xf7\xb6\x88\n\x82@%\x99d\xb7\xc8#;3\[\r_\xcddr\x87\xbd\xcf9\xf7\xaeu\
SF:xeeY\xeb\xdc\xb3oX\xacY\xf92\xf3e\xfe\xdf\xff\xff\xff=2\x9f\xf3\x99\xd3
SF:\x08y}\xb8a\xe3\x06\xc8\xc5\x05\x82>`\xfe\x20\xa7\x05:\xb4y\xaf\xf8\xa0
SF:\xf8\xc0\^\xf1\x97sC\x97\xbd\x0b\xbd\xb7nc\xdc\xa4I\xd0\xc4\+j\xce\[\x8
SF:7\xa0\xe5\x1b\xf7\xcc=,\xce\x9a\xbb\xeb\xeb\xdds\xbf\xde\xbd\xeb\x8b\xf
SF:4\xfdis\x0f\xeeM\?\xb0\xf4\x1f\xa3\xcceY\xfb\xbe\x98\x9b\xb6\xfb\xe0\xd
SF:c\]sS\xc5bQ\xfa\xee\xb7\xe7\xbc\x05AoA\x93\xfe9\xd3\x82\x7f\xcc\xe4\xd5
SF:\x1dx\xa2O\x0e\xdd\x994\x9c\xe7\xfe\x871\xb0N\xea\x1c\x80\xd63w\xf1\xaf
SF:\xbd&&q\xf9\x97'i\x85fL\x81\xe2\\\xf6\xb9\xba\xcc\x80\xde\x9a\xe1\xe2:\
SF:xc3\xc5\xa9\x85`\x08r\x99\xfc\xcf\x13\xa0\x7f{\xb9\xbc\xe5:i\xb2\x1bk\x
SF:8a\xfbT\x0f\xe6\x84\x06/\xe8-\x17W\xd7\xb7&\xb9N\x9e<\xb1\\\.\xb9\xcc\x
SF:e7\xd0\xa4\x19\x93\xbd\xdf\^\xbe\xd6\xcdg\xcb\.\xd6\xbc\xaf\|W\x1c\xfd\
SF:xf6\xe2\x94\xf9\xebj\xdbf~\xfc\x98x'\xf4\xf3\xaf\x8f\xb9O\xf5\xe3\xcc\x
SF:9a\xed\xbf`a\xd0\xa2\xc5KV\x86\xad\n\x7fou\xc4\xfa\xf7\xa37\xc4\|\xb0\x
SF:f1\xc3\x84O\xb6nK\xdc\xbe#\)\xf5\x8b\xdd{\xd2\xf6\xa6g\x1c8\x98u\(\[r\x
SF:f8H~A\xe1qYQq\xc9w\xa7\xbe\?}\xa6\xfc\x0f\?\x9c\xbdTy\xf9\xca\xd5\xaak\
SF:xd7\x7f\xbcSW\xdf\xd0\xd8\xf4\xd3\xddf\xb5F\xabk\xd7\xff\xe9\xcf\x7fy\x
SF:d2\xd5\xfd\xb4\xa7\xf7Y_\?n2\xff\xf5\xd7\xdf\x86\^\x0c\x8f\x90\x7f\x7f\
SF:xf9\xea\xb5m\x1c\xfc\xfef\"\.\x17\xc8\xf5\?B\xff\xbf\xc6\xc5,\x82\xcb\[
SF:\x93&\xb9NbM\xc4\xe5\xf2V\xf6\xc4\t3&M~{\xb9\x9b\xf7\xda-\xac\]_\xf9\xc
SF:c\[qt\x8a\xef\xbao/\xd6\xb6\xb9\xcf\x0f\xfd\x98\x98\xf9\xf9\xd7\x8f\xa7
SF:\xfa\xbd\xb3\x12_@N\x84\xf6\x8f\xc8\xfe{\x81\x1d\xfb\x1fE\xf6\x1f\x81\x
SF:fd\xef\xb8\xfa\xa1i\xae\.L\xf2\\g@\x08D\xbb\xbfp\xb5\xd4\xf4Ym\x0bI\x96
SF:\x1e\xcb\x879-a\)T\x02\xc8\$\x14k\x08\xae\xfcZ\x90\xe6E\xcb<C\xcap\x8f\
SF:xd0\x8f\x9fu\x01\x8dvT\xf0'\x9b\xe4ST%\x9f5\x95\xab\rSWb\xecN\xfb&\xf4\
SF:xed\xe3v\x13O\xb73A#\xf0,\xd5\xc2\^\xe8\xfc\xc0\xa7\xaf\xab4\xcfC\xcd\x
SF:88\x8e}\xac\x15\xf6~\xc4R\x8e`wT\x96\xa8KT\x1cam\xdb\x99f\xfb\n\xbc\xbc
SF:L}AJ\xe5H\x912\x88\(O\0k\xc9\xa9\x1a\x93\xb8\x84\x8fdN\xbf\x17\xf5\xf0\
SF:.npy\.9\x04\xcf\x14\x1d\x89Rr9\xe4\xd2\xae\x91#\xfbOg\xed\xf6\x15\x04\x
SF:f6~\xf1\]V\xdcBGu\xeb\xaa=\x8e\xef\xa4HU\x1e\x8f\x9f\x9bI\xf4\xb6GTQ\xf
SF:3\xe9\xe5\x8e\x0b\x14L\xb2\xda\x92\x12\xf3\x95\xa2\x1c\xb3\x13\*P\x11\?
SF:\xfb\xf3\xda\xcaDfv\x89`\xa9\xe4k\xc4S\x0e\xd6P0");
Service Info: Host: RED; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 120.61 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
http://stapler.com [404 Not Found] Country[RESERVED][ZZ], HTML5, IP[10.77.0.78], Title[404 Not Found]
```

nikto-scan
```
└─$ nikto -h $IP | tee nikto-stapler.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.78
+ Target Hostname:    10.77.0.78
+ Target Port:        80
+ Start Time:         2023-06-07 09:34:52 (GMT2)
---------------------------------------------------------------------------
+ Server: No banner retrieved
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /.bashrc: User home dir was found with a shell rc file. This may reveal file and path information.
+ /.profile: User home dir with a shell profile was found. May reveal directory information and system configuration.
+ 8110 requests: 9 error(s) and 4 item(s) reported on remote host
+ End Time:           2023-06-07 09:35:07 (GMT2) (15 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing
```
.bashrc                 [Status: 200, Size: 3771, Words: 522, Lines: 118, Duration: 15ms]
.bash_logout            [Status: 200, Size: 220, Words: 35, Lines: 8, Duration: 18ms]
.profile                [Status: 200, Size: 675, Words: 107, Lines: 23, Duration: 22ms]
:: Progress: [37050/37050] :: Job [1/1] :: 1285 req/sec :: Duration: [0:00:23] :: Errors: 1 ::
```
other
```
Password Complexity: Disabled                                                                                       
Minimum Password Length: 5

[+] Password Info for Domain: RED

        [+] Minimum password length: 5
        [+] Password history length: None
        [+] Maximum password age: Not Set
        [+] Password Complexity Flags: 000000

                [+] Domain Refuse Password Change: 0
                [+] Domain Password Store Cleartext: 0
                [+] Domain Password Lockout Admins: 0
                [+] Domain Password No Clear Change: 0
                [+] Domain Password No Anon Change: 0
                [+] Domain Password Complex: 0

        [+] Minimum password age: None
        [+] Reset Account Lockout Counter: 30 minutes 
        [+] Locked Account Duration: 30 minutes 
        [+] Account Lockout Threshold: None
        [+] Forced Log off Time: Not Set

```

</details>

<details><summary><ins>SERVICES</ins></summary>

FTP
```
anonymous:anonymous
[21][ftp] host: 10.77.0.78   login: JBare   password: cookie
works on FTP also.
[21][ftp] host: 10.77.0.78   login: MFrei   password: letmein

```

SSH
```

```

SNMP
```

```

DNS
```
dnsmasq service running. dns-bruteforce. vhost or sub-domain?

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
1. Collect usernames
2. Bruteforce ssh,ftp,mysql
3. Enumerate SMB to get users
4. profit.
```
</details>

# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
JBare@red:/var/www/https$ ls /var/mail
root  www-data

JBare@red:/var/www/https$ ll /usr/local/src/nc.sh
-rwxr-xr-x 1 root root 99 Jun  3  2016 /usr/local/src/nc.sh*

/bin/bash /root/python.sh
/bin/bash /root/python.sh
```

**SUID's**:

```
JBare@red:/var/www/https$ find / -perm -u=s -type f 2>/dev/null
/usr/bin/newuidmap
/usr/bin/chsh
/usr/bin/sudo
/usr/bin/chfn
/usr/bin/pkexec
/usr/bin/newgidmap
/usr/bin/at
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/gpasswd
/usr/bin/ubuntu-core-launcher
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device                                                                                                   
/usr/lib/policykit-1/polkit-agent-helper-1                                                                                          
/usr/lib/i386-linux-gnu/lxc/lxc-user-nic                                                                                            
/usr/lib/dbus-1.0/dbus-daemon-launch-helper                                                                                         
/usr/lib/authbind/helper                                                                                                            
/bin/mount                                                                                                                          
/bin/umount                                                                                                                         
/bin/ping                                                                                                                           
/bin/fusermount
/bin/ping6
/bin/su
```
**SGID's**:

```
/usr/bin/expiry
/usr/bin/at
/usr/bin/ssh-agent
/usr/bin/chage
/usr/bin/wall
/usr/bin/crontab
/usr/bin/screen
/usr/lib/i386-linux-gnu/utempter/utempter
/usr/sbin/postqueue
/usr/sbin/postdrop
/sbin/unix_chkpwd
/sbin/pam_extrausers_chkpwd
```
**OTHERS**:

```
sshpass -p thisimypassword ssh JKanode@localhost
apt-get install sshpass
sshpass -p JZQuyIN5 peter@localhost
```
</details>


# LOOT

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*
```
/bin/bash: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=9ea3f9e5a889dd9eb671c7507bf87bc6962db4b2, stripped
 

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 16.04 LTS
Release:        16.04
Codename:       xenial


Linux red.initech 4.4.0-21-generic #37-Ubuntu SMP Mon Apr 18 18:34:49 UTC 2016 i686 i686 i686 GNU/Linux

```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
JBare:cookie
Mfrei:letmein

define('DB_USER', 'root');
define('DB_PASSWORD', 'plbkac');

Wordpress:
-> John:$P$B7889EMq/erHIuZapMB8GEizebcIy9.:incorrect
-> garry:$P$BzjfKAHd6N4cHKiugLX.4aLes8PxnZ1:football
-> harry:$P$BqV.SQ6OtKhVV7k7h1wqESkMh41buR0:monkey
-> scott:$P$BFmSPiDX1fChKRsytp1yp8Jo7RdHeI1:cookie
-> kathy:$P$BZlxAMnC6ON.PYaurLGrhfBi6TjtcA0:coolgirl
-> barry:$P$BIp1ND3G70AnRAkRY41vpVypsTfZhk0:washere
```
```
+-----------+------------------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--------------+------------+-----------------------+------------------+--------------+-----------------+------------------+------------------+----------------+---------------------+--------------------+------------------+------------+--------------+------------------------+----------+------------+-------------+--------------+---------------+-------------+-----------------+----------------------+-----------------------+-------------------------------------------+------------------+-----------------------+-------------------+----------------+
| Host      | User             | Select_priv | Insert_priv | Update_priv | Delete_priv | Create_priv | Drop_priv | Reload_priv | Shutdown_priv | Process_priv | File_priv | Grant_priv | References_priv | Index_priv | Alter_priv | Show_db_priv | Super_priv | Create_tmp_table_priv | Lock_tables_priv | Execute_priv | Repl_slave_priv | Repl_client_priv | Create_view_priv | Show_view_priv | Create_routine_priv | Alter_routine_priv | Create_user_priv | Event_priv | Trigger_priv | Create_tablespace_priv | ssl_type | ssl_cipher | x509_issuer | x509_subject | max_questions | max_updates | max_connections | max_user_connections | plugin                | authentication_string                     | password_expired | password_last_changed | password_lifetime | account_locked |
+-----------+------------------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--------------+------------+-----------------------+------------------+--------------+-----------------+------------------+------------------+----------------+---------------------+--------------------+------------------+------------+--------------+------------------------+----------+------------+-------------+--------------+---------------+-------------+-----------------+----------------------+-----------------------+-------------------------------------------+------------------+-----------------------+-------------------+----------------+
| localhost | root             | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                | Y          | Y            | Y                      |          |            |             |              |             0 |           0 |               0 |                    0 | mysql_native_password | *9B2DDC0D01126C483D173FB2A0ED14FFEC2B45AA | N                | 2016-06-03 14:17:55   |              NULL | N              |
| localhost | mysql.sys        | N           | N           | N           | N           | N           | N         | N           | N             | N            | N         | N          | N               | N          | N          | N            | N          | N                     | N                | N            | N               | N                | N                | N              | N                   | N                  | N                | N          | N            | N                      |          |            |             |              |             0 |           0 |               0 |                    0 | mysql_native_password | *THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE | N                | 2016-06-03 14:17:54   |              NULL | Y              |
| localhost | debian-sys-maint | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                | Y          | Y            | Y                      |          |            |             |              |             0 |           0 |               0 |                    0 | mysql_native_password | *DA79B10C207695571B8B72309996531AC6504291 | N                | 2016-06-03 14:17:55   |              NULL | N              |
| localhost | phpmyadmin       | N           | N           | N           | N           | N           | N         | N           | N             | N            | N         | N          | N               | N          | N          | N            | N          | N                     | N                | N            | N               | N                | N                | N              | N                   | N                  | N                | N          | N            | N                      |          |            |             |              |             0 |           0 |               0 |                    0 | mysql_native_password | *5153994ADAD440E919F0FD79B30131EB30A54CBB | N                | 2016-06-04 00:02:01   |              NULL | N              |
| %         | root             | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                | Y          | Y            | Y                      |          |            |             |              |             0 |           0 |               0 |                    0 | mysql_native_password | *9B2DDC0D01126C483D173FB2A0ED14FFEC2B45AA | N                | 2016-06-03 15:17:41   |              NULL | N              |
5 rows in set (0.00 sec) 

mysql> select * from message;
+--------------------------------------------------------------------------+
| text                                                                     |
+--------------------------------------------------------------------------+
| Vicki, You really need to sort out this database when you get the chance |



mysql> mysql> select * from wp_users;
+----+------------+------------------------------------+---------------+-----------------------+------------------+---------------------+---------------------+-------------+-----------------+
| ID | user_login | user_pass                          | user_nicename | user_email            | user_url         | user_registered     | user_activation_key | user_status | display_name    |
+----+------------+------------------------------------+---------------+-----------------------+------------------+---------------------+---------------------+-------------+-----------------+
|  1 | John       | $P$B7889EMq/erHIuZapMB8GEizebcIy9. | john          | john@red.localhost    | http://localhost | 2016-06-03 23:18:47 |                     |           0 | John Smith      |                                         
|  2 | Elly       | $P$BlumbJRRBit7y50Y17.UPJ/xEgv4my0 | elly          | Elly@red.localhost    |                  | 2016-06-05 16:11:33 |                     |           0 | Elly Jones      |                                         
|  3 | Peter      | $P$BTzoYuAFiBA5ixX2njL0XcLzu67sGD0 | peter         | peter@red.localhost   |                  | 2016-06-05 16:13:16 |                     |           0 | Peter Parker    |                                         
|  4 | barry      | $P$BIp1ND3G70AnRAkRY41vpVypsTfZhk0 | barry         | barry@red.localhost   |                  | 2016-06-05 16:14:26 |                     |           0 | Barry Atkins    |                                                                                                                      
|  5 | heather    | $P$Bwd0VpK8hX4aN.rZ14WDdhEIGeJgf10 | heather       | heather@red.localhost |                  | 2016-06-05 16:18:04 |                     |           0 | Heather Neville |                                                                                                                      
|  6 | garry      | $P$BzjfKAHd6N4cHKiugLX.4aLes8PxnZ1 | garry         | garry@red.localhost   |                  | 2016-06-05 16:18:23 |                     |           0 | garry           |                                                                                                                      
|  7 | harry      | $P$BqV.SQ6OtKhVV7k7h1wqESkMh41buR0 | harry         | harry@red.localhost   |                  | 2016-06-05 16:18:41 |                     |           0 | harry           |                                                                                                                      
|  8 | scott      | $P$BFmSPiDX1fChKRsytp1yp8Jo7RdHeI1 | scott         | scott@red.localhost   |                  | 2016-06-05 16:18:59 |                     |           0 | scott           |                                                                                                                      
|  9 | kathy      | $P$BZlxAMnC6ON.PYaurLGrhfBi6TjtcA0 | kathy         | kathy@red.localhost   |                  | 2016-06-05 16:19:14 |                     |           0 | kathy           |                                                                                                                      
| 10 | tim        | $P$BXDR7dLIJczwfuExJdpQqRsNf.9ueN0 | tim           | tim@red.localhost     |                  | 2016-06-05 16:19:29 |                     |           0 | tim             |                                                                                                                      
| 11 | ZOE        | $P$B.gMMKRP11QOdT5m1s9mstAUEDjagu1 | zoe           | zoe@red.localhost     |                  | 2016-06-05 16:19:50 |                     |           0 | ZOE             |                                                                                                                      
| 12 | Dave       | $P$Bl7/V9Lqvu37jJT.6t4KWmY.v907Hy. | dave          | dave@red.localhost    |                  | 2016-06-05 16:20:09 |                     |           0 | Dave            |                                                                                                                      
| 13 | Simon      | $P$BLxdiNNRP008kOQ.jE44CjSK/7tEcz0 | simon         | simon@red.localhost   |                  | 2016-06-05 16:20:35 |                     |           0 | Simon           |                                                                                                                      
| 14 | Abby       | $P$ByZg5mTBpKiLZ5KxhhRe/uqR.48ofs. | abby          | abby@red.localhost    |                  | 2016-06-05 16:20:53 |                     |           0 | Abby            |                                                                                                                      
| 15 | Vicki      | $P$B85lqQ1Wwl2SqcPOuKDvxaSwodTY131 | vicki         | vicki@red.localhost   |                  | 2016-06-05 16:21:14 |                     |           0 | Vicki           |                                                                                                                      
| 16 | Pam        | $P$BuLagypsIJdEuzMkf20XyS5bRm00dQ0 | pam           | pam@red.localhost     |                  | 2016-06-05 16:42:23 |                     |           0 | Pam             |                                                                                                                      
+----+------------+------------------------------------+---------------+-----------------------+------------------+---------------------+---------------------+-------------+-----------------+  
``` 

</details>

<details><summary><ins>HASHES:</ins></summary>

```
9B2DDC0D01126C483D173FB2A0ED14FFEC2B45AA
THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE
DA79B10C207695571B8B72309996531AC6504291
5153994ADAD440E919F0FD79B30131EB30A54CBB
9B2DDC0D01126C483D173FB2A0ED14FFEC2B45AA
```
</details>

# PROOFS

<details><summary><ins>Proofs</ins></summary>

Final payload:
```
su peter $PASS
sudo su -> root
```
		
```
fix-wordpress.sh  flag.txt  issue  python.sh  wordpress.sql
➜  ~ cat flag.txt
~~~~~~~~~~<(Congratulations)>~~~~~~~~~~
                          .-'''''-.
                          |'-----'|
                          |-.....-|
                          |       |
                          |       |
         _,._             |       |
    __.o`   o`"-.         |       |
 .-O o `"-.o   O )_,._    |       |
( o   O  o )--.-"`O   o"-.`'-----'`
 '--------'  (   o  O    o)  
              `----------`
b6b545dc11b7a270f4bad23432190c75162c4a2b

```

</details>