from collections import namedtuple
x = int(input())
fields = input().split()
t = 0
for i in range(x):
    students = namedtuple('student', fields)
    MARKS, ID, NAME, CLASS = input().split()
    student = students(MARKS, CLASS, ID, NAME) 
    t += int(student.MARKS)
print('{:.2f'.format(t / x))
