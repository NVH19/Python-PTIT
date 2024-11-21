t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    b = [0]*1000002
    for i in a:
        b[i] += 1
    for i in a:
        if b[i]%2!=0:
            print(i)
            b[i]=0
    t-=1