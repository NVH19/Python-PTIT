t = int(input())
a = []
while t>0:
    s = input()
    a.append(s)
    t -=1
a = set(a)
print(len(a))