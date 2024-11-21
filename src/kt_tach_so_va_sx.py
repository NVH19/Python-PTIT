t = int(input())
a = []
while t>0:
    s = input()
    res = ''
    for i in s:
        
        if i.isdigit():
            res += i
        else:
            if len(res)>0:
                a.append(int(res))
            res=''
    if len(res)>0: a.append(int(res))
    t-=1
a.sort()
for i in a:
    print(i)
        