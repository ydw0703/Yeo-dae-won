# 환경 변수의 경로(PATH)에 패키지,모듈을 찾기 위해서 결로 설정을 해주어야 함.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import numpy as np
from urllib.parse import quote_plus
from bs4 import BeautifulSoup


Baseurl = 'https://programmers.co.kr/job?job_position%5Btags%5D%5B%5D=Python'
url = Baseurl
print(url)
#웹 드라이버(chromedriver.exe의 경로를 설정해 주어야 함.)
driver = webdriver.Chrome("C:/Coding/web_crawling/chromedriver.exe")
driver.implicitly_wait(30)
driver.get(url)

jobneeds_requirements_list = []
jobneeds_preference_list = []

clicklist = driver.find_element_by_xpath('//*[@id="list-positions-wrapper"]/ul/li[1]/div[2]/h5/a').click()
jobneeds_requirements = driver.find_elements_by_css_selector('section.section-requirements > div > div > ul > li')
jobneeds_preference = driver.find_elements_by_css_selector('section.section-preference > div > div > ul> li')
backclick = driver.find_element_by_xpath('/html/body/div[1]/div/ul[1]/li[2]/a').click() #뒤로가기 
for k in range(1,):
    clicklist

    for i in jobneeds_requirements:
        print(i.text)
        print('\n')
        print(jobneeds_requirements_list.append(i.text.strip()))

    for j in jobneeds_preference:
        print(j.text)
        print('\n')
        print(jobneeds_preference_list.append(j.text.strip()))
    
    backclick
    
# print(jobneeds_requirements)




# driver.find_element_by_xpath('//*[@id="list-positions-wrapper"]/ul/li[2]/div[2]/h5/a').click()

# jobneeds_requirements = driver.find_elements_by_css_selector('section.section-preference > div > div > ul > li')
# jobneeds_requirements_list = []
# jobneeds_preference = driver.find_elements_by_css_selector('section.section-preference > div > div > ul> li')
# jobneeds_preference_list = []

# for i in jobneeds_requirements:
#     print(i.text)
#     print('\n')
#     jobneeds_requirements_list.append(i.text.strip())

# for j in jobneeds_preference:
#     print(j.text)
#     print('\n')
#     jobneeds_preference_list.append(j.text.strip())

# print(jobneeds_requirements)


# #뒤로가기
# go_back = driver.find_element_by_xpath('/html/body/div[1]/div/ul[1]/li[2]/a').click()

   
driver.close()

raw_data3 = pd.DataFrame(
    {
        '자격조건' : jobneeds_requirements_list,
        '우대조건' : jobneeds_preference_list
    })

xlxs_dir = 'jobneeds1.xlsx'
# with pd.ExcelWriter(xlxs_dir) as writer:
raw_data3.to_excel('jobneeds1.xlsx', sheet_name='조건')



