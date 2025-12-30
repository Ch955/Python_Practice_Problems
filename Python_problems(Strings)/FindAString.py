a = input()
b = input()
l = len(b)
res = 0
for i in range(len(a)-2):
    if a[i: l+i] == b:
        res = res+1
print(res)