n = int(input())
a = []
for i in range(n):
    a.append([int(x) for x in input().split()])
s = 0
for i in a:
    s += sum(i)
s /= 2
s_n = s/(n-1)
for i in range(n):
    res = 0
    for j in range(n):
        res += a[i][j]
    if n-2==0:
        print((1), end=" ")
    else:
        print(int((res-s_n)/(n-2)), end=" ")
    