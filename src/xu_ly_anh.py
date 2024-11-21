t = int(input())
while t>0:
    n,m,l = map(int,input().split())
    a = [[0] *(m+1)]*(n+1)
    for i in range(1,n+1):
        a[i] = [0] + list(map(int,input().split()))
    for i in range(1,n+1):
        for j in range(1,m+1):
            a[i][j] += a[i][j-1] + a[i-1][j] - a[i-1][j-1]
    for i in range(1,n+2-l):
        for j in range(1,m+2-l):
            tmp = int((a[i-1+l][j-1+l] -a[i-1][j-1+l] - a[i-1+l][j-1] + a[i-1][j-1])/(l*l)) 
            print(tmp, end = ' ')
        print()
    t-=1
# 4 4 3
# 2 1 0 0
# 3 2 1 1
# 4 5 2 1
# 2 2 9 0
# 3 3 3
# 1 2 3
# 4 5 6
# 7 8 9