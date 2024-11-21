s = input()
cnt = 0
while(True):
    if (len(s)==1): break
    sum = 0
    for i in s:
        sum += ord(i)-ord('0')
    s = str(sum)
    cnt+=1
print(cnt)