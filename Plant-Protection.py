#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 19:45:48 2020

@author: apple
"""


import requests
from bs4 import BeautifulSoup
page=requests.get("http://vikaspedia.in/agriculture/national-schemes-for-farmers/plant-protection")
soup=BeautifulSoup(page.content,'html.parser')
week=soup.find(id="parent-fieldname-title")
t1=soup.find(class_="documentEditable")
tb=soup.find('table','grid listing')
title=list()
arr=list()
count=int()
temp=int()
for i in tb.find_all('b'):
    title.append(i.get_text())
    count+=1
    print(i.get_text(),end='*****')
temp=count    
for i in tb.find_all('tr'):
    subarr=list()
    count=temp
    for j in i.find_all('td'):
        count-=1
        if(count>=0):
            print(j.get_text(),end="  ++  ")
            subarr.append(j.get_text())
    arr.append(subarr)
    ##subarr.clear()
    print()    
    