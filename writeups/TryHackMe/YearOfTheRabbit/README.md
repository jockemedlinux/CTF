# BOX NAME: YearOfTheRabbit [EASY]
**LINK**: https://tryhackme.com/room/yearoftherabbit

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
[+] IP:		
[+] URL:	http://
```
</details>
<details><summary><ins>NMAP</ins></summary>

```

```
</details>
<details><summary><ins>WEB</ins></summary>

whatweb-scan
```

```

nikto-scan
```

```

fuzzing
```

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

ftpuser:5iez1wGXKfPKQ
eli:DSpDiM1wAEwid
gwendoline:MniVCQVhQHUNI

eli@10.10.151.18's password: 


1 new message
Message from Root to Gwendoline:

"Gwendoline, I am not happy with you. Check our leet s3cr3t hiding place. I've left you a hidden message there"

END MESSAGE


_

THM{112i3GEaM9rnY33oTh3H8XjtbWwdZ5SvB3}

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
gwendoline@year-of-the-rabbit:/tmp$ gcc -shared pwnkit.c -o PwnKit -Wl,-e,entry -fPIC

```

```
root@year-of-the-rabbit:~# cat root.txt 
THM{8d6f163a87a1c80de27a4fd61aef0f3a0ecf9161}
root@year-of-the-rabbit:~# 

sudo -u#-1

```

```
THM{112i3GEaM9rnY33oTh3H8XjtbWwdZ5SvB3}
THM{8d6f163a87a1c80de27a4fd61aef0f3a0ecf9161}
```

</details>
