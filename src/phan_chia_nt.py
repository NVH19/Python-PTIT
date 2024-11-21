def nt(n):
    if n<2: return 0
    for i in range(2, int(n/2)+1):
        if n%i==0: return 0
    return 1
n = int(input())
a = [int(x) for x in input().split()]
b = []
for i in a:
    if i not in b: b.append(i)
s = sum(b)
res = 0
ok = 1
for idx,i in enumerate(b):
    res += i
    if(nt(res) and nt(s-res)):
        print(idx)
        ok = 0
        break
if(ok): print("NOT FOUND")