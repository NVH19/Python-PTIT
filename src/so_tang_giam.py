def check(s):
    tmp=0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            return 0
        elif s[i]>s[i+1]:
            tmp = i
            break
    if tmp==0:
        return 0 
    else:
        for i in range(tmp,len(s)-1):
            if s[i]<s[i+1]:
                return 0
    return 1
t = int(input())
while t>0:
    s = input()
    print('YES' if check(s) else 'NO')
    t-=1