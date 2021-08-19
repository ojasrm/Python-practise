# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
n = int(input())
val = []

for _ in range(n):
    B = set(input().split())
    val.append(A.issuperset(B))

print(all(val))