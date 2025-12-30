n = int(input())
m = int(input())

for i in range(n):
    if(i == n//2):
        print(f"{(m-7)//2*'-'}WELCOME{(m-7)//2*'-'}")
    elif(i <= n//2):
        middle=(2*i)+1
        corner=(m-(middle*3))//2
        print(f"{corner*'-'}{middle*'.|.'}{corner*'-'}")
    else:
        middle=(2*(n-i))-1
        corner = (m - (middle * 3)) // 2
        print(f"{corner * '-'}{middle * ".|."}{corner * '-'}")
        