n = int(input())
arr1 = set(map(int, input().split()))
m = int(input())
for _ in range(m):
    key, value = input().split()
    arr2 = set(map(int, input().split()))
    getattr(arr1, key)(arr2)
print(sum(arr1))
