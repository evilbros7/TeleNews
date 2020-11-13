import requests
from bs4 import BeautifulSoup as bs

def gsm():
	url="https://www.gsmarena.com/news.php3"
	response=requests.get(url)

	soup=bs(response.content,"html.parser")
	headings=soup.findAll("h3")

	count=0
	newsList=[]
	for heading in headings:
		count+=1

		if count==15:
			break

		#if count==11:
			#List.append("\n\n🌐 Join @premiumcoursesdrive for daily tech news !")
		
		newsList.append("\n\n🌐")
		newsList.append(heading.text)

	return newsList
