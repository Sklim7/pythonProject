'''
파일명: Ex04-6-conditions.py

조건 연산자(삼항 연산자)
    조건식 결과에 따라 참 또는 거짓의 결과를 반환한다.
    참 if 조건식 else 거짓

'''

a = 20
b = 100
result = (a - b) if (a >= b) else (b-a)
print(f'{a}과 {b}의 차이는 {result}입니다.')

#위에는 밑에있는걸 간결하게 쓴거임.
a = 20
b = 100

if a >= b:
    result = a - b
else:
    result = b - a

print(f'{a}과 {b}의 차이는 {result}입니다.')

