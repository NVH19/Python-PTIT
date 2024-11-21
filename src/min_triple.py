t = int(input())
while t>0:
    n = int(input())
    a = list(map(int,input().split()))
    min_1,min_2,min_3 = 1e9,1e9,1e9
    for num in a:
        if num<min_1:
            min_3 = min_2
            min_2 = min_1
            min_1 = num
        elif num<min_2:
            min_3 = min_2
            min_2 = num
        elif num<min_3:
            min_3 = num
    print(min_1 + min_2 + min_3)
    t-=1