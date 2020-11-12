import requests
from bs4 import BeautifulSoup as bs

def xdaa():
 url="https://www.xda-developers.com/category/xda-news/"
 response=requests.get(url)
  

 soup=bs(response.content,"html.parser")
 headings=soup.findAll("div",class_="item_content")

 count=0
 newsList=[]
 for heading in headings:
  count+=1
  newsList.append("\n\n🌐")
  newsList.append(heading.a.text)
  if count==30:
   break
   
 return newsList
 
List=xdaa()
#print(List)
List.insert(0,'☆☆☆☆☆💥 Tech News 💥☆☆☆☆☆')
#print(List)
text = " ".join(List)
print(text)
