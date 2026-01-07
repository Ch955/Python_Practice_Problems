import numpy
a, b = map(int, input().split())
mat = []
for i in range(a):
    c = list(map(int, input().split()))
    mat.append(c)
num = numpy.array(mat)
min = numpy.min(num, axis=1)
print(max(min))