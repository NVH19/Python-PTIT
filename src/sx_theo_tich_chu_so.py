import functools
def tich(n):
    s = 1
    for i in n:
        s *= int(i)
    return s
def cmp(a,b):
    if tich(a)==tich(b):
        if int(a) > int(b): return 1
        else: return -1
    elif tich(a)>tich(b): return 1
    return -1
t = int(input())
while t>0:
    n = int(input())
    a = list(input().split())
    a = sorted(a, key=functools.cmp_to_key(cmp))
    for i in a: print(i,end=' ')
    print()
    t-=1