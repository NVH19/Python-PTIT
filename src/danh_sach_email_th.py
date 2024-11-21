src = open('CONTACT.in')
s = src.read().split('\n')
a = []
for i in s:
    a.append(i.lower())
a = list(set(a))
a.sort()
for i in a:
    print(i)