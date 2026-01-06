from itertools import groupby
a = input()
for key, group in groupby(a):
    group_str = "".join(group)
    if key:
        print(f"({len(group_str)}, { key})", end=" ")