
def check(s1,s2):
    for i in range(1,len(s1)):
        if abs(ord(s1[i])-ord(s1[i-1])) != abs(ord(s2[i])-ord(s2[i-1])):
            return 0
    return 1
t = int(input())
while t>0:
    s = input()
    s_re = s[::-1]
    print('YES' if check(s,s_re) else 'NO')
    t-=1