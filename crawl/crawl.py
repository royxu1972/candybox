#!
# coding: UTF-8
# crawl test

import urllib.request
import bs4

class Crawl:
	search_str = ""
	def __init__(self, str):
		self.search_str = str


	def execute(self):
		print("search in IEEE explore...")
		url = "http://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=search+based+Combinatorial+Testing"
		url_prefix = "http://ieeexplore.ieee.org"
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

		req = urllib.request.Request(url, None, headers)
		resp = urllib.request.urlopen(req, None, 5)
		html = resp.read()
		#print(html)

		#html = html.decode('utf-8').encode('gbk')
		#html = html.replace(u'\xa0',u'')
		#print(type(html))

		# soup
		soup = bs4.BeautifulSoup(html)
		#print(soup.prettify("gbk"))

		# <h3>paper title</h3>
		for link in soup.find_all("h3"):
			text = link.get_text().strip()

			# get new url <a href="">...</a>
			if(text == self.search_str):
				#print(link.a.get("href"))
				url_new = url_prefix + link.a.get("href")
				break

		# go to new page
		print("go to the paper page...")
		req = urllib.request.Request(url_new, None, headers)
		resp = urllib.request.urlopen(req, None, 5)
		html = resp.read()

		# soup
		soup = bs4.BeautifulSoup(html)

		# find information
		paper_pub = soup.find(attrs={"name": "citation_conference"})
		print(paper_pub)



#
c = Crawl("Search Based Combinatorial Testing")
c.execute()