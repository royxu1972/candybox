#!
# coding: UTF-8

'''
export plain paper list from MySQL
'''
import pymysql

class pList:
	file_name = ""

	generation = "" ;
	application = "" ;
	model = "" ;
	evaluation = "" ;
	constraint = "" ;
	prioritization = "" ;
	diagnosis = "" ;
	survey = "" ;
	oracle = "" ;

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

				# deal with the field
				if( str(r[11]) == "Generation" ):
					self.generation += "[" + str(index) + "], "
				elif( str(r[11]) == "Application" ):
					self.application += "[" + str(index) + "], "
				elif( str(r[11]) == "Model" ):
					self.model += "[" + str(index) + "], "
				elif( str(r[11]) == "Evaluation" ):
					self.evaluation += "[" + str(index) + "], "
				elif( str(r[11]) == "Constraint" ):
					self.constraint += "[" + str(index) + "], "
				elif( str(r[11]) == "Prioritization" ):
					self.prioritization += "[" + str(index) + "], "
				elif( str(r[11]) == "Diagnosis" ):
					self.diagnosis += "[" + str(index) + "], "
				elif( str(r[11]) == "Survey" ):
					self.survey += "[" + str(index) + "], "
				elif( str(r[11]) == "Oracle" ):
					self.oracle += "[" + str(index) + "], "
				
				index += 1

		cur.close()
		conn.close()


		# write field file
		with open("field.txt", 'w') as wfile:
			generation = self.generation.encode('UTF-8')
			wfile.writelines("generation: " + generation.decode('gbk') + "\n")

			application = self.application.encode('UTF-8')
			wfile.writelines("application: " + application.decode('gbk') + "\n")

			model = self.model.encode('UTF-8')
			wfile.writelines("model: " + model.decode('gbk') + "\n")

			evaluation = self.evaluation.encode('UTF-8')
			wfile.writelines("evaluation: " + evaluation.decode('gbk') + "\n")

			constraint = self.constraint.encode('UTF-8')
			wfile.writelines("constraint: " + constraint.decode('gbk') + "\n")

			prioritization = self.prioritization.encode('UTF-8')
			wfile.writelines("prioritization: " + prioritization.decode('gbk') + "\n")

			diagnosis = self.diagnosis.encode('UTF-8')
			wfile.writelines("diagnosis: " + diagnosis.decode('gbk') + "\n")

			survey = self.survey.encode('UTF-8')
			wfile.writelines("survey: " + survey.decode('gbk') + "\n")

			oracle = self.oracle.encode('UTF-8')
			wfile.writelines("oracle: " + oracle.decode('gbk') + "\n")

#
p = pList("out.txt")
p.execution()
