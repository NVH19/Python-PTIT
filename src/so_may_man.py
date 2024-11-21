s = input()
c_4, c_7 = 0,0
for i in s:
    if i=='4':
         c_4+=1
    elif i=='7':
         c_7+=1
print('YES' if (c_4+c_7==4 or c_4+c_7==7) else 'NO')