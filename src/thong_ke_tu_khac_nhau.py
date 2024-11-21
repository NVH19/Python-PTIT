from collections import Counter
t = int(input())
res = ''
while t>0:
    t-=1
    res += input().lower()
    res += ' '
a = ''
for i in res:
    if i==',' or i=='.' or i=='?' or i=='!' or i==':' or i==';' or i=='-' or i=='/':
        a += ' '
    else: a += i
a = a.split()
d = Counter(a)
d = sorted(d.items(), key=lambda x: (-x[1],x[0]))
for i in d:
    print(f'{i}')