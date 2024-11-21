def reset(a,b,c):
    d = []
    for i in a:
        if i!=b and i!=c:
            d.append(i)
    return d
n = int(input())
a = list(map(float, input().split()))
a = reset(a,min(a),max(a))
sum = 0
for i in a: sum += i
print(f'{sum/len(a):.2f}')