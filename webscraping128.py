######### PROJETO C-128 AQUI #########
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd 
import requests


start_url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"


page= requests.get(start_url) 
soup=BeautifulSoup(page.content, "html.parser")

star_table= soup.find_all("table", {"class": "wikitable sortable"})

total_table=len(star_table)

temp_list=[]

table_rows= star_table[1].find_all("tr")

for tr in table_rows:
    td= tr.find_all("td")
    row= [i.text.rstrip()for i in td]
    temp_list.append(row)

star_names=[]
distance=[]
mass=[]
radius=[]

for i in range(1,len(temp_list)):
        star_names= temp_list[i][0]
        distance= temp_list[i][5]
        mass= temp_list[i][8]
        radius= temp_list[i][9]

headers= ["Star_name", "Distance", "Mass", "Radius"]      

df2= pd.DataFrame(list(zip(star_names, distance, mass, radius)), columns=headers)

df2.to_csv("dwarf_stars.csv", index=True, index_label="id")

######### PROJETO C-128 TERMINA AQUI #########



