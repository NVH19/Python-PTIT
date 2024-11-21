s = ''
while True:
    try:
        tmp = input()
        s += tmp
        s += ' '
        # if tmp=='0': break
    except EOFError: break
a = []
res = ''
for i in s.lower().split():
    # print(i,end=' ')
    res += i
    res += ' '
    if i[len(i)-1]=='.' or i[len(i)-1]=='?' or i[len(i)-1]=='!':
        a.append(res[:len(res)-2].capitalize())
        res = ''
for i in range(len(a)):
    print(a[i])