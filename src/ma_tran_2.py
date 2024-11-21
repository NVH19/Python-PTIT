n = int(input())
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
k = int(input())
s1,s2 = 0,0
for i in range(n):
    for j in range(n):
        if i+j<n-1:
            s1 += a[i][j]
        elif i+j>n-1: s2 += a[i][j]
print("YES" if abs(s1-s2)<=k else "NO")
print(abs(s1-s2))

