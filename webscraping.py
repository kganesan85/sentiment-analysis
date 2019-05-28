from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import selenium
import requests
import bs4
import time
import pandas as pd


li  = []
driver = selenium.webdriver.Chrome(executable_path='/home/clustrex-22/Downloads/chromedriver_linux64/chromedriver')
driver.get('http://results.eci.gov.in/pc/en/constituencywise/ConstituencywiseU011.htm?ac=1')
for i in range(1,37):
    obj = Select(driver.find_element_by_id('ddlState'))
    obj.select_by_index(i)
    for  j in range(1,ind[i]+1):
        print(i,j)
        obj1 = Select(driver.find_element_by_id('ddlAC'))
        obj1.select_by_index(j)
        html = driver.page_source
        #print(html)
        soup = bs4.BeautifulSoup(html,'html.parser')
        #soup.prettify()
        for con in soup.find_all('th',attrs={"align":"center","colspan":"9"}):
            if '-' in con.text.strip():
                cons = con.text.strip().split('-')[1]
                sta = con.text.strip().split('-')[0]
        print(cons)
        for k in soup.find_all('tr',attrs={"style":"font-size:12px;"}):
            li_1 = []
            for l in k.findAll('td'):
                li_1.append(l.text)
            li_1.append(sta)
            li_1.append(cons)
            li.append(li_1)
result = pd.DataFrame(li)

