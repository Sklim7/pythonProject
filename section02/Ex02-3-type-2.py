'''
파일명: Ex02-3-type-2.py

컬렉션 타입:
    - 리스트(list): 여러 값을 순서대로 저장
    - 튜플(tuple): 리스트와 비슷하지만 수정 불가능 쓰는 이유: Tuples use less memory than lists + faster.
    - 딕셔너리(dict): 키와 값의 쌍으로 저장
    - 세트(set): 중복없이 저장
'''

# 1. 컬렉션 타입예제
pokemon_list = ['피카츄', '라이츄', '파이리']
pokemon_tuple = ('피카츄', '라이츄', '파이리')
pokemon_dict = {'name': '피카츄', '기술':'백만볼트'}
meal_dict = {'food': 'pizza', 'drink': 'orange juice', 'dessert':'ice_cream'}
pokemon_set = {'피카츄', '라이츄', '파이리'} #순서가 없음 print 할때 마다  output이 different

print('리스트:', pokemon_list)
print('튜플:', pokemon_tuple)
print('딕셔너리:', pokemon_dict)
print('세트:', pokemon_set)


print('리스트 첫번째 값 불러오기:', pokemon_list[0])
print('튜플 첫번째 값 불러오기:', pokemon_tuple[1])
print('딕셔너리 name 값 불러오기:', pokemon_dict['name'])
print('딕셔너리 음식 불러오기:', meal_dict['food'])
print('딕셔너리 디저트 값불러오기:', meal_dict['dessert'])
