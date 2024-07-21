# BOX NAME: Torment

LINK:  https://www.vulnhub.com/entry/digitalworldlocal-torment,299/[](https://www.vulnhub.com/entry/kioptrix-2014-5,62/)

### **IP=192.168.56.117**

**URL=http://digitalworld.local**

# Remote Enumeration & Scan-outputs:

### <ins>Host Discovery</ins>

```
Host is up (0.0012s latency).
MAC Address: 08:00:27:66:1B:58 (Oracle VirtualBox virtual NIC)
Nmap scan report for digitalworld.local (192.168.56.117)
```

### <ins>Nmap scan</ins>

```
└─# nmap -n -sS -sV -sC $IP                                              
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-22 11:42 EST
Stats: 0:00:00 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 7.69% done; ETC: 11:42 (0:00:00 remaining)
Nmap scan report for 192.168.56.117
Host is up (0.000092s latency).
Not shown: 987 closed tcp ports (reset)
PORT     STATE SERVICE     VERSION
21/tcp   open  ftp         vsftpd 2.0.8 or later
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--    1 ftp      ftp        112640 Dec 28  2018 alternatives.tar.0
| -rw-r--r--    1 ftp      ftp          4984 Dec 23  2018 alternatives.tar.1.gz
| -rw-r--r--    1 ftp      ftp         95760 Dec 28  2018 apt.extended_states.0
| -rw-r--r--    1 ftp      ftp         10513 Dec 27  2018 apt.extended_states.1.gz
| -rw-r--r--    1 ftp      ftp         10437 Dec 26  2018 apt.extended_states.2.gz
| -rw-r--r--    1 ftp      ftp           559 Dec 23  2018 dpkg.diversions.0
| -rw-r--r--    1 ftp      ftp           229 Dec 23  2018 dpkg.diversions.1.gz
| -rw-r--r--    1 ftp      ftp           229 Dec 23  2018 dpkg.diversions.2.gz
| -rw-r--r--    1 ftp      ftp           229 Dec 23  2018 dpkg.diversions.3.gz
| -rw-r--r--    1 ftp      ftp           229 Dec 23  2018 dpkg.diversions.4.gz
| -rw-r--r--    1 ftp      ftp           229 Dec 23  2018 dpkg.diversions.5.gz
| -rw-r--r--    1 ftp      ftp           229 Dec 23  2018 dpkg.diversions.6.gz
| -rw-r--r--    1 ftp      ftp           505 Dec 28  2018 dpkg.statoverride.0
| -rw-r--r--    1 ftp      ftp           295 Dec 28  2018 dpkg.statoverride.1.gz
| -rw-r--r--    1 ftp      ftp           295 Dec 28  2018 dpkg.statoverride.2.gz
| -rw-r--r--    1 ftp      ftp           295 Dec 28  2018 dpkg.statoverride.3.gz
| -rw-r--r--    1 ftp      ftp           295 Dec 28  2018 dpkg.statoverride.4.gz
| -rw-r--r--    1 ftp      ftp           281 Dec 27  2018 dpkg.statoverride.5.gz
| -rw-r--r--    1 ftp      ftp           208 Dec 23  2018 dpkg.statoverride.6.gz
| -rw-r--r--    1 ftp      ftp       1719127 Jan 01  2019 dpkg.status.0
|_Only 20 shown. Use --script-args ftp-anon.maxlist=-1 to see all.
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.56.101
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp   open  ssh         OpenSSH 7.4p1 Debian 10+deb9u4 (protocol 2.0)
| ssh-hostkey: 
|   2048 84c7317a217d10d3a99c73c2c22dd677 (RSA)
|   256 a512e77ff017cef16aa5bc1f69ac1404 (ECDSA)
|_  256 66c7d0be8d9d9fbf7867d2bccc7d33b9 (ED25519)
25/tcp   open  smtp        Postfix smtpd
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=TORMENT
| Subject Alternative Name: DNS:TORMENT
| Not valid before: 2018-12-23T14:28:47
|_Not valid after:  2028-12-20T14:28:47
|_smtp-commands: TORMENT.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8
80/tcp   open  http        Apache httpd 2.4.25
|_http-server-header: Apache/2.4.25
|_http-title: Apache2 Debian Default Page: It works
111/tcp  open  rpcbind     2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100003  3,4         2049/udp   nfs
|   100003  3,4         2049/udp6  nfs
|   100005  1,2,3      43641/tcp6  mountd
|   100005  1,2,3      55785/tcp   mountd
|   100005  1,2,3      58474/udp   mountd
|   100005  1,2,3      59116/udp6  mountd
|   100021  1,3,4      34041/udp   nlockmgr
|   100021  1,3,4      34119/tcp   nlockmgr
|   100021  1,3,4      39729/tcp6  nlockmgr
|   100021  1,3,4      55174/udp6  nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
143/tcp  open  imap        Dovecot imapd
|_imap-capabilities: AUTH=PLAIN more LITERAL+ IDLE have Pre-login IMAP4rev1 LOGIN-REFERRALS listed ID capabilities post-login OK AUTH=LOGINA0001 SASL-IR ENABLE
445/tcp  open  netbios-ssn Samba smbd 4.5.12-Debian (workgroup: WORKGROUP)
631/tcp  open  ipp         CUPS 2.2
|_http-server-header: CUPS/2.2 IPP/2.1
| http-robots.txt: 1 disallowed entry 
|_/
|_http-title: Home - CUPS 2.2.1
| http-methods: 
|_  Potentially risky methods: PUT
2049/tcp open  nfs_acl     3 (RPC #100227)
6667/tcp open  irc         ngircd
6668/tcp open  irc         ngircd
6669/tcp open  irc         ngircd
MAC Address: 08:00:27:81:04:5D (Oracle VirtualBox virtual NIC)
Service Info: Hosts:  TORMENT.localdomain, TORMENT, irc.example.net; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_nbstat: NetBIOS name: TORMENT, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
|_clock-skew: mean: -1h40m02s, deviation: 4h37m07s, median: 59m57s
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.5.12-Debian)
|   Computer name: torment
|   NetBIOS computer name: TORMENT\x00
|   Domain name: \x00
|   FQDN: torment
|_  System time: 2023-01-23T01:42:48+08:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-01-22T17:42:49
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.26 seconds
```

```
└─# nmap -n -sS $IP --script=smb-enum-shares
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-22 12:24 EST
Nmap scan report for 192.168.56.117
Host is up (0.00031s latency).
Not shown: 987 closed tcp ports (reset)
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
25/tcp   open  smtp
80/tcp   open  http
111/tcp  open  rpcbind
139/tcp  open  netbios-ssn
143/tcp  open  imap
445/tcp  open  microsoft-ds
631/tcp  open  ipp
2049/tcp open  nfs
6667/tcp open  irc
6668/tcp open  irc
6669/tcp open  irc
MAC Address: 08:00:27:81:04:5D (Oracle VirtualBox virtual NIC)

Host script results:
| smb-enum-shares: 
|   note: ERROR: Enumerating shares failed, guessing at common ones (NT_STATUS_ACCESS_DENIED)
|   account_used: guest
|   \\192.168.56.117\BACKUP: 
|     warning: Couldn't get details for share: NT_STATUS_ACCESS_DENIED
|     Anonymous access: <none>
|     Current user access: <none>
|   \\192.168.56.117\IPC$: 
|     warning: Couldn't get details for share: NT_STATUS_ACCESS_DENIED
|     Anonymous access: <none>
|     Current user access: <none>
|   \\192.168.56.117\PRINT$: 
|     warning: Couldn't get details for share: NT_STATUS_ACCESS_DENIED
|     Anonymous access: <none>
|_    Current user access: <none>

Nmap done: 1 IP address (1 host up) scanned in 48.78 seconds
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

**Kernel Info:
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
[+]
```

# Credentials:

```
username:password

qiu:
root:
patrick:mostmachineshaveasupersecurekeyandalongpassphrase

ssh
patrik[id_rsa]:mostmachineshaveasupersecurekeyandalongpassphrase
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

==PROOFS==

==![5f6cef2b2961d10baafc43f1b391b5cb.png](../../_resources/5f6cef2b2961d10baafc43f1b391b5cb.png)==

# TAKEAWAYS

```
1.
2.
3.
```