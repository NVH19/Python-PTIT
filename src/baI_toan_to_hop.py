from itertools import combinations
n,k = map(int,input().split())
a = list(map(int,input().split()))
a = set(a)
a = list(a)
a.sort()
b = combinations(a,k)
for i in b:
    for j in i: print(j,end=' ')
    print()