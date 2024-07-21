# BOX NAME: Symfonos 5
**LINK**: https://www.vulnhub.com/entry/symfonos-52,415/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. 
2. 
3. 
4. 

So right of the bat the scans show we have som LDAP configured on the box. I'm not very comfortable with LDAP on linux so this machine is gonna take som research i recon..

```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.60
[+] URL:	http://symfonos.local
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-symfonos5.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-29 08:09 CEST
Nmap scan report for symfonos.local (10.77.0.60)
Host is up (0.00020s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 7.9p1 Debian 10+deb10u1 (protocol 2.0)
| ssh-hostkey: 
|   2048 1670137722f96878400d2176c1505423 (RSA)
|   256 a80623d093187d7a6b05778d8bc9ec02 (ECDSA)
|_  256 52c08318f4c738655ace9766f375684c (ED25519)
80/tcp  open  http     Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Site doesn't have a title (text/html).
389/tcp open  ldap     OpenLDAP 2.2.X - 2.3.X
636/tcp open  ldapssl?
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.66 seconds
```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
└─$ whatweb $URL --log-verbose=whatweb-symfonos5.log
http://symfonos.local [200 OK] Apache[2.4.29], Country[RESERVED][ZZ], HTTPServer[Ubuntu Linux][Apache/2.4.29 (Ubuntu)], IP[10.77.0.60]

```

nikto-scan

```
└─$ nikto -h $URL | tee nikto-symfonos5.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.60
+ Target Hostname:    symfonos.local
+ Target Port:        80
+ Start Time:         2023-04-29 08:10:09 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.29 (Ubuntu)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.29 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Server may leak inodes via ETags, header found with file /, inode: cf, size: 59b7f675f3d40, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ OPTIONS: Allowed HTTP Methods: GET, POST, OPTIONS, HEAD .
+ /home.php?arsc_language=elvish: Cookie PHPSESSID created without the httponly flag. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies
+ /admin.php?en_log_id=0&action=config: EasyNews version 4.3 allows remote admin access. This PHP file should be protected. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2006-5412
+ /admin.php?en_log_id=0&action=users: EasyNews version 4.3 allows remote admin access. This PHP file should be protected. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2006-5412
+ /admin.php: This might be interesting.
+ /static/: Directory indexing found.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 7962 requests: 0 error(s) and 11 item(s) reported on remote host
+ End Time:           2023-04-29 08:10:47 (GMT2) (38 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing

```
admin.php
```
Summary

```
So there is an admin page. Fuzz the auth bypass: *))%00
on the admin-page source-html there seems to be a link referencing localhost and a ?url parameter also referencing localhost.
**<a class="nav-link" href="http://127.0.0.1/home.php?url=http://127.0.0.1/portraits.php">Portraits</a>**
If we proxy the traffic through foxyproxy to 127.0.0.1:8000 and setting up a proxy on our local-machine to the remote localhost on port 80, we can access the page. Seems to only be some pictures of gods.
socat tcp-listen:8000,fork tcp:symfonos.local:80

We're able to fuzz the remote machine web-root with:
**ffuf -u http://127.0.0.1:8000/FUZZ -w /base/wordlists/lfi/jml-lfi.txt**


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

```

</details>