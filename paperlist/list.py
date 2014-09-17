#!
# coding: UTF-8

'''
export plain paper list from MySQL
'''
import pymysql

class pList:
	file_name = ""
	def __init__(self, str):
		self.file_name = str

	def execution(self):
		conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='paper')  
		cur = conn.cursor()  
		cur.execute("SELECT * FROM list order by year DESC")

		index = 1
		with open(self.file_name, 'w') as wfile:
			for r in cur:
				# [index] + author + title  + "in" + publication
				content = "[" + str(index) + "] " + str(r[4]) + ", " + str(r[5]) + ", in " + str(r[6])

				# abbr
				abbr = str(r[7])
				if( abbr not in ["None", "book", "phd", "tech"] ):
					content += " (" + abbr + ")"

				# "vol(no): page, year" for article
				if( str(r[2]) == "article" ):
					content += ", " + str(r[8]) + "(" + str(r[9]) + "): " + str(r[10]) + ", " + str(r[3])
				# "year: page" for inproceedings
				elif( str(r[2]) == "inproceedings" ):
					content += ", " + str(r[3]) + ": " + str(r[10])
				# "TechNo, year" for techreport
				elif( str(r[2]) == "techreport" ):
					content += ", " + str(r[9]) + ", " + str(r[3])
				# for phdthesis and book
				else:
					content += ", " + str(r[3])

				con = content.encode('UTF-8')
				#print("content" + str(type(content)))
				#print("con" + str(type(con)))
				wfile.writelines(con.decode('gbk') + "\n")

				index += 1

		cur.close()
		conn.close()
	
#
p = pList("out.txt")
p.execution()
