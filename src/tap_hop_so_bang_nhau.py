m,n = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a1 = list(set(a))
b1 = list(set(b))
print("YES" if a1==b1 else "NO")