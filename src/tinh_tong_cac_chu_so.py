t = int(input())
while t>0:
    s = input()
    a = []
    res = 0
    for i in s:
        if i.isdigit(): res += int(i)
        else: a.append(i)
    a.sort()
    for i in a: print(i,end='')
    print(res)
    t-=1