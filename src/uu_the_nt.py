def nt(n):
    if n<2: return 0
    for i in range(2,n//2 + 1):
        if n%i==0: return 0
    return 1
t = int(input())
while t>0:
    s = input()
    l,r = 0,0
    a = [2,3,5,7]
    for i in s:
        if int(i) in a: l+=1
        else: r+=1
    print('YES' if nt(len(s)) and l>r else 'NO')
    t-=1