from itertools import combinations
a = int(input())
b = input().split()
k = int(input())
outp = combinations(b,k)
l = []
count = 0
for i in outp:
    l.append(i)
for i in l:
    if 'a' in i:
        count+=1
print(f"{count/len(l):.4f}")    
    