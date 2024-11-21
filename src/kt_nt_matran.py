def nt(n):
    if n<2: return 0
    for i in range(2,n//2 + 1): 
        if n%i==0: return 0
    return 1
n,m = map(int,input().split())
b = []
for i in range(n):
    a = list(map(int,input().split()))
    b.append(a)
for i in range(n):
    for j in range(len(b[i])):
        if nt(b[i][j]): b[i][j]=1
        else: b[i][j]=0
        print(b[i][j], end=' ')
    print()
