t = int(input())
while t>0:
    n,m = map(int,input().split())
    a,b = [],[]
    sum = 0
    for i in range(n):
        a.append(list(map(int,input().split())))
    for i in range(3):
        b.append(list(map(int,input().split())))
    for i in range(2,n):
        for j in range(2,m):
            sum += a[i-2][j-2]*b[0][0]
            sum += a[i-2][j-1]*b[0][1]
            sum += a[i-2][j]*b[0][2]
            sum += a[i-1][j-2]*b[1][0]
            sum += a[i-1][j-1]*b[1][1]
            sum += a[i-1][j]*b[1][2]
            sum += a[i][j-2]*b[2][0]
            sum += a[i][j-1]*b[2][1]
            sum += a[i][j]*b[2][2]
    print(sum)
    t-=1
# 2 1 0 0
# 3 2 1 1
# 4 3 2 1
# 2 2 1 0
# -1 -1 -1
# -1 8 -1
# -1 -1 -1