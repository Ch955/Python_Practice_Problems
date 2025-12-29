n = input()
p,c = input().split(" ")
p = int(p)
n = n[:p-1]+c+n[p+1:]
print(n)