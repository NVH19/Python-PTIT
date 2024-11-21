def tong(n):
    n_re = n[::-1]
    return str(int(n)+int(n_re))
t = int(input())
while t>0:
    n = input()
    cnt=0
    ok=1
    while int(n)%7!=0:
        n = tong(n)
        cnt+=1
        if cnt==1000:
            ok=0
            break
    print(n if ok else -1)
    t-=1