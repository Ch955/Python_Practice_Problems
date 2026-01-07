x = int(input())
a = int(input())
b = int(input())
print(pow((x),a))
if b>= 0:
    if a < 0:
        raise ValueError("Input cannot be less than 0")
    else:
        print(pow(x,a,b))