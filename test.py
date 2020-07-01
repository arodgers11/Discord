import pandas as pd
import requests
import numpy as np
import math
import matplotlib
from bs4 import BeautifulSoup

profile=requests.get('https://playoverwatch.com/en-us/career/pc/arodgers-11140#competitive')
soup=BeautifulSoup(profile.text,'html.parser')

mydivs = soup.findAll("div", {"class": "competitive-rank-section"})
comp_rank=['']*3
for i in [1,2,3]:
    comp_rank[i-1]=mydivs[2*i-1].findAll("div",{"class":"competitive-rank-level"})
