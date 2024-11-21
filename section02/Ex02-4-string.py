'''
파일명:Ex02-4-string.py
문자열(String, str)
    -문자들의 순서가 있는 나열
    -작은 따옴표(') 또는 큰 따옴표(")로 표현
    -문자열은 변경 불가능(immutable)
    '''

#1. 문자열 생성 방법
str1 = 'Hello python' #작은 따옴표
str2 = "Hello python" #큰 따옴표
# 여러줄 문자열 작은 따옴표
str3 = '''Hello
Python
'''
str4 = """Hello
Python
"""
print(str1)
print(str2)
print(str3)
print(str4)


# 2. 문자열 인덱싱
'''
     ㅣh ㅣe ㅣl ㅣl ㅣo ㅣ 
index  0  1   2  3   4
역순번호 -5  -4 -3 -2  -1
'''
str5 = 'hello'
print('1번째 문자:', str5[0])
print('마지막 문자:', str5[4])
print('-1번째 문자:', str5[-1])

# 3.문자열 인덱싱  #[]브라켓 앞에 숫자는 as is, 마지막은 하나전까지
str6 = 'Python Programming'
    #   012345678
print('처음부터 4글자:', str6[0:4])
print('처음부터 4글자:', str6[:4])
print('7번째문자부터:', str6[7:])
print('마지막 5글자:', str6[-5:])



#4.주요 문자열 메소드(함수)
str7 = '   P y t h o n   '
print('원본:', str7)
print('공백제거:', str7.strip()) # 앞부분 ','에 의해 생긴 공백 제외한 앞 공백 사라짐.
print('모두 대문자:', str7.upper())
print('모두 소문자:', str7.lower())
print('문자 교체:', str7.replace('P', 'J'))
print('문자 사이 공백 제거:', str7.replace(' ',''))

print('             가나다라'.strip())

