n = int(input())
a = list(map(int,input().split()))
a.sort()
ok=1
for id,i in enumerate(a):
    if id!=i-1:
        print(id+1)
        ok=0
        break
if ok: print(n+1)