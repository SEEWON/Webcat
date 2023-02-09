def testing():
    # 컴퓨터공학과 주요공지 웹캣
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from fake_useragent import UserAgent

    import os
    from dotenv import load_dotenv

    load_dotenv()
    Chromedriver_path = os.environ.get("WEBDRIVER_PATH")

    # Refer File
    slack_channel = "log-working"
    detecting_website = (
        "https://scc.sogang.ac.kr/front/cmsboardlist.do?siteId=cs&bbsConfigFK=1905"
    )
    domain = "https://scc.sogang.ac.kr"

    # Selenium options
    chrome_options = webdriver.ChromeOptions()
    ua = UserAgent()
    userAgent = ua.random
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(f"user-agent={userAgent}")

    driver = webdriver.Chrome(executable_path=Chromedriver_path, options=chrome_options)

    # 3초 기다림
    driver.implicitly_wait(3)
    driver.get(detecting_website)

    # 페이지의 elements 모두 가져오기
    html = driver.page_source
    driver.quit()

    # BeautifulSoup 적용
    soup = BeautifulSoup(html, "html.parser")

    # 첫 번째 공지
    latest_notice_html = soup.select_one("div.list_box > ul > li > div > a.title")
    import slack_api
    from datetime import datetime

    timestamp = datetime.now().strftime("%H:%M:%S %Y-%m-%d")
    if latest_notice_html:
        slack_api.post_message(slack_channel, f"_{timestamp}_ 데몬과 셀레니움이 일하고 있어요!\n")
    else:
        slack_api.post_message(slack_channel, f"<!channel> _{timestamp}_ 셀레니움 장애 발생\n")
