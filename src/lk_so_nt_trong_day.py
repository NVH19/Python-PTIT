import math
def nt(n):
    if n<2: return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0: return 0
    return 1
n = int(input())
a = list(map(int,input().split()))
b = {}
for i in a:
    if nt(i):
        if i in b: b[i]+=1
        else: b[i]=1
for i in b:
    print(i, b[i])