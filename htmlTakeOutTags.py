# -*- coding: utf-8 -*-

def Remove(text,fro):
	if text.find("<",fro)==-1:
		return text
	ind1=text.find("<",fro)
	ind2=text.find(">",ind1+1)
	text=text[0:fro]+text[fro:ind1]+text[ind2+1:]
	return Remove(text,ind1)


