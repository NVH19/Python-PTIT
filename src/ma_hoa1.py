t = int(input())
while t>0:
    s = input()
    s += '@'
    res = ''
    i = 0
    while i<len(s)-1:
        cnt = 0
        while s[i]==s[i+1]:
            cnt+=1
            i+=1
        res += str(cnt+1)
        res += s[i]
        i+=1
    print(res)
    t-=1