'''
파일명: Ex02-2-variable-2.py

변수명 규칙:
    -영문, 한글, 숫자, _로 구성
    -특수문자 사용 불가
    -첫 글자는 숫자 불가
    -키워드(명령어) 사용불가

    주석 단축키 Crtl + /
    줄 복사 단축키 Crtl + d
    줄 삭제 단축키 Crtl + y
'''

# 1. 여러 변수에 다른 값 할당
x, y, z = "피카츄", "라이추", "파이리"
print('포켓몬 1:', x)
print('포켓몬 2:', y)
print('포켓몬 3:', z)

# 2. 여러 변수에 같은 값 할당
x = y = z = "꼬부기"
print('변경된 포켓몬:', x)
print('변경된 포켓몬:', y)
print('변경된 포켓몬:', z)

# 3. 잘못된 변수명 예시
'''
7myvar = 'Python1' #숫자로 시작
my-car = 'Python2' #특수문자 포함
my var = 'Python3' #There's a space in between

'''
my_var = 'Python4' #_가능