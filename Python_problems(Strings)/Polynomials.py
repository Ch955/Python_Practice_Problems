import numpy
x = list(map(float, input().split()))
y = int(input())
print(numpy.polyval(x,y))