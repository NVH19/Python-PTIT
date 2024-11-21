t = int(input())
while t>0:
    s = input()
    sum = 0
    for i in s:
        sum += int(i)
    print('YES' if sum%3==0 else 'NO')
    t-=1