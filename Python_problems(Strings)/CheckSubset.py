a = int(input())
l = []
for i in range(a):
    i = input()
    setA = input().split()
    setA = set(setA)
    j = input()
    setB = input().split()
    setB = set(setB)
    l.append(setA.issubset(setB))
for i in l:
    print(i)

