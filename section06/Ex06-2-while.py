'''
파일명: Ex06-2-while.py

'''

my_list = []
n = int(input('정수를 입력하세요(종료는 0입니다).')) # 딱 한번만 실행 됨.
while n != 0:
    my_list.append(n)
    n = int(input('정수를 입력하세요(종료는 0입니다.)')) #0을 입력하기 전까지 계속 실행 됨

print(my_list)