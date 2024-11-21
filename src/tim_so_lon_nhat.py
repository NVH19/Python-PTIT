t = int(input())
while t > 0:
    string = input()
    res = 0
    result = -1e9
    for i in string:
        if i.isdigit():
            res = res*10 + int(i)
        else:
            res = 0
        result = max(result,res)
    print(result)
    t -= 1