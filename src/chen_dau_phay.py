s = input()
l = len(s)
res = ''
i = 1
while i<=l:
    res = s[l-i] + res
    if i%3==0 and i!=len(s):
        res = ',' + res
    i+=1
print(res)