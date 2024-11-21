class SDT:
    def __init__(self, name, sdt, ngay):
        self.name = name
        self.sdt = sdt
        self.ngay = ngay
        self.ten = name.split()[-1]
    def get(self):
        return f"{self.name}: {self.sdt} {self.ngay}"
src = open('SOTAY.txt','r')
s = src.read().split('\n')
a = []
while len(s)>0:
    day = s[0]
    s.pop()
    if day[:4]=='Ngay': ngay = day[5:]
    else:
        name = s[0]
        s.pop(0)
        sdt = s[0]
        s.pop(0)
        a.append(SDT(name,sdt,ngay))
a = sorted(a, key= lambda x:(x.ten,x.name))
src.close
file = open('DIENTHOAI.txt','w')
for i in a:
    file.write(i.get() + '\n')
file.close