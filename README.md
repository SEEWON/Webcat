# Webcat - 서강대 전 공지 수신기
서강대학교 공식 홈페이지에 새로운 공지사항이 등록되면, 1분 안에 알려주는 Slack 봇입니다.

2022년 11월부터 2023년 10월까지 **1년간 운영**했습니다.

2023년 11월 온프레미스 서버 가동을 중지함에 따라 **운영을 중단**했고, 종료일 기준 137명의 활성 유저가 있었습니다.


---
웹캣은 [AWS](https://aws.amazon.com/pm/ec2/)의 EC2 인스턴스, [GCP](https://cloud.google.com/)의 VM 인스턴스를 거쳐 현재는 개인 온프레미스 서버에서 운영 중입니다. <br>
[Docker](https://www.docker.com/) 컨테이너 기반으로 동작하며, [Python](https://www.python.org/)과 [Selenium](https://www.selenium.dev/), [Chrome](https://www.google.co.kr/chrome)으로 이루어져 있습니다.


현재 지원하고 있는 채널은 아래와 같습니다.
- [서강대학교 일반공지](http://www.sogang.ac.kr/front/boardlist.do?bbsConfigFK=1)
- [서강대학교 장학공지](https://www.sogang.ac.kr/front/boardlist.do?bbsConfigFK=141)
- [서강대학교 학사공지](http://www.sogang.ac.kr/front/boardlist.do?bbsConfigFK=2)
- [공과대학 전자공학전공 일반공지](https://ee.sogang.ac.kr/kor/community/notice02.php)
- [공과대학 전자공학전공 학사공지](https://ee.sogang.ac.kr/kor/community/notice03.php)
- [공과대학 컴퓨터공학전공 주요공지](https://scc.sogang.ac.kr/front/cmsboardlist.do?siteId=cs&bbsConfigFK=1905)
- [공과대학 컴퓨터공학전공 취업/인턴십공지](https://scc.sogang.ac.kr/front/cmsboardlist.do?siteId=cs&bbsConfigFK=1748)
- [경제대학 경제학전공 학부/일반대학원공지](https://econ.sogang.ac.kr/front/cmsboardlist.do?siteId=econ&bbsConfigFK=2607)
- [경영대학 경영학전공 학부공지](https://sbs.sogang.ac.kr/front/cmsboardlist.do?siteId=sbs&bbsConfigFK=2371)
- [서강대학교 일반대학원 공지](https://gradsch.sogang.ac.kr/gradsch/index_new.html)
- [슈퍼루키(채용 플랫폼) 인턴 채용공고](https://www.superookie.com/jobs?job_level%5B%5D=579f18168b129f673b4efebe)

---
![webcat](https://github.com/SEEWON/Webcat/assets/50395394/98ed98d7-1f79-4b89-906c-86c91b8b34fe)
