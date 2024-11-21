def check(a):
    for i in range(len(a)-1):
        if((a[i] + a[i+1]) %2==0):
            return 1
    return 0
n = int(input())
a = list(map(int,input().split()))
while check(a):
    i = 0
    b = []
    while i<len(a):
        if i < len(a)-1 and (a[i] + a[i+1]) % 2==0:
            i += 2
        else:
            b.append(a[i])
            i += 1
    a = b
print(len(a))