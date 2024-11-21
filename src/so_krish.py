def gt(n):
    s = 1
    for i in range(1,n+1):
        s *= i
    return s
t = int(input())
while t>0:
    n = int(input())
    sum = 0
    ok=1
    for i in str(n):
        sum += gt(int(i))
        if sum==n:
            ok=0
            break
        elif sum>n:
            break
    print('Yes' if ok==0 else 'No')
    t-=1