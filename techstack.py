# -*- encoding: utf-8 -*-
import os
import pandas as pd
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "https://programmers.co.kr/job"
link ="https://programmers.co.kr"
TechStacks = []
TSdict = {}

for i in range(1,35):
    html = urlopen(url + "?page=" + str(i))
    bsObject = BeautifulSoup(html, "html.parser")
    div = bsObject.find_all("div", {"class":"item-body"})
    for item in div:
        a = item.find("h5",{"class":"position-title"}).find("a")["href"]
        html = urlopen(link + a)
        bsObject = BeautifulSoup(html, "html.parser")
        print(i)
        techstack = bsObject.find("tr",{"class":"heavy-use"})
        if(not techstack):
            continue
        techstack = techstack.find("td").find_all("code")
        for tech in techstack:
            tech = tech.text
            if not tech in TechStacks:
                TechStacks.append(tech)
                TSdict[tech] = 1
            else:
                TSdict[tech] += 1

ts = pd.DataFrame(TSdict.values(),TSdict.keys())
ts.to_csv("TechStack_dict.csv")