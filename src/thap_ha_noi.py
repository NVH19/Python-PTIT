def thap_ha_noi(n,a,b,c):
    if n==1:
        print(f'{a} -> {b}')
        return
    thap_ha_noi(n-1,a,c,b)
    print(f'{a} -> {b}')
    thap_ha_noi(n-1,c,b,a)
n = int(input())
thap_ha_noi(n,'A','C','B')
