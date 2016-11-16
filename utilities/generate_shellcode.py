#!/usr/bin/python

import sys
import subprocess

if len(sys.argv) == 1:
	print "usage: generate_shellcode.py <file>.asm"
	sys.exit(1)

fileName = sys.argv[1]
if "." in fileName:
	fileName = fileName.split(".")[0]
fileName = fileName + ".o"

subprocess.check_output(["nasm", "-f elf", "-o", fileName, sys.argv[1]])
subprocess.check_output(["ld", fileName, "-o", fileName + "ut"])

#objdump -s -j .text HelloWorld.o
objdumpLines = subprocess.check_output(["objdump", "-s", "-j", ".text", fileName + "ut"], universal_newlines=False)
for line in objdumpLines.split("\n"):
	if line.startswith(" "):
		code = line[9:44].replace(" ", "")
		t = iter(code)
		code = "\\x".join(a+b for a,b in zip(t,t))
		sys.stdout.write("\\x" + code)

print ""
