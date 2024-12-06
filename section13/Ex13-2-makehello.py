'''
파일명: Ex13-2-makehello.py

open 함수 모드
    w(write mode): 쓰기 전용모드 / 파일이 없으면 생성
    t(text mode): 해당 파일의 데이터를 텍스트 파일로 인식하여 입출력


'''

with open('hello.txt', 'wt', encoding='UTF') as file:    #인코딩안하면 깨짐
    file.write('안녕하세요.')
    file.write('\n')
    file.write('반갑습니다.')
    file.write('\n')

print('hello.txt 파일이 생성 되었습니다.')