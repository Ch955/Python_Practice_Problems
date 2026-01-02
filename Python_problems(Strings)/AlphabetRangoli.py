import string
size = int(input())
l = []
for i in range(2 * size - 1):
    if i < size:
        l.append(string.ascii_lowercase[(size-1) - i])
        a = '-'.join(l)
        r = a[::-1]
        print((a + r[1:]).center(4 * size - 3, '-'))
    else:
        l.pop()
        a = '-'.join(l)
        r = a[::-1]
        print((a + r[1:]).center(4 * size - 3, '-'))