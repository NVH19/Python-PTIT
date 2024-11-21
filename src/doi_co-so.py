t = int(input())
s = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while t>0:
    n,k = map(int,input().split())
    res = ''
    while n>0:
        x = int(n%k)
        res = s[x] + res
        n = n//k
    print(res)
    t-=1