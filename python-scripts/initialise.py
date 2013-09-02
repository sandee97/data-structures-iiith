#!/usr/bin/python
## Initialize script
## inst_i denotes ith instruction
## if inst_i==0 than instruction is successful else not
 
import os
inst_1=os.system("export http_proxy=http://proxy.iiit.ac.in:8080/")
inst_2=os.system("apt-get update")
filen="./dependencies.txt"
f=open(filen,"r")
dep=f.readlines()
f.close()
for pack in dep:
	p=pack.strip()
	inst_3=os.system("apt-get install -y "+p)

inst_4=os.system("./build.py")
if((inst_1 or inst_2 or inst_3 or inst_4)==0):
	print "************************"
	print "Intialization Successful"
	print "************************"
else:
	print "**************************"
	print "Intialization Unsuccessful"
	print "**************************"

