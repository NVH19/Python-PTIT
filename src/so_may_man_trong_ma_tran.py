m,n = map(int,input().split())
a = []
for i in range(m):
    a.append(list(map(int,input().split())))
min,max = 1e9,-1e9
for i in range(m):
    for j in range(n):
        if a[i][j]>max:
            max = a[i][j]
        if a[i][j]<min:
            min = a[i][j]
smm = max-min
ok=1
for i in range(m):
    for j in range(n):
        if a[i][j] == smm: 
            ok=0
            break
if ok: print("NOT FOUND")
else:
    print(smm)
    for i in range(m):
        for j in range(n):
            if a[i][j] == smm:
                print(f"Vi tri [{i}][{j}]")