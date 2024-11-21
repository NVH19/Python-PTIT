n,m = map(int,input().split())
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
cnt = abs(n-m)
if n>m:
    for i in range(n):
        if cnt>0 and i%2==0:
            cnt-=1
            continue
        else:
            for j in range(m):
                print(a[i][j], end=' ')
        print()
elif m>n:
    for i in range(n):
        for j in range(m):
            if j % 2 == 1 and (j - 1) // 2 < cnt:
                continue
            else: print(a[i][j], end=' ')
        print()
else:
    for i in range(n):
        for j in range(m):
            print(a[i][j], end=' ')
        print()
