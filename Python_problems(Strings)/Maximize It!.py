from itertools import product
x, a = map(int,input().split())
l = []
for i in range(x):
    val = list(map(int,input().split()))
    l.append(val)
val = 0

for i in product(*l):
    val = max(val, sum(i)%a)
print(val)