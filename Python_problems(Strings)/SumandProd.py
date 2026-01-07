import numpy
a, b = map(int, input().split())
mat = []
for i in range(a):
    c = list(map(int, input().split()))
    mat.append(c)
num = numpy.array(mat)
sum = numpy.sum(num, axis=0)
out = 1
for i in sum:
    out *= i
print(out)
