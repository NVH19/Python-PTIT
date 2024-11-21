def nt(n):
    if n<2: return 0
    for i in range(2,n//2 +1):
        if n%i==0: return 0
    return 1
t = int(input())
while t>0:
    s = input()
    print('YES' if nt(int(s[:3])) and nt(int(s[-3:])) else 'NO')
    t-=1