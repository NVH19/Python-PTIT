from itertools import permutations
s = input()
a = []
for i in range(len(s)): a.append(s[i])
b = permutations(a)
for i in b:
    for j in i: print(j,end='')
    print()