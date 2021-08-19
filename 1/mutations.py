n = int(input())
A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    comm, ne = input().split()
    B = set(map(int, input().split()))
    if comm == 'intersection_update':
        A.intersection_update(B)
    elif comm == 'update':
        A.update(B)
    elif comm == 'difference_update':
        A.difference_update(B)
    elif comm == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
    
print(sum(A))