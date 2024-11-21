
a = [True] *  1000002
def sang():
    for i in range(2, 1000):
        if a[i]:
            for j in range(i*i, 1000002,i):
                a[j]=False
t = int(input())
while t>0:
    n = int(input())
    sang()
    cnt=0
    for i in range(5,n-6):
        if (a[i] and a[i+6]) and (a[i+2] or a[i+4]):
            cnt+=1
    print(cnt)
    t-=1