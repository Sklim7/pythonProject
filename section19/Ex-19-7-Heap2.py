'''
파일명: Ex-19-7-Heap2.py

힙(heap)
최대값 및 최소값 찾아내는 연산을 빠르게 하기위해 고민된
연산
'''

import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, item)

    def pop(self):
        return heapq.heappop(self.heap)

#실행코드
heap = MinHeap()
heap.push(3)
heap.push(1)
heap.push(4)
heap.push(2)

print('========MinHeap=======')
print(heap.pop())
print(heap.pop())
print(heap.pop())
print(heap.pop())