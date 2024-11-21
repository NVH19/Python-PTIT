m,n = map(int,input().split())
a = set(map(int,input().split()))
b = set(map(int,input().split()))
x = a.intersection(b)
y = a-b
z = b-a
x = sorted(list(x))
y = sorted(list(y))
z = sorted(list(z))
for i in x: print(i,end=' ')
print()
for i in y: print(i,end=' ')
print()
for i in z: print(i,end=' ')