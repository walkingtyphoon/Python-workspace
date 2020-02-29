from collections import deque

q = deque([1, 2, 3])
print(q)
q.append(6)
print("追加后的元素：", q)
q.appendleft(0)
print("追加后的元素：", q)