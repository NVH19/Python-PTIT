def nt(n):
    if n<2: return 0
    for i in range(2,n//2+1):
        if n%i==0:
            return 0
    return 1
n = int(input())
a = [int(x) for x in input().split()]
sum = 0
for i in a:
    x = i
    j1,j2 = 0,0
    while nt(x+j1)==0:
        j1+=1
    while nt(x-j2)==0:
        j2+=1
    sum = max(sum,min(j1,j2))
print(sum)
    