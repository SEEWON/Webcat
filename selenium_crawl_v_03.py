"""
Selenium_crawl_v_03
v_02에서 발생하는 아래 이슈 개선
1) 공지 위치가 TOP -> 일반공지로 수정되는 경우
2) 공지 제목이 수정되는 경우
3) 공지가 삭제되는 경우
변경된 공지 이후 모든 공지들 새 공지로 인식
"""

from selenium import webdriver
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

import os
import itertools
from dotenv import load_dotenv

load_dotenv()
Chromedriver_path = os.environ.get("WEBDRIVER_PATH")


def send_msg(slack_channel, text, link):
    import slack_api

    slack_api.catch_change(slack_channel, text, link)


def crawl_all_notices_firstpage(
    refer_file,
    slack_channel,
    detecting_website,
    notice_board_html_tree,
    each_notice_html_tree,
    domain,
):
    # Selenium options
    chrome_options = webdriver.ChromeOptions()
    ua = UserAgent()
    userAgent = ua.random
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f"user-agent={userAgent}")

    driver = webdriver.Chrome(executable_path=Chromedriver_path, options=chrome_options)

    # 3초 기다림
    driver.implicitly_wait(3)
    driver.get(detecting_website)

    # 페이지의 elements 모두 가져오기
    html = driver.page_source
    driver.quit()

    # BeautifulSoup 적용, html parsing
    soup = BeautifulSoup(html, "html.parser")

    # notice board 공지 모두 가져와서 notices list에 dictionary 형태로 저장
    notice_list_html = soup.select_one(notice_board_html_tree)

    # 새로 가져온 공지들
    notices = []
    for a in notice_list_html.select(each_notice_html_tree):
        dic = {"title": a.span.text.rstrip(), "link": a["href"].rstrip()}
        notices.append(dic)

    # 기존 파일 읽어와서 변화 감지
    with open(refer_file, "r") as f_read:
        # 기존 파일 old_notices에 dictionary 형태로 저장
        old_notices = []
        for line in f_read:
            old_dic = {"title": line.rstrip(), "link": f_read.readline().rstrip()}
            old_notices.append(old_dic)
        f_read.close()

        # O(n)으로 한 줄씩 내려가면서 변화 감지
        changed = False
        for i, (notice, old_notice) in enumerate(zip(notices, old_notices)):
            # 게시글 삭제되기만 한 경우 예외 처리
            # 중간 게시글 삭제 시 notice board 끝에 이전 공지 끌올
            # 끝 2개 정도는 검사 제외
            # 추후 공지 날짜 확인 등 로직으로 개선
            if 2 >= len(notices) - i:
                continue
            if notice["title"] != old_notice["title"]:
                changed = True

        # 변화 감지 시
        if changed == True:
            for notice in notices:
                updated = True
                for old_notice in old_notices:
                    if notice["title"] == old_notice["title"]:
                        updated = False
                        break
                # 새 공지와 일치하는 기존 공지가 없을 경우 메시지 전송
                if updated == True:
                    send_msg(slack_channel, notice["title"], domain + notice["link"])

            # 파일에 새로 받아온 공지들 모두 저장
            with open(refer_file, "w") as f_write:
                for notice in notices:
                    f_write.write(notice["title"] + "\n")
                    f_write.write(notice["link"] + "\n")
                f_write.close()
