def check(s):
    cnt = 0
    for i in s:
        if not i.isdigit():
            return 1
        cnt = cnt * 10 + int(i)
    if cnt <= 2147483647 and cnt >= -2147483647:
        return 0
    return 1
info = open('DATA.in','r')
res = []
for i in info:
    for j in i.split():
        if check(j)==1: res.append(j)
res.sort()
for i in res:
    print(i, end=" ")