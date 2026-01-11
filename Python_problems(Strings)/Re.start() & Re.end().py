import re
s = input()
k = input()
pattern = f"(?=({k}))"
matches = list(re.finditer(pattern, s))
if not matches:
    print("(-1, -1)")
else:
    for m in matches:
        print((m.start(), m.start()+len(k)-1))
    

