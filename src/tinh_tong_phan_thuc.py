t = int(input())
while t>0:
    c,l = 0,0
    n = int(input())
    for i in range(1,n+1):
        if i%2==0:
            c += float(1)/i
        else:
            l += float(1)/i
    print(f'{c:.6f}' if n%2==0 else f'{l:.6f}')
    t-=1
