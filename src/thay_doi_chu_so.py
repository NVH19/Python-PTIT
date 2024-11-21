t = int(input())
while t>0:
    n,m = map(int,input().split())
    s1 = input()
    if s1.count(" "):
        s1,s2 = s1.split()
    else:
        s2 = input()
    m_in = min(n,m)
    m_ax = max(n,m)
    s1_min = int(s1.replace(str(m_ax),str(m_in)))
    s2_min = int(s2.replace(str(m_ax),str(m_in)))

    s1_max = int(s1.replace(str(m_in),str(m_ax)))
    s2_max = int(s2.replace(str(m_in),str(m_ax)))

    print(s1_min+s2_min, s1_max+s2_max)
    t -= 1