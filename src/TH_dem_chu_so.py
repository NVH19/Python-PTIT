t = int(input())
while t>0:
    l,r = map(int,input().split())
    res = ''
    m = [0]*10
    for i in range(l,r+1):
        tmp = str(i)
        for j in tmp:
            m[int(j)] +=1

    for i in range(0,10):
        print(m[i],end=' ')
    print()
    t-=1