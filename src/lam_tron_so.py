t = int(input())
while t>0:
    s = input()
    ok = 19
    ans = ''
    for i in range(1,len(s)):
        ans = '0' + ans
        if ok==1:
            if int(s[-i])>3:
                ok=1
            else:
                ok=0
        else:
            if int(s[-i])>4:
                ok=1
            else:
                ok=0
    if ok==1:
        ans = str(int(s[0])+1) + ans
    else:
        ans = s[0] + ans
    print(ans)
    t-=1