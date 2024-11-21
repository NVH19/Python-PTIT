def check(s):
    for i in s:
        if i!='0' and i!='1' and i!='2':
            return 0
    return 1
t = int(input())
while t>0:
    s = input()
    print('YES' if check(s) else 'NO')
    t-=1