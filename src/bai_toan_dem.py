n = int(input())
cnt = 0
a = []
while True:
    if cnt==n: break
    tmp = [int(x) for x in input().split()]
    cnt += len(tmp)
    for i in tmp: a.append(i)
if a[-1]==n:
    print("Excellent!")
else:
    for i in range(1,max(a)+1):
        if i not in a:
            print(i)