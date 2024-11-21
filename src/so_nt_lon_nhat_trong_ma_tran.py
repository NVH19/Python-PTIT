def nt(n):
    if n<2: return 0
    for i in range(2, n+1 // 2):
        if n%i==0: return 0
    return 1
n,m = map(int,input().split())
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
max = 0
ok = 1
for i in range(n):
    for j in range(m):
        if nt(a[i][j]) and a[i][j]>max:
            max = a[i][j]
            ok = 0
if ok:
    print("NOT FOUND")
else:
    print(max)
    for i in range(n):
        for j in range(m):
            if a[i][j] == max:
                print(f"Vi tri [{i}][{j}]")
# 23 21 26 10
# 13 13 22 14
# 28 29 28 23
# 29 19 11 19
# 16 26 24 21
# 13 25 21 29