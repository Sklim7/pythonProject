'''
파일명: Ex13-4-readHello.py

open 함수모드
    r(read mode):읽기 전용 모드 / 파일 없으면 에러
$$
'''

with open('hello.txt', 'rt', encoding='UTF-8') as file:
    # str = file.read() #전체 읽기
    # = file.readline() #한줄씩 읽기
    #str += file.readline() #한줄씩 읽기
    #str += file.readline() #한줄씩 읽기
    #str += file.readline() #한줄씩 읽기



line_list = file.readlines()
print(line_list)
