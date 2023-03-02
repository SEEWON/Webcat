from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from fake_useragent import UserAgent
import datetime
import time

from dotenv import load_dotenv

import slack_api

#! 슈퍼루키의 경우, 공고가 올라온 날짜 정보가 표시되지 않으므로 아래 #!로 표시된 로직 변경
#################### Detecting Site에 따른 변경부 ####################
# slack_channel = "l-슈퍼루키-인턴공고"
slack_channel = "zz-dev-feature"
detecting_website = (
    "https://www.superookie.com/jobs?job_level%5B%5D=579f18168b129f673b4efebe"
)
detecting_interval = 60

xpath_list = []
for i in range(1, 21):
    notice = {
        "company": f"/html/body/div[1]/div[4]/section/div[1]/div[3]/div/div[2]/div[{i}]/div/a/div/div[2]/div/div[1]/div/h5",
        "job_title": f"/html/body/div[1]/div[4]/section/div[1]/div[3]/div/div[2]/div[{i}]/div/a/div/div[2]/div/p",
        "link": f"/html/body/div[1]/div[4]/section/div[1]/div[3]/div/div[2]/div[{i}]/div/a",
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

# Initialize: Use gloabl variable
old_notices = []
new_notices = []


#! 상위 20건 crawl
def crawl_today_notices():
    new_notices.clear()
    for each_xpath in xpath_list:
        #! 날짜 비교하지 않음
        company = driver.find_element(By.XPATH, each_xpath["company"]).text
        job_title = driver.find_element(By.XPATH, each_xpath["job_title"]).text
        link = driver.find_element(By.XPATH, each_xpath["link"]).get_attribute("href")
        notice = {"company": company, "job_title": job_title, "link": link}
        new_notices.append(notice)


def detect_changed_notices():
    for new_notice in new_notices:
        if new_notice not in old_notices:
            slack_api.notify_change_detected(
                slack_channel,
                new_notice["company"],
                new_notice["job_title"],
                new_notice["link"],
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
