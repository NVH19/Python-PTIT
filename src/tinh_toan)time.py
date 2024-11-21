class Game:
    def __init__(self,id,name,gio,phut) -> None:
        self.id = id
        self.name = name
        self.gio = gio
        self.phut = phut
    def tmp(self):
        s = str(self.gio) + str(self.phut)
        return int(s)
    def __str__(self) -> str:
        return self.id + ' ' + self.name + ' ' + str(self.gio) + ' gio ' + str(self.phut) + ' phut'
def tinh(s):
    s1 = int(s[:2])
    s2 = int(s[3:])
    return s1*60+s2
t = int(input())
a = []
while t>0:
    t-=1 
    id = input()
    name = input()
    giovao = tinh(input().strip())
    giora = tinh(input().strip())
    sum = giora - giovao
    gio = sum // 60
    phut = sum % 60
    a.append(Game(id,name,gio,phut))
a.sort(key= lambda x:-x.tmp())
for i in a:
    print(i)
# 01T
# Nguyen Van An
# 09:00
# 10:30
# 06T
# Hoang Van Nam
# 15:30
# 18:00
# 02I
# Tran Hoa Binh
# 09:05
# 10:00