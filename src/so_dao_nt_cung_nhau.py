import math
t = int(input())
while t>0:
    n = input()
    print('YES' if math.gcd(int(n),int(n[::-1]))==1 else 'NO')
    t-=1