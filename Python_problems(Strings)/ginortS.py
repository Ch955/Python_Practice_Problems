x = input()
lower = ""
upper = ""
even = ""
odd  =""
for i in x:
    if i.islower():
        lower+=i
    elif i.isdigit() and int(i)%2 == 0:
        even+=i
    elif i.isdigit() and int(i)%2 == 1:
        odd+=i
    else:
        upper+=i
lower = sorted(lower)
upper = sorted(upper)
even = sorted(even)
odd = sorted(odd)
print(f"{"".join(lower)}{"".join(upper)}{"".join(odd)}{"".join(even)}")
        