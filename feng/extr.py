# python
# coding:utf-8

import re

class Extr:
	
	def __init__(self,str1,str2,str3):
		self.file1_name = str1
		self.file2_name = str2
		self.file3_name = str3
		self.output1 = []
		self.output2 = []


	def read_file1(self):
		file1 = open(self.file1_name, 'r')
		line = file1.readline()
		line = line.strip()

		# mode 1
		if( line.startswith('k') ):
			flag = 1
			str_tp = ""
			for line in file1:
				line = line.strip()
				
				# read state
				if(flag and re.match("[0-9|-]",line) is not None):
					#print(line)
					str_tp = str_tp + line + " "

				# unread state
				if(flag == 0 and line.startswith('k')):
					flag = 1
					continue ;

				if(flag == 1):
					if(line.startswith('o')):
						#print(str_tp)
						self.output1.append(str_tp)
						flag = 0 ;
						str_tp = ""
					elif(line.startswith('k')):
						print(str_tp)
						self.output1.append(str_tp)
						str_tp = ""

			if(str_tp != ""):
				self.output1.append(str_tp)

		# mode 2
		if( line.startswith('&') ):
			num = int(line[line.find('nbnd=')+5: line.find(',')])
			flag = 0
			str_tp = ""

			line = file1.readline()
			for line in file1:
				line = line.strip()
				elements = line.split()

				# insert state
				if(flag == num and len(elements) == 3):
					self.output1.append(str_tp)
					str_tp = ""
					flag = 0
					continue
				# read state
				if( 0 <= flag <= num):
					str_tp = str_tp + ' '.join(elements) + " "
					flag += len(elements)
			
			if(str_tp != ""):
				self.output1.append(str_tp)


	def execution(self):
		self.read_file1()

		file2 = open(self.file2_name, 'r')
		for line in file2:
			line = line.strip()
			lines = line.split()
			self.output2.append(lines[0] + " " + lines[1] )

		file3 = open(self.file3_name, 'w')
		if(len(self.output1) == len(self.output2)):
			for i in range(0,len(self.output1)):
				file3.write(self.output2[i] + " " + self.output1[i] + "\n")


e = Extr("input1.txt","input2.txt","output.txt")
e.execution()




