a = []
b = [0] * 10002
def sang():
    for i in range(2,1002):
        if b[i]==0:
            for j in range(i*i,10002,i):
                b[j]=1
sang()
for i in range(2,10002):
    if b[i]==0: a.append(i)
x,n = map(int,input().split())
print(n, end=' ')
for i in range(x):
    n += a[i]
    print(n, end = ' ')
