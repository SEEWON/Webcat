import os
import requests
from dotenv import load_dotenv

load_dotenv()
myToken = os.environ.get("SLACK_API_TOKEN")


def post_message(channel, text):
    requests.post(
        "https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer " + myToken},
        json={
            "channel": channel,
            "blocks": [{"type": "section", "text": {"type": "mrkdwn", "text": text}}],
        },
    )


# 변화를 감지하면 Slack 메시지 전송
def notify_change_detected(channel, company, job_title, link):
    post_message(
        channel,
        f"\n{channel} 페이지에 새 인턴 공고가 올라왔어요!\n* {company}*\n{job_title}\n<{link}|바로가기>\n",
    )


# 봇 시작 시 Slack 알림
def notify_started(channel):
    post_message("zz-log-working", f"{channel} detector가 시작되었어요.")


# 봇 종료 시 Slack 알림
def notify_terminated(channel):
    post_message("zz-log-working", f"{channel} detector가 종료되었어요.")
