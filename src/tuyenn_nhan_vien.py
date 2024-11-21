class NhanVien:
    def __init__(self, id,name, diem) -> None:
        self.id = id
        self.name = name
        self.diem = diem
    
    def cham(self):
        if self.diem<5: return 'TRUOT'
        if self.diem<8: return 'CAN NHAC'
        if self.diem<9.5: return 'DAT'
        return 'XUAT SAC'
    def __str__(self) -> str:
        return '{} {} {:.2f} {}'.format(self.id, self.name, self.diem,self.cham())
t = int(input())
a = []
for i in range(t):
    id = 'TS0{:02}'.format(i+1)
    name = input()
    lt = float(input())
    th = float(input())
    if lt>10:
        lt /=10
    if th>10:
        th /=10
    diem = (lt+th)/2
    a.append(NhanVien(id, name,diem))
a.sort(key=lambda x: -x.diem)
for i in a:
    print(i)