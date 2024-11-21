t = int(input())
while t>0:
    a = {}
    n = int(input())
    while n>0:
        m = int(input())
        if m in a:
            a[m] += 1
        else: a[m]=1
        n-=1
    s = 0
    for i in a:
        if a[i]>s:
            s = a[i]
            res = i
        elif a[i]==s:
            res = min(res,i)
    print(res)
    t-=1  
