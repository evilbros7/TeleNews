import requests
from bs4 import BeautifulSoup

def arena():
	url = "https://www.gsmarena.com/news.php3"
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	cl = soup.findAll(class_='news-item')
	
	txt=cl.text
	#print(txt)
	cl=txt.split("\n\n\n\n\n\n\n\n")
	
	List = []
	for i in cl:
		#print(i.text)
		List.append("\n\n🌐")
		List.append(i)


	return List
