# 환경 변수의 경로(PATH)에 패키지,모듈을 찾기 위해서 결로 설정을 해주어야 함.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import numpy as np
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

######## 유튜브 댓글 추출
Baseurl = 'https://www.youtube.com/results?search_query='
Plusurl = input("검색 :")
url = Baseurl + quote_plus(Plusurl)
print(url)
#웹 드라이버(chromedriver.exe의 경로를 설정해 주어야 함.)
driver = webdriver.Chrome("C:/Coding/web_crawling/chromedriver.exe")
driver.implicitly_wait(30)
driver.get(url)



# # 동영상 클릭
# driver.find_element_by_css_selector('.style-scope ytd-video-renderer').click() 

# # 유튜브 댓글 페이지 새로고침
# last_page_height = driver.execute_script("return document.documentElement.scrollHeight") 

# while True:
#     driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
#     time.sleep(3.0)
#     new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
   
#     if new_page_height == last_page_height:
#         break
#     last_page_height = new_page_height

# # html_source = driver.page_source

# # soup = BeautifulSoup(html_source, 'lxml')

# youtube_comment = driver.find_elements_by_css_selector('.style-scope ytd-expander')
# youtube_comment_list = []

# for i in youtube_comment:
#     print(i.text)
#     print('\n')
#     youtube_comment_list.append(i.text.strip())


# # print(youtube_comment_list)
# driver.close()

# ####### .xlsx형태로 저장
# raw_data2 = youtube_comment_list
# raw_data3 = pd.DataFrame(raw_data2)
# xlxs_dir = 'comment_youtube.xlsx' # pylint: disable=abstract-class-instantiated
# with pd.ExcelWriter(xlxs_dir) as writer:
#     raw_data3.to_excel(writer, sheet_name='Youtube Comment')


######## 무의미한 글자 추출하기
comment_youtube_xlsx = pd.read_excel('C:/Coding/comment_youtube.xlsx')
from collections import Counter
count = Counter(comment_youtube_xlsx)
common_comment_200 = count.most_common(200)

from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import matplotlib

matplotlib.rcParams['font.family'] = "Malgun Gothic"
font_path = "C:/Windows/Fonts/Century Gothic.ttf"

# denne_mask = np.array(Image.open('cloud.png'))

wc = WordCloud(font_path=font_path, background_color="white", width=800, height=600)#mask = denne_mask) 
cloud = wc.generate_from_frequencies(dict(common_comment_200)) 
plt.figure(figsize = (20, 16)) 
plt.axis('off') 
plt.imshow(cloud)



######## 구글 로그인 후 메일 보내기 자동화
# driver = webdriver.Chrome("C:/Coding/web_crawling/chromedriver.exe")
# url = 'https://www.google.co.kr/'
# driver.implicitly_wait(30)
# driver.get(url)
# action = ActionChains(driver)

# driver.find_element_by_css_selector('gb_70').click() #로그인버튼 클릭
# time.sleep(1) #해당 페이지가 데이터를 처리하는데 걸리는 시간이 있을 수 있으므로 값을 설정해줌.
# action.send_keys('yeodaewon6@gmail.com').perform() #구글아이디 입력
# action.reset_actions()#action들이 중복되는 것을 방지하기 위해서 종료하는 기능.
# driver.find_element_by_css_selector('VfPpkd-vQzf8d').click() #다음버튼 클릭
# action.send_keys('ydwmon0703').perform() #구글비밀번호 입력-(1)
# # driver.find_element_by_css_selector('비밀번호입력클래스').send_keys('google PW') #구글비밀번호 입력-(2)
# driver.find_element_by_css_selector('VfPpkd-vQzf8d').click() #다음버튼 클릭

# # 로그인 후 이메일 창 접속
# url = 'https://mail.google.com/mail/u/0/?ogbl#inbox'
# driver.get(url)

# driver.find_element_by_css_selector('메일쓰기클래스').click()
# time.sleep()

# send_button = driver.find_element_by_css_selector('보내기버튼클래스')
# # move_to_element = 클릭해서 아무일 없는 클릭버튼까지고 클릭가능하게 함.
# # 2초 쉼 
# action.send_keys('받는사람이메일').pause(2).key_down(Keys.TAB).key_down(Keys.TAB)\
#     .send_keys('제목입니다.').key_down(Keys.TAB)\
#         .send_keys('내용입니다.').pasue(2)\
#             .key_down(Keys.SHIFT).send_keys('contents').key_up(Keys.SHIFT)\
#                 .move_to_element(send_button).click().perform()





# 더보기 계속 클릭하기
# while True:
#     try:
#         더보기 = driver.find_element_by_css_selector('a.u_cbox_btn_more')
#         더보기.click()
#         time.sleep(1)
#     except:
#         break



######## 네이버 댓글추출
# naver_댓글_list = []

# contents = driver.find_elements_by_css_selector('span.u_cbox_contents')
# for content in contents:
#     print(content.text)
#     print('\n')
#     naver_댓글_list.append(content.text.strip())

# print(naver_댓글_list)
# driver.close()

########.txt 형태로 저장
# file = open('data.txt', 'w', encoding='utf-8')

# for content in naver_댓글_list:
#      naver_댓글_list.write(content + '\n')

# file.close

######## .xlsx형태로 저장
# raw_data = naver_댓글_list
# raw_data1 = pd.DataFrame(raw_data)
# xlxs_dir = 'sample.xlsx'
# with pd.ExcelWriter(xlxs_dir) as writer:
#     raw_data1.to_excel(writer)

