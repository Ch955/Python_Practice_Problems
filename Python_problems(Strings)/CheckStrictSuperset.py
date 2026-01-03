s = input().split()
s = set(s)
x = int(input())
m = 0
l = []
for i in range(x):
    a = input().split()
    a = set(a)
    l.append(a.issubset(s))
    if (a.issubset(s)) == True:
        m+=1
if m == x:
    print("True")
else:
    print("False")    
print(all(l))