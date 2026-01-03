n=input()
k = int(input())
start = 0
end = k
if k==1:
    for i in n:
        print(i)
else:
    for i in range(k):
        subString = n[start:end]
        uni=""
        for ch in subString:
            if ch not in uni:
                uni+=ch
        print(uni)
        start+=k
        end+=k
            
    
# print(l)