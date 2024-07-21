# BOX NAME: Dawn 1

LINK: [](https://www.vulnhub.com/entry/kioptrix-2014-5,62/)

IP=192.168.56.104

URL=http://192.168.56.104

## Credentials:

```
dawn:onii-chan29
ganimedes
```

## Hashes:

```
$1$$bOKpT2ijO.XcGlpjgAup9/
```

## Remote Enumeration:

## <ins>Host Discovery</ins>

```
fping -agq 192.168.56.1/24
> 192.168.56.104
```

## <ins>Nmap scan</ins>

```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-01-06 15:28 EST
Nmap scan report for 192.168.56.104
Host is up (0.00013s latency).
Not shown: 996 closed tcp ports (reset)
PORT     STATE SERVICE     VERSION
80/tcp   open  http        Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Site doesn't have a title (text/html).
139/tcp  open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp  open  netbios-ssn Samba smbd 4.9.5-Debian (workgroup: WORKGROUP)
3306/tcp open  mysql       MySQL 5.5.5-10.3.15-MariaDB-1
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.15-MariaDB-1
|   Thread ID: 14
|   Capabilities flags: 63486
|   Some Capabilities: Support41Auth, DontAllowDatabaseTableColumn, ODBCClient, Speaks41ProtocolNew, SupportsTransactions, IgnoreSigpipes, Speaks41ProtocolOld, ConnectWithDatabase, LongColumnFlag, InteractiveClient, SupportsLoadDataLocal, IgnoreSpaceBeforeParenthesis, SupportsCompression, FoundRows, SupportsAuthPlugins, SupportsMultipleResults, SupportsMultipleStatments
|   Status: Autocommit
|   Salt: ~)L&r2>#4x$DifC["3z1
|_  Auth Plugin Name: mysql_native_password
MAC Address: 08:00:27:8C:46:B9 (Oracle VirtualBox virtual NIC)
Device type: general purpose
Running: Linux 3.X|4.X
OS CPE: cpe:/o:linux:linux_kernel:3 cpe:/o:linux:linux_kernel:4
OS details: Linux 3.2 - 4.9
Network Distance: 1 hop
Service Info: Host: DAWN

Host script results:
|_clock-skew: mean: 1h39m58s, deviation: 2h53m12s, median: -2s
| smb-os-discovery: 
|   OS: Windows 6.1 (Samba 4.9.5-Debian)
|   Computer name: dawn
|   NetBIOS computer name: DAWN\x00
|   Domain name: dawn
|   FQDN: dawn.dawn
|_  System time: 2023-01-06T15:29:05-05:00
| smb2-security-mode: 
|   311: 
|_    Message signing enabled but not required
|_nbstat: NetBIOS name: DAWN, NetBIOS user: <unknown>, NetBIOS MAC: 000000000000 (Xerox)
| smb-security-mode: 
|   account_used: guest
|   authentication_level: user
|   challenge_response: supported
|_  message_signing: disabled (dangerous, but default)
| smb2-time: 
|   date: 2023-01-06T20:29:05
|_  start_date: N/A

TRACEROUTE
HOP RTT     ADDRESS
1   0.13 ms 192.168.56.104
```

## Hosts and computers:

## \[+\] HOSTS: Dawn

\[+\] FQDN: Dawn.dawn
\[+\] COMPUTER NAME: DAWN
\[+\] OS: Linux 3.2-4.9

## Special searchsploit findings:

## \[+\] Port 80 \[HTTP\]

\[+\] Port 139 \[NETBIOS\]
\[+\] Port 445 \[SAMBA\]
\[+\] Port 3306 \[MySQL\]

## Local Filesystem Findings:

## \[+\] FILES OF INTEREST

## \[+\] SUID

## \[+\] SGID

## \[+\] Dumps, outputs, other useful information

## Kernel Info:

## \[+\] file /bin/bash | lsb_release -a | uname -a

```
output
```

## Exploits and Payloads:

## \[+\] XXX

## Writeup:

```
>>> Remote Enumeration
Started with basic remote enumeration. Host discovery, nmap scan, web-fuzzers m.m.
Found directories:
/logs/
/cctv/

In /logs/ were some log files. In maintenance we found some discrepencies (1).
It seems a cronjob is running and making file "web-control" and "product-control" world-RWX. and then executing them with "bash -c".
We enumerate some smb-shares and find there is share "ITDEPT" which is located at "/home/dawn/ITDEPT/". Coincidence? I think not.

So we put a basic reverse shell in web-control and product-control and start up our listener.
Product-control comes back and bam. We have compromised the machine.(2)
We stabalize the shell and start out Local Enumeration.

>>> Local Enumeration:
sudo -l shows us we're able to run mysql as root without a password.(3)
We could exploit this but there seems to be a faulty configuration. The password must be provided.
Further enumeration shows the user has left the md5crypted password echoed in the terminal. 
We grab that, crack that and perform a privilege escalation via the mysql.(4)(5)

Proof the box was fully compromised without the use of any known kernel exploits. (6)

Assessment Value: Critical!
```

## 1)

## ![44ce8b73544db8a68b5a6358fddb4e31.png](../../_resources/44ce8b73544db8a68b5a6358fddb4e31.png)

## ![129aef312ebe3ec8c290b435cf3f7411.png](../../_resources/129aef312ebe3ec8c290b435cf3f7411.png)

## ![a59d70869c7ac26324fae5af84aa95f4.png](../../_resources/a59d70869c7ac26324fae5af84aa95f4.png)

## 4)

## ![39bafe913f0618363b9ebd2bd7f20a11.png](../../_resources/39bafe913f0618363b9ebd2bd7f20a11.png)

## 5)

## ![cda53de6dfb70635151578c32bcdddb5.png](../../_resources/cda53de6dfb70635151578c32bcdddb5.png)

## 6

## ![8a17111aab2e4c09b806ea7c9e0647d7.png](../../_resources/8a17111aab2e4c09b806ea7c9e0647d7.png)

## ==PROOF==

==flag{3a3e52f0a6af0d6e36d7c1ced3a9fd59}==

## TAKEAWAYS

```
1. If mysql is able to run as root but requires password. Keep looking.
2.
3.
```

## OTHER VULNERABILITIS FOUND:

```bash
/usr/bin/zsh is has a setuid bit as root (1) 
can be exploited with the "/usr/bin/zsh -p" payload
```

```
the machine is also vulnerable to the CVE-2021-4034 exploit (1.1)
```

## 1.1)

## ![be867a5a8f91bd9547245e8808433ae1.png](../../_resources/be867a5a8f91bd9547245e8808433ae1.png)