def br(a):
    for i in a:
        if i!=0: return 0
    return 1
def check(a):
    for i in range(len(a)-1):
        if a[i]!=a[i+1]: return 1
    return 0
while True:
    a = list(int(x) for x in input().split())
    cnt=0
    if br(a): break
    while check(a):
        tmp  = a[0]
        for i in range(len(a)-1):
            a[i] = abs(a[i] - a[i+1])
        a[3] = abs(a[3] - tmp)
        # print(a)
        cnt+=1
    print(cnt)
