# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()
A = input().split()
S1 = set()
S2 = set()
for i in A:
    if i not in S1:
        S1.add(i)
        S2.add(i)
    else:
        S2.discard(i)
print(S2.pop())
