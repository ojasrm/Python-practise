# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
lst = input().split()
if all(int(i) >= 0 for i in lst):
    if any(dig == dig[-1:] for dig in lst):
        print("True")
    else:
        print("False")
else:
    print("False")