'''
파일명:Ex12-5-random.py

random - 난수 생성 모듈

'''

import random

# 두 인자 사이 난수
print(random.randint(1,10))

# randrange - range 범위 난수 생성
print(random.randrange(10)) #0~9
print(random.randrange(1,10))#1~9
print(random.randrange(1,10,2))# 1~9 홀수만


# 0 이상 1 미만
print(random.random())

# 예시, 확률 50퍼
if random.random() < 0.5:
    print('s')
else:
    print("l")

#choice 함수 - 리스트에서 랜덤
seasons = ['spring', 'summer','fall','winter']
print(f'랜덤 계절은: {random.choice(seasons)}')

#shuffle 함수 - 임의로 섞는 함수
my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)

#4, 8, 14, 18, 44, 45]