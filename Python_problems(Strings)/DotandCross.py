import numpy
x = int(input())
a = []
b = []
for i in range(x):
    c = list(map(int,input().split()))
    a.append(c)
for i in range(x):
    c = list(map(int,input().split()))
    b.append(c)
print(numpy.dot(a, b))