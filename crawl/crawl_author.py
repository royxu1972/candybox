#!
# coding: UTF-8
# crawl author's institution and mail from goolge scholar

import urllib.request
import bs4
import random

class CrawlAuthor:

	def __init__(self):
		self.author_list = []

	# pre-process, remove middle name
	def pre_process(self, author):
		temp = author.split(" ")
		return temp[0] + " " + temp[len(temp)-1]

	# crawl
	def search_author(self, author):
		tp = self.pre_process(author).split(' ')
		ar = "+".join(tp)
		print("search " + ar + " in google scholar ...")
		url = "http://scholar.google.com/citations?hl=en&view_op=search_authors&mauthors=" + ar

		user_agents = (['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0', 
         'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
         'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ (KHTML, like Gecko) Element Browser 5.0', 
         'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)', 
         'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)', 
         'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14', 
         'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25',
         'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36', 
         'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)'])
		user_agent = user_agents[random.randint(0, 9)]
		headers = {'User-Agent':user_agent}

		req = urllib.request.Request(url, None, headers)
		resp = urllib.request.urlopen(req, None,10)
		html = resp.read()

		#print(html)

		#html = html.decode('utf-8').encode('gbk')
		#html = html.replace(u'\xa0',u'')
		#print(type(html))

		# soup
		soup = bs4.BeautifulSoup(html,from_encoding="gbk")
		#print(soup.prettify("gbk"))

		'''
		<td>
			<a>name</a>
			institution<br/>
			verified email<br/>
		</td>
		'''
		# return value
		author_dic = {}
		# try to get
		na = soup.find_all("a", class_="cit-dark-large-link")
		# if there exist more, or nothing, then no information
		if( len(na) > 1 or len(na) == 0 ):
			author_dic["name"] = author
			author_dic["institution"] = ""
			author_dic["mail"] = ""
		else:
			na = soup.find("a", class_="cit-dark-large-link")
			top = na.parent # get the parent
			temp = [] # format information
			for each in top:
				if( type(each) != type(na) ):
					temp.append(each.string.encode("utf-8","ignore").decode("utf-8"))
				else:
					temp.append(each.get_text().encode("utf-8","ignore").decode("utf-8"))
			#print(temp)

			author_dic["name"] = author
			author_dic["institution"] = temp[2]

			s = temp[3]
			s = s[18:len(s)]
			s = s[0:s.find("Cite")]
			s = "@" + s
			author_dic["mail"] = s

		return author_dic


	# execute
	def execute(self, in_file, out_file):
		with open(in_file, 'r') as infile:
			for line in infile:
				line = line.strip("\n")
				item = self.search_author(line)
				self.author_list.append(item)

		# write
		with open(out_file, 'w') as outfile:
			for each in self.author_list:
				o = each["name"] + "|" + each["institution"] + "|" + each["mail"] + "\r\n"
				o = o.encode('utf-8').decode("ascii","ignore")
				outfile.writelines( o )

#
c = CrawlAuthor()
c.execute("authorlist.txt","out.txt")


