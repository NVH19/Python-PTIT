t = int(input())
while t>0:
    n = int(input())
    a,b = [],[]
    d = []
    res = 0
    c = [1] * n
    for i in range(n):
        d.append([float(x) for x in input().split()])
    for i in range(n):
        a.append(d[i][0])
        b.append(d[i][1])
    for i in range(n):
        for j in range(0,i):
            if a[i]>a[j] and b[i]<b[j]:
                c[i] = max(c[i],c[i]+1)
        res = max(res,c[i])
    print(res)
    t-=1