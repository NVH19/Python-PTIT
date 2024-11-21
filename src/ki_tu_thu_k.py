def result(n,k):
    tmp = 2**n/2
    if k==tmp: return chr(n+64)
    elif k<tmp: return result(n-1,k)
    return result(n-1,k-tmp)
t = int(input())
while t>0:
    n,k = map(int,input().split())
    print(result(n,k))
    t-=1