t = int(input())
while t>0:
    n = int(input())
    a = [int(x) for x in input().split()]
    l = min(a)
    r = max(a)
    print(r-l-len(set(a))+1)
    t-=1
