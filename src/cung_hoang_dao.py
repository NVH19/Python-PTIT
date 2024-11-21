
a = ['Ma Ket','Bao Binh','Song Ngu','Bach Duong','Kim Nguu','Song Tu','Cu Giai','Su Tu','Xu Nu','Thien Binh','Thien Yet','Nhan Ma']
b = [[1,20],[2,19],[3,21],[4,20],[5,21],[6,21],[7,23],[8,23],[9,23],[10,23],[11,23],[12,22]]
t = int(input())
while t>0:
    d,m = map(int,input().split())
    for i in b:
        if m==i[0] and m!=12:
            if d<= i[1]-1:
                print(a[m-1])
                break
            else:
                print(a[m])
                break
        elif i[0]==12:
            if d<= i[1]-1:
                print(a[m-1])
                break
            else:
                print(a[0])
                break
    t -= 1