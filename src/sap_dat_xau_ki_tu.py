t = int(input())
for i in range(t):
    s1 = list(input())
    s2 = list(input())
    s1.sort()
    s2.sort()
    # print(s1,s2)
    print(f'Test {i+1}: ', end='')
    print("YES" if s1==s2 else "NO")