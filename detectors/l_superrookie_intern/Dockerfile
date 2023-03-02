FROM python:3.8.10-slim
WORKDIR /l_superrookie_intern

# 컨테이너에 크롬 설치
RUN apt-get update \
  && apt-get install -y wget \
  && wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
  && apt-get install -y ./google-chrome-stable_current_amd64.deb

# Python dependency 설치
COPY requirements.txt requirements.txt
RUN pip3 install --use-deprecated=legacy-resolver -r requirements.txt

COPY . .
CMD [ "python3", "superrookie_intern.py"]