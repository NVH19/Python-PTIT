n,m = map(int,input().split())
a = [int(x) for x in input().split()]
d = {}
for i in range(1,m+1):
    d[i]=0
for i in a:
    if i not in d:
        d[i]=1
    else: d[i]+=1
max1,max2 = -1e9,-1e9
# print(d[4])
for i in range(1,m+1):
    if d[i]>max1:
        max1,max2 = d[i],max1
    elif d[i]>max2 and d[i]!=max1:
        max2 = d[i]
print(max1,max2)
if max1==max2 or max2==0 or max2 ==-1e9: print("NONE")
else:
    for i in range(1,m+1):
        if d[i]==max2:
            print(i)
            break