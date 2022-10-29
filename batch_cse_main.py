import selenium_crawl

def exec_batch():
  refer_file = 'cse_main.txt'
  slack_channel = '컴퓨터공학과_주요공지'
  detecting_website = 'https://scc.sogang.ac.kr/front/cmsboardlist.do?siteId=cs&bbsConfigFK=1905'
  detecting_html_tree = 'div.list_box > ul > li > div > a.title'
  domain='https://scc.sogang.ac.kr'
  selenium_crawl.crawl_site(refer_file, slack_channel, detecting_website, detecting_html_tree, domain)