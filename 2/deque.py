from collections import deque
d = deque()
N = int(input())
for _ in range(N):
    task, *num = input().split()
    getattr(d, task)(*num)
    
print(*d)
    