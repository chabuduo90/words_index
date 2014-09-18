# -*- coding: utf-8 -*-

import urllib,htmlTakeOutTags

startingUrl="http://ie.u-ryukyu.ac.jp/~e125716/"

#html=urllib.urlopen(url).read()
toCheck=[""]
checked=[]

def getLink(html,i,list):
	if html.find("<a href",i)==-1:
		return list
	ind1=html.find("<a href",i)+9
	ind2=html.find('"',ind1+1)
	list.append(html[ind1:ind2])
	return getLink(html,ind2,list)

def removeNonLocal(list):
	toRemove=[]
	for i in list:
		if i.find("http://") !=-1 or i.find("https://") !=-1 or i.find(".html") ==-1:
			toRemove.append(i)
	for i in toRemove:
		list.remove(i)
	return list




allHtml=""
while len(toCheck)!=0:
	url=startingUrl+toCheck.pop()
	if url in checked:
		continue
	checked.append(url)
	try:
		html=urllib.urlopen(url).read().lower()
		localLinks=removeNonLocal(getLink(html,0,[]))
		toCheck.extend(localLinks)
		allHtml+=html
	except:
		continue
	
t=htmlTakeOutTags.Remove(allHtml,0)
t=t.decode('utf8').replace(u" ", u"")
#t.replace(u"\n", u"")
print t
	



