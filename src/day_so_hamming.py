def get_index(a,x):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m + 1
        elif a[m] > x:
            r = m - 1
        else:
            l = m + 1
    return 0
a = set()
def Try(x):
    a.add(x)
    if 2*x not in a and 2*x <10**18:
        Try(2*x)
    if 3*x not in a and 3*x < 10**18:
        Try(3*x)
    if 5*x not in a and 5*x < 10**18:
        Try(5*x)
Try(1)
s = sorted(a)
# for i in a: print(i, end=' ')
t = int(input())
while t>0:
    n = int(input())
    if n in a: 
        print(get_index(s,n))
    else: print('Not in sequence')
    t-=1