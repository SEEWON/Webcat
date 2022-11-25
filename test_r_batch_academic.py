import selenium_crawl_v_02
import sys
import os

refer_file = 'webcat/top_notices/test_notices.txt'
slack_channel = 'dev-feature'
detecting_website = 'http://www.sogang.ac.kr/front/boardlist.do?bbsConfigFK=2'
notice_board_html_tree = 'div.grid.bbs-list.tr-hover'
each_notice_html_tree = 'div.subject > a'
domain = 'https://www.sogang.ac.kr'

selenium_crawl_v_02.crawl_all_notices_firstpage(
    refer_file, slack_channel, detecting_website, notice_board_html_tree, each_notice_html_tree, domain)
