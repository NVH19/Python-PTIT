def lai(n,x):
    return n+n*(x/100)
t = int(input())
while t>0:
    n,x,m = map(float, input().split())
    year = 0
    while n<m:
        n = lai(n,x)
        year += 1
    print(year)
    t-=1