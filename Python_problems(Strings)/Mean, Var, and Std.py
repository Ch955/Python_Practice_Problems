import numpy
a, b = map(int, input().split())
mat = []
for i in range(a):
    c = list(map(int, input().split()))
    mat.append(c)
num = numpy.array(mat)
print(numpy.mean(num, axis=1))
print(numpy.var(num, axis=0))
print(numpy.std(num, axis=None),11)