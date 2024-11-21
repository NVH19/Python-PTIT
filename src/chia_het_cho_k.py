a,k,n = map(int,input().split())
ok=1
d=0
if a>=n:
    ok=0
else:
    m = a%k
    d = k-m
    if a+d>=n:
        ok=0
if ok==0:
    print(-1)
else:
    while a+d<=n:
        print(d,end=' ')
        d += k