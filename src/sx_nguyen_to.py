def nt(n):
    if n<2: return 0
    for i in range(2,n//2 +1):
        if n%i==0: return 0
    return 1
n = int(input())
a = [int(x) for x in input().split()]
x = []
for i in a:
    if nt(i): x.append(i)
x.sort(reverse=True)
for i in range(n):
    if nt(a[i])==0: print(a[i],end=' ')
    else:
        print(x[-1],end=' ')
        x.pop()