import selenium_crawl

def exec_batch():
  refer_file = 'general.txt'
  slack_channel = '일반공지'
  detecting_website = 'https://www.sogang.ac.kr/front/boardlist.do?bbsConfigFK=1'
  detecting_html_tree = 'tr.notice > td > div > a'
  domain='https://www.sogang.ac.kr'
  selenium_crawl.crawl_site(refer_file, slack_channel, detecting_website, detecting_html_tree, domain)