s = input()
up,low = 0,0
for i in s:
    if i.isupper() :up+=1
    else : low+=1
# print(up,low)
if up>low: print(s.upper())
else: print(s.lower())
