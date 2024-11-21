import math
import sys
t = int(input())
sum = 0
cnt = 0
for inp in sys.stdin:
    n = int(inp)
    cnt+=1
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            while n%i==0:
                sum += i
                n /= i
    if n>1: sum += n
    if cnt==t: break
print(int(sum))