t = int(input())
while t>0:
    d = {}
    n = int(input())
    a = list(int(x) for x in input().split())
    for i in a:
        if i in d: d[i]+=1
        else: d[i]=1
    s = 0
    b = list(set(a))
    for i in b:
        if d[i] > s: 
            s = d[i]
            tmp = i
        elif d[i]==s:
            tmp = min(tmp,i)
    print(tmp if s>n//2 else 'NO')
    # print(d)
    t-=1