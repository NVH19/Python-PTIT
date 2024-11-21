t = int(input())
while t>0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ok=0
    for i in range(n):
        if a[i]>b[i]:
            print('NO')
            ok=1
            break
    if ok==0: print('YES')
    t-=1
