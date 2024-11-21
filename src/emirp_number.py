a = [1] * 1000002
def sang():
    a[0]=a[1]=0
    for i in range(2,1002):
        if a[i]:
            for j in range(i*i,1000002,i):
                a[j]=0
sang()
t = int(input())
while t>0:
    res = []
    n = int(input())
    cnt = 0
    for i in range(2,n):
        i_re = int(str(i)[::-1])
        if a[i] and a[i_re] and i_re>i and i_re<n:
            print(i,i_re,end=' ')
    print()
    t -= 1
