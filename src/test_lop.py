with open('e:/Python_codeptit/Python_codeptit/test.txt') as fi:
    s = fi.read()
a = list(s.split())
m = 0
for i in a:
    if len(i)>m: m = len(i)
for i in a:
    if len(i)==m: print(i)