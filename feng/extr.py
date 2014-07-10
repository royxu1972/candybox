# python
# coding:utf-8

import re

file1 = open("input1.txt", 'r')
file2 = open("input2.txt", 'r')

output1 = []
output2 = []

flag = 0
str_tp = ""

for line in file1:
	line = line.strip()

	# unread state
	if(flag == 0 and line.startswith('k')):
		flag = 1
		continue ;

	# read state
	if(flag == 1):
		if(line.startswith('o')):
			#print(str_tp)
			output1.append(str_tp)
			flag = 0 ;
			str_tp = ""
		elif(line.startswith('k')):
			print(str_tp)
			output1.append(str_tp)
			str_tp = ""

	if(flag and re.match("[0-9|-]",line) is not None):
		#print(line)
		str_tp = str_tp + line + " "	

if(str_tp != ""):
	output1.append(str_tp)


for line in file2:
	line = line.strip()
	lines = line.split()
	output2.append(lines[0] + " " + lines[1] )

file3 = open("output.txt", 'w')
if(len(output1) == len(output2)):
	for i in range(0,len(output1)):
		file3.write(output2[i] + " " + output1[i] + "\n")

