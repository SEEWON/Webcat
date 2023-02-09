from selenium import webdriver
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

import os
from dotenv import load_dotenv

load_dotenv()
Chromedriver_path = os.environ.get("WEBDRIVER_PATH")

# 일반공지 html tree 형식 # 'tr.notice > td > div > a'
# 학과공지 html tree 형식 # 'div.list_box > ul > li > div > a.title'

detecting_html_tree = "tr.notice > td > div > a"
detecting_website = "https://www.sogang.ac.kr/front/boardlist.do?bbsConfigFK=1"

# Selenium options
chrome_options = webdriver.ChromeOptions()
ua = UserAgent()
userAgent = ua.random
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument(f"user-agent={userAgent}")
chrome_options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(executable_path=Chromedriver_path, options=chrome_options)

# 3초 기다림
driver.implicitly_wait(3)
driver.get(detecting_website)

# 페이지의 elements 모두 가져오기
html = driver.page_source
driver.quit()

# BeautifulSoup 적용, html parsing
soup = BeautifulSoup(html, "html.parser")

# 가장 위 공지 불러오기
latest_notice_html = soup.select_one(detecting_html_tree)
latest_notice = latest_notice_html.text
print(latest_notice_html)
print("\n", latest_notice)
