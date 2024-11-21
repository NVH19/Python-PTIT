def tinh(s,n):
    if s=="Xe_con":
        if n=='5': return 10000
        else: return 15000
    elif s=="Xe_khach":
        if n=='29': return 50000
        else: return 70000
    return 20000
t = int(input())
d = dict()
while t>0:
    tmp = input().split()
    if tmp[3]=="IN":
        if tmp[4] in d:
            d[tmp[4]] += tinh(tmp[1], tmp[2])
        else:
            d[tmp[4]] = tinh(tmp[1], tmp[2])
    t-=1
for key in d:
    print(f'{key}: {d[key]}')