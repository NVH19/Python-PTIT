t = int(input())
a = [0] * 93
a[0] = a[1] = 1
for i in range(2,93):
    a[i] = a[i-1] + a[i-2]
while t>0:
    l,r = map(int,input().split())
    for i in range(l,r+1):
        print(a[i-1], end = ' ')
    print()
    t-=1