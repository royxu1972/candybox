#!
# coding: UTF-8
#
# paper format
import re

class Paper:
	"""
	@article : id, type, author, title, journal, volume, number, pages, year, field, doi
	@inproceedings: id, type, author, title, booktitle, pages, year, field, doi
	@phdthesis: id, type, author, title, school, year, field, doi
	@techreport: id, type, author, title, institution, number, year, field 

	"""
	def __init__(self, item):
		self.dic = item

		# bib id and type, @...
		self.id = item.get('id')
		self.type = item.get('type')
		# 
		self.author = ""
		self.title = ""
		self.publication = ""
		self.vol = ""
		self.no = ""
		self.pages = ""
		self.year = ""
		self.field = ""
		self.doi = ""

		# format data
		self._formatAuthor()
		self._formatTitle()
		self._formatPublication()
		self._formatKeyfield()
		self._formatDOI()


	# author: convert to First + Middle. + Last Name
	def _formatAuthor(self):
		a = self.dic.get('author')
		if( a is None ):
			self.author = ""
			print("missing author for " + self.id )
			return

		author_list = a.split(' and ')
		for index in range(len(author_list)):
			seprate = author_list[index].split(',')
			# First + Middle. + Last Name
			pattern = re.compile(".*\s[A-Z]$")
			if( pattern.match(seprate[1]) ):
				combine = seprate[1] + ". " + seprate[0]
			else:
				combine = seprate[1] + " " + seprate[0]
			author_list[index] = combine

		# join author_list
		self.author = ",".join(author_list)
		self.author = self.author.strip()

	# title
	def _formatTitle(self):
		self.title = self.dic.get('title')
		if( self.title is None ):
			self.title = ""
			print("missing title for " + self.id )


	 # publication: convert to "Interactional conference on ..."
	def _formatPublication(self):
		if( self.type == "inproceedings" ):
			self.publication = self.dic.get('booktitle')
			# if begin with "XXX' 00: "
			index = self.publication.find(": ")
			if( index != -1 ):
				self.publication = self.publication[index+2:len(self.publication)]

			# replace "\{\&\}" with "&"
			self.publication = self.publication.replace("\{\&\}","&")

		if( self.type == "article" ):
			self.publication = self.dic.get('journal')
			self.vol = self.dic.get('volume')
			self.no = self.dic.get('number')
			if( self.vol is None ):
				self.vol = ""
				print("missing volume for " + self.id )
			if( self.no is None ):
				self.no = ""
				print("missing number for " + self.id )

		if( self.type == "phdthesis" ):
			self.publication = self.dic.get('school')


		# pages
		if( self.type == "inproceedings" or self.type == "article" ):
			page = self.dic.get('pages')
			if( page is None ):
				print("missing pages for " + self.id )
			else:
				strinfo = re.compile('-+')
				self.pages = strinfo.sub('-', page)

		# year
		y = self.dic.get('year')
		if( y is None ):
			print("missing year for " + self.id )
		else:
			self.year = y


	# field: read from keyword
	def _formatKeyfield(self):
		keywords = self.dic.get('keyword')
		if( keywords is None ):
			print("missing keyword for " + self.id )
			return

		words = keywords.split(',')
		if( len(words) > 1 ):
			if( words[0] == "CT List" ):
				self.field = words[1]
			else:
				self.field = words[0]
			self.field = self.field.strip()

    # set DOI link
	def _formatDOI(self):
		d = self.dic.get('doi')
		if( d is None ):
			print("missing doi for " + self.id )
			return

		self.doi = "http://dx.doi.org/" + d


	# print plain text reference
	def printPlainRef(self):
		out = self.author + ", " + self.title + ", " + self.publication + ", "
		if( self.type == "article" ):
			out += self.vol + "(" + self.no + "): " + self.pages + ", "
		if( self.type == "inproceedings" ):
			out += "pp." + self.pages + ", "
		out += self.year
		out += " (DOI: " + self.doi + ", field: " + self.field + ")"
		print(out)


	# print ourput data
	# bib_id | type | year | autohr | title | publication | vol | no | pages | field | doi
	# return str
	def Data(self):
		data = (self.id + "|" + self.type + "|" + self.year + "|" + 
			self.author + "|" + self.title + "|" + self.publication + "|" +
			self.vol + "|" + self.no + "|" + self.pages + "|" +
			self.field + "|" + self.doi + "\n")
		return data
