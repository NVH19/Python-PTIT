class GiaDinh:
    def __init__(self,id, name, csc,csm) -> None:
        self.id = id
        self.name = name
        self.csm = csm
        self.csc = csc
        self.tien() 
    def tien(self):
        cs = self.csm - self.csc
        if cs <= 50: self.tong = cs*100*1.02
        elif cs <=100: self.tong = 1.03*(50*100 + (cs-50)*150)
        elif cs >100: self.tong = 1.05*(50*100 + 50*150 + (cs-100)*200)
        self.tong = round(self.tong)
    def __str__(self) -> str:
        return f'{self.id} {self.name} {self.tong}'
t = int(input())
a = []
for i in range(t):
    id = 'KH{:02}'.format(i+1)
    name = input()
    csc = int(input())
    csm = int(input())
    a.append(GiaDinh(id, name, csc,csm))
a.sort(key=lambda x : -x.tong)
for i in a:
    print(i)