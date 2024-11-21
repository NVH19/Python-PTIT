class sophuc:
    def __init__(self, thuc , ao) -> None:
        self.thuc = thuc
        self.ao = ao
    def tong(self,x):
        s1 = self.thuc + x.thuc
        s2 = self.ao + x.ao
        s = sophuc(s1,s2)
        return s
    def tich(self,x):
        s1 = self.thuc*x.thuc + self.ao*x.ao*(-1)
        s2 = self.thuc*x.ao + x.thuc * self.ao
        return sophuc(s1,s2)
    def __str__(self) -> str:
        if self.ao <0: tmp = '-'
        else: tmp = '+'
        return f'{self.thuc} {tmp} {abs(self.ao)}i'
t = int(input())
while t>0:
    t-=1
    a1,b1,a2,b2 = map(int,input().split())
    x = sophuc(a1,b1)
    y = sophuc(a2,b2)
    z = x.tong(y)
    print(z.tich(x), end=', ')
    m = z.tich(z)
    print(m)
