s = input()
if len(s)%2!=0:
    s = s[:len(s)-1]
# print(s)
a = []
for i in range(0,len(s)-1,2):
        tmp = s[i] + s[i+1]
        # print(tmp)
        a.append(int(tmp))
a = list(set(a))
a.sort()
for i in a: print(i,end=' ')

