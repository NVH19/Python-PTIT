while True:
    t = int(input())
    if t==0: break
    a = []
    while t>0:
        n = input()
        a.append(int(n))
        t-=1
    if min(a) != max(a):
        print(f'{min(a)} {max(a)}')
    else: print('BANG NHAU')
