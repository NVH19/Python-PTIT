t = int(input())
while t>0:
    s = input()
    res = ''
    for i in range(len(s)-1):
        if s[i].isalpha():
            res += s[i]
            if s[i+1].isdigit():
                for j in range(int(s[i+1])-1):
                    res += s[i]
    print(res)
    t-=1