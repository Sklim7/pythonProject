''''
파일명: Ex20-4-O(nlogn).py

O(nlogN)
    선형 로드 시간 복잡도, 병합(머지)정렬 등의 알고리즘

'''

def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    mid = len(arr) //2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []

    i = j = 0

    while i<len(left) and j < len(right):

    if left[i] < right[j]:
        result.append(left[i])
        i += 1
    else:
        result.append(right[j])
        j += 1
    result += left[i:]
    result += right[j:]

    return results

# 실행코드
arr = [5, 2, 8, 6, 1, 9, 3, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)
