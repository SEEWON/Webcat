import os
import sys
import selenium_crawl
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

def exec_batch():
  refer_file = 'webcat/top_notices/t_notice_scholarship.txt'
  slack_channel = '장학공지'
  detecting_website = 'https://www.sogang.ac.kr/front/boardlist.do?bbsConfigFK=141'
  detecting_html_tree = 'tr.notice > td > div > a'
  domain='https://www.sogang.ac.kr'
  selenium_crawl.crawl_site(refer_file, slack_channel, detecting_website, detecting_html_tree, domain)