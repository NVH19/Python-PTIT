alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def Rotate(s):
    res = ""
    sum = 0
    for i in s:
        sum += ord(i)-ord('A')
    sum %= 26
    for i in range(len(s)):
        tmp = (sum + (ord(s[i])-ord('A'))) % 26
        res += alpha[tmp]
    return res
t = int(input())
while t>0:
    s = input()
    l = len(s)
    left = Rotate(s[:l//2])
    right = Rotate(s[l//2:])
    for i in range(len(left)):
        tmp = ord(left[i])-ord('A')
        idx = (tmp +(ord(right[i])-ord('A'))) % 26
        print(alpha[idx],end="")
    print()
    t-=1