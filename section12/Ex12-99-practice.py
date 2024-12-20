'''
파일명: Ex12-99-practice.py


'''

import random
import time

# 리스트 컴프리헨션(list comprehension)문법
pot = [n for n in range(1,46)] #creates a list from 1 to 45. same as code below.
#pot = []
#for n in range(1, 46):
    #pot.append(n)
jackpot = []

for n in range(1,7):
    random.shuffle(pot)

    pick = pot.pop()
    print(f'{n}번째 번호는 {pick} 입니다.')
    jackpot.append(pick)
    time.sleep(1)

jackpot.sort()
print(jackpot)

