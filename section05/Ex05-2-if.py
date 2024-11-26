'''
파일명: Ex05-2-if.py
'''

choices = ['가위', '바위', '보']

computer = random.choice(choices)

# 사용자 입력 받기
print('가위, 바위, 보 중 하나를 선택하세요!')
player = input()

# 승부 판정
if player == computer:
    print('비겼습니다!')
elif player == '가위':
    if computer == '보':