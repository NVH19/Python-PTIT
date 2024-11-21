khuvuc = [1,2,3]
class ThiSinh:
    def __init__(self, ma, ten, diem, dan, khu):
        self.ma = ('TS'+ ma.zfill(2))
        self.ten = self.chuanhoa(ten)
        self.diem = diem
        self.dan = dan
        self.khu = khu

    def trangthai(self, tmp):
        self.tmp=tmp
    def chuanhoa(self, ten) -> str:
        return ' '.join(i.title() for i in ten.strip().split())
    
t = int(input())
a = []
for i in range(t):
    ma = str(i+1)
    ten = input()
    diem = float(input())
    dan = input()
    khu = int(input())
    a.append(ThiSinh(ma,ten,diem,dan,khu))
for i in a:
    tmp = ""
    if i.khu==1:
        i.diem += 1.5
    elif i.khu==2:
        i.diem += 1
    if i.dan!="Kinh": i.diem+=1.5
    if i.diem > 20.5: i.trangthai("Do")
    else:  i.trangthai("Truot")
a=sorted(a,key = lambda x : (x.ma))
a=sorted(a,key = lambda x : (x.diem),reverse=True)
for i in a:
    print(f'{i.ma} {i.ten} {"{:.1f}".format(i.diem)} {i.tmp}')
# 3
# Nguyen hong ngat
# 22.22
# Kinh
# 1
#     Chu thi MINh
# 14
# Dao
# 3
# nguyen van nam
# 20.72
# Dao
# 1