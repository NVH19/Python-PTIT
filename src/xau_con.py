def giaithua(n):
    if n==1: return 1
    return n*giaithua(n-1)
t = int(input())
while t>0:
    n ,m =map(int,input().split())
    s = input()
    l = n - len(s)
    a = list(set(i for i in s))
    res = (26)*l*2*giaithua(len(s)) % m
    # print(f'{l} {a} {giaithua(len(a))}')
    print(res if res!=0 else 1)
    t-=1