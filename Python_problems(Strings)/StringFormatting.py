x = int(input())
width = len(bin(x)[2:])
for i in range(1,x+1):
    print(f" {str(i).rjust(width)} {oct(i)[2:].rjust(width)} {(hex(i)[2:]).upper().rjust(width)} {bin(i)[2:].rjust(width)}")