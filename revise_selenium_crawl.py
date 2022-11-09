from selenium import webdriver
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

import os
from dotenv import load_dotenv
load_dotenv()
Chromedriver_path = os.environ.get('WEBDRIVER_PATH')

def read_file(refer_file):
    with open(refer_file, 'r') as f_read:
        all_data = f_read.readline()
        f_read.close()
        print(all_data)
        
def send_msg(slack_channel, text, link):
    import slack_api
    slack_api.catch_change(slack_channel, text, link)

def crawl_all_notices_firstpage(refer_file, slack_channel, detecting_website, notice_board_html_tree, each_notice_html_tree, domain):
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

    ## notice board 공지 모두 가져와서 notices list에 dictionary형태로 저장
    notice_list_html = soup.select_one(notice_board_html_tree)
    notices=[]  #새로 가져온 공지들
    for a in notice_list_html.select(each_notice_html_tree):
        dic = {'title': a.span.text, 'link': a['href']}
        notices.append(dic)
    
    ## 기존 파일 읽어와서 마지막 줄과 비교, 변화 감지
    with open(refer_file, 'r') as f_read:
        #-1은 마지막 공지 링크, -2는 마지막 공지 제목
        origin_last_line = f_read.readlines()[-2]
        f_read.close()
        
        ## 변화 감지 시
        if notices[-1]['title']!=origin_last_line.strip():
            ## 새로 받아온 공지 한 줄씩 읽으면서 기존 파일과 비교(진행중)
            with open(refer_file, 'r') as f_read:
                # 새 공지인지 여부 flag
                is_new_notice = False
                # 크롤링해온 모든 공지에 대해:
                for each_notice in notices:
                    if is_new_notice == False:
                        old_notice = f_read.readline().rstrip()
                        f_read.readline()
                    is_new_notice = False
                    if each_notice['title'] != old_notice:
                        ## 변경된 공지 슬랙 메시지 전송
                        send_msg(slack_channel, each_notice['title'], domain+each_notice['link'])
                        is_new_notice = True
                f_read.close()
                
            ## 파일에 새로 저장
            with open(refer_file, 'w') as f_write:
                for i in notices:
                    f_write.write(i['title'] + '\n')
                    f_write.write(i['link'] + '\n')
                f_write.close()
    
    
    #기존 부분
    
    #print(notice_list_html)
    
    # latest_notice = latest_notice_html.text
    # with open(refer_file, 'r') as f_read:
    #     origin_notice = f_read.readline()
    #     f_read.close()
    #     if origin_notice != latest_notice:
    #         # 공지 게시글 주소 불러와 message 전송
    #         link = domain+latest_notice_html['href']
    #         import slack_api
    #         slack_api.catch_change(slack_channel, latest_notice, link)
    #         #파일에 저장
    #         with open(refer_file, 'w') as f_write:
    #             f_write.write(latest_notice)
    #             f_write.close()
