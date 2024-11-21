class Tram:
    def __init__(self,id,name, thoigian, luongmua) -> None:
        self.name = name 
        self.id = id
        self.thoigian = thoigian
        self.luongmua = luongmua
    def __str__(self) -> str:
        return self.id + ' ' + self.name + ' ' + '%.2f'%(self.luongmua / (self.thoigian / 60))
def tinh(s):
    gio = int(s[:2])
    phut = int(s[3:])
    return 60*gio + phut
t = int(input())
a = []
idx = 1
d = {}
for i in range(t):
    id = 'T%02d'%(idx)
    name = input()
    s1 = tinh(input())
    s2 = tinh(input())
    thoigian = s2-s1
    luongmua = float(input())
    if name in d:
        d[name].thoigian += thoigian
        d[name].luongmua += luongmua
    else:
        d[name] = Tram(id,name,thoigian,luongmua)
        idx+=1
for i in d:
    print(d[i])

# Dong Anh
# 07:30
# 08:00
# 60
# Cau Giay
# 07:45
# 08:12
# 50
# Soc Son
# 08:00
# 09:15
# 78
# Dong Anh
# 18:50
# 20:00
# 88
# Cau Giay
# 19:01
# 20:00
# 77
# Soc Son
# 19:06
# 20:21
# 66
# Dong Anh
# 21:00
# 21:40
# 49
# Cau Giay
# 21:50
# 22:20
# 68
# Dong Anh
# 22:15
# 23:45
# 30
# Cau Giay
# 22:50
# 23:45
# 35