def nt(n):
    if n<2: return 0
    for i in range(2,n//2):
        if n%i==0:
            return 0
    return 1
def check(s):
    sum = 0
    for i in s:
        sum += int(i)
    if nt(sum)==0:
        return 0
    for i in range(len(s)):
        if i%2==0:
            if int(s[i])%2!=0: return 0
        else:
            if int(s[i])%2==0: return 0
    return 1
t = int(input())
while t>0:
    s = input()
    print('YES' if check(s) else 'NO')
    t-=1