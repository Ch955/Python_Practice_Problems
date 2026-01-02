import re
s = input()
print(''.join(word.capitalize() for word in re.split(r"(\s+)",s)))