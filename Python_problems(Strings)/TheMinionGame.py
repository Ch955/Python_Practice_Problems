a = input()
n = len(a)
stuartScore = 0
kevinScore = 0
# for i in range(1,n+1):
#     for j in range(n-i+1):
#         # print(x[j:j+i])
#         if x[j:j+i][0] in 'aeiou':
#             kevinScore+=1
#         else:
#             stuartScore+=1
            
# if stuartScore > kevinScore:
#     print(f"Stuart {stuartScore}")
# elif kevinScore > stuartScore:
#     print(f"Kevin {kevinScore}")
# else:
#     print("Drawo")    #O(n)**2
    
#Approach 2
for i in range(n):
    if a[i] in 'aeiouAEIOU':
        kevinScore += n-i
    else:
        stuartScore += n-i
if stuartScore > kevinScore:
    print(f"Stuart {stuartScore}")
elif kevinScore > stuartScore:
    print(f"Kevin {kevinScore}")
else:
    print("Draw")   #Approach2(O(n))
#BANANA
