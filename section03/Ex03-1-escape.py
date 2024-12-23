'''
파일명: Ex03-1-escape.py

이스케이프 문자(Escape Character)
    -특수 기능을 가진 제어 문자
    -백 슬래시(\)로 시작

    \t : 탭
    \b : 백스페이스
    \' : 작은 따옴표
    \" : 큰 따옴표
    \n : 개행(줄바꿈)
    \\:  백 슬래시
'''
from ftplib import error_temp

from wheel.cli.convert import egg_info_re

# 1. 이스케이프 문자 활용
pokemon_info = 'ID: \'피카츄\'\n타입: \'전기\'\tLevel: 25'
print (pokemon_info)

# 2. 경로 표시
file_path = 'C:\\Program Files\\Java\\Git'
print('폴더 경로:', file_path)

test = 'eth and ada'
print('test:', test)


print("Hello\bWorld")

s = "123\b4"
print(s)
