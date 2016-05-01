#!/usr/bin/python
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import re
import random
import datetime

#try:
#	html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
#except HTTPError as e:
#	print(e)
#if html is None:
#	print("URL is not found")
#else:
#	bsObj = BeautifulSoup(html, "html.parser")
	#nameList = bsObj.findAll("span",{"class":"green"})
	#for name in nameList:
	#	print(name.get_text())
#	links = bsObj.findAll("a")
#	for link in links:
#		if 'href' in link.attrs:
#			print(link.attrs['href'])
#random.seed(datetime.datetime.now())
pages = set()
def getLinks(domain,dir):
	global pages
	html = urlopen("domain")
	bsObj = BeautifulSoup(html, "html.parser")
	#try:
		
	#except AttributeError:
		#print ("This page is missing something! no worries its taken care of")
	#links = bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki)((?!:).)*$"))
	#for link in links:
	#	print(link.attrs['href'])
	for link in bsObj.findAll("a",href=re.compile("^(/en-gb/)")):
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newPage = link.attrs['href']
				print("-----------------\n"+newPage)
				pages.add(newPage)
				getLinks(domain+newPage)

getLinks("","")
print (len(pages))




		