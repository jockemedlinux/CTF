# BOX NAME: Brainpan 1 (TryHackMe)
**LINK**: https://tryhackme.com/room/brainpan

<details open><summary><ins>SUMMARY</ins></summary>

```
1. So this is a buffer overflow box on a linux machine. The steps to the overlow is shown below.
2. While on the box we leverage a SUID binary to open up a manual.
3. Break out of manual to give us a root shell!

Fun box. I was messing a lot with the checksrv.sh until I realized it wouldn't matter since it's only executed by the user "pucks" cronjob. So eventually I found the /usr/bin/validate SUID and from there managed to get root. Great stuff! :)
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.10.62.20
[+] URL:	N/A
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-brainpan5.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-29 10:39 CEST
Nmap scan report for 10.10.62.20
Host is up (0.053s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT      STATE SERVICE VERSION
9999/tcp  open  abyss?
| fingerprint-strings: 
|   NULL: 
|     _| _| 
|     _|_|_| _| _|_| _|_|_| _|_|_| _|_|_| _|_|_| _|_|_| 
|     _|_| _| _| _| _| _| _| _| _| _| _| _|
|     _|_|_| _| _|_|_| _| _| _| _|_|_| _|_|_| _| _|
|     [________________________ WELCOME TO BRAINPAN _________________________]
|_    ENTER THE PASSWORD
10000/tcp open  http    SimpleHTTPServer 0.6 (Python 2.7.3)
|_http-title: Site doesn't have a title (text/html).
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port9999-TCP:V=7.93%I=7%D=4/29%Time=644CD7B0%P=x86_64-pc-linux-gnu%r(NU
SF:LL,298,"_\|\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20_\|\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\n_\|_\|_\|\x20\x20\x20\x20_\|\x20\x20_\|_\|\x20\x20\x20\x20_\|_\|_\|
SF:\x20\x20\x20\x20\x20\x20_\|_\|_\|\x20\x20\x20\x20_\|_\|_\|\x20\x20\x20\
SF:x20\x20\x20_\|_\|_\|\x20\x20_\|_\|_\|\x20\x20\n_\|\x20\x20\x20\x20_\|\x
SF:20\x20_\|_\|\x20\x20\x20\x20\x20\x20_\|\x20\x20\x20\x20_\|\x20\x20_\|\x
SF:20\x20_\|\x20\x20\x20\x20_\|\x20\x20_\|\x20\x20\x20\x20_\|\x20\x20_\|\x
SF:20\x20\x20\x20_\|\x20\x20_\|\x20\x20\x20\x20_\|\n_\|\x20\x20\x20\x20_\|
SF:\x20\x20_\|\x20\x20\x20\x20\x20\x20\x20\x20_\|\x20\x20\x20\x20_\|\x20\x
SF:20_\|\x20\x20_\|\x20\x20\x20\x20_\|\x20\x20_\|\x20\x20\x20\x20_\|\x20\x
SF:20_\|\x20\x20\x20\x20_\|\x20\x20_\|\x20\x20\x20\x20_\|\n_\|_\|_\|\x20\x
SF:20\x20\x20_\|\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20_\|_\|_\|\x20\x20_
SF:\|\x20\x20_\|\x20\x20\x20\x20_\|\x20\x20_\|_\|_\|\x20\x20\x20\x20\x20\x
SF:20_\|_\|_\|\x20\x20_\|\x20\x20\x20\x20_\|\n\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20_\|\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\x20\x20\x20\x20\x20\x20\x2
SF:0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\
SF:x20\x20_\|\n\n\[________________________\x20WELCOME\x20TO\x20BRAINPAN\x
SF:20_________________________\]\n\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20ENTER\x
SF:20THE\x20PASSWORD\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x
SF:20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\n\n\
SF:x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
SF:\x20\x20\x20\x20\x20\x20\x20\x20>>\x20");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 40.79 seconds

```
```
└─$ sudo nmap -sV -O $IP -oN nmap-brainpan1-os.log
dont give us shit... well we know its a linux box so lets assume its x86
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```

```

nikto-scan

```

```

fuzzing

```
/bin/brainpan.exe
```
other

```

```
### Summary

```
So we download the brainpan.exe file and start testing it with our script.

1. Find the offset.
	By sending a cyclic pattern and crashing the program whilst running in Immunity debugger we can find the value of the EIP. And thus find the offset. which is at 524.
2. Control the EIP. 
	By sending exactly 524 A's and 4 B's we se the EIP return a 42424242 value, which hex-to-ascii gives BBBB. We control the EIP-
3. Find bad bytes.
	Once we control the EIP we can check if the program operates with some bad bytes. usually there's always a null-byte "\x00". But we can do this using mona-modules. which makes this process super-easy.
	3A) !mona bytearray -b "\x00" | which generates a bytearray we can compare our bad characters to later.
	3B) Once we've sent the bad characters we specify !mona compare -f bytearray.bin -a $ESP-ADDRESS.
	3C) Eliminate all the bad-bytes one by one to make sure there is not double-byte errors.
4. Find a return addres.
	For us to be able to execute shellcode on the machine we need to instruct the program to return to the top of the stack or to the controlled return-address of our choosing.  We can do this by entering !mona jmp -r esp -cpb "\x00" and specifyig all the bad bytes we found in step 3.
5. Generate malicious shellcode, add nops, and fire-away.
	We generate some malicous shellcode with the help of msfvenom. To do this correctly we need to know what kind of system we're dealing with. What can we do here? Well the only thing we can do for sure is to use NMAP and try to the best of its ability to predict the OS-version.

6. Profit?
```

</details>
<details><summary><ins>OTHER</ins></summary>


</details>


# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
"""" /usr/local/bin/validate """"
We can exploit this SUID binary to enter a manual page for say, wget, then breakout with to a root-shel..
```

**SUID's**:

```
/bin/umount
/bin/su
/bin/mount
/bin/fusermount
/bin/ping6
/bin/ping
/tmp/rootbash
/usr/bin/sudo
/usr/bin/mtr
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/sudoedit
/usr/bin/chfn
/usr/bin/traceroute6.iputils
/usr/bin/at
/usr/bin/lppasswd
/usr/bin/passwd
/usr/bin/gpasswd
/usr/sbin/uuidd
/usr/sbin/pppd
"""" /usr/local/bin/validate """"
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/pt_chown

```
**SGID's**:

```
puck@brainpan:/home/puck$ find / -perm -g=s -type f 2>/dev/null
/tmp/rootbash
/usr/bin/wall
/usr/bin/chage
/usr/bin/crontab
/usr/bin/dotlockfile
/usr/bin/mlocate
/usr/bin/expiry
/usr/bin/bsd-write
/usr/bin/mail-lock
/usr/bin/at
/usr/bin/mail-touchlock
/usr/bin/mail-unlock
/usr/bin/ssh-agent
/usr/sbin/uuidd
/sbin/unix_chkpwd
```
**OTHERS**:

```

```
</details>

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
N/A
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

# Proofs

<details><summary><ins>Proofs</ins></summary>

Final payload:
```
(root) NOPASSWD: /home/anansi/bin/anansi_util
sudo /home/anansi/bin/anansi_util manual wget

!/bin/bash

root@brainpan:/usr/share/man# id
uid=0(root) gid=0(root) groups=0(root)
root@brainpan:/usr/share/man# 
```

</details>