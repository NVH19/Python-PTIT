a = []
while 1:
    s1 = input()
    if s1[-1]!='.' and s1[-1]!='?' and s1[-1]!='!' : s1 += '.'
    a.append(s1)
    if s1[-1]=='!': break
for i in range(len(a)):
    res = ""
    a[i] = a[i].lower()
    a[i] = a[i].capitalize()
    x = list(a[i].split())
    for j in x:
        res += j
        res += " "
    res = res.strip()
    if res[-2]==" ": 
        res = res.replace(res[-2], "")
        print(res)
    else: print(res)
# for i in s:
#     if i!='.' and i!='?' and i!='!' and i!='\n':
#         tmp += i
#     else:
#         tmp.lower()
#         tmp.capitalize()
#         print(tmp)
#         tmp = ""