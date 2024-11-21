def check(s):
    tmp = s[0]
    if s[0]==s[1] or len(s)%2==0: return 0
    for i in range(len(s)):
        if i%2==0:
            if s[i]!=tmp:
                return 0
    return 1
t = int(input())
while t>0:
    s = input()
    print('YES' if check(s) else 'NO')
    t-=1