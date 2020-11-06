import requests
from bs4 import BeautifulSoup
from sites import (gadgetsndtv,livemint,indiatoday,indianexpress,zeenews,beebom,arena)
import telebot # pyTelegramBotAPI library
import pyfiglet

print("\n")
banner = pyfiglet.figlet_format('TELE-NEWS')
print(banner)
print("Welcome to TechNews posting bot for telegram! by t.me/pvxtechnews <3 \n")

f=open("data.txt",'r')
data=f.readline()
data=eval(data)
bot_token=data["token"]
chat_tag=data["tag"]
msg=data["msg"]
f.close()

bot = telebot.TeleBot(token=bot_token)

site=input("[Note: GadgetsNdtv is best]\nEnter 1 to get Technews from GadgetsNdtv\nEnter 2 to get TechNews from LiveMint\nEnter 3 to get Technews from IndiaToday\nEnter 4 to get Technews from IndianExpress\nEnter 5 to get Technews from zeenews\nEnter 6 to get Technews from beenews\nEnter 7 to get Technews from Gsmarena\nEnter Choice:-")

if(site=='1'):
	print("\nCREATING TECH NEWS FROM GADGETSNDTV !\n")
	List=gadgetsndtv.ndtv()
	
elif(site=='2'):
	print("\nCREATING TECH NEWS FROM LIVEMINT !\n")
	List=livemint.mint()
	
elif(site=='3'):
	print("\nCREATING TECH NEWS FROM INDIATODAY !\n")
	List=indiatoday.today()
	
elif(site=='4'):
	print("\nCREATING TECH NEWS FROM INDIANEXPRESS !\n")
	List=indianexpress.express()

elif(site=='5'):
	print("\nCREATING TECH NEWS FROM ZEENEWS !\n")
	List=zeenews.zee()
	
elif(site=='6'):
	print("\nCREATING TECH NEWS FROM ZEENEWS !\n")
	List=beebom.bom()
	
elif(site=='7'):
	print("\nCREATING TECH NEWS FROM ZEENEWS !\n")
	List=gsm.arena()
	
else:
	print("\nWrong Choice! Exit")
	exit()

List.insert(0,'☆☆☆☆💥 𝗧𝗲𝗰𝗵 𝗡𝗲𝘄𝘀 𝗕𝘆 𝗘𝗩𝗜𝗟𝗭𝗢𝗡𝗘 💥☆☆☆☆')
List.append("\n\n"+msg)
#print(List)
text = " ".join(List)
print(text)

print("\n------------------------")
ch=input(f"ENTER 1 TO SEND ABOVE TECH NEWS TO GROUP LINK TAG or id: {chat_tag} or ENTER ANY OTHER CHARACTER NOT TO SEND! :")
if(ch=='1'):
	try:
		bot.send_message(chat_tag,text)
		print("\nTECH NEWS POSTED :) !!")
	except:
		print("Something is wrong!!!!!!! (maybe token or chat link tag is not correct!")

else:
		print("\nNot Posted :( !!")
		
