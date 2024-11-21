t = int(input())
a = []
for i in range(t):
    a.append(list(input()))
sum = 0
for i in range(t):
    cnt = a[i].count('C')
    sum += cnt*(cnt-1)//2
for j in range(t):
    tmp = 0
    for i in range(t):
        if a[i][j]=='C':
            tmp += 1
    sum += tmp*(tmp-1)//2
print(sum)
# CC..
# C..C
# .CC.
# .CC.