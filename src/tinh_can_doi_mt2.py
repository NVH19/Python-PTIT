n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
k = int(input())
s,res = 0,0
for i in range(n):
    for j in range(n):
        if i+j<n-1: s += a[i][j]
        elif i+j>n-1: res += a[i][j]
print("NO" if abs(s-res)>k else "YES")
print(abs(s-res))
# 2 8 10 6 7
# 6 3 2 6 9
# 10 2 6 2 8
# 9 9 7 9 8
# 9 6 5 6 9