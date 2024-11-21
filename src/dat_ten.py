from itertools import combinations
n,m = map(int,input().split())
a = [x for x in input().split()]
a = list(set(a))
a.sort()
s = combinations(a,m)
for i in s:
    for j in i:
        print(j,end=' ')
    print()