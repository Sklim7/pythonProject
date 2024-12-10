'''
파일명: Ex18-1-requests.py

requests library
    HTTP 요청을 보내기 위한 간편하고 인기있는 라이브러리
    이를 사용하여 웹페이지 데이터를 가져오거나,
    API와 상호 작용할 수 있다.

라이브러리 설치 방법
pip install requests

URL(uniform resource locator)
    인터넷에서 웹 페이지, 이미지, 동영상 등과 같은 리소스를 찾을 수 있는 주소.
    ex)https://n.news.naver.com:443/article/003/0012954121?ntype=RANKING

프로토콜(protocal)
    컴퓨터 네트워크를 통해 통신을 수행하기 워한 표준화된 규칙, 절차, 통신 프로세스를 의미
    ex)
    http/https - 웹서버 프로토콜
    ftp - 파일서버 프로토콜
    mailto - 메일서버 프로토콜
    telnet - 원격지 프로토콜

호스트(host)
    리소스가 위치한 서버의 이름
    ex) n.news.naver.com

포트(port)
    서버에서 사용하는 방번호
    ex) http - 80, https - 443

경로(path)
    웹서버에서 지원에 대한 경로(물리적 또는 추상적 경로)
    ex) /article/003/0012955421

쿼리(Query) - 추가로 서버에 보내는 데이터(parameter)
    ex) ntype=RANKING

'''

import requests

url = 'https://n.news.naver.com/article/057/0001859521' #?cds=news_media_pc&type=editn'
param = {
    'ntype':'RANKING'
}

response = requests.get(url, params=param)
print(response.text)

