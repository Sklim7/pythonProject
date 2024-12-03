'''
파일명: Ex07-2-for-range.py

for문과 range() 함수

range()
    연속된 숫자를 만들어 주는 함수
    예) range(1,10) => 1, 2, 3, 4, 5, 6, 7, 8, 9

'''


# range(stop)
factor = 2 # 구구단 2단
for n in range(1,10):
    print(f'{factor} X {n} = {factor * n}')
print()
# range(start, stop)
factor = 3 # 구구단 3단
for n in range(1,10): # range(1,10) 1 ~ 9
    print(f'{factor} X {n} = {factor * n}', end=" ")
print()

# range(start, stop, step)
factor = 4
for n in range(1, 10, 2): # 1부터 2씩 증가 < 10
    print(f'{dan} X {n} = {dan * n}', end=" ")
print()
