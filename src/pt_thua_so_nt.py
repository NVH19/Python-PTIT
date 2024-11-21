import math
def nt(n):
    if n<2: return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: 
            return 0
    return 1
t = int(input())
while t>0:
    n = int(input())
    res = '1 '
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            cnt=0
            while n%i==0:
                cnt += 1
                n /= i
            res = res + '* ' + str(i) + '^' + str(cnt)  + ' '
    if nt(n): 
        res = res + '* ' + str(int(n)) + '^' + '1'
    print(res)
    t-=1