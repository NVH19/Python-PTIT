n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
res = 0
dic = dict()
for i in range(1,n+1):
    dic[str(i)] = a[i-1]-b[i-1]
dic = dict(sorted(dic.items(), key= lambda x:x[1]))
for x,y in dic.items():
    print(x,y)
    if k!=0:
        res += a[int(x)-1]
        k-=1
    else: res += b[int(x)-1]
print(res)
