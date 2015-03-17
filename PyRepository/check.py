#!
# coding: UTF-8

import os
import pymysql

path = r'D:\exp - application'
sum = 0

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='paper')  
cur = conn.cursor()  
cur.execute("SELECT * FROM list")
index = 0
for r in cur:
	name = str(r[5])
	name = name.replace(':', ',')

	# search paper name
	flag = False
	for root, dirs, files in os.walk(path):
		for i in files:
			
			pos = i.index('.')
			filename = i[:pos]

			#print(filename)
			if( filename == name ):
				flag = True
	if( not flag ):
		print(name)
		index = index + 1

print("index %d" % index)



for root, dirs, files in os.walk(path):   
    #for i in dirs:
    	#print(i)

    #for j in files:
    #	print(j)
    sum = sum + len(files)

print("sum %d" % sum)