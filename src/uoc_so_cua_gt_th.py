t = int(input())
while t>0:
    n,p = map(int,input().split())
    res = 0
    tmp = p
    while tmp < n:
        x = n//tmp
        res += x
        tmp *= p
    print(res)
    t-=1