import math
a = [1] * 1000002
def nt(n):
    if n<2:
        return 0
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0:
            return 0
    return 1
def check(n):
    s = 0
    for i in str(n):
        s += int(i)
    return nt(s)
def check1(n):
    n_re = int(str(n)[::-1])
    if nt(n)==0 or nt(n_re)==0:
        return 0
    for i in str(n):
        if nt(int(i))==0:
            return 0
    return 1
t = int(input())
while t>0:
    n = int(input())
    print('Yes' if check(n)==1 and check1(n)==1 else 'No')
    t -= 1