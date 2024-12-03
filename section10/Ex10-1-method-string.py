'''
파일명: Ex10-1-method-string.py

메서드(method)

    특정 객체가 가지고 있는 함수를 의미한다.
    객체 메서드() 사용가능


'''

# string 객체 format 메서드
print('10자리 폭 왼쪽 정렬 "{:<10d}"'.format(123))
print('10자리 폭 오른쪽  정렬 "{:>10d}"'.format(123))
print('10자리 폭 가운데 정렬 "{:^10d}"'.format(123))


print('10자리 폭 왼쪽 정렬 채움문자 "{:*<10d}"'.format(123))
print('10자리 폭 오른쪽  정렬 채움문자 "{:*>10d}"'.format(123))
print('10자리 폭 가운데 정렬 채움문자  "{:*^10d}"'.format(123))


# join 메서드 추가 예제
s = '-'.join('python')
print(s)
s = '+'.join(['a', 'b','c','d','e'])
print(s)


#split() 메서드 추가 예제
s = '010-1234-5678'
result = s.split('-')
print(result)
print(f'010-****-{result[2]}')







# replace 메서드
s = '    apple    '
result = s.replace(' ', '')
print(result)

s = 'Life is to short'
result = s.replace('short', 'long')
print(result)

# strip(), lstrip(), rstrip() 공백 제거 메서드

s = '    apple    '
result = s.strip()
print(result)

s = '    apple    '
result = s.lstrip()
print(result)

s = '    apple    '
result = s.rstrip()
print(result)



