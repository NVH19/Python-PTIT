import math
def nt(n):
    if n<2: return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
def tong(n):
    s = 0
    for i in str(n):
        s += int(i)
    return s
t = int(input())
while t>0:
    a,b = map(int,input().split())
    gc_d = math.gcd(a,b)
    print('YES' if nt(tong(gc_d)) else 'NO')
    t-=1