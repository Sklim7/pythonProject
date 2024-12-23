'''
파일명: Ex20-1-O(1).py

빅 오 표기법(Big O notation)
    알고리즘의 시간 복잡도와 공간 복잡도를 분석할 떄 사용되는 표기법
    빅오 표기법을 최악의 경우 성능 표현

O(1)
    상수 시간 복잡도, 입력 크기와 상관없이 일정한 시간이 걸림
'''

def return_first_value(arr):
    return arr[0]

arr = [1,2,3,4,5,6,7,8,9]
print(return_first_value(arr))
