t = int(input())
while t>0:
    s = input()
    sum=0
    for i in s:
        sum += int(i)
    print('YES' if str(sum)==(str(sum)[::-1]) and len(str(sum))>1 else 'NO')
    t-=1