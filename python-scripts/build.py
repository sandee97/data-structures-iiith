#!/usr/bin/python
## Build script
## inst_i denotes ith instruction
## if inst_i==0 than instruction is successful else not
 
import os
inst_1=os.chdir("../src")
inst_2=os.system("make all")
inst_3=os.system("cd ..")
inst_4=os.system("cp -r ../build/ /var/www/")
inst_5=os.system("chmod 777 /var/www/build/ -R")

if((inst_1 or inst_2 or inst_3 or inst_4 or inst_5)==0):
	print "****************"
	print "Build Successful"
	print "****************"
else:
	print "******************"
	print "Build Unsuccessful"
	print "******************"
