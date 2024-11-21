import math
a, b = map(int,input().split())
u = math.gcd(a,b)
print(f'{a//u}/{b//u}')