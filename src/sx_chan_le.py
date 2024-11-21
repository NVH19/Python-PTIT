n = int(input())
a = []
while True:
    a += list(map(int,input().split()))
    if len(a)==n: break
c,l,idx = [],[],[0]*n
for i in range(n):
    if a[i] % 2 == 1 :
        c.append(a[i])
        idx[i] = 1
    else : l.append(a[i])
c.sort()
l.sort(reverse=True)
for i in range(n):
    if idx[i] == 1 :
        print(c[-1], end = " ")
        c.pop()
    else :
        print(l[-1], end = " ")
        l.pop()