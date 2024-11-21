import math
n,k = map(int,input().split())
l = 10**(k-1)
r = 10**k 
cnt=0
for i in range(l,r):
    if math.gcd(n,i)==1:
        print(i,end = ' ')
        cnt+=1
    if cnt==10:
        print()
        cnt=0
