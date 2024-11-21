def thaun_nghich(n):
    s = str(n)
    if s == s[::-1]:
        return 1
    return 0
def check(n):
    s = str(n)
    for i in s:
        if int(i)%2!=0:
            return 0
    return 1
t = int(input())
while t>0:
    n = int(input())
    for i in range(n):
        if thaun_nghich(i)==1 and check(i)==1 and len(str(i))%2==0:
            print(i,end=' ')
    print()
    t -= 1
    