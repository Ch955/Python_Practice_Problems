from dateutil import parser
import re
from datetime import timedelta
a = int(input())
for i in range(a):
    t1 = input()
    t2 = input()
    t1 = parser.parse(t1)
    t2 = parser.parse(t2)
    res = abs(t1-t2)
    # out = str(int(res.total_seconds()))
    # if out[0] == '-':
    #     print(out[1:])
    # else:
    #     print(out)
    print(str(int(res.total_seconds())))
# res = str(res)
# l = res.split(',')
# hms = l[1].split(':')
# res = ((int(l[0][0])*24)*3600) + ((int(hms[0])*3600)+(int(hms[1])*60)+(int(hms[2])))
# print(res)
# print(res.split(','))
# parts = list(map(int, time_string.split(":")))
# duration = timedelta(days=parts[0], hours=parts[1], minutes=parts[2],seconds=parts[3])
# print(int(duration.total_seconds()))
