def check(s):
    cnt=0
    for i in range(len(s)-2):
        cnt+=1
        if s[i]!=s[i+2]:
            return 0
    return 1
t = int(input())
while t>0:
    s = input()
    print('YES' if check(s) else 'NO')
    t-=1