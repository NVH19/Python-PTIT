s = input()
res = ''
while len(s)%3!=0: s = '0' + s
for i in range(0,len(s),3):
    x = s[i:i+3]
    res = res + str(int(x,2))
print(res)