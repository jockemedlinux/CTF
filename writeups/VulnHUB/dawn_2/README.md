# BOX NAME: Dawn 2

LINK: [](https://www.vulnhub.com/entry/kioptrix-2014-5,62/)

IP=10.10.35.115
URL=10.10.35.115

# Credentials:

# Hashes:

# Remote Enumeration:

### <ins>Host Discovery</ins>

### <ins>Nmap scan</ins>

```
PORT     STATE SERVICE
80/tcp   open  http
1435/tcp open  ibm-cics
1985/tcp open  hsrp
```

# Hosts and computers:

\[+\] HOSTS: wonderland
\[+\] FQDN: 
\[+\] COMPUTER NAME: wonderland
\[+\] OS:

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

# Local Filesystem Findings:

\[+\] FILES OF INTEREST

\[+\] SUID

\[+\] SGID

\[+\] Dumps, outputs, other useful information

# Kernel Info:

\[+\] file /bin/bash | lsb_release -a | uname -a

```
output
```

# Exploits and Payloads:

\[+\] XXX

# Writeup:

==DIARY==

```
Started with ...
```

==PROOF==

![7b037fdf0c23d8066bf2df4e99a7a6ee.png](../../_resources/7b037fdf0c23d8066bf2df4e99a7a6ee.png)

# TAKEAWAYS (SCRIPT)

```python
##########################################
##Template created by jkarlberget @ 2023-01-08##
##########################################

import os,sys,subprocess,socket

# // target
host = "192.168.56.101"
port = 0

# // fun stuff.
cowsending = subprocess.getoutput("echo 'Sending beezneez:::' | cowsay")
cowsent = subprocess.getoutput("echo ':::Beezneez sent' | cowsay")
cowfail	= subprocess.getoutput("echo 'Is it even running, guy?' | cowsay")

# // Tinker variables
#As = 0
#Bs = 0 
#Cs = 0
#Nops = 0
#Null = 0

# // Alternative way of runnin the buffer. Dont forget to change payload to "buf"
# buf = ""
# buf += ""
# buf += ""
# buf += ""
# buf += ""

# // badcharacters check

#bad = (
#"\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
#"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
#"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
#"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
#"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
#"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
#"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
#"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
#"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
#"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
#"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
#"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
#"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
#"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
#"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
#"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
#)

#// Malicious shellcode to run. (if not using buf as above)
#buf = (
#
#
#	)

# // Actual program
def main():
    target = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    try:
        print(cowsending)
        target.connect((host, ip))
        print(payload)
        target.send(payload) # remeber to define payload as bytes if using alternative buf method
        print(cowsent)
    except:
        print(cowfail)

if __name__ == "__main__":
```