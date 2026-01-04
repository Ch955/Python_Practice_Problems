from collections import Counter

x = input()
a = input().split()
y = int(input())
shoesSizeAvailable = Counter(a)
output = 0
for _ in range(y):
    b = list(map(int, input().split()))
    for item,count in (shoesSizeAvailable.items()):
        if b[0] == int(item) and count >= 1:
            shoesSizeAvailable[item] -= 1
            output += b[1]
        
print(output)
print(shoesSizeAvailable)

# from collections import Counter 

# number_of_shoes = int(input())
# shoe_sizes = input().split()
# number_of_customers = int(input())

# shoe_stock = Counter(shoe_sizes)
# earned = 0
# for _ in range(number_of_customers):
#     shoe_size, price = map(int, input().split())
#     if shoe_stock[shoe_size]:
#         shoe_stock[shoe_size] -= 1
#         earned += price
    
# print(earned)