BOX NAME: Derp'N'Stink  
LINK: https://www.vulnhub.com/entry/derpnstink-1,221/

IP=192.168.0.172  
URL=http://192.168.0.172

# Credentials:

\[+\] admin:admin \[wordpress\]  
\[+\] root:mysql \[mysql\]  
\[+\] unclestinky:wedgie57  
\[+\] mrdep:derpderpderpderpderpderpderp

# Hashes:

\[+\] admin:$P$BgnU3VLAv.RWd3rdrkfVIuQr6mFvpd/  
\[+\] unclestinky:$P$BW6NTkFvboVVCHU2R9qmNai1WfHSC41  
\[+\] unclestinky:9b776afb479b31e8047026f1185e952dd1e530cb:wedgie57

# Remote Enumeration:

Host Discovery

```
# Nmap 7.93 scan initiated Thu Nov  3 19:29:16 2022 as: nmap -n -A -oN nmap.log 192.168.0.172
Nmap scan report for 192.168.0.172
Host is up (0.00044s latency).
Not shown: 997 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.2
22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 124ef86e7b6cc6d87cd82977d10beb72 (DSA)
|   2048 72c51c5f817bdd1afb2e5967fea6912f (RSA)
|   256 06770f4b960a3a2c3bf08c2b57b597bc (ECDSA)
|_  256 28e8ed7c607f196ce3247931caab5d2d (ED25519)
80/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
|_http-title: DeRPnStiNK
| http-robots.txt: 2 disallowed entries 
|_/php/ /temporary/
|_http-server-header: Apache/2.4.7 (Ubuntu)
MAC Address: 08:00:27:01:D7:93 (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.9
Network Distance: 1 hop
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE
HOP RTT     ADDRESS
1   0.44 ms 192.168.0.172

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Thu Nov  3 19:29:25 2022 -- 1 IP address (1 host up) scanned in 9.19 seconds

```

# Hosts and computers:

\[+\] HOSTS: http://derpnstink.local/weblog/  
\[+\] FQDN: derpnstink.local  
\[+\] COMPUTER NAME:  
\[+\] OS:

# Look at.

\[+\] FTP  
\[+\] SSH  
\[+\] HTTP

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

\[+\] gobuster dir http://$IP  
\[+\] gobuster vhost http://$IP

\[+\] Nikto --url http://$IP -C all

\[+\] ffuf -u '$URL/FUZZ' -w wordlist.txt -fs filtersize

# enum4linux:

\[+\] enum4linux -A $IP

# CMS:

\[+\] cmseek -u http://$IP --random-agent

\[+\] wpscan -u $IP

```
[i] It seems like you have not updated the database for some time.
[?] Do you want to update now? [Y]es [N]o, default: [N]N
[+] URL: http://derpnstink.local/weblog/ [192.168.0.172]
[+] Started: Thu Nov  3 19:53:47 2022

Interesting Finding(s):

[+] Headers
 | Interesting Entries:
 |  - Server: Apache/2.4.7 (Ubuntu)
 |  - X-Powered-By: PHP/5.5.9-1ubuntu4.22
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://derpnstink.local/weblog/xmlrpc.php
 | Found By: Headers (Passive Detection)
 | Confidence: 100%
 | Confirmed By:
 |  - Link Tag (Passive Detection), 30% confidence
 |  - Direct Access (Aggressive Detection), 100% confidence
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://derpnstink.local/weblog/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://derpnstink.local/weblog/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

Fingerprinting the version - Time: 00:00:01 <===============================================================================================> (676 / 676) 100.00% Time: 00:00:01
[i] The WordPress version could not be detected.

[+] WordPress theme in use: twentysixteen
 | Location: http://derpnstink.local/weblog/wp-content/themes/twentysixteen/
 | Last Updated: 2022-05-24T00:00:00.000Z
 | Readme: http://derpnstink.local/weblog/wp-content/themes/twentysixteen/readme.txt
 | [!] The version is out of date, the latest version is 2.7
 | Style URL: http://derpnstink.local/weblog/wp-content/themes/twentysixteen/style.css?ver=4.6.25
 | Style Name: Twenty Sixteen
 | Style URI: https://wordpress.org/themes/twentysixteen/
 | Description: Twenty Sixteen is a modernized take on an ever-popular WordPress layout — the horizontal masthead ...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.3 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://derpnstink.local/weblog/wp-content/themes/twentysixteen/style.css?ver=4.6.25, Match: 'Version: 1.3'

[+] Enumerating All Plugins (via Passive Methods)
[+] Checking Plugin Versions (via Passive and Aggressive Methods)

[i] Plugin(s) Identified:

[+] slideshow-gallery
 | Location: http://derpnstink.local/weblog/wp-content/plugins/slideshow-gallery/
 | Last Updated: 2022-09-12T19:05:00.000Z
 | [!] The version is out of date, the latest version is 1.7.5
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 1.4.6 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://derpnstink.local/weblog/wp-content/plugins/slideshow-gallery/readme.txt

[+] Enumerating Users (via Passive and Aggressive Methods)
 Brute Forcing Author IDs - Time: 00:00:00 <==================================================================================================> (10 / 10) 100.00% Time: 00:00:00

[i] User(s) Identified:

[+] admin
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Thu Nov  3 19:53:52 2022
[+] Requests Done: 1034
[+] Cached Requests: 12
[+] Data Sent: 297.53 KB
[+] Data Received: 6.203 MB
[+] Memory used: 230.074 MB
[+] Elapsed time: 00:00:04
```

\[+\] droopescan -u $IP

\[+\] joomscan -u $IP -ec

# Local Filesystem Findings:

\[+\] FILES OF INTEREST

```
wp-config.php
```

\[+\] SUID

```
/bin/mount
/bin/fusermount
/bin/su
/bin/ping6
/bin/umount
/bin/ping
/usr/bin/mtr
/usr/bin/sudo
/usr/bin/pkexec
/usr/bin/newgrp
/usr/bin/passwd
/usr/bin/lppasswd
/usr/bin/traceroute6.iputils
/usr/bin/gpasswd
/usr/bin/chsh
/usr/bin/chfn
/usr/sbin/uuidd
/usr/sbin/pppd
/usr/lib/i386-linux-gnu/oxide-qt/chrome-sandbox
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
```

\[+\] SGID

```
/etc/ppp/peers
/etc/chatscripts
/sbin/unix_chkpwd
/usr/local/lib/python3.4
/usr/local/lib/python3.4/dist-packages
/usr/local/lib/python2.7
/usr/local/lib/python2.7/site-packages
/usr/local/lib/python2.7/dist-packages
/usr/local/share/sgml
/usr/local/share/sgml/dtd
/usr/local/share/sgml/declaration
/usr/local/share/sgml/stylesheet
/usr/local/share/sgml/misc
/usr/local/share/sgml/entities
/usr/local/share/fonts
/usr/local/share/ca-certificates
/usr/local/share/xml
/usr/local/share/xml/declaration
/usr/local/share/xml/misc
/usr/local/share/xml/schema
/usr/local/share/xml/entities
/usr/bin/expiry
/usr/bin/ssh-agent
/usr/bin/chage
/usr/bin/mlocate
/usr/bin/crontab
/usr/bin/mail-unlock
/usr/bin/bsd-write
/usr/bin/dotlockfile
/usr/bin/mail-lock
/usr/bin/mail-touchlock
/usr/bin/wall
/usr/sbin/uuidd
/usr/lib/evolution/camel-lock-helper-1.2
/usr/lib/utempter/utempter
/usr/lib/libvte-2.90-9/gnome-pty-helper
/usr/share/ppd/custom
/var/log/mysql
/var/local
/var/cache/man
/var/cache/man/bs
/var/cache/man/bs/cat1
/var/cache/man/ug
/var/cache/man/ug/cat1
/var/cache/man/cat2
/var/cache/man/sr
/var/cache/man/sr/cat1
/var/cache/man/cat5
/var/cache/man/vi
/var/cache/man/vi/cat1
/var/cache/man/mhr
/var/cache/man/mhr/cat1
/var/cache/man/zh_CN
/var/cache/man/zh_CN/cat5
/var/cache/man/zh_CN/cat8
/var/cache/man/zh_CN/cat1
/var/cache/man/bo
/var/cache/man/bo/cat1
/var/cache/man/cat7
/var/cache/man/ca@valencia
/var/cache/man/ca@valencia/cat1
/var/cache/man/fr
/var/cache/man/fr/cat5
/var/cache/man/fr/cat7
/var/cache/man/fr/cat8
/var/cache/man/fr/cat1
/var/cache/man/eu
/var/cache/man/eu/cat1
/var/cache/man/hr
/var/cache/man/hr/cat1
/var/cache/man/tr
/var/cache/man/tr/cat5
/var/cache/man/tr/cat8
/var/cache/man/tr/cat1
/var/cache/man/cat8
/var/cache/man/sk
/var/cache/man/sk/cat1
/var/cache/man/eo
/var/cache/man/eo/cat1
/var/cache/man/nn
/var/cache/man/nn/cat1
/var/cache/man/uk
/var/cache/man/uk/cat1
/var/cache/man/he
/var/cache/man/he/cat1
/var/cache/man/sv
/var/cache/man/sv/cat5
/var/cache/man/sv/cat8
/var/cache/man/sv/cat1
/var/cache/man/it
/var/cache/man/it/cat5
/var/cache/man/it/cat8
/var/cache/man/it/cat1
/var/cache/man/my
/var/cache/man/my/cat1
/var/cache/man/pt_BR
/var/cache/man/pt_BR/cat5
/var/cache/man/pt_BR/cat8
/var/cache/man/pt_BR/cat1
/var/cache/man/hu
/var/cache/man/hu/cat5
/var/cache/man/hu/cat8
/var/cache/man/hu/cat1
/var/cache/man/th
/var/cache/man/th/cat1
/var/cache/man/ast
/var/cache/man/ast/cat1
/var/cache/man/kk
/var/cache/man/kk/cat1
/var/cache/man/el
/var/cache/man/el/cat1
/var/cache/man/zh_HK
/var/cache/man/zh_HK/cat1
/var/cache/man/cat4
/var/cache/man/nl
/var/cache/man/nl/cat5
/var/cache/man/nl/cat8
/var/cache/man/nl/cat1
/var/cache/man/nb
/var/cache/man/nb/cat1
/var/cache/man/io
/var/cache/man/io/cat1
/var/cache/man/es
/var/cache/man/es/cat5
/var/cache/man/es/cat8
/var/cache/man/es/cat1
/var/cache/man/bn
/var/cache/man/bn/cat1
/var/cache/man/ro
/var/cache/man/ro/cat1
/var/cache/man/cat3
/var/cache/man/cy
/var/cache/man/cy/cat1
/var/cache/man/en_AU
/var/cache/man/en_AU/cat1
/var/cache/man/ca
/var/cache/man/ca/cat1
/var/cache/man/ru
/var/cache/man/ru/cat5
/var/cache/man/ru/cat8
/var/cache/man/ru/cat1
/var/cache/man/da
/var/cache/man/da/cat5
/var/cache/man/da/cat8
/var/cache/man/da/cat1
/var/cache/man/zh_TW
/var/cache/man/zh_TW/cat5
/var/cache/man/zh_TW/cat8
/var/cache/man/zh_TW/cat1
/var/cache/man/lv
/var/cache/man/lv/cat1
/var/cache/man/ta
/var/cache/man/ta/cat1
/var/cache/man/fy
/var/cache/man/fy/cat1
/var/cache/man/fr.UTF-8
/var/cache/man/fr.UTF-8/cat7
/var/cache/man/fr.UTF-8/cat8
/var/cache/man/fo
/var/cache/man/fo/cat1
/var/cache/man/pa
/var/cache/man/pa/cat1
/var/cache/man/cs
/var/cache/man/cs/cat5
/var/cache/man/cs/cat7
/var/cache/man/cs/cat8
/var/cache/man/cs/cat1
/var/cache/man/ko
/var/cache/man/ko/cat5
/var/cache/man/ko/cat8
/var/cache/man/ko/cat1
/var/cache/man/en_GB
/var/cache/man/en_GB/cat1
/var/cache/man/ar
/var/cache/man/ar/cat1
/var/cache/man/ja
/var/cache/man/ja/cat5
/var/cache/man/ja/cat8
/var/cache/man/ja/cat1
/var/cache/man/si
/var/cache/man/si/cat1
/var/cache/man/uz
/var/cache/man/uz/cat1
/var/cache/man/oc
/var/cache/man/oc/cat1
/var/cache/man/pt
/var/cache/man/pt/cat5
/var/cache/man/pt/cat8
/var/cache/man/pt/cat1
/var/cache/man/se
/var/cache/man/se/cat1
/var/cache/man/fi
/var/cache/man/fi/cat1
/var/cache/man/gd
/var/cache/man/gd/cat1
/var/cache/man/cat1
/var/cache/man/fa
/var/cache/man/fa/cat1
/var/cache/man/ps
/var/cache/man/ps/cat1
/var/cache/man/ku
/var/cache/man/ku/cat1
/var/cache/man/sl
/var/cache/man/sl/cat8
/var/cache/man/sl/cat1
/var/cache/man/bg
/var/cache/man/bg/cat1
/var/cache/man/lt
/var/cache/man/lt/cat1
/var/cache/man/fr.ISO8859-1
/var/cache/man/fr.ISO8859-1/cat7
/var/cache/man/fr.ISO8859-1/cat8
/var/cache/man/ms
/var/cache/man/ms/cat1
/var/cache/man/shn
/var/cache/man/shn/cat1
/var/cache/man/cat6
/var/cache/man/gl
/var/cache/man/gl/cat1
/var/cache/man/pl
/var/cache/man/pl/cat5
/var/cache/man/pl/cat8
/var/cache/man/pl/cat1
/var/cache/man/te
/var/cache/man/te/cat1
/var/cache/man/km
/var/cache/man/km/cat1
/var/cache/man/hi
/var/cache/man/hi/cat1
/var/cache/man/de
/var/cache/man/de/cat5
/var/cache/man/de/cat7
/var/cache/man/de/cat8
/var/cache/man/de/cat3
/var/cache/man/de/cat1
/var/cache/man/ml
/var/cache/man/ml/cat1
/var/cache/man/en_CA
/var/cache/man/en_CA/cat1
/var/cache/man/be
/var/cache/man/be/cat1
/var/cache/man/et
/var/cache/man/et/cat1
/var/cache/man/sq
/var/cache/man/sq/cat1
/var/cache/man/id
/var/cache/man/id/cat5
/var/cache/man/id/cat8
/var/cache/man/id/cat1
/var/mail
/var/crash
/var/lib/libuuid
/var/metrics
```

\[+\] Dumps, outputs, other useful information

```
[+] flag1(52E37291AEDF6A46D7D0BB8A6312F4F9F1AA4975C248C3F0E008CBA09D6E9166)
[+] flag2(a7d355b26bda6bf1196ccffead0b2cf2b81f0a9de5b4876b44407f1dc07e51e6)
[+] flag3(07f62b021771d3cf67e2e1faf18769cc5e5c119ad7d4d1847a11e11d6d5a7ecb)
[+] flag4(49dca65f362fee401292ed7ada96f96295eab1e589c52e4e66bf4aedda715fdd)
```

# Kernel Info:

\[+\] file /bin/bash

```
/bin/bash: ELF 32-bit LSB  executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=4ead65aeca4e9f1eabf3a0d63eb1f96c225b25fd, stripped
```

\[+\] lsb_release -a

```
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 14.04.5 LTS
Release:        14.04
Codename:       trusty
```

\[+\] uname -a

```
Linux DeRPnStiNK 4.4.0-31-generic #50~14.04.1-Ubuntu SMP Wed Jul 13 01:06:37 UTC 2016 i686 i686 i686 GNU/Linux
```

# Exploits and Payloads:

\[+\] wpscan bruteforce credentials  
\[+\] use either metasplits slideshow upload or php/webapps/34681.py and gain shell  
\[+\] exploit wp-config to find more creds in mysql db  
\[+\] try to pivot user with new credentials. then ssh  
\[+\] copy private ssh-key and ssh in  
\[+\] found a .pcap file iin stinky's Documents-folder. Parse a password to mrderp. pivot to mrderp  
\[+\] mrderp can run sudo in /home/mrderp/binaries/derpy\* . create /bin/bash script, sudo ./derpy  
\[+\] $root

# Writeup:

==DIARY==

```
Started with ...
```

==PROOF==

```
flag4(49dca65f362fee401292ed7ada96f96295eab1e589c52e4e66bf4aedda715fdd)

Congrats on rooting my first VulnOS!

Hit me up on twitter and let me know your thoughts!

@securekomodo
```

==BACKDOOR==  
\[+\] changed rootpassword & changed sshd_config to permit passwordauthentication