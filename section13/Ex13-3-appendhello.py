'''
파일명: Ex13-3-appendhello.py

open 함수모듈
    a(append mode):추가 모드

'''

with open('hello.txt', 'at', encoding='UTF') as file:    #at
    file.write('Hello\n')
    file.write('Nice to meet you\n')
    

print('hello.txt 파일에 새로운 내용이 추가 되었습니다.')