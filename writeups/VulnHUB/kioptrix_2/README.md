# BOX NAME: Kioptrix 2

LINK: [https://www.vulnhub.com/entry/kioptrix-level-11-2,23/\[\](https://www.vulnhub.com/entry/kioptrix-2014-5,62/)](https://www.vulnhub.com/entry/kioptrix-level-11-2,23/%5B%5D%28https://www.vulnhub.com/entry/kioptrix-2014-5,62/%29 "https://www.vulnhub.com/entry/kioptrix-level-11-2,23/%5B%5D(https://www.vulnhub.com/entry/kioptrix-2014-5,62/)")

### **IP= 192.168.56.112**

**URL=http://192.168.56.112**

# Credentials:

username:password

# Hashes:

# Remote Enumeration & Scan-outputs:

### <ins>Host Discovery</ins>

```
└─# netdiscover -r 192.168.56.1/24 -i eth0 -L -N
 192.168.56.1    0a:00:27:00:00:0b      1      60  Unknown vendor
 192.168.56.100  08:00:27:8d:88:af      1      60  PCS Systemtechnik GmbH
 192.168.56.112  08:00:27:70:50:04      1      60  PCS Systemtechnik GmbH
```

### <ins>Nmap scan</ins>

```
└─# nmap -n -sS -sC -sV --version-all $IP -p-
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-14 13:25 EST
Nmap scan report for 192.168.56.112
Host is up (0.0011s latency).
Not shown: 65528 closed tcp ports (reset)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 3.9p1 (protocol 1.99)
|_sshv1: Server supports SSHv1
| ssh-hostkey: 
|   1024 8f3e8b1e5863fecf27a318093b52cf72 (RSA1)
|   1024 346b453dbacecab25355ef1e43703836 (DSA)
|_  1024 684d8cbbb65abd7971b87147ea004261 (RSA)
80/tcp   open  http     Apache httpd 2.0.52 ((CentOS))
|_http-server-header: Apache/2.0.52 (CentOS)
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
111/tcp  open  rpcbind  2 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2            111/tcp   rpcbind
|   100000  2            111/udp   rpcbind
|   100024  1            665/udp   status
|_  100024  1            668/tcp   status
443/tcp  open  ssl/http Apache httpd 2.0.52 ((CentOS))
|_http-title: Site doesn't have a title (text/html; charset=UTF-8).
| sslv2: 
|   SSLv2 supported
|   ciphers: 
|     SSL2_RC4_128_WITH_MD5
|     SSL2_RC4_128_EXPORT40_WITH_MD5
|     SSL2_RC4_64_WITH_MD5
|     SSL2_RC2_128_CBC_WITH_MD5
|     SSL2_RC2_128_CBC_EXPORT40_WITH_MD5
|     SSL2_DES_192_EDE3_CBC_WITH_MD5
|_    SSL2_DES_64_CBC_WITH_MD5
| ssl-cert: Subject: commonName=localhost.localdomain/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--
| Not valid before: 2009-10-08T00:10:47
|_Not valid after:  2010-10-08T00:10:47
|_http-server-header: Apache/2.0.52 (CentOS)
|_ssl-date: 2023-01-14T23:25:56+00:00; +4h59m58s from scanner time.
631/tcp  open  ipp      CUPS 1.1
|_http-title: 403 Forbidden
| http-methods: 
|_  Potentially risky methods: PUT
|_http-server-header: CUPS/1.1
668/tcp  open  status   1 (RPC #100024)
3306/tcp open  mysql    MySQL (unauthorized)
MAC Address: 08:00:27:70:50:04 (Oracle VirtualBox virtual NIC)

Host script results:
|_clock-skew: 4h59m57s
```

### <ins>Nikto scan</ins>

```
[+]
```

### <ins>Whatweb scan</ins>

```
[+]
```

# Hosts and computers:

### **HOSTS:**

\*\*FQDN: \*\*  
\*\*COMPUTER NAME: \*\*  
**OS:**

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
\*\**"file /bin/bash | lsb_release -a | uname -a"*

```
[+]
```

# Exploits and Payloads:

```
[+] Sock_sendpage()

The sock_sendpage() vulnerability is a security issue that affects certain versions of the Linux operating system. The vulnerability allows a local attacker to gain elevated privileges on a vulnerable system by sending a specially crafted message to the kernel.
The vulnerability exists in the way that the Linux kernel's networking subsystem handles certain types of messages, called "page fragments." These messages are used to transmit large amounts of data over a network, and they can contain multiple pages of memory. The vulnerability lies in the fact that the kernel does not properly check the size of these page fragments, which allows an attacker to send a message that is larger than it should be.
The vulnerability can be exploited by a local attacker with a low privilege account to gain root or kernel level access.
It is recommended to update the kernel version to a version that has the fix for this vulnerability.
```

# Writeup:

==REPORT==

```
Started with ...
```

==PROOF==

==![68a5a69e3d41a5c9e9d25808b50a4e17.png](../../_resources/68a5a69e3d41a5c9e9d25808b50a4e17.png)==