#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 18:31:48 2020

@author: Shaliq
"""

import requests
from bs4 import BeautifulSoup
page=requests.get("http://vikaspedia.in/agriculture/national-schemes-for-farmers/soil-health-soil-conservation-and-fertilizers")
soup=BeautifulSoup(page.content,'html.parser')
week=soup.find(id="parent-fieldname-title")
t1=soup.find(class_="documentEditable")
tb=soup.find('table','grid listing')
title=list()
arr=list()
count=int()
for i in tb.find_all('b'):
    title.append(i.get_text())
    print(i.get_text(),end='*****')
for i in tb.find_all('tr'):
    count=1
    subarr=list()
    for j in i.find_all('td'):
        count+=1
        if(count<=4):
            print(j.get_text(),end="  ++  ")
            subarr.append(j.get_text())
    arr.append(subarr)
    ##subarr.clear()
    print()    
    