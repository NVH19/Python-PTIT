def check(s):
    sum=0
    for i in s:
        sum += int(i)
    for i in range(len(s)-1):
        if abs(int(s[i])-int(s[i+1])) !=2:
            return 0
    if sum%10!=0: return 0
    return 1
t = int(input())
while t>0:
    s = input()
    print('YES' if check(s) else 'NO')
    t-=1