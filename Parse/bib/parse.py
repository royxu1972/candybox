#!
# coding: UTF-8
# convert .bib file

from bibtexparser.bparser import BibTexParser
from paper import *  

class Parse:
	def __init__(self):
		self.bib_list = []
		self.bib_num = -1
		self.papers = []

	def ReadFromFile(self, file_name):
		with open(file_name, 'r') as bibfile:
			bp = BibTexParser(bibfile)
			self.bib_list = bp.get_entry_list()
			self.bib_num = len(self.bib_list)

			for each in self.bib_list:
				pd = Paper(each)
				#pd.printPlainRef()
				self.papers.append(pd)

	def WriteData(self):
		with open("data.txt", 'w') as wfile:
			for pa in self.papers:
				wfile.writelines(pa.Data())



class ParseAuthor:
	def __init__(self):
		self.listauthor = set()

	def Parse(self, input_name, output_name):
		with open(input_name, "r") as readfile:
			count = 0
			for authors in readfile: 
				authors = authors.strip('\n')
				author = authors.split(',')[0]
				self.listauthor.add(author)
				count += 1
				#print(author)

		# print to file
		print( "all " + str(len(self.listauthor)) + " authors" )

		with open(output_name, 'w') as writefile:
			for each in self.listauthor:
				writefile.writelines(each + "\n")


#
#p = Parse()
#p.ReadFromFile("0422.bib")
#p.WriteData()

a = ParseAuthor()
a.Parse("author.txt","listauthor.txt")





		