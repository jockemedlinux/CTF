# BOX NAME:

LINK: [https://www.vulnhub.com/entry/digitalworldlocal-mercy-v2,263/\[\](https://www.vulnhub.com/entry/kioptrix-2014-5,62/)](https://www.vulnhub.com/entry/digitalworldlocal-mercy-v2,263/%5B%5D%28https://www.vulnhub.com/entry/kioptrix-2014-5,62/%29 "https://www.vulnhub.com/entry/digitalworldlocal-mercy-v2,263/%5B%5D(https://www.vulnhub.com/entry/kioptrix-2014-5,62/)")

### IP=192.168.56.120
**URL=http://192.168.56.120**

# Remote Enumeration & Scan-outputs:

<ins>Host Discovery</ins>

```
[+] 192.168.56.120
```

<ins>Nmap scan</ins>

```
└─# nmap -n -sV -sC $IP -p-   
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-20 15:35 EST
Nmap scan report for 192.168.56.120
Host is up (0.00013s latency).
Not shown: 65525 closed tcp ports (reset)
PORT     STATE    SERVICE     VERSION
22/tcp   filtered ssh
53/tcp   open     domain      ISC BIND 9.9.5-3ubuntu0.17 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.9.5-3ubuntu0.17-Ubuntu
80/tcp   filtered http
110/tcp  open     pop3        Dovecot pop3d
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=localhost/organizationName=Dovecot mail server
| Not valid before: 2018-08-24T13:22:55
|_Not valid after:  2028-08-23T13:22:55
|_pop3-capabilities: TOP AUTH-RESP-CODE UIDL SASL RESP-CODES STLS PIPELINING CAPA
139/tcp  open     netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
143/tcp  open     imap        Dovecot imapd (Ubuntu)
| ssl-cert: Subject: commonName=localhost/organizationName=Dovecot mail server
| Not valid before: 2018-08-24T13:22:55
|_Not valid after:  2028-08-23T13:22:55
|_ssl-date: TLS randomness does not represent time
|_imap-capabilities: LITERAL+ ID have more OK capabilities IDLE listed STARTTLS Pre-login post-login LOGINDISABLEDA0001 LOGIN-REFERRALS ENABLE IMAP4rev1 SASL-IR
445/tcp  open     netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
993/tcp  open     ssl/imap    Dovecot imapd (Ubuntu)
| ssl-cert: Subject: commonName=localhost/organizationName=Dovecot mail server
| Not valid before: 2018-08-24T13:22:55
|_Not valid after:  2028-08-23T13:22:55
|_ssl-date: TLS randomness does not represent time
|_imap-capabilities: LITERAL+ ID more have capabilities IDLE Pre-login LOGIN-REFERRALS listed post-login OK AUTH=PLAINA0001 ENABLE IMAP4rev1 SASL-IR
995/tcp  open     ssl/pop3    Dovecot pop3d
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=localhost/organizationName=Dovecot mail server
| Not valid before: 2018-08-24T13:22:55
|_Not valid after:  2028-08-23T13:22:55
|_pop3-capabilities: TOP AUTH-RESP-CODE UIDL SASL(PLAIN) USER RESP-CODES PIPELINING CAPA
8080/tcp open     http        Apache Tomcat/Coyote JSP engine 1.1
|_http-server-header: Apache-Coyote/1.1
|_http-open-proxy: Proxy might be redirecting requests
| http-methods: 
|_  Potentially risky methods: PUT DELETE
|_http-title: Apache Tomcat
| http-robots.txt: 1 disallowed entry 
|_/tryharder/tryharder
MAC Address: 08:00:27:E2:03:55 (Oracle VirtualBox virtual NIC)
Service Info: Host: MERCY; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -1h37m36s, deviation: 4h37m07s, median: 1h02m22s
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: mercy
|   NetBIOS computer name: MERCY\x00
|   Domain name: \x00
|   FQDN: mercy
|_  System time: 2023-01-21T05:37:46+08:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_nbstat: NetBIOS name: MERCY, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| smb2-time: 
|   date: 2023-01-20T21:37:46
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.26 seconds
└─# nmap -n -sV -sC $IP -p-   
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-20 15:35 EST
Nmap scan report for 192.168.56.120
Host is up (0.00013s latency).
Not shown: 65525 closed tcp ports (reset)
PORT     STATE    SERVICE     VERSION
22/tcp   filtered ssh
53/tcp   open     domain      ISC BIND 9.9.5-3ubuntu0.17 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.9.5-3ubuntu0.17-Ubuntu
80/tcp   filtered http
110/tcp  open     pop3        Dovecot pop3d
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=localhost/organizationName=Dovecot mail server
| Not valid before: 2018-08-24T13:22:55
|_Not valid after:  2028-08-23T13:22:55
|_pop3-capabilities: TOP AUTH-RESP-CODE UIDL SASL RESP-CODES STLS PIPELINING CAPA
139/tcp  open     netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
143/tcp  open     imap        Dovecot imapd (Ubuntu)
| ssl-cert: Subject: commonName=localhost/organizationName=Dovecot mail server
| Not valid before: 2018-08-24T13:22:55
|_Not valid after:  2028-08-23T13:22:55
|_ssl-date: TLS randomness does not represent time
|_imap-capabilities: LITERAL+ ID have more OK capabilities IDLE listed STARTTLS Pre-login post-login LOGINDISABLEDA0001 LOGIN-REFERRALS ENABLE IMAP4rev1 SASL-IR
445/tcp  open     netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
993/tcp  open     ssl/imap    Dovecot imapd (Ubuntu)
| ssl-cert: Subject: commonName=localhost/organizationName=Dovecot mail server
| Not valid before: 2018-08-24T13:22:55
|_Not valid after:  2028-08-23T13:22:55
|_ssl-date: TLS randomness does not represent time
|_imap-capabilities: LITERAL+ ID more have capabilities IDLE Pre-login LOGIN-REFERRALS listed post-login OK AUTH=PLAINA0001 ENABLE IMAP4rev1 SASL-IR
995/tcp  open     ssl/pop3    Dovecot pop3d
|_ssl-date: TLS randomness does not represent time
| ssl-cert: Subject: commonName=localhost/organizationName=Dovecot mail server
| Not valid before: 2018-08-24T13:22:55
|_Not valid after:  2028-08-23T13:22:55
|_pop3-capabilities: TOP AUTH-RESP-CODE UIDL SASL(PLAIN) USER RESP-CODES PIPELINING CAPA
8080/tcp open     http        Apache Tomcat/Coyote JSP engine 1.1
|_http-server-header: Apache-Coyote/1.1
|_http-open-proxy: Proxy might be redirecting requests
| http-methods: 
|_  Potentially risky methods: PUT DELETE
|_http-title: Apache Tomcat
| http-robots.txt: 1 disallowed entry 
|_/tryharder/tryharder
MAC Address: 08:00:27:E2:03:55 (Oracle VirtualBox virtual NIC)
Service Info: Host: MERCY; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Host script results:
|_clock-skew: mean: -1h37m36s, deviation: 4h37m07s, median: 1h02m22s
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.3.11-Ubuntu)
|   Computer name: mercy
|   NetBIOS computer name: MERCY\x00
|   Domain name: \x00
|   FQDN: mercy
|_  System time: 2023-01-21T05:37:46+08:00
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
|_nbstat: NetBIOS name: MERCY, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| smb2-time: 
|   date: 2023-01-20T21:37:46
|_  start_date: N/A

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.26 seconds
```

<ins>Nikto scan</ins>

```
└─# nikto -h $IP --port 8080  
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          192.168.56.120
+ Target Hostname:    192.168.56.120
+ Target Port:        8080
+ Start Time:         2023-01-20 15:43:47 (GMT-5)
---------------------------------------------------------------------------
+ Server: Apache-Coyote/1.1
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ "robots.txt" contains 1 entry which should be manually viewed.
+ Allowed HTTP Methods: GET, HEAD, POST, PUT, DELETE, OPTIONS 
+ OSVDB-397: HTTP method ('Allow' Header): 'PUT' method could allow clients to save files on the web server.
+ OSVDB-5646: HTTP method ('Allow' Header): 'DELETE' may allow clients to remove files on the web server.
+ /: Appears to be a default Apache Tomcat install.
+ /examples/servlets/index.html: Apache Tomcat default JSP pages present.
+ OSVDB-3720: /examples/jsp/snp/snoop.jsp: Displays information about page retrievals, including other users.
+ /manager/html: Default Tomcat Manager / Host Manager interface found
+ /host-manager/html: Default Tomcat Manager / Host Manager interface found
+ /manager/status: Default Tomcat Server Status interface found
+ 8222 requests: 0 error(s) and 13 item(s) reported on remote host
+ End Time:           2023-01-20 15:44:20 (GMT-5) (33 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

<ins>Whatweb scan</ins>

```
└─# whatweb $URL:8080 | tr ',' '\n'
http://digitalworld.local:8080 [200 OK] Apache
 Apache-Tomcat
 Country[RESERVED][ZZ]
 HTTPServer[Apache-Coyote/1.1]
 IP[192.168.56.120]
 Title[Apache Tomcat]
```

# Fuzz

`ffuf -w /base/wordlists/web-fuzz/raft-large-directories.txt -u $URL/FUZZ/`
`ffuf -w /base/wordlists/web-fuzz/raft-large-files.txt -u $URL/FUZZ -recursion -mc 200,301,403`
`ffuf -w path/to/param_names.txt -u https://target/script.php?FUZZ=test_value -fs 4242`

```
/robots.txt
/tryharder/tryharder

/index.html
/login.html
/robots.txt
```

```
└─# curl $IP:8080/tryharder/tryharder -s | base64 -d
It's annoying, but we repeat this over and over again: cyber hygiene is extremely important. Please stop setting silly passwords that will get cracked with any decent password list.

Once, we found the password "password", quite literally sticking on a post-it in front of an employee's desk! As silly as it may be, the employee pleaded for mercy when we threatened to fire her.

No fluffy bunnies for those who set insecure passwords and endanger the enterprise.
```

# Port findings:

\[+\] Port 445 \[SAMBA\]

```
└─# enum4linux -aA $IP
Starting enum4linux v0.9.1 ( http://labs.portcullis.co.uk/application/enum4linux/ ) on Fri Jan 20 15:47:31 2023

 =========================================( Target Information )=========================================
                                                                                                                                                                                            
Target ........... 192.168.56.120                                                                                                                                                           
RID Range ........ 500-550,1000-1050
Username ......... ''
Password ......... ''
Known Usernames .. administrator, guest, krbtgt, domain admins, root, bin, none


 ===========================( Enumerating Workgroup/Domain on 192.168.56.120 )===========================
                                                                                                                                                                                            
                                                                                                                                                                                            
[+] Got domain/workgroup name: WORKGROUP                                                                                                                                                    
                                                                                                                                                                                            
                                                                                                                                                                                            
 ===============================( Nbtstat Information for 192.168.56.120 )===============================
                                                                                                                                                                                            
Looking up status of 192.168.56.120                                                                                                                                                         
        MERCY           <00> -         B <ACTIVE>  Workstation Service
        MERCY           <03> -         B <ACTIVE>  Messenger Service
        MERCY           <20> -         B <ACTIVE>  File Server Service
        ..__MSBROWSE__. <01> - <GROUP> B <ACTIVE>  Master Browser
        WORKGROUP       <00> - <GROUP> B <ACTIVE>  Domain/Workgroup Name
        WORKGROUP       <1d> -         B <ACTIVE>  Master Browser
        WORKGROUP       <1e> - <GROUP> B <ACTIVE>  Browser Service Elections

        MAC Address = 00-00-00-00-00-00

 ==================================( Session Check on 192.168.56.120 )==================================
                                                                                                                                                                                            
                                                                                                                                                                                            
[+] Server 192.168.56.120 allows sessions using username '', password ''                                                                                                                    
                                                                                                                                                                                            
                                                                                                                                                                                            
 ===============================( Getting domain SID for 192.168.56.120 )===============================
                                                                                                                                                                                            
Domain Name: WORKGROUP                                                                                                                                                                      
Domain Sid: (NULL SID)

[+] Can't determine if host is part of domain or part of a workgroup                                                                                                                        
                                                                                                                                                                                            
                                                                                                                                                                                            
 ==================================( OS information on 192.168.56.120 )==================================
                                                                                                                                                                                            
                                                                                                                                                                                            
[E] Can't get OS info with smbclient                                                                                                                                                        
                                                                                                                                                                                            
                                                                                                                                                                                            
[+] Got OS info for 192.168.56.120 from srvinfo:                                                                                                                                            
        MERCY          Wk Sv PrQ Unx NT SNT MERCY server (Samba, Ubuntu)                                                                                                                    
        platform_id     :       500
        os version      :       6.1
        server type     :       0x809a03


 ======================================( Users on 192.168.56.120 )======================================
                                                                                                                                                                                            
index: 0x1 RID: 0x3e8 acb: 0x00000010 Account: pleadformercy    Name: QIU       Desc:                                                                                                       
index: 0x2 RID: 0x3e9 acb: 0x00000010 Account: qiu      Name:   Desc: 

user:[pleadformercy] rid:[0x3e8]
user:[qiu] rid:[0x3e9]

 ================================( Share Enumeration on 192.168.56.120 )================================
                                                                                                                                                                                            
                                                                                                                                                                                            
        Sharename       Type      Comment
        ---------       ----      -------
        print$          Disk      Printer Drivers
        qiu             Disk      
        IPC$            IPC       IPC Service (MERCY server (Samba, Ubuntu))
Reconnecting with SMB1 for workgroup listing.

        Server               Comment
        ---------            -------

        Workgroup            Master
        ---------            -------
        WORKGROUP            MERCY

[+] Attempting to map shares on 192.168.56.120                                                                                                                                              
                                                                                                                                                                                            
//192.168.56.120/print$ Mapping: DENIED Listing: N/A Writing: N/A                                                                                                                           
//192.168.56.120/qiu    Mapping: DENIED Listing: N/A Writing: N/A

[E] Can't understand response:                                                                                                                                                              
                                                                                                                                                                                            
NT_STATUS_OBJECT_NAME_NOT_FOUND listing \*                                                                                                                                                  
//192.168.56.120/IPC$   Mapping: N/A Listing: N/A Writing: N/A

 ===========================( Password Policy Information for 192.168.56.120 )===========================
                                                                                                                                                                                            
                                                                                                                                                                                            

[+] Attaching to 192.168.56.120 using a NULL share

[+] Trying protocol 139/SMB...

[+] Found domain(s):

        [+] MERCY
        [+] Builtin

[+] Password Info for Domain: MERCY

        [+] Minimum password length: 5
        [+] Password history length: None
        [+] Maximum password age: Not Set
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
        [+] Forced Log off Time: Not Set



[+] Retieved partial password policy with rpcclient:                                                                                                                                        
                                                                                                                                                                                            
                                                                                                                                                                                            
Password Complexity: Disabled                                                                                                                                                               
Minimum Password Length: 5


 ======================================( Groups on 192.168.56.120 )======================================
                                                                                                                                                                                            
                                                                                                                                                                                            
[+] Getting builtin groups:                                                                                                                                                                 
                                                                                                                                                                                            
                                                                                                                                                                                            
[+]  Getting builtin group memberships:                                                                                                                                                     
                                                                                                                                                                                            
                                                                                                                                                                                            
[+]  Getting local groups:                                                                                                                                                                  
                                                                                                                                                                                            
                                                                                                                                                                                            
[+]  Getting local group memberships:                                                                                                                                                       
                                                                                                                                                                                            
                                                                                                                                                                                            
[+]  Getting domain groups:                                                                                                                                                                 
                                                                                                                                                                                            
                                                                                                                                                                                            
[+]  Getting domain group memberships:                                                                                                                                                      
                                                                                                                                                                                            
                                                                                                                                                                                            
 =================( Users on 192.168.56.120 via RID cycling (RIDS: 500-550,1000-1050) )=================
                                                                                                                                                                                            
                                                                                                                                                                                            
[I] Found new SID:                                                                                                                                                                          
S-1-22-1                                                                                                                                                                                    

[I] Found new SID:                                                                                                                                                                          
S-1-5-32                                                                                                                                                                                    

[I] Found new SID:                                                                                                                                                                          
S-1-5-32                                                                                                                                                                                    

[I] Found new SID:                                                                                                                                                                          
S-1-5-32                                                                                                                                                                                    

[I] Found new SID:                                                                                                                                                                          
S-1-5-32                                                                                                                                                                                    

[+] Enumerating users using SID S-1-5-32 and logon username '', password ''                                                                                                                 
                                                                                                                                                                                            
S-1-5-32-544 BUILTIN\Administrators (Local Group)                                                                                                                                           
S-1-5-32-545 BUILTIN\Users (Local Group)
S-1-5-32-546 BUILTIN\Guests (Local Group)
S-1-5-32-547 BUILTIN\Power Users (Local Group)
S-1-5-32-548 BUILTIN\Account Operators (Local Group)
S-1-5-32-549 BUILTIN\Server Operators (Local Group)
S-1-5-32-550 BUILTIN\Print Operators (Local Group)

[+] Enumerating users using SID S-1-5-21-3544418579-3748865642-433680629 and logon username '', password ''                                                                                 
                                                                                                                                                                                            
S-1-5-21-3544418579-3748865642-433680629-501 MERCY\nobody (Local User)                                                                                                                      
S-1-5-21-3544418579-3748865642-433680629-513 MERCY\None (Domain Group)
S-1-5-21-3544418579-3748865642-433680629-1000 MERCY\pleadformercy (Local User)
S-1-5-21-3544418579-3748865642-433680629-1001 MERCY\qiu (Local User)

[+] Enumerating users using SID S-1-22-1 and logon username '', password ''                                                                                                                 
                                                                                                                                                                                            
S-1-22-1-1000 Unix User\pleadformercy (Local User)                                                                                                                                          
S-1-22-1-1001 Unix User\qiu (Local User)
S-1-22-1-1002 Unix User\thisisasuperduperlonguser (Local User)
S-1-22-1-1003 Unix User\fluffy (Local User)

 ==============================( Getting printer info for 192.168.56.120 )==============================
                                                                                                                                                                                            
No printers returned.                                                                                                                                                                       


enum4linux complete on Fri Jan 20 15:47:49 2023
```

\[+\] Port 587 \[SMTP /SSL\]
\[+\] Port 993 \[IMAP /SSL\]
\[+\] Port 995 \[POP3 /SSL\]
\[+\] Port 8080 \[HTTP\]

# Local Filesystem Findings:

**FILES OF INTEREST**

```
[+]
```

**SUID**

```
[+]
```

**SGID**

```
[+]
```

**Dumps, outputs, other useful information**

**Kernel Info:
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
[+]
```

# Credentials:

```
username:password

qui:password [smb]
pleadformercy
thisisasuperduperlonguser:heartbreakisinevitable
fluffy:freakishfluffybunny

<? <role rolename="admin-gui"/>
<? <role rolename="manager-gui"/>
<? <user username="thisisasuperduperlonguser" password="heartbreakisinevitable" roles="admin-gui,manager-gui"/>
<? <user username="fluffy" password="freakishfluffybunny" roles="none"/>
<? </tomcat-users>
```

# Hashes:

```
MD4:
MD5:
SHA1:
SHA512:
```

# Exploits and Payloads:

```
[+]
```

# Writeup:

```
Started with ...
```

==PROOFS==

==![6299094866ca8bb5097d4368508f12c1.png](../../_resources/6299094866ca8bb5097d4368508f12c1.png)==

# TAKEAWAYS

```
1.
2.
3.
```