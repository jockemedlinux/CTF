# BOX NAME: Covfefe

LINK: [https://www.vulnhub.com/entry/covfefe-1,199/\[\](https://www.vulnhub.com/entry/kioptrix-2014-5,62/)](https://www.vulnhub.com/entry/covfefe-1,199/%5B%5D%28https://www.vulnhub.com/entry/kioptrix-2014-5,62/%29 "https://www.vulnhub.com/entry/covfefe-1,199/%5B%5D(https://www.vulnhub.com/entry/kioptrix-2014-5,62/)")

### **IP=10.77.0.36**

**URL=http://10.77.0.36**

# Remote Enumeration & Scan-outputs:

### <ins>Host Discovery</ins>

```
[+]
```

### <ins>Nmap scan</ins>

```
└─$ nmap $IP                           
Starting Nmap 7.93 ( https://nmap.org ) at 2023-03-26 21:48 CEST
Nmap scan report for 10.77.0.36
Host is up (0.00016s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
31337/tcp open  Elite
```

### <ins>Nikto scan</ins>

```
[+]
```

### <ins>Whatweb scan</ins>

```
[+]
```

# Fuzz

`ffuf -w /base/wordlists/web-fuzz/raft-large-directories.txt -u $URL/FUZZ/`  
`ffuf -w /base/wordlists/web-fuzz/raft-large-files.txt -u $URL/FUZZ -recursion -mc 200,301,403`  
`ffuf -w path/to/param_names.txt -u https://target/script.php?FUZZ=test_value -fs 4242`

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

# Local Filesystem Findings:

### **FILES OF INTEREST**

```
[+]
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

\*\*Kernel Info:  
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
[+]
```

# Credentials:

```
username:password

simon:starwars (ssh-key)
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
[+]
```

# Writeup:

```
Started with ...
```

# \*\*PROOFS\*\* 

SimonAAAAAAAAAAAAAAA/bin/sh

flag1{make_america_great_again}  
flag2{use_the_source_luke}  
flag3{das_bof_meister}