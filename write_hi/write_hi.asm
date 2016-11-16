global _start

section .data
	msg db 'hi'

section .text
_start:
	XOR EAX, EAX
	XOR EBX, EBX
	XOR ECX, ECX
	XOR EDX, EDX

	MOV AX, 0x6968
	PUSH AX
	XOR EAX,EAX

	MOV DL, 2
	MOV ECX, ESP
	MOV BL, 1
	MOV AL, 4
	INT 0x80
