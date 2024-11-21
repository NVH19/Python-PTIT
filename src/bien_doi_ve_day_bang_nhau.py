t = int(input())
a = [int(x) for x in input().split()]
step = 10**9
id = 0
for i in range(t):
    sum = 0
    for j in range(t):
        sum += abs(a[j]-a[i])
    if sum < step:
        step = sum
        id = a[i]
print(f'{step} {id}')