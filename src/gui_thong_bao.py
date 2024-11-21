t = int(input())
while t>0:
    t-=1
    s = input()
    res = s[:100]
    tmp1 = s.split()
    tmp2 = res.split()
    # print(len(res))
    if tmp2[-1]==tmp1[len(tmp2)-1]:
        print(res)
    else:
        # print(1)
        tmp = res[::-1]
        idx = tmp.find(' ')
        print(res[:len(res)-idx])
    

