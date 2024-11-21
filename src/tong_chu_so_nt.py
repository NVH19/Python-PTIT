import math
def nt(n):
    if n<2: return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return 0
    return 1
t = int(input())
while t>0:
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    print('YES' if nt(sum) else 'NO')
    t-=1