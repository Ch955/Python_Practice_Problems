x = input()
y = input().split()
print(all(int(i) > 0 for i in y) and any(y[x] == y[x][::-1] for x in range(len(y))))