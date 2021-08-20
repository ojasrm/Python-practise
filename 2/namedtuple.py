from collections import namedtuple
N = int(input())
a = input()
total = 0
Student = namedtuple('Student', a)
for _ in range(N):
    student = Student(*input().split())
    total += int(student.MARKS)
print('{:.2f}'.format(total/N))