import math
a = [int(x) for x in input().split()]
y = math.lcm(a[1],a[3])
x = a[0]*(y//a[1]) + a[2]*(y//a[3])
print(f'{x//math.gcd(x,y)}/{y//math.gcd(x,y)}')