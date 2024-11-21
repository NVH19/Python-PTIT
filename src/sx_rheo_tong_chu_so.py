import functools
def tong(n):
    sum = 0
    for i in n:
        sum += int(i)
    return sum
def cmp(a,b):
    if tong(a)==tong(b):
        if int(a) > int(b): return 1
        else: return -1
    elif tong(a)>tong(b): return 1
    return -1
t = int(input())
while t>0:
    n = int(input())
    a = list(input().split())
    a = sorted(a, key=functools.cmp_to_key(cmp))
    for i in a: print(i,end=' ')
    t-=1