'''
파일명: Ex02-5-list.py

리스트(List)
    -순서가 있는 데이터 집합
    -중복 허용, 수정 가능
    -다양한 자료형 포함 가능
'''


# 문자열 (len)
print('문자열 길이:', len('hello'))

# 1. 리스트 생성과 접근
pokemon_list = ['피카츄', '라이츄', '파이리']
print('리스트 전체:', pokemon_list)
print('첫번째 포켓몬:', pokemon_list[0])
print('리스트 길이:', len(pokemon_list)) # 리스트 몇개 있나 기능
print('첫번째 문자열 길이:', len(pokemon_list[0]))

# 2. 리스트 슬라이싱
fruit_list =['블루베리','바나나','사과','자몽', '체리', '망고']
print(fruit_list[2:4]) #0,1,2,3,4 맞고 사과부터 4에 하나 앞에꺼까지 즉 인덱스 3.
print(fruit_list[1:]) # 바나나 부터
print(fruit_list[-3:]) # 마지막 3개
print(fruit_list[::-1]) #역순
print(fruit_list[5:2:-1]) # 마지막 세번째 숫자는 스탭. index 5에서 -1 increment 씩 index 2까지
print(fruit_list[2:5:2]) #index 2에서 시작해서 step 2개씩 index 5에서 하나 전, 4까지.
print(fruit_list[:3])



# 3. 다양한 데이터 타입
string_list = ['A', 'B', 'C']
number_list = [1,2,3,4,5]
boolean_list = [True, False, True, False, False]
mixed_list = ['문자열', 100, True, 3.14] # 섞인 리스트

# 4. 리스트 수정.
pokemon_list = ['피카츄', '라이츄', '파이리']
pokemon_list[1] = '잠만보' # 단일 항목 수정. 라이츄를 잠만보를 바꾼거임.
print('수정된 리스트:', pokemon_list)

# 5. 범위 수정
evolution_list=['피카츄', '라이츄', '파이리', '리자드', '리자몽']
evolution_list[1:3] = ['메가 라이츄', '메가 파이리']
print('진화 업데이트', evolution_list)