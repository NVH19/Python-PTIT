t = int(input())
while t>0:
    t-=1
    n,m = map(int,input().split())
    a = []
    for i in range(n):
        a.append([int(x) for x in input().split()])
    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(m):
                sum += a[i][k]*a[j][k]
            print(sum,end=' ')
        print()
