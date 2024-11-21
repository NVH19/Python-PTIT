import queue

t = int(input())
while t>0:
    q = queue.Queue()
    q.put('1')
    q.put('2')
    n = int(input())
    while n>0:
        tmp = q.get()
        
        if tmp.count('2') > len(tmp)//2:
            print(tmp, end=' ')
            n-=1
        q.put(tmp + '0')
        q.put(tmp + '1')
        q.put(tmp + '2')
    print()
    t-=1
