p = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'
while 1:
    n = input()
    if n=='0': break
    k,s = n.split()
    k = int(k)
    res=''
    for id,i in enumerate(s):
        res += p[(p.index(i)+k)%28]
    print(res[::-1])