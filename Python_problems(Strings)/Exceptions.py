s = int(input())
for i in range(s):
    a, b = map(str, input().split())
    try:
        print(int(a)//int(b))
    except ZeroDivisionError as e:
        print("Error Code:",e)
    except ValueError as e:
        print("Error Code:",e)
        