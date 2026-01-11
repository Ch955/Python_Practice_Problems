from collections import Counter
s = input()
count = Counter(s)
sorted = sorted(count.items(), key=lambda x:(-x[1], x[0]))
for i, j in sorted[:3]:
    print(i, j)
