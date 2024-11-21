def check(s):
    for i in range(len(s)-1):
        if int(s[i]) > int(s[i+1]):
            return 0
    return 1
t = int(input())
while t>0:
    s = input()
    print('YES' if check(s) else 'NO')
    t -= 1