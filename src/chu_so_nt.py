import math
def nt(n):
    if n<2: return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return 0
    return 1
def check(s):
    if nt(len(s))==0:
        return 0
    a,b = 0,0
    for i in s:
        if nt(int(i)): a+=1
        else: b+=1
    if b>=a: return 0
    return 1
t = int(input())
while t>0:
    s = input()
    print('YES' if check(s) else 'NO')
    t-=1