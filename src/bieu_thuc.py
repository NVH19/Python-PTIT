t = int(input())
while t>0:
    s = input()
    st = []
    cnt = 0
    for i in s:
        if i=='(':
            cnt+=1
            st.append(cnt)
            print(st[-1],end=' ')
        elif i==')':
            print(st[-1], end=' ')
            st.pop()
    print()
    t-=1
