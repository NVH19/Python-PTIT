n = int(input())
a = list(map(int,input().split()))
a.sort()
m1 = max(a[0]*a[1]*a[2],a[0]*a[1])
m2 = max(a[n-1]*a[n-2]*a[n-3], a[n-1]*a[n-2])
m3 = max(a[0]*a[1]*a[n-1],m2)
print(max(m1,m3))