n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
k = int(input())
s,s1,s2 = 0,0,0
for i in range(n):
    for j in range(i+1,n):
        s += a[i][j]
for i in range(n):
    s1 += a[i][i]
    s2 += sum(a[i])
s3 = s2-s1-s
print("YES" if abs(s-s3)<=k else "NO")
print(abs(s-s3))
# 2 8 10 6 7
# 6 3 2 6 9
# 10 2 6 2 8
# 9 9 7 9 8
# 9 6 5 6 9