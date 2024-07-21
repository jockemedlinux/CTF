# BOX NAME: Fawkes
**LINK**: https://www.vulnhub.com/entry/harrypotter-fawkes,686/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. 
2. 
3. 
4. 
5.

```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.94
[+] URL:	http://10.77.0.94
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ jml-scanner -u $IP -p 65535

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|J|M|L|-|P|O|R|T|S|C|A|N|N|E|R|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

[+] Port 21 is open.
[+] Port 22 is open.
[+] Port 80 is open.
[+] Port 2222 is open.

[+] A total of 4 found ports open     

└─$ nmap -sV -sC $IP -oN nmap-fawkes.log
Starting Nmap 7.94 ( https://nmap.org ) at 2023-06-29 22:08 CEST
Nmap scan report for 10.77.0.94
Host is up (0.00022s latency).
Not shown: 995 closed tcp ports (conn-refused)
PORT     STATE SERVICE    VERSION
21/tcp   open  ftp        vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.77.0.88
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 3
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_-rwxr-xr-x    1 0        0          705996 Apr 12  2021 server_hogwarts
22/tcp   open  ssh        OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 48:df:48:37:25:94:c4:74:6b:2c:62:73:bf:b4:9f:a9 (RSA)
|   256 1e:34:18:17:5e:17:95:8f:70:2f:80:a6:d5:b4:17:3e (ECDSA)
|_  256 3e:79:5f:55:55:3b:12:75:96:b4:3e:e3:83:7a:54:94 (ED25519)
80/tcp   open  http       Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Site doesn't have a title (text/html).
2222/tcp open  ssh        OpenSSH 8.4 (protocol 2.0)
| ssh-hostkey: 
|   3072 c4:1d:d5:66:85:24:57:4a:86:4e:d9:b6:00:69:78:8d (RSA)
|   256 0b:31:e7:67:26:c6:4d:12:bf:2a:85:31:bf:21:31:1d (ECDSA)
|_  256 9b:f4:bd:71:fa:16:de:d5:89:ac:69:8d:1e:93:e5:8a (ED25519)
9898/tcp open  tcpwrapped
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
└─$ whatweb $URL --log-verbose=whatweb-fawkes-verbose.log | tee whatweb-dobby.log
http://10.77.0.94 [200 OK] Apache[2.4.38], Country[RESERVED][ZZ], HTTPServer[Debian Linux][Apache/2.4.38 (Debian)], IP[10.77.0.94]

```

nikto-scan
```
└─$ nikto -h $URL | tee nikto-fawkes.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.94
+ Target Hostname:    10.77.0.94
+ Target Port:        80
+ Start Time:         2023-06-29 22:08:12 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.38 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/                          
+ No CGI Directories found (use '-C all' to force check all possible dirs)                                                                                
+ /: Server may leak inodes via ETags, header found with file /, inode: 61, size: 5bf5c5e4e96a6, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ Apache/2.4.38 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.                                  
+ OPTIONS: Allowed HTTP Methods: OPTIONS, HEAD, GET, POST .                                                                                                                              
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/                                                                      
+ 8102 requests: 0 error(s) and 6 item(s) reported on remote host                                                                                                                        
+ End Time:           2023-06-29 22:08:40 (GMT2) (28 seconds)                                                                                                                            
---------------------------------------------------------------------------                                                                                                              
+ 1 host(s) tested       
```

fuzzing
```

```
other
```
└─$ telnet $IP 9898          
Trying 10.77.0.94...
Connected to 10.77.0.94.
Escape character is '^]'.
Welcome to Hogwart's magic portal
Tell your spell and ELDER WAND will perform the magic

Here is list of some common spells:
1. Wingardium Leviosa
2. Lumos
3. Expelliarmus
4. Alohomora
5. Avada Kedavra 

Enter your spell: 

```

</details>

<details><summary><ins>SERVICES</ins></summary>

FTP
```

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


# LOOT

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*
```

```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password

harry:HarrYp0tter@Hogwarts123
nevilla:bL!Bsg3k
root:mySecr3tPass
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
docker container:
sudo -l 
User harry may run the following commands on 2b1599256ca6:
    (ALL) NOPASSWD: ALL
sudo su
cd /root/
cat note.txt

Hello Admin!!

We have found that someone is trying to login to our ftp server by mistake.You are requested to analyze the traffic and figure out the user.
```
```
tcpdump -i eth0 port ftp -w cap.pcap
analyze cap.pcap in wireshark

220 (vsFTPd 3.0.3)
USER neville
331 Please specify the password.
PASS bL!Bsg3k
530 Login incorrect.
QUIT
221 Goodbye.
```

```
horcrux_{NjogSGFSclkgUG90VGVyIGRFc1RyT3llZCBieSB2b2xEZU1vclQ=}
-> 6: HaRrY PotTer dEsTrOyed by volDeMorT
horcrux_{NzogTmFHaU5pIHRIZSBTbkFrZSBkZVN0cm9ZZWQgQnkgTmVWaWxsZSBMb25HYm9UVG9t}
-> 7: NaGiNi tHe SnAke deStroYed By NeVille LonGboTTom

```

```

```

</details>