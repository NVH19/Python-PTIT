def nt(n):
    if n<2: return 0
    for i in range(2,n//2 + 1):
        if n%i==0: return 0
    return 1
def check(s):
    for id,i in enumerate(s):
        if nt(int(i)):
            if nt(id)==0: return 0
        else:
            if nt(id): return 0
    return 1
t= int(input())
while t>0:
    s = input()
    print('YES' if check(s) else 'NO')
    # for id,i in enumerate(s):
    #     print(id, i)
    t-=1