from collections import Counter
n = int(input())
a = input().split()
c = Counter(a)
for i, j in c.items():
    if j == 1:
        print(i)


