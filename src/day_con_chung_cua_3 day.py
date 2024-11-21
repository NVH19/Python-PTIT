t = int(input())
while t>0:
    m,n,p = map(int,input().split())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    x,y,z = 0,0,0
    ok=1
    while x<m and y<n and z<p:
        if a[x]==b[y] and b[y]==c[z]:
            print(a[x],end=' ')
            ok=0
            x+=1
            y+=1
            z+=1
        elif a[x]<b[y]: x+=1
        elif b[y]<c[z]: y+=1
        elif c[z]<a[x]: z+=1
    if ok: print('NO', end=' ')
    print()
    t-=1