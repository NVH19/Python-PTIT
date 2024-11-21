t = int(input())
while t>0:
    s = input()
    chan,le = int(s[0]), int(s[1])
    for i in range(2,len(s)):
        if i%2==0:
            if s[i]!='0': chan *= int(s[i])
        else: le += int(s[i])
    print(chan, le)
    t-=1