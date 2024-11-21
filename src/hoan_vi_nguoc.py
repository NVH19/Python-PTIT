from itertools import permutations
t = int(input())
while t>0:
    n = int(input())
    s = ''
    for i in range(n):
        s += str(i+1)
    a = permutations(s)
    b = []
    for i in a:
        res = ''
        for j in i:
            res += j 
        b.append(res)
    b = b[::-1]
    print(len(b))
    for i in b:
        print(i,end=' ')
    print()
    t -= 1