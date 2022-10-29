from selenium import webdriver
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

#Refer File
refer_file = 'academic.txt'
slack_channel = 'test'
detecting_website = 'http://www.sogang.ac.kr/front/boardlist.do?bbsConfigFK=2'
domain='https://www.sogang.ac.kr'

#Selenium options
chrome_options = webdriver.ChromeOptions()
ua = UserAgent()
userAgent = ua.random
chrome_options.add_argument('--headless')
chrome_options.add_argument(f'user-agent={userAgent}')

driver = webdriver.Chrome(executable_path="/home/ec2-user/chromedriver", options=chrome_options)

##3초 기다림
driver.implicitly_wait(3)
driver.get(detecting_website)

## 페이지의 elements 모두 가져오기
html = driver.page_source 
driver.quit()

## BeautifulSoup 적용
soup = BeautifulSoup(html, 'html.parser')

# 첫 번째 공지
latest_notice_html = soup.select_one('tr.notice > td > div > a')
latest_notice = latest_notice_html.text
link = domain+latest_notice_html['href']
with open(refer_file, 'r') as f_read:
    origin_notice = f_read.readline()
    f_read.close()
    print(link) 
    import slack_api
    slack_api.catch_change(slack_channel, latest_notice, link)
