import math
l1 = list(map(int, input().split(',')))
l2 = list(map(int, input().split(',')))
a = sorted(l1+l2)
for i in a:
    b = len(a)
    if b%2 == 1:
        c = b//2
        print(f"{a[c]:.5f}")
        break
    else:
        c = (b//2)
        print(f"{((a[c]+a[c-1])/2):.5f}")
        break
