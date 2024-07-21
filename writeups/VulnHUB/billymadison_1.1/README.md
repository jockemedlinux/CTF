BOX NAME: BillyMadison1.1  
LINK: https://www.vulnhub.com/entry/billy-madison-11,161/

IP=172.168.0.125  
URL=http://172.168.0.125:80

Portknocking:  
1466,67,1469,1514,1981,1986

# Credentials:

\[+\] eric:exschmenuating \[smb\]  
\[+\] eric:ericdoesntdrinkhisownpee \[ftp\]  
\[+\] max  
\[+\] veronica:babygirl_veronica07@yahoo.com \[ftp\]

# Hashes:

\[+\]

# Hosts and computers:

\[+\] HOSTS: bm  
\[+\] FQDN: bm  
\[+\] COMPUTER NAME: bm  
\[+\] OS:

# NOTES

\[+\] webroot

```
                             ****** UH OH! ******
                          [eric-tongue-animated.gif]
                         ****** Silly Billy!!! ******
**** If you're reading this, you clicked on the link I sent you. OH NOES! Your
computer's all locked up, and now you can't get access to your final 12th grade
  assignment you've been working so hard on! You need that to graduate, Billy
                                  Boy!! ****
       **** Now all I have to do is sit and wait for a while and... ****
                                 [hotels.gif]
                   ***** I bet this is you right now: *****
                 [billy-mad.png][billy-mad.png][billy-mad.png]
  ***** Think you can get your computer unlocked and recover your final paper
            before time runs out and you FAAAAIIIILLLLL????? *****
                              Good luck, schmuck.
```

# Remote Enumeration:

netdiscover -r $IP -i eth0

```
 _____________________________________________________________________________
   IP            At MAC Address     Count     Len  MAC Vendor / Hostname      
 -----------------------------------------------------------------------------
 172.168.0.1     08:00:27:d5:d3:e8      1      60  PCS Systemtechnik GmbH                                          
 172.168.0.125   08:00:27:92:99:69      1      60  PCS Systemtechnik GmbH
```

nmap -n -sS $IP -p-

```
PORT     STATE  SERVICE     VERSION
22/tcp   open   tcpwrapped
23/tcp   open   telnet?
69/tcp   open   caldav      Radicale calendar and contacts server (Python BaseHTTPServer)
80/tcp   open   http        Apache httpd 2.4.18 ((Ubuntu))
137/tcp  closed netbios-ns
138/tcp  closed netbios-dgm
139/tcp  open   netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open   netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
2525/tcp open   smtp        SubEtha smtpd
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port23-TCP:V=7.93%I=7%D=11/2%Time=6362825F%P=x86_64-pc-linux-gnu%r(NULL
SF:,E6,"\n\n\*\*\*\*\*\x20HAHAH!\x20You're\x20banned\x20for\x20a\x20while,
SF:\x20Billy\x20Boy!\x20\x20By\x20the\x20way,\x20I\x20caught\x20you\x20try
SF:ing\x20to\x20hack\x20my\x20wifi\x20-\x20but\x20the\x20joke's\x20on\x20y
SF:ou!\x20I\x20don't\x20use\x20ROTten\x20passwords\x20like\x20rkfpuzrahngv
SF:at\x20anymore!\x20Madison\x20Hotels\x20is\x20as\x20good\x20as\x20MINE!!
SF:!!\x20\*\*\*\*\*\n\n");
MAC Address: 08:00:27:92:99:69 (Oracle VirtualBox virtual NIC)
Service Info: Host: BM
```

# Interesting:

\[+\] Wordpress running on port 69. Restricted from Firefox. Proxy that.  
\[+\] Port 2525 seems to be a SMTP-log file. Potential Logpoison.  
\[+\] Telnet port 23 gives haunting message.

```
    ***** HAHAH! You're banned for a while, Billy Boy!  By the way, I caught you trying to hack my wifi - but the joke's on you! I don't use ROTten passwords like rkfpuzrahngvat anymore! Madison Hotels is as good as MINE!!!! *****

```

# Searchsploit Findings:

\[+\] Port 21 \[FTP\]  
\[+\] Port 22 \[SSH\]  
\[+\] Port 23 \[TELNET\]  
\[+\] Port 25 \[SMTP\]  
\[+\] Port 53 \[DNS\]  
\[+\] Port 80 \[HTTP\]  
\[+\] Port 88 \[Kerberos\]  
\[+\] Port 110 \[POP3\]  
\[+\] Port 111 \[NFS\]  
\[+\] Port 137 \[NETBIOS\]  
\[+\] Port 139 \[NETBIOS\]  
\[+\] Port 143 \[IMAP\]  
\[+\] Port 443 \[HTTPS\]  
\[+\] Port 445 \[SAMBA\]  
\[+\] Port 464 \[Kerberos\]  
\[+\] Port 465 \[SMTP\]  
\[+\] Port 631 \[CUPS\]  
\[+\] Port 587 \[SMTP /SSL\]  
\[+\] Port 993 \[IMAP /SSL\]  
\[+\] Port 995 \[POP3 /SSL\]  
\[+\] Port 1194 \[OPENVPN\]  
\[+\] Port 2049 \[NFS\]  
\[+\] Port 3306 \[MySQL\]  
\[+\] Port 5432 \[PostgreSQL\]  
\[+\] Port 5900 \[VNC\]  
\[+\] Port 5901 \[VNC\]  
\[+\] Port 6001 \[X-SERVER\]  
\[+\] Port 6667 \[IRC\]  
\[+\] Port 6668 \[IRC\]  
\[+\] Port 6669 \[IRC\]  
\[+\] Port 6881 \[TORRENT\]  
\[+\] Port 8080 \[HTTP\]

# FTP:

\[+\] ftp anonyomus@$IP

# SMB:

\[+\] smbclient -L $IP

# NFS:

\[+\] showmount -e $IP  
\[+\] mount -t nfs $IP:/remote/folder local/folder

# SMTP:

\[+\] smtp-user-enum -U users.txt -t $IP

# HTTP/HTTPS:

\[+\] feroxbuster -u $IP -d 1

\[+\] gobuster dir|vhost http://$IP

\[+\] Nikto --url http://$IP -C all

\[+\] ffuf -u '$URL/FUZZ' -w wordlist.txt -fs filtersize

# enum4linux:

\[+\] enum4linux -A $IP

# CMS:

\[+\] cmseek -u http://$IP --random-agent

\[+\] wpscan -u $IP

\[+\] droopescan -u $IP

\[+\] joomscan -u $IP -ec

# Local Filesystem Findings:

\[+\] FILES OF INTEREST

\[+\] SUID

```
/usr/local/share/sgml/donpcgd
/usr/bin/sudo
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/newgidmap
/usr/bin/chsh
/usr/bin/gpasswd
/usr/bin/newuidmap
/usr/bin/newgrp
/usr/bin/at
/usr/bin/chfn
/usr/bin/ubuntu-core-launcher
/usr/lib/eject/dmcrypt-get-device
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/bin/mount
/bin/su
/bin/umount
/bin/fusermount
/bin/ping6
/bin/ping
/bin/ntfs-3g

```

\[+\] SGID

\[+\] Dumps, outputs, others

# Kernel Info:

\[+\] file /bin/bash

```
/bin/bash: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=0428e4834e687e231fa865562d32fbb64ce45577, stripped
```

\[+\] lsb_release -a

```
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.1 LTS
Release:        16.04
Codename:       xenial
```

\[+\] uname -a

```
Linux BM 4.4.0-36-generic #55-Ubuntu SMP Thu Aug 11 18:01:55 UTC 2016 x86_64 x86_64 x86_64 GNU/Linux
```

# Exploits and Payloads:

\[+\] PwnKit to root the box

```
PwnKit (CVE-2021-4034) \\
cd /base/exploits/kernel ; python3 -m http.server
gcc -shared PwnKit.c -o PwnKit -Wl,-e,entry -fPIC
```

# Writeup:

STEPS TAKEN:  
\[+\]  
\[+\]  
\[+\]  
\[+\]  
\[+\]

==DIARY==

```
Started with ...
```

==PROOF==

den hade allt...

truecrypt -t file -w wordlist  
knock 172.168.0.125 port port port port  
hcxpcapngtool -o hash.hc22000 eg-01.cap  
kernel exploit