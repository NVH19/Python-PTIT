import math
t = int(input())
while t>0:
    n = int(input())
    s = input()
    convert = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    n = int(math.log(n) / math.log(2))
    while len(s)%n!=0:
        s = '0' + s
    for i in range(0,len(s),n):
        num = 0
        for j in range(i,i+n):
            if s[j]=='1':
                num += pow(2,n-j+i-1)
        print(convert[num], end="")
    print()
    t -= 1
