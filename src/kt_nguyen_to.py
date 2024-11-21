import math
def nt(n):
    if n<2: return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return 0
    return 1
t = int(input())
while t>0:
    s = input()
    print('YES' if nt(int(s[-4:])) else 'NO')
    t-=1