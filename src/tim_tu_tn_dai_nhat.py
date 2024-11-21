def thuannghic(s):
    if s==s[::-1]:
        return 1
    return 0
a = []
with open('VANBAN.in') as file:
    for i in file:
        a.append(i.split())
b = {}
maxx=0
for i in a:
    if(thuannghic(i) and len(i)>0):
        if(len(i)>maxx):
            maxx = len(i)
        if i in b:
            b[i]+=1
        else: b[i]=1
for i in b:
    if len(i)==maxx:
        print(i,end=' ')
        print(b[i])