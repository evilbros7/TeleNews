import requests
from bs4 import BeautifulSoup

def xnews():
	url = "https://cyware.com/hacker-news"
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	cl = soup.findAll(class_='cursor-pointer')
	
	txt=cl[0].text
	#print(txt)
	cl=txt.split("\n\n\n\n\n\n\n\n")
	
	List = []
	for i in cl:
		#print(i.text)
		List.append("\n\n🌐")
		List.append(i)

	List[1]=List[1].replace("\n\n\n\n\n\n\n","")
	return List
