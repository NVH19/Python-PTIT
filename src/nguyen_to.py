import math
a = [1] * 100002
def sang():
    a[0]=a[1]=0
    for i in range(1002):
        if a[i]:
            for j in range(i*i,100002,i):
                a[j] = 0
t = int(input())
sang()
while t>0:
    n = int(input())
    cnt=0
    for i in range(1,n):
        if math.gcd(i,n)==1:
            cnt+=1
    print('YES' if a[cnt]==1 else 'NO')
    t-=1