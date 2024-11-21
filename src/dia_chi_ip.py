t = int(input())
while t>0:
    s = input().split(".")
    ok = 1
    for i in s:
        if i.isdigit()==0 or int(i)<0 or int(i)>255 or len(s)!=4:
            ok=0
    print("YES" if ok else "NO")
    t-=1