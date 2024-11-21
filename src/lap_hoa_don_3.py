class MatHang:
    def __init__(self,id,name,soluong,dongia,tienchietkhau) -> None:
        self.id = id 
        self.name = name
        self.soluong = soluong
        self.dongia = dongia
        self.tienchietkhau = tienchietkhau
    def tien(self):
        return self.dongia*self.soluong - self.tienchietkhau
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.soluong} {self.dongia} {self.tienchietkhau} {self.tien()}'
t = int(input())
a = []
while t>0:
    t-=1
    id = input()
    name = input()
    soluong = int(input())
    dongia = int(input())
    tienchietkhau = int(input())
    a.append(MatHang(id,name,dongia,soluong,tienchietkhau))
a.sort(key=lambda x : -x.tien())
for i in a:
    print(i)
# ML01
# May lanh SANYO
# 12
# 4000000
# 2400000
# ML02
# May lanh HITACHI
# 4
# 2550000000
# 0
# ML03
# May lanh NATIONAL
# 5
# 3000000
# 150000