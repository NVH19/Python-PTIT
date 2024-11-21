t = 0
a = []
while t!=10:
    n = list(map(int,input().split()))
    t += len(n)
    a = a + n
for i in range(len(a)): a[i] = a[i]%42
a = set(a)
print(len(a))