import math
t = int(input())
for i in range(t):
    n = int(input())
    x = 3 + math.sqrt(5)
    res = str(x**n)
    # print(res)
    print(f'Case #{i+1}:',end=" ")
    k = res.find('.')
    if k<3:
        s = res[:k]
        while len(s)<3:
            s = '0'+s
    else:
        s = res[k-3:k]
    print(s)