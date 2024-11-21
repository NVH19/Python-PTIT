t = int(input())
while t>0:
    string = input()
    m_in = 1e9
    res = 0
    a = []
    for i in string:
        if i.isdigit():
            res = res*10 + int(i)
        else:
            if res != 0:
                a.append(res)
            res = 0
    print(min(a))
    t-=1
    
        