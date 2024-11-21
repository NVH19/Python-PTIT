k = int(input())
while k>0:
    n,m = map(int,input().split())
    a = [int(x) for x in input().split()]
    tmp = max(a)
    res = []
    t,ok = 0,1
    am,duong = [],[]
    for id,i in enumerate(a):
        if i<0:
            am.append(i)
        else:
            if i==tmp and ok==1:
                duong.append(m)
                ok=0
            duong.append(i)
    for i in am: print(i, end=' ')
    for i in duong: print(i,end=' ')
    print()
    k-=1

