from itertools import product
x, a = map(int,input().split())
l = []
for i in range(x):
    val = list(map(int,input().split()))
    l.append(val)
val = 0
for i in l:
    max_value = max(i)
    # print(max_value)
    val+=(max_value)**2
output = val%a
print(output)
for i in product(*l):
    val = max(val, sum(i)%a)
print(val)