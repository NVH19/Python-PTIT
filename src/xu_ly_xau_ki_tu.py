s1 = set(input().lower().split())
s2 = set(input().lower().split())
giao = list(s1.union(s2))
hop = list(s1.intersection(s2))
# giao = []
# hop = s2
# for i in s1:
#     if i in s2:
#         giao.append(i)
#     else:
#         hop.append(i)
# giao = list(set(giao))
# hop = list(set(hop))
giao.sort()
hop.sort()
for i in giao: print(i, end=' ')
print()

for i in hop: print(i,end=' ')
