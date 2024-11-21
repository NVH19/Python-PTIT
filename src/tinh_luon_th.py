class NV:
    def __init__ (self,ma,ten,luong,songay):
        self.ma = ma
        self.ten = ten
        self.luong = luong
        self.songay = songay
    def phongban(self,phong):
        self.phong = phong
def reset(s):
    loai = s[0]
    nam = int(s[1:3])
    if loai=='A':
        if nam>=1 and nam<=3: return 10
        elif nam>=4 and nam<=8: return 12
        elif nam>=9 and nam<=15: return 14
        else: return 20
    elif loai=='B':
        if nam>=1 and nam<=3: return 10
        elif nam>=4 and nam<=8: return 11
        elif nam>=9 and nam<=15: return 13
        else: return 16
    elif loai=='C':
        if nam>=1 and nam<=3: return 9
        elif nam>=4 and nam<=8: return 10
        elif nam>=9 and nam<=15: return 12
        else: return 14
    else:
        if nam>=1 and nam<=3: return 8
        elif nam>=4 and nam<=8: return 9
        elif nam>=9 and nam<=15: return 11
        else: return 13
t1 = int(input())
zoom = []
NhanVien = []
while t1>0:
    zoom.append(input())
    t1-=1
t2 = int(input())
while t2>0:
    NhanVien.append(NV(input(),input(),int(input()),int(input())))
    t2-=1
for i in NhanVien:
    phong = i.ma[-2:]
    for j in zoom:
        if phong == j[:2]:
            i.phongban(j[3:])
    print(f'{i.ma} {i.ten} {i.phong} {i.luong*i.songay*reset(i.ma)*1000}')
    
