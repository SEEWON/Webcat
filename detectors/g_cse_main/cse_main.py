from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from fake_useragent import UserAgent
import datetime
import time

from dotenv import load_dotenv

import slack_api

#################### Detecting Site에 따른 변경부 ####################
slack_channel = "g-컴퓨터공학-주요공지"
detecting_website = (
    "https://scc.sogang.ac.kr/front/cmsboardlist.do?siteId=cs&bbsConfigFK=1905"
)
detecting_interval = 60

xpath_list = []
for i in range(1, 43):
    notice = {
        "title": f"/html/body/div/div[4]/div[2]/div[4]/div/div/ul/li[{i}]/div/a",
        "registered_date": f"/html/body/div/div[4]/div[2]/div[4]/div/div/ul/li[{i}]/div/div/span[2]",
    }
    xpath_list.append(notice)
#################### Detecting Site에 따른 변경부 ####################

load_dotenv()


# Selenium options
chrome_options = webdriver.ChromeOptions()
ua = UserAgent()
userAgent = ua.random
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument(f"user-agent={userAgent}")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=chrome_options
)

# 3초 기다림
driver.implicitly_wait(3)
driver.get(detecting_website)

# UTC+9 Timezone에서의 오늘 날짜 formatting
date_today = (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).strftime(
    "%Y.%m.%d"
)

# Initialize: Use gloabl variable
old_notices = []
new_notices = []


# 오늘 등록된 공지만 crawl
def crawl_today_notices():
    new_notices.clear()
    for each_xpath in xpath_list:
        notice_date = driver.find_element(By.XPATH, each_xpath["registered_date"]).text
        if notice_date == date_today:
            notice_title = driver.find_element(By.XPATH, each_xpath["title"])
            notice = {
                "title": notice_title.text,
                "link": notice_title.get_attribute("href"),
            }
            new_notices.append(notice)


def detect_changed_notices():
    for new_notice in new_notices:
        if new_notice not in old_notices:
            slack_api.notify_change_detected(
                slack_channel, new_notice["title"], new_notice["link"]
            )


# Initialize: update old_notices at Script execution point
crawl_today_notices()
old_notices = new_notices.copy()

try:
    slack_api.notify_started(slack_channel)

    # 반복 실행
    while True:
        # 오늘 올라온 공지 detect
        crawl_today_notices()

        # 기존 공지-새 공지 비교
        detect_changed_notices()

        # 저장하고 있던 공지 업데이트
        old_notices = new_notices.copy()

        # 1분 후 다시 실행
        time.sleep(detecting_interval)
        driver.refresh()

finally:
    driver.quit()
    slack_api.notify_terminated(slack_channel)
