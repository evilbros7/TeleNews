import requests
from bs4 import BeautifulSoup

def arena():
	url = 'https://www.gsmarena.com/news.php3'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	cl = soup.findAll(class_='news-item')

	#print(cl[1])
	#print(cl[1].a.get('title'))
	List = []
	
	count=0 #to get only top 15 news
	for i in cl:
		#print(i.a.get('title'))
		count=count+1
		if(count==15):
			break
		#if(count==11):
			#List.append("\n\n🌐 Join @pvxtechnews for daily tech news !")

		List.append("\n\n🔅")
		List.append(i.a.get('title'))
	return List

