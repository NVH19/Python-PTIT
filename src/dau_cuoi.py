t = int(input())
while t>0:
    s = input()
    print('YES' if s[:2]==s[len(s)-2:] else 'NO')
    t-=1