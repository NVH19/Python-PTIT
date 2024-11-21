t = int(input())
while t>0:
    s = input()
    ok=1
    for i in s:
        if i!='4' and i!='7':
            ok=0
            break
    print('YES' if ok else 'NO')
    t-=1