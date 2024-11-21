def check(s):
    if s!=s[::-1] or len(s)%2!=0: return 0
    for i in s:
        if int(i)%2!=0:
            return 0
    return 1
t = int(input())
while t>0:
    n = int(input())
    for i in range(n):
       if check(str(i)): print(i,end=' ')
    print()
    t-=1