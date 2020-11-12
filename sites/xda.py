import requests
from bs4 import BeautifulSoup as bs

def xdaa():
	url="https://www.xda-developers.com/category/xda-news/"
	response=requests.get(url)
		

	soup=bs(response.content,"html.parser")
	headings=soup.findAll("h4")

	count=0
	newsList=[]
	for heading in headings:
		count+=1
		newsList.append("\n\n🌐")
		newsList.append(heading.text)
		if count==15:
			break

	return newsList
