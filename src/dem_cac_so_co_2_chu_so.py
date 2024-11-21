s = input()
m = {}
a = []
l = len(s)
if len(s)%2!=0:
    l = len(s)-1
# print(l)
for i in range(0,l-1,2):
    tmp = s[i:i+2]
    a.append(tmp)
    if tmp not in m:
        m[tmp] = 1
    else: m[tmp]+=1
# print(a)
for i in a:
    if m[i]>0:
        print(f'{i} {m[i]}')
        m[i]=0