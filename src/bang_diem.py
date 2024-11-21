import math
class SinhVien:
    def __init__(self, id, name,tong):
        self.id = id
        self.name = name
        self.avg = round(tong /12 + 0.01,1)
    def diem(self):
        if self.avg >= 9: return 'XUAT SAC'
        if self.avg >=8 : return 'GIOI'
        if self.avg >=7 : return 'KHA'
        if self.avg >=5 : return 'TB'
        return 'YEU'
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.avg} {self.diem()}'
a = []
t = int(input())
for i in range(t):
    id = 'HS{:02}'.format(i+1)
    name = input()
    listdiem = [float(x) for x in input().split()]
    tong = sum(listdiem) + listdiem[0] + listdiem[1]
    a.append(SinhVien(id,name,tong))
a.sort(key=lambda x: (-x.avg, x.id))
for i in a:
    print(i)
