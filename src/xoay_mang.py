t = int(input())
while t>0:
    n,d = map(int,input().split())
    a = list(map(int,input().split()))
    b = a[d:]
    c = a[:d]
    for i in b: print(i, end=' ')
    for i in c: print(i, end=' ')
    print()
    t-=1