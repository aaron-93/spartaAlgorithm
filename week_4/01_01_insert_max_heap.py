# 나의 코드1 - 오답

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value) -> object:
        self.items.append(value)
        for i in range(len(self.items)):
            print(self.items)
            try:
                if self.items[i//2] < self.items[i]:
                    self.items[i//2], self.items[i] = self.items[i], self.items[i//2]
                elif self.items[i*2+1] < self.items[i]:
                    self.items[i*2+1], self.items[i] = self.items[i], self.items[i*2+1]
                elif self.items[i*2] < self.items[i]:
                    self.items[i*2], self.items[i] = self.items[i],self.items[i*2]
            except:
                pass
        return MaxHeap

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!

# 분석 : value가 추가 된 이후 for문이 돌기 때문에 제일 마지막 9가 삽입된 이후 4,9,2,3으로 정렬은 되지만 그 이후로 정렬이 안됌

#나의 코드 - 수정본

class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value) -> object:
        self.items.append(value)
        for i in range(len(self.items),0,-1):
            print(self.items)
            try:
                if self.items[i//2] < self.items[i]:
                    self.items[i//2], self.items[i] = self.items[i], self.items[i//2]
                elif self.items[i*2+1] < self.items[i]:
                    self.items[i*2+1], self.items[i] = self.items[i], self.items[i*2+1]
                elif self.items[i*2] < self.items[i]:
                    self.items[i*2], self.items[i] = self.items[i],self.items[i*2]
            except:
                pass
        return MaxHeap

max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)

#힙의 구조상 아래에서 위로 올라가야하기 때문에 for문을 역순으로 실행


# 강의 코드
# class MaxHeap:
#     def __init__(self):
#         self.items = [None]
#
#     def insert(self, value) -> object:
#         self.items.append(value)
#         cur_index = len(self.items) -1
#         while cur_index > 1:
#             parent_index = cur_index //2
#             if self.items[cur_index] > self.items[parent_index]:
#                 self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
#                 cur_index = parent_index
#             else:
#                 break
#         return
#
# max_heap = MaxHeap()
# max_heap.insert(3)
# max_heap.insert(4)
# max_heap.insert(2)
# max_heap.insert(9)
# print(max_heap.items)