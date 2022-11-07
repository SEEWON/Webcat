from selenium import webdriver
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

import os
from dotenv import load_dotenv
load_dotenv()
Chromedriver_path = os.environ.get('WEBDRIVER_PATH')

def crawl_site(refer_file, slack_channel, detecting_website, detecting_html_tree, domain):
    #Selenium options
    chrome_options = webdriver.ChromeOptions()
    ua = UserAgent()
    userAgent = ua.random
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(f'user-agent={userAgent}')
    # chrome_options.add_argument('--remote-debugging-port=9222')

    driver = webdriver.Chrome(executable_path=Chromedriver_path, options=chrome_options)

    ##3초 기다림
    driver.implicitly_wait(3)
    driver.get(detecting_website)

    ## 페이지의 elements 모두 가져오기
    html = driver.page_source 
    driver.quit()

    ## BeautifulSoup 적용, html parsing
    soup = BeautifulSoup(html, 'html.parser')

    # 가장 위 공지 불러오기
    latest_notice_html = soup.select_one(detecting_html_tree)
    latest_notice = latest_notice_html.text
    with open(refer_file, 'r') as f_read:
        origin_notice = f_read.readline()
        f_read.close()
        if origin_notice != latest_notice:
            # 공지 게시글 주소 불러와 message 전송
            link = domain+latest_notice_html['href']
            import slack_api
            slack_api.catch_change(slack_channel, latest_notice, link)
            #파일에 저장
            with open(refer_file, 'w') as f_write:
                f_write.write(latest_notice)
                f_write.close()
